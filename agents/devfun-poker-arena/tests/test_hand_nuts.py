"""Unit tests for river unbeatable enumeration (hand_nuts.py)."""
from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from hand_nuts import (  # noqa: E402
    arena_to_treys,
    best_possible_river_score,
    river_unbeatable,
    treys_available,
)

pytestmark = pytest.mark.skipif(not treys_available(), reason="treys not installed")


# (hole, board, expected_unbeatable, label)
_MATRIX: list[tuple[list[str], list[str], bool, str]] = [
    (["Qh", "Jh"], ["Ah", "Kh", "Th", "5d", "2c"], True, "royal"),
    (["Ac", "Ah"], ["As", "Ad", "7c", "2h", "3s"], True, "quad_aces"),
    (["Ac", "3h"], ["As", "Ad", "7c", "7h", "2s"], False, "vulnerable_boat"),
    (["Tc", "2d"], ["9s", "8h", "7d", "6c", "5s"], False, "board_straight"),
    (["Jc", "Th"], ["9s", "8h", "7d", "6c", "2s"], True, "nut_straight"),
    (["9c", "8d"], ["9s", "8h", "7d", "6c", "5s"], False, "lower_straight"),
    (["Ah", "Qh"], ["Jh", "Th", "5h", "2h", "3c"], True, "nut_flush"),
    (["Kh", "Qd"], ["Jh", "Th", "5h", "2h", "3c"], False, "second_nut_flush"),
    (["Ah", "2c"], ["Jh", "Th", "5h", "7h", "3c"], False, "flush_board_sf_possible"),
    (["Ad", "Kc"], ["Qh", "Jh", "2h", "7h", "3c"], False, "high_card_on_flush_board"),
    (["3d", "4c"], ["2c", "2d", "2h", "2s", "Ac"], True, "board_quad_chop"),
    (["7c", "2d"], ["7s", "7h", "Kd", "3c", "2s"], False, "vulnerable_full_house"),
]


@pytest.mark.parametrize("hole,board,expected,label", _MATRIX)
def test_river_unbeatable_matrix(
    hole: list[str],
    board: list[str],
    expected: bool,
    label: str,
) -> None:
    unbeatable, score, cls = river_unbeatable(hole, board)
    assert unbeatable is expected, f"{label}: score={score} class={cls}"
    if expected:
        assert score is not None
        assert cls != "unknown"


def test_incomplete_board_returns_false() -> None:
    ok, score, cls = river_unbeatable(["As", "Kd"], ["Qh", "Jc", "2d"])
    assert ok is False and score is None and cls == "unknown"


def test_duplicate_card_returns_false() -> None:
    ok, _, _ = river_unbeatable(["As", "As"], ["Ad", "Kh", "Qc", "Jd", "2s"])
    assert ok is False


def test_royal_score_is_one() -> None:
    ok, score, cls = river_unbeatable(["Qh", "Jh"], ["Ah", "Kh", "Th", "5d", "2c"])
    assert ok is True
    assert score == 1
    assert cls == "Royal Flush"


def test_unbeatable_implies_hero_at_least_as_strong_as_best_villain() -> None:
    """Lower treys score = stronger; unbeatable hero must beat or tie best villain hand."""
    for hole, board, expected, label in _MATRIX:
        if not expected:
            continue
        ok, hero_score, _ = river_unbeatable(hole, board)
        best_villain = best_possible_river_score(hole, board)
        assert ok is True, label
        assert hero_score <= best_villain, (
            f"{label}: hero {hero_score} worse than best villain {best_villain}"
        )


def test_property_no_villain_beats_when_unbeatable() -> None:
    from treys import Card, Deck, Evaluator

    ev = Evaluator()
    for hole, board, expected, label in _MATRIX:
        if not expected:
            continue
        hole_t = [Card.new(arena_to_treys(c)) for c in hole]
        board_t = [Card.new(arena_to_treys(c)) for c in board]
        dead = set(hole_t) | set(board_t)
        hero_score = ev.evaluate(board_t, hole_t)
        deck = Deck()
        remaining = [c for c in deck.cards if c not in dead]
        for c1, c2 in combinations(remaining, 2):
            v_score = ev.evaluate(board_t, [c1, c2])
            assert v_score >= hero_score, f"{label}: villain {v_score} < hero {hero_score}"


def test_not_unbeatable_has_at_least_one_beater() -> None:
    from treys import Card, Deck, Evaluator

    ev = Evaluator()
    for hole, board, expected, label in _MATRIX:
        if expected:
            continue
        hole_t = [Card.new(arena_to_treys(c)) for c in hole]
        board_t = [Card.new(arena_to_treys(c)) for c in board]
        dead = set(hole_t) | set(board_t)
        hero_score = ev.evaluate(board_t, hole_t)
        deck = Deck()
        remaining = [c for c in deck.cards if c not in dead]
        found_beater = any(
            ev.evaluate(board_t, [c1, c2]) < hero_score
            for c1, c2 in combinations(remaining, 2)
        )
        assert found_beater, f"{label}: expected a villain hand that beats hero"


def test_arena_to_treys_ten() -> None:
    assert arena_to_treys("10h") == "Th"
    assert arena_to_treys("Ah") == "Ah"
