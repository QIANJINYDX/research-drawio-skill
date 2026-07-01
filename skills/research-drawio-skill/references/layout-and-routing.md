# Layout and Connector Routing

Use this reference before creating or repairing dense scientific diagrams,
especially model architectures, attention mechanisms, graphical abstracts, and
multi-module pipelines.

## Layout Before Drawing

Create a layout blueprint before writing `.drawio` cells:

```text
Canvas:
  page width:
  page height:
  grid unit:
Modules:
  name:
  x/y/width/height:
Rows:
  baseline y:
  nodes:
Columns:
  baseline x:
  nodes:
Routing corridors:
  horizontal:
  vertical:
Protected zones:
  formulas:
  matrix tiles:
  legends:
  module headers:
```

Rules:

- Use a 20 px placement grid for nodes and modules; use a 10 px grid only for
  small tiles or ports.
- Align peer nodes to shared x or y coordinates. Avoid "almost aligned" values.
- Use equal node sizes within a lane unless visual hierarchy requires otherwise.
- Reserve 40-60 px gutters between major modules and at least 24 px between a
  node body and any connector corridor.
- Place formulas and legends in protected zones with no connector traffic.

## Routing Corridors

Treat connectors as layout objects:

- Draw nodes first, then edge routes.
- Route connectors through empty horizontal or vertical corridors.
- Use the simplest connector that preserves clarity:
  - 0 explicit waypoints for adjacent aligned nodes.
  - 1 explicit waypoint for a simple L-shaped turn.
  - 2 explicit waypoints for a single obstacle detour.
  - More than 2 waypoints only when there is a named, unavoidable obstacle.
- Use orthogonal connectors with explicit waypoints only when the route is
  non-trivial. Do not add waypoints by habit.
- Do not route edges through node interiors, text labels, formula cells, matrix
  tiles, legends, or module headers.
- If an edge needs a long detour, place the route outside the module group
  rather than between tightly packed labels.
- If several edges share a corridor, separate them by at least 8-12 px.
- Remove micro-jogs shorter than one grid unit and redundant collinear
  waypoints. They create visual noise without improving routing.

Preferred edge style:

```text
edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#4D5E6E;strokeWidth=1.2;
```

## Direct-First Routing

Before finalizing each edge, test routes in this order:

1. Direct edge with no explicit waypoint.
2. Single-bend orthogonal route through an open corridor.
3. Two-bend detour around a protected zone.
4. Multi-bend route only when the contract names the obstacle being avoided.

If a direct or one-bend route does not cross a protected element, use it. A
visually clean line is usually better than a technically elaborate route.

## Edge Labels

Use connector labels only for short, straight edges. For long, bent, or crowded
edges:

- Keep the edge `value=""`.
- Add a separate text cell near the edge in open whitespace.
- Align all route labels in the same corridor to a shared baseline.
- Keep label cells away from arrowheads and formula cells.

## Dense Model Diagrams

For transformer, attention, neural network, or computational architecture
figures:

- Use a central hero computation block and peripheral data rails.
- Keep tensors or matrices as compact visual glyphs; do not let their internal
  grid fight with connector routes.
- Put the main equation in a formula strip below or above the hero block.
- Route value/content streams on a separate lane from similarity/weight streams.
- Use color to encode stream identity, but keep all routes spatially separated.

## Revision Checklist

Before styling, inspect the raw layout:

- Are all peer nodes exactly aligned?
- Can the eye follow the main route without reading labels?
- Does every connector have a clear corridor?
- Does every connector use the fewest bends needed?
- Are there any micro-jogs that could be removed?
- Are formulas and matrix tiles protected from connector traffic?
- Would moving one module remove multiple edge crossings?

Only after this passes should color, font, and polish be finalized.
