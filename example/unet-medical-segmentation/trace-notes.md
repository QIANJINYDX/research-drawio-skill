# U-Net Medical Image Segmentation Draw.io Trace Notes

## Working Contract

Scientific message: A U-Net encoder-decoder uses multiscale feature maps and skip connections to transform a medical image slice into a pixel-level segmentation mask and overlay.
Figure type: Method architecture / scientific schematic.
Audience/journal style: Restrained publication-style figure for biomedical imaging or AI-methods paper.
Final output: Editable diagrams.net/draw.io source plus SVG and PNG preview.
Reference image role: Raster concept for composition, hierarchy, U-shaped topology, and approximate region bboxes.
Draw.io trace role: Editable source rebuilt from primitives; no reference bitmap is embedded as the final diagram body.
Core entities: Medical image tile, encoder feature maps, bottleneck feature maps, decoder feature maps, skip connections, output mask, overlay, segmentation metrics.
Topology: Left-to-right input; downward encoder; bottleneck; upward decoder; lateral skip connections; output mask, overlay, metrics.
Labels/formulas: Editable short text labels only; no formulas used.
Style constraints: White background, low-saturation blue/green/purple palette, no shadows, no glossy gradients, no decorative texture.
QA risks: Medical image texture is simplified; exact raster text and CT texture are intentionally not copied; long skip routes can dominate strict edge-difference metrics.
Consistency loop: At least three export/compare/fix iterations are recorded below after local QA.
Complex asset policy: No network SVG assets were used. Medical slices and masks are abstract primitives because the diagram does not require a recognizable organ silhouette.

## Raster Layout Extraction

Reference image: reference-unet-medical-segmentation.png
Pixel size: 1774 x 887
Canvas target: 1774 x 887 draw.io page, near 1:1 mapping.

Major regions:

| Region | Reference bbox (px) | Draw.io bbox | Visual role |
|---|---:|---:|---|
| Input medical image | [30,145,260,320] | [30,145,260,320] | Grayscale imaging input |
| Encoder pathway | [345,65,320,650] | [345,65,320,650] | Downsampling feature maps |
| Bottleneck | [700,660,190,160] | [700,660,190,160] | Lowest-resolution representation |
| Decoder pathway | [900,65,480,660] | [900,65,480,660] | Upsampling feature maps |
| Skip connections | [500,170,720,500] | [500,170,720,500] | Feature reuse between matched scales |
| Mask output | [1490,80,230,260] | [1490,80,230,260] | Segmentation mask |
| Overlay output | [1455,380,295,290] | [1455,380,295,290] | Mask over imaging context |
| Metrics panel | [1370,695,390,140] | [1370,695,390,140] | Dice / IoU / uncertainty glyphs |

Repeated motifs:
- Feature-map stacks: 4 encoder levels, bottleneck, 4 decoder levels; 4-5 layered parallelograms per block.
- Skip connections: four long lateral routes from encoder scales to decoder scales.
- Output glyphs: black imaging tiles with purple mask signal; metric panel with bars, Dice-like ring, and probability map.

Trace fidelity decisions:
- Preserve: U-shaped topology, relative module locations, output panel placement, blue encoder, green decoder, purple mask/bottleneck signal.
- Simplify: CT texture, pseudo-3D depth, generated small text, shadow-like antialiasing, exact organ texture.
- Replace with editable text: all labels including Input, Encoder, Decoder, Bottleneck, Mask, Overlay, Metrics.

## Asset Notes

Source mode: Self-designed draw.io primitives.
Selected external assets: None.
License/attribution: Not applicable.
Fallbacks: Abstract medical slice built from black tile plus grayscale ellipses; mask/overlay from purple ellipses; metric glyphs from bars, donut-like ellipses, and dots.

## Consistency Loop

Local QA:
- `qa_drawio.py --grid 5`: passed; XML parsed, 130 vertices, 16 edges, 0 warnings.
- `export_drawio_preview.py --formats png svg`: passed; PNG and SVG exported and probed as nonblank / valid.

Strict comparison records:

| Iteration | Main fix | Strict pass | MAE | SSIM | Foreground IoU | Edge IoU | Worst tile MAE | Worst remaining region |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | Initial primitive trace from raster reference | No | 16.774 | 0.718 | 0.743 | 0.053 | 54.172 | Overlay output |
| 2 | Re-routed arrows through invisible ports and removed extra small labels | No | 16.423 | 0.727 | 0.751 | 0.056 | 53.683 | Overlay output |
| 3 | Removed obsolete transparent boundaries; restored 0-warning draw.io QA | No | 16.424 | 0.727 | 0.751 | 0.056 | 53.683 | Overlay output |
| 4 | Rebuilt mask/overlay as more liver-like primitive blobs and added CT contour detail | No | 16.663 | 0.725 | 0.751 | 0.059 | 58.330 | Overlay output |
| 5 | Snapped added CT/mask primitives back to 5px grid and re-exported final source | No | 16.639 | 0.725 | 0.751 | 0.058 | 58.128 | Overlay output |

Final strict comparison status: not passed.

Remaining mismatches:
- `edge_iou` stayed around 0.05-0.06, below the strict threshold of 0.28.
- `ssim` stayed around 0.725, below the strict threshold of 0.78.
- The largest mismatch remains the Overlay output region, where the reference contains raster CT texture and antialiased mask boundaries while the draw.io file uses editable primitive contours.
- Further small primitive edits after iteration 5 were no longer improving the blocking edge-overlap metric. Passing the strict edge threshold would require a substantially more detailed manual trace of the CT/overlay texture or embedding bitmap material, which was not used in the final diagram body.
