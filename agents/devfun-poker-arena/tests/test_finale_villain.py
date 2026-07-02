"""Tests for finale human-table exploit layer."""
from __future__ import annotations

import os

import pytest


def _table(*, call_chips: int = 0, pot: int = 100) -> dict:
    return {
        "street": "Flop",
        "potChips": pot,
        "boardCards": ["Ah", "7d", "2c"],
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "holeCards": ["As", "Kd"], "stackChips": 1000},
            {"seatNumber": 2, "holeCards": ["Qh", "Jh"], "stackChips": 1000},
        ],
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": call_chips,
            "canCheck": False,
            "raiseRange": {"min": 20, "max": 500},
        },
    }


def test_finale_villain_env(monkeypatch: pytest.MonkeyPatch) -> None:
    from finale_villain import finale_exploit_enabled, finale_villain

    monkeypatch.delenv("CEMINI_FINALE_EXPLOIT", raising=False)
    monkeypatch.delenv("CEMINI_FINALE_VILLAIN", raising=False)
    assert finale_exploit_enabled() is False
    assert finale_villain() == "none"

    monkeypatch.setenv("CEMINI_FINALE_EXPLOIT", "1")
    monkeypatch.setenv("CEMINI_FINALE_VILLAIN", "dwan")
    assert finale_villain() == "durrrr"


def test_durrrr_widens_call_vs_bomb(monkeypatch: pytest.MonkeyPatch) -> None:
    from finale_durrrr_exploit import apply_durrrr_overlay

    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    table = _table(call_chips=80, pot=100)
    out = apply_durrrr_overlay(
        table=table,
        allowed=table["allowedActions"],
        available=["fold", "call", "raise"],
        hole=["As", "Kd"],
        board=["Ah", "7d", "2c"],
        street="Flop",
        action_name="fold",
        amount=None,
        equity=0.55,
        pot_odds=0.44,
        call_chips=80,
        pot=100,
        in_position=True,
    )
    assert out == ("call", 80)


def test_jungleman_probe_vs_check(monkeypatch: pytest.MonkeyPatch) -> None:
    from finale_jungleman_exploit import apply_jungleman_overlay

    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    table = _table(call_chips=0, pot=120)
    table["allowedActions"]["availableActions"] = ["check", "bet"]
    table["allowedActions"]["betRange"] = {"min": 10, "max": 200}
    out = apply_jungleman_overlay(
        table=table,
        allowed=table["allowedActions"],
        available=["check", "bet"],
        hole=["As", "Kd"],
        board=["Ah", "7d", "2c"],
        street="Turn",
        action_name="check",
        amount=None,
        equity=0.62,
        pot_odds=0.0,
        call_chips=0,
        pot=120,
        in_position=True,
    )
    assert out is not None
    assert out[0] == "bet"


def test_finale_overlay_disabled_without_env(monkeypatch: pytest.MonkeyPatch) -> None:
    from finale_exploit import apply_finale_action_overlay

    monkeypatch.delenv("CEMINI_FINALE_EXPLOIT", raising=False)
    table = _table()
    assert apply_finale_action_overlay(
        table=table,
        allowed=table["allowedActions"],
        available=["fold", "call"],
        hole=["As", "Kd"],
        board=["Ah", "7d", "2c"],
        street="Flop",
        action_name="fold",
        amount=None,
        equity=0.5,
        pot_odds=0.3,
        call_chips=30,
        pot=100,
        in_position=True,
        ctx={},
    ) is None


def test_bundle_excludes_finale_by_default(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    from submit_sandbox_pvp import _FINALE_ASSETS, _bundle_includes_finale

    monkeypatch.delenv("CEMINI_BUNDLE_FINALE", raising=False)
    assert _bundle_includes_finale() is False
    assert "finale_villain.py" in _FINALE_ASSETS

    monkeypatch.setenv("CEMINI_BUNDLE_FINALE", "1")
    assert _bundle_includes_finale() is True
