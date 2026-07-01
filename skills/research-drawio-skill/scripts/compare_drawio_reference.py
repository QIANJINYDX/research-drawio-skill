#!/usr/bin/env python3
"""Compare a draw.io export against a raster reference image.

Use this after exporting a .drawio preview. For traced GPT/imagegen figures, the
script quantifies whether the editable redraw still matches the reference
composition closely enough to continue or deliver.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps


THRESHOLDS = {
    "exact": {
        "mae": 10.0,
        "rmse": 22.0,
        "ssim": 0.94,
        "foreground_iou": 0.90,
        "edge_iou": 0.65,
        "bbox_aspect_delta": 0.015,
        "content_area_delta": 0.08,
        "worst_tile_mae": 35.0,
    },
    "strict": {
        "mae": 28.0,
        "rmse": 55.0,
        "ssim": 0.78,
        "foreground_iou": 0.62,
        "edge_iou": 0.28,
        "bbox_aspect_delta": 0.08,
        "content_area_delta": 0.28,
        "worst_tile_mae": 85.0,
    },
    "semantic": {
        "mae": 45.0,
        "rmse": 78.0,
        "ssim": 0.60,
        "foreground_iou": 0.45,
        "edge_iou": 0.16,
        "bbox_aspect_delta": 0.16,
        "content_area_delta": 0.45,
        "worst_tile_mae": 120.0,
    },
}


def load_rgb(path: Path) -> Image.Image:
    image = Image.open(path)
    if image.mode in ("RGBA", "LA"):
        background = Image.new("RGBA", image.size, (255, 255, 255, 255))
        background.alpha_composite(image.convert("RGBA"))
        return background.convert("RGB")
    return image.convert("RGB")


def foreground_mask(image: Image.Image, threshold: int) -> np.ndarray:
    arr = np.asarray(image.convert("RGB"), dtype=np.int16)
    distance_from_white = np.max(np.abs(255 - arr), axis=2)
    return distance_from_white > threshold


def content_bbox(image: Image.Image, threshold: int, pad: int) -> tuple[int, int, int, int]:
    mask = foreground_mask(image, threshold)
    ys, xs = np.where(mask)
    if len(xs) == 0 or len(ys) == 0:
        return (0, 0, image.width, image.height)
    x0 = max(int(xs.min()) - pad, 0)
    y0 = max(int(ys.min()) - pad, 0)
    x1 = min(int(xs.max()) + 1 + pad, image.width)
    y1 = min(int(ys.max()) + 1 + pad, image.height)
    return (x0, y0, x1, y1)


def crop_content(image: Image.Image, bbox: tuple[int, int, int, int]) -> Image.Image:
    return image.crop(bbox)


def resize_like(image: Image.Image, target_size: tuple[int, int]) -> Image.Image:
    if image.size == target_size:
        return image
    return image.resize(target_size, Image.Resampling.LANCZOS)


def image_arrays(reference: Image.Image, candidate: Image.Image) -> tuple[np.ndarray, np.ndarray]:
    ref = np.asarray(reference.convert("RGB"), dtype=np.float32)
    cand = np.asarray(candidate.convert("RGB"), dtype=np.float32)
    return ref, cand


def ssim_score(reference: Image.Image, candidate: Image.Image) -> float:
    try:
        from skimage.metrics import structural_similarity
    except ImportError:
        return float("nan")
    ref = np.asarray(ImageOps.grayscale(reference), dtype=np.float32)
    cand = np.asarray(ImageOps.grayscale(candidate), dtype=np.float32)
    return float(structural_similarity(ref, cand, data_range=255))


def edge_mask(image: Image.Image, threshold: int) -> np.ndarray:
    try:
        import cv2
    except ImportError:
        gray = ImageOps.grayscale(image).filter(ImageFilter.FIND_EDGES)
        return np.asarray(gray) > threshold
    gray_arr = np.asarray(ImageOps.grayscale(image), dtype=np.uint8)
    return cv2.Canny(gray_arr, threshold, threshold * 2) > 0


def iou(a: np.ndarray, b: np.ndarray) -> float:
    union = np.logical_or(a, b).sum()
    if union == 0:
        return 1.0
    return float(np.logical_and(a, b).sum() / union)


def compute_metrics(
    reference: Image.Image,
    candidate: Image.Image,
    *,
    foreground_threshold: int,
    edge_threshold: int,
) -> dict[str, float]:
    ref, cand = image_arrays(reference, candidate)
    diff = ref - cand
    mae = float(np.mean(np.abs(diff)))
    rmse = float(math.sqrt(np.mean(np.square(diff))))
    ref_fg = foreground_mask(reference, foreground_threshold)
    cand_fg = foreground_mask(candidate, foreground_threshold)
    ref_edge = edge_mask(reference, edge_threshold)
    cand_edge = edge_mask(candidate, edge_threshold)
    return {
        "mae": mae,
        "rmse": rmse,
        "ssim": ssim_score(reference, candidate),
        "foreground_iou": iou(ref_fg, cand_fg),
        "edge_iou": iou(ref_edge, cand_edge),
    }


def bbox_metrics(
    reference_size: tuple[int, int],
    candidate_size: tuple[int, int],
    ref_bbox: tuple[int, int, int, int],
    cand_bbox: tuple[int, int, int, int],
) -> dict[str, float | list[int]]:
    ref_w = ref_bbox[2] - ref_bbox[0]
    ref_h = ref_bbox[3] - ref_bbox[1]
    cand_w = cand_bbox[2] - cand_bbox[0]
    cand_h = cand_bbox[3] - cand_bbox[1]
    ref_area = ref_w * ref_h
    cand_area = cand_w * cand_h
    return {
        "reference_size": list(reference_size),
        "candidate_size": list(candidate_size),
        "reference_content_bbox": list(ref_bbox),
        "candidate_content_bbox": list(cand_bbox),
        "reference_content_size": [ref_w, ref_h],
        "candidate_content_size": [cand_w, cand_h],
        "bbox_aspect_delta": abs((ref_w / max(ref_h, 1)) - (cand_w / max(cand_h, 1))),
        "content_area_delta": abs(ref_area - cand_area) / max(ref_area, 1),
        "canvas_width_delta": abs(reference_size[0] - candidate_size[0]) / max(reference_size[0], 1),
        "canvas_height_delta": abs(reference_size[1] - candidate_size[1]) / max(reference_size[1], 1),
    }


def parse_grid(value: str) -> tuple[int, int]:
    if "x" not in value:
        raise argparse.ArgumentTypeError("grid must be formatted like 12x6")
    cols, rows = value.lower().split("x", 1)
    return int(cols), int(rows)


def tile_report(
    reference: Image.Image,
    candidate: Image.Image,
    cols: int,
    rows: int,
    *,
    foreground_threshold: int,
    edge_threshold: int,
) -> list[dict[str, float | int]]:
    width, height = reference.size
    rows_out: list[dict[str, float | int]] = []
    for row in range(rows):
        for col in range(cols):
            x0 = round(col * width / cols)
            x1 = round((col + 1) * width / cols)
            y0 = round(row * height / rows)
            y1 = round((row + 1) * height / rows)
            ref_tile = reference.crop((x0, y0, x1, y1))
            cand_tile = candidate.crop((x0, y0, x1, y1))
            metrics = compute_metrics(
                ref_tile,
                cand_tile,
                foreground_threshold=foreground_threshold,
                edge_threshold=edge_threshold,
            )
            rows_out.append(
                {
                    "row": row,
                    "col": col,
                    "x0": x0,
                    "y0": y0,
                    "x1": x1,
                    "y1": y1,
                    **metrics,
                }
            )
    rows_out.sort(key=lambda item: float(item["mae"]), reverse=True)
    return rows_out


def load_regions(path: Path | None, *, ref_bbox: tuple[int, int, int, int], fmt: str) -> list[dict[str, object]]:
    if path is None:
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    regions = data.get("regions", data) if isinstance(data, dict) else data
    if not isinstance(regions, list):
        raise SystemExit("ERROR: regions JSON must be a list or an object with a 'regions' list")

    out: list[dict[str, object]] = []
    offset_x, offset_y = ref_bbox[0], ref_bbox[1]
    content_w = ref_bbox[2] - ref_bbox[0]
    content_h = ref_bbox[3] - ref_bbox[1]
    for index, region in enumerate(regions):
        if not isinstance(region, dict):
            raise SystemExit(f"ERROR: region {index} must be an object")
        name = str(region.get("name", f"region-{index + 1}"))
        bbox = region.get("bbox")
        if not (isinstance(bbox, list) and len(bbox) == 4):
            raise SystemExit(f"ERROR: region {name} must contain bbox: [x,y,w,h] or [x0,y0,x1,y1]")
        x0, y0, a, b = [float(value) for value in bbox]
        if fmt == "xywh":
            x1, y1 = x0 + a, y0 + b
        else:
            x1, y1 = a, b
        cx0 = max(round(x0 - offset_x), 0)
        cy0 = max(round(y0 - offset_y), 0)
        cx1 = min(round(x1 - offset_x), content_w)
        cy1 = min(round(y1 - offset_y), content_h)
        if cx1 <= cx0 or cy1 <= cy0:
            continue
        out.append({"name": name, "x0": cx0, "y0": cy0, "x1": cx1, "y1": cy1})
    return out


def region_report(
    reference: Image.Image,
    candidate: Image.Image,
    regions: list[dict[str, object]],
    *,
    foreground_threshold: int,
    edge_threshold: int,
) -> list[dict[str, float | int | str]]:
    rows_out: list[dict[str, float | int | str]] = []
    for region in regions:
        x0 = int(region["x0"])
        y0 = int(region["y0"])
        x1 = int(region["x1"])
        y1 = int(region["y1"])
        ref_tile = reference.crop((x0, y0, x1, y1))
        cand_tile = candidate.crop((x0, y0, x1, y1))
        metrics = compute_metrics(
            ref_tile,
            cand_tile,
            foreground_threshold=foreground_threshold,
            edge_threshold=edge_threshold,
        )
        rows_out.append({"name": str(region["name"]), "x0": x0, "y0": y0, "x1": x1, "y1": y1, **metrics})
    rows_out.sort(key=lambda item: float(item["mae"]), reverse=True)
    return rows_out


def save_diff_artifacts(
    reference: Image.Image,
    candidate: Image.Image,
    out_dir: Path,
    *,
    foreground_threshold: int,
    top_tiles: list[dict[str, float | int]],
) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    diff = ImageChops.difference(reference, candidate)
    diff_gray = ImageOps.grayscale(diff)
    diff_boost = ImageOps.autocontrast(diff_gray)
    heat = ImageOps.colorize(diff_boost, black="#FFFFFF", white="#C00000")
    heat_path = out_dir / "diff-heatmap.png"
    heat.save(heat_path)

    ref_mask = foreground_mask(reference, foreground_threshold)
    cand_mask = foreground_mask(candidate, foreground_threshold)
    overlay = np.full((reference.height, reference.width, 3), 255, dtype=np.uint8)
    overlap = np.logical_and(ref_mask, cand_mask)
    ref_only = np.logical_and(ref_mask, ~cand_mask)
    cand_only = np.logical_and(cand_mask, ~ref_mask)
    overlay[overlap] = (40, 40, 40)
    overlay[ref_only] = (220, 40, 40)
    overlay[cand_only] = (0, 150, 200)
    overlay_image = Image.fromarray(overlay, "RGB")
    draw = ImageDraw.Draw(overlay_image)
    for tile in top_tiles[:12]:
        draw.rectangle(
            [int(tile["x0"]), int(tile["y0"]), int(tile["x1"]), int(tile["y1"])],
            outline=(255, 170, 0),
            width=3,
        )
    overlay_path = out_dir / "foreground-overlay.png"
    overlay_image.save(overlay_path)

    side = Image.new("RGB", (reference.width * 2 + 24, reference.height), "white")
    side.paste(reference, (0, 0))
    side.paste(candidate, (reference.width + 24, 0))
    side_path = out_dir / "side-by-side.png"
    side.save(side_path)

    return {
        "diff_heatmap": str(heat_path),
        "foreground_overlay": str(overlay_path),
        "side_by_side": str(side_path),
    }


def pass_fail(metrics: dict[str, float], mode: str) -> tuple[bool, list[str]]:
    thresholds = THRESHOLDS[mode]
    failures = []
    for key in ("mae", "rmse", "bbox_aspect_delta", "content_area_delta", "worst_tile_mae"):
        if metrics[key] > thresholds[key]:
            failures.append(f"{key}={metrics[key]:.4g} > {thresholds[key]:.4g}")
    for key in ("ssim", "foreground_iou", "edge_iou"):
        value = metrics[key]
        if not math.isnan(value) and value < thresholds[key]:
            failures.append(f"{key}={value:.4g} < {thresholds[key]:.4g}")
    return not failures, failures


def maybe_export_candidate(candidate: Path, out_dir: Path) -> Path:
    if candidate.suffix.lower() != ".drawio":
        return candidate
    script_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(script_dir))
    import export_drawio_preview

    exe = export_drawio_preview.find_drawio_cli(None)
    preview = out_dir / f"{candidate.stem}.png"
    export_drawio_preview.run_export(exe, candidate.resolve(), preview.resolve(), "png", 90)
    return preview


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path, help="Reference PNG/JPG/WebP image")
    parser.add_argument("candidate", type=Path, help="Candidate PNG export or .drawio file")
    parser.add_argument("--out-dir", type=Path, help="Output report directory")
    parser.add_argument("--mode", choices=sorted(THRESHOLDS), default="strict")
    parser.add_argument("--grid", type=parse_grid, default=(12, 6), help="Tile grid, e.g. 12x6")
    parser.add_argument("--foreground-threshold", type=int, default=18)
    parser.add_argument("--edge-threshold", type=int, default=70)
    parser.add_argument("--content-pad", type=int, default=12)
    parser.add_argument("--regions-json", type=Path, help="Optional named regions in reference image coordinates")
    parser.add_argument("--regions-format", choices=["xywh", "xyxy"], default="xywh")
    parser.add_argument("--fail-on-threshold", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = (args.out_dir or Path("comparison-reports") / args.candidate.stem).resolve()
    candidate_path = maybe_export_candidate(args.candidate, out_dir)

    reference = load_rgb(args.reference)
    candidate = load_rgb(candidate_path)
    ref_bbox = content_bbox(reference, args.foreground_threshold, args.content_pad)
    cand_bbox = content_bbox(candidate, args.foreground_threshold, args.content_pad)
    ref_content = crop_content(reference, ref_bbox)
    cand_content = crop_content(candidate, cand_bbox)
    cand_norm = resize_like(cand_content, ref_content.size)

    metrics = bbox_metrics(reference.size, candidate.size, ref_bbox, cand_bbox)
    metrics.update(
        compute_metrics(
            ref_content,
            cand_norm,
            foreground_threshold=args.foreground_threshold,
            edge_threshold=args.edge_threshold,
        )
    )
    cols, rows = args.grid
    tiles = tile_report(
        ref_content,
        cand_norm,
        cols,
        rows,
        foreground_threshold=args.foreground_threshold,
        edge_threshold=args.edge_threshold,
    )
    metrics["worst_tile_mae"] = float(tiles[0]["mae"]) if tiles else 0.0
    regions = load_regions(args.regions_json, ref_bbox=ref_bbox, fmt=args.regions_format)
    region_rows = region_report(
        ref_content,
        cand_norm,
        regions,
        foreground_threshold=args.foreground_threshold,
        edge_threshold=args.edge_threshold,
    )
    if region_rows:
        metrics["worst_region"] = region_rows[0]
    passed, failures = pass_fail(metrics, args.mode)
    metrics["mode"] = args.mode
    metrics["pass"] = passed
    metrics["failures"] = failures
    metrics["reference"] = str(args.reference.resolve())
    metrics["candidate"] = str(candidate_path.resolve())

    out_dir.mkdir(parents=True, exist_ok=True)
    artifacts = save_diff_artifacts(
        ref_content,
        cand_norm,
        out_dir,
        foreground_threshold=args.foreground_threshold,
        top_tiles=tiles,
    )
    metrics["artifacts"] = artifacts

    report_path = out_dir / "comparison-report.json"
    report_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    tiles_path = out_dir / "tile-mismatches.csv"
    with tiles_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(tiles[0].keys()) if tiles else [])
        if tiles:
            writer.writeheader()
            writer.writerows(tiles)

    regions_path = None
    if region_rows:
        regions_path = out_dir / "region-mismatches.csv"
        with regions_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(region_rows[0].keys()))
            writer.writeheader()
            writer.writerows(region_rows)

    print(f"mode={args.mode} pass={passed}")
    print(f"reference={args.reference.resolve()}")
    print(f"candidate={candidate_path.resolve()}")
    for key in (
        "reference_size",
        "candidate_size",
        "reference_content_bbox",
        "candidate_content_bbox",
        "mae",
        "rmse",
        "ssim",
        "foreground_iou",
        "edge_iou",
        "bbox_aspect_delta",
        "content_area_delta",
        "worst_tile_mae",
    ):
        print(f"{key}={metrics[key]}")
    if failures:
        print("failures:")
        for failure in failures:
            print(f"- {failure}")
    print(f"report={report_path}")
    print(f"tiles={tiles_path}")
    if regions_path:
        print(f"regions={regions_path}")
        print(f"worst_region={region_rows[0]}")
    for name, path in artifacts.items():
        print(f"{name}={path}")
    if args.fail_on_threshold and not passed:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
