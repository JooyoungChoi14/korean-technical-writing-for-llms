---
name: korean-technical-writing-review
description: Review, rewrite, or draft Korean technical documentation so readers do not have to decode improvised metaphors, mixed-language compounds, compressed noun strings, or unsupported evaluations. Use for Korean Markdown, HTML prose, design documents, plans, reports, ADRs, READMEs, commit messages, and UI copy when clarity and semantic fidelity matter. Do not trigger merely because a document contains established English technical terms or code identifiers.
---

# Korean Technical Writing Review

Reduce the reader's reconstruction work without changing technical meaning.

## Choose the operation

- **Audit** when asked to find or explain awkward passages. Do not rewrite the whole document.
- **Limited revision** when asked to fix findings. Change only flagged passages.
- **Full rewrite** when explicitly asked to rewrite. Preserve facts, structure, code identifiers, and established project terminology; the original general wording and sentence structure need not be preserved.
- **Draft** when writing from source material. Use only supplied facts and mark unresolved details as `[확인 필요]`.

Read [the rubric](references/rubric.ko.md) before auditing or revising. Read [semantic fidelity](references/semantic-fidelity.ko.md) when the source is technical, security-sensitive, contractual, or ambiguous. Read [output formats](references/output-formats.ko.md) when the user did not specify a format.

## Review in the reader's order

For every title, paragraph, table cell, list item, and caption:

1. Identify the target being discussed.
2. Identify the actual operation or relationship.
3. Add the actor, condition, or result only when the reader needs it and the source supports it.
4. Check whether a metaphor, transliteration, English–Korean compound, noun string, or evaluation replaces that information.
5. Preserve code identifiers, product names, and terms demonstrably established in the project.
6. If the source does not determine the meaning, do not guess. Report `[확인 필요]` and the smallest question needed.

Do not flag a word only because it is English, figurative, or unfamiliar. Flag the passage only when the wording causes an omitted or ambiguous target, actor, operation, condition, result, or scope.

## Separate style from meaning

After revising, make two independent judgments:

- **Clarity:** Can a Korean reader understand the target and operation without reconstructing the sentence from surrounding context?
- **Semantic fidelity:** Did the revision preserve the actor, direction, condition, scope, certainty, and code-level meaning?

A fluent sentence that changes who performs an action is a failure. A slightly longer sentence that exposes the correct operation is usually preferable.

수정문을 짧게 만드는 것보다, 문제 표현이 대신하던 대상·동작·조건·범위를 문맥에서 확인해 수정문 안에 빠짐없이 되돌려 놓는다.

## Avoid negative priming

Do not place a long blacklist in the drafting prompt. Use positive, operational instructions during drafting. Use recurring problematic expressions only in the separate audit stage as regression examples.

## Default response

When auditing, return a short summary followed by a table with:

`location | source | reader must infer | finding | suggested revision | facts to verify`

When revising, show only meaningful before/after pairs, then provide the revised text. State any unresolved semantic risk separately.
