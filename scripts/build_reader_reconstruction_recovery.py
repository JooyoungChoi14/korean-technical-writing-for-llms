#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def parse_output(raw: str) -> dict:
    raw = raw.lstrip("\ufeff").strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, re.S | re.I)
    if fenced:
        raw = fenced.group(1)
    return json.loads(raw)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--judge", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=5)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    config = manifest["judges"][args.judge]
    expected = {
        item["item_id"]: item
        for item in manifest["items"]
        if item["source_agent"] in config["accepts"]
    }
    valid: set[str] = set()
    for meta_path in args.results.rglob("*.meta.json"):
        meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
        if meta.get("judge") != args.judge or meta.get("transport_status") != "completed":
            continue
        output_path = meta_path.with_name(meta_path.name.replace(".meta.json", ".output.json"))
        if not output_path.exists():
            continue
        try:
            payload = parse_output(output_path.read_text(encoding="utf-8-sig"))
        except (ValueError, json.JSONDecodeError):
            continue
        for judgment in payload.get("judgments", []):
            item_id = str(judgment.get("item_id"))
            if item_id not in expected:
                continue
            expected_props = {prop["id"] for prop in expected[item_id]["propositions"]}
            actual_props = {str(prop.get("id")) for prop in judgment.get("propositions", [])}
            if actual_props == expected_props and isinstance(judgment.get("actor_and_action_explicit"), bool):
                valid.add(item_id)

    missing = [item for item_id, item in expected.items() if item_id not in valid]
    judge_dir = args.output / args.judge
    judge_dir.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(missing), args.batch_size):
        payload = {
            "judge": args.judge,
            "items": [
                {"item_id": item["item_id"], "revision": item["revision"], "propositions": item["propositions"]}
                for item in missing[start:start + args.batch_size]
            ],
        }
        path = judge_dir / f"recovery-{start // args.batch_size + 1:03d}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{args.judge}: expected={len(expected)} valid={len(valid)} missing={len(missing)} batches={(len(missing) + args.batch_size - 1) // args.batch_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
