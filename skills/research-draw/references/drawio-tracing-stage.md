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
Text completeness audit:
What to simplify:
What not to copy:
Consistency loop:
Complex SVG glyph decisions:
SVG crop comparison:
Strict comparison plan:
```

## Redraw Rules

- Use `research-drawio-skill` for the actual `.drawio` construction, layout
  checks, export, and QA.
- Override any primitive-composite default for complex recognizable objects:
  those objects use the SVG glyph workflow in `complex-asset-sourcing.md`.
- Treat the raster reference as a layout guide, not an asset to paste.
- For PNG/JPG/WebP tracing, preserve relative object coordinates, module sizes,
  gutters, and label positions before applying style cleanup.
- Build abstract structure and simple glyphs as editable draw.io primitives.
- Build complex recognizable objects as dedicated SVG glyphs. Use
  `complex-asset-sourcing.md` before constructing any complex object from
  draw.io primitives.
- Do not duplicate an inserted SVG with redundant primitive glyphs.
- Keep the SVG file itself as the editable source for the complex glyph; keep
  draw.io text, formulas, containers, and connectors editable around it.
- Recreate text manually; do not trust generated image text.
- Recreate formulas with draw.io math support, not as raster pixels.
- Maintain an intended text inventory while tracing so the final text audit can
  compare source/intended text against actual draw.io text cells.
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
- the final text completeness audit has been run after pixel comparison
- all intended labels, formulas, legends, panel letters, axis text, and
  annotations are present, editable, correctly spelled, and not truncated
- generated pseudo-text from the reference has been removed or replaced
- complex objects have dedicated SVG glyphs, source/self-design notes, and
  per-glyph pixel-comparison records
- any primitive-only complex object has an explicit justification
- no generated bitmap is required for the final structure
- labels do not overlap glyphs
- connectors do not cross text, formulas, or node bodies
- formulas are MathJax-ready and `math="1"` is enabled
- the layout is compact and aligned to the grid
- colors have semantic roles
- the final `.drawio` can be edited independently of the reference image
