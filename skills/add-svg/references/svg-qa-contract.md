# SVG QA Contract

Use before final delivery, candidate handoff, or draw.io export.

## Source QA

| Check | Pass condition |
|---|---|
| Source mode | User explicitly chose network search or self-designed SVG |
| Provenance | Network candidates include source URL and license/usage notes |
| Candidate breadth | Multiple candidates are collected when network results exist |
| Fallback | Missing or unsuitable network results have self-designed fallbacks |
| License risk | Unclear or restrictive assets are not silently embedded as final |

## Visual QA

| Check | Pass condition |
|---|---|
| Scientific role | Each SVG has a clear role in the diagram's argument |
| Style match | Palette, line weight, and complexity match the draw.io figure |
| Text separation | Labels do not overlap SVG bodies |
| Layout | SVGs align to grid and do not block connectors or formulas |
| Scale | SVGs remain readable at final figure size |
| Restraint | No decorative stock-like icons, shadows, gradients, or clutter |
| No duplicate glyph | A concept represented by an inserted SVG is not also redrawn by redundant draw.io primitives |
| Compactness | Removed primitive-glyph space is reclaimed; the figure has no obvious stale placeholder zones |

## Draw.io QA

| Check | Pass condition |
|---|---|
| XML validity | `.drawio` parses after insertion |
| Cell placement | SVG image cells have stable IDs and geometry |
| Data URI encoding | SVG image styles use URL-encoded `data:image/svg+xml,` values, not raw `data:image/svg+xml;base64,...` values that contain an unescaped semicolon |
| Editability | SVG source is preserved or candidate files are retained |
| Export | SVG/PDF export keeps vector appearance where possible |
| Preview rendering | Exported PNG/SVG previews show inserted SVG assets visibly rendered, nonblank, unclipped, and not overlapping labels or connectors |
| Attribution | Required attribution is documented outside the figure body |
| Reflow | Connectors and labels are reattached or repositioned after old primitive glyphs are removed |

## Delivery Notes

When delivering, state:

```text
Source mode:
Candidate count:
Selected/inserted SVGs:
Self-designed fallbacks:
License/provenance notes:
QA performed:
Remaining user selection needed:
```

If `research-drawio-skill/scripts/export_drawio_preview.py` is available, include
the exported preview paths and state whether the SVGs rendered in the preview.
