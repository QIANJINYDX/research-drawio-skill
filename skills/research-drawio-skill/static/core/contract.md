# Flowchart Contract Before Drawing

A publication-style research flowchart is a compact visual argument. It should
show what happens, why the steps matter, and how the logic supports the paper's
claim. Establish this contract before creating shapes or styling.

## Required Contract

Use this template in working notes:

```text
Scientific message:
Diagram role:
Target output:
Final size:
Archetype:
Reading direction:
Grid/layout plan:
  columns:
  rows:
  gutters:
  routing corridors:
Composite elements:
  entity:
  visual glyph:
  primitives:
  grouping:
  semantic encoding:
Panel/page map:
Node map:
  module:
  node:
  scientific role:
Edge map:
  source -> target:
  meaning:
  route:
  bend count:
  direct route considered:
  label placement:
Math labels:
  formula:
  draw.io delimiter:
  fallback plain label:
Visual vocabulary:
  colors:
  shapes:
  icons:
  labels:
Export bundle:
Reviewer risk:
```

## Scientific Message Rules

- Write one sentence with a verb: "Single-cell preprocessing feeds a foundation
  model that identifies perturbation-specific cell states", not "workflow".
- Every node must answer a unique procedural or scientific question. If removing
  a node would not weaken the flowchart, remove or merge it.
- Use modules to separate evidence levels: sample/material input, processing,
  model/analysis, validation, and output.
- Make arrow meaning explicit: sequence, transformation, information flow,
  causal link, feedback, filtering, or comparison.
- Plan grid coordinates before drawing: module bounds, aligned node columns,
  row baselines, and connector corridors must be known before edges are added.
- Decide which scientific entities should become editable composite glyphs
  rather than plain text boxes. Use glyphs for concrete structures, data
  patterns, charts, biological entities, model modules, and instruments.
- Keep formula cells separate from busy connector regions. Scientific equations
  should sit in reserved whitespace or a dedicated formula strip.
- If the user provides a manuscript paragraph, derive the node map from the
  paragraph's logic rather than copying sentences into boxes.

## Diagram Logic

Use this order unless the manuscript story clearly requires another:

1. Establish the system: sample, cohort, model, device, material, or dataset.
2. Show the main workflow or mechanism.
3. Show the decision/branch/control structure only where it matters.
4. Show the output, validation, or biological interpretation.
5. Add feedback loops, secondary assays, or deployment steps only if they are
   part of the scientific claim.

For figure panels, one flowchart can serve as the hero panel. Supporting panels
should validate or quantify the flowchart, not repeat the same information.

## Layout Contract

- Choose a grid unit before authoring, usually 10 or 20 px.
- Use equal widths for nodes in the same semantic tier.
- Use shared x coordinates for vertical lanes and shared y coordinates for
  horizontal lanes.
- Reserve at least 24 px of whitespace between node bodies and connector
  corridors; use 40-60 px gutters between modules in dense architecture figures.
- Route edges after all nodes are placed. If a connector crosses a label or
  shape, move the node or reroute the edge before styling.
- Put long edge labels in separate text cells near the route; do not rely on
  connector labels when the edge is long or bends around modules.

## Composite Element Contract

- Use at least one semantic visual glyph when the diagram describes a concrete
  object, data structure, chart, biological system, or model architecture.
- Compose glyphs from editable draw.io primitives: rectangles, ellipses,
  cylinders, lines, curves, tiled cells, and connectors.
- Group child primitives under a clear parent cell or stable ID prefix.
- Keep text outside or below the glyph when possible. The glyph should carry
  visual meaning; the label should name it.
- Avoid decorative iconography. Every primitive should encode structure,
  category, quantity, modality, or direction.
- Never place ordinary labels over glyph primitives. Put labels outside the
  glyph or reserve a deliberate blank label zone.
- Use chart-like glyphs only when the underlying node is quantitative or
  comparative. If no metric exists, use a structural glyph instead.
- Keep glyphs on the same grid and reserve connector-free padding around them.

## Reviewer-Risk Prompts

Ask what a skeptical reviewer would challenge:

- Is the input material or dataset clearly defined?
- Are transformations and filters traceable?
- Are branches, controls, and validation steps visually distinct?
- Does the diagram imply causality where the evidence is only procedural?
- Are abbreviations expanded or defined nearby?
- Does the figure include semantic visual glyphs where plain text boxes would be
  too abstract?
- Are composite glyphs editable and built from draw.io primitives rather than
  raster images?
- Do chart-like glyphs represent an actual metric, comparison, or data pattern
  rather than arbitrary decorative bars?
- Are labels separated from glyph primitives with enough whitespace?
- Are formulas rendered through draw.io mathematical typesetting rather than
  shown as unparsed code-like text?
- Do any connectors pass through node text, formula labels, matrix cells, or
  module headers?
- Could any multi-bend connector be replaced with a direct or one-bend route?
- Could the same message be delivered with fewer nodes or less color?
- Will text remain editable and readable after journal-size export?
