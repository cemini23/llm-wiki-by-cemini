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


def run_selfplay_bb100(
    *,
    hands: int,
    seed: Optional[int],
    eval_panel: bool,
) -> float:
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw = _load_decide_from_path(str(decide_path))
    decide_fn = _wrap_eval_panel(raw) if eval_panel else raw
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
    return float(rock["bb_per_100"])


def run_gate(
    *,
    hands: int,
    seed: Optional[int],
    enforce: bool,
    write_metrics: bool = False,
    baseline_bb100: Optional[float] = None,
    tournament_posture: bool = False,
) -> int:
    if not eval_panel_gate_enabled() and not enforce:
        print("eval_panel_gate: CEMINI_EVAL_PANEL_GATE off — skip")
        return 0

    floor = eval_panel_bb100_floor()
    eval_panel = not tournament_posture
    bb = run_selfplay_bb100(hands=hands, seed=seed, eval_panel=eval_panel)
    label = "tournament posture (no eval_panel)" if tournament_posture else "eval_panel_mode=ON"
    print(f"eval_panel_gate: bb/100 vs rock ({label}) = {bb:+.2f}  floor={floor:+.2f}")

    if write_metrics:
        from deploy_registry import git_commit_short, load_preflight_metrics, write_preflight_metrics

        prev = load_preflight_metrics()
        prev_bb = prev.get("eval_panel_bb100")
        if baseline_bb100 is not None:
            ref = float(baseline_bb100)
        elif prev_bb is not None:
            ref = float(prev_bb)
        else:
            ref = None
        delta = round(float(bb) - ref, 2) if ref is not None else None

        merged = {
            **prev,
            "eval_panel_floor": floor,
            "eval_panel_hands": hands,
            "commit": git_commit_short(),
        }
        if tournament_posture:
            t_prev = prev.get("tournament_bb100")
            merged["tournament_bb100"] = round(float(bb), 2)
            merged["tournament_bb100_prev"] = t_prev
            merged["tournament_bb100_pass"] = bb >= floor
            if baseline_bb100 is not None:
                merged["tournament_bb100_baseline"] = float(baseline_bb100)
                merged["tournament_bb100_delta"] = round(
                    float(bb) - float(baseline_bb100), 2
                )
            elif t_prev is not None:
                merged["tournament_bb100_delta"] = round(float(bb) - float(t_prev), 2)
        else:
            merged.update({
                "eval_panel_bb100": round(float(bb), 2),
                "eval_panel_bb100_prev": prev_bb,
                "eval_panel_bb100_delta": delta,
                "eval_panel_bb100_baseline": baseline_bb100,
                "eval_panel_pass": bb >= floor,
            })
        agent_version = os.environ.get("AGENT_VERSION", "").strip()
        if agent_version:
            merged["agent_version"] = agent_version
        path = write_preflight_metrics(merged)
        print(f"eval_panel_gate: metrics → {path}")
        if delta is not None:
            print(f"eval_panel_gate: delta vs prior/baseline = {delta:+.2f} bb/100")

    if enforce and not tournament_posture and bb < floor:
        msg = f"FAIL: {bb:+.2f} < floor {floor:+.2f}"
        print(msg)
        return 1
    if enforce and tournament_posture:
        print("tournament_posture: enforce skipped (no floor gate)")
    elif not tournament_posture and bb >= floor:
        print("PASS")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Eval-panel bb/100 gate")
    p.add_argument("--hands", type=int, default=200)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gate", action="store_true", help="Exit 1 on fail")
    p.add_argument("--write-metrics", action="store_true", help="Update reports/hl-loop/preflight_metrics.json")
    p.add_argument(
        "--baseline",
        type=float,
        default=None,
        metavar="BB100",
        help="Compare delta vs this bb/100 (e.g. pre-patch −26.67)",
    )
    p.add_argument(
        "--tournament-posture",
        action="store_true",
        help="Self-play without eval_panel_mode (equal-stack tournament lanes)",
    )
    args = p.parse_args(argv)
    return run_gate(
        hands=args.hands,
        seed=args.seed,
        enforce=args.gate,
        write_metrics=args.write_metrics,
        baseline_bb100=args.baseline,
        tournament_posture=args.tournament_posture,
    )


if __name__ == "__main__":
    raise SystemExit(main())
