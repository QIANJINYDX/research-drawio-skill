# Composite Elements from Draw.io Primitives

Use this reference whenever a diagram risks becoming all text, or when a node
represents a concrete scientific object, data structure, biological entity,
chart, instrument, or model component.

## Core Rule

Before drawing a plain process box, ask:

```text
Can this node be shown as a small editable glyph that carries scientific meaning?
```

Use a composite glyph when the answer is yes. Build it from draw.io primitives
such as rectangles, ellipses, cylinders, lines, curves, tiled cells, and simple
connectors. Keep the glyph editable and grouped.

If a dedicated SVG has already been inserted for the same entity, treat that SVG
as the entity glyph and skip the primitive reconstruction unless the user asks
for a hybrid editable version. Do not show both an SVG icon and a self-drawn
primitive glyph for the same concept by default.

## When to Use Composite Glyphs

| Scientific entity | Composite glyph idea |
|---|---|
| Quantitative result | Mini axes + bars, line, points, or confidence band |
| DNA/RNA/sequence | Paired circles or short rounded rectangles on two rails |
| Matrix/attention/omics table | Tiled rectangles with low-saturation fills |
| Neural network/model | Layer blocks, circles, or matrix stack connected by thin lines |
| Cell/sample | Ellipse/circle body + nucleus/internal markers |
| Tissue/organ section | Irregular or rounded region + sparse internal dots |
| Database/dataset | Cylinder or stacked cards with small table marks |
| Sequencing/assay | Sample glyph + arrow + read/barcode strips |
| Microscope/imaging | Lens/circle + image tile, kept very abstract |
| Cohort/groups | Human/sample dots arranged in rows, with count labels nearby |

Do not use a glyph when it would add ambiguity or when the concept is purely
procedural and a labeled process node is clearer.

## General Construction Rules

- Use 3-12 primitives for most glyphs. Use more only for matrix tiles, dot
  cohorts, or repeated sequence motifs.
- Keep primitives on a 5 or 10 px internal grid.
- Use one parent group or a shared ID prefix, such as `glyph-dna-*`.
- Keep a transparent bounding rectangle if external connectors need a clean
  target.
- Put the label outside the glyph: below, above, or to the right. Leave at least
  6-10 px of padding between label text and glyph primitives.
- After replacing a primitive glyph with an SVG, move the label and module bounds
  to reclaim the old primitive-glyph area instead of leaving empty space.
- Do not place ordinary text on top of primitives. The only exceptions are
  intentional symbolic marks such as base letters, channel names, or compact
  panel labels placed in reserved blank space.
- Keep connectors outside the glyph interior unless the connector explains an
  internal mechanism.
- Use the figure palette. Avoid bright cartoon colors.

## Bar-Chart Miniature

Use for performance, expression, abundance, or comparison outputs. Do not use a
bar-chart miniature as a generic "result" decoration.

Primitive plan:

```text
transparent bounding box
x-axis line
y-axis line
3-5 filled rectangles as bars
optional highlighted bar
short label outside glyph
```

Draw.io style examples:

```text
Axis line:
endArrow=none;html=1;rounded=0;strokeColor=#4D5E6E;strokeWidth=1;

Neutral bar:
rounded=0;whiteSpace=wrap;html=1;fillColor=#D7E1EA;strokeColor=#4D5E6E;

Signal bar:
rounded=0;whiteSpace=wrap;html=1;fillColor=#0F4D92;strokeColor=#0F4D92;
```

Rules:

- Use this glyph only when the node has a real metric, comparison, abundance,
  expression, score, or other quantitative meaning.
- If exact data are unavailable, make the pattern qualitative and explain what
  the relative heights encode. If no such explanation exists, choose another
  glyph type.
- Do not include numeric axes unless the glyph is a real plot panel.
- Align bar bottoms exactly on the x-axis.
- Use the highlighted bar only when it maps to a method or finding.
- Avoid arbitrary decorative heights. A reviewer should be able to ask "what do
  these bars mean?" and receive a clear answer.

## DNA / RNA Chain

Use for sequence input, gene editing, motif discovery, regulatory DNA, or RNA
design.

Primitive plan:

```text
two thin curved/segmented rails
paired circles or short rounded rectangles as bases
small cross-links between paired bases
optional highlighted motif segment
label outside glyph
```

Practical draw.io version:

- Use 6-10 pairs of small circles or rounded rectangles.
- Alternate y positions to imply a helix instead of drawing a complex spline.
- Connect paired bases with thin neutral lines.
- Highlight a motif with one signal color, not every base.

Suggested primitives:

```text
Base circle:
ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#F7F9FC;strokeColor=#4D5E6E;

Highlighted base:
ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EAF2FB;strokeColor=#0F4D92;

Base-pair link:
endArrow=none;html=1;rounded=0;strokeColor=#D7E1EA;strokeWidth=1;
```

## Matrix / Heatmap / Attention Map

Use for attention weights, confusion matrices, omics heatmaps, embedding tables,
or feature maps.

Primitive plan:

```text
transparent bounding box
3 x 3 to 6 x 6 tiled rectangles
low-saturation sequential or diverging fills
optional row/column labels outside tiles
```

Rules:

- Keep matrix cells small and aligned.
- Do not route connectors through matrix tiles.
- Use opacity or lightness to show magnitude, not rainbow hues.
- If the matrix is only illustrative, avoid numbers inside cells.
- Keep labels outside the tile grid; do not overlay text on cells.

## Neural Network / Graph

Use for model blocks, message passing, cell-cell communication, or feature
aggregation.

Primitive plan:

```text
2-4 vertical layers of circles
thin connectors between adjacent layers
optional highlighted path
short label outside glyph
```

Rules:

- Use no more than 3-5 nodes per layer in a manuscript flowchart glyph.
- Avoid dense all-to-all lines unless the point is dense connectivity.
- Put the model equation in a separate formula cell.

## Cell / Sample Glyph

Use for cells, nuclei, perturbations, tissue spots, organoids, or patient samples.

Primitive plan:

```text
large ellipse/circle body
smaller nucleus/internal marker
1-3 small dots or marks for phenotype/channel
optional outline or fill color for condition
```

Rules:

- Keep biological glyphs abstract and restrained.
- Use shape and label to avoid relying only on color.
- Do not imply microscopy realism unless the figure is actually an image plate.

## Grouping Pattern

Preferred XML strategy:

```text
glyph parent: id="glyph-entity", style="group", vertex="1", connectable="0"
children: id="glyph-entity-part-*", parent="glyph-entity"
connector target: transparent boundary cell or named port
label: separate text cell outside the group
```

If a target draw.io workflow handles grouped geometry poorly, keep all child
cells at page level with a shared prefix and add a transparent rounded rectangle
as the connector target.

## Anti-Patterns

- A process diagram made entirely of text boxes when the topic has visible
  scientific entities.
- Decorative icons that do not encode any scientific structure.
- Arbitrary bar charts, line charts, or dot plots with no metric or scientific
  interpretation.
- Text labels overlapping bars, bases, cells, matrix tiles, network nodes, or
  other glyph primitives.
- Raster images pasted into an otherwise editable draw.io figure.
- SVG image cells and duplicated draw.io primitive glyphs representing the same
  concept side by side without a stated comparison purpose.
- Composite glyphs with so many primitives that the figure becomes hard to edit.
- External arrows attached to a random internal base, bar, dot, or tile.
