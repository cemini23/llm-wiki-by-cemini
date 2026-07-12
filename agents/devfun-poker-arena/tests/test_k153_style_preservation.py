"""K153 style preservation — D_policy TV + config."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import (  # noqa: E402
    compute_d_policy_tv,
    compute_style_drift_d_policy,
    load_style_preservation_config,
)
from rlcard_style_drift_trial import (  # noqa: E402
    ARCHETYPE_DISTRIBUTIONS,
    beta_mix_distribution,
)

STYLE_PATH = ROOT / "config" / "hu_style_preservation.json"


def test_style_preservation_config_loads():
    cfg = load_style_preservation_config(STYLE_PATH)
    assert cfg["schema"] == "devfun.hu_style_preservation.v1"
    assert cfg["beta_demo_mix"] == 0.05
    assert "NO LICENSE" in cfg["notes"]


def test_d_policy_tv_identity():
    dist = {"fold": 0.4, "call": 0.4, "raise": 0.2}
    assert compute_d_policy_tv(dist, dist) == 0.0


def test_d_policy_tv_disjoint():
    a = {"fold": 1.0, "check": 0.0, "call": 0.0, "raise": 0.0}
    b = {"fold": 0.0, "check": 0.0, "call": 0.0, "raise": 1.0}
    assert compute_d_policy_tv(a, b) == 1.0


def test_beta_mix_increases_tv_vs_seed():
    seed = ARCHETYPE_DISTRIBUTIONS["tight_passive"]
    uniform = {"fold": 0.25, "check": 0.25, "call": 0.25, "raise": 0.25}
    mixed = beta_mix_distribution(seed, uniform, 0.05)
    tv_low = compute_d_policy_tv(seed, mixed)
    mixed_high = beta_mix_distribution(seed, uniform, 0.5)
    tv_high = compute_d_policy_tv(seed, mixed_high)
    assert tv_high > tv_low


def test_style_drift_advisory_flags_gap():
    seed = ARCHETYPE_DISTRIBUTIONS["tight_passive"]
    wild = {"fold": 0.05, "check": 0.05, "call": 0.20, "raise": 0.70}
    out = compute_style_drift_d_policy(seed, wild, config=load_style_preservation_config(STYLE_PATH))
    assert out["advisory_only"] is True
    assert out["schema"] == "devfun.style_drift_d_policy.v1"
    assert out["style_ok"] is False


def test_style_drift_passes_near_seed():
    seed = ARCHETYPE_DISTRIBUTIONS["tight_passive"]
    near = beta_mix_distribution(seed, seed, 0.01)
    out = compute_style_drift_d_policy(seed, near, config=load_style_preservation_config(STYLE_PATH))
    assert out["style_ok"] is True
