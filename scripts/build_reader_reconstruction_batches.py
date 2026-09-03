#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path


JUDGES = {
    "claude-fable-5": {"family": "claude", "accepts": ["codex", "ollama-cloud"]},
    "codex-gpt-5.6-sol": {"family": "codex", "accepts": ["claude", "ollama-cloud"]},
    "ollama-kimi-k3": {"family": "ollama-cloud", "accepts": ["claude", "codex"]},
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--propositions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=60)
    parser.add_argument("--seed", type=int, default=20260903)
    args = parser.parse_args()

    scores = json.loads(args.scores.read_text(encoding="utf-8-sig"))
    proposition_data = json.loads(args.propositions.read_text(encoding="utf-8-sig"))
    propositions = {case["id"]: case["propositions"] for case in proposition_data["cases"]}
    items = []
    for row in scores["records"]:
        for case in row["cases"]:
            if case["id"] not in propositions:
                continue
            stable = f'{row["agent"]}|{row["model"]}|{row["variant"]}|{row["run"]}|{case["id"]}'
            item_id = "R" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:12]
            items.append({
                "item_id": item_id,
                "source_agent": row["agent"],
                "source_model": row["model"],
                "source_variant": row["variant"],
                "source_run": row["run"],
                "case_id": case["id"],
                "revision": case["suggested_revision"],
                "awkward_removed": case["awkward_removed"],
                "propositions": propositions[case["id"]],
            })

    args.output.mkdir(parents=True, exist_ok=True)
    manifest = {"seed": args.seed, "batch_size": args.batch_size, "judges": JUDGES, "items": items, "batches": []}
    for judge_index, (judge, config) in enumerate(JUDGES.items()):
        judge_items = [item for item in items if item["source_agent"] in config["accepts"]]
        random.Random(args.seed + judge_index).shuffle(judge_items)
        judge_dir = args.output / judge
        judge_dir.mkdir(parents=True, exist_ok=True)
        for start in range(0, len(judge_items), args.batch_size):
            batch_number = start // args.batch_size + 1
            batch_items = judge_items[start:start + args.batch_size]
            batch_name = f"batch-{batch_number:02d}.json"
            payload = {
                "judge": judge,
                "items": [
                    {
                        "item_id": item["item_id"],
                        "revision": item["revision"],
                        "propositions": item["propositions"],
                    }
                    for item in batch_items
                ],
            }
            (judge_dir / batch_name).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            manifest["batches"].append({"judge": judge, "file": f"{judge}/{batch_name}", "count": len(batch_items)})

    (args.output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built {len(items)} blind items and {len(manifest['batches'])} judge batches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
