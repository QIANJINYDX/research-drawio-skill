# Two-Stage Workflow

Use this file for every `research-draw` task.

## Stage 0: Contract

Write compact working notes before creating images or diagrams:

```text
Scientific message:
Figure type:
Audience/journal style:
Final output:
Reference image role:
Draw.io trace role:
Core entities:
Topology:
Labels/formulas:
Style constraints:
QA risks:
Consistency loop:
Text completeness audit:
Complex SVG policy:
```

## Stage 1: Raster Reference

Use an existing PNG/JPG/WebP reference when one is already available. Otherwise,
use imagegen to create a scientific illustration reference that clarifies:

- composition
- figure balance
- module hierarchy
- visual metaphor
- object silhouettes
- color discipline

The generated image must not be treated as final editable source. It is a
composition target for the next stage.

When an existing raster reference is available, do not regenerate it unless the
user asks. Treat the existing image as the geometry target and load
`png-layout-extraction.md`.

## Stage 2: Draw.io Trace

Use `research-drawio-skill` to rebuild the figure as `.drawio`:

- Translate the reference image into modules, nodes, glyphs, connectors, and
  labels.
- Preserve the reference image's relative geometry before making style
  improvements.
- Redraw abstract scientific structure with draw.io primitives.
- Redraw complex recognizable objects as dedicated SVG glyphs, then insert the
  rendered/validated SVG into draw.io.
- Recreate labels manually as editable text.
- Recreate formulas using draw.io MathJax.
- Simplify decorative details that do not carry scientific meaning.
- Use self-designed SVG glyphs by default for complex recognizable objects.
  Use online SVG/vector assets only when requested or when they are clearly
  legal, style-compatible, and more faithful than a self-designed glyph.
- Run the consistency loop before final delivery.
- After strict pixel comparison, run a final text completeness audit against
  the intended labels/formulas, not only against visual similarity metrics.

## Trace Fidelity

Match these properties:

- global composition
- reading path
- relative module scale
- approximate module coordinates
- repeated motif spacing
- semantic color roles
- major object shape
- connector direction
- complex object recognizability

Do not match these blindly:

- generated pseudo-text
- inconsistent icon detail
- decorative lighting
- shadows, gradients, texture, or background effects
- biologically or mathematically incorrect details

## Completion Criteria

The task is complete only when:

- the reference image is saved or clearly unavailable
- the `.drawio` source exists
- the final draw.io diagram does not depend on the bitmap for its structure
- text and formulas are editable
- intended labels, legends, panel letters, axis text, annotations, and formulas
  have been audited for omission, truncation, spelling drift, duplication, and
  pseudo-text remnants after pixel comparison
- connectors do not overlap labels or glyphs
- complex objects have SVG glyph notes and pixel-comparison records, or an
  explicit user-approved reason to keep a primitive-only version
- the consistency loop has been run and documented
- local draw.io QA has been run when Python is available
