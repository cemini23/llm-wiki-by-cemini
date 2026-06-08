"""HL runtime config + auto-analyst helpers."""
from __future__ import annotations

from pathlib import Path

import pytest

from examples.cemini_decide import decide
from examples.cemini_hl_auto_analyst import apply_response
from examples.hl_runtime_config import (
    activate_kill_switch,
    apply_style_overrides,
    clear_kill_switch,
    deploy_grace_status,
    is_deploy_grace_active,
    is_kill_switch_active,
    load_style_overrides,
    match_runtime_guard,
    merge_runtime_guards,
    record_deploy_grace,
    repair_runtime_guards,
    reset_style_overrides,
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


def test_when_facing_shove_guard(tmp_path: Path, monkeypatch):
    guards = tmp_path / "guards.json"
    monkeypatch.setenv("CEMINI_RUNTIME_GUARDS_PATH", str(guards))
    merge_runtime_guards([{
        "id": "btn_trash_vs_shove",
        "street": "Preflop",
        "positions": ["BTN"],
        "hand_classes": ["T5o", "Q9o"],
        "when_facing_shove": True,
        "min_commit_ratio": 0.28,
        "action": "fold",
        "reason": "test",
    }], source="pytest")
    g = match_runtime_guard(
        street="Preflop",
        position="BTN",
        hand_class="T5o",
        call_chips=400,
        can_check=False,
        hero_stack_chips=1000,
    )
    assert g is not None
    assert match_runtime_guard(
        street="Preflop",
        position="BTN",
        hand_class="T5o",
        call_chips=40,
        can_check=False,
        hero_stack_chips=1000,
    ) is None


def test_opening_guard_gets_shove_companion(tmp_path: Path, monkeypatch):
    guards = tmp_path / "guards.json"
    monkeypatch.setenv("CEMINI_RUNTIME_GUARDS_PATH", str(guards))
    merge_runtime_guards([{
        "id": "btn_co_open_fold_weak_offsuit",
        "street": "Preflop",
        "positions": ["BTN", "CO"],
        "hand_classes": ["T5o", "QJo", "72o"],
        "when_opening": True,
        "action": "fold",
        "reason": "test",
    }], source="pytest")
    repaired = repair_runtime_guards(source="pytest")
    ids = {g["id"] for g in repaired}
    assert "btn_co_open_fold_weak_offsuit_vs_shove" in ids
    g = match_runtime_guard(
        street="Preflop",
        position="BTN",
        hand_class="T5o",
        call_chips=500,
        can_check=False,
        hero_stack_chips=1000,
    )
    assert g is not None
    assert g["id"] == "btn_co_open_fold_weak_offsuit_vs_shove"


def test_style_delta_clamp_and_reset_on_deploy(tmp_path: Path, monkeypatch):
    style = tmp_path / "style.json"
    grace = tmp_path / "grace.json"
    monkeypatch.setenv("CEMINI_STYLE_OVERRIDES_PATH", str(style))
    monkeypatch.setenv("CEMINI_DEPLOY_GRACE_PATH", str(grace))
    apply_style_overrides({"fold_slack_delta": 0.12, "call_margin_delta": 0.15})
    assert load_style_overrides()["fold_slack_delta"] == 0.08
    assert load_style_overrides()["call_margin_delta"] == 0.08
    record_deploy_grace(commit="abc1234", source="pytest")
    assert load_style_overrides()["fold_slack_delta"] == 0.0
    reset_style_overrides(source="pytest", commit="manual")


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
