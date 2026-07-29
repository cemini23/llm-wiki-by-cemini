"""Eval S1 panel-exploit profile — unit checks."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
import sys

if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from eval_s1_profile import (  # noqa: E402
    PANEL_AGENT_IDS,
    apply_eval_s1_env_defaults,
    competition_is_eval,
    eval_exploit_margins,
    eval_s1_profile_active,
    table_has_eval_panel,
)


@pytest.fixture(autouse=True)
def _clear_profile_env(monkeypatch):
    for key in (
        "CEMINI_ARENA_PROFILE",
        "CEMINI_TABLE_FORMAT",
        "CEMINI_RESEARCHER_MODE",
        "CEMINI_SOLVER_V3",
        "CEMINI_NEMESIS_HANDLES",
    ):
        monkeypatch.delenv(key, raising=False)
    yield


def test_competition_is_eval():
    assert competition_is_eval("seed_poker_eval_s1")
    assert not competition_is_eval("cmr3n8tft01nilecm1u5jlny7")


def test_apply_defaults_activates_profile(monkeypatch):
    apply_eval_s1_env_defaults()
    assert eval_s1_profile_active()
    assert os.environ["CEMINI_TABLE_FORMAT"] == "6max"
    assert os.environ["CEMINI_RESEARCHER_MODE"] == "0"
    assert os.environ["CEMINI_SOLVER_V3"] == "0"
    handles = os.environ["CEMINI_NEMESIS_HANDLES"]
    assert "devfun_arena_poker_bot_1" in handles


def test_exploit_margins_widen_vs_nit():
    apply_eval_s1_env_defaults()
    m = eval_exploit_margins()
    assert m["open_steal_equity"] <= 0.20
    assert m["call_margin_delta"] < 0  # call down light
    assert m["bet_bar_delta"] < 0  # value thinner


def test_crush_opens_wide():
    apply_eval_s1_env_defaults()
    from eval_s1_profile import try_eval_panel_crush

    allowed = {
        "canRaise": True,
        "canBet": False,
        "canCall": False,
        "canCheck": True,
        "canFold": True,
        "raiseRange": {"min": 40, "max": 1000},
    }
    # A9o ~ mid score — should open under crush
    out = try_eval_panel_crush(
        {},
        allowed,
        ["fold", "check", "raise"],
        ["Ah", "9d"],
        [],
        "Preflop",
        30,
        0,
    )
    assert out is not None
    assert out[0] == "raise"


def test_table_has_eval_panel():
    table = {
        "seats": [
            {"seatNumber": 1, "agentId": "cmpy4lcyi001y11vnekn1zlo3"},
            {"seatNumber": 2, "agentId": "devfun_arena_poker_bot_3"},
        ]
    }
    assert table_has_eval_panel(table)
    assert PANEL_AGENT_IDS
    assert not table_has_eval_panel({"seats": [{"agentId": "other"}]})
