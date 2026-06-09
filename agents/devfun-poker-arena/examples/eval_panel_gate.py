#!/usr/bin/env python3
"""Eval-panel self-play gate — block widen deploy until bb/100 beats floor (default −17.45).

Usage:
  uv run python examples/eval_panel_gate.py
  uv run python examples/eval_panel_gate.py --gate --hands 200
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Callable, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from selfplay import run_selfplay, _load_decide_from_path  # noqa: E402
from villain_archetype import eval_panel_bb100_floor, eval_panel_gate_enabled  # noqa: E402


def _wrap_eval_panel(decide_fn: Callable) -> Callable:
    def wrapped(table: dict, **kwargs: Any) -> dict:
        ctx = dict(kwargs.get("research_context") or {})
        ctx["eval_panel_mode"] = True
        kwargs = dict(kwargs)
        kwargs["research_context"] = ctx
        return decide_fn(table, **kwargs)

    return wrapped


def run_gate(
    *,
    hands: int,
    seed: Optional[int],
    enforce: bool,
    write_metrics: bool = False,
) -> int:
    if not eval_panel_gate_enabled() and not enforce:
        print("eval_panel_gate: CEMINI_EVAL_PANEL_GATE off — skip")
        return 0

    floor = eval_panel_bb100_floor()
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw = _load_decide_from_path(str(decide_path))
    decide_fn = _wrap_eval_panel(raw)

    os.environ.setdefault("TRAINING_OPPONENT_MODE", "rock")
    rock = run_selfplay(
        decide_fn=decide_fn,
        n_hands=hands,
        opponent_label="rock",
        n_players=6,
        starting_stack=1000,
        small_blind=10,
        big_blind=20,
        seed=seed,
        training_hud=False,
    )

    bb = rock["bb_per_100"]
    print(f"eval_panel_gate: bb/100 vs rock (eval_panel_mode=ON) = {bb:+.2f}  floor={floor:+.2f}")

    if write_metrics:
        from deploy_registry import git_commit_short, load_preflight_metrics, write_preflight_metrics

        merged = {**load_preflight_metrics(), **{
            "eval_panel_bb100": round(float(bb), 2),
            "eval_panel_floor": floor,
            "eval_panel_hands": hands,
            "eval_panel_pass": bb >= floor,
            "commit": git_commit_short(),
        }}
        path = write_preflight_metrics(merged)
        print(f"eval_panel_gate: metrics → {path}")

    if bb < floor:
        msg = f"FAIL: {bb:+.2f} < floor {floor:+.2f}"
        print(msg)
        return 1 if enforce else 0
    print("PASS")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Eval-panel bb/100 gate")
    p.add_argument("--hands", type=int, default=200)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gate", action="store_true", help="Exit 1 on fail")
    p.add_argument("--write-metrics", action="store_true", help="Update reports/hl-loop/preflight_metrics.json")
    args = p.parse_args(argv)
    return run_gate(
        hands=args.hands,
        seed=args.seed,
        enforce=args.gate,
        write_metrics=args.write_metrics,
    )


if __name__ == "__main__":
    raise SystemExit(main())
