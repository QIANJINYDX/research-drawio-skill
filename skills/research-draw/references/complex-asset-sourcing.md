# Complex SVG Glyph Workflow

Use this file when tracing or redrawing objects that are difficult to represent
faithfully with simple draw.io primitives.

## Core Rule

Complex recognizable elements should become standalone SVG glyphs. Do not build
animals, organs, detailed cells, anatomy icons, protein cartoons, instruments,
or similar silhouette-sensitive objects by stitching many draw.io primitives
together. The SVG file is the editable source for that object; draw.io remains
the editable source for containers, connectors, labels, formulas, and layout.

## Complex Object Test

Treat an object as complex when any condition is true:

- It must be recognizable by silhouette, such as a cat, dog, mouse, organ,
  microscope, scanner, lab animal, protein cartoon, or anatomy icon.
- A draw.io primitive version would need more than about 12 shapes to look
  acceptable.
- A crude primitive sketch changes the scientific meaning or visual class.
- The object is a repeated icon where inconsistency would be obvious.
- The reference crop has meaningful outline, internal morphology, or pose.
- The user asks for online materials, assets, icons, SVGs, or reference
  elements.

## Decision

Use this order:

1. If the object is simple and abstract, draw it with normal draw.io primitives.
2. If the object fails the complex object test, author a dedicated SVG glyph by
   default.
3. If the user explicitly requests online assets, or a self-designed glyph would
   be legally/scientifically weaker, use `add-svg` network mode and follow its
   source gate.
4. If network results are absent, legally unclear, too detailed, or inconsistent
   with the figure style, create a self-designed SVG glyph.
5. Use a primitive-only complex object only when the user explicitly prioritizes
   full draw.io editability over visual fidelity, or no reference crop exists
   and the object is not silhouette-sensitive.

## SVG Authoring Contract

- Keep a compact `viewBox`, usually `0 0 96 96`, `0 0 120 120`, or the
  reference crop aspect ratio.
- Use vector primitives such as `path`, `rect`, `circle`, `ellipse`, `line`,
  `polyline`, and `polygon`.
- Use direct attributes for critical appearance; avoid embedded CSS that
  draw.io may strip.
- Use a restrained scientific palette and consistent stroke widths.
- Avoid shadows, filters, gradients, bitmap textures, and decorative realism.
- Put labels, formulas, captions, and long annotations outside the SVG as
  editable draw.io text.

## Glyph Pixel Comparison

Before inserting a complex SVG into draw.io:

1. Crop the reference object region and save it, for example
   `reference-crops/<concept>.png`.
2. Render the SVG to PNG at the target bbox size on a white or transparent
   background matching the reference crop.
3. Compare the rendered SVG PNG against the crop:

```bash
python skills/research-drawio-skill/scripts/compare_drawio_reference.py reference-crops/concept.png rendered-glyphs/concept.png --mode strict --out-dir glyph-comparison/concept
```

4. Inspect `comparison-report.json`, `diff-heatmap.png`,
   `foreground-overlay.png`, and worst tiles.
5. Revise the SVG until scale, silhouette, color family, and major internal
   features are close enough. If strict comparison still fails, record the
   remaining mismatch and do not present it as passed.

If no standalone SVG renderer is available, insert the SVG into a temporary
draw.io file, export that crop/preview, and run the same comparison on the
exported PNG.

## Draw.io Insertion Contract

- Insert selected SVGs as URL-encoded `data:image/svg+xml,` image cells.
- Do not use raw `data:image/svg+xml;base64,...` in draw.io style strings.
- Put the SVG image cell in the same bbox as the reference object.
- Preserve the reference object's approximate scale, baseline, and pose.
- Keep labels outside the SVG body.
- Route connectors to the SVG bbox or a transparent boundary cell, not to
  internal visual details.
- Remove duplicate draw.io primitive sketches for the same concept unless the
  user asks for a side-by-side comparison.
- Re-run the full consistency loop after insertion.

## Candidate Note Format

```text
Concept:
Why draw.io primitive assembly is insufficient:
Reference crop:
SVG source mode:
Editable SVG path:
Rendered SVG PNG:
Glyph comparison output:
Strict comparison pass/fail:
Remaining mismatches:
Selected online source, if any:
  source URL:
  direct SVG URL:
  license:
  attribution:
Draw.io cell:
Duplicate primitive removal:
```
