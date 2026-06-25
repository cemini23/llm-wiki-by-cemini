"""K129 tests — GARIP uniform baseline + IRumAI range probe helpers."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from garip_mixture import (  # noqa: E402
    exploitability_proxy,
    uniform_action_rates,
    uniform_stance_mixture,
)
from irumai_range_probe import (  # noqa: E402
    aggregate_hand_features,
    baseline_scores,
    hand_strength_norm,
    rank_auc,
    train_logistic,
)


def _sample_mix() -> dict:
    return {
        "rock": {
            "BTN": {
                "mid": {"fold": 0.6, "call": 0.3, "raise": 0.1},
            },
        },
    }


def test_uniform_action_rates():
    rates = uniform_action_rates()
    assert rates == {"fold": 1 / 3, "call": 1 / 3, "raise": 1 / 3}


def test_uniform_stance_mixture_matches_template_keys():
    template = _sample_mix()
    uniform = uniform_stance_mixture(template)
    assert uniform["rock"]["BTN"]["mid"] == uniform_action_rates()


def test_exploitability_proxy_higher_when_garip_beats_uniform():
    proxy = exploitability_proxy(garip_delta_ev=0.05, uniform_delta_ev=0.10)
    assert proxy == 0.05


def test_hand_strength_aa_beats_72():
    aa = hand_strength_norm("AsAh", "2c3d4h")
    junk = hand_strength_norm("7s2c", "2c3d4h")
    assert aa > junk


def test_rank_auc_perfect_separation():
    labels = [0.2, 0.4, 0.8, 0.9]
    scores = [0.1, 0.3, 0.7, 0.95]
    assert rank_auc(labels, scores) == 1.0


def test_aggregate_hand_features_counts_aggression():
    decisions = [
        {"street": "Preflop", "action": "raise", "pot_chips": 10, "amount": 6},
        {"street": "Flop", "action": "call", "pot_chips": 20, "amount": 10},
    ]
    feats = aggregate_hand_features(decisions)
    assert feats[2] == 1.0  # preflop_aggr
    assert feats[3] == 0.0  # flop_aggr


def test_probe_beats_constant_baseline_on_synthetic_pattern():
    x = [
        [1.0, 3.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 2.0],
        [0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.6, 0.2, 0.2, 0.0],
        [1.0, 4.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.25, 0.75, 0.8, 3.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    ]
    y = [0.9, 0.3, 0.95, 0.2]
    baseline = baseline_scores(x)
    probe = train_logistic(x, y, epochs=400, lr=0.1, seed=1)
    from irumai_range_probe import predict_scores

    probe_scores = predict_scores(x, *probe)
    assert rank_auc(y, probe_scores) >= rank_auc(y, baseline)
