# U-Net SVG Candidates

Source mode: network search.

## Candidate Contract

Scientific message: U-Net maps a biomedical image to a pixel-wise segmentation mask through an encoder-decoder network with skip connections.
Target draw.io file: `example/unet-network-architecture.drawio`
SVG role: compact input/output glyphs and optional model emblem.
Style constraints: restrained blue/teal palette, no shadows, labels outside SVG bodies.
Replacement plan: SVG input/output glyphs replace any self-drawn duplicate input image or mask primitives.

## Candidates

### Input medical image

1. Ct Scan
   - source URL: https://www.svgrepo.com/svg/311998/ct-scan
   - direct SVG URL: https://www.svgrepo.com/download/311998/ct-scan.svg
   - license: CC0 License as listed by SVGRepo
   - attribution: none required under CC0
   - style fit: good concept match, more literal radiology icon
   - risk: direct download returned HTTP 429 in this run, so it was not embedded
2. Ct Scanners
   - source URL: https://www.svgrepo.com/svg/83513/ct-scanners
   - direct SVG URL: https://www.svgrepo.com/download/83513/ct-scanners.svg
   - license: CC0 License as listed by SVGRepo
   - attribution: none required under CC0
   - style fit: usable but too instrument-focused for a network architecture input
   - risk: not embedded; kept as an alternative candidate
3. Health Icons
   - source URL: https://healthicons.org/
   - direct SVG URL: varies by icon in the Health Icons repository
   - license: Health Icons states the icons are free to use, edit, republish, and need no credit
   - attribution: none required according to the site text
   - style fit: strong for biomedical context
   - risk: specific SVG path was not resolved quickly in this run

Fallback used: `medical-image-fallback.svg`, original vector designed for this diagram.

### Output segmentation mask

1. Image Segmentation
   - source URL: https://www.svgrepo.com/svg/450984/image-segmentation
   - direct SVG URL: https://www.svgrepo.com/download/450984/image-segmentation.svg
   - license: CC0 License as listed by SVGRepo
   - attribution: none required under CC0
   - style fit: strong concept match for mask output
   - risk: direct download returned HTTP 429 in this run, so it was not embedded
2. Health Icons
   - source URL: https://healthicons.org/
   - direct SVG URL: varies by icon in the Health Icons repository
   - license: Health Icons states the icons are free to use, edit, republish, and need no credit
   - attribution: none required according to the site text
   - style fit: strong for biomedical segmentation output if an anatomy/tissue icon is chosen
   - risk: less direct for generic segmentation mask

Fallback used: `segmentation-mask-fallback.svg`, original vector designed for this diagram.

### Optional model emblem

1. Neural Network
   - source URL: https://www.svgrepo.com/svg/470666/neural-network
   - direct SVG URL: https://www.svgrepo.com/download/470666/neural-network.svg
   - license: CC0 License as listed by SVGRepo
   - attribution: none required under CC0
   - style fit: generic AI/model emblem
   - risk: not embedded to avoid duplicating the U-Net architecture, which is already drawn as editable primitives

Downloaded candidate: `neural-network.svg`
