"""Blind-orbit cost estimates for Playground chip preservation."""
from __future__ import annotations

DEFAULT_SB = 10
DEFAULT_BB = 20
DEFAULT_PLAYERS = 6


def blind_orbit_chips(table: dict | None = None) -> int:
    """Chips posted per full table orbit (one SB + one BB)."""
    if table:
        sb = int(table.get("smallBlindChips") or DEFAULT_SB)
        bb = int(table.get("bigBlindChips") or DEFAULT_BB)
        return sb + bb
    return DEFAULT_SB + DEFAULT_BB


def avg_blind_tax_per_hand(table: dict | None = None, *, players: int = DEFAULT_PLAYERS) -> float:
    """Expected blind chips lost per hand if never entering pots (6-max heuristic)."""
    return blind_orbit_chips(table) / max(players, 2)


def hands_to_erosion(buffer_chips: int, table: dict | None = None) -> int:
    """Hands of pure blind fold before buffer chips erode to zero."""
    tax = avg_blind_tax_per_hand(table)
    if tax <= 0:
        return 0
    return int(buffer_chips / tax)


# BTN/CO min-steal sets while lead-protect is on — chart-approved pressure, not maniac widens.
_BTN_LEAD_STEAL = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT",
    "A2s", "A3s", "A4s", "A5s", "A6s", "A7s", "A8s", "A9s", "ATs", "AJs", "AQs", "AKs",
    "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "QJs", "QTs", "JTs", "T9s",
})

_CO_LEAD_STEAL = frozenset({
    "55", "66", "77", "88", "99", "TT",
    "A9s", "ATs", "AJs", "AQs", "AKs", "ATo", "AJo", "AQo", "AKo",
    "KJs", "KTs", "KQs", "QJs", "JTs",
})


def lead_blind_steal(hand_class: str, position: str) -> bool:
    """True when lead-protect should still open to recapture blind decay."""
    if position == "BTN":
        return hand_class in _BTN_LEAD_STEAL
    if position == "CO":
        return hand_class in _CO_LEAD_STEAL
    return False


# placement_chase (rank > prize cutoff): widen steals toward top-20 VPIP (~25%) without maniac.
_CHASE_BTN_STEAL = _BTN_LEAD_STEAL | frozenset({
    "22", "33", "44",
    "A2o", "A3o", "A4o", "A5o", "A6o", "A7o",
    "K8s", "K9o", "K8o", "K7s", "Q9o", "Q9s", "Q8s", "Q8o",
    "J9o", "J9s", "J8s", "T9o", "T8s", "T8o", "98o", "98s",
    "87s", "76s", "65s", "54s", "97s", "86s", "96o", "85o",
})

_CHASE_CO_STEAL = _CO_LEAD_STEAL | frozenset({
    "22", "33", "44",
    "A2s", "A3s", "A4s", "A5s", "A6s", "A7s", "A8s", "A8o", "A9o",
    "K9s", "K9o", "K8s", "K7s", "Q9s", "Q9o", "Q8s", "J9s", "J9o", "J8s",
    "T9s", "T9o", "T8s", "98o", "98s", "87s", "76s", "65s", "54s",
})

_CHASE_MP_STEAL = frozenset({
    "66", "77", "88", "99", "TT", "JJ", "QQ", "KK", "AA",
    "ATs", "AJs", "AQs", "AKs", "AQo", "AKo", "AJo",
    "KQs", "KJs", "QJs", "JTs", "T9s", "98s", "87s",
})

_CHASE_SB_STEAL = frozenset({
    "22", "33", "44", "55", "66", "77", "88", "99", "TT",
    "A2s", "A3s", "A4s", "A5s", "A6s", "A7s", "A8s", "A9s",
    "ATs", "AJs", "AQs", "AKs", "A9o", "ATo", "AJo", "AQo", "AKo",
    "K9s", "KTs", "KJs", "KQs", "QJs", "QTs", "JTs", "T9s", "98s", "87s",
})


def placement_chase_steal(hand_class: str, position: str) -> bool:
    """True when placement_chase should open-steal (CO/BTN/SB/MP pressure lane)."""
    if position == "BTN":
        return hand_class in _CHASE_BTN_STEAL
    if position == "CO":
        return hand_class in _CHASE_CO_STEAL
    if position == "SB":
        return hand_class in _CHASE_SB_STEAL
    if position == "MP":
        return hand_class in _CHASE_MP_STEAL
    return False
