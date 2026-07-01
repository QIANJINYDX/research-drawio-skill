# GAN Handwritten Digit Generation Trace Notes

## Contract

Scientific message: Random latent noise is transformed by a generator into MNIST-like handwritten digits, while a discriminator compares generated and real digit samples and sends adversarial loss feedback to improve generation.

Figure type: Method architecture / computational pipeline schematic.

Audience/journal style: Research-paper schematic, clean Nature-style palette, white background, editable text and primitives.

Final output: Editable diagrams.net `.drawio` source plus SVG/PNG previews.

Reference image role: Raster composition guide only; it is not embedded in the final draw.io source.

Draw.io trace role: Rebuild the GAN architecture with editable draw.io primitives, short labels, aligned modules, and protected connector corridors.

Core entities: Latent noise table, generator layers, generated digit samples, real MNIST digit samples, discriminator layers, real/fake probability score, adversarial loss feedback.

Topology: Left-to-right primary path: noise -> generator -> generated digits -> discriminator -> probability score. Real digit path enters discriminator from above. Dashed feedback loop returns discriminator loss to generator.

Labels/formulas: Short English labels. No formula cells are used in this version to keep the figure compact and close to the reference.

Style constraints: White background, muted blue for generator, muted green for discriminator, warm yellow for probability output, black MNIST tiles, no shadows or gradients.

QA risks: Digit glyphs are editable text rather than raster MNIST strokes; strict pixel comparison must explicitly report any remaining contour mismatch instead of treating editability as a pass condition.

Consistency loop: Three export/compare/fix iterations are planned against `assets/reference-images/gan-handwritten-digits-reference.png`.

Complex asset policy: No online SVG assets used. All visual entities are simple enough to be represented with draw.io primitives and editable text.

## Region Mapping

Reference region: Latent noise table
Reference bbox: x=40, y=270, w=210, h=345
Draw.io module: `noise-table-boundary` plus 24 editable table cells
Draw.io bbox: x=40, y=270, w=210, h=340
Cells/glyphs: numeric cells and ellipsis row
Connectors: arrow to generator through `port-noise-out`
Labels: `Latent noise`
Formula handling: none
What to simplify: exact generated pseudo-random values are retained only as representative examples
What not to copy: raster text antialiasing

Reference region: Generator
Reference bbox: x=315, y=260, w=420, h=375
Draw.io module: `module-generator`
Draw.io bbox: x=320, y=260, w=410, h=370
Cells/glyphs: five increasing layer rectangles, lightweight side facets, and simple inter-layer connectors
Connectors: incoming noise, outgoing generated digits, incoming dashed loss feedback
Labels: `Generator`
Formula handling: none
What to simplify: 3D pseudo-depth from imagegen is reduced to editable front faces and side facets
What not to copy: decorative lighting and dashed texture artifacts

Reference region: Generated digits
Reference bbox: x=795, y=305, w=250, h=285
Draw.io module: `generated-digit-*`
Draw.io bbox: x=800, y=300, w=240, h=280
Cells/glyphs: 3 x 3 black sample tiles with editable white handwritten-style digit labels
Connectors: generator output and discriminator input
Labels: `Generated digits`
Formula handling: none
What to simplify: handwritten strokes are represented by editable digit text
What not to copy: raster blur

Reference region: Real digits
Reference bbox: x=1085, y=45, w=205, h=235
Draw.io module: `real-digit-*`
Draw.io bbox: x=1090, y=40, w=200, h=250
Cells/glyphs: 3 x 3 black sample tiles with editable white handwritten-style digit labels
Connectors: arrow down into discriminator
Labels: `Real digits`
Formula handling: none
What to simplify: sample strokes are represented by editable digit text
What not to copy: raster blur

Reference region: Discriminator
Reference bbox: x=1120, y=330, w=335, h=290
Draw.io module: `module-discriminator`
Draw.io bbox: x=1120, y=330, w=330, h=290
Cells/glyphs: five decreasing layer rectangles, lightweight side facets, and simple inter-layer connectors
Connectors: generated digit input, real digit input, probability output, loss feedback source
Labels: `Discriminator`
Formula handling: none
What to simplify: 3D pseudo-depth reduced to editable front faces and side facets
What not to copy: decorative highlights

Reference region: Real/Fake probability
Reference bbox: x=1505, y=395, w=170, h=205
Draw.io module: `module-probability`
Draw.io bbox: x=1510, y=400, w=170, h=200
Cells/glyphs: mini axis, real/fake columns, threshold guide
Connectors: discriminator output arrow
Labels: `Real / Fake probability score`, `Real`, `Fake`, `1.0`, `0.0`
Formula handling: none
What to simplify: illustrative probability bars are not treated as measured results
What not to copy: raster chart antialiasing

Reference region: Loss feedback
Reference bbox: x=520, y=600, w=900, h=245
Draw.io module: `edge-loss-feedback`
Draw.io bbox: routed through x=1415/y=770 and x=525/y=770
Cells/glyphs: dashed orthogonal feedback arrow
Connectors: discriminator output region to generator bottom
Labels: `Loss feedback`
Formula handling: none
What to simplify: one clean orthogonal return loop
What not to copy: slight wobble in reference route

## Asset Notes

Searched/selected assets: none.

License notes: not applicable; generated reference is only a local composition guide and is not embedded in the final source.

Self-designed fallbacks: all glyphs were built from draw.io primitives and editable text.

## Consistency Loop

Iteration: 1
Reference compared: `assets/reference-images/gan-handwritten-digits-reference.png`
Draw.io file: `example/gan-handwritten-digits/gan-handwritten-digits.drawio`
Exported preview: `example/gan-handwritten-digits/exports/gan-handwritten-digits.png`
Geometry mismatches: Major module bboxes were close after content normalization.
Semantic mismatches: Digit glyphs were editable font digits rather than raster-like handwritten strokes.
Asset mismatches: No external assets used.
Text/formula mismatches: Labels were rebuilt manually; no formulas.
Connector/routing mismatches: No blocking routing defects after QA cleanup.
Strict comparison metrics: pass=false; mae=17.1113; rmse=51.3991; ssim=0.7651; foreground_iou=0.7689; edge_iou=0.0755; worst_tile_mae=101.8752.
Fixes applied: Added network side facets, restored generator-to-sample dashed fan lines, adjusted digit font toward handwritten style.
Remaining mismatches: Real and generated digit regions were the worst local mismatches.
Stop reason: Continued to iteration 2.

Iteration: 2
Reference compared: `assets/reference-images/gan-handwritten-digits-reference.png`
Draw.io file: `example/gan-handwritten-digits/gan-handwritten-digits.drawio`
Exported preview: `example/gan-handwritten-digits/exports/gan-handwritten-digits.png`
Geometry mismatches: Global content bbox remained close; candidate export size was 1645 x 802 after draw.io crop.
Semantic mismatches: Digits remained visibly different from the imagegen reference.
Asset mismatches: None.
Text/formula mismatches: None blocking.
Connector/routing mismatches: QA warnings from added facets/fan lines were fixed before export.
Strict comparison metrics: pass=false; mae=17.6606; rmse=52.2407; ssim=0.7581; foreground_iou=0.7670; edge_iou=0.0763; worst_tile_mae=104.0941.
Fixes applied: Switched digit labels to a more handwritten system font and reran clean QA.
Remaining mismatches: Real digits region remained worst; edge_iou stayed far below strict threshold.
Stop reason: Continued to iteration 3.

Iteration: 3
Reference compared: `assets/reference-images/gan-handwritten-digits-reference.png`
Draw.io file: `example/gan-handwritten-digits/gan-handwritten-digits.drawio`
Exported preview: `example/gan-handwritten-digits/exports/gan-handwritten-digits.png`
Geometry mismatches: Bbox aspect delta stayed low at 0.0042; content area delta stayed low at 0.0129.
Semantic mismatches: Editable digit text cannot match the raster reference's exact handwritten contours.
Asset mismatches: None.
Text/formula mismatches: Labels are editable; no formula cells used.
Connector/routing mismatches: Final QA found no connector or overlap warnings.
Strict comparison metrics: pass=false; mae=17.6241; rmse=52.1227; ssim=0.7582; foreground_iou=0.7678; edge_iou=0.0764; worst_tile_mae=105.0931.
Fixes applied: Kept final handwritten-style digit font after visual inspection; retained clean side facets and fan lines.
Remaining mismatches: Worst region is `Real digits` with mae=89.2683, ssim=0.1806, edge_iou=0.0523. Strict failures are worst_tile_mae, ssim, and edge_iou.
Stop reason: Minimum three strict iterations completed. Final strict status: not passed. Remaining blocking issues are local handwritten digit contours and layer silhouettes that do not match the raster reference at edge level.

## QA

Draw.io QA: passed with `OK XML parsed; vertices=99 edges=16 warnings=0`.

Export QA: draw.io Desktop CLI at `D:\drawio\draw.io\draw.io.exe` exported PNG and SVG successfully. Final PNG probe: size=1645 x 802, nonblank RGB extrema.

Strict comparison: not passed after three strict iterations. The editable source is structurally complete and visually inspected; remaining pixel-level mismatches are recorded in the comparison artifacts.
