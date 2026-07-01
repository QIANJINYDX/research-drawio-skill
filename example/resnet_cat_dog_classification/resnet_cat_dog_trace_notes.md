# ResNet Cat-Dog Classification Trace Notes

## Working Contract

Scientific message: cat and dog images are normalized into tensors, processed through a ResNet residual feature extractor, and converted into class probabilities.

Figure type: computational pipeline / method architecture.

Audience/journal style: publication-style scientific schematic with restrained Nature-style palette, white background, editable text and primitives.

Final output: editable draw.io source plus SVG and PNG previews.

Reference image role: composition guide only; no bitmap is embedded in the final draw.io body.

Draw.io trace role: rebuild the four-module layout using editable containers, primitive animal thumbnails, preprocessing glyphs, feature-map stacks, residual block, and output bars.

Core entities: cat/dog samples, image preprocessing, tensor, ResNet residual block, feature-map stages, global average pooling, fully connected layer, softmax, class probability bars.

Topology: left-to-right flow: input images -> preprocessing -> ResNet feature extractor -> classifier output. Residual block contains an identity shortcut converging at addition before ReLU.

Labels/formulas: labels are rebuilt as editable text. Dimension labels use plain editable text (3 x H x W, C1 x H/4 x W/4, etc.).

Style constraints: no decorative shadows, no gradients, no raster icons, low-saturation palette, short labels, orthogonal arrows.

QA risks: strict pixel comparison is not passed because the generated reference uses detailed animal illustration and different local edge density. The editable schematic preserves the scientific modules and reading path, but it is not a pixel facsimile.

Complex asset policy: cat and dog are complex recognizable objects. For this task, they are used only as small input-sample identifiers, so self-designed primitive thumbnails are used to keep the final diagram fully editable. No online SVG assets were requested or inserted.

## Reference-to-Draw.io Mapping

| Reference region | Reference bbox (px) | Draw.io module | Draw.io bbox | Cells/glyphs | Simplification |
|---|---:|---|---:|---|---|
| Input Images | [20,137,230,578] | Input images | [20,137,230,578] | cat/dog thumbnail primitives | detailed fur and photoreal detail reduced to abstract sample glyphs |
| Preprocessing | [290,137,205,578] | Preprocessing | [290,137,205,578] | crop grid, normalized layer stack, tensor dot matrix | decorative pseudo-text removed |
| ResNet Feature Extractor | [530,95,940,650] | ResNet feature extractor | [530,95,940,650] | feature-map stacks, residual block, skip path, stage outputs | perspective/depth simplified into editable parallelograms |
| Classifier Output | [1520,137,230,590] | Classifier output | [1520,137,230,590] | pooled vector, fully connected, softmax, probability bars | generated label placement corrected and rebuilt |

## Asset Notes

Concept: cat/dog input samples.

Why primitive drawing is sufficient: animals are small identifiers for dataset input, not the scientific claim; recognizability is achieved by head, ears, eyes, muzzle, whiskers/tongue, and sample labels.

Source mode: self-designed fallback using draw.io primitives.

Candidates: none searched; online assets were not necessary for the requested editable scientific schematic.

Selected asset: primitive glyphs embedded as editable draw.io cells.

Fallback: active.

Duplicate primitive removal: not applicable; no SVG was inserted.

## Consistency Loop

| Iteration | Exported preview | Strict pass | MAE | SSIM | Foreground IoU | Edge IoU | Worst tile MAE | Worst region | Fixes applied | Remaining mismatch |
|---:|---|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | exports/resnet_cat_dog_classification.png | False | 19.7234 | 0.7041 | 0.4936 | 0.1263 | 51.1678 | Input images | first editable redraw; removed colliding edge labels; restored full-page background for matched canvas | animal thumbnails and local edge density differed from generated reference |
| 2 | exports/resnet_cat_dog_classification.png | False | 19.6869 | 0.7041 | 0.4881 | 0.1264 | 50.5799 | Input images | rebuilt cat ears as triangles; added primitive stripes, whiskers, and facial detail | input thumbnails still lower-detail than reference raster |
| 3 | exports/resnet_cat_dog_classification.png | False | 19.5403 | 0.7027 | 0.5083 | 0.1263 | 49.9657 | Input images | enlarged cat/dog thumbnail glyphs to match reference occupancy better | strict thresholds still fail, mainly Input images; local edge density also differs across ResNet blocks |

Strict comparison final status: not passed.

Strict comparison failures after iteration 3:

- ssim=0.7027 < 0.78
- foreground_iou=0.5083 < 0.62
- edge_iou=0.1263 < 0.28

Worst remaining region after iteration 3: Input images with MAE 36.5932, SSIM 0.5706, foreground IoU 0.4631.

Comparison artifacts:

- comparison_iter1/comparison-report.json, diff-heatmap.png, foreground-overlay.png, side-by-side.png, tile-mismatches.csv, region-mismatches.csv
- comparison_iter2/comparison-report.json, diff-heatmap.png, foreground-overlay.png, side-by-side.png, tile-mismatches.csv, region-mismatches.csv
- comparison_iter3/comparison-report.json, diff-heatmap.png, foreground-overlay.png, side-by-side.png, tile-mismatches.csv, region-mismatches.csv

## QA

Draw.io validation: `qa_drawio.py` parsed the source successfully with no XML errors; final run reported 162 vertices, 16 edges, and 350 warnings.

QA warnings reviewed: most warnings are off-10px-grid coordinates caused by preserving the generated reference geometry and small animal/detail primitives; remaining route warnings are conservative checks around attached arrows and large glyphs visible in the exported preview.

Export QA: draw.io Desktop CLI exported PNG and SVG successfully.

PNG preview: exports/resnet_cat_dog_classification.png, 1776 x 889 px, nonblank.

SVG preview: exports/resnet_cat_dog_classification.svg, exported and parsed successfully.

Remaining risks: strict pixel facsimile is not passed. If exact visual imitation is required, the input animals should be replaced with licensed SVG assets selected through an asset-source workflow, or the reference should be simplified to match the editable primitive style before tracing.
