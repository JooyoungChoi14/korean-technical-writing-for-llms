#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


def parse_output(raw: str) -> dict:
    raw = raw.lstrip("\ufeff").strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, re.S | re.I)
    if fenced:
        raw = fenced.group(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return json.loads(raw[raw.find("{"):raw.rfind("}") + 1])


def summarize(rows: list[dict]) -> dict:
    proposition_total = sum(row["proposition_total"] for row in rows)
    item_total = len(rows)
    return {
        "items": item_total,
        "items_with_two_judges": sum(row["judge_count"] == 2 for row in rows),
        "propositions": proposition_total,
        "strict_propositions": sum(row["strict_propositions"] for row in rows),
        "liberal_propositions": sum(row["liberal_propositions"] for row in rows),
        "agreed_propositions": sum(row["agreed_propositions"] for row in rows),
        "complete_reconstructions": sum(row["complete_reconstruction"] for row in rows),
        "actor_action_explicit": sum(row["actor_action_explicit"] for row in rows),
        "awkward_removed": sum(row["awkward_removed"] for row in rows),
        "strict_proposition_recall": round(sum(row["strict_propositions"] for row in rows) / proposition_total, 4) if proposition_total else 0,
        "liberal_proposition_recall": round(sum(row["liberal_propositions"] for row in rows) / proposition_total, 4) if proposition_total else 0,
        "judge_agreement": round(sum(row["agreed_propositions"] for row in rows) / proposition_total, 4) if proposition_total else 0,
        "complete_reconstruction_rate": round(sum(row["complete_reconstruction"] for row in rows) / item_total, 4) if item_total else 0,
        "actor_action_explicit_rate": round(sum(row["actor_action_explicit"] for row in rows) / item_total, 4) if item_total else 0,
        "awkward_removal_rate": round(sum(row["awkward_removed"] for row in rows) / item_total, 4) if item_total else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--judge-results", type=Path, required=True)
    parser.add_argument("--v5-scores", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    v5_scores = json.loads(args.v5_scores.read_text(encoding="utf-8-sig"))
    judgments: dict[str, dict[str, dict]] = defaultdict(dict)
    transport = []
    for meta_path in sorted(args.judge_results.rglob("batch-*.meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
        output_path = meta_path.with_name(meta_path.name.replace(".meta.json", ".output.json"))
        transport.append(meta)
        if meta.get("transport_status") != "completed" or not output_path.exists():
            continue
        try:
            payload = parse_output(output_path.read_text(encoding="utf-8-sig"))
        except Exception:
            continue
        for judgment in payload.get("judgments", []):
            judgments[str(judgment.get("item_id"))][meta["judge"]] = judgment

    rows = []
    for item in manifest["items"]:
        item_judgments = judgments.get(item["item_id"], {})
        proposition_results = []
        for proposition in item["propositions"]:
            values = []
            for judgment in item_judgments.values():
                by_id = {entry.get("id"): bool(entry.get("explicitly_entailed")) for entry in judgment.get("propositions", [])}
                if proposition["id"] in by_id:
                    values.append(by_id[proposition["id"]])
            proposition_results.append({
                "id": proposition["id"],
                "role": proposition["role"],
                "text": proposition["text"],
                "values": values,
                "strict": len(values) == 2 and all(values),
                "liberal": len(values) == 2 and any(values),
                "agreed": len(values) == 2 and values[0] == values[1],
            })
        actor_values = [bool(judgment.get("actor_and_action_explicit")) for judgment in item_judgments.values()]
        strict_count = sum(prop["strict"] for prop in proposition_results)
        row = {
            **{key: item[key] for key in ("item_id", "source_agent", "source_model", "source_variant", "source_run", "case_id", "revision", "awkward_removed")},
            "judges": sorted(item_judgments),
            "judge_count": len(item_judgments),
            "proposition_total": len(proposition_results),
            "strict_propositions": strict_count,
            "liberal_propositions": sum(prop["liberal"] for prop in proposition_results),
            "agreed_propositions": sum(prop["agreed"] for prop in proposition_results),
            "complete_reconstruction": len(item_judgments) == 2 and strict_count == len(proposition_results),
            "actor_action_explicit": len(actor_values) == 2 and all(actor_values),
            "proposition_results": proposition_results,
        }
        rows.append(row)

    grouped = defaultdict(list)
    model_grouped = defaultdict(list)
    case_grouped = defaultdict(list)
    for row in rows:
        grouped[row["source_variant"]].append(row)
        model_grouped[(row["source_model"], row["source_variant"])].append(row)
        case_grouped[(row["case_id"], row["source_variant"])].append(row)
    control_precision = {row["variant"]: row["control_precision"] for row in v5_scores["summary"]}
    summary = [{"variant": key, **summarize(value), "control_precision": control_precision[key]} for key, value in sorted(grouped.items())]
    per_model = [{"model": key[0], "variant": key[1], **summarize(value)} for key, value in sorted(model_grouped.items())]
    per_case = [{"case_id": key[0], "variant": key[1], **summarize(value)} for key, value in sorted(case_grouped.items())]
    by_variant = {row["variant"]: row for row in summary}
    baseline = by_variant["baseline"]
    candidate = by_variant["candidate"]
    agreement_ok = min(baseline["judge_agreement"], candidate["judge_agreement"]) >= 0.80
    checks = {
        "judge_agreement_at_least_80pct": agreement_ok,
        "strict_proposition_gain_at_least_5pp": candidate["strict_proposition_recall"] - baseline["strict_proposition_recall"] >= 0.05,
        "complete_reconstruction_gain_at_least_3pp": candidate["complete_reconstruction_rate"] - baseline["complete_reconstruction_rate"] >= 0.03,
    }
    signal = "aligned" if all(checks.values()) else ("unstable" if not agreement_ok else "no_signal")
    result = {"meta_signal": signal, "checks": checks, "transport": transport, "summary": summary, "per_model": per_model, "per_case": per_case, "records": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Scored {len(rows)} source revisions: {signal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
