from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.jsonl"
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

    if errors:
        print("Evaluation set validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {count} evaluation cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
