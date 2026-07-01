from __future__ import annotations

import json
from pathlib import Path
from xml.dom import minidom
from xml.etree import ElementTree as ET


OUT_DIR = Path(__file__).resolve().parent
DRAWIO_PATH = OUT_DIR / "unet-medical-segmentation.drawio"
REGIONS_PATH = OUT_DIR / "regions.json"
NOTES_PATH = OUT_DIR / "trace-notes.md"

PAGE_W = 1774
PAGE_H = 887


def add_cell(root: ET.Element, cell_id: str, value: str = "", parent: str = "1", **attrs: str) -> ET.Element:
    cell = ET.SubElement(root, "mxCell", {"id": cell_id, "value": value, "parent": parent, **attrs})
    return cell


def vertex(
    root: ET.Element,
    cell_id: str,
    value: str,
    style: str,
    x: int,
    y: int,
    w: int,
    h: int,
    *,
    parent: str = "1",
    connectable: str | None = None,
) -> ET.Element:
    attrs = {"style": style, "vertex": "1"}
    if connectable is not None:
        attrs["connectable"] = connectable
    cell = add_cell(root, cell_id, value, parent, **attrs)
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"})
    return cell


def edge(
    root: ET.Element,
    cell_id: str,
    source: str,
    target: str,
    style: str,
    *,
    points: list[tuple[int, int]] | None = None,
    value: str = "",
) -> ET.Element:
    cell = add_cell(root, cell_id, value, "1", style=style, edge="1", source=source, target=target)
    geo = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    if points:
        arr = ET.SubElement(geo, "Array", {"as": "points"})
        for px, py in points:
            ET.SubElement(arr, "mxPoint", {"x": str(px), "y": str(py)})
    return cell


def port(root: ET.Element, cell_id: str, cx: int, cy: int) -> None:
    vertex(
        root,
        cell_id,
        "",
        "ellipse;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;opacity=0;",
        cx - 5,
        cy - 5,
        10,
        10,
    )


TEXT = "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Arial;fontColor=#1F2933;"
LABEL = TEXT + "fontSize=24;fontStyle=1;"
SMALL = TEXT + "fontSize=14;"
TINY = TEXT + "fontSize=12;"
BOUNDARY = "rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=none;strokeColor=none;"
TILE = "rounded=1;whiteSpace=wrap;html=1;arcSize=6;fillColor=#050607;strokeColor=#1F2933;strokeWidth=1.2;"
SCAN = "ellipse;whiteSpace=wrap;html=1;fillColor=#9AA1AA;strokeColor=#D7E1EA;strokeWidth=1.1;opacity=78;"
SCAN_DARK = "ellipse;whiteSpace=wrap;html=1;fillColor=#505761;strokeColor=#AEB7C0;strokeWidth=1;opacity=82;"
MASK = "ellipse;whiteSpace=wrap;html=1;fillColor=#7D63B8;strokeColor=#5E458E;strokeWidth=1;opacity=92;"
METRIC_PANEL = "rounded=1;whiteSpace=wrap;html=1;arcSize=6;fillColor=#FFFFFF;strokeColor=#6B7280;strokeWidth=1.4;dashed=1;dashPattern=6 5;"
PRIMARY = "edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#4D5E6E;strokeWidth=1.4;"
BLUE = "edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#0F4D92;strokeWidth=2;"
GREEN = "edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#1F7A3A;strokeWidth=2;"
SKIP = "edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#6B7280;strokeWidth=1.4;"
STACK_STROKE = "strokeWidth=1.8;whiteSpace=wrap;html=1;"


def feature_stack(
    root: ET.Element,
    prefix: str,
    x: int,
    y: int,
    w: int,
    h: int,
    count: int,
    fill: str,
    stroke: str,
    *,
    dx: int = 15,
    dy: int = -10,
) -> None:
    for i in range(count):
        px = x + i * dx
        py = y + (count - 1 - i) * dy
        shade = fill
        if i == 0:
            shade = "#DDEAF7" if fill == "#8DB7E8" else "#D9ECD9" if fill == "#95C99C" else "#DCD2F0"
        style = f"shape=parallelogram;perimeter=parallelogramPerimeter;direction=east;fillColor={shade};strokeColor={stroke};{STACK_STROKE}"
        vertex(root, f"{prefix}-slice-{i + 1}", "", style, px, py, w, h)


def add_scan_tile(root: ET.Element, prefix: str, x: int, y: int, w: int, h: int, *, overlay: bool = False) -> None:
    vertex(root, f"{prefix}-bg", "", TILE, x, y, w, h)
    vertex(root, f"{prefix}-outer", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#252A31;strokeColor=#C8CDD2;strokeWidth=1.2;opacity=92;", x + 20, y + 40, w - 40, h - 80)
    vertex(root, f"{prefix}-ring", "", "ellipse;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#D0D5DB;strokeWidth=1.1;opacity=85;", x + 35, y + 55, w - 70, h - 110)
    vertex(root, f"{prefix}-body", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#8B929B;strokeColor=#D7E1EA;strokeWidth=0.9;opacity=75;", x + 40, y + 60, w - 80, h - 120)
    vertex(root, f"{prefix}-organ-a", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#BFC5CB;strokeColor=#E2E8F0;strokeWidth=0.8;opacity=82;", x + 60, y + 70, 120, 80)
    vertex(root, f"{prefix}-organ-b", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#696F78;strokeColor=#CBD5E1;strokeWidth=0.8;opacity=78;", x + 155, y + 75, 60, 75)
    vertex(root, f"{prefix}-spine", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#E6E8EB;strokeColor=#98A2B3;strokeWidth=0.8;opacity=92;", x + 105, y + 155, 50, 35)
    vertex(root, f"{prefix}-lesion", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#727985;strokeColor=#AEB7C0;strokeWidth=0.8;opacity=82;", x + 120, y + 95, 30, 25)
    vertex(root, f"{prefix}-vessel-a", "", "shape=line;html=1;strokeColor=#D7E1EA;strokeWidth=1;endArrow=none;opacity=60;", x + 85, y + 115, 80, 1)
    vertex(root, f"{prefix}-vessel-b", "", "shape=line;html=1;strokeColor=#D7E1EA;strokeWidth=1;endArrow=none;opacity=55;rotation=18;", x + 95, y + 130, 60, 1)
    if overlay:
        vertex(root, f"{prefix}-mask-overlay-a", "", MASK + "opacity=68;", x + 45, y + 60, 170, 105)
        vertex(root, f"{prefix}-mask-overlay-b", "", MASK + "opacity=68;", x + 30, y + 90, 115, 90)


def add_mask_tile(root: ET.Element, prefix: str, x: int, y: int, w: int, h: int) -> None:
    vertex(root, f"{prefix}-bg", "", TILE, x, y, w, h)
    vertex(root, f"{prefix}-blob-a", "", MASK, x + 40, y + 60, 165, 90)
    vertex(root, f"{prefix}-blob-b", "", MASK, x + 40, y + 100, 105, 80)
    vertex(root, f"{prefix}-cut", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#050607;strokeColor=#050607;opacity=100;", x + 140, y + 125, 60, 40)


def add_metrics(root: ET.Element) -> None:
    vertex(root, "node-metrics-panel", "", METRIC_PANEL, 1370, 695, 390, 140)
    vertex(root, "node-metrics-label", "Metrics<br>(Dice / IoU)", SMALL, 1385, 805, 105, 25)
    # Bar glyph: boundary, axes, bars.
    vertex(root, "node-metrics-bar-axis-x", "", "shape=line;html=1;strokeColor=#4D5E6E;strokeWidth=1;endArrow=none;", 1410, 790, 80, 1)
    vertex(root, "node-metrics-bar-axis-y", "", "shape=line;html=1;strokeColor=#4D5E6E;strokeWidth=1;endArrow=none;rotation=-90;", 1410, 735, 1, 55)
    for i, height in enumerate((25, 40, 60, 75)):
        vertex(root, f"node-metrics-bar-{i + 1}", "", "rounded=0;whiteSpace=wrap;html=1;fillColor=#2F6DAA;strokeColor=#2F6DAA;", 1420 + i * 20, 790 - height, 12, height)
    # Donut-like Dice glyph.
    vertex(root, "node-metrics-dice-ring", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#8BCF8B;strokeColor=#2E7D4F;strokeWidth=1.4;", 1525, 735, 80, 80)
    vertex(root, "node-metrics-dice-hole", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#FFFFFF;strokeWidth=1;", 1545, 755, 40, 40)
    vertex(root, "node-metrics-dice-gap", "", "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#FFFFFF;", 1575, 730, 40, 35)
    # Small uncertainty/probability map.
    vertex(root, "node-metrics-map-frame", "", "rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#F7F9FC;strokeColor=#4C3279;strokeWidth=1.4;", 1660, 735, 75, 75)
    for i, (cx, cy) in enumerate(((1675, 750), (1710, 750), (1675, 790), (1710, 790))):
        vertex(root, f"node-metrics-map-dot-{i + 1}", "", "ellipse;whiteSpace=wrap;html=1;fillColor=#B8A6D9;strokeColor=#4C3279;strokeWidth=1.2;", cx, cy, 10, 10)
    for x in (1505, 1630):
        vertex(root, f"node-metrics-separator-{x}", "", "shape=line;html=1;strokeColor=#6B7280;strokeWidth=1;endArrow=none;rotation=-90;", x, 720, 1, 95)


def build_drawio() -> None:
    mxfile = ET.Element("mxfile", {"host": "app.diagrams.net", "agent": "Codex", "version": "24.7.17"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": "unet-medical-segmentation", "name": "U-Net medical segmentation"})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1774",
            "dy": "887",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(PAGE_W),
            "pageHeight": str(PAGE_H),
            "math": "1",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    # Labels.
    vertex(root, "label-input", "Input", LABEL, 95, 145, 130, 40)
    vertex(root, "label-encoder", "Encoder", LABEL + "fontColor=#0F4D92;", 345, 20, 400, 40)
    vertex(root, "label-decoder", "Decoder", LABEL + "fontColor=#1F7A3A;", 970, 20, 400, 40)
    vertex(root, "label-bottleneck", "Bottleneck", LABEL + "fontColor=#5E458E;", 700, 790, 190, 40)
    vertex(root, "label-mask", "Mask", LABEL, 1540, 80, 160, 40)
    vertex(root, "label-overlay", "Overlay", LABEL, 1525, 380, 180, 40)

    # Brackets above encoder and decoder.
    vertex(root, "brace-encoder-left", "", "shape=line;html=1;strokeColor=#0F4D92;strokeWidth=2;endArrow=none;", 350, 70, 390, 1)
    vertex(root, "brace-encoder-l", "", "shape=line;html=1;strokeColor=#0F4D92;strokeWidth=2;endArrow=none;rotation=90;", 350, 70, 1, 20)
    vertex(root, "brace-encoder-r", "", "shape=line;html=1;strokeColor=#0F4D92;strokeWidth=2;endArrow=none;rotation=90;", 740, 70, 1, 20)
    vertex(root, "brace-decoder-line", "", "shape=line;html=1;strokeColor=#1F7A3A;strokeWidth=2;endArrow=none;", 970, 70, 400, 1)
    vertex(root, "brace-decoder-l", "", "shape=line;html=1;strokeColor=#1F7A3A;strokeWidth=2;endArrow=none;rotation=90;", 970, 70, 1, 20)
    vertex(root, "brace-decoder-r", "", "shape=line;html=1;strokeColor=#1F7A3A;strokeWidth=2;endArrow=none;rotation=90;", 1370, 70, 1, 20)

    # Main visual entities.
    add_scan_tile(root, "node-input", 30, 190, 260, 275)
    feature_stack(root, "node-enc1", 365, 135, 80, 130, 5, "#8DB7E8", "#295F9D")
    feature_stack(root, "node-enc2", 405, 320, 70, 100, 4, "#AFCDF0", "#2F6DAA")
    feature_stack(root, "node-enc3", 465, 475, 65, 85, 4, "#C7DCF5", "#4D7FB6")
    feature_stack(root, "node-enc4", 555, 610, 55, 90, 4, "#D9E8FA", "#4D7FB6")
    feature_stack(root, "node-bottleneck", 715, 680, 60, 90, 5, "#B8A6D9", "#5E458E")
    feature_stack(root, "node-dec4", 920, 610, 60, 100, 5, "#BFDDBF", "#2E7D4F")
    feature_stack(root, "node-dec3", 1015, 505, 70, 105, 5, "#AED7B0", "#2E7D4F")
    feature_stack(root, "node-dec2", 1145, 330, 80, 125, 5, "#9FD09F", "#2E7D4F")
    feature_stack(root, "node-dec1", 1240, 125, 85, 145, 5, "#95C99C", "#2E7D4F")
    add_mask_tile(root, "node-mask", 1490, 115, 230, 225)
    add_scan_tile(root, "node-overlay", 1455, 420, 295, 250, overlay=True)
    add_metrics(root)

    # Invisible ports keep connectors on the same visual corridors as the raster reference.
    for pid, cx, cy in [
        ("port-input-out", 295, 200),
        ("port-enc1-in", 350, 200),
        ("port-enc1-down", 455, 275),
        ("port-enc2-up", 455, 285),
        ("port-enc2-down", 500, 430),
        ("port-enc3-up", 500, 435),
        ("port-enc3-down", 560, 565),
        ("port-enc4-up", 560, 575),
        ("port-enc4-out", 665, 700),
        ("port-bottleneck-in", 700, 720),
        ("port-bottleneck-out", 850, 720),
        ("port-dec4-in", 905, 720),
        ("port-dec4-up", 1045, 600),
        ("port-dec3-down", 1045, 630),
        ("port-dec3-up", 1135, 455),
        ("port-dec2-down", 1135, 470),
        ("port-dec2-up", 1245, 275),
        ("port-dec1-down", 1245, 285),
        ("port-dec1-out", 1395, 200),
        ("port-mask-in", 1485, 200),
        ("port-decoder-overlay", 1365, 520),
        ("port-overlay-in", 1450, 520),
        ("port-overlay-out", 1605, 675),
        ("port-metrics-in", 1605, 690),
        ("port-skip1-a", 520, 195),
        ("port-skip1-b", 1230, 195),
        ("port-skip2-a", 525, 365),
        ("port-skip2-b", 1135, 365),
        ("port-skip3-a", 590, 520),
        ("port-skip3-b", 1010, 520),
        ("port-skip4-a", 670, 575),
        ("port-skip4-b", 910, 575),
    ]:
        port(root, pid, cx, cy)

    # Main data-flow and scale-change edges.
    edge(root, "edge-input-enc1", "port-input-out", "port-enc1-in", PRIMARY)
    edge(root, "edge-enc1-enc2", "port-enc1-down", "port-enc2-up", BLUE)
    edge(root, "edge-enc2-enc3", "port-enc2-down", "port-enc3-up", BLUE)
    edge(root, "edge-enc3-enc4", "port-enc3-down", "port-enc4-up", BLUE)
    edge(root, "edge-enc4-bottleneck", "port-enc4-out", "port-bottleneck-in", BLUE)
    edge(root, "edge-bottleneck-dec4", "port-bottleneck-out", "port-dec4-in", GREEN)
    edge(root, "edge-dec4-dec3", "port-dec4-up", "port-dec3-down", GREEN)
    edge(root, "edge-dec3-dec2", "port-dec3-up", "port-dec2-down", GREEN)
    edge(root, "edge-dec2-dec1", "port-dec2-up", "port-dec1-down", GREEN)
    edge(root, "edge-dec1-mask", "port-dec1-out", "port-mask-in", PRIMARY)
    edge(root, "edge-decoder-overlay", "port-decoder-overlay", "port-overlay-in", PRIMARY)
    edge(root, "edge-overlay-metrics", "port-overlay-out", "port-metrics-in", PRIMARY)

    # Long skip connections, routed through open horizontal corridors.
    edge(root, "edge-skip1", "port-skip1-a", "port-skip1-b", SKIP)
    edge(root, "edge-skip2", "port-skip2-a", "port-skip2-b", SKIP)
    edge(root, "edge-skip3", "port-skip3-a", "port-skip3-b", SKIP)
    edge(root, "edge-skip4", "port-skip4-a", "port-skip4-b", SKIP)

    xml = ET.tostring(mxfile, encoding="utf-8")
    pretty = minidom.parseString(xml).toprettyxml(indent="  ", encoding="utf-8")
    DRAWIO_PATH.write_bytes(pretty)


def write_regions() -> None:
    regions = [
        {"name": "Input medical image", "bbox": [30, 145, 260, 320]},
        {"name": "Encoder pathway", "bbox": [345, 65, 320, 650]},
        {"name": "Bottleneck", "bbox": [700, 660, 190, 160]},
        {"name": "Decoder pathway", "bbox": [900, 65, 480, 660]},
        {"name": "Skip connections", "bbox": [500, 170, 720, 500]},
        {"name": "Mask output", "bbox": [1490, 80, 230, 260]},
        {"name": "Overlay output", "bbox": [1455, 380, 295, 290]},
        {"name": "Metrics panel", "bbox": [1370, 695, 390, 140]},
    ]
    REGIONS_PATH.write_text(json.dumps(regions, indent=2), encoding="utf-8")


def write_notes() -> None:
    notes = """# U-Net Medical Image Segmentation Draw.io Trace Notes

## Working Contract

Scientific message: A U-Net encoder-decoder uses multiscale feature maps and skip connections to transform a medical image slice into a pixel-level segmentation mask and overlay.
Figure type: Method architecture / scientific schematic.
Audience/journal style: Restrained publication-style figure for biomedical imaging or AI-methods paper.
Final output: Editable diagrams.net/draw.io source plus SVG and PNG preview.
Reference image role: Raster concept for composition, hierarchy, U-shaped topology, and approximate region bboxes.
Draw.io trace role: Editable source rebuilt from primitives; no reference bitmap is embedded as the final diagram body.
Core entities: Medical image tile, encoder feature maps, bottleneck feature maps, decoder feature maps, skip connections, output mask, overlay, segmentation metrics.
Topology: Left-to-right input; downward encoder; bottleneck; upward decoder; lateral skip connections; output mask, overlay, metrics.
Labels/formulas: Editable short text labels only; no formulas used.
Style constraints: White background, low-saturation blue/green/purple palette, no shadows, no glossy gradients, no decorative texture.
QA risks: Medical image texture is simplified; exact raster text and CT texture are intentionally not copied; long skip routes can dominate strict edge-difference metrics.
Consistency loop: At least three export/compare/fix iterations are recorded below after local QA.
Complex asset policy: No network SVG assets were used. Medical slices and masks are abstract primitives because the diagram does not require a recognizable organ silhouette.

## Raster Layout Extraction

Reference image: reference-unet-medical-segmentation.png
Pixel size: 1774 x 887
Canvas target: 1774 x 887 draw.io page, near 1:1 mapping.

Major regions:

| Region | Reference bbox (px) | Draw.io bbox | Visual role |
|---|---:|---:|---|
| Input medical image | [30,145,260,320] | [30,145,260,320] | Grayscale imaging input |
| Encoder pathway | [345,65,320,650] | [345,65,320,650] | Downsampling feature maps |
| Bottleneck | [700,660,190,160] | [700,660,190,160] | Lowest-resolution representation |
| Decoder pathway | [900,65,480,660] | [900,65,480,660] | Upsampling feature maps |
| Skip connections | [500,170,720,500] | [500,170,720,500] | Feature reuse between matched scales |
| Mask output | [1490,80,230,260] | [1490,80,230,260] | Segmentation mask |
| Overlay output | [1455,380,295,290] | [1455,380,295,290] | Mask over imaging context |
| Metrics panel | [1370,695,390,140] | [1370,695,390,140] | Dice / IoU / uncertainty glyphs |

Repeated motifs:
- Feature-map stacks: 4 encoder levels, bottleneck, 4 decoder levels; 4-5 layered parallelograms per block.
- Skip connections: four long lateral routes from encoder scales to decoder scales.
- Output glyphs: black imaging tiles with purple mask signal; metric panel with bars, Dice-like ring, and probability map.

Trace fidelity decisions:
- Preserve: U-shaped topology, relative module locations, output panel placement, blue encoder, green decoder, purple mask/bottleneck signal.
- Simplify: CT texture, pseudo-3D depth, generated small text, shadow-like antialiasing, exact organ texture.
- Replace with editable text: all labels including Input, Encoder, Decoder, Bottleneck, Mask, Overlay, Metrics.

## Asset Notes

Source mode: Self-designed draw.io primitives.
Selected external assets: None.
License/attribution: Not applicable.
Fallbacks: Abstract medical slice built from black tile plus grayscale ellipses; mask/overlay from purple ellipses; metric glyphs from bars, donut-like ellipses, and dots.

## Consistency Loop

Iteration records are appended after export/compare/fix runs.
"""
    NOTES_PATH.write_text(notes, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_drawio()
    write_regions()
    write_notes()
    print(DRAWIO_PATH)
    print(REGIONS_PATH)
    print(NOTES_PATH)


if __name__ == "__main__":
    main()
