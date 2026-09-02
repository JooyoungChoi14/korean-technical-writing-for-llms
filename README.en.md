# Korean Technical Writing for LLMs

An exploratory study and an installable Agent Skill for reviewing Korean technical writing generated or revised by LLMs.

The project asks a reader-centered question: even when a sentence is grammatically possible, does the reader have to decode a metaphor, infer an omitted actor, or reconstruct the operation before understanding it?

## Contents

- A Korean [experiment report](report/experiment.ko.md) and [web edition](docs/index.html)
- The installable [`korean-technical-writing-review`](plugins/korean-technical-writing-review/skills/korean-technical-writing-review/SKILL.md) Agent Skill
- A public-safe evaluation set of 24 synthetic cases
- Codex plugin and repository marketplace metadata

```bash
npx skills add JooyoungChoi14/korean-technical-writing-for-llms --skill korean-technical-writing-review
```

The method separates drafting, diagnosis, limited revision, and semantic verification. It is model-neutral and does not attempt to identify which model authored a document.

## Authorship

Conceived, directed, evaluated, and authored by **Jooyoung Choi ([@JooyoungChoi14](https://github.com/JooyoungChoi14))**. AI systems were used as experimental subjects and as drafting and review tools. Corpus selection, evaluation criteria, factual verification, publication decisions, and final conclusions were reviewed and approved by the author.

See [`CITATION.cff`](CITATION.cff) for citation metadata.
