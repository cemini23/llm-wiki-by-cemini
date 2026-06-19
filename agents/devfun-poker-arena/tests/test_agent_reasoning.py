"""agent.py reasoning + researcher runtime helpers."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from agent import _apply_researcher_runtime_context, _build_reasoning  # noqa: E402
from position_utils import hero_is_in_position  # noqa: E402


def _table(self_seat: int, street: str = "Flop", board: list[str] | None = None) -> dict:
    seats = [{"seatNumber": i, "stackChips": 1000, "status": "Active"} for i in range(1, 7)]
    return {
        "street": street,
        "selfSeatNumber": self_seat,
        "seats": seats,
        "boardCards": board or ["Kh", "7d", "2c"],
        "buttonSeatNumber": 1,
    }


def test_build_reasoning_uses_position_not_seat_parity():
    ip_table = _table(1)  # BTN
    oop_table = _table(2)  # SB
    ip_yaml = _build_reasoning("check", 0.55, 0.2, ip_table, {})
    oop_yaml = _build_reasoning("check", 0.45, 0.2, oop_table, {})
    if hero_is_in_position(ip_table):
        assert "IP" in ip_yaml
    else:
        assert "OOP" in ip_yaml
    if hero_is_in_position(oop_table):
        assert "IP" in oop_yaml
    else:
        assert "OOP" in oop_yaml
    assert ip_yaml != oop_yaml or hero_is_in_position(ip_table) == hero_is_in_position(oop_table)
    assert "ln:unknown" not in ip_yaml
    assert "@" in ip_yaml  # position tag in vr


def test_researcher_runtime_strips_eval_panel(monkeypatch):
    monkeypatch.setenv("CEMINI_RESEARCHER_MODE", "1")
    ctx = {"eval_panel_mode": True, "placement_chase": True}
    out = _apply_researcher_runtime_context(ctx)
    assert out.get("researcher_mode") is True
    assert "eval_panel_mode" not in out
    assert out.get("placement_chase") is False
