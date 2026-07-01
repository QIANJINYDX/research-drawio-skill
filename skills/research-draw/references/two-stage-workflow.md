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
Complex asset policy:
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
- Redraw scientific objects with draw.io primitives or approved SVG assets.
- Recreate labels manually as editable text.
- Recreate formulas using draw.io MathJax.
- Simplify decorative details that do not carry scientific meaning.
- Use online SVG/vector assets for complex recognizable objects when primitive
  sketches would be visibly inferior.
- Run the consistency loop before final delivery.

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
- connectors do not overlap labels or glyphs
- complex objects have asset-search notes or acceptable primitive fidelity
- the consistency loop has been run and documented
- local draw.io QA has been run when Python is available
