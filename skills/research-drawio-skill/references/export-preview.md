# Draw.io Export Preview

Use this before final delivery when a `.drawio` file has been created or edited
and visual fidelity matters.

## Required Tool

Use diagrams.net/draw.io Desktop CLI. On Windows, install it with:

```powershell
winget install --id JGraph.Draw --accept-package-agreements --accept-source-agreements
```

If the executable is not on `PATH`, set `DRAWIO_CLI` or pass `--drawio-cli`.
Known Windows installations may live under `D:\drawio\draw.io\draw.io.exe`,
`%LOCALAPPDATA%\Programs\draw.io\draw.io.exe`, or `Program Files`.

## Export Command

Prefer the bundled helper because it locates the executable, uses relative paths
for Windows CLI compatibility, waits for output files, and probes the exported
preview:

```bash
python skills/research-drawio-skill/scripts/export_drawio_preview.py path/to/figure.drawio --formats png svg
```

Expected outputs:

```text
path/to/exports/figure.png
path/to/exports/figure.svg
```

## Visual QA Loop

After exporting:

- Inspect the PNG preview when the environment can display images.
- Confirm the preview is nonblank and the expected page content is visible.
- Check that inserted SVGs render inside the exported PNG/SVG, not only in XML.
- Check that labels do not overlap glyphs, connectors, formulas, or SVG assets.
- Check that the crop/canvas does not hide important content.
- Compare the preview against the source reference image for traced figures.
- If mismatches are visible, edit the `.drawio`, export again, and repeat.

For traced GPT/imagegen/raster figures, run strict comparison after export:

```bash
python skills/research-drawio-skill/scripts/compare_drawio_reference.py reference.png path/to/exports/figure.png --mode strict
```

Use `diff-heatmap.png`, `foreground-overlay.png`, and `tile-mismatches.csv` to
locate the next edits. Preview export without this comparison is not sufficient
when the goal is close imitation.

For close imitation tasks, repeat export and strict comparison for at least
three iterations. A failed strict comparison remains blocking; do not present it
as acceptable simply because the final diagram is editable or vectorized.

## Failure Handling

- If export returns success but no file appears, retry through
  `export_drawio_preview.py`; some Windows draw.io builds are sensitive to
  absolute `--output` paths.
- If draw.io Desktop is unavailable, say that preview-based consistency QA could
  not be completed and provide the exact missing install/configuration step.
- XML QA alone is not enough for tasks that involve SVG insertion, image cells,
  complex layouts, formula rendering, or trace fidelity.
