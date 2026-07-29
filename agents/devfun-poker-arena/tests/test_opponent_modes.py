"""Opponent-conditioned best-response modes (WP1)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT / "tests"))

from opponent_modes import (  # noqa: E402
    DELTA_CLAMP,
    apply_opponent_mode_to_margins,
    attach_opponent_mode_to_hud,
    mode_from_spectrum,
    mode_margin_deltas,
    opponent_modes_enabled,
    resolve_opponent_mode,
)
from risk_spectrum import build_risk_spectrum  # noqa: E402
from cemini_decide import decide  # noqa: E402
from helpers.cemini_tables import hu_sb_unopened  # noqa: E402


@pytest.fixture(autouse=True)
def _clear_mode_flag(monkeypatch):
    monkeypatch.delenv("CEMINI_OPPONENT_MODES", raising=False)
    yield


def test_mode_map_from_spectrum():
    assert mode_from_spectrum(build_risk_spectrum(0.10, 0.02)) == "nit"  # low/low
    assert mode_from_spectrum(build_risk_spectrum(0.10, 0.08)) == "nit"  # low/med
    assert mode_from_spectrum(build_risk_spectrum(0.50, 0.20)) == "lag"  # high/high
    assert mode_from_spectrum(build_risk_spectrum(0.50, 0.0)) == "wide_passive"  # high/low
    assert mode_from_spectrum(build_risk_spectrum(0.50, 0.08)) == "wide_passive"  # high/med
    assert mode_from_spectrum(build_risk_spectrum(0.30, 0.20)) == "balanced"  # med/high
    assert mode_from_spectrum(None) == "balanced"
    assert mode_from_spectrum({}) == "balanced"


def test_cold_start_and_missing_hud_balanced():
    assert resolve_opponent_mode({"coldStart": True, "vpip": 0.10, "pfr": 0.02}) == "balanced"
    assert resolve_opponent_mode({}) == "balanced"
    assert resolve_opponent_mode({"vpip": 0.10, "pfr": 0.02}) == "nit"


def test_deltas_clamped_and_balanced_zero():
    assert mode_margin_deltas("balanced") == {}
    for mode in ("nit", "lag", "wide_passive"):
        d = mode_margin_deltas(mode)
        assert d, f"{mode} should have deltas"
        for _k, v in d.items():
            assert abs(v) <= DELTA_CLAMP + 1e-9


def test_apply_stacks_additive_not_replace():
    base = {"bet_bar_delta": 0.02, "fold_slack_delta": 0.01, "call_margin_delta": 0.0}
    out = apply_opponent_mode_to_margins(base, mode="lag")
    # lag: +0.04 bet_bar, -0.03 fold_slack, +0.04 call
    assert out["bet_bar_delta"] == pytest.approx(0.06)
    assert out["fold_slack_delta"] == pytest.approx(-0.02)
    assert out["call_margin_delta"] == pytest.approx(0.04)
    # HUD open_steal wins; nit does not clobber
    base2 = {"open_steal_equity": 0.55, "bet_bar_delta": 0.0}
    out2 = apply_opponent_mode_to_margins(base2, mode="nit")
    assert out2["open_steal_equity"] == 0.55
    out3 = apply_opponent_mode_to_margins({"bet_bar_delta": 0.0}, mode="nit")
    assert out3.get("open_steal_equity") == pytest.approx(0.48)


def test_attach_tags_mode_on_hud():
    hud = attach_opponent_mode_to_hud({"vpip": 0.516, "pfr": 0.0, "mode": "maniac"})
    assert hud["mode"] == "maniac"
    assert hud["opponent_mode"] == "wide_passive"
    assert "risk_spectrum" in hud


def test_flag_off_enabled_false():
    assert opponent_modes_enabled() is False


def test_flag_off_decide_identical(monkeypatch):
    """Flag off → stable decide output (no mode overlay path)."""
    monkeypatch.setenv("CEMINI_OPPONENT_MODES", "0")
    table = hu_sb_unopened(["Ah", "Kd"])
    a1 = decide(table, deadline_s=10.0)
    a2 = decide(table, deadline_s=10.0)
    assert a1 == a2


def test_mode_changes_action_vs_balanced():
    """Mode deltas move free-spot bet bar enough to flip check↔bet at fixed equity."""
    equity = 0.70  # just under default 0.72 free bet bar
    default_bar = 0.72
    nit_m = apply_opponent_mode_to_margins({}, mode="nit")
    lag_m = apply_opponent_mode_to_margins({}, mode="lag")
    bal_m = apply_opponent_mode_to_margins({}, mode="balanced")
    assert bal_m.get("bet_bar_delta", 0.0) == 0.0

    nit_bar = default_bar + float(nit_m.get("bet_bar_delta", 0.0))
    lag_bar = default_bar + float(lag_m.get("bet_bar_delta", 0.0))
    nit_action = "bet" if equity >= nit_bar else "check"
    lag_action = "bet" if equity >= lag_bar else "check"
    bal_action = "bet" if equity >= default_bar else "check"
    assert bal_action == "check"
    assert nit_action == "bet"
    assert lag_action == "check"
    assert nit_action != lag_action


def test_flag_on_apply_changes_margins(monkeypatch):
    monkeypatch.setenv("CEMINI_OPPONENT_MODES", "1")
    assert opponent_modes_enabled() is True
    hud = {"vpip": 0.10, "pfr": 0.02, "coldStart": False}
    m_on = apply_opponent_mode_to_margins({}, hud)
    assert m_on.get("bet_bar_delta", 0) < 0
