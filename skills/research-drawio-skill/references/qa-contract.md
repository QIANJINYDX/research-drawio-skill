# Research Flowchart QA Contract

Use this before final delivery, export, or reviewer-facing revision.

## Logic QA

| Check | Pass condition |
|---|---|
| Scientific message | One-sentence message exists and the diagram supports it |
| Node necessity | Every node carries unique procedural or scientific meaning |
| Edge meaning | Arrows indicate sequence, transformation, causality, filtering, or feedback clearly |
| Visual entities | Major scientific objects are represented by semantic glyphs when visual structure is useful |
| Branch logic | Decisions, exclusions, controls, and alternatives are visually distinct |
| Abbreviations | Abbreviations are defined once in labels, legend, or caption |
| Reviewer risk | The diagram does not overclaim causality or hide key controls |

## Visual QA

| Check | Pass condition |
|---|---|
| Reading path | The eye can follow the diagram without backtracking |
| Alignment | Nodes and modules share clean x/y coordinates and consistent sizes |
| Arrow crossings | Crossings are absent or rare and justified |
| Connector occlusion | No connector crosses text, formula cells, node bodies, matrix tiles, module headers, panel labels, or legends |
| Text/glyph separation | Labels do not cover bars, bases, cells, matrix tiles, network nodes, or other glyph primitives |
| Connector simplicity | Direct or one-bend routes are used whenever they do not cross protected elements |
| Color semantics | Each color has stable meaning and remains readable in grayscale |
| Typography | Text is readable at final size and remains editable |
| Formula rendering | Formulas use draw.io mathematical typesetting delimiters and the graph model has `math="1"` |
| Density | No node contains manuscript-length prose |
| All-text avoidance | The figure is not merely a collection of text boxes when the science has visual entities |
| Glyph editability | Composite elements are made from editable draw.io primitives and can be selected/revised |
| Glyph semantics | Chart-like glyphs encode actual metrics, comparisons, or data patterns rather than arbitrary decoration |
| Style restraint | No decorative shadows, glossy gradients, clip art, or unused icons |

## Draw.io Integrity QA

| Check | Pass condition |
|---|---|
| Source file | `.drawio` source is present when a diagram is created from scratch |
| XML validity | XML parses without errors |
| Connectors | Edges are attached to source and target cells |
| Routing | Explicit waypoints are used when edges need to pass around other elements |
| Bend count | Connectors have no redundant waypoints, avoid micro-jogs, and use the minimum practical bend count |
| Canvas | No important object is off-canvas or clipped |
| Grouping | Module containers do not trap unrelated elements |
| Exports | SVG/PDF/PNG exports open and match the source layout |

## Required Local QA for Generated Draw.io Files

When Python is available, run:

```bash
python skills/research-drawio-skill/scripts/qa_drawio.py path/to/figure.drawio
```

Treat any `ERROR` as blocking. Treat `WARN` as a reason to inspect and revise
the layout unless the warning is clearly explained by the intended design.

## Export Bundle

For publication-oriented work, deliver or prepare:

```text
editable source: figure.drawio
primary preview: figure.svg
optional print: figure.pdf
optional quick preview: figure.png
notes: scientific message, archetype, abbreviations, and reviewer-risk flags
```

If local export tooling is unavailable, still provide the `.drawio` source and
explain the exact missing step needed to export.
