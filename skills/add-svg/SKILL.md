---
name: add-svg
description: >-
  Add, collect, design, audit, and integrate SVG elements into editable
  diagrams.net/draw.io scientific figures. Use when the user asks to supplement
  a draw.io diagram with SVG icons, mechanisms, biological objects, model
  components, pathway symbols, instruments, graphical abstract elements, or
  publication-style vector assets. Every execution must first ask the user to
  choose the SVG source mode: network search or self-designed SVG. For network
  mode, search for multiple relevant SVG candidates for later user selection,
  record sources and license notes, and fall back to self-designed SVG for
  concepts with no suitable result. For self-design mode, create restrained,
  editable, Nature-style SVGs from simple vector primitives. Use with .drawio,
  SVG, diagrams.net, 科研流程图, 论文示意图, SVG补图, 图标补充, and draw.io配图.
---

# Add SVG Skill

Add SVG assets to draw.io research figures as evidence-aware visual elements,
not decorative stickers. This skill follows the `nature-figure` and
`research-drawio-skill` philosophy: establish the scientific message and visual
role first, decide the SVG source explicitly, then integrate only assets that
serve the diagram's logic and pass layout/export QA.

## Mandatory Source Gate

Before doing any SVG search, drawing, download, file edit, or draw.io insertion,
ask exactly one blocking question and stop:

```text
SVG 来源选择：网络搜索，还是自行绘制？
```

Do this on every invocation. Continue only after the user answers. The answer
sets `source_mode`:

- `network` / `网络搜索`: search the web for multiple SVG candidates.
- `self_design` / `自行绘制`: design new SVGs from vector primitives.

If the user already describes a preference in the same message, still confirm
briefly before execution unless the conversation already contains an explicit
answer to this exact source gate for the current invocation.

## Routing Protocol

1. Read [manifest.yaml](manifest.yaml).
2. Read every file listed under `always_load`:
   - `static/core/contract.md`
   - `static/core/stance.md`
3. Ask the mandatory source gate and wait for the user's answer.
4. Load the reference file for the chosen mode:
   - network search: `references/network-svg-search.md`
   - self design: `references/self-design-svg.md`
5. Load `references/drawio-svg-integration.md` before editing `.drawio`.
6. Load `references/svg-qa-contract.md` before final delivery.

## Core Workflow

After the source gate is answered, create a compact SVG contract:

```text
Scientific message:
Target draw.io file:
SVG role:
Source mode:
Needed concepts:
Candidate plan:
Integration targets:
Style constraints:
License/provenance notes:
Fallback plan:
QA checks:
```

## Network Mode

Search for multiple SVG candidates for each requested concept. Keep candidates
for later user selection rather than silently choosing one. For each candidate,
record:

- concept
- preview/name
- source URL
- direct SVG URL if available
- license or usage note
- style fit for Nature-style draw.io figures
- any required attribution

If no suitable SVG is found for a concept, mark it as `self-designed fallback`
and create a simple original SVG following `references/self-design-svg.md`.

## Self-Design Mode

Create original SVGs from simple vector primitives. Keep them restrained,
editable, and compatible with draw.io. Use one neutral family, one signal
family, and one accent family. Avoid complex illustration, gradients, shadows,
bitmap effects, and decorative detail.

## Draw.io Integration Rules

- Preserve the user's existing `.drawio` content and layout.
- Insert SVGs as editable/vector-friendly draw.io image cells when possible.
- Encode SVG image values as draw.io-safe URL-encoded `data:image/svg+xml,`
  URIs. Do not use raw `data:image/svg+xml;base64,...` inside `style=`, because
  the semicolon in `svg+xml;base64` breaks mxGraph style parsing.
- Treat an inserted SVG as the visual glyph for that concept. Do not also draw
  duplicate draw.io primitive glyphs for the same object unless the user asks for
  a hybrid editable reconstruction.
- After SVG insertion, re-balance the layout and remove empty placeholder zones
  so the figure remains compact rather than leaving the old self-drawn glyph
  space unused.
- Keep SVG labels separate from the icon body unless text is a scientific mark.
- Match the diagram's grid, spacing, color semantics, and connector rules.
- Run available QA checks and export a draw.io PNG/SVG preview when
  `research-drawio-skill/scripts/export_drawio_preview.py` is available. Do not
  treat XML validity as sufficient for SVG insertion; the exported preview must
  show the SVG assets rendered, nonblank, unclipped, and not overlapping labels.

## Related Files

| File | Open when |
|---|---|
| `references/network-svg-search.md` | User chooses network search |
| `references/self-design-svg.md` | User chooses self-designed SVGs or network search fails |
| `references/drawio-svg-integration.md` | Need to insert, encode, or edit SVGs in `.drawio` |
| `references/svg-qa-contract.md` | Before final delivery or candidate handoff |
| `scripts/svg_data_uri.py` | Need to convert a local SVG into a draw.io data URI |
