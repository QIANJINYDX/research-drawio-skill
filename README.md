# research-drawio-skill

**Language:** English | [中文](README.zh-CN.md)

`research-drawio-skill` is a Codex skill for creating publication-style
scientific flowcharts and schematic workflows in diagrams.net / draw.io.

The skill is designed for research-paper figures such as method pipelines,
experimental workflows, cohort flow diagrams, mechanism schematics,
multi-omics/data-integration diagrams, model architecture diagrams, and graphical
abstracts. Its design philosophy follows the `nature-figure` style of thinking:
define the scientific message first, build the evidence and topology next,
engineer the layout and connectors, then apply restrained journal-ready visual
style and export QA.

The current version also enforces layout engineering and visual construction:
grid-first alignment, protected formula zones, connector corridors, semantic
composite elements built from draw.io primitives, and a lightweight `.drawio` QA
script that catches common source-level mistakes before visual export.

Recent design rules also prevent three common failure modes: labels covering
glyph primitives, decorative chart glyphs without scientific meaning, and
over-routed connector paths with unnecessary bends.

## What It Helps With

- Editable `.drawio` scientific workflow diagrams
- Nature-style method and experimental design flowcharts
- Computational pipeline and model architecture schematics
- Cohort/study flow diagrams with inclusion and exclusion logic
- Mechanism and graphical abstract diagrams for manuscripts
- SVG/PDF-ready publication exports with QA-oriented guidance

## Repository Structure

```text
.
|-- README.md
|-- README.zh-CN.md
|-- .gitignore
|-- example/
|   `-- attention-mechanism-nature.drawio
`-- skills/
    `-- research-drawio-skill/
        |-- SKILL.md
        |-- manifest.yaml
        |-- agents/
        |   `-- openai.yaml
        |-- scripts/
        |   `-- qa_drawio.py
        |-- static/
        |   `-- core/
        |       |-- contract.md
        |       `-- stance.md
        `-- references/
            |-- archetypes.md
            |-- composite-elements.md
            |-- drawio-authoring.md
            |-- layout-and-routing.md
            |-- math-typesetting.md
            |-- qa-contract.md
            `-- style-guide.md
```

The actual skill lives in `skills/research-drawio-skill/`. The root README is
only for GitHub presentation and installation guidance.

## Example

`example/attention-mechanism-nature.drawio` is an editable Nature-style attention
mechanism schematic created with this skill. It shows how input token embeddings
are projected into query, key, and value vectors; how scaled dot-product scores
are normalized into attention weights; and how value vectors are pooled into
context-aware token representations.

This example is intentionally useful as a QA target while the skill evolves:
newer versions of the skill include stricter checks for alignment, connector
occlusion, and formula rendering.

## Installation

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force `
  "skills\research-drawio-skill" `
  "$env:USERPROFILE\.codex\skills\research-drawio-skill"
```

On macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R skills/research-drawio-skill ~/.codex/skills/research-drawio-skill
```

Then invoke it in Codex with:

```text
Use $research-drawio-skill to create an editable paper-style draw.io workflow diagram.
```

## Design Philosophy

This skill treats a research flowchart as a visual argument rather than a
decorative process map.

Every diagram starts with:

1. A one-sentence scientific message.
2. A diagram role, such as method overview, experimental workflow, cohort flow,
   mechanism schematic, analytical pipeline, model architecture, or graphical
   abstract.
3. A topology map of nodes, modules, branches, loops, inputs, and outputs.
4. A grid layout plan with aligned rows, columns, gutters, and connector
   corridors.
5. A composite-element plan that decides which scientific entities should be
   grouped visual glyphs rather than plain text boxes.
6. A math-label contract for formulas and symbols that need draw.io
   mathematical typesetting.
7. A visual vocabulary that maps colors, shapes, labels, and arrows to
   scientific meaning.
8. An export and reviewer-risk contract for journal-ready delivery.

## Skill Contents

- `SKILL.md`: main trigger metadata and routing protocol.
- `manifest.yaml`: declares always-loaded core files and on-demand references.
- `static/core/contract.md`: required flowchart contract before drawing.
- `static/core/stance.md`: default scientific diagram stance and privacy rule.
- `references/archetypes.md`: scientific flowchart archetypes and anti-patterns.
- `references/composite-elements.md`: editable glyph recipes for bar-chart
  miniatures, DNA/RNA chains, matrices, neural networks, cells, samples, and
  other scientific objects, with rules against decorative charts and label
  overlap.
- `references/layout-and-routing.md`: grid alignment, connector corridors, edge
  labels, collision avoidance, and minimum-bend routing rules.
- `references/math-typesetting.md`: MathJax / draw.io formula handling.
- `references/style-guide.md`: typography, color, shape, connector, and draw.io
  style presets.
- `references/drawio-authoring.md`: `.drawio` / mxGraph XML authoring guidance.
- `references/qa-contract.md`: logic, visual, source-file, and export QA checks.
- `scripts/qa_drawio.py`: lightweight XML, math, alignment, endpoint,
  text/glyph overlap, chart-glyph semantics, bend-count, and
  connector-through-node QA.

## Example Prompts

```text
Use $research-drawio-skill to draw a Nature-style method workflow for my single-cell analysis pipeline.
```

```text
Use $research-drawio-skill to convert this manuscript methods paragraph into an editable draw.io experimental workflow.
```

```text
Use $research-drawio-skill to audit and polish this .drawio mechanism schematic for a paper figure.
```

## Validation

If you have the Codex `skill-creator` validation script available, run:

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "skills\research-drawio-skill"
```

Expected result:

```text
Skill is valid!
```

`PYTHONUTF8=1` is recommended on Windows because the skill metadata includes
Chinese trigger phrases.

To inspect a generated `.drawio` file:

```powershell
python "skills\research-drawio-skill\scripts\qa_drawio.py" "example\attention-mechanism-nature.drawio"
```

Warnings should be reviewed before using a diagram as a polished example or
publication-facing export.
