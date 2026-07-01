# Consistency Loop

Use this file before final delivery for every traced draw.io figure.

## Goal

Close the gap between the raster reference and the editable draw.io redraw. For
GPT/imagegen/raster tracing where close imitation matters, strict pixel-level
comparison is a blocking delivery gate, not an optional note.

Do not stop after a single redraw if major layout, object, label, or route
differences remain. Do not explain away a failed strict comparison by saying the
final figure is editable, vectorized, formula-enhanced, or not intended as a
pixel replica. Those facts can guide the edits, but they do not convert a
failed comparison into a pass.

## Loop Contract

For close GPT/imagegen/raster imitation, run at least three focused
export/compare/fix iterations. Every iteration must export a fresh PNG and run
strict comparison against the same reference, unless the user explicitly changes
the reference or accepts a different target.

```text
Iteration:
Reference compared:
Draw.io file:
Exported preview:
Geometry mismatches:
Semantic mismatches:
Asset mismatches:
Text/formula mismatches:
Connector/routing mismatches:
Strict comparison metrics:
Fixes applied:
Remaining mismatches:
Stop reason:
```

Do not stop before three strict-comparison iterations, even if an early pass is
achieved; use remaining iterations as verification and small cleanup passes. Do
not stop after three if strict comparison still fails and there are concrete
edits available. Continue until strict comparison passes, the user changes the
target, or a real blocker prevents further export/comparison/editing.

If a strict comparison remains failed after the available iteration budget, the
final status is `not passed`, not `passed with explanation`. Trace notes may
record why a mismatch remains, but the user-facing answer must not present that
reason as completion.

## Iteration 1: Geometry And First Strict Compare

Compare:

- canvas aspect ratio
- major module x/y positions
- module width/height
- gutters between modules
- label baselines
- output panel location
- repeated motif count and spacing

Fix geometry before changing style. If the reference is a PNG/JPG/WebP, use the
bbox mapping from `png-layout-extraction.md`.

Then export and run strict comparison. Use `tile-mismatches.csv`,
`foreground-overlay.png`, and `diff-heatmap.png` to select the next edits.

## Iteration 2: Visual Semantics And Second Strict Compare

Compare:

- color families
- object silhouettes
- feature-map stack direction and density
- residual or feedback route shape
- chart/probability encoding
- whether complex objects are recognizable

If a complex object is not recognizable when built from primitives, do not keep
tweaking the primitive sketch. Use `complex-asset-sourcing.md` and `add-svg`.

Then export and run strict comparison again. Fix the largest local regions
first; do not make global style changes while major object placement or
silhouette errors remain.

## Iteration 3: Technical QA And Third Strict Compare

Run draw.io QA:

```bash
python skills/research-drawio-skill/scripts/qa_drawio.py path/to/file.drawio
```

Then export a visual preview when draw.io Desktop CLI is available:

```bash
python skills/research-drawio-skill/scripts/export_drawio_preview.py path/to/file.drawio --formats png svg
```

For close GPT/imagegen/raster imitation, run strict comparison:

```bash
python skills/research-drawio-skill/scripts/compare_drawio_reference.py reference.png path/to/exports/file.png --mode strict
```

Fix:

- XML errors
- off-canvas objects
- labels overlapping glyphs
- connector routes through text or key node bodies
- unsafe SVG data URI encoding
- duplicate primitive glyphs after SVG insertion
- missing, blank, clipped, or visually incorrect exported previews
- inserted SVGs that appear in XML but fail to render in exported PNG/SVG
- strict comparison failures in `mae`, `ssim`, `foreground_iou`, `edge_iou`,
  content bbox, or worst mismatch tiles

Use the generated `foreground-overlay.png` and `tile-mismatches.csv` to decide
the next edits. Fix worst tiles first; do not make broad style changes before
resolving major local geometry or object mismatches.

## Additional Iterations

After iteration 3, continue the same export/compare/fix cycle whenever strict
comparison still fails and a local edit is available. Prioritize:

- worst named regions in `region-mismatches.csv`
- worst tiles by `mae`
- foreground objects with poor overlap
- edge/silhouette mismatches
- text or formula baselines that drift from the reference
- connectors whose shape differs without avoiding a real obstacle

Only stop with `not passed` when further progress is blocked by missing tools,
missing source assets, impossible target conflict, or explicit user direction.

## Acceptance Criteria

Deliver only when:

- draw.io QA has no blocking errors
- exported preview QA has been completed when draw.io Desktop CLI is available
- for close GPT/imagegen/raster tracing, at least three strict pixel-level
  export/compare/fix iterations have been run and recorded
- strict reference comparison has passed; if it has not passed, the work must be
  reported as not yet passing rather than complete
- major reference regions are present and close in relative geometry
- complex objects are either recognizable primitives or selected assets
- all generated/raster labels have been rebuilt as editable text
- no reference bitmap is required for the final diagram structure
- trace notes include iteration count and remaining mismatches

## Prohibited Completion Pattern

Do not answer with any variant of:

```text
Strict pixel comparison did not pass because the final figure is an editable
scientific redraw with formulas/vector glyphs; reasons and metrics are recorded
in trace notes.
```

Instead, say the strict comparison did not pass, list the worst remaining
mismatches, and continue editing if tools and time are available. If stopping is
unavoidable, mark the artifact as `not passed`.
