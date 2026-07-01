# Imagegen Reference Stage

Use this file before generating the raster reference.

## Purpose

Generate a composition reference, not a final figure. The reference should help
decide layout, hierarchy, grouping, and visual tone before the editable draw.io
redraw.

## Prompt Contract

Use the `imagegen` skill default built-in path unless the user explicitly asks
for CLI/API mode. Keep the prompt concise and technically constrained:

```text
Use case: scientific-educational
Asset type: reference image for redraw into editable draw.io
Primary request:
Scientific message:
Subject:
Diagram structure:
Style/medium: clean publication-style scientific schematic, white background,
  restrained Nature-style palette, flat vector-like rendering
Composition/framing:
Required visual elements:
Text: minimal placeholder labels only; no dense text
Constraints: no shadows, no glossy gradients, no decorative texture, no
  watermarks, no pseudo-UI, no microscopic unreadable labels
Avoid:
```

## Reference Image Rules

- Prefer a white or very light background.
- Ask for modular composition with clear whitespace corridors.
- Use placeholder labels only when labels are needed for layout.
- Avoid detailed prose, exact equations, and small text because generated text is
  unreliable.
- Ask for simple arrows and clear spatial grouping.
- Avoid photorealism unless the user specifically asks for a realistic
  conceptual figure.
- Save the selected image into the workspace when it will guide the draw.io
  redraw.

## Inspection Checklist

After generation, inspect the reference:

- Are the main modules visible and separable?
- Is the reading path clear?
- Are scientific objects plausible?
- Are generated labels ignored or corrected in draw.io?
- Are there elements that should be deleted before tracing?
- Is the composition compact enough for a paper figure?

If the reference fails composition or scientific plausibility, iterate once with
a targeted prompt correction before tracing.
