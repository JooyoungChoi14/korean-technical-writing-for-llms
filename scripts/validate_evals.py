from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.jsonl"
CLI_SMOKE = ROOT / "evals" / "cli-smoke"
NATURALNESS_V4 = ROOT / "evals" / "naturalness-effect-v4"
NATURALNESS_V5 = ROOT / "evals" / "naturalness-tuning-v5"
REQUIRED = {"id", "source", "category", "text", "expected", "inference", "rewrite", "preserve"}
VERDICTS = {"통과", "구체화 필요", "의미 확인 필요"}


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()
    count = 0

    for line_number, raw in enumerate(CASES.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        count += 1
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc}")
            continue

        missing = REQUIRED - case.keys()
        if missing:
            errors.append(f"line {line_number}: missing {sorted(missing)}")
        case_id = case.get("id")
        if case_id in seen:
            errors.append(f"line {line_number}: duplicate id {case_id}")
        seen.add(case_id)
        if case.get("expected") not in VERDICTS:
            errors.append(f"line {line_number}: invalid verdict {case.get('expected')}")
        if not isinstance(case.get("preserve"), list):
            errors.append(f"line {line_number}: preserve must be a list")
        else:
            for term in case["preserve"]:
                if term not in case.get("rewrite", ""):
                    errors.append(f"line {line_number}: preserved term {term!r} missing from rewrite")

    if count < 10:
        errors.append(f"expected at least 10 cases, found {count}")

    smoke_files = [
        CLI_SMOKE / "README.md",
        CLI_SMOKE / "prompt.ko.txt",
        CLI_SMOKE / "expected.json",
        CLI_SMOKE / "run-metadata.json",
        CLI_SMOKE / "outputs" / "claude-code-sonnet.md",
        CLI_SMOKE / "outputs" / "claude-code-opus-5.md",
        CLI_SMOKE / "outputs" / "codex-gpt-5.6-sol.md",
        CLI_SMOKE / "outputs" / "codex-gpt-5.3-codex-spark.md",
    ]
    for path in smoke_files:
        if not path.is_file():
            errors.append(f"missing CLI smoke-test file: {path.relative_to(ROOT)}")

    try:
        smoke_expected = json.loads((CLI_SMOKE / "expected.json").read_text(encoding="utf-8"))
        smoke_cases = smoke_expected.get("cases", [])
        smoke_ids = [case.get("id") for case in smoke_cases]
        if smoke_ids != ["CLI-SMOKE-001", "CLI-SMOKE-002", "CLI-SMOKE-003"]:
            errors.append(f"unexpected CLI smoke-test case IDs: {smoke_ids}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid CLI smoke expected.json: {exc}")

    try:
        smoke_metadata = json.loads((CLI_SMOKE / "run-metadata.json").read_text(encoding="utf-8"))
        smoke_runs = smoke_metadata.get("runs", [])
        smoke_results = {
            (run.get("agent"), run.get("requested_model")): run.get("result") for run in smoke_runs
        }
        expected_smoke_results = {
            ("Claude Code", "sonnet"): "passed",
            ("Claude Code", "claude-opus-5"): "passed",
            ("Codex CLI", "gpt-5.6-sol"): "passed",
            ("Codex CLI", "gpt-5.3-codex-spark"): "failed",
        }
        if smoke_results != expected_smoke_results:
            errors.append(f"unexpected CLI smoke-test run results: {smoke_results}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid CLI smoke run-metadata.json: {exc}")

    naturalness_files = [
        NATURALNESS_V4 / "README.md",
        NATURALNESS_V4 / "tasks.json",
        NATURALNESS_V4 / "output-schema.json",
        NATURALNESS_V4 / "scores-exact.json",
        NATURALNESS_V4 / "scores-patterns.json",
    ]
    for path in naturalness_files:
        if not path.is_file():
            errors.append(f"missing naturalness v4 file: {path.relative_to(ROOT)}")

    try:
        naturalness = json.loads((NATURALNESS_V4 / "tasks.json").read_text(encoding="utf-8"))
        naturalness_cases = naturalness.get("cases", [])
        naturalness_ids = [case.get("id") for case in naturalness_cases]
        if len(naturalness_cases) != 12 or len(set(naturalness_ids)) != 12:
            errors.append("naturalness v4 must contain 12 unique cases")
        if sum(case.get("kind") == "awkward" for case in naturalness_cases) != 9:
            errors.append("naturalness v4 must contain 9 awkward cases")
        if sum(case.get("kind") == "control" for case in naturalness_cases) != 3:
            errors.append("naturalness v4 must contain 3 control cases")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid naturalness v4 tasks.json: {exc}")

    naturalness_meta_paths = list((NATURALNESS_V4 / "cli-results").rglob("run-1.json"))
    naturalness_meta_paths += list((NATURALNESS_V4 / "ollama-results").rglob("run-1.json"))
    try:
        naturalness_runs = [json.loads(path.read_text(encoding="utf-8-sig")) for path in naturalness_meta_paths]
        if len(naturalness_runs) != 20:
            errors.append(f"expected 20 naturalness v4 runs, found {len(naturalness_runs)}")
        if any(run.get("transport_status") != "completed" for run in naturalness_runs):
            errors.append("naturalness v4 contains an incomplete transport record")
        pairs = {(run.get("model"), run.get("variant")) for run in naturalness_runs}
        models = {run.get("model") for run in naturalness_runs}
        if len(models) != 10 or len(pairs) != 20:
            errors.append(f"unexpected naturalness v4 model/variant coverage: {len(models)} models, {len(pairs)} pairs")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid naturalness v4 run metadata: {exc}")

    for mode in ("exact", "patterns"):
        try:
            score = json.loads((NATURALNESS_V4 / f"scores-{mode}.json").read_text(encoding="utf-8"))
            if score.get("coverage_mode") != mode:
                errors.append(f"naturalness v4 scores-{mode}.json has the wrong coverage mode")
            if len(score.get("records", [])) != 20:
                errors.append(f"naturalness v4 scores-{mode}.json must contain 20 records")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid naturalness v4 scores-{mode}.json: {exc}")

    tuning_files = [
        NATURALNESS_V5 / "README.md",
        NATURALNESS_V5 / "protocol.md",
        NATURALNESS_V5 / "candidate-SKILL.md",
        NATURALNESS_V5 / "tasks.json",
        NATURALNESS_V5 / "output-schema.json",
        NATURALNESS_V5 / "scores-exact.json",
        NATURALNESS_V5 / "scores-patterns.json",
        NATURALNESS_V5 / "adoption-decision.json",
    ]
    for path in tuning_files:
        if not path.is_file():
            errors.append(f"missing naturalness v5 file: {path.relative_to(ROOT)}")

    try:
        tuning = json.loads((NATURALNESS_V5 / "tasks.json").read_text(encoding="utf-8"))
        tuning_cases = tuning.get("cases", [])
        tuning_ids = [case.get("id") for case in tuning_cases]
        if len(tuning_cases) != 15 or len(set(tuning_ids)) != 15:
            errors.append("naturalness v5 must contain 15 unique cases")
        if sum(case.get("kind") == "awkward" for case in tuning_cases) != 12:
            errors.append("naturalness v5 must contain 12 awkward cases")
        if sum(case.get("kind") == "control" for case in tuning_cases) != 3:
            errors.append("naturalness v5 must contain 3 control cases")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid naturalness v5 tasks.json: {exc}")

    deployed_skill = ROOT / "plugins" / "korean-technical-writing-review" / "skills" / "korean-technical-writing-review" / "SKILL.md"
    candidate_line = "수정문을 짧게 만드는 것보다, 문제 표현이 대신하던 대상·동작·조건·범위를 문맥에서 확인해 수정문 안에 빠짐없이 되돌려 놓는다."
    try:
        deployed_text = deployed_skill.read_text(encoding="utf-8").replace("\r\n", "\n")
        candidate_text = (NATURALNESS_V5 / "candidate-SKILL.md").read_text(encoding="utf-8").replace("\r\n", "\n")
        if candidate_text.replace(candidate_line + "\n\n", "", 1) != deployed_text:
            errors.append("naturalness v5 candidate must differ from the deployed skill by exactly the registered line")
    except OSError as exc:
        errors.append(f"invalid naturalness v5 candidate skill: {exc}")

    tuning_meta_paths = list((NATURALNESS_V5 / "cli-results").rglob("run-*.json"))
    tuning_meta_paths += list((NATURALNESS_V5 / "ollama-results").rglob("run-*.json"))
    try:
        tuning_runs = [json.loads(path.read_text(encoding="utf-8-sig")) for path in tuning_meta_paths]
        if len(tuning_runs) != 60:
            errors.append(f"expected 60 naturalness v5 runs, found {len(tuning_runs)}")
        if any(run.get("transport_status") != "completed" for run in tuning_runs):
            errors.append("naturalness v5 contains an incomplete transport record")
        triples = {(run.get("model"), run.get("variant"), run.get("run")) for run in tuning_runs}
        models = {run.get("model") for run in tuning_runs}
        if len(models) != 10 or len(triples) != 60:
            errors.append(f"unexpected naturalness v5 model/variant/run coverage: {len(models)} models, {len(triples)} triples")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid naturalness v5 run metadata: {exc}")

    for mode in ("exact", "patterns"):
        try:
            score = json.loads((NATURALNESS_V5 / f"scores-{mode}.json").read_text(encoding="utf-8"))
            if score.get("coverage_mode") != mode:
                errors.append(f"naturalness v5 scores-{mode}.json has the wrong coverage mode")
            if len(score.get("records", [])) != 60:
                errors.append(f"naturalness v5 scores-{mode}.json must contain 60 records")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid naturalness v5 scores-{mode}.json: {exc}")

    try:
        decision = json.loads((NATURALNESS_V5 / "adoption-decision.json").read_text(encoding="utf-8"))
        if decision.get("decision") != "hold" or len(decision.get("checks", [])) != 6:
            errors.append("naturalness v5 adoption decision must be hold with six checks")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid naturalness v5 adoption decision: {exc}")

    if errors:
        print("Evaluation set validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {count} baseline cases and naturalness v4/v5 artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
