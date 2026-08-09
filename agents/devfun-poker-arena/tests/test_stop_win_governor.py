"""P2-4 stop-win governor — default off, pure slow-join decision."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from stop_win_governor import (  # noqa: E402
    stop_win_hands,
    stop_win_mult,
    stop_win_slow_join,
)


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("CEMINI_STOP_WIN_MULT", raising=False)
    monkeypatch.delenv("CEMINI_STOP_WIN_HANDS", raising=False)


def test_stop_win_default_off():
    assert stop_win_mult() == 0.0
    assert stop_win_slow_join(
        hand_count=30, current_stack=5000, start_stack=1000,
    ) is None


def test_stop_win_enabled_via_env(monkeypatch):
    monkeypatch.setenv("CEMINI_STOP_WIN_MULT", "2.2")
    assert stop_win_mult() == 2.2


def test_stop_win_hands_default_20():
    assert stop_win_hands() == 20


def test_stop_win_triggers(monkeypatch):
    monkeypatch.setenv("CEMINI_STOP_WIN_MULT", "2.2")
    out = stop_win_slow_join(
        hand_count=25, current_stack=2400, start_stack=1000,
    )
    assert out is not None and out[0] is True
    assert out[1] == 600


def test_stop_win_not_enough_hands(monkeypatch):
    monkeypatch.setenv("CEMINI_STOP_WIN_MULT", "2.2")
    assert stop_win_slow_join(
        hand_count=19, current_stack=5000, start_stack=1000,
    ) is None


def test_stop_win_not_enough_chips(monkeypatch):
    monkeypatch.setenv("CEMINI_STOP_WIN_MULT", "2.2")
    assert stop_win_slow_join(
        hand_count=25, current_stack=2000, start_stack=1000,
    ) is None
