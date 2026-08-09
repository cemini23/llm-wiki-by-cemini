"""P2-2 flat-dominate — call over fold/3bet vs leader/nemesis opens IP/BB."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from flat_dominate import (  # noqa: E402
    flat_dominate_enabled,
    is_leader_nemesis_handle,
    try_flat_dominate_call,
)


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("CEMINI_FLAT_DOMINATE", raising=False)
    monkeypatch.delenv("CEMINI_NEMESIS_HANDLES", raising=False)
    monkeypatch.delenv("CEMINI_NEMESIS_PREFIXES", raising=False)


def test_flat_dominate_off_by_default():
    assert flat_dominate_enabled() is False


def test_nemesis_handle_known():
    assert is_leader_nemesis_handle("hunterguy102") is True
    assert is_leader_nemesis_handle("v12_whatever") is True
    assert is_leader_nemesis_handle("random_guy") is False
    assert is_leader_nemesis_handle("") is False


def test_flat_call_vs_nemesis_ip(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    out = try_flat_dominate_call(
        hand_class="AQs", position="BTN", in_position=True,
        call_chips=40, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="hunterguy102",
    )
    assert out == ("call", None)


def test_flat_call_vs_nemesis_bb(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    out = try_flat_dominate_call(
        hand_class="JJ", position="BB", in_position=False,
        call_chips=40, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="thaddius",
    )
    assert out == ("call", None)


def test_flat_not_for_trash(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    assert try_flat_dominate_call(
        hand_class="72o", position="BTN", in_position=True,
        call_chips=40, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="hunterguy102",
    ) is None


def test_flat_not_vs_unknown_villain(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    assert try_flat_dominate_call(
        hand_class="AQs", position="BTN", in_position=True,
        call_chips=40, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="random_guy",
    ) is None


def test_flat_blocked_big_raise(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    assert try_flat_dominate_call(
        hand_class="AQs", position="BTN", in_position=True,
        call_chips=100, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="hunterguy102",
    ) is None


def test_flat_blocked_oop(monkeypatch):
    monkeypatch.setenv("CEMINI_FLAT_DOMINATE", "1")
    assert try_flat_dominate_call(
        hand_class="AQs", position="MP", in_position=False,
        call_chips=40, big_blind=20, hero_stack_chips=1500,
        available=["fold", "call", "raise"], villain_handle="hunterguy102",
    ) is None
