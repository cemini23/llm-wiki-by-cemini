"""Parse Arena table chat / recentEvents for leaked villain cards (Tier 1).

The live UI chat mirrors `recentEvents` on pending-actions tables — especially
`ActionTaken.summary.cards` and showdown reveals. Use only API fields (no scraping).
"""
from __future__ import annotations

import os
from typing import Any, Optional


def chat_intel_enabled() -> bool:
    raw = os.environ.get("CEMINI_CHAT_INTEL", "1")
    return raw.strip().lower() not in ("0", "false", "no", "off")


def normalize_arena_card(card: Any) -> Optional[str]:
    """Normalize to Arena-style card token (Ah, Ts, …)."""
    if not card or not isinstance(card, str):
        return None
    s = card.strip()
    if not s:
        return None
    if s.startswith("10") and len(s) >= 3:
        rank, suit = "T", s[2].lower()
    else:
        if len(s) < 2:
            return None
        rank, suit = s[0].upper(), s[-1].lower()
    if rank not in "23456789TJQKA" or suit not in "shdc":
        return None
    return f"{rank}{suit}"


def _hero_hole_and_board(table: dict) -> tuple[list[str], list[str], Optional[int]]:
    hero_seat = table.get("selfSeatNumber")
    board = list(table.get("boardCards") or [])
    hole: list[str] = []
    if hero_seat is not None:
        for seat in table.get("seats") or []:
            if seat.get("seatNumber") == hero_seat:
                hole = list(seat.get("holeCards") or [])
                break
    return hole, board, int(hero_seat) if hero_seat is not None else None


def _cards_from_summary(summary: dict) -> list[str]:
    out: list[str] = []
    if not isinstance(summary, dict):
        return out
    raw = summary.get("cards") or summary.get("holeCards")
    if isinstance(raw, list):
        for c in raw:
            nc = normalize_arena_card(c)
            if nc:
                out.append(nc)
    for row in summary.get("seats") or summary.get("hands") or []:
        if not isinstance(row, dict):
            continue
        hc = row.get("holeCards") or row.get("cards")
        if isinstance(hc, list):
            for c in hc:
                nc = normalize_arena_card(c)
                if nc:
                    out.append(nc)
    return out


def _villain_key(summary: dict) -> str:
    seat = summary.get("seatNumber")
    name = summary.get("agentName") or summary.get("agentHandle")
    if seat is not None and name:
        return f"{name}@{seat}"
    if seat is not None:
        return f"seat:{seat}"
    if name:
        return str(name)
    return "unknown"


def extract_chat_intel(table: dict) -> dict[str, Any]:
    """
    Return Tier-1 chat intel from `table.recentEvents`.

    dead_cards: villain hole cards seen in chat/showdown, excluding hero hole + board
    villain_cards: per-villain leaked cards (audit / future tiers)
  showdown_cards: all cards revealed at showdown events
    """
    if not chat_intel_enabled():
        return {
            "dead_cards": [],
            "villain_cards": {},
            "showdown_cards": [],
            "event_count": 0,
        }

    hero_hole, board, hero_seat = _hero_hole_and_board(table)
    hero_set = set(hero_hole)
    board_set = set(board)

    villain_cards: dict[str, list[str]] = {}
    showdown_cards: list[str] = []
    dead: set[str] = set()

    for ev in table.get("recentEvents") or []:
        if not isinstance(ev, dict):
            continue
        typ = ev.get("type") or ""
        summary = ev.get("summary") if isinstance(ev.get("summary"), dict) else {}
        cards = _cards_from_summary(summary)
        if not cards:
            continue

        seat = summary.get("seatNumber")
        is_villain = hero_seat is None or seat is None or int(seat) != hero_seat

        if typ == "Showdown":
            for c in cards:
                if c not in hero_set and c not in board_set:
                    dead.add(c)
                showdown_cards.append(c)
            if is_villain and seat is not None:
                key = _villain_key(summary)
                villain_cards.setdefault(key, []).extend(cards)
        elif typ == "ActionTaken" and is_villain:
            key = _villain_key(summary)
            villain_cards.setdefault(key, []).extend(cards)
            for c in cards:
                if c not in hero_set and c not in board_set:
                    dead.add(c)

    return {
        "dead_cards": sorted(dead),
        "villain_cards": villain_cards,
        "showdown_cards": showdown_cards,
        "event_count": len(table.get("recentEvents") or []),
    }


def nuts_extra_dead_cards(
    table: dict,
    hole: list[str],
    board: list[str],
    chat_intel: Optional[dict] = None,
) -> list[str]:
    """Dead cards from chat intel for river_unbeatable extra_dead_arena."""
    intel = chat_intel if chat_intel is not None else extract_chat_intel(table)
    return merge_dead_for_nuts(hole, board, intel)


def merge_dead_for_nuts(hole: list[str], board: list[str], chat_intel: dict) -> list[str]:
    """Extra dead cards safe to pass into river_unbeatable (excludes hero + board)."""
    hero_set = set(hole)
    board_set = set(board)
    extra: list[str] = []
    for c in chat_intel.get("dead_cards") or []:
        if c in hero_set or c in board_set:
            continue
        if c not in extra:
            extra.append(c)
    return extra
