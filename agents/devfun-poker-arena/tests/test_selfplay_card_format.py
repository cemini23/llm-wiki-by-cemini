"""Selfplay pokerkit → Arena card string normalization."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from selfplay import _arena_card_str  # noqa: E402


def test_arena_card_str_pokerkit_nested_list():
    assert _arena_card_str(["Ad"]) == "Ad"


def test_arena_card_str_pokerkit_card_repr():
    class _FakeCard:
        def __repr__(self) -> str:
            return "9c"

        def __str__(self) -> str:
            return "NINE OF CLUBS (9c)"

    assert _arena_card_str(_FakeCard()) == "9c"


def test_arena_card_str_long_form_fallback():
    assert _arena_card_str("ACE OF HEARTS (Ah)") == "Ah"
