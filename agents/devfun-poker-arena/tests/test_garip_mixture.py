"""Tests for K127 GARIP running-average mixture helpers."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from garip_mixture import (  # noqa: E402
    mixture_l2_drift,
    polyak_update_mixtures,
    snapshot_mixtures,
)


def _sample_mix(fold: float = 0.6) -> dict:
    return {
        "rock": {
            "BTN": {
                "mid": {"fold": fold, "call": 0.3, "raise": 0.1},
            },
        },
    }


def test_polyak_first_step_equals_current():
    cur = _sample_mix(0.5)
    out = polyak_update_mixtures(None, cur, alpha=0.3)
    assert out["rock"]["BTN"]["mid"]["fold"] == 0.5


def test_polyak_converges_toward_current():
    prev = _sample_mix(0.9)
    cur = _sample_mix(0.1)
    out = polyak_update_mixtures(prev, cur, alpha=1.0)
    assert out["rock"]["BTN"]["mid"]["fold"] == 0.1
    out_half = polyak_update_mixtures(prev, cur, alpha=0.5)
    assert 0.4 < out_half["rock"]["BTN"]["mid"]["fold"] < 0.6


def test_mixture_l2_drift_zero_on_identical():
    a = _sample_mix(0.55)
    b = snapshot_mixtures(a)
    assert mixture_l2_drift(a, b) == 0.0


def test_mixture_l2_drift_positive_on_change():
    a = _sample_mix(0.9)
    b = _sample_mix(0.1)
    assert mixture_l2_drift(a, b) > 0.0
