# Trace Notes: Multi-omics disease subtyping

## Working Contract

Scientific message: 多组学数据经过质控、特征提取和共享表示学习后，可将患者队列划分为可解释的疾病亚型，并连接到标志物和治疗反应。
Figure type: multi-omics/data-integration workflow.
Audience/journal style: Nature-style scientific schematic, white background, restrained palette, editable vector elements.
Final output: editable draw.io source plus SVG/PNG preview when export tooling is available.
Reference image role: composition and hierarchy guide only.
Draw.io trace role: rebuild all scientific entities as editable draw.io primitives.
Core entities: genomics, transcriptomics, proteomics, metabolomics, clinical covariates, QC/normalization, feature matrices, fusion model, latent embedding, subtype biomarkers, response rate.
Topology: five parallel data lanes converge into one integration model; the model produces latent subtype clusters; clusters feed biomarker and treatment-response outputs.
Labels/formulas: no formulas; labels are editable Chinese text with English abbreviations where needed.
Style constraints: no bitmap body, no shadows, no gradients, no decorative texture, no unlicensed external assets.
QA risks: connector routing around five converging lanes; glyph/text separation inside dense output panels; strict visual comparison may be sensitive to rebuilt labels.
Complex asset policy: no external SVG search; omics objects are self-designed primitive glyphs.

## PNG Layout Extraction

Reference image: `multiomics-disease-subtyping-reference.png`
Pixel size: 1717 x 916
Canvas target: 1720 x 920 draw.io page, near 1:1 mapping, 10 px grid.

Major regions:

- Multi-omics data: reference bbox approx [0, 85, 425, 760]; draw.io bbox [0, 90, 430, 760]; role: five modality lanes with cohort matrices.
- Preprocessing and feature extraction: reference bbox approx [450, 95, 270, 745]; draw.io bbox [450, 100, 270, 740]; role: modality-specific QC and feature vector extraction.
- Integration model: reference bbox approx [790, 300, 285, 330]; draw.io bbox [780, 290, 300, 340]; role: central fusion model with omics stack and graph/neural glyph.
- Latent representation: reference bbox approx [1130, 245, 290, 470]; draw.io bbox [1128, 230, 300, 490]; role: UMAP-like three-cluster subtype map.
- Clinical outputs: reference bbox approx [1480, 120, 235, 700]; draw.io bbox [1470, 110, 250, 720]; role: subtype biomarker heatmap and therapy response chart.

Alignment lines:

- Top stage labels: y = 20.
- Main data path: y centers = 170, 320, 470, 620, 770, converging through x = 750.
- Model-to-latent rail: y = 460.
- Output branch corridor: x = 1440.

Repeated motifs:

- Input patient dots: 6 per lane, first three colored by modality.
- Omics matrices: 6 x 4 tiles per input lane.
- Feature vectors: five qualitative columns per preprocessing module.
- UMAP dots: three subtype clusters, with consistent A/B/C colors.
- Biomarker heatmap: 5 x 5 tiles.

Trace fidelity decisions:

- Preserve: horizontal five-stage pipeline, relative module order, convergence arrows, central model, UMAP-like subtype clusters, two clinical output panels.
- Simplify: generated pseudo-text, decorative line curvature, internal icon detail.
- Replace with editable text: all stage and module labels.

## Asset Notes

No external assets were searched or embedded. All glyphs are self-designed from draw.io primitives:

- DNA/genomics: paired ellipses and thin link lines.
- Transcriptomics: wave-like bead motif plus heatmap.
- Proteomics: graph/network nodes and link lines.
- Metabolomics: metabolite bubble motif.
- Clinical data: clipboard/table motif.
- Fusion model: stacked matrices and neural/graph nodes.
- Outputs: heatmap tiles and response-rate columns.

## Consistency Loop

Iteration 1:

- Reference compared: `multiomics-disease-subtyping-reference.png`
- Draw.io file: `multiomics-disease-subtyping.drawio`
- Exported preview: `exports/multiomics-disease-subtyping.png`
- Geometry mismatches: exported draw.io crop was 1716 x 853 versus 1717 x 916 reference; major module order was preserved.
- Semantic mismatches: labels were rebuilt as editable Chinese text; generated English pseudo-labels were not copied.
- Asset mismatches: initial ellipse syntax rendered circular glyphs as square-like marks in several modules.
- Text/formula mismatches: no formulas; all labels editable.
- Connector/routing mismatches: no QA connector warnings.
- Strict comparison metrics: MAE 24.46, RMSE 56.95, SSIM 0.6135, foreground IoU 0.1957, edge IoU 0.0512, worst tile MAE 63.46; strict pass = false.
- Fixes applied: corrected draw.io ellipse style syntax for all circular glyphs.
- Remaining mismatches: output panel and subtype cluster silhouettes differed from reference.

Iteration 2:

- Reference compared: `multiomics-disease-subtyping-reference.png`
- Draw.io file: `multiomics-disease-subtyping.drawio`
- Exported preview: `exports/multiomics-disease-subtyping.png`
- Geometry mismatches: module order and coordinates preserved; crop height remained 853 px.
- Semantic mismatches: Chinese labels and simplified editable glyphs remained different from the imagegen reference.
- Asset mismatches: circular glyph rendering was fixed.
- Text/formula mismatches: no formulas; all labels editable.
- Connector/routing mismatches: no QA connector warnings.
- Strict comparison metrics: MAE 24.19, RMSE 56.60, SSIM 0.6147, foreground IoU 0.1938, edge IoU 0.0509, worst tile MAE 63.46; strict pass = false.
- Fixes applied: identified clinical outputs as the worst region for the next edit.
- Remaining mismatches: clinical output heatmap/icons were too dense and shifted relative to the reference.

Iteration 3:

- Reference compared: `multiomics-disease-subtyping-reference.png`
- Draw.io file: `multiomics-disease-subtyping.drawio`
- Exported preview: `exports/multiomics-disease-subtyping.png`
- Geometry mismatches: content crop remained 1716 x 853; global layout was stable.
- Semantic mismatches: final diagram intentionally keeps editable Chinese labels and primitive glyphs.
- Asset mismatches: clinical output icons were redrawn as smaller primitive glyphs; heatmap enlarged; therapy response ticks added.
- Text/formula mismatches: no formulas; all labels editable.
- Connector/routing mismatches: no QA connector warnings.
- Strict comparison metrics: MAE 24.16, RMSE 56.57, SSIM 0.6137, foreground IoU 0.1990, edge IoU 0.0505, worst tile MAE 63.46; strict pass = false.
- Fixes applied: output panel spacing improved and QA remained clean.
- Remaining mismatches: strict pixel-level match is not achieved; worst region remains Clinical outputs with MAE 35.38, RMSE 73.43, SSIM 0.4449, foreground IoU 0.2384, edge IoU 0.0348.

Additional semantic check:

- Mode: semantic
- Result: pass = false.
- Metrics: MAE 24.16, RMSE 56.57, SSIM 0.6137, foreground IoU 0.1990, edge IoU 0.0505.
- Remaining mismatches: foreground and edge overlap are below the semantic thresholds, mainly because the editable redraw uses different text, simplified glyph silhouettes, and a compact clinical-output reconstruction.

## QA

- Draw.io XML/layout QA: `OK XML parsed; vertices=571 edges=13 warnings=0`.
- Export QA: draw.io Desktop CLI found at `D:\drawio\draw.io\draw.io.exe`; PNG and SVG exports created successfully; PNG probe nonblank, SVG probe OK.
- Final strict comparison status: not passed.
- Final semantic comparison status: not passed.
- Reviewer-facing residual risk: the diagram is suitable as an editable scientific schematic, but it should not be described as a pixel-faithful trace of the generated reference image.
