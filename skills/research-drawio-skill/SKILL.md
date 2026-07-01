---
name: research-drawio-skill
description: >-
  Create, revise, audit, and export publication-style scientific flowcharts and
  schematic workflows in diagrams.net/draw.io. Use for research-paper
  flowcharts, Nature-style workflows, graphical abstracts, method pipelines,
  experimental design, cohort/study flow, mechanism schematics, model
  architecture, editable .drawio files, and SVG/PDF-ready scientific diagrams,
  including 科研流程图, 论文流程图, draw.io作图, 方法流程图, 实验设计图, 技术路线图,
  机制示意图, and 图形摘要. Start from a scientific message, topology, grid
  layout, semantic composite-element plan, collision-free routing, math-label
  contract, export contract, and reviewer-risk check. Build editable glyphs
  from draw.io primitives, such as bar miniatures, DNA helices, matrices,
  neural networks, cells, samples, and model blocks. Enforce alignment,
  non-overlap, readable labels, and MathJax formulas. Not for dashboards,
  generic business diagrams, or illustration-first artwork.
---

# Research Draw.io Skill

Build scientific flowcharts as visual arguments, not decorative process maps.
The diagram must make a paper's method, mechanism, cohort flow, model
architecture, or analytical logic easier to review.

This skill mirrors the `nature-figure` philosophy: first define the scientific
claim and evidence hierarchy, then choose the minimum diagram structure, then
engineer the layout and connectors, then apply restrained journal style and
export QA.

The output should not be an all-text box diagram when the topic has visual
entities. Use editable draw.io primitives to build semantic glyphs for the key
scientific objects, while keeping labels short and reviewable.

## Routing Protocol

Follow these steps whenever the skill is invoked.

### 1. Load the manifest and core layer

Read [manifest.yaml](manifest.yaml). Then read every file listed under
`always_load`:

- `static/core/contract.md`
- `static/core/stance.md`

Do not draw from memory or from a favorite template before the contract exists.
If the diagram contains formulas, load `references/math-typesetting.md` before
authoring any formula labels.
If the diagram contains biological structures, charts, tensors, model modules,
or other visual entities, load `references/composite-elements.md` before drawing
those entities.

### 2. Establish the diagram contract before authoring

Create a compact working contract:

1. Scientific message: the one-sentence point the flowchart must defend.
2. Diagram role: method overview, experimental workflow, cohort flow, mechanism,
   analytical pipeline, graphical abstract, or hybrid figure panel.
3. Topology: ordered nodes, grouped modules, edge meanings, branches, loops, and
   inputs/outputs.
4. Layout blueprint: rows, columns, modules, gutters, and connector corridors.
5. Composite-element plan: which nodes become grouped visual glyphs, which
   draw.io primitives compose them, and what each primitive means.
6. Visual vocabulary: colors, shapes, icons, and labels that map to scientific
   entities rather than decoration.
7. Math contract: formula cells, MathJax delimiters, and fallback plain labels.
8. Export contract: target size, editable source, SVG/PDF needs, and review
   risks.

If the user provides only a topic, infer a provisional message and topology, then
make the uncertainty visible in the working notes or response.

### 3. Use draw.io as the default editable source

Use diagrams.net/draw.io `.drawio` as the source format unless the user asks for
another format. If no export format is specified, provide or prepare:

- `.drawio` editable source as the primary artifact.
- `.svg` as the primary publication/export preview.
- `.pdf` or `.png` only when requested or needed for submission/preview.

When editing an existing `.drawio`, preserve user content, page structure, IDs,
grouping, and geometry unless the requested redesign requires a change.

### 4. Engineer layout before connectors

Before writing edges, create a grid layout plan:

- Place modules on a strict column/row grid with consistent node sizes.
- Decide which major nodes should be visual glyphs instead of plain text boxes.
- Reserve empty routing corridors between modules and around formula blocks.
- Route connectors only through corridors, never through text-bearing shapes.
- Use the simplest valid connector: direct line first, one-bend orthogonal line
  second, multi-bend detour only when it avoids a real obstacle.
- Prefer separate label cells near connectors over text directly on long edges.
- Avoid crossings by changing geometry before adding style.

For detailed rules, load `references/layout-and-routing.md` whenever creating or
repairing a `.drawio` file.

### 5. Build semantic composite elements

Use grouped draw.io primitives when they clarify the science:

- Use bars + axes for a "quantitative result" or "metric comparison" glyph.
- Use paired circles + crossing rails for a DNA/RNA helix glyph.
- Use tiled rectangles for matrices, heatmaps, attention maps, or omics tables.
- Use circles connected by lines for neural networks, graphs, or cell-cell
  communication.
- Use ellipses/circles with internal marks for cells, nuclei, organelles, or
  samples.

Composite elements must be editable, grouped, and semantic. They are not clip
art. Each repeated primitive should encode a real object, category, feature, or
data structure. Do not draw arbitrary chart glyphs with invented values. For
detailed recipes, load `references/composite-elements.md`.

### 6. Classify the diagram archetype

Choose the closest archetype before layout:

- `experimental workflow`
- `computational pipeline`
- `study/cohort flow`
- `method architecture`
- `mechanism schematic`
- `multi-omics/data-integration workflow`
- `graphical abstract`
- `hybrid multi-panel flowchart`

Use one dominant archetype. Treat secondary archetypes as supporting modules, not
competing layouts.

### 7. Load references only when needed

Use the `references.on_demand` table in `manifest.yaml`.

| File | Open when |
|---|---|
| `references/archetypes.md` | Need to choose or combine flowchart archetypes |
| `references/style-guide.md` | Need typography, color, shape, arrow, spacing, and panel-label rules |
| `references/composite-elements.md` | Need editable grouped glyphs such as DNA, bar-chart miniatures, matrices, networks, cells, tissues, or model blocks |
| `references/layout-and-routing.md` | Need grid alignment, connector routing, collision avoidance, or dense model diagrams |
| `references/math-typesetting.md` | Need formulas, symbols, MathJax, or draw.io mathematical typesetting |
| `references/drawio-authoring.md` | Need to create or edit `.drawio`/mxGraph XML directly |
| `references/qa-contract.md` | Before final delivery, export, reviewer-facing audit, or journal submission |

## Operating Rules

- The scientific logic outranks style. Delete nodes and branches that do not
  carry a unique piece of evidence or procedural meaning.
- Prefer one clear reading path over a dense network. Use branches only for real
  alternatives, controls, or parallel assays.
- Draw the layout from a grid plan, not by eye. Nodes in the same semantic lane
  must share aligned x/y coordinates and dimensions.
- Avoid all-text diagrams. For each major scientific entity, ask whether it
  should be a grouped visual glyph made from draw.io primitives.
- Build composite glyphs from simple editable shapes, not raster icons. Group
  their child elements, use stable IDs, and keep a short label near the group.
- Keep labels outside glyph interiors unless the label is an intentional symbol
  such as A/C/G/T on a base or a channel mark. Text must not cover primitive
  shapes.
- Treat connector routing as a first-class design object. No connector may pass
  through a text label, formula cell, node body, matrix tile, or module title.
- Minimize connector bends. Remove micro-jogs and redundant waypoints before
  final delivery.
- Render mathematical notation through draw.io MathJax syntax: set `math="1"`
  in the graph model and use `\(...\)` or `$$...$$` delimiters.
- Use restrained journal style: white background, clean typography, subtle
  module grouping, consistent arrows, and low-saturation color families.
- Make text editable and readable at final print size. Avoid rasterized labels,
  decorative shadows, gradients, and clip-art-like icons.
- Run `scripts/qa_drawio.py` on generated uncompressed `.drawio` files when
  Python is available, then fix all reported layout or source-integrity issues.
- Keep a private working trail private. Do not expose private paths, filenames,
  internal template names, or provenance unless the user explicitly asks.
