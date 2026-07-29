"""CEMINI_SOLVER_HARD — sample bake freqs vs soft bias fail-open."""
from __future__ import annotations

import random
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from postflop_buckets import (  # noqa: E402
    sample_action_from_freqs,
    solver_hard_enabled,
    spr_bin,
)


def test_spr_bins():
    assert spr_bin(40, 20) == "spr2"
    assert spr_bin(100, 20) == "spr5"
    assert spr_bin(200, 20) == "spr10"
    assert spr_bin(500, 20) == "spr20"


def test_sample_free_prefers_bet_with_seed():
    freqs = {"bet": 0.9, "check": 0.1, "call": 0, "fold": 0, "raise": 0, "size_pot_frac": 0.5}
    rng = random.Random(0)
    counts = {"bet": 0, "check": 0}
    for _ in range(200):
        out = sample_action_from_freqs(
            freqs, facing_bet=False, available=["bet", "check"], rng=rng
        )
        assert out is not None
        counts[out[0]] += 1
    assert counts["bet"] > counts["check"]


def test_sample_facing_legal_only():
    freqs = {"bet": 0, "check": 0, "call": 0.2, "fold": 0.7, "raise": 0.1, "size_pot_frac": 0.66}
    rng = random.Random(1)
    out = sample_action_from_freqs(
        freqs, facing_bet=True, available=["fold", "call"], rng=rng
    )
    assert out is not None
    assert out[0] in ("fold", "call")


def test_sample_empty_fail_open():
    rng = random.Random(2)
    assert sample_action_from_freqs({}, facing_bet=False, available=["check"], rng=rng) is None
    assert (
        sample_action_from_freqs(
            {"bet": 1.0}, facing_bet=False, available=["fold"], rng=rng
        )
        is None
    )


def test_solver_hard_flag(monkeypatch):
    monkeypatch.delenv("CEMINI_SOLVER_HARD", raising=False)
    assert solver_hard_enabled() is False
    monkeypatch.setenv("CEMINI_SOLVER_HARD", "1")
    assert solver_hard_enabled() is True
