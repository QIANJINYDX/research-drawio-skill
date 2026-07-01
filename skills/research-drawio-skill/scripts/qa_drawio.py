#!/usr/bin/env python3
"""Lightweight QA for uncompressed diagrams.net/draw.io files.

Checks XML validity, graph math flag, grid alignment, edge endpoints, and
obvious connector-through-node intersections. This is intentionally conservative:
it catches common layout mistakes but does not replace visual inspection in
diagrams.net.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


FORMULA_RE = re.compile(
    r"(\\\(|\\\[|\$\$|`[^`]+`|\\sqrt|sqrt\(|softmax|\\mathrm|\^[A-Za-z0-9{]|_[A-Za-z0-9{])"
)


@dataclass
class Box:
    cell_id: str
    x: float
    y: float
    w: float
    h: float
    value: str
    style: str

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    def expanded(self, pad: float) -> "Box":
        return Box(
            self.cell_id,
            self.x - pad,
            self.y - pad,
            self.w + 2 * pad,
            self.h + 2 * pad,
            self.value,
            self.style,
        )


def is_background_container(box: Box) -> bool:
    style = box.style
    return (
        box.w >= 220
        and box.h >= 140
        and "align=left" in style
        and "verticalAlign=top" in style
    )


def is_small_internal_glyph(box: Box) -> bool:
    return box.w <= 30 and box.h <= 30 and not box.value.strip()


def belongs_to_endpoint(box_id: str, source: str | None, target: str | None) -> bool:
    return any(endpoint and box_id.startswith(f"{endpoint}-") for endpoint in (source, target))


def is_text_label(box: Box) -> bool:
    return bool(box.value.strip()) and box.style.startswith("text;")


def is_glyph_primitive(box: Box) -> bool:
    if box.value.strip():
        return False
    if is_background_container(box):
        return False
    style = box.style
    return any(
        token in style
        for token in (
            "ellipse",
            "rounded=0",
            "fillColor=",
            "shape=",
        )
    )


def explicit_waypoints(edge: ET.Element) -> list[tuple[float, float]]:
    geo = edge.find("mxGeometry")
    if geo is None:
        return []
    arr = geo.find("Array[@as='points']")
    if arr is None:
        return []
    return [(attr_float(pt, "x"), attr_float(pt, "y")) for pt in arr.findall("mxPoint")]


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def collinear(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> bool:
    return (math.isclose(a[0], b[0]) and math.isclose(b[0], c[0])) or (
        math.isclose(a[1], b[1]) and math.isclose(b[1], c[1])
    )


def direct_route_is_clear(
    source: str | None,
    target: str | None,
    boxes: dict[str, Box],
    padding: float,
) -> bool:
    if source not in boxes or target not in boxes:
        return False
    a = (boxes[source].cx, boxes[source].cy)
    b = (boxes[target].cx, boxes[target].cy)
    if not (math.isclose(a[0], b[0]) or math.isclose(a[1], b[1])):
        return False
    for box in boxes.values():
        if box.cell_id in {source, target}:
            continue
        if belongs_to_endpoint(box.cell_id, source, target):
            continue
        if is_background_container(box):
            continue
        if segment_intersects_box(a, b, box.expanded(padding)):
            return False
    return True


def nearby_text_for_boxes(boxes: list[Box], candidates: list[Box], radius: float = 140) -> str:
    if not boxes:
        return ""
    cx = sum(box.cx for box in boxes) / len(boxes)
    cy = sum(box.cy for box in boxes) / len(boxes)
    nearby: list[str] = []
    for candidate in candidates:
        if distance((cx, cy), (candidate.cx, candidate.cy)) <= radius:
            nearby.append(candidate.value.lower())
    return " ".join(nearby)


def attr_float(node: ET.Element, name: str, default: float = 0.0) -> float:
    value = node.get(name)
    if value is None or value == "":
        return default
    return float(value)


def parse(path: Path) -> tuple[ET.Element, dict[str, Box], list[ET.Element]]:
    root = ET.parse(path).getroot()
    boxes: dict[str, Box] = {}
    edges: list[ET.Element] = []

    for cell in root.findall(".//mxCell"):
        if cell.get("vertex") == "1":
            geo = cell.find("mxGeometry")
            if geo is None:
                continue
            boxes[cell.get("id", "")] = Box(
                cell.get("id", ""),
                attr_float(geo, "x"),
                attr_float(geo, "y"),
                attr_float(geo, "width"),
                attr_float(geo, "height"),
                cell.get("value", ""),
                cell.get("style", ""),
            )
        elif cell.get("edge") == "1":
            edges.append(cell)

    return root, boxes, edges


def segment_intersects_box(
    p1: tuple[float, float], p2: tuple[float, float], box: Box
) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    left, right = box.x, box.x + box.w
    top, bottom = box.y, box.y + box.h

    if max(x1, x2) < left or min(x1, x2) > right:
        return False
    if max(y1, y2) < top or min(y1, y2) > bottom:
        return False

    if math.isclose(x1, x2):
        return left <= x1 <= right and max(min(y1, y2), top) <= min(max(y1, y2), bottom)
    if math.isclose(y1, y2):
        return top <= y1 <= bottom and max(min(x1, x2), left) <= min(max(x1, x2), right)

    # Non-orthogonal segment: sample a few points to catch obvious crossings.
    for i in range(1, 20):
        t = i / 20
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        if left <= x <= right and top <= y <= bottom:
            return True
    return False


def edge_points(edge: ET.Element, boxes: dict[str, Box]) -> list[tuple[float, float]]:
    source = edge.get("source")
    target = edge.get("target")
    points: list[tuple[float, float]] = []
    if source in boxes:
        points.append((boxes[source].cx, boxes[source].cy))

    geo = edge.find("mxGeometry")
    if geo is not None:
        arr = geo.find("Array[@as='points']")
        if arr is not None:
            for pt in arr.findall("mxPoint"):
                points.append((attr_float(pt, "x"), attr_float(pt, "y")))

    if target in boxes:
        points.append((boxes[target].cx, boxes[target].cy))
    return points


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("drawio", type=Path)
    parser.add_argument("--grid", type=int, default=10)
    parser.add_argument("--padding", type=float, default=4.0)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        root, boxes, edges = parse(args.drawio)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR XML parse failed: {exc}")
        return 2

    models = root.findall(".//mxGraphModel")
    if not models:
        errors.append("No mxGraphModel found")
    else:
        model = models[0]
        if any(FORMULA_RE.search(box.value) for box in boxes.values()) and model.get("math") != "1":
            errors.append('Formula-like labels found but mxGraphModel math!="1"')

    for box in boxes.values():
        if is_small_internal_glyph(box):
            continue
        for name, value in (("x", box.x), ("y", box.y), ("width", box.w), ("height", box.h)):
            if name in {"width", "height"} and value <= 30:
                continue
            if value and value % args.grid != 0:
                warnings.append(f"{box.cell_id} {name}={value:g} is off {args.grid}px grid")

    text_boxes = [box for box in boxes.values() if is_text_label(box)]
    glyph_boxes = [box for box in boxes.values() if is_glyph_primitive(box)]
    for text_box in text_boxes:
        for glyph_box in glyph_boxes:
            if text_box.cell_id == glyph_box.cell_id:
                continue
            if text_box.cell_id.startswith(glyph_box.cell_id) or glyph_box.cell_id.startswith(text_box.cell_id):
                continue
            if segment_intersects_box(
                (text_box.x, text_box.cy),
                (text_box.x + text_box.w, text_box.cy),
                glyph_box.expanded(args.padding),
            ) or segment_intersects_box(
                (text_box.cx, text_box.y),
                (text_box.cx, text_box.y + text_box.h),
                glyph_box.expanded(args.padding),
            ):
                warnings.append(
                    f"{text_box.cell_id} text overlaps or touches glyph primitive {glyph_box.cell_id}"
                )
                break

    bar_boxes = [box for box in glyph_boxes if "-bar-" in box.cell_id or box.cell_id.startswith("bar-")]
    if bar_boxes:
        text_context = nearby_text_for_boxes(bar_boxes, boxes.values())
        quantitative_terms = (
            "metric",
            "score",
            "accuracy",
            "auc",
            "loss",
            "expression",
            "abundance",
            "count",
            "rate",
            "performance",
            "comparison",
            "quant",
            "fold",
            "change",
        )
        if not any(term in text_context for term in quantitative_terms):
            warnings.append(
                "Bar-chart glyph detected without nearby quantitative meaning; use bars only for real metrics/comparisons"
            )

    for edge in edges:
        edge_id = edge.get("id", "<missing-id>")
        source = edge.get("source")
        target = edge.get("target")
        if source not in boxes:
            errors.append(f"{edge_id} missing or invalid source {source!r}")
        if target not in boxes:
            errors.append(f"{edge_id} missing or invalid target {target!r}")

        waypoints = explicit_waypoints(edge)
        if len(waypoints) > 3:
            warnings.append(
                f"{edge_id} has {len(waypoints)} explicit waypoints; simplify the route or document the obstacle"
            )
        if waypoints and direct_route_is_clear(source, target, boxes, args.padding):
            warnings.append(f"{edge_id} has waypoints but a direct aligned route appears clear")

        pts = edge_points(edge, boxes)
        if len(pts) < 2:
            continue
        for a, b in zip(pts, pts[1:]):
            if 0 < distance(a, b) < args.grid:
                warnings.append(f"{edge_id} contains a micro-jog shorter than {args.grid}px")
                break
        for a, b, c in zip(pts, pts[1:], pts[2:]):
            if collinear(a, b, c):
                warnings.append(f"{edge_id} contains a redundant collinear waypoint")
                break
        for a, b in zip(pts, pts[1:]):
            for box in boxes.values():
                if box.cell_id in {source, target}:
                    continue
                if belongs_to_endpoint(box.cell_id, source, target):
                    continue
                if is_background_container(box):
                    continue
                if segment_intersects_box(a, b, box.expanded(args.padding)):
                    warnings.append(
                        f"{edge_id} route may cross {box.cell_id}; add waypoints or move nodes"
                    )
                    break

    for msg in errors:
        print(f"ERROR {msg}")
    for msg in warnings:
        print(f"WARN {msg}")

    if errors:
        return 2
    print(
        f"OK XML parsed; vertices={len(boxes)} edges={len(edges)} "
        f"warnings={len(warnings)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
