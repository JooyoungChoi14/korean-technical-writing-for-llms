#!/usr/bin/env python3
"""Join public benchmark cohorts to prompt-ladder outcomes.

The script intentionally computes correlations only within each source table.
It does not merge scores reported under different harnesses.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import mean


def pearson(xs: list[float], ys: list[float]) -> float | None:
    x_mean = mean(xs)
    y_mean = mean(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - x_mean) ** 2 for x in xs)
        * sum((y - y_mean) ** 2 for y in ys)
    )
    return numerator / denominator if denominator else None


def average_ranks(values: list[float]) -> list[float]:
    ordered = sorted(values)
    return [
        mean(index + 1 for index, candidate in enumerate(ordered) if candidate == value)
        for value in values
    ]


def rounded(value: float | None) -> float | None:
    return round(value, 3) if value is not None else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", type=Path, required=True)
    parser.add_argument("--aggregate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    context = json.loads(args.context.read_text(encoding="utf-8"))
    aggregate = json.loads(args.aggregate.read_text(encoding="utf-8"))
    outcomes = {item["model"]: item["variants"] for item in aggregate["models"]}

    analyses = []
    for cohort in context["cohorts"]:
        rows = []
        for entry in cohort["entries"]:
            variants = outcomes[entry["model"]]
            rows.append(
                {
                    **entry,
                    "baseline_passed_of_3": variants["baseline"]["passed"],
                    "task_specific_passed_of_3": variants["task-specific"]["passed"],
                }
            )

        scores = [row["score"] for row in rows]
        baseline = [row["baseline_passed_of_3"] for row in rows]
        task_specific = [row["task_specific_passed_of_3"] for row in rows]
        analyses.append(
            {
                "id": cohort["id"],
                "benchmark": cohort["benchmark"],
                "source": cohort["source"],
                "n": len(rows),
                "rows": rows,
                "correlations": {
                    "baseline": {
                        "pearson": rounded(pearson(scores, baseline)),
                        "spearman": rounded(
                            pearson(average_ranks(scores), average_ranks(baseline))
                        ),
                    },
                    "task-specific": {
                        "pearson": rounded(pearson(scores, task_specific)),
                        "spearman": rounded(
                            pearson(
                                average_ranks(scores), average_ranks(task_specific)
                            )
                        ),
                    },
                },
            }
        )

    result = {
        "generated_from": {
            "context": str(args.context.name),
            "aggregate": str(args.aggregate.name),
        },
        "warning": "소표본 탐색값이며 통계적 유의성, 인과성 또는 모델 순위를 뜻하지 않는다.",
        "cohorts": analyses,
    }
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
