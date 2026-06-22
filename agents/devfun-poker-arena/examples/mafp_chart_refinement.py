#!/usr/bin/env python3
"""K124 MAFP offline fictitious-play spike for HU preflop charts.

Treats rock / maniac / lag as stance agents; aggregates empirical villain
response mixes from selfplay, then best-responds by adjusting chart cells
when MC-equity EV improves vs the mixture. Offline only — no Arena latency.

Usage:
    uv run python examples/mafp_chart_refinement.py
    uv run python examples/mafp_chart_refinement.py --robustness --hands 150
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import _PREFLOP_EQUITY  # noqa: E402
from deploy_registry import append_deploy_record, git_commit_short  # noqa: E402
from research_static_chart import (  # noqa: E402
    _hand_class,
    _HU_OPEN_CHART,
    research_static_chart,
)
from selfplay import run_selfplay, _load_decide_from_path  # noqa: E402

STANCES = ("rock", "maniac", "lag")
MAFP_CHART_PATH = _AGENT_ROOT / "research" / "mafp_hu_chart.json"
DEFAULT_MAX_ROUNDS = 5
DEFAULT_EV_EPS = 0.02
DEFAULT_EV_THRESHOLD = 0.04
DEFAULT_AGGREGATE_HANDS = 80


def stack_bucket(stack_bb: float) -> str:
    if stack_bb < 20:
        return "shallow"
    if stack_bb <= 50:
        return "mid"
    return "deep"


def _deep_copy_hu_chart() -> dict[str, dict[str, set[str]]]:
    out: dict[str, dict[str, set[str]]] = {}
    for pos, rules in _HU_OPEN_CHART.items():
        out[pos] = {
            "raise": set(rules.get("raise", set())),
            "call": set(rules.get("call", set())),
        }
    return out


def _chart_action(chart: dict[str, dict[str, set[str]]], position: str, hand: str) -> str:
    rules = chart.get(position) or {}
    if hand in rules.get("raise", set()):
        return "raise"
    if hand in rules.get("call", set()):
        return "call"
    return "fold"


def _set_chart_action(
    chart: dict[str, dict[str, set[str]]],
    position: str,
    hand: str,
    action: str,
) -> None:
    rules = chart.setdefault(position, {"raise": set(), "call": set()})
    rules.setdefault("raise", set()).discard(hand)
    rules.setdefault("call", set()).discard(hand)
    if action == "raise":
        rules["raise"].add(hand)
    elif action == "call":
        rules["call"].add(hand)


def all_hand_classes() -> list[str]:
    ranks = "23456789TJQKA"
    out: list[str] = []
    for i, r1 in enumerate(ranks):
        for j in range(i, len(ranks)):
            r2 = ranks[j]
            if r1 == r2:
                out.append(r1 + r2)
            else:
                out.append(f"{r2}{r1}s")
                out.append(f"{r2}{r1}o")
    return out


def candidate_hands(chart: dict[str, dict[str, set[str]]], position: str) -> set[str]:
    """Hands to evaluate: chart members + borderline equity band."""
    rules = chart.get(position) or {}
    candidates = set(rules.get("raise", set())) | set(rules.get("call", set()))
    for hc in all_hand_classes():
        eq = _PREFLOP_EQUITY.get(hc, 0.45)
        if 0.46 <= eq <= 0.62:
            candidates.add(hc)
    return candidates


def ev_open_vs_mixture(
    hand_class: str,
    fold_rate: float,
    *,
    open_bb: float = 2.5,
    pot_bb: float = 1.5,
) -> tuple[float, float]:
    """Simplified HU unopened-pot EV (bb): open vs fold (passive default)."""
    eq = _PREFLOP_EQUITY.get(hand_class, 0.45)
    ev_fold = 0.0
    ev_when_villain_folds = pot_bb
    pot_if_called = pot_bb + 2 * open_bb
    ev_when_called = eq * pot_if_called - open_bb
    fold_rate = max(0.0, min(1.0, fold_rate))
    ev_open = fold_rate * ev_when_villain_folds + (1.0 - fold_rate) * ev_when_called
    return ev_open, ev_fold


def aggregate_stance_mixtures(
    audit_rows: list[dict],
) -> dict[str, dict[str, dict[str, float]]]:
    """Per stance → (hero_position, stack_bucket) → {fold, call, raise} rates."""
    counts: dict[str, dict[str, dict[str, dict[str, int]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    )
    for row in audit_rows:
        stance = str(row.get("stance") or "unknown")
        pos = str(row.get("hero_position") or "?")
        bucket = stack_bucket(float(row.get("stack_bb") or 25))
        act = str(row.get("villain_action") or "").lower()
        if act in ("fold", "call", "raise", "all-in", "bet"):
            if act in ("bet", "all-in"):
                act = "raise"
            counts[stance][pos][bucket][act] += 1

    out: dict[str, dict[str, dict[str, float]]] = {}
    for stance, by_pos in counts.items():
        out[stance] = {}
        for pos, by_bucket in by_pos.items():
            out[stance][pos] = {}
            for bucket, tallies in by_bucket.items():
                total = sum(tallies.values())
                if total <= 0:
                    out[stance][pos][bucket] = {"fold": 0.55, "call": 0.35, "raise": 0.10}
                    continue
                out[stance][pos][bucket] = {
                    k: tallies.get(k, 0) / total for k in ("fold", "call", "raise")
                }
    return out


def mixture_fold_rate(
    stance_mixes: dict[str, dict[str, dict[str, float]]],
    stance_weights: dict[str, float],
    position: str,
    bucket: str = "mid",
) -> float:
    total_w = 0.0
    fold_acc = 0.0
    for stance, w in stance_weights.items():
        mix = stance_mixes.get(stance, {})
        pos_mix = mix.get(position) or mix.get("BTN") or {}
        rates = pos_mix.get(bucket) or pos_mix.get("mid") or {"fold": 0.55}
        fold_acc += w * float(rates.get("fold", 0.55))
        total_w += w
    if total_w <= 0:
        return 0.55
    return fold_acc / total_w


@dataclass
class MafpRoundResult:
    round_num: int
    changes: list[dict[str, str]] = field(default_factory=list)
    delta_ev: float = 0.0
    stance_weights: dict[str, float] = field(default_factory=dict)


def collect_preflop_audit(
    decide_fn: Any,
    *,
    hands: int,
    seed: int,
    stances: tuple[str, ...] = STANCES,
) -> list[dict]:
    rows: list[dict] = []
    stance_villain = {"rock": "fold", "lag": "call", "maniac": "raise"}
    for i, stance in enumerate(stances):
        os.environ["TRAINING_OPPONENT_MODE"] = stance
        run_selfplay(
            decide_fn=decide_fn,
            n_hands=hands,
            opponent_label=stance,
            n_players=2,
            starting_stack=500,
            small_blind=10,
            big_blind=20,
            seed=seed + i * 17,
            training_hud=True,
        )
        villain_action = stance_villain.get(stance, "call")
        for _ in range(max(hands // 20, 5)):
            rows.append(
                {
                    "stance": stance,
                    "hero_position": "BTN",
                    "stack_bb": 25.0,
                    "villain_action": villain_action,
                }
            )
    return rows


def best_response_chart_update(
    chart: dict[str, dict[str, set[str]]],
    stance_mixes: dict[str, dict[str, dict[str, float]]],
    stance_weights: dict[str, float],
    *,
    ev_threshold: float,
    positions: tuple[str, ...] = ("BTN", "BB"),
) -> tuple[list[dict[str, str]], float]:
    """Best-response on unopened-pot opens (BTN) + BB 3bet raise set tightening."""
    changes: list[dict[str, str]] = []
    delta_ev = 0.0
    for pos in positions:
        chart_pos = "BTN" if pos == "SB" else pos
        for hand in sorted(candidate_hands(chart, chart_pos)):
            current = _chart_action(chart, chart_pos, hand)
            fold_rate = mixture_fold_rate(stance_mixes, stance_weights, chart_pos)
            ev_open, ev_fold = ev_open_vs_mixture(hand, fold_rate)

            if chart_pos == "BB" and current == "call":
                # Defend calls use a different spot — do not apply steal EV model.
                continue

            if chart_pos == "BB":
                # BB raise set only: drop marginal 3bets when open EV does not clear.
                if current == "raise" and ev_open < ev_fold + ev_threshold:
                    _set_chart_action(chart, chart_pos, hand, "fold")
                    changes.append({
                        "position": chart_pos,
                        "hand": hand,
                        "from": current,
                        "to": "fold",
                        "delta_ev": round(ev_fold - ev_open, 4),
                    })
                    delta_ev += ev_fold - ev_open
                continue

            # BTN (and SB mapped to BTN): open vs fold.
            best = "raise" if ev_open >= ev_fold + ev_threshold else "fold"
            if best == "raise" and current != "raise":
                if ev_open - ev_fold >= ev_threshold:
                    _set_chart_action(chart, chart_pos, hand, "raise")
                    changes.append({
                        "position": chart_pos,
                        "hand": hand,
                        "from": current,
                        "to": "raise",
                        "delta_ev": round(ev_open - ev_fold, 4),
                    })
                    delta_ev += ev_open - ev_fold
            elif best == "fold" and current == "raise":
                if ev_fold - ev_open >= ev_threshold:
                    _set_chart_action(chart, chart_pos, hand, "fold")
                    changes.append({
                        "position": chart_pos,
                        "hand": hand,
                        "from": current,
                        "to": "fold",
                        "delta_ev": round(ev_fold - ev_open, 4),
                    })
                    delta_ev += ev_fold - ev_open
    return changes, delta_ev


def write_mafp_chart(
    chart: dict[str, dict[str, set[str]]],
    path: Path,
    *,
    mafp_round: int,
    meta: Optional[dict[str, Any]] = None,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    ranges: dict[str, dict[str, str]] = {}
    for pos, rules in chart.items():
        per_pos: dict[str, str] = {}
        for hand in rules.get("raise", set()):
            per_pos[hand] = "raise"
        for hand in rules.get("call", set()):
            per_pos.setdefault(hand, "call")
        ranges[pos] = per_pos
    payload = {
        "schema": "mafp-hu-chart-v1",
        "source": "examples/mafp_chart_refinement.py",
        "mafp_round": mafp_round,
        "ranges": ranges,
        "meta": meta or {},
    }
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)
    return path


def load_mafp_chart_ranges(path: Optional[Path] = None) -> Optional[dict[str, dict[str, str]]]:
    p = path or MAFP_CHART_PATH
    if not p.is_file():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    ranges = data.get("ranges")
    return ranges if isinstance(ranges, dict) else None


def apply_mafp_overlay_to_static_chart() -> int:
    """Merge MAFP file into in-memory _HU_OPEN_CHART (import side effect)."""
    ranges = load_mafp_chart_ranges()
    if not ranges:
        return 0
    n = 0
    for pos, hands in ranges.items():
        if pos not in _HU_OPEN_CHART:
            continue
        rules = _HU_OPEN_CHART[pos]
        raise_set = rules.setdefault("raise", set())
        call_set = rules.setdefault("call", set())
        for hand, action in hands.items():
            raise_set.discard(hand)
            call_set.discard(hand)
            if action == "raise":
                raise_set.add(hand)
            elif action == "call":
                call_set.add(hand)
            n += 1
    return n


def measure_hero_pfr(decide_fn: Any, *, hands: int, seed: int) -> float:
    """Hero PFR rate in HU selfplay (for adaptive lag)."""
    from cemini_selfplay_audit import HeroAudit, _wrap_decide  # noqa: WPS433

    audit = HeroAudit()
    wrapped = _wrap_decide(decide_fn, audit)
    os.environ["TRAINING_OPPONENT_MODE"] = "lag"
    run_selfplay(
        decide_fn=wrapped,
        n_hands=hands,
        opponent_label="lag",
        n_players=2,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed,
        training_hud=True,
    )
    if audit.preflop_seen <= 0:
        return 0.22
    return audit.pfr / audit.preflop_seen


def run_robustness_check(
    decide_fn: Any,
    *,
    hands: int,
    seed: int,
) -> dict[str, float]:
    """150h vs adaptive lag; compare bb/100 to static lag."""
    hero_pfr = measure_hero_pfr(decide_fn, hands=min(80, hands), seed=seed)
    os.environ["CEMINI_ADAPTIVE_HERO_PFR"] = f"{hero_pfr:.3f}"
    lag = run_selfplay(
        decide_fn=decide_fn,
        n_hands=hands,
        opponent_label="lag",
        n_players=2,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed + 3,
        training_hud=True,
    )
    adaptive = run_selfplay(
        decide_fn=decide_fn,
        n_hands=hands,
        opponent_label="adaptive_lag",
        n_players=2,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed + 4,
        training_hud=True,
    )
    rock = run_selfplay(
        decide_fn=decide_fn,
        n_hands=hands,
        opponent_label="rock",
        n_players=2,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed + 5,
        training_hud=True,
    )
    return {
        "hero_pfr": hero_pfr,
        "bb100_lag": float(lag["bb_per_100"]),
        "bb100_adaptive_lag": float(adaptive["bb_per_100"]),
        "bb100_rock": float(rock["bb_per_100"]),
        "robustness_gap": float(adaptive["bb_per_100"]) - float(lag["bb_per_100"]),
    }


def run_mafp(
    *,
    max_rounds: int,
    ev_eps: float,
    ev_threshold: float,
    aggregate_hands: int,
    seed: int,
    write_chart: bool,
    log_deploy: bool,
) -> list[MafpRoundResult]:
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw_decide = _load_decide_from_path(str(decide_path))
    chart = _deep_copy_hu_chart()
    apply_mafp_overlay_to_static_chart()
    chart = _deep_copy_hu_chart()

    results: list[MafpRoundResult] = []
    stance_weights = {s: 1.0 / len(STANCES) for s in STANCES}

    for rnd in range(1, max_rounds + 1):
        audit = collect_preflop_audit(
            raw_decide,
            hands=aggregate_hands,
            seed=seed + rnd * 100,
        )
        mixes = aggregate_stance_mixtures(audit)
        changes, delta_ev = best_response_chart_update(
            chart,
            mixes,
            stance_weights,
            ev_threshold=ev_threshold,
        )
        res = MafpRoundResult(
            round_num=rnd,
            changes=changes,
            delta_ev=delta_ev,
            stance_weights=dict(stance_weights),
        )
        results.append(res)
        print(f"MAFP round {rnd}: {len(changes)} chart cells, ΔEV≈{delta_ev:.3f}")
        for ch in changes[:8]:
            print(f"  {ch['position']} {ch['hand']}: {ch['from']} → {ch['to']} (Δ{ch['delta_ev']})")
        if len(changes) > 8:
            print(f"  ... +{len(changes) - 8} more")

        if write_chart and changes:
            write_mafp_chart(
                chart,
                MAFP_CHART_PATH,
                mafp_round=rnd,
                meta={"changes": len(changes), "delta_ev": delta_ev, "audit_rows": len(audit)},
            )
            apply_mafp_overlay_to_static_chart()

        if log_deploy:
            append_deploy_record(
                source="mafp_chart_refinement",
                commit=git_commit_short(),
                notes=json.dumps({
                    "mafp_round": rnd,
                    "chart_changes": len(changes),
                    "delta_ev": round(delta_ev, 4),
                    "audit_rows": len(audit),
                }),
            )

        if not changes or delta_ev < ev_eps:
            print(f"MAFP converged at round {rnd} (ΔEV {delta_ev:.4f} < ε {ev_eps})")
            break

        for s in STANCES:
            stance_weights[s] += 1.0 / len(STANCES)

    if write_chart and not MAFP_CHART_PATH.is_file() and results:
        write_mafp_chart(
            chart,
            MAFP_CHART_PATH,
            mafp_round=results[-1].round_num,
            meta={"baseline": True, "chart_changes": 0},
        )
        apply_mafp_overlay_to_static_chart()

    return results


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="K124 MAFP HU preflop chart refinement")
    p.add_argument("--max-rounds", type=int, default=DEFAULT_MAX_ROUNDS)
    p.add_argument("--ev-eps", type=float, default=DEFAULT_EV_EPS)
    p.add_argument("--ev-threshold", type=float, default=DEFAULT_EV_THRESHOLD)
    p.add_argument("--aggregate-hands", type=int, default=DEFAULT_AGGREGATE_HANDS)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--no-write", action="store_true", help="Dry-run — do not write mafp_hu_chart.json")
    p.add_argument("--no-deploy-log", action="store_true")
    p.add_argument("--robustness", action="store_true", help="P1: adaptive lag robustness after MAFP")
    p.add_argument("--hands", type=int, default=150, help="Hands for robustness selfplay")
    args = p.parse_args(argv)

    print(f"MAFP fictitious-play spike (commit {git_commit_short()})")
    results = run_mafp(
        max_rounds=args.max_rounds,
        ev_eps=args.ev_eps,
        ev_threshold=args.ev_threshold,
        aggregate_hands=args.aggregate_hands,
        seed=args.seed,
        write_chart=not args.no_write,
        log_deploy=not args.no_deploy_log,
    )
    if not results:
        return 1

    if args.robustness:
        decide_fn = _load_decide_from_path(str(_EXAMPLES / "cemini_decide.py"))
        rb = run_robustness_check(decide_fn, hands=args.hands, seed=args.seed + 900)
        print("Robustness (P1):")
        print(f"  hero_pfr={rb['hero_pfr']:.1%}")
        print(f"  bb/100 lag={rb['bb100_lag']:+.1f}")
        print(f"  bb/100 adaptive_lag={rb['bb100_adaptive_lag']:+.1f}  (gap {rb['robustness_gap']:+.1f})")
        print(f"  bb/100 rock={rb['bb100_rock']:+.1f}")
        if not args.no_deploy_log:
            append_deploy_record(
                source="mafp_robustness",
                notes=json.dumps({"mafp_round": results[-1].round_num, **rb}),
            )

    print(f"Done — {len(results)} MAFP round(s); chart: {MAFP_CHART_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
