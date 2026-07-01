# Cat/Dog SVG Candidate Notes

Source mode: network search.

Target draw.io file: `example/resnet-cat-dog-classification.drawio`

SVG role: replace crude primitive cat/dog sketches in the input image tile with recognizable, compact vector silhouettes.

## Selected Assets

| Concept | Selected file | Source URL | Direct SVG URL | License / usage note | Edit made |
|---|---|---|---|---|---|
| Cat silhouette | `cat-silhouette-selected.svg` | https://commons.wikimedia.org/wiki/File:Cat_silhouette.svg | https://upload.wikimedia.org/wikipedia/commons/6/60/Cat_silhouette.svg | Wikimedia page marks the file as public domain / presumed PD-self. | Added `viewBox`; recolored fill to `#5F6368`. |
| Dog silhouette | `dog-silhouette-selected.svg` | https://commons.wikimedia.org/wiki/File:Dog_Silhouette_01.svg | https://upload.wikimedia.org/wikipedia/commons/5/51/Dog_Silhouette_01.svg | Wikimedia page marks the file as public domain / PD-self. | Recolored fill to `#C99436`. |

Original downloaded files are retained beside the selected versions:

- `cat-silhouette-wikimedia.svg`
- `dog-silhouette-01-wikimedia.svg`

Preview PNGs were rendered only for local visual QA:

- `cat-silhouette-selected.png`
- `dog-silhouette-selected.png`
- `reference-input-silhouettes.png`

## Reference-Derived Local Asset

| Concept | File | Source | License / usage note | Outcome |
|---|---|---|---|---|
| Cat/dog input tile silhouettes | `reference-input-silhouettes.svg` | Derived from `assets/reference-images/resnet-cat-dog-reference.png` by color-mask contour tracing. | Local reference-derived vector for redraw fidelity; not a network asset. | Used in `example/resnet-cat-dog-classification-strict.drawio` and `example/resnet-cat-dog-classification-generated-trace.drawio` to match the generated reference input tile more closely without embedding the full raster PNG. |

## Additional Network Candidates

| Concept | Candidate | Source URL | License / usage note | Outcome |
|---|---|---|---|---|
| Cat silhouette | SVGRepo Cat Silhouette | https://www.svgrepo.com/svg/481046/cat-silhouette | Page lists CC0 license. | Kept as candidate; direct download endpoint returned HTTP 429. |
| Dog silhouette | SVGRepo Cute Dog Silhouette | https://www.svgrepo.com/svg/5265/cute-dog-silhouette | Page lists CC0 license. | Kept as candidate; direct download endpoint returned HTTP 429. |
| Dog silhouette | SVGRepo Sitting Dog | https://www.svgrepo.com/svg/70224/sitting-dog | Page lists CC0 license. | Kept as candidate; not embedded because Wikimedia direct source was available. |
| Cat silhouette | FreeSVG Sitting Cat | https://freesvg.org/sitting-cat-silhouette-vector-clip-art | Page lists Public Domain. | Kept as candidate; direct download returned HTTP 403 in local fetch. |

## Integration

- Inserted `node-input-image-cat-svg` at `x=40, y=390, width=100, height=100`.
- Inserted `node-input-image-dog-svg` at `x=150, y=390, width=110, height=110`.
- Removed duplicate primitive glyph cells for cat and dog.
- Encoded SVGs as URL-encoded `data:image/svg+xml,` image styles.
- Confirmed no raw `data:image/svg+xml;base64,...` appears in the draw.io style strings.

Strict redraw integration:

- Inserted `node-input-image-ref-silhouettes` at `x=15, y=340, width=250, height=230`.
- The asset contains only the reference-derived animal silhouettes; the draw.io
  input tile border and label remain editable.

Imagegen-to-draw.io trace integration:

- Reused `node-input-image-ref-silhouettes` in
  `example/resnet-cat-dog-classification-generated-trace.drawio`.
- No duplicate primitive cat/dog sketch is drawn in that file.
