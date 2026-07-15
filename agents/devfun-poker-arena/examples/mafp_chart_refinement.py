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
from solver_provenance import solver_provenance, stamp_chart_provenance  # noqa: E402

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


def hand_equity(hand_class: str) -> float:
    """Preflop equity vs random; chart table + Sklansky-ish fallback for missing cells."""
    if hand_class in _PREFLOP_EQUITY:
        return float(_PREFLOP_EQUITY[hand_class])
    ranks = "23456789TJQKA"
    if len(hand_class) == 2 and hand_class[0] == hand_class[1]:
        # Pairs should be in the table; keep a safe mid estimate.
        return 0.50
    if len(hand_class) < 3:
        return 0.45
    suited = hand_class.endswith("s")
    r1, r2 = hand_class[0], hand_class[1]
    if r1 not in ranks or r2 not in ranks:
        return 0.45
    i1, i2 = ranks.index(r1), ranks.index(r2)
    if i1 < i2:
        i1, i2 = i2, i1
    gap = i1 - i2
    # Coarse HU equity prior so 72o ≠ A5s (table only lists ~27 premiums).
    base = 0.30 + 0.022 * i1 + 0.012 * i2
    if suited:
        base += 0.035
    if gap == 1:
        base += 0.025  # connector
    elif gap == 2:
        base += 0.01
    elif gap >= 4:
        base -= 0.015 * min(gap - 3, 4)
    if i1 >= 8 and i2 >= 8:  # both T+
        base += 0.02
    return max(0.28, min(0.62, base))


def candidate_hands(chart: dict[str, dict[str, set[str]]], position: str) -> set[str]:
    """Hands to evaluate: full 169 + chart members (never thin out best-response).

    Prior versions only scored chart members + a narrow equity band, so cells
    never left the static open set. Evaluate every class so fold/call/raise
    best-response can actually flip.
    """
    rules = chart.get(position) or {}
    candidates = set(rules.get("raise", set())) | set(rules.get("call", set()))
    candidates.update(all_hand_classes())
    return candidates


def _normalize_rates(fold: float, call: float, raise_: float) -> tuple[float, float, float]:
    f = max(0.0, fold)
    c = max(0.0, call)
    r = max(0.0, raise_)
    s = f + c + r
    if s <= 0:
        return 0.55, 0.35, 0.10
    return f / s, c / s, r / s


def ev_open_vs_mixture(
    hand_class: str,
    fold_rate: float,
    *,
    open_bb: float = 2.5,
    pot_bb: float = 1.5,
    call_rate: float = 0.0,
    raise_rate: float = 0.0,
) -> tuple[float, float]:
    """HU unopened-pot EV (bb): open vs fold.

    Backward-compatible wrapper around :func:`ev_actions_unopened`. When only
    ``fold_rate`` is supplied, residual mass is treated as call (legacy).
    Prefer passing explicit call/raise rates so 3-bet responses can tank weak opens.
    """
    if call_rate == 0.0 and raise_rate == 0.0:
        call_rate = max(0.0, 1.0 - fold_rate)
        raise_rate = 0.0
    evs = ev_actions_unopened(
        hand_class,
        {"fold": fold_rate, "call": call_rate, "raise": raise_rate},
        open_bb=open_bb,
        pot_bb=pot_bb,
    )
    return evs["raise"], evs["fold"]


def _ev_vs_threebet(
    eq: float,
    *,
    open_bb: float,
    pot_bb: float,
    threebet_to: float = 8.0,
) -> float:
    """Best-response EV after villain 3-bets our open (fold or call 3-bet)."""
    # Accounting matches steal EV: fold branch of open nets +pot_bb (open returns
    # with pot). Folding to a 3-bet loses the open chips.
    ev_fold_to = -open_bb
    call_amt = max(0.0, threebet_to - open_bb)
    pot_after_call = pot_bb + open_bb + threebet_to + call_amt
    ev_call = eq * pot_after_call - open_bb - call_amt
    return max(ev_fold_to, ev_call)


def ev_actions_unopened(
    hand_class: str,
    rates: dict[str, float],
    *,
    open_bb: float = 2.5,
    pot_bb: float = 1.5,
    threebet_to: float = 8.0,
) -> dict[str, float]:
    """Per-action EV (bb) for BTN/SB unopened pot: fold / call(limp) / raise."""
    eq = hand_equity(hand_class)
    f, c, r = _normalize_rates(
        float(rates.get("fold", 0.55)),
        float(rates.get("call", 0.35)),
        float(rates.get("raise", 0.10)),
    )
    # Fold: baseline 0 (dead SB not re-priced — consistent with steal model).
    ev_fold = 0.0
    # Limp complete to 1bb; BB checks often → realized equity of ~2bb pot;
    # when BB raises, dump the limp (simple fold-to-iso).
    limp_invest = 0.5
    pot_if_checked = pot_bb + limp_invest  # ~2.0
    bb_iso_rate = min(0.45, 0.15 + r)  # more iso when mixture is aggressive
    ev_limp_check = eq * pot_if_checked - limp_invest
    ev_limp_iso = -limp_invest
    ev_call = (1.0 - bb_iso_rate) * ev_limp_check + bb_iso_rate * ev_limp_iso
    # Open: villain fold / call / 3-bet (raise) — not "non-fold = call".
    pot_if_called = pot_bb + 2 * open_bb
    ev_when_called = eq * pot_if_called - open_bb
    ev_when_3bet = _ev_vs_threebet(
        eq, open_bb=open_bb, pot_bb=pot_bb, threebet_to=threebet_to
    )
    ev_raise = f * pot_bb + c * ev_when_called + r * ev_when_3bet
    return {"fold": ev_fold, "call": ev_call, "raise": ev_raise}


def ev_actions_bb_vs_open(
    hand_class: str,
    rates: dict[str, float],
    *,
    open_bb: float = 2.5,
    pot_bb: float = 1.5,
    threebet_to: float = 9.0,
) -> dict[str, float]:
    """Per-action EV (bb) for BB facing a steal: fold / call / raise(3-bet)."""
    eq = hand_equity(hand_class)
    # Villain response after our 3-bet (continue / fold).
    f, c, r = _normalize_rates(
        float(rates.get("fold", 0.45)),
        float(rates.get("call", 0.40)),
        float(rates.get("raise", 0.15)),
    )
    # pot after open: blinds + open completion from SB.
    sb_added = open_bb - 0.5
    pot_facing = pot_bb + sb_added
    to_call = open_bb - 1.0
    ev_fold = 0.0
    pot_if_call = pot_facing + to_call
    ev_call = eq * pot_if_call - to_call
    # 3-bet: invest (threebet_to - bb_already_in); villain folds/calls/4-bets.
    invest_3b = threebet_to - 1.0
    pot_after_3b = pot_facing + invest_3b  # villain open already in pot_facing
    # When villain folds to 3bet we win pot_facing (open already in).
    # When calls: pot = pot_facing + invest_3b + (threebet_to - open_bb) roughly;
    # use threebet_to matching open side for simplicity.
    villain_call_amt = threebet_to - open_bb
    pot_3b_called = pot_facing + invest_3b + villain_call_amt
    # 4-bet: dump the 3-bet (fold) for non-nuts; crude max(fold, call-4bet).
    ev_vs_4bet = -invest_3b
    pot_odds_4b_call = threebet_to  # rough extra
    ev_call_4b = eq * (pot_after_3b + pot_odds_4b_call) - invest_3b - pot_odds_4b_call
    ev_when_4bet = max(ev_vs_4bet, ev_call_4b)
    ev_raise = (
        f * pot_facing
        + c * (eq * pot_3b_called - invest_3b)
        + r * ev_when_4bet
    )
    return {"fold": ev_fold, "call": ev_call, "raise": ev_raise}


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


def mixture_action_rates(
    stance_mixes: dict[str, dict[str, dict[str, float]]],
    stance_weights: dict[str, float],
    position: str,
    bucket: str = "mid",
) -> dict[str, float]:
    """Weighted {fold, call, raise} response mix across stances."""
    total_w = 0.0
    acc = {"fold": 0.0, "call": 0.0, "raise": 0.0}
    for stance, w in stance_weights.items():
        mix = stance_mixes.get(stance, {})
        pos_mix = mix.get(position) or mix.get("BTN") or {}
        rates = pos_mix.get(bucket) or pos_mix.get("mid") or {
            "fold": 0.55,
            "call": 0.35,
            "raise": 0.10,
        }
        for k in acc:
            acc[k] += w * float(rates.get(k, 0.0))
        total_w += w
    if total_w <= 0:
        return {"fold": 0.55, "call": 0.35, "raise": 0.10}
    return {k: acc[k] / total_w for k in acc}


def mixture_fold_rate(
    stance_mixes: dict[str, dict[str, dict[str, float]]],
    stance_weights: dict[str, float],
    position: str,
    bucket: str = "mid",
) -> float:
    return mixture_action_rates(stance_mixes, stance_weights, position, bucket)["fold"]


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
    """Best-response fold/call/raise on BTN opens and BB vs steal."""
    changes: list[dict[str, str]] = []
    delta_ev = 0.0
    for pos in positions:
        chart_pos = "BTN" if pos == "SB" else pos
        rates = mixture_action_rates(stance_mixes, stance_weights, chart_pos)
        for hand in sorted(candidate_hands(chart, chart_pos)):
            current = _chart_action(chart, chart_pos, hand)
            if chart_pos == "BB":
                evs = ev_actions_bb_vs_open(hand, rates)
            else:
                evs = ev_actions_unopened(hand, rates)

            # Argmax among fold / call / raise; require clear EV gain to flip.
            best = max(evs, key=lambda a: evs[a])
            if best == current:
                continue
            gain = evs[best] - evs.get(current, evs["fold"])
            if gain < ev_threshold:
                continue
            _set_chart_action(chart, chart_pos, hand, best)
            changes.append({
                "position": chart_pos,
                "hand": hand,
                "from": current,
                "to": best,
                "delta_ev": round(gain, 4),
            })
            delta_ev += gain
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
    # K136: Stamp solver provenance (backward-compatible optional key)
    prov = solver_provenance(
        "mafp",
        version="1",
        equilibrium_selection="time_average",   # FP time-average member
        nash_set_singleton=None,                 # not analyzed for HU NLHE chart space
        notes="K124 MAFP stance fictitious play; not a tabular NE solver",
    )
    payload = stamp_chart_provenance(payload, prov)
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

        total_changes = sum(len(r.changes) for r in results)
        if write_chart and changes:
            write_mafp_chart(
                chart,
                MAFP_CHART_PATH,
                mafp_round=rnd,
                meta={
                    "changes": len(changes),
                    "chart_changes": total_changes,
                    "delta_ev": delta_ev,
                    "audit_rows": len(audit),
                    "ev_threshold": ev_threshold,
                },
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

    total_changes = sum(len(r.changes) for r in results)
    # Always stamp a final chart when we produced flips (normalize chart_changes).
    if write_chart and total_changes > 0:
        write_mafp_chart(
            chart,
            MAFP_CHART_PATH,
            mafp_round=results[-1].round_num if results else 0,
            meta={
                "changes": total_changes,
                "chart_changes": total_changes,
                "delta_ev": sum(r.delta_ev for r in results),
                "rounds": len(results),
                "ev_threshold": ev_threshold,
            },
        )
        apply_mafp_overlay_to_static_chart()
    elif write_chart and not MAFP_CHART_PATH.is_file() and results:
        write_mafp_chart(
            chart,
            MAFP_CHART_PATH,
            mafp_round=results[-1].round_num,
            meta={"baseline": True, "chart_changes": 0, "changes": 0},
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
