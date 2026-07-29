#!/usr/bin/env python3
"""Offline agreement gate: held-out TexasSolver dumps vs baked blueprint v3.

Re-aggregates per-hand-bucket freqs from cached dumps and compares to
``research/postflop_hu_buckets_v3.json`` using total variation distance.
Free nodes (combos≥20): also track argmax action agreement.

PASS when mean TV ≤ 0.25 AND free-node argmax agreement ≥ 0.55.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from bake_blueprint_v3 import (  # noqa: E402
    DEFAULT_DUMP_DIR,
    DEFAULT_GRID,
    DEFAULT_OUT,
    accumulate_v3_node,
    extract_v3_nodes,
    finalize_v3,
    spot_cache_key,
)
from bake_texassolver_buckets import load_dump, parse_board  # noqa: E402
from solver_policy_v3 import FACING_ACTIONS, FREE_ACTIONS  # noqa: E402

DEFAULT_REPORT = _ROOT / "reports" / "blueprint-v3-agreement.json"

MEAN_TV_PASS = 0.25
ARGMAX_AGREE_PASS = 0.55
MIN_COMBOS_ARGMAX = 20


def total_variation_distance(
    freqs_a: dict[str, float],
    freqs_b: dict[str, float],
    action_keys: tuple[str, ...] | list[str],
) -> float:
    """Total variation distance between two action frequency vectors."""
    total = 0.0
    for key in action_keys:
        total += abs(float(freqs_a.get(key, 0.0)) - float(freqs_b.get(key, 0.0)))
    return total / 2.0


def _argmax_action(freqs: dict[str, float]) -> str:
    return max(freqs, key=lambda k: float(freqs.get(k, 0.0)))


def aggregate_spot_from_dump(
    spot: dict[str, Any],
    dump_path: Path,
    defaults: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    """Re-aggregate v3 bucket keys for one spot from a solver dump."""
    street = str(spot.get("street") or "flop").lower()
    texture = str(spot.get("texture") or "dry").lower()
    line = str(spot.get("line") or defaults.get("line") or "srp").lower()
    spr = str(spot.get("spr") or "2to5").lower()
    board = parse_board(spot)
    pot = float(spot.get("pot", defaults.get("pot", 20)))

    root = load_dump(dump_path)
    nodes = extract_v3_nodes(root, pot=pot)

    acc: dict[str, dict[str, float]] = {}
    combo_acc: dict[str, int] = defaultdict(int)
    mass_acc: dict[str, float] = defaultdict(float)

    for role, node_label, node_dict in nodes:
        accumulate_v3_node(
            acc,
            combo_acc,
            mass_acc,
            street=street,
            line=line,
            role=role,
            texture=texture,
            spr=spr,
            node=node_label,
            board=board,
            node_dict=node_dict,
            pot=pot,
        )

    return finalize_v3(acc, combo_acc, mass_acc)


def resolve_dump_path(
    spot: dict[str, Any],
    defaults: dict[str, Any],
    dump_dir: Path,
) -> Optional[Path]:
    sid = str(spot.get("id") or spot.get("board"))
    ck = spot_cache_key(spot, defaults)
    dump_path = dump_dir / f"{sid}_{ck}.json"
    if dump_path.is_file() and dump_path.stat().st_size > 50:
        return dump_path
    return None


def select_holdout_spots(
    spots: list[dict[str, Any]],
    defaults: dict[str, Any],
    dump_dir: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Hold out last ~20% of grid spots or any spot with ``_gt5`` suffix."""
    with_dump: list[dict[str, Any]] = []
    for spot in spots:
        if resolve_dump_path(spot, defaults, dump_dir):
            with_dump.append(spot)

    n = len(spots)
    last_cut = max(1, int(n * 0.8))
    last_20_ids = {str(s.get("id")) for s in spots[last_cut:]}

    holdout: list[dict[str, Any]] = []
    train: list[dict[str, Any]] = []
    for spot in with_dump:
        sid = str(spot.get("id") or "")
        if sid in last_20_ids or "_gt5" in sid:
            holdout.append(spot)
        else:
            train.append(spot)
    return holdout, train


def compare_spot_to_baked(
    spot_buckets: dict[str, dict[str, Any]],
    baked_buckets: dict[str, dict[str, Any]],
) -> tuple[list[float], list[bool]]:
    """Return per-key TV distances and free-node argmax agreement flags."""
    tv_distances: list[float] = []
    argmax_agreements: list[bool] = []

    for key, dump_entry in spot_buckets.items():
        baked_entry = baked_buckets.get(key)
        if not baked_entry:
            continue

        dump_freqs = dump_entry.get("freqs") or {}
        baked_freqs = baked_entry.get("freqs") or {}
        node = str(dump_entry.get("node") or key.split("|")[5])
        facing = node != "free"
        action_keys = FACING_ACTIONS if facing else FREE_ACTIONS

        tv = total_variation_distance(dump_freqs, baked_freqs, action_keys)
        tv_distances.append(tv)

        if not facing:
            combos = int(dump_entry.get("combos") or baked_entry.get("combos") or 0)
            if combos >= MIN_COMBOS_ARGMAX:
                agree = _argmax_action(dump_freqs) == _argmax_action(baked_freqs)
                argmax_agreements.append(agree)

    return tv_distances, argmax_agreements


def run_gate(
    *,
    baked_path: Path,
    grid_path: Path,
    dump_dir: Path,
    report_path: Path,
) -> dict[str, Any]:
    baked = json.loads(baked_path.read_text(encoding="utf-8"))
    baked_buckets = baked.get("buckets") or {}

    grid = json.loads(grid_path.read_text(encoding="utf-8"))
    defaults = grid.get("defaults") or {}
    spots = list(grid.get("spots") or [])

    holdout, train = select_holdout_spots(spots, defaults, dump_dir)

    all_tv: list[float] = []
    all_argmax: list[bool] = []
    spot_results: list[dict[str, Any]] = []

    for spot in holdout:
        sid = str(spot.get("id") or spot.get("board"))
        dump_path = resolve_dump_path(spot, defaults, dump_dir)
        if dump_path is None:
            continue
        try:
            spot_buckets = aggregate_spot_from_dump(spot, dump_path, defaults)
        except Exception as exc:
            spot_results.append({"spot_id": sid, "error": str(exc)})
            continue

        tv_list, argmax_list = compare_spot_to_baked(spot_buckets, baked_buckets)
        all_tv.extend(tv_list)
        all_argmax.extend(argmax_list)
        spot_results.append(
            {
                "spot_id": sid,
                "keys_compared": len(tv_list),
                "mean_tv": (sum(tv_list) / len(tv_list)) if tv_list else None,
                "free_argmax_agree_rate": (
                    sum(argmax_list) / len(argmax_list) if argmax_list else None
                ),
            }
        )

    mean_tv = sum(all_tv) / len(all_tv) if all_tv else float("inf")
    argmax_rate = sum(all_argmax) / len(all_argmax) if all_argmax else 0.0

    passed = mean_tv <= MEAN_TV_PASS and argmax_rate >= ARGMAX_AGREE_PASS

    report: dict[str, Any] = {
        "schema": "blueprint-v3-agreement-gate.v1",
        "date": date.today().isoformat(),
        "baked_path": str(baked_path.as_posix()),
        "grid_path": str(grid_path.as_posix()),
        "dump_dir": str(dump_dir.as_posix()),
        "thresholds": {
            "mean_tv_max": MEAN_TV_PASS,
            "free_argmax_agree_min": ARGMAX_AGREE_PASS,
            "min_combos_argmax": MIN_COMBOS_ARGMAX,
        },
        "holdout_count": len(holdout),
        "train_with_dump_count": len(train),
        "keys_compared": len(all_tv),
        "free_argmax_keys": len(all_argmax),
        "mean_tv": mean_tv,
        "free_argmax_agreement_rate": argmax_rate,
        "pass": passed,
        "spots": spot_results,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Blueprint v3 offline agreement gate")
    ap.add_argument("--baked", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--grid", type=Path, default=DEFAULT_GRID)
    ap.add_argument("--dump-dir", type=Path, default=DEFAULT_DUMP_DIR)
    ap.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = ap.parse_args(argv)

    if not args.baked.is_file():
        print(f"FAIL: baked JSON missing: {args.baked}", file=sys.stderr)
        return 1

    report = run_gate(
        baked_path=Path(args.baked),
        grid_path=Path(args.grid),
        dump_dir=Path(args.dump_dir),
        report_path=Path(args.report),
    )

    status = "PASS" if report["pass"] else "FAIL"
    print(
        f"[blueprint-v3-agreement] {status} "
        f"mean_tv={report['mean_tv']:.4f} "
        f"free_argmax={report['free_argmax_agreement_rate']:.4f} "
        f"holdout={report['holdout_count']} keys={report['keys_compared']}"
    )
    print(f"report → {args.report}")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
