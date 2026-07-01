# PNG Layout Extraction

Use this file when the user provides or references an existing PNG/JPG/WebP
figure and asks for a faithful draw.io redraw.

## Purpose

Avoid loose semantic redesign. First extract the reference figure's geometry,
then redraw it as editable draw.io primitives.

## Required Layout Pass

Before authoring `.drawio`, inspect the raster reference and write:

```text
Reference image:
Pixel size:
Canvas target:
Major regions:
  name:
  approximate bbox in pixels:
  target bbox in draw.io:
  visual role:
Alignment lines:
  top labels:
  main data path:
  output row:
Repeated motifs:
  motif:
  count:
  spacing:
  color family:
Complex elements:
  object:
  primitive suitability:
  asset search needed:
Trace fidelity decisions:
  preserve:
  simplify:
  replace with editable text:
```

Use image inspection tools when available:

- `view_image` for visual inspection.
- Python/Pillow for image size and optional crop checks.
- Manual coordinate estimates are acceptable, but they must be explicit.

## Fidelity Priority

Preserve, in order:

1. main reading path and object order
2. relative x/y positions of major modules
3. module widths, heights, and gutters
4. repeated motif counts and spacing
5. color families
6. label placement and line breaks
7. fine decorative style

Do not preserve generated or raster-specific artifacts:

- anti-aliased shadows
- gradients that do not encode meaning
- noisy pseudo-text
- perspective depth that harms editability
- bitmap-only textures

## Draw.io Scaling Rule

Choose a draw.io canvas with the same aspect ratio as the PNG unless the user
requests a new format. Map pixel coordinates to draw.io coordinates with one
constant scale factor where practical.

If the reference image is already close to a useful draw.io canvas size, use a
1:1 or near-1:1 mapping and snap major objects to a 10 px grid. Small internal
details may use 5 px increments only when needed for visual fidelity.

## Faithfulness QA

After drawing, compare against the PNG:

- Does each major object occupy a similar relative position?
- Are stage labels above the same modules?
- Are input/output labels and probability bars placed like the reference?
- Do feature-map stacks have similar count, angle/offset, and color family?
- Do residual bypasses wrap around the residual unit rather than appear as
  generic arrows?
- Are complex recognizable objects faithful enough, or should they be replaced
  with searched SVG/vector assets?
- Did any simplification change the scientific meaning?

If the answer to any item is no, revise before final delivery.
