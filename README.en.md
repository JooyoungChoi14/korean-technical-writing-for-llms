# Korean Technical Writing for LLMs

An exploratory study and an installable Agent Skill for reviewing Korean technical writing generated or revised by LLMs.

The project asks a reader-centered question: even when a sentence is grammatically possible, does the reader have to decode a metaphor, infer an omitted actor, or reconstruct the operation before understanding it?

## Contents

- A Korean [experiment report](report/experiment.ko.md) and [web edition](docs/index.html)
- The installable [`korean-technical-writing-review`](plugins/korean-technical-writing-review/skills/korean-technical-writing-review/SKILL.md) Agent Skill
- A public-safe evaluation set of 20 synthetic cases
- Codex plugin and repository marketplace metadata

```bash
npx skills add JooyoungChoi14/korean-technical-writing-for-llms --skill korean-technical-writing-review
```

The method separates drafting, diagnosis, limited revision, and semantic verification. It is model-neutral and does not attempt to identify which model authored a document.

## Public study scope

The published evidence consists entirely of material available in this repository:

- Three black-box tasks covering authorization, revenue recognition, and policy-experiment analysis
- Two models: Claude Sonnet and Codex gpt-5.4
- Six raw outputs, one run per task and model
- Twenty synthetic regression cases: 16 findings and 4 passing or counter-examples
- Two separate evaluation axes: reader clarity and semantic fidelity

The models were not told that their writing style would be evaluated. Because the sample contains only three outputs per model with no repeated runs, the study does not claim general model rankings or generational effects. Earlier observations from private workplace documents motivated the question but are not part of the published corpus, evaluation set, or model comparison.

## Authorship

Conceived, directed, evaluated, and authored by **Jooyoung Choi ([@JooyoungChoi14](https://github.com/JooyoungChoi14))**. AI systems were used as experimental subjects and as drafting and review tools. Corpus selection, evaluation criteria, factual verification, publication decisions, and final conclusions were reviewed and approved by the author.

See [`CITATION.cff`](CITATION.cff) for citation metadata.
