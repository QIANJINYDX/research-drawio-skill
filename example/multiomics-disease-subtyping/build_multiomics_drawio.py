from __future__ import annotations

import json
from datetime import datetime, timezone
from html import escape
from pathlib import Path


OUT_DIR = Path(__file__).resolve().parent
DRAWIO = OUT_DIR / "multiomics-disease-subtyping.drawio"
REGIONS = OUT_DIR / "regions.json"
TRACE_NOTES = OUT_DIR / "trace-notes.md"

W = 1720
H = 920

TEXT_COLOR = "#1F2933"
NEUTRAL = "#4D5E6E"
LIGHT = "#F7F9FC"
MODULE = "#EEF3F8"
BLUE = "#0F4D92"
BLUE_FILL = "#EAF2FB"
PURPLE = "#7A4EA3"
PURPLE_FILL = "#EFE7F5"
TEAL = "#148D89"
TEAL_FILL = "#E8F5F4"
ORANGE = "#F47C20"
ORANGE_FILL = "#FFF1E5"
GRAY = "#8D949A"
RED = "#B64342"
RED_FILL = "#F6D9D9"


cells: list[str] = []


def style(parts: dict[str, str | int | float | None]) -> str:
    return ";".join(f"{k}={v}" for k, v in parts.items() if v is not None) + ";"


TITLE = style(
    {
        "text": "",
        "html": 1,
        "strokeColor": "none",
        "fillColor": "none",
        "align": "center",
        "verticalAlign": "middle",
        "whiteSpace": "wrap",
        "rounded": 0,
        "fontFamily": "Arial",
        "fontSize": 22,
        "fontStyle": 1,
        "fontColor": TEXT_COLOR,
        "spacing": 4,
    }
)

LABEL = style(
    {
        "text": "",
        "html": 1,
        "strokeColor": "none",
        "fillColor": "none",
        "align": "center",
        "verticalAlign": "middle",
        "whiteSpace": "wrap",
        "rounded": 0,
        "fontFamily": "Arial",
        "fontSize": 15,
        "fontColor": TEXT_COLOR,
        "spacing": 3,
    }
)

SMALL_LABEL = LABEL.replace("fontSize=15", "fontSize=12")
TINY_LABEL = LABEL.replace("fontSize=15", "fontSize=10")

CONTAINER_BASE = {
    "rounded": 1,
    "whiteSpace": "wrap",
    "html": 1,
    "arcSize": 8,
    "fontColor": TEXT_COLOR,
    "fontFamily": "Arial",
    "fontSize": 12,
    "spacing": 8,
}

EDGE = {
    "edgeStyle": "orthogonalEdgeStyle",
    "endArrow": "block",
    "html": 1,
    "rounded": 0,
    "orthogonalLoop": 1,
    "jettySize": "auto",
    "strokeWidth": 1.4,
}


def add_vertex(cell_id: str, value: str, cell_style: str, x: float, y: float, w: float, h: float) -> None:
    cells.append(
        f'        <mxCell id="{cell_id}" value="{escape(value, quote=True)}" style="{cell_style}" vertex="1" parent="1">\n'
        f'          <mxGeometry x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" as="geometry"/>\n'
        f"        </mxCell>"
    )


def add_edge(cell_id: str, source: str, target: str, color: str = NEUTRAL, points: list[tuple[float, float]] | None = None) -> None:
    edge_style = style({**EDGE, "strokeColor": color})
    if points:
        pts = "\n".join(f'              <mxPoint x="{x:g}" y="{y:g}"/>' for x, y in points)
        geometry = (
            '          <mxGeometry relative="1" as="geometry">\n'
            '            <Array as="points">\n'
            f"{pts}\n"
            "            </Array>\n"
            "          </mxGeometry>\n"
        )
    else:
        geometry = '          <mxGeometry relative="1" as="geometry"/>\n'
    cells.append(
        f'        <mxCell id="{cell_id}" value="" style="{edge_style}" edge="1" parent="1" source="{source}" target="{target}">\n'
        f"{geometry}"
        "        </mxCell>"
    )


def add_text(cell_id: str, value: str, x: float, y: float, w: float, h: float, text_style: str = LABEL) -> None:
    add_vertex(cell_id, value, text_style, x, y, w, h)


def add_container(cell_id: str, x: float, y: float, w: float, h: float, stroke: str, fill: str = LIGHT, width: float = 1.4) -> None:
    add_vertex(
        cell_id,
        "",
        style({**CONTAINER_BASE, "fillColor": fill, "strokeColor": stroke, "strokeWidth": width}),
        x,
        y,
        w,
        h,
    )


def add_tinted_module(cell_id: str, x: float, y: float, w: float, h: float) -> None:
    add_vertex(
        cell_id,
        "",
        style(
            {
                **CONTAINER_BASE,
                "fillColor": MODULE,
                "strokeColor": "#D7E1EA",
                "strokeWidth": 1,
                "align": "left",
                "verticalAlign": "top",
            }
        ),
        x,
        y,
        w,
        h,
    )


def rect_style(fill: str, stroke: str = NEUTRAL, rounded: int = 0, width: float = 1) -> str:
    return style(
        {
            "rounded": rounded,
            "whiteSpace": "wrap",
            "html": 1,
            "fillColor": fill,
            "strokeColor": stroke,
            "strokeWidth": width,
        }
    )


def ellipse_style(fill: str, stroke: str = NEUTRAL, width: float = 1) -> str:
    return (
        "ellipse;whiteSpace=wrap;html=1;aspect=fixed;"
        f"fillColor={fill};strokeColor={stroke};strokeWidth={width};"
    )


def line_style(color: str = NEUTRAL, width: float = 1.2, arrow: str | None = None, rotation: float | None = None) -> str:
    return style(
        {
            "shape": "line",
            "html": 1,
            "strokeColor": color,
            "strokeWidth": width,
            "endArrow": arrow,
            "rotation": rotation,
        }
    )


def add_line(cell_id: str, x: float, y: float, w: float, h: float, color: str = NEUTRAL, width: float = 1.2, arrow: str | None = None, rotation: float | None = None) -> None:
    add_vertex(cell_id, "", line_style(color, width, arrow, rotation), x, y, w, h)


def add_matrix(prefix: str, x: float, y: float, cols: int, rows: int, cell: float, fills: list[str], stroke: str = NEUTRAL) -> None:
    add_vertex(prefix + "-boundary", "", rect_style("none", stroke, 0, 1), x, y, cols * cell, rows * cell)
    for r in range(rows):
        for c in range(cols):
            fill = fills[(r * cols + c) % len(fills)]
            add_vertex(
                f"{prefix}-tile-{r+1}-{c+1}",
                "",
                rect_style(fill, stroke, 0, 0.8),
                x + c * cell,
                y + r * cell,
                cell,
                cell,
            )


def add_patient_dots(prefix: str, x: float, y: float, color: str) -> None:
    for i in range(6):
        fill = color if i < 3 else GRAY
        add_vertex(f"{prefix}-patient-{i+1}", "", ellipse_style(fill, fill), x + i * 28, y, 14, 14)
        add_vertex(f"{prefix}-patient-body-{i+1}", "", rect_style(fill, fill, 1), x + i * 28 - 4, y + 14, 22, 10)
    add_text(prefix + "-ellipsis", "...", x + 170, y, 30, 20, SMALL_LABEL)


def add_dna_icon(prefix: str, x: float, y: float, color: str = BLUE) -> None:
    for i in range(7):
        yy = y + i * 10
        add_vertex(f"{prefix}-base-a-{i}", "", ellipse_style(BLUE_FILL if i in (2, 3) else LIGHT, color), x + (i % 2) * 10, yy, 12, 12)
        add_vertex(f"{prefix}-base-b-{i}", "", ellipse_style(LIGHT, color), x + 42 - (i % 2) * 10, yy, 12, 12)
        add_line(f"{prefix}-link-{i}", x + 10 + (i % 2) * 10, yy + 10, 30 - (i % 2) * 20, 0, "#9EB8D3", 1)
    add_line(prefix + "-rail-a", x, y, 20, 70, color, 2, None, -18)
    add_line(prefix + "-rail-b", x + 40, y, 20, 70, color, 2, None, 18)


def add_wave_icon(prefix: str, x: float, y: float, color: str) -> None:
    for i, yy in enumerate([34, 24, 14, 24, 34]):
        add_vertex(f"{prefix}-wave-{i}", "", ellipse_style(PURPLE_FILL, color), x + i * 13, y + yy, 12, 12)


def add_network_icon(prefix: str, x: float, y: float, color: str = TEAL) -> None:
    pts = [(20, 10), (50, 20), (40, 50), (10, 50), (30, 30)]
    links = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (4, 1), (4, 2)]
    for i, j in links:
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        add_line(f"{prefix}-link-{i}-{j}", x + x1, y + y1, x2 - x1, y2 - y1, "#8FC6C4", 1)
    for i, (px, py) in enumerate(pts):
        add_vertex(f"{prefix}-node-{i}", "", ellipse_style(TEAL_FILL, color, 1.4), x + px - 8, y + py - 8, 16, 16)


def add_metabolite_icon(prefix: str, x: float, y: float, color: str = ORANGE) -> None:
    circles = [(12, 40, 20), (36, 20, 22), (62, 44, 16), (42, 66, 14), (8, 70, 18), (68, 22, 10)]
    for i, (cx, cy, d) in enumerate(circles):
        add_vertex(f"{prefix}-bubble-{i}", "", ellipse_style(ORANGE_FILL if i in (2, 5) else color, color), x + cx, y + cy, d, d)


def add_clipboard_icon(prefix: str, x: float, y: float, color: str = BLUE) -> None:
    add_vertex(prefix + "-board", "", rect_style("#F7FBFF", color, 1, 1.4), x + 10, y + 10, 60, 70)
    add_vertex(prefix + "-clip", "", rect_style(BLUE_FILL, color, 1, 1.2), x + 25, y, 30, 20)
    for i in range(6):
        add_line(f"{prefix}-row-{i}", x + 30, y + 30 + i * 10, 30, 0, "#9EB8D3", 1)
        add_vertex(f"{prefix}-dot-{i}", "", rect_style(color, color, 0), x + 20, y + 28 + i * 10, 4, 4)


def add_feature_columns(prefix: str, x: float, y: float, color: str) -> None:
    heights = [20, 40, 30, 60, 30]
    for i, hh in enumerate(heights):
        add_vertex(f"{prefix}-featurecol-{i}", "", rect_style(color if i == 3 else "#D7E1EA", color, 0, 0.8), x + i * 10, y + (60 - hh), 8, hh)


def add_qc_curve(prefix: str, x: float, y: float, color: str) -> None:
    for i, (xx, yy, ww, hh, rot) in enumerate([(0, 40, 30, 0, -58), (20, 20, 40, 0, -20), (50, 30, 30, 0, 30)]):
        add_line(f"{prefix}-curve-{i}", x + xx, y + yy, ww, hh, color, 1.6, None, rot)
    for i, (xx, yy, ww, hh, rot) in enumerate([(40, 40, 30, 0, -58), (60, 20, 30, 0, -20), (80, 30, 20, 0, 30)]):
        add_line(f"{prefix}-curve-dashed-{i}", x + xx, y + yy, ww, hh, color, 1.2, None, rot)


def add_subtype_dots(prefix: str, x: float, y: float, color: str, points: list[tuple[int, int]]) -> None:
    for i, (px, py) in enumerate(points):
        add_vertex(f"{prefix}-point-{i}", "", ellipse_style(color, color), x + px, y + py, 14, 14)


def add_titles() -> None:
    add_text("title-input", "1. 多组学数据<br>(患者队列)", 50, 20, 270, 60, TITLE)
    add_text("title-preprocess", "2. 预处理与<br>特征提取", 450, 20, 260, 60, TITLE)
    add_text("title-integration", "3. 整合模型", 780, 20, 280, 60, TITLE)
    add_text("title-latent", "4. 潜在表示<br>(UMAP-like)", 1130, 20, 280, 60, TITLE)
    add_text("title-output", "5. 临床输出", 1480, 20, 230, 60, TITLE)


def add_input_lane(key: str, label: str, sublabel: str, y: float, color: str, fill: str, icon: str) -> None:
    prefix = f"node-input-{key}"
    if icon == "dna":
        add_dna_icon(prefix + "-icon", 10, y + 20, color)
    elif icon == "wave":
        add_wave_icon(prefix + "-icon", 10, y + 20, color)
    elif icon == "network":
        add_network_icon(prefix + "-icon", 10, y + 12, color)
    elif icon == "metabolite":
        add_metabolite_icon(prefix + "-icon", 10, y + 0, color)
    else:
        add_clipboard_icon(prefix + "-icon", 10, y + 10, color)
    add_text(prefix + "-label", f"<b>{label}</b><br>{sublabel}", 90, y + 20, 130, 60, LABEL)
    add_patient_dots(prefix, 250, y, color)
    fills = [fill, "#FFFFFF", fill, "#FFFFFF", fill, "#E4EAF0", "#FFFFFF", fill]
    add_matrix(prefix + "-matrix", 240, y + 30, 6, 4, 30, fills, color)
    add_vertex(prefix + "-matrix-port", "", rect_style("none", "none", 0, 0), 420, y + 80, 10, 10)


def add_preprocess_lane(key: str, y: float, color: str, fill: str, label: str = "QC 与标准化") -> None:
    prefix = f"node-preprocess-{key}"
    add_container(prefix, 470, y, 220, 100, color, fill, 1.5)
    add_text(prefix + "-label", f"<b>{label}</b>", 490, y + 10, 160, 20, LABEL)
    if key in {"genomics", "metabolomics"}:
        add_qc_curve(prefix, 500, y + 40, color)
    elif key == "proteomics":
        add_network_icon(prefix + "-network", 500, y + 30, color)
    elif key == "clinical":
        add_clipboard_icon(prefix + "-clip", 500, y + 30, color)
    else:
        add_matrix(prefix + "-miniheat", 500, y + 40, 5, 2, 20, [fill, "#FFFFFF", "#CDB8DD", fill], color)
    add_line(prefix + "-internal-arrow", 580, y + 60, 40, 0, NEUTRAL, 1.2, "block")
    add_feature_columns(prefix, 630, y + 30, color)


def add_integration_model() -> None:
    add_container("node-integration", 800, 310, 260, 300, "#222222", "#FFFFFF", 1.5)
    add_text("node-integration-title", "<b>多组学融合模型</b>", 840, 330, 180, 30, LABEL)
    stack_x = 820
    stack_y = 370
    colors = [BLUE, PURPLE, TEAL, ORANGE, BLUE]
    fills = [BLUE_FILL, PURPLE_FILL, TEAL_FILL, ORANGE_FILL, "#D7E1EA"]
    for i, (stroke, fill) in enumerate(zip(colors, fills)):
        add_matrix(f"node-integration-omicsstack-{i}", stack_x, stack_y + i * 40, 4, 2, 15, [fill, "#D7E1EA", fill, "#FFFFFF"], stroke)
        add_line(f"node-integration-stream-{i}", 890, stack_y + i * 40 + 20, 40, (2 - i) * 10, NEUTRAL, 1, "block")
    xs = [930, 970, 1010]
    layers = [[0, 1, 2, 3], [0, 1, 2], [0, 1]]
    for li, layer in enumerate(layers):
        for ni, _ in enumerate(layer):
            cy = 390 + ni * 50 + (li * 10)
            add_vertex(f"node-integration-network-l{li}-n{ni}", "", ellipse_style("#D9D9D9", "#555555", 1.2), xs[li], cy, 20, 20)
    for li in range(2):
        for ni in range(len(layers[li])):
            for nj in range(len(layers[li + 1])):
                x1 = xs[li] + 20
                y1 = 400 + ni * 50 + (li * 10)
                x2 = xs[li + 1]
                y2 = 400 + nj * 50 + ((li + 1) * 10)
                add_line(f"node-integration-network-link-{li}-{ni}-{nj}", x1, y1, x2 - x1, y2 - y1, "#B8B8B8", 0.8)
    add_text("node-integration-caption", "共享潜在空间<br>Deep neural network / Graph", 830, 550, 200, 40, SMALL_LABEL)


def add_latent_panel() -> None:
    add_container("node-latent", 1140, 250, 260, 450, GRAY, "#FFFFFF", 1.3)
    add_line("node-latent-yaxis", 1160, 550, 0, -250, "#111111", 1.4, "block")
    add_line("node-latent-xaxis", 1160, 550, 210, 0, "#111111", 1.4, "block")
    blue_pts = [(82, 58), (102, 52), (122, 66), (142, 82), (78, 82), (100, 94), (122, 100), (150, 112), (70, 118), (94, 130), (118, 138), (145, 145), (86, 158), (112, 170), (135, 166), (160, 174), (75, 190), (103, 202), (132, 198), (154, 212)]
    purple_pts = [(45, 210), (68, 202), (88, 216), (32, 234), (56, 240), (82, 250), (104, 238), (38, 268), (62, 278), (92, 278), (50, 305), (76, 306), (100, 296), (28, 296), (70, 330), (96, 326)]
    teal_pts = [(166, 224), (188, 216), (204, 238), (148, 250), (174, 258), (200, 264), (220, 282), (152, 292), (182, 296), (210, 306), (164, 332), (192, 326), (218, 338), (178, 360), (206, 358)]
    add_subtype_dots("node-latent-subtype-a", 1148, 250, "#2E86DE", blue_pts)
    add_subtype_dots("node-latent-subtype-b", 1148, 250, PURPLE, purple_pts)
    add_subtype_dots("node-latent-subtype-c", 1148, 250, TEAL, teal_pts)
    add_vertex("node-latent-legend-a-dot", "", ellipse_style("#2E86DE", "#2E86DE"), 1202, 590, 14, 14)
    add_text("node-latent-legend-a", "亚型 A", 1220, 580, 80, 30, SMALL_LABEL)
    add_vertex("node-latent-legend-b-dot", "", ellipse_style(PURPLE, PURPLE), 1202, 624, 14, 14)
    add_text("node-latent-legend-b", "亚型 B", 1220, 620, 80, 30, SMALL_LABEL)
    add_vertex("node-latent-legend-c-dot", "", ellipse_style(TEAL, TEAL), 1202, 658, 14, 14)
    add_text("node-latent-legend-c", "亚型 C", 1220, 650, 80, 30, SMALL_LABEL)


def add_biomarker_panel() -> None:
    add_container("node-biomarkers", 1490, 130, 220, 320, "#222222", "#FFFFFF", 1.4)
    add_text("node-biomarkers-title", "<b>亚型标志物</b>", 1520, 150, 160, 30, LABEL)
    add_text("node-biomarkers-cols", "A      B      C", 1560, 190, 130, 20, SMALL_LABEL)
    for i in range(4):
        add_vertex(f"node-biomarkers-dna-left-{i}", "", ellipse_style(BLUE_FILL, BLUE), 1510 + (i % 2) * 12, 222 + i * 10, 10, 10)
        add_vertex(f"node-biomarkers-dna-right-{i}", "", ellipse_style("#FFFFFF", BLUE), 1532 - (i % 2) * 12, 222 + i * 10, 10, 10)
    for i, yy in enumerate([272, 262, 252, 262, 272]):
        add_vertex(f"node-biomarkers-rna-dot-{i}", "", ellipse_style(PURPLE_FILL, PURPLE), 1510 + i * 8, yy, 9, 9)
    for i, (px, py) in enumerate([(1512, 312), (1538, 312), (1524, 332), (1510, 346), (1542, 346)]):
        add_vertex(f"node-biomarkers-protein-node-{i}", "", ellipse_style(TEAL_FILL, TEAL), px, py, 10, 10)
    for i, (px, py, fill) in enumerate([(1512, 382, ORANGE), (1538, 382, ORANGE), (1524, 402, ORANGE_FILL), (1510, 418, ORANGE), (1542, 418, ORANGE)]):
        add_vertex(f"node-biomarkers-metabolite-dot-{i}", "", ellipse_style(fill, ORANGE), px, py, 12, 12)
    fills = [
        RED,
        RED_FILL,
        "#FDF4F4",
        "#D6E6F7",
        "#9BC3EC",
        RED_FILL,
        "#F8F8F8",
        "#FFFFFF",
        "#C8DDF4",
        "#7FB0E4",
        "#FFFFFF",
        RED,
        RED_FILL,
        "#FDF4F4",
        "#AAD0EF",
        RED,
        RED_FILL,
        "#F2F2F2",
        "#FFFFFF",
        "#8DBAE6",
        "#BDD7EE",
        "#D5E5F5",
        "#FFFFFF",
        "#FFFFFF",
        "#B7D2EF",
    ]
    add_matrix("node-biomarkers-heatmap", 1560, 220, 5, 5, 24, fills, "#9AA9B5")
    add_text("node-biomarkers-caption", "每个亚型的<br>特征签名", 1550, 380, 140, 40, SMALL_LABEL)


def add_response_panel() -> None:
    add_container("node-response", 1490, 500, 220, 300, "#222222", "#FFFFFF", 1.4)
    add_text("node-response-title", "<b>治疗反应</b>", 1520, 520, 160, 30, LABEL)
    add_text("node-response-ylabel", "Response rate<br>响应率", 1500, 600, 50, 70, TINY_LABEL)
    add_line("node-response-yaxis", 1560, 690, 0, -140, "#111111", 1.2, None)
    add_line("node-response-xaxis", 1560, 690, 140, 0, "#111111", 1.2, None)
    for i, (label, tick_y) in enumerate([("100%", 550), ("75%", 580), ("50%", 620), ("25%", 650), ("0%", 690)]):
        add_text(f"node-response-tick-{i}", label, 1530, tick_y - 10, 30, 20, TINY_LABEL)
        add_line(f"node-response-tickline-{i}", 1550, tick_y, 10, 0, "#111111", 1, None)
    heights = [90, 50, 100]
    cols = [BLUE, PURPLE, TEAL]
    labels = ["A", "B", "C"]
    for i, (h, col, lab) in enumerate(zip(heights, cols, labels)):
        add_vertex(f"node-response-rate-column-{lab}", "", rect_style(col, col, 0, 1), 1570 + i * 50, 690 - h, 30, h)
        add_text(f"node-response-label-{lab}", lab, 1570 + i * 50, 700, 30, 20, SMALL_LABEL)
    add_text("node-response-caption", "预测治疗获益<br>按疾病亚型分层", 1520, 730, 160, 40, SMALL_LABEL)


def add_edges() -> None:
    lane = {
        "genomics": (BLUE, 170),
        "transcriptomics": (PURPLE, 320),
        "proteomics": (TEAL, 470),
        "metabolomics": (ORANGE, 620),
        "clinical": (BLUE, 770),
    }
    for key, (color, cy) in lane.items():
        add_edge(f"edge-input-{key}-preprocess", f"node-input-{key}-matrix-port", f"node-preprocess-{key}", color)
        add_edge(f"edge-preprocess-{key}-integration", f"node-preprocess-{key}", "node-integration", color, [(750, cy), (750, 460)])
    add_edge("edge-integration-latent", "node-integration", "node-latent", "#111111")
    add_edge("edge-latent-biomarkers", "node-latent", "node-biomarkers", "#111111", [(1440, 460), (1440, 290)])
    add_edge("edge-latent-response", "node-latent", "node-response", "#111111", [(1440, 460), (1440, 650)])


def build_drawio() -> str:
    add_titles()
    add_tinted_module("module-input", 0, 90, 430, 760)
    add_tinted_module("module-preprocess", 450, 100, 270, 740)
    add_input_lane("genomics", "基因组学", "突变 / CNV", 120, BLUE, BLUE_FILL, "dna")
    add_input_lane("transcriptomics", "转录组学", "基因表达", 270, PURPLE, PURPLE_FILL, "wave")
    add_input_lane("proteomics", "蛋白质组学", "蛋白丰度", 420, TEAL, TEAL_FILL, "network")
    add_input_lane("metabolomics", "代谢组学", "代谢物丰度", 570, ORANGE, ORANGE_FILL, "metabolite")
    add_input_lane("clinical", "临床数据", "表型 / 人口学", 720, BLUE, "#EDF4FB", "clinical")
    add_preprocess_lane("genomics", 120, BLUE, BLUE_FILL)
    add_preprocess_lane("transcriptomics", 270, PURPLE, PURPLE_FILL)
    add_preprocess_lane("proteomics", 420, TEAL, TEAL_FILL)
    add_preprocess_lane("metabolomics", 570, ORANGE, ORANGE_FILL)
    add_preprocess_lane("clinical", 720, BLUE, "#EDF4FB", "编码与缺失填补")
    add_integration_model()
    add_latent_panel()
    add_biomarker_panel()
    add_response_panel()
    add_edges()

    body = "\n".join(cells)
    return f'''<mxfile host="app.diagrams.net" modified="{datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")}" agent="Codex" version="24.7.17">
  <diagram id="multiomics-disease-subtyping" name="Multi-omics disease subtyping">
    <mxGraphModel dx="{W}" dy="{H}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{W}" pageHeight="{H}" math="1" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
{body}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''


def build_regions() -> list[dict[str, object]]:
    return [
        {"name": "Multi-omics data", "bbox": [0, 90, 430, 760]},
        {"name": "Preprocessing and feature extraction", "bbox": [450, 100, 270, 740]},
        {"name": "Integration model", "bbox": [780, 290, 300, 340]},
        {"name": "Latent representation", "bbox": [1128, 230, 300, 490]},
        {"name": "Clinical outputs", "bbox": [1470, 110, 250, 720]},
    ]


def build_notes() -> str:
    return """# Trace Notes: Multi-omics disease subtyping

## Working Contract

Scientific message: 多组学数据经过质控、特征提取和共享表示学习后，可将患者队列划分为可解释的疾病亚型，并连接到标志物和治疗反应。
Figure type: multi-omics/data-integration workflow.
Audience/journal style: Nature-style scientific schematic, white background, restrained palette, editable vector elements.
Final output: editable draw.io source plus SVG/PNG preview when export tooling is available.
Reference image role: composition and hierarchy guide only.
Draw.io trace role: rebuild all scientific entities as editable draw.io primitives.
Core entities: genomics, transcriptomics, proteomics, metabolomics, clinical covariates, QC/normalization, feature matrices, fusion model, latent embedding, subtype biomarkers, response rate.
Topology: five parallel data lanes converge into one integration model; the model produces latent subtype clusters; clusters feed biomarker and treatment-response outputs.
Labels/formulas: no formulas; labels are editable Chinese text with English abbreviations where needed.
Style constraints: no bitmap body, no shadows, no gradients, no decorative texture, no unlicensed external assets.
QA risks: connector routing around five converging lanes; glyph/text separation inside dense output panels; strict visual comparison may be sensitive to rebuilt labels.
Complex asset policy: no external SVG search; omics objects are self-designed primitive glyphs.

## PNG Layout Extraction

Reference image: `multiomics-disease-subtyping-reference.png`
Pixel size: 1717 x 916
Canvas target: 1720 x 920 draw.io page, near 1:1 mapping, 10 px grid.

Major regions:

- Multi-omics data: reference bbox approx [0, 85, 425, 760]; draw.io bbox [0, 90, 430, 760]; role: five modality lanes with cohort matrices.
- Preprocessing and feature extraction: reference bbox approx [450, 95, 270, 745]; draw.io bbox [450, 100, 270, 740]; role: modality-specific QC and feature vector extraction.
- Integration model: reference bbox approx [790, 300, 285, 330]; draw.io bbox [780, 290, 300, 340]; role: central fusion model with omics stack and graph/neural glyph.
- Latent representation: reference bbox approx [1130, 245, 290, 470]; draw.io bbox [1128, 230, 300, 490]; role: UMAP-like three-cluster subtype map.
- Clinical outputs: reference bbox approx [1480, 120, 235, 700]; draw.io bbox [1470, 110, 250, 720]; role: subtype biomarker heatmap and therapy response chart.

Alignment lines:

- Top stage labels: y = 20.
- Main data path: y centers = 170, 320, 470, 620, 770, converging through x = 750.
- Model-to-latent rail: y = 460.
- Output branch corridor: x = 1440.

Repeated motifs:

- Input patient dots: 6 per lane, first three colored by modality.
- Omics matrices: 6 x 4 tiles per input lane.
- Feature vectors: five qualitative columns per preprocessing module.
- UMAP dots: three subtype clusters, with consistent A/B/C colors.
- Biomarker heatmap: 5 x 5 tiles.

Trace fidelity decisions:

- Preserve: horizontal five-stage pipeline, relative module order, convergence arrows, central model, UMAP-like subtype clusters, two clinical output panels.
- Simplify: generated pseudo-text, decorative line curvature, internal icon detail.
- Replace with editable text: all stage and module labels.

## Asset Notes

No external assets were searched or embedded. All glyphs are self-designed from draw.io primitives:

- DNA/genomics: paired ellipses and thin link lines.
- Transcriptomics: wave-like bead motif plus heatmap.
- Proteomics: graph/network nodes and link lines.
- Metabolomics: metabolite bubble motif.
- Clinical data: clipboard/table motif.
- Fusion model: stacked matrices and neural/graph nodes.
- Outputs: heatmap tiles and response-rate columns.

## Consistency Loop

Iteration records are appended after local export/comparison QA.
"""


def main() -> None:
    DRAWIO.write_text(build_drawio(), encoding="utf-8")
    REGIONS.write_text(json.dumps(build_regions(), indent=2, ensure_ascii=False), encoding="utf-8")
    TRACE_NOTES.write_text(build_notes(), encoding="utf-8")
    print(DRAWIO)
    print(REGIONS)
    print(TRACE_NOTES)


if __name__ == "__main__":
    main()
