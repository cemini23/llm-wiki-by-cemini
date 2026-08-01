"""Tests for short-stack push/fold + gin kill switch."""
from __future__ import annotations

import os

import pytest


def test_gin_killed_blocks_style(monkeypatch: pytest.MonkeyPatch):
    from gin_style import gin_killed, gin_style_preflop_enabled, gin_style_postflop_enabled

    monkeypatch.setenv("CEMINI_GIN_KILL", "1")
    monkeypatch.setenv("CEMINI_GIN_STYLE", "1")
    monkeypatch.setenv("CEMINI_GIN_STYLE_PREFLOP", "1")
    monkeypatch.setenv("CEMINI_GIN_STYLE_POSTFLOP", "1")
    assert gin_killed()
    assert not gin_style_preflop_enabled()
    assert not gin_style_postflop_enabled()


def test_gin_alive_when_kill_off(monkeypatch: pytest.MonkeyPatch):
    from gin_style import gin_style_preflop_enabled

    monkeypatch.delenv("CEMINI_GIN_KILL", raising=False)
    monkeypatch.setenv("CEMINI_GIN_STYLE_PREFLOP", "1")
    assert gin_style_preflop_enabled()


def test_short_stack_detect():
    from short_stack import is_short_stack, hero_stack_bb

    table = {
        "bigBlind": 20,
        "selfSeatNumber": 1,
        "seats": [{"seatNumber": 1, "stackChips": 300}],
    }
    assert hero_stack_bb(table) == 15.0
    assert is_short_stack(table)


def test_short_stack_push_btn_open():
    from short_stack import short_stack_preflop_action

    act = short_stack_preflop_action(
        hand_class="ATs",
        position="BTN",
        available=["fold", "raise", "all-in"],
        allowed={"canRaise": True, "canAllIn": True, "canFold": True},
        call_chips=0,
        stack_chips=280,
    )
    assert act is not None
    assert act[0] in ("raise", "all-in")


def test_short_stack_fold_trash():
    from short_stack import short_stack_preflop_action

    act = short_stack_preflop_action(
        hand_class="72o",
        position="UTG",
        available=["fold", "raise"],
        allowed={"canRaise": True, "canFold": True},
        call_chips=0,
        stack_chips=200,
    )
    assert act == ("fold", None)
