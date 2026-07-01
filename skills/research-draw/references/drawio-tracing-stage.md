# Draw.io Tracing Stage

Use this file before creating or editing `.drawio`.

## Trace Contract

Before authoring XML, write a mapping:

```text
Reference region:
Reference bbox:
Draw.io module:
Draw.io bbox:
Cells/glyphs:
Connectors:
Labels:
Formula handling:
What to simplify:
What not to copy:
Consistency loop:
Complex asset decisions:
Strict comparison plan:
```

## Redraw Rules

- Use `research-drawio-skill` for the actual `.drawio` construction.
- Treat the raster reference as a layout guide, not an asset to paste.
- For PNG/JPG/WebP tracing, preserve relative object coordinates, module sizes,
  gutters, and label positions before applying style cleanup.
- Build final scientific objects as editable draw.io primitives unless a
  dedicated SVG is intentionally selected through `add-svg`.
- For complex recognizable objects, use `complex-asset-sourcing.md` before
  accepting a crude primitive sketch.
- Do not duplicate an inserted SVG with redundant primitive glyphs.
- Recreate text manually; do not trust generated image text.
- Recreate formulas with draw.io math support, not as raster pixels.
- Use direct connectors first, one-bend routes second, and multi-bend routes only
  when a named obstacle requires them.
- Keep labels outside glyph bodies.
- Remove decorative background, lighting, texture, fake depth, and ornamental
  detail from the final draw.io version.
- For close GPT/imagegen/raster imitation, plan for at least three strict
  pixel-level export/compare/fix iterations before final delivery. Treat failed
  strict comparison as unfinished work, not as a tradeoff that can be explained
  away.

## QA Checklist

Run:

```bash
python skills/research-drawio-skill/scripts/qa_drawio.py path/to/file.drawio
```

Then inspect:

- all major modules from the reference are represented
- major module positions and dimensions are visibly close to the reference
- the consistency loop has been run and documented
- close tracing tasks include at least three strict comparison iterations and a
  final strict-comparison pass before being called complete
- complex objects have either acceptable fidelity or asset-search notes
- no generated bitmap is required for the final structure
- labels do not overlap glyphs
- connectors do not cross text, formulas, or node bodies
- formulas are MathJax-ready and `math="1"` is enabled
- the layout is compact and aligned to the grid
- colors have semantic roles
- the final `.drawio` can be edited independently of the reference image
