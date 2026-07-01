# Research Draw.io Style Guide

Use this guide when creating or polishing a paper-style flowchart.

## Typography

- Font family: Arial, Helvetica, or a clean sans-serif fallback.
- Final journal-size text: usually 6-8 pt for dense figures, 8-10 pt for a
  standalone schematic, and 10-12 pt only for slide-style output.
- Use bold sparingly for panel labels, module headers, and the hero module.
- Keep labels short. Prefer "Model training" over "The model was trained using".
- Do not rasterize text if SVG/PDF export is expected.
- Keep formulas in dedicated math text cells. Do not mix long equations with
  process labels inside the same node.

## Size and Canvas

- Single-column journal target: about 89 mm wide.
- Double-column journal target: about 183 mm wide.
- Work in a larger editable canvas if useful, but inspect the exported SVG/PDF at
  the final physical size.
- Leave enough margin for panel labels and caption placement.
- Use fixed grid spacing: 20 px for node placement, 10 px for small internal
  elements, and 40-60 px gutters between major modules.
- Keep nodes in the same semantic tier equal in width and height unless one is
  intentionally the hero node.

## Palette

Default restrained palette:

| Role | Color |
|---|---|
| Text / key stroke | `#1F2933` |
| Neutral stroke | `#4D5E6E` |
| Neutral fill | `#F7F9FC` |
| Module band | `#EEF3F8` |
| Main method / signal | `#0F4D92` |
| Secondary signal | `#42949E` |
| Validation / positive cue | `#8BCF8B` |
| Warning / exclusion cue | `#B64342` |
| Soft accent | `#E4CCD8` |

Rules:

- Keep the same entity or method in the same color throughout the diagram.
- Use low-saturation fills and darker strokes for print readability.
- Do not use rainbow palettes, decorative gradients, or red/green as the only
  distinction.
- Use color plus shape, position, or label when accessibility matters.

## Shape Semantics

| Meaning | Preferred shape |
|---|---|
| Process / action | rounded rectangle with small radius |
| Data / document | document or rectangle with label |
| Stored database | cylinder, used sparingly |
| Decision / branch | diamond only for true yes/no or inclusion/exclusion logic |
| Sample/material | rectangle or simple icon plus label |
| Output/result | emphasized rectangle or callout |
| Group/module | light container band without heavy border |

Avoid mixing many shape types. Shape changes should carry meaning.

## Composite Visual Elements

- Use composite visual elements for key scientific objects: datasets, plots,
  matrices, DNA/RNA, cells, networks, model layers, instruments, samples, and
  outputs.
- Build them from editable draw.io primitives. Do not paste bitmap icons when a
  simple grouped glyph can express the idea.
- Keep each glyph simple enough to read at final size: usually 3-12 primitive
  shapes, more only for matrix/tile patterns.
- Put the label below or beside the glyph; do not fill the glyph with prose.
- Use the same palette and line weights as the rest of the figure.

## Connectors

- Use orthogonal connectors with consistent stroke width.
- Use solid arrows for primary sequence or information flow.
- Use dashed arrows for optional, inferred, or feedback relationships.
- Label arrows only when the relationship is not obvious, such as "filter",
  "train", "validate", "inhibit", or "merge". Put those labels in separate
  frameless text cells when the edge is long, bent, or near other labels.
- Avoid diagonal arrows, arrow crossings, and decorative arrowheads.
- No connector may run through a text-bearing shape, formula cell, matrix cell,
  module header, panel label, or legend item.

## Draw.io Style Presets

Process node:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#F7F9FC;strokeColor=#4D5E6E;fontColor=#1F2933;fontFamily=Arial;fontSize=11;spacing=8;
```

Hero node:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#EAF2FB;strokeColor=#0F4D92;strokeWidth=1.5;fontColor=#1F2933;fontFamily=Arial;fontSize=12;fontStyle=1;spacing=8;
```

Module container:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=6;fillColor=#EEF3F8;strokeColor=#D7E1EA;fontColor=#1F2933;fontFamily=Arial;fontSize=11;fontStyle=1;spacing=8;
```

Primary connector:

```text
edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#4D5E6E;strokeWidth=1.2;
```

Secondary connector:

```text
edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;dashed=1;dashPattern=4 3;orthogonalLoop=1;jettySize=auto;strokeColor=#767676;strokeWidth=1;
```

Math text cell:

```text
text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Arial;fontSize=12;fontColor=#1F2933;spacing=4;
```

## Panel Labels and Legends

- Use lowercase bold panel letters (`a`, `b`, `c`) near the upper-left of each
  panel.
- Keep legends frameless and compact. Prefer direct labels when possible.
- Define abbreviations either inside a small legend strip or in the caption, not
  repeatedly inside nodes.
- Keep formulas out of legends unless the legend is explicitly mathematical.
