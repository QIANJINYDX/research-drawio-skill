# Default Operating Stance

## Philosophy

Start from topology, then style. A good research flowchart has a clear reading
path, a disciplined visual vocabulary, and enough restraint that the reviewer can
audit the science rather than decode decoration.

## Stance

- Prefer one dominant reading direction: left-to-right for pipelines and
  top-to-bottom for protocols or cohort flow.
- Use a hero module when one step carries the main scientific idea, then make
  setup and validation visually quieter.
- Build a layout blueprint before drawing: modules, nodes, formulas, matrices,
  legends, and connector corridors each get reserved space.
- Prefer semantic glyphs over text-only nodes for concrete scientific entities.
  A DNA step should look like a small editable DNA glyph; a quantitative-result
  step can show mini axes and bars; a model step can show layers or matrices.
- Keep the background white. Use tinted module bands or light containers only to
  group related steps.
- Use one neutral family, one signal family, and one accent family. Reserve red
  and green for signed meaning such as exclusion/inclusion, loss/gain, or
  negative/positive controls.
- Prefer direct labels over detached legends. Use a legend only when symbols or
  colors recur across several modules.
- Use icons sparingly and only when they identify real entities such as sample,
  sequencing, model, microscope, patient, or database. Prefer building these
  identifiers from draw.io primitive shapes instead of inserting raster icons.
- Keep shape semantics stable: process rectangles, data/document shapes,
  decision diamonds only for true branching, database cylinders only for stored
  data, and output shapes only for final results.
- Group composite glyphs and treat them as first-class nodes. Connectors attach
  to the group boundary or an intentional port, not to random internal shapes.
- Keep text and glyph primitives in separate zones. A label may name a glyph,
  but it should not sit on top of bars, bases, matrix tiles, cells, or network
  nodes.
- Use orthogonal connectors with explicit waypoints by default. Avoid crossing
  arrows; if a crossing or label collision appears, revise the layout before
  styling.
- Prefer no waypoint for adjacent aligned nodes and one bend for simple
  orthogonal turns. Use multiple bends only to avoid a named obstacle.
- Do not place connector text on top of long routed edges. Prefer small,
  frameless label cells positioned in whitespace.
- Use draw.io mathematical typesetting for equations. Formula source belongs in
  dedicated text cells with MathJax delimiters, not inside crowded process boxes.
- Make labels short noun phrases or verb phrases. Long manuscript prose belongs
  in the caption, not inside nodes.
- Treat exportability as part of the design: editable text, vector shapes,
  readable line weights, and journal-size type are required, not cleanup.

## Privacy Rule

Do not disclose private local paths, private filenames, attachment names, or
internal template provenance in user-facing replies, diagram labels, captions, or
comments unless the user explicitly asks for that audit trail.
