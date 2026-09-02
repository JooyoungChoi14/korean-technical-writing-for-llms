#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    scores = json.loads(args.scores.read_text(encoding="utf-8-sig"))
    if scores.get("coverage_mode") != "patterns":
        raise SystemExit("The adoption decision requires patterns coverage mode.")

    summaries = {row["variant"]: row for row in scores["summary"]}
    baseline = summaries["baseline"]
    candidate = summaries["candidate"]
    per_model = {(row["model"], row["variant"]): row for row in scores["per_model"]}
    models = sorted({model for model, _ in per_model})

    model_deltas = []
    non_decrease = 0
    improved = 0
    for model in models:
        before = per_model[(model, "baseline")]["successful_rewrite_rate"]
        after = per_model[(model, "candidate")]["successful_rewrite_rate"]
        delta = round(after - before, 4)
        non_decrease += delta >= 0
        improved += delta > 0
        model_deltas.append({"model": model, "baseline": before, "candidate": after, "delta": delta})

    checks = [
        {
            "id": "semantic_coverage_gain",
            "passed": candidate["semantic_coverage_rate"] - baseline["semantic_coverage_rate"] >= 0.10,
            "actual_delta": round(candidate["semantic_coverage_rate"] - baseline["semantic_coverage_rate"], 4),
            "threshold": ">= 0.10",
        },
        {
            "id": "successful_rewrite_gain",
            "passed": candidate["successful_rewrite_rate"] - baseline["successful_rewrite_rate"] >= 0.08,
            "actual_delta": round(candidate["successful_rewrite_rate"] - baseline["successful_rewrite_rate"], 4),
            "threshold": ">= 0.08",
        },
        {
            "id": "awkward_removal_noninferiority",
            "passed": candidate["awkward_removal_rate"] - baseline["awkward_removal_rate"] >= -0.02,
            "actual_delta": round(candidate["awkward_removal_rate"] - baseline["awkward_removal_rate"], 4),
            "threshold": ">= -0.02",
        },
        {
            "id": "control_precision",
            "passed": candidate["control_precision"] >= 0.95 and candidate["control_precision"] - baseline["control_precision"] >= -0.02,
            "candidate": candidate["control_precision"],
            "actual_delta": round(candidate["control_precision"] - baseline["control_precision"], 4),
            "threshold": ">= 0.95 and delta >= -0.02",
        },
        {
            "id": "semantic_safety",
            "passed": candidate["semantic_safety_rate"] >= 0.99,
            "candidate": candidate["semantic_safety_rate"],
            "threshold": ">= 0.99",
        },
        {
            "id": "model_distribution",
            "passed": non_decrease >= 6 and improved >= 4,
            "non_decrease": non_decrease,
            "improved": improved,
            "threshold": "non_decrease >= 6 and improved >= 4",
        },
    ]

    result = {
        "decision": "adopt" if all(check["passed"] for check in checks) else "hold",
        "checks": checks,
        "baseline": baseline,
        "candidate": candidate,
        "model_deltas": model_deltas,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(result["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
