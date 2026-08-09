"""Postflop telemetry rollup — pure fold-to-cbet helpers over export jsonl rows.

P1-4: enrich postflop_decisions.jsonl rows (facing_bet / board_len / pot_odds /
hand_class) and expose a pure fold-to-cbet rollup for the next climb loop.
"""
from __future__ import annotations

from typing import Any


def fold_to_cbet_rate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Fold% when facing a flop cbet.

    Filters to flop rows where ``facing_bet`` is truthy (hero faced a bet/raise),
    then computes the share that folded vs called/raised. Returns counts + rate.
    """
    facing: list[dict[str, Any]] = []
    for row in rows:
        if (row.get("street") or "").lower() != "flop":
            continue
        if not row.get("facing_bet"):
            continue
        facing.append(row)
    folds = [r for r in facing if (r.get("action") or "").lower() == "fold"]
    calls = [
        r for r in facing
        if (r.get("action") or "").lower() in ("call", "raise")
    ]
    total = len(facing)
    rate = (len(folds) / total) if total else 0.0
    return {
        "flop_facing": total,
        "fold": len(folds),
        "call_raise": len(calls),
        "fold_to_cbet_rate": rate,
    }
