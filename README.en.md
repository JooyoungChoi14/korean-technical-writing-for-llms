# Korean Technical Writing for LLMs

An exploratory study and an installable Agent Skill for reviewing Korean technical writing generated or revised by LLMs.

The project asks a reader-centered question: even when a sentence is grammatically possible, does the reader have to decode a metaphor, infer an omitted actor, or reconstruct the operation before understanding it?

## Contents

- A Korean [experiment report](report/experiment.ko.md) and [web edition](docs/index.html)
- The installable [`korean-technical-writing-review`](plugins/korean-technical-writing-review/skills/korean-technical-writing-review/SKILL.md) Agent Skill
- A public-safe evaluation set of 20 synthetic cases
- A reproducible [CLI installation and behavior smoke test](evals/cli-smoke/README.md)
- A same-prompt [Codex and Ollama Cloud smoke test across 19 public models](evals/ollama-cloud/README.md)
- A 285-run [prompt-ladder experiment](evals/ollama-cloud/prompt-ladder/README.md) separating harness failures from prompt-sensitive content failures
- Codex plugin and repository marketplace metadata

```bash
npx skills add JooyoungChoi14/korean-technical-writing-for-llms --skill korean-technical-writing-review
```

The method separates drafting, diagnosis, limited revision, and semantic verification. It is model-neutral and does not attempt to identify which model authored a document.

## Verified CLI behavior

On September 2, 2026, the skill was installed from the public GitHub repository into a clean local project and invoked with two models in each CLI. Claude Sonnet 4.5, Claude Opus 5, and gpt-5.6-sol met all three behavioral criteria. gpt-5.3-codex-spark found general ambiguity in the authorization sentence but missed the specific logical conflict between the listed order and the deny-first claim, so that run is recorded as failed rather than rounded up to a pass.

The same Codex harness was also connected to 19 Ollama Cloud models for one exploratory run per model. Fifteen produced final answers; GLM 5.3 and GLM 5.3 Flash met all three strict criteria. Four models were not scored because of tool-schema or service-availability errors. Configuration, judgments, limitations, and the 15 raw outputs are recorded in [`evals/ollama-cloud/`](evals/ollama-cloud/README.md).

A follow-up direct-API experiment removed tools and ran five prompt conditions three times on all 19 models. All 285 calls reached the API without an error, separating the initial MiniMax, Mistral, and Qwen failures from Korean content quality. Generic self-check and counterexample instructions did not beat the baseline; explicitly naming the task-specific authorization conflict increased strict passes from 7 to 21 of 57. Public reasoning, instruction-following, and agentic benchmarks were then joined within source-comparable cohorts. Their relationship with this task changed direction across cohorts and prompt conditions, so the report treats base capability as one interacting variable rather than a single cause. The [raw outputs, benchmark context, exact prompt additions, repeated judgments, and limitations](evals/ollama-cloud/prompt-ladder/README.md) are published for inspection.

This is a compatibility and single-run behavioral smoke test, not a repeated performance benchmark. The [commands, per-model results, acceptance criteria, metadata, and captured outputs](evals/cli-smoke/README.md) are included for review.

## Public study scope

The core writing study consists entirely of new, public material available in this repository:

- Three black-box tasks covering authorization, revenue recognition, and policy-experiment analysis
- Two models: Claude Sonnet and Codex gpt-5.4
- Six raw outputs, one run per task and model
- Twenty synthetic regression cases: 16 findings and 4 passing or counter-examples
- Two separate evaluation axes: reader clarity and semantic fidelity

The models were not told that their writing style would be evaluated. Because the sample contains only three outputs per model with no repeated runs, the study does not claim general model rankings or generational effects. Earlier observations from private workplace documents motivated the question but are not part of the published corpus, evaluation set, or model comparison.

The CLI installation checks and the 19-model Ollama prompt ladder are separate follow-up validations. They test installation compatibility, harness failures, and prompt sensitivity on one short regression task; they do not expand the core corpus or support a general ranking of Korean-language model quality.

## Authorship

Conceived, directed, evaluated, and authored by **Jooyoung Choi ([@JooyoungChoi14](https://github.com/JooyoungChoi14))**. AI systems were used as experimental subjects and as drafting and review tools. Corpus selection, evaluation criteria, factual verification, publication decisions, and final conclusions were reviewed and approved by the author.

See [`CITATION.cff`](CITATION.cff) for citation metadata.
