# Strict Visual Comparison

Use this when a draw.io redraw is meant to imitate a GPT/imagegen/raster
reference closely, not only preserve the scientific idea.

## Purpose

Exported previews make rendering visible, but visual inspection alone is too
weak for tracing. Run a quantitative comparison between the reference image and
the exported draw.io PNG so geometry, silhouette, color, and local mismatch
problems are surfaced before delivery.

## Required Command

First export the draw.io preview:

```bash
python skills/research-drawio-skill/scripts/export_drawio_preview.py path/to/figure.drawio --formats png svg
```

Then compare the exported PNG against the reference:

```bash
python skills/research-drawio-skill/scripts/compare_drawio_reference.py reference.png path/to/exports/figure.png --mode strict
```

The script writes:

```text
comparison-report.json
tile-mismatches.csv
region-mismatches.csv when --regions-json is provided
diff-heatmap.png
foreground-overlay.png
side-by-side.png
```

For named module checks, create a small JSON file from the trace notes:

```json
[
  {"name": "Input image tile", "bbox": [15, 340, 250, 230]},
  {"name": "Stage 1", "bbox": [500, 285, 170, 360]},
  {"name": "Output probabilities", "bbox": [1540, 290, 230, 230]}
]
```

Then run:

```bash
python skills/research-drawio-skill/scripts/compare_drawio_reference.py reference.png path/to/exports/figure.png --mode strict --regions-json regions.json
```

## Modes

| Mode | Use when | Expected behavior |
|---|---|---|
| `exact` | The redraw should be a near-facsimile of a clean raster or previous draw.io export | Very tight thresholds; most intentional redesigns fail |
| `strict` | Default for GPT/imagegen-to-drawio tracing | Allows editable simplification but flags visible layout, silhouette, color, and density drift |
| `semantic` | The reference is only a loose concept image | Checks broad object placement and nonblank rendering |

For "make draw.io as close as possible to GPT drawing", use `strict` during
every iteration and optionally run `exact` as an aspirational diagnostic.

## Metrics To Inspect

- `mae` / `rmse`: global pixel color difference after content-bbox normalization.
- `ssim`: grayscale structural similarity; useful for overall layout.
- `foreground_iou`: overlap of non-white content masks; sensitive to missing or
  displaced objects.
- `edge_iou`: overlap of edge maps; sensitive to layer outlines, arrows, and
  silhouettes.
- `bbox_aspect_delta`: content-shape aspect mismatch after cropping margins.
- `content_area_delta`: content density mismatch.
- `worst_tile_mae`: largest local mismatch in the grid report.

Do not rely on one score. A diagram can pass global MAE while still having a
bad local region. Inspect the worst rows in `tile-mismatches.csv` and the orange
boxes in `foreground-overlay.png`.

When named regions are available, inspect `region-mismatches.csv` first. It is
more actionable than global scores because it maps failures to figure modules.

## Iteration Policy

Run comparison after each meaningful redraw. For close GPT/imagegen/raster
tracing tasks, perform at least three export/compare/fix iterations before
calling the work complete. If a pass occurs before iteration 3, keep running the
remaining iterations as verification and cleanup passes with the same
thresholds.

Fix in this order:

1. Canvas/content bbox: match reference crop, aspect ratio, and major margins.
2. Major modules: fix x/y positions, width/height, and gutters for the worst
   mismatch tiles.
3. Object silhouettes: replace weak primitive sketches with SVG/vector assets
   or more faithful draw.io primitives.
4. Repeated motifs: match counts, offsets, angle, density, and color family.
5. Text baselines: align labels and remove overlap.
6. Connectors: simplify routes and match arrow placement without crossing text.

Stop only after at least three strict-comparison iterations and a passing strict
result. Do not treat editability, vectorization, formula rebuilding, or
scientific-cleanup language as automatic exceptions to failed metrics. If strict
comparison still fails, keep editing while concrete local fixes remain. If
further progress is blocked, report `not passed` with the worst remaining
mismatches and the blocking reason.
