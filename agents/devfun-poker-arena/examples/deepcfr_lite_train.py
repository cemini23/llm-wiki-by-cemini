#!/usr/bin/env python3
"""DeepCFR-lite — tabular regret-matching over HU postflop bucket infosets.

Offline-only. Ships average strategy as ``research/deepcfr_hu_buckets.json``
with the same schema as ``postflop_hu_buckets.json``. No torch / open_spiel.

Warm-starts from texas_solver_v1 priors, then runs external-sampling-style
CFR against a simple pot-EV model on abstract strength bins.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from postflop_buckets import (  # noqa: E402
    ROLES,
    STREETS,
    STRENGTH_BINS,
    TEXTURES,
    _FREQ_KEYS,
    _normalize_freqs,
    bucket_key,
)

EQUITY_MID = {
    "air": 0.25,
    "weak": 0.425,
    "medium": 0.575,
    "strong": 0.75,
    "nuts": 0.925,
}

FREE_ACTIONS = ("bet", "check")
FACING_ACTIONS = ("fold", "call", "raise")
DEFAULT_PRIOR = _ROOT / "research" / "postflop_hu_buckets.json"
DEFAULT_OUT = _ROOT / "research" / "deepcfr_hu_buckets.json"


def _load_prior(path: Path) -> dict[str, dict[str, float]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    buckets = data.get("buckets") or {}
    out: dict[str, dict[str, float]] = {}
    for key, raw in buckets.items():
        if isinstance(raw, dict):
            out[key] = _normalize_freqs(raw)
    return out


def _regret_match(regrets: dict[str, float], actions: tuple[str, ...]) -> dict[str, float]:
    pos = {a: max(0.0, float(regrets.get(a, 0.0))) for a in actions}
    total = sum(pos.values())
    if total <= 1e-12:
        u = 1.0 / len(actions)
        return {a: u for a in actions}
    return {a: pos[a] / total for a in actions}


def _full_strategy(
    free_sigma: dict[str, float],
    face_sigma: dict[str, float],
    size_pot_frac: float,
    *,
    free_weight: float = 0.55,
) -> dict[str, float]:
    """Blend free-spot and facing strategies into the 5-key bucket schema."""
    fw = max(0.05, min(0.95, free_weight))
    out = {k: 0.0 for k in _FREQ_KEYS}
    for a, p in free_sigma.items():
        out[a] = fw * float(p)
    for a, p in face_sigma.items():
        out[a] = (1.0 - fw) * float(p)
    return _normalize_freqs({**out, "size_pot_frac": size_pot_frac})


def _showdown_ev(hero_eq: float, pot: float, invest: float) -> float:
    """Hero chip EV at showdown after investing ``invest`` into pot ``pot``."""
    # pot already includes invest from both sides in our accounting below
    return hero_eq * pot - invest


def _terminal_free(
    hero_eq: float,
    vill_eq: float,
    hero_act: str,
    vill_face: dict[str, float],
    *,
    pot: float = 10.0,
    bet: float = 6.0,
) -> float:
    if hero_act == "check":
        # Check-down: pot realized at showdown, no extra invest
        return (hero_eq - 0.5) * pot
    # Hero bets; villain mixes fold/call/raise
    fold_p = float(vill_face.get("fold", 0.0))
    call_p = float(vill_face.get("call", 0.0))
    raise_p = float(vill_face.get("raise", 0.0))
    s = fold_p + call_p + raise_p
    if s <= 1e-12:
        fold_p, call_p, raise_p = 0.4, 0.45, 0.15
        s = 1.0
    fold_p, call_p, raise_p = fold_p / s, call_p / s, raise_p / s

    ev_fold = pot  # villain folds → hero wins pot, invest = bet later netted
    # Accounting: hero already "puts" bet; if fold, wins pot+bet net = pot
    # Use relative EV vs check-down baseline for CFR stability.
    ev_call = _showdown_ev(hero_eq, pot + 2 * bet, bet) - bet
    # Raise: simplify as 2.2x bet call-or-fold at 50/50 vs equity
    raise_size = 2.2 * bet
    ev_raise_call = _showdown_ev(hero_eq, pot + 2 * raise_size, raise_size) - raise_size
    ev_raise_fold = pot  # villain shove-bluff fails often — treat as fold win
    # Villain raise then we call for EV (abstract); weight 0.55 call / 0.45 fold
    ev_raise = 0.55 * ev_raise_call + 0.45 * ev_raise_fold
    # fold branch: hero invested bet but wins pot+bet → net +pot relative to 0
    return fold_p * (pot) + call_p * ev_call + raise_p * ev_raise - bet * (1.0 - fold_p) * 0.0


def _terminal_facing(
    hero_eq: float,
    hero_act: str,
    *,
    pot: float = 10.0,
    bet: float = 6.0,
) -> float:
    if hero_act == "fold":
        return 0.0
    if hero_act == "call":
        return _showdown_ev(hero_eq, pot + 2 * bet, bet) - bet
    # raise
    raise_size = 2.2 * bet
    # Assume villain calls 60% / folds 40%
    ev_fold = pot + bet  # win current pot + their bet
    ev_call = _showdown_ev(hero_eq, pot + 2 * raise_size, raise_size) - raise_size
    return 0.4 * ev_fold + 0.6 * ev_call


def train(
    prior: dict[str, dict[str, float]],
    *,
    iters: int,
    seed: int,
) -> dict[str, dict[str, float]]:
    rng = random.Random(seed)
    keys = sorted(prior.keys())
    if not keys:
        raise SystemExit("prior buckets empty")

    regret_free: dict[str, dict[str, float]] = {
        k: {a: 0.0 for a in FREE_ACTIONS} for k in keys
    }
    regret_face: dict[str, dict[str, float]] = {
        k: {a: 0.0 for a in FACING_ACTIONS} for k in keys
    }
    sum_free: dict[str, dict[str, float]] = {
        k: {a: float(prior[k].get(a, 0.0)) * 5000.0 for a in FREE_ACTIONS} for k in keys
    }
    sum_face: dict[str, dict[str, float]] = {
        k: {a: float(prior[k].get(a, 0.0)) * 5000.0 for a in FACING_ACTIONS} for k in keys
    }

    for t in range(1, iters + 1):
        street = rng.choice(STREETS)
        texture = rng.choice(TEXTURES)
        role = rng.choice(ROLES)
        hero_s = rng.choice(STRENGTH_BINS)
        vill_s = rng.choice(STRENGTH_BINS)
        key = bucket_key(street, role, texture, hero_s)
        if key not in prior:
            continue
        vill_role = "oop" if role == "ip" else "ip"
        vkey = bucket_key(street, vill_role, texture, vill_s)
        if vkey not in prior:
            vkey = key

        hero_eq = EQUITY_MID[hero_s]
        # Soft-normalize vs villain equity mid so hero_eq + vill_eq ≈ 1
        vill_eq = EQUITY_MID[vill_s]
        norm = hero_eq + vill_eq
        hero_eq, vill_eq = hero_eq / norm, vill_eq / norm

        facing = rng.random() < 0.45
        if not facing:
            sigma = _regret_match(regret_free[key], FREE_ACTIONS)
            vill_face = _regret_match(regret_face[vkey], FACING_ACTIONS)
            utils = {
                a: _terminal_free(hero_eq, vill_eq, a, vill_face) for a in FREE_ACTIONS
            }
            ev = sum(sigma[a] * utils[a] for a in FREE_ACTIONS)
            for a in FREE_ACTIONS:
                regret_free[key][a] += utils[a] - ev
                sum_free[key][a] += sigma[a] * t
        else:
            sigma = _regret_match(regret_face[key], FACING_ACTIONS)
            utils = {a: _terminal_facing(hero_eq, a) for a in FACING_ACTIONS}
            ev = sum(sigma[a] * utils[a] for a in FACING_ACTIONS)
            for a in FACING_ACTIONS:
                regret_face[key][a] += utils[a] - ev
                sum_face[key][a] += sigma[a] * t

    # Emit average strategies blended into schema
    out: dict[str, dict[str, float]] = {}
    for key, pref in prior.items():
        size = float(pref.get("size_pot_frac", 0.5))
        free_sum = sum_free.get(key) or {a: 0.0 for a in FREE_ACTIONS}
        face_sum = sum_face.get(key) or {a: 0.0 for a in FACING_ACTIONS}
        fs = sum(free_sum.values())
        vs = sum(face_sum.values())
        free_sigma = (
            {a: free_sum[a] / fs for a in FREE_ACTIONS}
            if fs > 1e-12
            else _regret_match({}, FREE_ACTIONS)
        )
        face_sigma = (
            {a: face_sum[a] / vs for a in FACING_ACTIONS}
            if vs > 1e-12
            else _regret_match({}, FACING_ACTIONS)
        )
        # Street-aware free weight: rivers face more bets
        street = key.split("|", 1)[0]
        fw = 0.50 if street == "river" else 0.58 if street == "turn" else 0.62
        avg = _full_strategy(free_sigma, face_sigma, size, free_weight=fw)
        # Mild shrink toward prior to avoid OOS overfit
        shrink = 0.25
        blended = {
            a: (1.0 - shrink) * avg[a] + shrink * float(pref.get(a, 0.0))
            for a in _FREQ_KEYS
        }
        blended["size_pot_frac"] = size
        out[key] = _normalize_freqs(blended)
    return out


def write_bake(
    buckets: dict[str, dict[str, float]],
    out_path: Path,
    *,
    iters: int,
    seed: int,
    prior_generator: str,
    force: bool,
) -> Path:
    if out_path.exists() and not force:
        raise SystemExit(f"refusing to overwrite {out_path} (pass --force)")
    payload: dict[str, Any] = {
        "schema": "postflop-hu-buckets-v1",
        "meta": {
            "generator": "deepcfr_lite_v1",
            "prior_generator": prior_generator,
            "iters": iters,
            "seed": seed,
            "infosets": len(buckets),
            "key_count": len(buckets),
        },
        "solver_provenance": {
            "notes": (
                "deepcfr_lite_v1 tabular regret-matching over HU bucket infosets; "
                "warm-started from texas_solver_v1; offline only"
            ),
        },
        "buckets": buckets,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prior", type=Path, default=DEFAULT_PRIOR)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--iters", type=int, default=50_000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args(argv)

    if not args.prior.is_file():
        raise SystemExit(f"prior missing: {args.prior}")

    prior_raw = json.loads(args.prior.read_text(encoding="utf-8"))
    prior_gen = str((prior_raw.get("meta") or {}).get("generator") or "unknown")
    prior = _load_prior(args.prior)
    # Ensure full 90-key grid even if prior sparse
    for street in STREETS:
        for role in ROLES:
            for texture in TEXTURES:
                for strength in STRENGTH_BINS:
                    k = bucket_key(street, role, texture, strength)
                    if k not in prior:
                        prior[k] = _normalize_freqs(
                            {
                                "bet": 0.35,
                                "check": 0.35,
                                "call": 0.15,
                                "fold": 0.10,
                                "raise": 0.05,
                                "size_pot_frac": 0.5,
                            }
                        )

    buckets = train(prior, iters=args.iters, seed=args.seed)
    path = write_bake(
        buckets,
        args.out,
        iters=args.iters,
        seed=args.seed,
        prior_generator=prior_gen,
        force=args.force,
    )
    print(f"wrote {path} keys={len(buckets)} generator=deepcfr_lite_v1 iters={args.iters}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
