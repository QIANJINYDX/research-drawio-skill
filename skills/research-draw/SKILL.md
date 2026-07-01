---
name: research-draw
description: >-
  Two-stage workflow for publication-style scientific schematics: generate or
  use a raster reference with imagegen/PNG/JPG/WebP, then trace it into an
  editable diagrams.net/draw.io file using research-drawio-skill. Use for
  Nature-style scientific illustrations, graphical abstracts, model or mechanism
  schematics, biomedical workflows, AI architecture figures, and paper-style
  visual drafts that should become editable .drawio source. Supports optional
  online SVG/vector asset search for complex objects and enforces a minimum
  three-round strict pixel-level export/compare/fix loop for close
  raster-to-draw.io tracing tasks. Use with imagegen, draw.io, diagrams.net,
  scientific illustration, graphical abstract, paper schematic, figure tracing,
  and drawio redraw requests.
---

# Research Draw

Create or use a high-quality scientific illustration reference first, then
redraw it as an editable draw.io diagram. The raster image is a composition and
geometry guide, not the final source of truth.

## Required Skill Sequence

1. Use `imagegen` for the reference-image stage only when no suitable raster
   reference already exists.
2. Use `research-drawio-skill` for the draw.io tracing stage.
3. Do not embed the generated bitmap as the final diagram body unless the user
   explicitly asks for a raster-backed figure.

## Routing Protocol

1. Read `references/two-stage-workflow.md` before starting.
2. Read `references/imagegen-reference-stage.md` before generating the raster
   reference image.
3. If tracing an existing PNG/JPG/WebP, read
   `references/png-layout-extraction.md` before authoring or editing `.drawio`.
4. Read `references/drawio-tracing-stage.md` before authoring or editing
   `.drawio`.
5. If complex real-world elements are present, such as animals, organs,
   instruments, cells with detailed morphology, or domain icons, read
   `references/complex-asset-sourcing.md`.
6. Before final delivery, read `references/consistency-loop.md` and run the
   loop. For GPT/imagegen/raster tracing where close imitation matters, this is
   a minimum three-round strict pixel-level export/compare/fix loop.
7. For GPT/imagegen/raster tracing where close imitation matters, make the
   draw.io stage load `research-drawio-skill` strict visual comparison rules.
8. If formulas appear, make the draw.io stage load the math reference from
   `research-drawio-skill`.
9. If SVG icons or online assets are needed during the draw.io stage, use the
   local `add-svg` skill and follow its source gate.

## Operating Rules

- Establish the scientific message before image generation.
- Keep the reference image label-light. Final labels, formulas, and captions
  should be rebuilt as editable draw.io text.
- Treat imagegen text as unreliable unless it is visually inspected and correct.
- Use imagegen to explore composition, visual hierarchy, spatial grouping,
  lighting-free style, and object silhouettes.
- When a PNG/JPG/WebP reference exists, trace geometry before redesigning:
  preserve relative object positions, sizes, gutters, and visual density unless
  the user asks for redesign.
- Use draw.io primitives for the final network blocks, arrows, matrices,
  biological objects, charts, and labels.
- Do not hand-draw complex recognizable objects when the primitive version would
  reduce fidelity. Search for licensed SVG/vector assets through `add-svg`
  network mode, or create a self-designed fallback only when search is
  unavailable, unsuitable, or the user rejects online assets.
- Preserve scientific correctness, but do not use editability, vectorization,
  formula rebuilding, or scientific-cleanup language to excuse avoidable visual
  mismatch. If strict comparison fails, keep editing or report the task as not
  yet passed.
- Run the consistency loop after tracing. Fix blocking geometry, semantic, and
  draw.io QA mismatches before delivery, or state the remaining mismatches.
- When the goal is close imitation of a GPT/imagegen reference, export the
  draw.io PNG and run quantitative comparison in at least three iterations. Use
  the worst mismatch tiles and diff overlays to drive each additional edit pass.
- Do not claim completion with wording such as "strict pixel comparison did not
  pass because this is an editable redraw" or "metrics are documented in trace
  notes." A failed strict comparison remains a failed QA gate unless the user
  explicitly accepts a different target.

## Output Contract

Deliver or prepare:

```text
reference image: path to generated raster concept
editable source: .drawio file
trace notes: mapping from reference regions to draw.io modules, including
  approximate reference coordinates for major regions
asset notes: searched/selected assets, license notes, and self-designed fallbacks
consistency loop: at least three iteration records for close tracing, fixes
  made, remaining mismatches
strict comparison: per-iteration metrics, pass/fail, diff overlay paths, worst
  mismatch tiles, and final status as passed or not passed
QA: draw.io validation result and remaining risks
```

If image generation is unavailable, skip the raster stage only after stating the
blocker, then proceed with `research-drawio-skill` directly.
