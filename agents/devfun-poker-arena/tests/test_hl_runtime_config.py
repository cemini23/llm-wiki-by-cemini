"""HL runtime config + auto-analyst helpers."""
from __future__ import annotations

from pathlib import Path

import pytest

from examples.cemini_decide import decide
from examples.hl_runtime_config import (
    activate_kill_switch,
    clear_kill_switch,
    is_kill_switch_active,
    match_runtime_guard,
    merge_runtime_guards,
)
from examples.testing import _allowed, _table


def test_kill_switch_fold(tmp_path: Path, monkeypatch):
    ks = tmp_path / "kill.json"
    monkeypatch.setenv("CEMINI_KILL_SWITCH_PATH", str(ks))
    activate_kill_switch(reason="test", source="pytest")
    assert is_kill_switch_active()
    clear_kill_switch(source="pytest")
    assert not is_kill_switch_active()


def test_runtime_guard_match(tmp_path: Path, monkeypatch):
    guards = tmp_path / "guards.json"
    monkeypatch.setenv("CEMINI_RUNTIME_GUARDS_PATH", str(guards))
    merge_runtime_guards(
        [{
            "id": "test_sb_trash",
            "street": "Preflop",
            "positions": ["SB"],
            "hand_classes": ["72o"],
            "when_facing_bet": True,
            "action": "fold",
            "reason": "test",
        }],
        source="pytest",
    )
    g = match_runtime_guard(
        street="Preflop",
        position="SB",
        hand_class="72o",
        call_chips=40,
        can_check=False,
    )
    assert g is not None
    assert g["id"] == "test_sb_trash"


def test_decide_respects_kill_switch(tmp_path: Path, monkeypatch):
    ks = tmp_path / "kill.json"
    monkeypatch.setenv("CEMINI_KILL_SWITCH_PATH", str(ks))
    activate_kill_switch(reason="pytest", source="pytest")
    table = _table(
        name="ks",
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=["As", "Ah"],
        hero_stack=1800,
        villain_bet=100,
        villain_committed=100,
        allowed=_allowed(can_call=True, call_chips=100, call_to=100),
    )
    out = decide(table, deadline_s=10.0, research_context={"kill_switch": True})
    assert out["action"] in ("fold", "check")
    clear_kill_switch(source="pytest")


def test_heuristic_catastrophe():
    from examples.cemini_hl_auto_analyst import _heuristic_catastrophe
    trip, _ = _heuristic_catastrophe({
        "hands": 100,
        "net_delta": -8610,
        "losses": 90,
    })
    assert trip is True
