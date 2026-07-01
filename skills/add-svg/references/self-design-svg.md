# Self-Designed SVG Mode

Use this file after the user chooses self-designed SVGs, or as the fallback when
network search cannot find a suitable candidate.

## Design Contract

Design SVGs as restrained scientific glyphs:

- White or transparent background.
- Simple vector primitives: `path`, `rect`, `circle`, `ellipse`, `line`,
  `polyline`, `polygon`, and minimal `text` only when needed.
- Consistent stroke width, usually 1.2-2 px at icon scale.
- Low-saturation Nature-style palette.
- Clear silhouette at small size.
- No shadows, gradients, noisy textures, bitmap filters, or decorative detail.

## Palette

Use this default palette unless the target diagram already defines one:

```text
text/stroke: #1F2933
neutral:     #4D5E6E
soft fill:   #F7F9FC
module:      #EEF3F8
signal:      #0F4D92
secondary:   #42949E
positive:    #8BCF8B
warning:     #B64342
soft accent: #E4CCD8
```

## Common Original SVG Glyphs

- DNA/RNA: paired circles or short bars connected by neutral rungs.
- Protein/molecule: compact bead chain with one highlighted domain.
- Cell: ellipse body, nucleus, and 1-3 phenotype dots.
- Sequencing: sample tube/card plus read strips.
- Database: cylinder or stacked cards with table marks.
- Model: layered blocks, matrix tiles, or network nodes.
- Microscope/image: lens circle plus small image tile.
- Assay/experiment: sample glyph plus arrow to measurement tile.

## SVG Authoring Rules

- Include `xmlns="http://www.w3.org/2000/svg"`.
- Set a compact `viewBox`, usually `0 0 96 96` or `0 0 120 120`.
- Keep IDs semantic when useful, such as `cell-body`, `dna-rung-1`.
- Use `fill="none"` where possible and explicit colors where needed.
- Avoid embedded CSS that draw.io may strip; use direct attributes for critical
  appearance.
- Keep text editable only when it is a necessary scientific label; otherwise put
  labels outside the SVG in draw.io.

## Self-Design Handoff

For every self-designed SVG, note:

```text
Concept:
Scientific role:
Design summary:
Palette:
Intended size:
Editable SVG path:
Integration target:
```
