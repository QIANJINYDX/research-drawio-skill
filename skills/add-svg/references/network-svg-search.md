# Network SVG Search Mode

Use this file only after the user chooses network search.

## Search Goal

Find multiple SVG candidates for each concept, then leave them for later user
selection. Do not silently choose one unless the user explicitly authorizes it.

## Search Procedure

1. Parse the requested concepts and their scientific roles.
2. Search the web for SVG-specific results.
3. Prefer sources with clear direct SVG files and license pages.
4. Collect 3-6 candidates per important concept when possible.
5. Record source URL, direct SVG URL, license/usage note, attribution needs, and
   style fit.
6. If no suitable result is found, mark the concept as `self-designed fallback`
   and design an original SVG.

## Candidate Table

Use this candidate handoff format:

```text
Concept:
Scientific role:
Candidates:
  1. name:
     source URL:
     direct SVG URL:
     license:
     attribution:
     style fit:
     risks:
  2. ...
Fallback:
```

## Search Query Patterns

Use targeted queries such as:

```text
<concept> svg icon
<concept> vector svg
<concept> schematic svg
<concept> scientific illustration svg
site:commons.wikimedia.org <concept> svg
site:svgrepo.com <concept> svg
site:openclipart.org <concept> svg
```

For manuscript figures, prefer scientific clarity over icon popularity.

## Licensing and Provenance

- Do not assume a random SVG is free to reuse.
- Prefer public domain, CC0, permissive Creative Commons, or project-specific
  open-license sources.
- Record attribution needs.
- If license is unclear, keep the asset in the candidate list but avoid final
  embedding until the user chooses.
- Do not copy logos, proprietary icons, or trademarked assets unless the user
  explicitly provides authorization.

## Fallback Rule

If search results are absent, low-quality, visually inconsistent, or legally
unclear, create a self-designed fallback SVG. Label it as original/self-designed
in the candidate handoff.
