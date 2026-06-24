#!/usr/bin/env python3
"""K127 GARIP offline chart refinement — running-average villain mixture anchor.

Best-responds against Polyak running average μ̄_t instead of instantaneous μ_t
(K124 MAFP). Offline only — no Arena latency.

Usage:
    uv run python examples/garip_chart_refinement.py
    uv run python examples/garip_chart_refinement.py --garip-alpha 0.3 --write
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from deploy_registry import append_deploy_record, git_commit_short  # noqa: E402
from garip_mixture import (  # noqa: E402
    decayed_alpha,
    mixture_l2_drift,
    polyak_update_mixtures,
    snapshot_mixtures,
)
from mafp_chart_refinement import (  # noqa: E402
    DEFAULT_AGGREGATE_HANDS,
    DEFAULT_EV_EPS,
    DEFAULT_EV_THRESHOLD,
    MAFP_CHART_PATH,
    STANCES,
    apply_mafp_overlay_to_static_chart,
    best_response_chart_update,
    collect_preflop_audit,
    _deep_copy_hu_chart,
    _load_decide_from_path,
    write_mafp_chart,
)

DEFAULT_GARIP_ALPHA = 0.3
DEFAULT_R_NAD_SNAPSHOT_EVERY = 0  # 0 = disabled


@dataclass
class GaripRoundResult:
    round_num: int
    changes: list[dict[str, str]] = field(default_factory=list)
    delta_ev: float = 0.0
    mixture_l2_drift: float = 0.0
    r_nad_delta_ev_gap: float = 0.0


def run_garip(
    *,
    max_rounds: int,
    ev_eps: float,
    ev_threshold: float,
    aggregate_hands: int,
    garip_alpha: float,
    seed: int,
    write_chart: bool,
    log_deploy: bool,
    r_nad_snapshot_every: int = 0,
    garip_alpha_decay: float = 0.0,
) -> list[GaripRoundResult]:
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw_decide = _load_decide_from_path(str(decide_path))
    chart = _deep_copy_hu_chart()
    apply_mafp_overlay_to_static_chart()
    chart = _deep_copy_hu_chart()

    results: list[GaripRoundResult] = []
    stance_weights = {s: 1.0 / len(STANCES) for s in STANCES}
    running_avg: Optional[dict[str, Any]] = None
    r_nad_snapshot: Optional[dict[str, Any]] = None
    audit_hand_counter = 0

    for rnd in range(1, max_rounds + 1):
        audit = collect_preflop_audit(
            raw_decide,
            hands=aggregate_hands,
            seed=seed + rnd * 100,
        )
        audit_hand_counter += len(audit)
        from mafp_chart_refinement import aggregate_stance_mixtures  # noqa: WPS433

        mixes_t = aggregate_stance_mixtures(audit)
        prev_avg = running_avg
        round_alpha = decayed_alpha(garip_alpha, rnd, garip_alpha_decay)
        running_avg = polyak_update_mixtures(prev_avg, mixes_t, round_alpha)
        drift = mixture_l2_drift(mixes_t, running_avg) if running_avg else 0.0

        if r_nad_snapshot_every > 0 and (
            audit_hand_counter >= r_nad_snapshot_every
            or r_nad_snapshot is None
        ):
            r_nad_snapshot = snapshot_mixtures(mixes_t)
            audit_hand_counter = 0

        anchor = running_avg if running_avg else mixes_t
        changes, delta_ev = best_response_chart_update(
            chart,
            anchor,
            stance_weights,
            ev_threshold=ev_threshold,
        )

        r_nad_gap = 0.0
        if r_nad_snapshot is not None and r_nad_snapshot_every > 0:
            _, delta_snapshot = best_response_chart_update(
                _deep_copy_hu_chart(),
                r_nad_snapshot,
                stance_weights,
                ev_threshold=ev_threshold,
            )
            r_nad_gap = delta_ev - delta_snapshot

        res = GaripRoundResult(
            round_num=rnd,
            changes=changes,
            delta_ev=delta_ev,
            mixture_l2_drift=drift,
            r_nad_delta_ev_gap=r_nad_gap,
        )
        results.append(res)

        print(
            f"GARIP round {rnd}: changes={len(changes)} ΔEV={delta_ev:.4f} "
            f"drift={drift:.4f} α={round_alpha}"
        )

        if write_chart and changes:
            write_mafp_chart(
                chart,
                MAFP_CHART_PATH,
                mafp_round=rnd,
                meta={
                    "garip": True,
                    "garip_alpha": round_alpha,
                    "garip_alpha_base": garip_alpha,
                    "garip_alpha_decay": garip_alpha_decay,
                    "mixture_l2_drift": round(drift, 4),
                    "chart_changes": len(changes),
                },
            )
            apply_mafp_overlay_to_static_chart()

        if log_deploy:
            append_deploy_record(
                source="garip_chart_refinement",
                commit=git_commit_short(),
                notes=json.dumps({
                    "garip_round": rnd,
                    "garip_alpha": round_alpha,
                    "garip_alpha_base": garip_alpha,
                    "garip_alpha_decay": garip_alpha_decay,
                    "mixture_l2_drift": round(drift, 4),
                    "chart_changes": len(changes),
                    "delta_ev": round(delta_ev, 4),
                    "r_nad_delta_ev_gap": round(r_nad_gap, 4),
                    "audit_rows": len(audit),
                }),
            )

        if not changes or delta_ev < ev_eps:
            print(f"GARIP converged at round {rnd} (ΔEV {delta_ev:.4f} < ε {ev_eps})")
            break

        for s in STANCES:
            stance_weights[s] += 1.0 / len(STANCES)

    if write_chart and not MAFP_CHART_PATH.is_file() and results:
        write_mafp_chart(
            chart,
            MAFP_CHART_PATH,
            mafp_round=results[-1].round_num,
            meta={"garip": True, "garip_alpha": garip_alpha, "baseline": True},
        )
        apply_mafp_overlay_to_static_chart()

    return results


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="K127 GARIP HU preflop chart refinement")
    p.add_argument("--max-rounds", type=int, default=5)
    p.add_argument("--ev-eps", type=float, default=DEFAULT_EV_EPS)
    p.add_argument("--ev-threshold", type=float, default=DEFAULT_EV_THRESHOLD)
    p.add_argument("--aggregate-hands", type=int, default=DEFAULT_AGGREGATE_HANDS)
    p.add_argument("--garip-alpha", type=float, default=DEFAULT_GARIP_ALPHA)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--write",
        action="store_true",
        help="Write mafp_hu_chart.json (default dry-run)",
    )
    p.add_argument("--no-deploy-log", action="store_true")
    p.add_argument(
        "--r-nad-snapshot-every",
        type=int,
        default=DEFAULT_R_NAD_SNAPSHOT_EVERY,
        help="P1 ablation: snapshot μ_t every N audit rows (0=off)",
    )
    p.add_argument(
        "--garip-alpha-decay",
        type=float,
        default=0.0,
        help="EMA decay per round (0=constant α; e.g. 0.85 → EMAgnet-style schedule)",
    )
    args = p.parse_args(argv)

    print(f"GARIP chart refinement (commit {git_commit_short()})")
    results = run_garip(
        max_rounds=args.max_rounds,
        ev_eps=args.ev_eps,
        ev_threshold=args.ev_threshold,
        aggregate_hands=args.aggregate_hands,
        garip_alpha=args.garip_alpha,
        seed=args.seed,
        write_chart=args.write,
        log_deploy=not args.no_deploy_log,
        r_nad_snapshot_every=args.r_nad_snapshot_every,
        garip_alpha_decay=args.garip_alpha_decay,
    )
    if not results:
        return 1
    print(f"Done — {len(results)} GARIP round(s); chart: {MAFP_CHART_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
