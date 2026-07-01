# Complex Asset Sourcing

Use this file when tracing or redrawing objects that are difficult to represent
faithfully with simple draw.io primitives.

## Complex Object Test

Treat an object as complex when any condition is true:

- It must be recognizable by silhouette, such as a cat, dog, mouse, organ,
  microscope, scanner, lab animal, protein cartoon, or anatomy icon.
- Hand-drawn primitives would need more than about 12 shapes to look acceptable.
- A crude primitive sketch changes the scientific meaning or visual class.
- The object is a repeated icon where inconsistency would be obvious.
- The user asks for online materials, assets, icons, SVGs, or reference
  elements.

## Decision

Use this order:

1. If the user explicitly requests online assets, use `add-svg` network mode.
2. If the object fails the complex object test, ask or invoke the `add-svg`
   source gate and prefer network search.
3. If search results are absent, legally unclear, too detailed, or inconsistent
   with the figure style, create a simple self-designed fallback and record it.
4. If the object is simple and abstract, draw it with primitives.

## Network Search Contract

When using online assets, use the local `add-svg` skill:

- Follow its mandatory source gate.
- Search for multiple SVG/vector candidates.
- Prefer public-domain, CC0, permissive Creative Commons, or clearly reusable
  sources.
- Record source URL, direct SVG URL when available, license, attribution needs,
  style fit, and risks.
- Store candidates in `assets/svg-candidates/<concept>/`.
- Insert selected SVGs as URL-encoded `data:image/svg+xml,` image cells.
- Do not use raw `data:image/svg+xml;base64,...` in draw.io style strings.

## Replacement Rule

An inserted SVG/vector asset becomes the visual glyph for that concept. Remove
or skip duplicate primitive sketches for the same concept unless the user asks
for a side-by-side comparison.

## Placement Rule

For traced PNG figures:

- Put the selected asset in the same bbox as the reference object.
- Preserve the reference object's approximate scale and baseline.
- Keep labels outside the SVG body.
- Route connectors to the asset boundary, not to internal visual details.
- Re-run the consistency loop after insertion.

## Candidate Note Format

```text
Concept:
Why primitive drawing is insufficient:
Source mode:
Candidates:
  name:
  source URL:
  direct SVG URL:
  license:
  attribution:
  style fit:
Selected asset:
Fallback:
Draw.io cell:
Duplicate primitive removal:
```
