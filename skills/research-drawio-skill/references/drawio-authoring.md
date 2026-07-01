# Draw.io / mxGraph Authoring

Use this when creating or editing `.drawio` files directly.

## Source Format

Prefer uncompressed diagrams.net XML for generated files:

```xml
<mxfile host="app.diagrams.net">
  <diagram id="diagram-1" name="Figure">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="1" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Each visible shape is an `mxCell` with `vertex="1"` and an `mxGeometry`.
Each connector is an `mxCell` with `edge="1"`, `source`, `target`, and relative
geometry.

## Authoring Rules

- Use stable, descriptive IDs such as `node-sample-input`, `edge-preprocess-model`,
  or `group-validation` when generating new diagrams.
- Escape XML-sensitive characters in labels: `&`, `<`, `>`, and quotes.
- Use `html=1` labels for controlled line breaks (`<br>`) and simple emphasis
  (`<b>...</b>`), but keep labels short.
- Keep geometry on a clean grid. Align nodes by shared `x`, `y`, width, and
  height values rather than eyeballing.
- Write all nodes first, then connectors. Do not create connectors until module
  bounds, node positions, formula cells, and route corridors are fixed.
- Use parent-child relationships for grouped modules only when the group should
  move as a unit. Otherwise use background containers behind normal cells.
- For semantic glyphs, create a parent group cell or use a stable ID prefix for
  all child primitives, then keep connectors attached to the group boundary or a
  named port. Do not connect external arrows to arbitrary internal decorative
  primitives.
- Keep connectors attached to source/target IDs, not loose line segments.
- Use explicit `mxPoint` waypoints for any connector that is not a simple
  adjacent left-to-right or top-to-bottom edge.
- Keep edge labels empty for long or bent connectors. Use separate text cells
  for relationship labels so labels can be aligned and protected from overlap.
- Do not encode long captions inside the diagram. Put caption prose in the
  response or a separate legend draft.

## Minimal Vertex

```xml
<mxCell id="node-preprocess" value="Preprocess&lt;br&gt;data" style="rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#F7F9FC;strokeColor=#4D5E6E;fontColor=#1F2933;fontFamily=Arial;fontSize=11;spacing=8;" vertex="1" parent="1">
  <mxGeometry x="220" y="120" width="120" height="54" as="geometry"/>
</mxCell>
```

## Minimal Edge

```xml
<mxCell id="edge-input-preprocess" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;orthogonalLoop=1;jettySize=auto;strokeColor=#4D5E6E;strokeWidth=1.2;" edge="1" parent="1" source="node-input" target="node-preprocess">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Formula Cell

Enable math in the graph model (`math="1"`) and use MathJax delimiters inside a
text cell:

```xml
<mxCell id="formula-attention" value="\( \mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^{\mathsf T}/\sqrt{d_k})V \)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Arial;fontSize=12;fontColor=#1F2933;spacing=4;" vertex="1" parent="1">
  <mxGeometry x="420" y="460" width="320" height="42" as="geometry"/>
</mxCell>
```

## Grouped Composite Glyph

Use a group parent when a visual element is made from multiple primitives:

```xml
<mxCell id="glyph-dna" value="" style="group" vertex="1" connectable="0" parent="1">
  <mxGeometry x="120" y="140" width="120" height="80" as="geometry"/>
</mxCell>
<mxCell id="glyph-dna-backbone-a" value="" style="shape=partialRectangle;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#4D5E6E;" vertex="1" parent="glyph-dna">
  <mxGeometry x="10" y="10" width="100" height="60" as="geometry"/>
</mxCell>
```

If grouping makes connector behavior difficult in a target environment, keep
the child cells at page level with a shared prefix (`glyph-dna-*`) and create a
transparent bounding rectangle as the connector target.

## Editing Existing Files

- Parse XML with a real XML parser when possible. Avoid broad regex edits.
- Preserve pages, diagram names, and unrelated cells.
- Before rewriting, identify whether the diagram is plain XML or compressed data
  inside the `<diagram>` element. If compressed and no reliable decoder is
  available, report the blocker and make a copy before attempting repair.
- Keep an original backup when the edit is structural or destructive.
- After editing, verify the file opens in diagrams.net or render/export it if the
  local environment supports that.
- Run `scripts/qa_drawio.py path/to/file.drawio` when available. Fix XML,
  grid-alignment, missing endpoint, and connector-through-node warnings before
  final delivery.

## Export Notes

- SVG is the primary publication preview because it keeps vector shapes and
  editable text in many downstream tools.
- PDF is useful for submission packages and print checks.
- PNG is for quick preview only unless a journal specifically requests raster.
- Inspect exports for clipped labels, missing fonts, detached arrows, off-canvas
  objects, and unexpected rasterization.
