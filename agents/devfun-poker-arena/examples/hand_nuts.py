"""River unbeatable detection via exhaustive treys enumeration.

See briefs/2026-06-05_nuts-detection-spec.md — v1 module only; decide() wiring
requires CEMINI_NUTS_DETECT=1 after test gate passes.
"""
from __future__ import annotations

from itertools import combinations
from typing import Optional

try:
    from treys import Card as TreysCard
    from treys import Deck as TreysDeck
    from treys import Evaluator as TreysEvaluator

    _HAS_TREYS = True
except Exception:  # pragma: no cover
    _HAS_TREYS = False

_EVALUATOR: Optional[TreysEvaluator] = None


def arena_to_treys(card_str: str) -> str:
    """Arena 'Ah' / '10s' → treys 'Ah' / 'Ts'."""
    if not card_str:
        return "2c"
    if card_str.startswith("10"):
        r = "T"
        s = card_str[2].lower() if len(card_str) > 2 else "x"
        return r + s
    return card_str[0].upper() + card_str[-1].lower()


def _evaluator() -> TreysEvaluator:
    global _EVALUATOR
    if _EVALUATOR is None:
        _EVALUATOR = TreysEvaluator()
    return _EVALUATOR


def _to_treys_cards(cards: list[str]) -> Optional[list[int]]:
    if not cards:
        return None
    try:
        return [TreysCard.new(arena_to_treys(c)) for c in cards]
    except Exception:
        return None


def _remaining_deck(dead: set[int]) -> list[int]:
    deck = TreysDeck()
    return [c for c in deck.cards if c not in dead]


def river_unbeatable(
    hole: list[str],
    board: list[str],
    *,
    extra_dead_arena: Optional[list[str]] = None,
) -> tuple[bool, Optional[int], str]:
    """Return (unbeatable, hero_treys_score, hero_class_str).

    Unbeatable means no remaining hole-card pair strictly beats hero on this
    5-card board (chops allowed). False when board incomplete or treys missing.
    """
    if not _HAS_TREYS:
        return False, None, "unknown"
    if len(hole) != 2 or len(board) != 5:
        return False, None, "unknown"

    hole_t = _to_treys_cards(hole)
    board_t = _to_treys_cards(board)
    if hole_t is None or board_t is None:
        return False, None, "unknown"

    dead = set(hole_t) | set(board_t)
    if len(hole_t) != 2 or len(board_t) != 5:
        return False, None, "unknown"
    if len(set(hole_t)) != 2 or len(set(board_t)) != 5:
        return False, None, "unknown"
    if set(hole_t) & set(board_t):
        return False, None, "unknown"

    if extra_dead_arena:
        extra_t = _to_treys_cards(list(extra_dead_arena))
        if extra_t:
            dead |= set(extra_t)

    ev = _evaluator()
    hero_score = ev.evaluate(board_t, hole_t)
    hero_class = ev.class_to_string(ev.get_rank_class(hero_score))

    for c1, c2 in combinations(_remaining_deck(dead), 2):
        if ev.evaluate(board_t, [c1, c2]) < hero_score:
            return False, hero_score, hero_class

    return True, hero_score, hero_class


def best_possible_river_score(
    hole: list[str],
    board: list[str],
    *,
    extra_dead_arena: Optional[list[str]] = None,
) -> Optional[int]:
    """Strongest hand any player could hold (minimum treys score), given dead cards."""
    if not _HAS_TREYS or len(hole) != 2 or len(board) != 5:
        return None
    hole_t = _to_treys_cards(hole)
    board_t = _to_treys_cards(board)
    if hole_t is None or board_t is None:
        return None
    dead = set(hole_t) | set(board_t)
    if len(set(hole_t)) != 2 or len(set(board_t)) != 5:
        return None
    if set(hole_t) & set(board_t):
        return None
    if extra_dead_arena:
        extra_t = _to_treys_cards(list(extra_dead_arena))
        if extra_t:
            dead |= set(extra_t)
    ev = _evaluator()
    best = 7462
    for c1, c2 in combinations(_remaining_deck(dead), 2):
        score = ev.evaluate(board_t, [c1, c2])
        if score < best:
            best = score
    return best


def treys_available() -> bool:
    return _HAS_TREYS
