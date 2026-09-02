#!/usr/bin/env python3
"""Score skill-effect-v2 outputs without using hidden model judgments.

This is a screening score, not a complete semantic evaluation. It checks response
structure, expected decisions, preservation anchors, requested conflict pairs, and
explicitly forbidden invented mechanisms. Shortlisted variants still require a
human or independent LLM semantic review.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from statistics import median
from pathlib import Path


VALID_DECISIONS = {"통과", "구체화 필요", "의미 확인 필요"}


def extract_json(text: str) -> dict:
    text = text.lstrip("\ufeff").strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.S | re.I)
    if fenced:
        text = fenced.group(1)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        raise


def norm(value: object) -> str:
    return "" if value is None else re.sub(r"\s+", " ", str(value)).strip()


def score_output(output_path: Path, tasks: dict) -> dict:
    result = {
        "path": str(output_path),
        "response_nonempty": False,
        "json_valid": False,
        "case_count_valid": False,
        "cases": [],
        "error": None,
    }
    text = output_path.read_text(encoding="utf-8-sig") if output_path.exists() else ""
    result["response_nonempty"] = bool(text.strip())
    if not text.strip():
        result["error"] = "empty"
        return result
    try:
        document = extract_json(text)
        answers = document.get("cases", [])
        if not isinstance(answers, list):
            raise ValueError("cases is not a list")
        result["json_valid"] = True
    except (json.JSONDecodeError, ValueError, AttributeError) as exc:
        result["error"] = f"json: {exc}"
        return result

    by_id = {str(item.get("id")): item for item in answers if isinstance(item, dict)}
    expected_ids = {case["id"] for case in tasks["cases"]}
    result["case_count_valid"] = set(by_id) == expected_ids and len(answers) == len(expected_ids)

    for case in tasks["cases"]:
        answer = by_id.get(case["id"], {})
        decision = norm(answer.get("decision"))
        revision = norm(answer.get("suggested_revision"))
        question = norm(answer.get("verification_question"))
        combined = " ".join([revision, question])
        expected = case["expected_decision"]

        decision_correct = decision == expected and decision in VALID_DECISIONS
        false_positive_free = not (
            expected == "통과" and (decision != "통과" or revision or question)
        )
        question_terms = case.get("required_question_terms", [])
        question_complete = all(term.lower() in question.lower() for term in question_terms)
        if expected == "의미 확인 필요":
            question_complete = bool(question) and question_complete
        revision_terms = case.get("required_revision_terms", [])
        revision_preserves = all(term.lower() in revision.lower() for term in revision_terms)
        if expected == "구체화 필요":
            revision_preserves = bool(revision) and revision_preserves
        forbidden = [term for term in case.get("forbidden_assumptions", []) if term.lower() in combined.lower()]
        unsupported_assumption_free = not forbidden

        dimensions = [decision_correct, false_positive_free, question_complete, revision_preserves, unsupported_assumption_free]
        applicable = [True, expected == "통과", bool(question_terms), bool(revision_terms), bool(case.get("forbidden_assumptions", []))]
        earned = sum(v for v, use in zip(dimensions, applicable) if use)
        possible = sum(applicable)
        result["cases"].append(
            {
                "id": case["id"],
                "category": case["category"],
                "expected": expected,
                "actual": decision,
                "decision_correct": decision_correct,
                "false_positive_free": false_positive_free,
                "question_complete": question_complete,
                "revision_preserves": revision_preserves,
                "unsupported_assumption_free": unsupported_assumption_free,
                "forbidden_found": forbidden,
                "earned": earned,
                "possible": possible,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    tasks = json.loads(args.tasks.read_text(encoding="utf-8-sig"))
    records = []
    for metadata_path in sorted(args.results.rglob("run-*.json")):
        metadata = json.loads(metadata_path.read_text(encoding="utf-8-sig"))
        output_path = metadata_path.with_suffix(".md")
        scored = score_output(output_path, tasks)
        scored.update({key: metadata.get(key) for key in (
            "model", "variant", "task_set", "run", "transport_status",
            "response_status", "elapsed_seconds",
        )})
        records.append(scored)

    groups: dict[tuple[str, str], dict] = defaultdict(lambda: {
        "runs": 0, "completed": 0, "json_valid": 0, "case_count_valid": 0,
        "earned": 0, "possible": 0, "decision_correct": 0, "decisions": 0,
        "clear_false_positives": 0, "clear_cases": 0,
        "unsupported_assumptions": 0, "assumption_cases": 0,
        "conflict_questions_complete": 0, "conflict_cases": 0,
    })
    for record in records:
        group = groups[(record["variant"], record["model"])]
        group["runs"] += 1
        group["completed"] += int(record["response_nonempty"])
        group["json_valid"] += int(record["json_valid"])
        group["case_count_valid"] += int(record["case_count_valid"])
        for case in record["cases"]:
            group["earned"] += case["earned"]
            group["possible"] += case["possible"]
            group["decision_correct"] += int(case["decision_correct"])
            group["decisions"] += 1
            if case["expected"] == "통과":
                group["clear_false_positives"] += int(not case["false_positive_free"])
                group["clear_cases"] += 1
            if case["category"] == "ambiguous_metaphor":
                group["unsupported_assumptions"] += int(not case["unsupported_assumption_free"])
                group["assumption_cases"] += 1
            if case["category"] == "rule_conflict":
                group["conflict_questions_complete"] += int(case["question_complete"])
                group["conflict_cases"] += 1

    summary = []
    for (variant, model), group in sorted(groups.items()):
        group.update({
            "variant": variant,
            "model": model,
            "screen_score": round(group["earned"] / group["possible"], 4) if group["possible"] else 0,
            "decision_accuracy": round(group["decision_correct"] / group["decisions"], 4) if group["decisions"] else 0,
            "clear_false_positive_rate": round(group["clear_false_positives"] / group["clear_cases"], 4) if group["clear_cases"] else 0,
            "unsupported_assumption_rate": round(group["unsupported_assumptions"] / group["assumption_cases"], 4) if group["assumption_cases"] else 0,
            "conflict_question_rate": round(group["conflict_questions_complete"] / group["conflict_cases"], 4) if group["conflict_cases"] else 0,
        })
        summary.append(group)

    aggregate = []
    for variant in sorted({item["variant"] for item in summary}):
        items = [item for item in summary if item["variant"] == variant]
        totals = {key: sum(item[key] for item in items) for key in (
            "runs", "completed", "json_valid", "case_count_valid", "earned", "possible",
            "decision_correct", "decisions", "clear_false_positives", "clear_cases",
            "unsupported_assumptions", "assumption_cases", "conflict_questions_complete",
            "conflict_cases",
        )}
        elapsed = [
            record["elapsed_seconds"] for record in records
            if record["variant"] == variant and record.get("elapsed_seconds") is not None
        ]
        totals.update({
            "variant": variant,
            "completion_rate": round(totals["completed"] / totals["runs"], 4) if totals["runs"] else 0,
            "json_valid_rate": round(totals["json_valid"] / totals["runs"], 4) if totals["runs"] else 0,
            "screen_score": round(totals["earned"] / totals["possible"], 4) if totals["possible"] else 0,
            "decision_accuracy": round(totals["decision_correct"] / totals["decisions"], 4) if totals["decisions"] else 0,
            "clear_false_positive_rate": round(totals["clear_false_positives"] / totals["clear_cases"], 4) if totals["clear_cases"] else 0,
            "unsupported_assumption_rate": round(totals["unsupported_assumptions"] / totals["assumption_cases"], 4) if totals["assumption_cases"] else 0,
            "conflict_question_rate": round(totals["conflict_questions_complete"] / totals["conflict_cases"], 4) if totals["conflict_cases"] else 0,
            "median_elapsed_seconds": round(median(elapsed), 3) if elapsed else None,
        })
        aggregate.append(totals)

    payload = {"task_set": tasks["set"], "records": records, "summary": summary, "aggregate": aggregate}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Scored {len(records)} outputs -> {args.output}")


if __name__ == "__main__":
    main()
