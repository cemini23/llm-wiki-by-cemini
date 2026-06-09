"""Tests for table_chat_intel — Tier 1 chat leak parsing."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from table_chat_intel import (  # noqa: E402
    extract_chat_intel,
    merge_dead_for_nuts,
    normalize_arena_card,
    nuts_extra_dead_cards,
)


def _table(
    hero_seat: int,
    hole: list[str],
    board: list[str],
    events: list[dict],
) -> dict:
    return {
        "selfSeatNumber": hero_seat,
        "boardCards": board,
        "seats": [{"seatNumber": hero_seat, "holeCards": hole}],
        "recentEvents": events,
    }


def test_normalize_arena_card() -> None:
    assert normalize_arena_card("Ah") == "Ah"
    assert normalize_arena_card("10s") == "Ts"
    assert normalize_arena_card("kd") == "Kd"
    assert normalize_arena_card("") is None


def test_action_taken_villain_cards_become_dead() -> None:
    table = _table(
        1,
        ["Kh", "Qh"],
        ["Jh", "Th", "5h", "2h", "3c"],
        [
            {
                "type": "ActionTaken",
                "summary": {
                    "seatNumber": 3,
                    "agentName": "villain",
                    "cards": ["Ah", "Kd"],
                    "action": "bet",
                },
            },
        ],
    )
    intel = extract_chat_intel(table)
    assert "Ah" in intel["dead_cards"]
    assert "Kd" in intel["dead_cards"]
    assert intel["villain_cards"]["villain@3"] == ["Ah", "Kd"]


def test_hero_cards_not_counted_as_dead() -> None:
    table = _table(
        1,
        ["Kh", "Qh"],
        ["Jh", "Th", "5h", "2h", "3c"],
        [
            {
                "type": "ActionTaken",
                "summary": {
                    "seatNumber": 1,
                    "cards": ["Kh", "Qh"],
                },
            },
        ],
    )
    intel = extract_chat_intel(table)
    assert intel["dead_cards"] == []


def test_showdown_reveal_adds_dead_cards() -> None:
    table = _table(
        2,
        ["9c", "8d"],
        ["9s", "8h", "7d", "6c", "5s"],
        [
            {
                "type": "Showdown",
                "summary": {
                    "seats": [
                        {"seatNumber": 1, "holeCards": ["Ac", "Ad"]},
                    ],
                },
            },
        ],
    )
    intel = extract_chat_intel(table)
    assert "Ac" in intel["dead_cards"]
    assert "Ad" in intel["dead_cards"]


def test_chat_intel_disabled_via_env(monkeypatch) -> None:
    monkeypatch.setenv("CEMINI_CHAT_INTEL", "0")
    table = _table(
        1,
        ["Kh", "Qh"],
        ["Jh", "Th", "5h", "2h", "3c"],
        [
            {
                "type": "ActionTaken",
                "summary": {"seatNumber": 2, "cards": ["Ah", "Kd"]},
            },
        ],
    )
    intel = extract_chat_intel(table)
    assert intel["dead_cards"] == []


def test_nuts_extra_dead_excludes_board_and_hero() -> None:
    hole = ["Kh", "Qh"]
    board = ["Jh", "Th", "5h", "2h", "3c"]
    intel = {"dead_cards": ["Ah", "Kd", "Jh"]}
    extra = merge_dead_for_nuts(hole, board, intel)
    assert extra == ["Ah", "Kd"]


def test_leaked_ah_makes_kh_qh_nuts_unbeatable() -> None:
    from hand_nuts import river_unbeatable, treys_available  # noqa: E402

    if not treys_available():
        return
    hole = ["Kh", "Qh"]
    board = ["Jh", "Th", "5h", "2h", "3c"]
    ok_base, _, _ = river_unbeatable(hole, board)
    assert ok_base is False
    table = _table(
        1,
        hole,
        board,
        [
            {
                "type": "ActionTaken",
                "summary": {"seatNumber": 2, "cards": ["Ah", "2d"]},
            },
        ],
    )
    extra = nuts_extra_dead_cards(table, hole, board)
    ok, _, _ = river_unbeatable(hole, board, extra_dead_arena=extra)
    assert ok is True
