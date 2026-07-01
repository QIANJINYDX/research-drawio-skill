# Transformer Machine Translation Figure Trace Notes

## Working Contract

Scientific message: A Transformer machine-translation model converts source tokens into contextual encoder memory, uses decoder masked self-attention plus encoder-decoder cross-attention, and emits target-token probabilities that form the translated sentence.

Figure type: Method architecture schematic.

Audience/journal style: Research-paper figure, white background, restrained Nature-style palette, editable vector primitives.

Final output: `output/transformer_machine_translation.drawio` with SVG and PNG previews in `output/exports/`.

Reference image role: Composition and module-hierarchy guide only.

Draw.io trace role: Editable scientific redraw using draw.io primitives, not a pasted bitmap.

Core entities: Source tokens, token IDs, token embeddings, positional encoding, input representations, encoder stack, encoder memory, decoder stack, attention heatmaps, softmax probability bars, target tokens, translated sentence.

Topology: Source tokens -> token IDs -> embeddings/position information -> encoder stack -> encoder memory -> decoder cross-attention; previous target tokens -> decoder masked self-attention; decoder states -> output probabilities -> target tokens -> translated sentence.

Labels/formulas: Short editable English labels. No final formula cell, because the generated reference used no equation and strict tracing improved after removing the extra formula strip.

Style constraints: No raster-backed final diagram, no external SVG assets, no gradients/shadows, short labels, orthogonal arrows, semantic colors for source/embedding/encoder/decoder/output.

QA risks: Strict pixel matching remains difficult because the imagegen reference uses raster text, antialiasing, sine waves, and non-editable pseudo-layout details, while the final source is a cleaned editable schematic.

Complex asset policy: No real-world or complex recognizable assets were needed. All glyphs were self-designed with draw.io primitives.

## Trace Mapping

| Reference region | Approx. reference bbox | Draw.io module | Approx. draw.io bbox | Cells/glyphs | Connectors | Notes |
|---|---:|---|---:|---|---|---|
| Source sentence tokens | `[35, 35, 275, 390]` | Source tokenization | `[35, 35, 280, 390]` | Token chips, token ID chips | Source tokenization arrows | Text rebuilt manually as editable labels. |
| Embedding and positional encoding | `[335, 35, 250, 555]` | Embedding / PE lane | `[335, 35, 260, 555]` | Embedding columns, PE bars, input representation columns | Source-to-representation and representation-to-encoder arrows | PE simplified from raster wave to editable bar/dot motif. |
| Encoder stack | `[625, 115, 240, 395]` | Encoder layer stack | `[630, 118, 230, 392]` | MHA, Add & Norm, FFN blocks, residual routes | Encoder input and encoder-memory arrows | Encoder repeated `x N` marker kept editable. |
| Encoder self-attention heatmap | `[585, 555, 350, 215]` | Self-attention example | `[580, 558, 322, 210]` | 7 x 7 heatmap tiles, colorbar, axis labels | Dashed example connector | Final strict worst region remains here. |
| Encoder memory | `[888, 298, 126, 170]` | Encoder memory | `[892, 302, 118, 160]` | Vector-column glyphs | Encoder-to-memory and memory-to-cross-attention arrows | Label separated from glyph after preview QA. |
| Decoder stack | `[1060, 85, 260, 430]` | Decoder layer stack | `[1066, 88, 250, 422]` | Masked MHA, cross-attention, Add & Norm, FFN blocks | Previous-target and encoder-memory inputs, decoded-state output | Decoder repeated `x N` marker kept editable. |
| Decoder attention heatmaps | `[955, 565, 530, 230]` | Masked and cross-attention examples | `[898, 568, 520, 224]` | Triangular masked heatmap, cross-attention heatmap, colorbars | Dashed example connectors | Shifted left in iteration 2 to better match the reference. |
| Output probabilities and target tokens | `[1370, 120, 310, 455]` | Output module | `[1370, 120, 350, 455]` | Softmax bar miniatures, target-token chips, final sentence box | Decoder-to-probability, probability-to-target, target-to-sentence arrows | Bar miniatures encode next-token probability distributions. |

## Asset Notes

- Reference image: `output/transformer_machine_translation_reference.png`.
- Reference source: generated with the built-in imagegen tool as a composition guide.
- External assets: none.
- SVG assets: none.
- Final diagram body: draw.io primitives only; no reference bitmap embedded.

## Consistency Loop

### Iteration 1

Reference compared: `output/transformer_machine_translation_reference.png`.

Draw.io file: `output/transformer_machine_translation.drawio`.

Exported preview: `output/exports/transformer_machine_translation.png`.

Geometry mismatches: Candidate content height was shorter than reference; decoder attention examples were too far right.

Semantic mismatches: Bottom formula/legend strip was not present in reference.

Connector/routing mismatches: Previous-target arrow used a long colored route that added extra foreground.

Strict comparison metrics: `mae=16.9208`, `rmse=45.3990`, `ssim=0.6672`, `foreground_iou=0.3090`, `edge_iou=0.0434`, `worst_tile_mae=47.5442`.

Fixes applied: Removed unnecessary main title before comparison; separated encoder-memory label from glyph; after comparison, removed formula/legend strip and shifted decoder attention panel left.

Remaining mismatches: Strict comparison failed; worst region was decoder attention heatmaps.

Stop reason: Continued to iteration 2.

### Iteration 2

Reference compared: `output/transformer_machine_translation_reference.png`.

Exported preview: `output/exports/transformer_machine_translation.png`.

Geometry mismatches: Encoder self-attention example box still differed in width and internal edge density.

Semantic mismatches: PE bar motif remained different from the reference wave motif.

Connector/routing mismatches: Previous-target stream still created extra foreground relative to the reference.

Strict comparison metrics: `mae=16.6323`, `rmse=45.2227`, `ssim=0.6757`, `foreground_iou=0.3005`, `edge_iou=0.0406`, `worst_tile_mae=66.4713`.

Fixes applied: Tightened the encoder self-attention example box and changed the previous-target stream to a neutral route through the masked/cross-attention corridor.

Remaining mismatches: Strict comparison failed; worst region moved to encoder self-attention heatmap.

Stop reason: Continued to iteration 3.

### Iteration 3

Reference compared: `output/transformer_machine_translation_reference.png`.

Exported preview: `output/exports/transformer_machine_translation.png`.

Geometry mismatches: Candidate content height remained shorter; strict bbox aspect delta remained above threshold.

Semantic mismatches: Major modules are present, but raster-specific text, wave, and edge shapes do not match the reference foreground masks.

Connector/routing mismatches: Automated comparison still detects low edge overlap, especially around attention heatmaps and routed arrows.

Strict comparison metrics: `mae=16.6408`, `rmse=45.2199`, `ssim=0.6758`, `foreground_iou=0.2997`, `edge_iou=0.0408`, `bbox_aspect_delta=0.0835`, `content_area_delta=0.0235`, `worst_tile_mae=66.4713`.

Fixes applied: None after this comparison.

Remaining mismatches: Strict comparison not passed. Worst named region: encoder self-attention heatmap (`ssim=0.4615`, `foreground_iou=0.3433`, `edge_iou=0.0450`).

Stop reason: Final artifact is delivered as an editable scientific schematic with a recorded strict-comparison failure. Further strict progress would require a near-facsimile redraw of the generated raster reference, including its raster text, waves, antialiasing, and edge masks.

## QA Summary

- Draw.io XML QA: parsed successfully.
- Final default QA command: `python skills/research-drawio-skill/scripts/qa_drawio.py output/transformer_machine_translation.drawio`.
- Final default QA result: `OK XML parsed; vertices=427 edges=29 warnings=396`.
- Fine-grid QA command: `python skills/research-drawio-skill/scripts/qa_drawio.py output/transformer_machine_translation.drawio --grid 2`.
- Fine-grid QA result: parsed successfully with 80 warnings.
- Preview export: PNG and SVG exported successfully.
- Strict comparison: not passed.
- Final strict report directory: `comparison-reports/transformer_machine_translation/`.

## Remaining Risks

- The final figure is scientifically readable and editable, but it is not a strict pixel-level match to the generated raster reference.
- Most QA warnings are from small heatmap/probability primitives, transparent routing anchors, and container-background crossing detections; no XML errors were reported.
- If exact trace fidelity is required, the next work should replace the cleaned scientific redraw with a closer facsimile of the reference geometry and reference-specific wave/text/edge positions.
