#!/usr/bin/env python3
"""K149 policy-representation opponent embedding — clean-room (methods-only).

Steals the *idea* from arXiv:2607.01498 "Towards Learning Representations of
Policies in Two-Player Zero-Sum Imperfect-Information Games" (CC BY 4.0 paper):
encode a *policy* by its behaviour, not by states. The reference repo
`VitamintK/ssl-project` has **no LICENSE** — this is a clean-room implementation
from the described method, no upstream code copied.

Approach (offline, no Arena API):
  1. Probe battery — a fixed set of canonical HU/6-max tables (regression spots).
  2. For each opponent archetype bot, tally its action mix on the battery.
  3. Embedding = normalized action-frequency vector bucketed by street x facing-bet.
  4. Downstream evals:
       a. cluster archetypes; verify aggressive vs passive separation.
       b. nearest-neighbour payoff predictor from embedding vs global-mean baseline.

Usage:
    uv run python scripts/policy_ssl_embedding.py
    uv run python scripts/policy_ssl_embedding.py --hands 200 --json-out /tmp/ssl.json
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
for p in (ROOT, ROOT / "examples"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from selfplay import BOT_POOL, _opponents_for_selfplay, play_one_hand  # noqa: E402

# Archetypes we build policy embeddings for (each is a fixed villain bot).
DEFAULT_ARCHETYPES = ("tight", "rock", "maniac", "lag", "loose", "call")
AGGRESSIVE = frozenset({"maniac", "lag"})

ACTION_RAISE = frozenset({"bet", "raise", "all-in"})
EMBED_KEYS = (
    "pre_raise", "pre_call", "pre_fold",
    "post_raise", "post_call", "post_fold",
    "facing_bet_fold", "facing_bet_raise",
)


def _probe_battery() -> list[dict]:
    """Canonical arena tables from frozen regression spots (dev-time only)."""
    from tests.fixtures.hu_regression_spots import hu_regression_spots
    from tests.fixtures.regression_spots import regression_spots

    tables = [s.table for s in hu_regression_spots()]
    tables += [s.table for s in regression_spots()]
    return tables


def _is_preflop(table: dict) -> bool:
    return str(table.get("street") or table.get("phase") or "").lower() in ("preflop", "")


def _call_chips(table: dict) -> int:
    allowed = table.get("allowedActions") or {}
    for key in ("callChips", "toCall", "call_to", "callAmount"):
        val = allowed.get(key)
        if isinstance(val, (int, float)) and val > 0:
            return int(val)
    return 0


def policy_embedding(bot: Callable, battery: list[dict], *, seed: int = 42) -> list[float]:
    """Behavioural policy embedding: bucketed action frequencies over the battery."""
    rng = random.Random(seed)
    tally = {k: 0.0 for k in EMBED_KEYS}
    pre_n = post_n = facing_n = 0.0

    for table in battery:
        # Bots may use randomness; seed the module RNG deterministically per table.
        random.seed(rng.randint(0, 2**31 - 1))
        try:
            out = bot(table) or {}
        except Exception:
            continue
        act = str(out.get("action") or "").lower()
        if not act:
            continue
        facing = _call_chips(table) > 0
        pre = _is_preflop(table)
        bucket = "pre" if pre else "post"
        if bucket == "pre":
            pre_n += 1
        else:
            post_n += 1
        if act in ACTION_RAISE:
            tally[f"{bucket}_raise"] += 1
        elif act in ("call", "check"):
            tally[f"{bucket}_call"] += 1
        elif act == "fold":
            tally[f"{bucket}_fold"] += 1
        if facing:
            facing_n += 1
            if act == "fold":
                tally["facing_bet_fold"] += 1
            elif act in ACTION_RAISE:
                tally["facing_bet_raise"] += 1

    def _norm(v: float, d: float) -> float:
        return v / d if d > 0 else 0.0

    return [
        _norm(tally["pre_raise"], pre_n),
        _norm(tally["pre_call"], pre_n),
        _norm(tally["pre_fold"], pre_n),
        _norm(tally["post_raise"], post_n),
        _norm(tally["post_call"], post_n),
        _norm(tally["post_fold"], post_n),
        _norm(tally["facing_bet_fold"], facing_n),
        _norm(tally["facing_bet_raise"], facing_n),
    ]


def _dist(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def _aggression_score(embed: list[float]) -> float:
    """Linear probe on the policy embedding: raise-frequency across buckets."""
    # pre_raise + post_raise + facing_bet_raise (indices 0, 3, 7).
    return embed[0] + embed[3] + embed[7]


def _payoff_vs(archetype: str, hands: int, seed: int) -> float:
    """Hero (cemini_decide) bb/100 vs this archetype — downstream target."""
    from cemini_decide import decide as hero_decide

    opponents = _opponents_for_selfplay(2, archetype)
    rng = random.Random(seed)
    total = 0
    bb = 2
    for hand_id in range(1, hands + 1):
        hero_idx = rng.randint(0, 1)
        total += play_one_hand(
            hero_decide, opponents, 200, 1, bb, hand_id, hero_idx=hero_idx,
        )
    return round((total / max(hands, 1)) * (100.0 / bb), 3)


def nn_payoff_mae(embeds: dict[str, list[float]], payoffs: dict[str, float]) -> dict[str, float]:
    """Leave-one-out nearest-neighbour payoff predictor vs global-mean baseline."""
    names = list(embeds)
    if len(names) < 3:
        return {"nn_mae": 0.0, "baseline_mae": 0.0, "beats_baseline": False}
    nn_err = base_err = 0.0
    for held in names:
        others = [n for n in names if n != held]
        nearest = min(others, key=lambda n: _dist(embeds[held], embeds[n]))
        nn_err += abs(payoffs[held] - payoffs[nearest])
        mean_others = sum(payoffs[n] for n in others) / len(others)
        base_err += abs(payoffs[held] - mean_others)
    nn_mae = nn_err / len(names)
    base_mae = base_err / len(names)
    return {
        "nn_mae": round(nn_mae, 3),
        "baseline_mae": round(base_mae, 3),
        "beats_baseline": nn_mae <= base_mae,
    }


def run(archetypes: tuple[str, ...] = DEFAULT_ARCHETYPES, *, hands: int = 150,
        seed: int = 42, with_payoff: bool = True) -> dict[str, Any]:
    battery = _probe_battery()
    archetypes = tuple(a for a in archetypes if a in BOT_POOL)
    embeds = {a: policy_embedding(BOT_POOL[a], battery, seed=seed) for a in archetypes}

    # Downstream linear probe: does a raise-frequency projection separate
    # aggressive archetypes from the rest? (paper-style embedding eval)
    aggro = [a for a in archetypes if a in AGGRESSIVE]
    passive = [a for a in archetypes if a not in AGGRESSIVE]
    scores = {a: round(_aggression_score(embeds[a]), 4) for a in archetypes}
    min_aggro = min((scores[a] for a in aggro), default=None)
    max_passive = max((scores[a] for a in passive), default=None)
    separates = bool(aggro and passive) and min_aggro > max_passive

    report: dict[str, Any] = {
        "note": "clean-room; VitamintK/ssl-project has no LICENSE — methods-only",
        "embed_keys": list(EMBED_KEYS),
        "archetypes": list(archetypes),
        "embeddings": {a: [round(v, 4) for v in e] for a, e in embeds.items()},
        "aggression_probe": {
            "scores": scores,
            "min_aggressive_score": min_aggro,
            "max_passive_score": max_passive,
            "separates": separates,
        },
        "battery_size": len(battery),
    }
    if with_payoff:
        payoffs = {a: _payoff_vs(a, hands, seed) for a in archetypes}
        report["payoff_bb_per_100"] = payoffs
        report["nn_payoff_predictor"] = nn_payoff_mae(embeds, payoffs)
    return report


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="K149 clean-room policy embedding")
    p.add_argument("--hands", type=int, default=150)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--no-payoff", action="store_true", help="Skip selfplay payoff eval (fast)")
    p.add_argument("--json-out", type=str, default="")
    args = p.parse_args(argv)

    report = run(hands=args.hands, seed=args.seed, with_payoff=not args.no_payoff)
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
