# Scientific Flowchart Archetypes

Choose one primary archetype before layout. Hybrids are allowed, but one
archetype should control the reading order.

| Archetype | Use when | Layout signal | Common modules |
|---|---|---|---|
| `experimental workflow` | Wet-lab, animal, clinical, or assay steps must be understood | Top-to-bottom or left-to-right protocol | sample, treatment, assay, measurement, analysis |
| `computational pipeline` | Data are transformed through scripts, models, or statistics | Left-to-right data flow | input data, preprocessing, model, evaluation, output |
| `study/cohort flow` | Patient/sample inclusion, exclusion, grouping, or follow-up matters | Funnel or staged branching | screened, excluded, assigned, followed, analyzed |
| `method architecture` | A model/device/platform has internal components | Central hero module with input/output rails | encoder, module, database, classifier, feedback |
| `mechanism schematic` | The claim is causal or biological/physical | Spatial pathway with highlighted causal step | trigger, pathway, mediator, phenotype, intervention |
| `multi-omics/data-integration workflow` | Several data modalities converge into interpretation | Parallel input lanes merging into an integration module | genomics, transcriptomics, imaging, metadata, integration |
| `graphical abstract` | The figure must summarize the paper's whole message | Three-act structure: problem, approach, result | context, intervention/method, key finding |
| `hybrid multi-panel flowchart` | A flowchart is one panel within a larger paper figure | One dominant schematic plus compact support areas | overview, validation, controls, outcome |

## Selection Rules

- Use `experimental workflow` when time, treatments, or assays are the main
  ordering principle.
- Use `computational pipeline` when the object changes form as it moves through
  analysis stages.
- Use `study/cohort flow` when counts and exclusions are scientifically
  important. Keep sample counts close to branches.
- Use `method architecture` when component relationships matter more than
  chronological order.
- Use `mechanism schematic` only when the evidence supports the implied causal
  direction. Otherwise label the flow as association, processing, or hypothesis.
- Use `graphical abstract` when the user asks for a paper-wide summary, but keep
  it more restrained than a promotional illustration.

## Anti-Patterns

- A flowchart where every box is the same size despite unequal importance.
- A pipeline with many branch colors but no stable color meaning.
- A mechanism diagram that uses arrows to imply causality without labels or
  evidence.
- A cohort flow where exclusion counts are detached from the branch they explain.
- A graphical abstract that becomes a collage of icons rather than a single
  scientific sentence.

