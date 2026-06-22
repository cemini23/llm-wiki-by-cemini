#!/usr/bin/env python3
"""Offline trajectory-bound report for selfplay JSONL exports."""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import cemini_trajectory_bound  # noqa: E402


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def load_config(path: Path | None) -> dict[str, Any]:
    if path is None:
        return cemini_trajectory_bound.merged_config(None)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("--config must point to a JSON object")
    return cemini_trajectory_bound.merged_config(data)


def group_decisions_by_hand(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("record_type") != "decision":
            continue
        hand_id = row.get("hand_id")
        if hand_id is None:
            continue
        grouped[str(hand_id)].append(row)
    return dict(grouped)


def build_summary(rows: list[dict[str, Any]], config: dict[str, Any]) -> dict[str, Any]:
    tau = float(config.get("tau", 0.05))
    mode = str(config.get("mode") or "independent")
    per_hand: list[dict[str, Any]] = []

    for hand_id, decisions in sorted(
        group_decisions_by_hand(rows).items(),
        key=lambda item: _hand_sort_key(item[0]),
    ):
        decision_bounds = cemini_trajectory_bound.per_decision_bounds_trajectory(decisions, config)
        r_star = cemini_trajectory_bound.propagate_trajectory(decision_bounds, config)
        per_hand.append({
            "hand_id": _json_hand_id(hand_id),
            "r_star": r_star,
            "breached": r_star > tau,
            "decision_count": len(decisions),
        })

    return {
        "per_hand": per_hand,
        "totals": {
            "hand_count": len(per_hand),
            "decision_count": sum(h["decision_count"] for h in per_hand),
            "breach_count": sum(1 for h in per_hand if h["breached"]),
            "tau": tau,
            "mode": mode,
        },
    }


def write_summary(summary: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "trajectory_bound_summary.json"
    out_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline selfplay trajectory bound report")
    parser.add_argument("--selfplay", type=Path, required=True, help="selfplay trajectory JSONL")
    parser.add_argument("--config", type=Path, default=None, help="optional JSON bound config")
    parser.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="directory for trajectory_bound_summary.json",
    )
    args = parser.parse_args(argv)

    config = load_config(args.config)
    summary = build_summary(load_jsonl(args.selfplay), config)
    out_path = write_summary(summary, args.out_dir)
    totals = summary["totals"]
    print(
        "[trajectory-bound] "
        f"wrote {out_path} hands={totals['hand_count']} breaches={totals['breach_count']}"
    )
    return 0


def _hand_sort_key(hand_id: str) -> tuple[int, int | str]:
    try:
        return (0, int(hand_id))
    except ValueError:
        return (1, hand_id)


def _json_hand_id(hand_id: str) -> int | str:
    try:
        return int(hand_id)
    except ValueError:
        return hand_id


if __name__ == "__main__":
    raise SystemExit(main())
