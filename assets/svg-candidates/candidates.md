# SVG Candidate Index

Source mode: network search

Target draw.io file: `example/protein-structure-prediction-progress.drawio`

## Selected and Inserted

| Concept | Inserted cell ID | Local SVG | Source URL | License / attribution | Style fit |
|---|---|---|---|---|---|
| Protein backbone / template structure | `stage-template-svg-protein-backbone` | `bioicons/protein-backbone-schematic.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Molecular_modelling/Simon_D%C3%BCrr/protein-backbone-schematic.svg | Bioicons, CC0, Simon Durr | Schematic protein-like fold; good for template/physics era |
| Sequence / MSA evidence | `stage-coevolution-svg-dna-helix` | `bioicons/DNA-double-helix.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Nucleic_acids/James-Lloyd/DNA_double_helix.svg | Bioicons, CC0, James-Lloyd | Clear sequence/nucleic-acid glyph; used as visual proxy for evolutionary sequence evidence |
| Neural network / deep map learning | `stage-deep-maps-svg-neural-network` | `bioicons/neural-network-1.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Machine_Learning/Simon_D%C3%BCrr/neural-network-1.svg | Bioicons, CC0, Simon Durr | Sparse network symbol; suitable for model stage |
| AI model / end-to-end learning | `stage-end-to-end-svg-ai-model` | `bioicons/ai.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Machine_Learning/Simon_D%C3%BCrr/ai.svg | Bioicons, CC0, Simon Durr | General AI glyph; suitable for integrated learned model |
| Ligands / molecular complex scope | `stage-foundation-svg-chemical-library` | `bioicons/chemical-library.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Molecular_modelling/Simon_D%C3%BCrr/chemical_library.svg | Bioicons, CC0, Simon Durr | Molecular library glyph; suitable for AF3-style complex prediction |

## Additional Downloaded Candidates

| Concept | Local SVG | Source URL | License / attribution | Notes |
|---|---|---|---|---|
| Molecular force field | `bioicons/forcefield.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Molecular_modelling/Simon_D%C3%BCrr/forcefield.svg | Bioicons, CC0, Simon Durr | Candidate for template/physics stage |
| Molecular database | `bioicons/database.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Molecular_modelling/OpenClipart/database.svg | Bioicons, CC0, OpenClipart | Candidate for PDB/template database |
| DNA alternative | `bioicons/DNA.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Nucleic_acids/Kumar/DNA.svg | Bioicons, CC0, Kumar | Large file; not embedded to keep the draw.io source lighter |
| Algorithm | `bioicons/algorithm.svg` | https://raw.githubusercontent.com/duerrsimon/bioicons/refs/heads/main/static/icons/cc-0/Machine_Learning/Simon_D%C3%BCrr/algorithm.svg | Bioicons, CC0, Simon Durr | Candidate for model architecture or method stage |
| Neural network alternative | `model/neural-network-470666.svg` | https://www.svgrepo.com/svg/470666/neural-network | SVG Repo, CC0 | Download succeeded before rate limiting |

## Network Candidates Not Downloaded

SVG Repo returned HTTP 429 during batch download. These remain source candidates
because their pages report CC0, but they were not embedded.

| Concept | Source URL | License note | Reason not embedded |
|---|---|---|---|
| Protein icon | https://www.svgrepo.com/svg/530663/protein | Page reports CC0 | Download endpoint rate-limited |
| Proteins icon | https://www.svgrepo.com/svg/41258/proteins | Page reports CC0 | Download endpoint rate-limited |
| Protein atomic structure | https://www.svgrepo.com/svg/136474/protein-atomic-structure | Page reports CC0 | Download endpoint rate-limited |
| DNA icon | https://www.svgrepo.com/svg/449355/dna | Page reports CC0 | Download endpoint rate-limited |
| DNA string | https://www.svgrepo.com/svg/78859/dna-string | Page reports CC0 | Download endpoint rate-limited |
| Molecule icon | https://www.svgrepo.com/svg/458802/molecule | Page reports CC0 | Download endpoint rate-limited |
| Database icon | https://www.svgrepo.com/svg/530267/database | Page reports CC0 | Download endpoint rate-limited |

## QA Notes

- Embedded SVGs are stored as draw.io `shape=image` cells with URL-encoded SVG
  data URIs. Raw `data:image/svg+xml;base64,...` was avoided because the
  semicolon in `svg+xml;base64` breaks draw.io style parsing.
- Labels remain separate from SVG bodies.
- Inserted cells use 10 px grid-aligned geometry.
- `qa_drawio.py` reports `warnings=0` for the edited `.drawio` file.
