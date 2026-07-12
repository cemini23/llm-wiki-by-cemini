#!/usr/bin/env python3
"""K153 Leduc stylized archetype + D_policy style-drift trial (RLCard isolated venv).

MPPO-shaped β-mix stub only — no PPO training. Advisory output; exit 0 always.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

# Pure functions importable without rlcard (unit tests).
from researcher_trajectory_summary import (  # noqa: E402
    compute_d_policy_tv,
    compute_style_drift_d_policy,
    load_style_preservation_config,
)

_ACTION_BUCKETS = ("fold", "check", "call", "raise")

ARCHETYPE_DISTRIBUTIONS: dict[str, dict[str, float]] = {
    "tight_passive": {"fold": 0.45, "check": 0.20, "call": 0.30, "raise": 0.05},
    "loose_passive": {"fold": 0.15, "check": 0.20, "call": 0.50, "raise": 0.15},
    "tight_aggressive": {"fold": 0.35, "check": 0.10, "call": 0.20, "raise": 0.35},
    "loose_aggressive": {"fold": 0.10, "check": 0.10, "call": 0.30, "raise": 0.50},
}


def beta_mix_distribution(
    seed: dict[str, float],
    perturb: dict[str, float],
    beta: float,
) -> dict[str, float]:
    """MPPO-shaped demo mix: (1-β)*seed + β*perturb."""
    b = max(0.0, min(1.0, float(beta)))
    keys = set(seed) | set(perturb) | set(_ACTION_BUCKETS)
    mixed = {k: (1.0 - b) * float(seed.get(k, 0.0)) + b * float(perturb.get(k, 0.0)) for k in keys}
    total = sum(mixed.values())
    if total <= 0:
        return dict(seed)
    return {k: mixed[k] / total for k in mixed}


def _bucket_action(raw: str) -> str:
    text = str(raw).lower()
    if "fold" in text:
        return "fold"
    if "check" in text:
        return "check"
    if "call" in text:
        return "call"
    if "raise" in text or "bet" in text:
        return "raise"
    return "call"


def histogram_from_actions(actions: list[str]) -> dict[str, float]:
    counts = {b: 0 for b in _ACTION_BUCKETS}
    for act in actions:
        counts[_bucket_action(act)] += 1
    total = sum(counts.values()) or 1
    return {b: counts[b] / total for b in _ACTION_BUCKETS}


def run_rlcard_trial(episodes: int, seed: int, env_id: str) -> dict[str, Any]:
    import rlcard  # noqa: WPS433
    from rlcard.agents import RandomAgent
    from rlcard.utils import set_seed

    set_seed(seed)
    random.seed(seed)
    env = rlcard.make(env_id, config={"seed": seed, "allow_raw_data": True})
    agents = [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players)]
    env.set_agents(agents)

    actions: list[str] = []
    for _ in range(episodes):
        trajectories, _payoffs = env.run(is_training=False)
        for player_traj in trajectories:
            for idx in range(1, len(player_traj), 2):
                state = player_traj[idx - 1]
                action_id = player_traj[idx]
                legal = list(state.get("legal_actions", {}).keys())
                raw = state.get("raw_legal_actions", [])
                if action_id in legal and len(raw) == len(legal):
                    actions.append(str(raw[legal.index(action_id)]))
                else:
                    mapping = {0: "call", 1: "raise", 2: "fold", 3: "check"}
                    actions.append(mapping.get(int(action_id), "call"))

    return {"actions_recorded": len(actions), "histogram": histogram_from_actions(actions)}


def run_synthetic_trial(episodes: int, seed: int) -> dict[str, Any]:
    """Fallback when rlcard unavailable — sample from archetype + noise."""
    rng = random.Random(seed)
    archetype = ARCHETYPE_DISTRIBUTIONS["tight_passive"]
    actions: list[str] = []
    buckets = list(_ACTION_BUCKETS)
    weights = [archetype[b] for b in buckets]
    for _ in range(episodes * 8):
        actions.append(rng.choices(buckets, weights=weights, k=1)[0])
    return {"actions_recorded": len(actions), "histogram": histogram_from_actions(actions)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="K153 Leduc style-drift trial")
    parser.add_argument("--episodes", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--env", default="leduc-holdem")
    parser.add_argument("--out-dir", type=Path, default=Path("reports/rlcard-style-drift"))
    args = parser.parse_args(argv)

    cfg = load_style_preservation_config()
    beta = float(cfg.get("beta_demo_mix", 0.05))
    archetype_name = cfg.get("archetypes", ["tight_passive"])[0]
    seed_dist = ARCHETYPE_DISTRIBUTIONS.get(str(archetype_name), ARCHETYPE_DISTRIBUTIONS["tight_passive"])
    uniform = {b: 0.25 for b in _ACTION_BUCKETS}

    trial_mode = "synthetic"
    try:
        field_hist = run_rlcard_trial(args.episodes, args.seed, args.env)
        trial_mode = "rlcard"
    except ImportError:
        print("[arena-pokerkit] WARN: rlcard not installed — synthetic trial", file=sys.stderr)
        field_hist = run_synthetic_trial(args.episodes, args.seed)

    field_dist = field_hist["histogram"]
    upgraded_dist = beta_mix_distribution(seed_dist, uniform, beta)
    style_drift = compute_style_drift_d_policy(seed_dist, upgraded_dist, config=cfg)
    field_vs_seed = compute_style_drift_d_policy(seed_dist, field_dist, config=cfg)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "schema": "devfun.rlcard_style_drift_trial.v1",
        "advisory_only": True,
        "trial_mode": trial_mode,
        "env": args.env,
        "episodes": args.episodes,
        "archetype": archetype_name,
        "beta_demo_mix": beta,
        "seed_distribution": seed_dist,
        "upgraded_beta_mix_distribution": upgraded_dist,
        "field_histogram": field_dist,
        "beta_mix_style_drift": style_drift,
        "field_vs_seed_style_drift": field_vs_seed,
        "d_policy_tv_beta_mix": compute_d_policy_tv(seed_dist, upgraded_dist),
        "reference": "references/mppo-style-preservation.md",
    }
    out_path = args.out_dir / "summary.json"
    out_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[arena-pokerkit] style drift trial → {out_path}")
    print(
        f"  mode={trial_mode} beta_mix_tv={style_drift.get('d_policy_tv')} "
        f"style_ok={style_drift.get('style_ok')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
