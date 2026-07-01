# Draw.io SVG Integration

Use this file before editing a `.drawio` file or inserting SVG assets.

## Integration Principles

- Preserve existing pages, IDs, groups, and unrelated geometry.
- Insert SVG as a draw.io image cell when the SVG should remain a single asset.
- Rebuild it from draw.io primitives only when editability of subparts matters.
- Keep labels outside the SVG unless the label is part of the symbol.
- Do not let SVGs overlap text, connectors, formulas, or existing glyphs.
- Place SVGs on the same grid and inside the same visual hierarchy as the
  target diagram.
- Treat an inserted SVG as the final visual glyph for its concept. Remove the
  previous draw.io primitive glyph for that same concept unless the user asks
  for both representations.

## Replacement and Compaction

Before inserting SVGs into an existing diagram, list the old visual cells that
represent the same concept:

```text
concept:
  inserted SVG cell:
  old primitive glyph cells:
  labels to keep:
  connectors to keep or reattach:
  compaction move:
```

After insertion:

- Delete duplicate primitive glyphs that encode the same object already shown by
  the SVG.
- Preserve labels, scientific annotations, connector semantics, and provenance
  notes unless they become redundant.
- Recenter the SVG inside the module and move labels toward it so the module no
  longer contains an empty former-glyph zone.
- Shrink or reposition modules when removed primitives create large unused
  regions, while preserving a readable 8-12 px clearance around SVGs and text.
- Use direct connectors first after reflow; do not keep old detour routes that
  were only needed to avoid removed primitives.

## Data URI Image Cell

For a local SVG file, use `scripts/svg_data_uri.py` to create a draw.io-safe
data URI:

```bash
python skills/add-svg/scripts/svg_data_uri.py path/to/icon.svg
```

Use the script output directly in the `image=` style field. It URL-encodes the
SVG source so that draw.io reads the full image value as one style field.

Do not write a raw base64 SVG URI such as
`image=data:image/svg+xml;base64,...` inside a draw.io style string. mxGraph
styles are separated by semicolons, so the semicolon in `svg+xml;base64`
truncates the `image=` value and the SVG will not render. If authoring manually,
use `data:image/svg+xml,` followed by percent-encoded SVG XML, or otherwise
escape every style-breaking character before insertion.

Then insert an image cell:

```xml
<mxCell id="svg-cell-1" value="" style="shape=image;html=1;image=data:image/svg+xml,%3Csvg%20...%3E;aspect=fixed;imageAspect=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="64" height="64" as="geometry"/>
</mxCell>
```

After insertion, inspect the style string: `image=` must contain no unescaped
semicolon before the next draw.io style key such as `aspect=` or `strokeColor=`.

Then export a preview through `research-drawio-skill` when available:

```bash
python skills/research-drawio-skill/scripts/export_drawio_preview.py path/to/figure.drawio --formats png svg
```

The preview must show the SVG visibly rendered. If the SVG appears in XML but
not in the exported PNG/SVG, treat the insertion as failed and repair the data
URI encoding, SVG source, image-cell style, or geometry before delivery.

## Candidate Storage During Execution

When executing the skill, store downloaded or self-designed SVGs in a local
working folder such as:

```text
assets/svg-candidates/<concept>/
```

Also create a short candidate index, for example:

```text
assets/svg-candidates/candidates.md
```

Do not create this folder in the skill package itself unless the user is
explicitly developing the skill.

## Layout Rules

- SVG should not become the dominant panel unless it is the requested hero
  schematic.
- Leave at least 8-12 px between SVGs and labels; more for dense diagrams.
- Route connectors to SVG boundary boxes or named ports, not to visual details.
- Match stroke width and color saturation to the existing figure.
- Use the target diagram's source-data/attribution notes when relevant.
- If the page has obvious unused whitespace after SVG insertion, reduce the
  canvas or tighten the module spacing before delivery.
- Re-export the preview after reflow; do not rely on stale previews from before
  SVG insertion or compaction.
