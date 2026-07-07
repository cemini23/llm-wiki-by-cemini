#!/usr/bin/env python3
"""K149 ADVENT-style predicate invention harness for poker leaks.

Steals the pattern from arXiv:2607.01585 "ADVENT: LLM-Driven Automatic
Predicate Invention for ILP": name a leak class as an interpretable predicate,
verify it with an executable check, and accumulate verified predicates in a
private knowledge pool for the next Heuristic-Learning epoch.

Here a *predicate* is a named, executable check over frozen HU regression spots:
  - `applies_to(spot)` — is this spot in the predicate's domain?
  - `fires(spot, action)` — does the leak manifest for the bot's chosen action?

A predicate is **sound / verified** when it NEVER fires on the current
known-good `decide()` (the leak it names is already guarded). Verified
predicates become regression invariants; a firing predicate is a live leak
(regression alert) and gates deploy under --gate.

Prod `decide()` is unchanged — this is offline research tooling.

Usage:
    uv run python scripts/predicate_invention.py
    uv run python scripts/predicate_invention.py --gate
    uv run python scripts/predicate_invention.py --pool research/predicates/verified_predicates.json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
for p in (ROOT, ROOT / "examples"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

DEFAULT_POOL = ROOT / "research" / "predicates" / "verified_predicates.json"

RAISE_ACTIONS = frozenset({"bet", "raise", "all-in"})
CONTINUE_ACTIONS = frozenset({"call", "bet", "raise", "all-in"})


@dataclass(frozen=True)
class Predicate:
    """A named, interpretable, executable leak descriptor (ADVENT-style)."""

    name: str
    description: str
    applies_to: Callable[[Any], bool]
    fires: Callable[[Any, str], bool]
    invented_by: str = "operator"
    tags: tuple[str, ...] = field(default_factory=tuple)


def _hole(spot: Any) -> list[str]:
    tbl = spot.table
    self_seat = tbl.get("selfSeatNumber")
    for seat in tbl.get("seats") or []:
        if seat.get("seatNumber") == self_seat and isinstance(seat.get("holeCards"), list):
            return [str(c) for c in seat["holeCards"]]
    for key in ("holeCards", "hole", "heroHole"):
        val = tbl.get(key)
        if isinstance(val, list) and val:
            return [str(c) for c in val]
    return []


def _hand_class(hole: list[str]) -> str:
    if len(hole) != 2:
        return ""
    ranks = "23456789TJQKA"
    r0, r1 = hole[0][0].upper(), hole[1][0].upper()
    suited = hole[0][-1].lower() == hole[1][-1].lower()
    if r0 == r1:
        return r0 + r1
    hi, lo = (r0, r1) if ranks.index(r0) >= ranks.index(r1) else (r1, r0)
    return f"{hi}{lo}{'s' if suited else 'o'}"


def _is_premium_pair(hc: str) -> bool:
    return hc in {"AA", "KK", "QQ"}


def _is_trash_offsuit(hc: str) -> bool:
    return hc in {"72o", "82o", "83o", "92o", "T3o", "Q5o", "J2o"}


# ─── Invented predicate pool (interpretable leak descriptors) ────────────────

def _predicate_pool() -> list[Predicate]:
    return [
        Predicate(
            name="folds_premium_bb_defend",
            description="Hero folds AA/KK/QQ in BB vs a minraise (must never fold premium).",
            applies_to=lambda s: "bb_" in s.id and _is_premium_pair(_hand_class(_hole(s))),
            fires=lambda s, a: a == "fold",
            invented_by="advent-llm-proposed",
            tags=("preflop", "bb-defend"),
        ),
        Predicate(
            name="opens_trash_sb_hu",
            description="Hero opens (raises) obvious trash offsuit from SB/BTN first-in.",
            applies_to=lambda s: "sb_" in s.id and _is_trash_offsuit(_hand_class(_hole(s))),
            fires=lambda s, a: a in RAISE_ACTIONS,
            invented_by="advent-llm-proposed",
            tags=("preflop", "open"),
        ),
        Predicate(
            name="calls_off_dominated_broadway_vs_shove",
            description="Hero calls/jams dominated offsuit broadway vs a stack-off shove.",
            applies_to=lambda s: "vs_shove" in s.id or "btn_vs_shove" in s.id,
            fires=lambda s, a: (
                a in CONTINUE_ACTIONS
                and _hand_class(_hole(s)) in {"AJo", "KQo", "KJo", "QJo"}
            ),
            invented_by="advent-llm-proposed",
            tags=("preflop", "stack-off"),
        ),
    ]


@dataclass
class PredicateResult:
    name: str
    description: str
    applicable_spots: int
    fired_spots: list[str]
    verified: bool
    tags: list[str]
    invented_by: str


def _decide_action(spot: Any) -> str:
    from tests.test_cemini_regression import _run

    return _run(spot.table, spot.context)["action"]


def evaluate(pool: list[Predicate] | None = None) -> dict[str, Any]:
    from tests.fixtures.hu_regression_spots import hu_regression_spots

    pool = pool or _predicate_pool()
    spots = hu_regression_spots()
    results: list[PredicateResult] = []

    for pred in pool:
        applicable = [s for s in spots if _safe(pred.applies_to, s)]
        fired = [s.id for s in applicable if _safe2(pred.fires, s, _decide_action(s))]
        results.append(
            PredicateResult(
                name=pred.name,
                description=pred.description,
                applicable_spots=len(applicable),
                fired_spots=fired,
                verified=(len(applicable) > 0 and not fired),
                tags=list(pred.tags),
                invented_by=pred.invented_by,
            )
        )

    verified = [r for r in results if r.verified]
    live_leaks = [r for r in results if r.fired_spots]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "predicate_count": len(results),
        "verified_count": len(verified),
        "live_leak_count": len(live_leaks),
        "results": [r.__dict__ for r in results],
        "verified_predicates": [r.name for r in verified],
        "live_leaks": [{"name": r.name, "spots": r.fired_spots} for r in live_leaks],
        "gate_pass": not live_leaks,
    }


def _safe(fn: Callable[[Any], bool], spot: Any) -> bool:
    try:
        return bool(fn(spot))
    except Exception:
        return False


def _safe2(fn: Callable[[Any, str], bool], spot: Any, action: str) -> bool:
    try:
        return bool(fn(spot, action))
    except Exception:
        return False


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="K149 ADVENT predicate invention harness")
    p.add_argument("--gate", action="store_true", help="Exit 1 if any predicate fires (live leak)")
    p.add_argument("--pool", type=Path, default=DEFAULT_POOL, help="Verified-predicate pool path")
    p.add_argument("--json-out", type=str, default="")
    args = p.parse_args(argv)

    report = evaluate()
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")

    # Accumulate verified predicates into the private knowledge pool.
    args.pool.parent.mkdir(parents=True, exist_ok=True)
    pool_payload = {
        "updated_at": report["generated_at"],
        "verified_predicates": report["verified_predicates"],
        "detail": {r["name"]: r for r in report["results"] if r["verified"]},
    }
    args.pool.write_text(json.dumps(pool_payload, indent=2) + "\n", encoding="utf-8")

    if args.gate and not report["gate_pass"]:
        print(f"GATE FAIL: {report['live_leak_count']} live leak(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
