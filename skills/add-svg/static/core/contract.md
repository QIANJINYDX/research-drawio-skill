# SVG Addition Contract

Adding SVGs to a scientific draw.io figure is a visual-argument task. The SVG
must clarify a mechanism, object, model component, assay, or data structure; it
must not merely decorate the diagram.

## Mandatory Source Gate

Every invocation must ask the user:

```text
SVG 来源选择：网络搜索，还是自行绘制？
```

Stop until the user answers. This gate is part of the contract, not optional
clarification.

## Required Contract

After the source gate is answered, create working notes:

```text
Scientific message:
Target draw.io file:
SVG role:
Source mode:
Needed concepts:
  concept:
  scientific role:
  preferred visual form:
Candidate plan:
  network candidates per concept:
  self-designed fallbacks:
Integration targets:
  page:
  module:
  x/y/width/height:
  connector relationship:
Replacement plan:
  existing primitive glyphs to remove:
  labels or connectors to preserve:
  compact reflow after insertion:
Style constraints:
  palette:
  line weight:
  label placement:
License/provenance:
Fallback plan:
QA checks:
```

## Scientific Rules

- Every SVG must map to a scientific role: sample, assay, molecule, model,
  database, instrument, pathway, output, validation, or mechanism.
- Delete or skip SVGs that do not improve the figure's argument.
- Prefer fewer, clearer SVG elements over a visually busy icon collection.
- Keep SVGs compatible with the existing diagram's palette, typography, grid,
  and connector logic.
- When an SVG is inserted as the glyph for a concept, remove or skip any
  duplicate self-drawn primitive glyph for the same concept unless the user
  explicitly requests a hybrid editable reconstruction.
- After replacing primitives with SVGs, reflow the affected module so stale
  placeholder space does not create excessive whitespace.
- If a network SVG has unclear license or provenance, keep it as a candidate
  only; do not embed it as the final asset unless the user accepts the risk.
