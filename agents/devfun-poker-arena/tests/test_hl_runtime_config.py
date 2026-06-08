"""HL runtime config + auto-analyst helpers."""
from __future__ import annotations

from pathlib import Path

import pytest

from examples.cemini_decide import decide
from examples.cemini_hl_auto_analyst import apply_response
from examples.hl_runtime_config import (
    activate_kill_switch,
    clear_kill_switch,
    deploy_grace_status,
    is_deploy_grace_active,
    is_kill_switch_active,
    match_runtime_guard,
    merge_runtime_guards,
    record_deploy_grace,
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


def test_deploy_grace_active(tmp_path: Path, monkeypatch):
    grace = tmp_path / "deploy_grace.json"
    monkeypatch.setenv("CEMINI_DEPLOY_GRACE_PATH", str(grace))
    monkeypatch.setenv("CEMINI_HL_DEPLOY_GRACE_HOURS", "6")
    record_deploy_grace(commit="abc1234", round_num=3, hands=114, source="pytest")
    assert is_deploy_grace_active()
    status = deploy_grace_status()
    assert status["commit"] == "abc1234"
    assert status["remaining_hours"] > 0


def test_apply_response_suppresses_kill_during_grace(tmp_path: Path, monkeypatch):
    grace = tmp_path / "deploy_grace.json"
    ks = tmp_path / "kill.json"
    monkeypatch.setenv("CEMINI_DEPLOY_GRACE_PATH", str(grace))
    monkeypatch.setenv("CEMINI_KILL_SWITCH_PATH", str(ks))
    record_deploy_grace(commit="deadbeef", source="pytest")
    out = apply_response({
        "severity": "catastrophic",
        "kill_switch": True,
        "kill_reason": "test bleed",
        "runtime_guards": [],
        "style_tweaks": {},
    })
    assert "suppressed_kill_switch" in out["actions_taken"]
    assert not is_kill_switch_active()
    assert out.get("kill_switch_suppressed") is True
