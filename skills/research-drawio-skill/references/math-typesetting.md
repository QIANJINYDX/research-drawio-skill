# Math Typesetting in Draw.io

Use this reference whenever a diagram contains equations, tensor notation,
matrix operations, model formulas, Greek letters, superscripts/subscripts, or
mathematical symbols.

## Required Rules

- Enable mathematical typesetting in the draw.io source by setting
  `math="1"` on `mxGraphModel`.
- Put formulas in dedicated text cells, not inside crowded process boxes.
- Use MathJax delimiters:
  - Inline LaTeX: `\(...\)`
  - Display LaTeX: `$$...$$`
  - AsciiMath: single backticks
- Keep line breaks outside math delimiters. For multi-part equations, use
  separate formula cells instead of forcing a long multiline label.
- Keep formula cells in protected zones where connectors cannot pass through.
- If the local export tool does not render MathJax reliably, deliver the
  `.drawio` source and tell the user to enable mathematical typesetting in
  diagrams.net before exporting.

Official draw.io documentation: https://www.drawio.com/docs/manual/text/math-typesetting/

## Attention Formula Example

Use this in a dedicated formula cell:

```text
\( \mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^{\mathsf T}/\sqrt{d_k})V \)
```

As XML:

```xml
<mxCell id="formula-attention" value="\( \mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^{\mathsf T}/\sqrt{d_k})V \)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Arial;fontSize=12;fontColor=#1F2933;spacing=4;" vertex="1" parent="1">
  <mxGeometry x="420" y="460" width="320" height="42" as="geometry"/>
</mxCell>
```

## Safe Plain-Text Fallback

When MathJax is unavailable or the user needs maximum compatibility, use a
plain-text formula with Unicode kept minimal:

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
```

Label the fallback as plain text in the delivery notes so the user knows it was
intentional.

## QA

- Open the `.drawio` file in diagrams.net.
- Confirm Extras > Mathematical Typesetting is enabled if formulas are visible
  as raw LaTeX.
- Export SVG/PDF only after formulas render correctly.
- Inspect the export at final size; MathJax output can change label dimensions,
  so formulas may need extra whitespace.

