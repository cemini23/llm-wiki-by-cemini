"""K276 withhold contract (arXiv 2608.12292 pattern, Cybersec lane).

Dual-ID:
- Cybersec K276 = withhold contract (2608.12292)   <- this module
- Cybersec K277 = RSM (same 2608.12311)            -> examples/helper_roles.py
- CCC K274 = CDH (2608.12273)                      -> examples/skill_invocation_budget.py
- CCC K275 = VAKRA (2608.12282)                    -> examples/vakra_eval_axes.py
- CCC K276 = RSM (2608.12311)                      -> examples/helper_roles.py

Per-turn machine-checkable "withhold what must not be revealed" contract for
arena agents holding private hole/strategy state. Non-LLM policy core fed
**only decide-trusted state** (hole cards + optional hand_class from decide,
never table chat / tool_result). Deterministic detector outranks the model;
**revise over block** — redacted text is returned instead of raising, because
over-blocking is a measured failure (users route around friction).

Env gate ``CEMINI_WITHHOLD_CONTRACT`` defaults **on** (``1``); ``0`` keeps
``detect_leak`` working but makes ``check_outbound_action`` a no-op
passthrough.
"""
from __future__ import annotations

import logging
import os
import re
from typing import Any

logger = logging.getLogger("arena-pokerkit.withhold_contract")

# Rank tokens accept either case + 10. Explicit character classes (rather than
# re.IGNORECASE) keep matching scoped to rank/suit tokens.
_CARD_PAIR_RE = re.compile(
    r"(?<![A-Za-z0-9])([2-9TJQKAtjqka]|10)([hdscHDSC♥♦♣♠])"
    r"([2-9TJQKAtjqka]|10)([hdscHDSC♥♦♣♠])(?![A-Za-z0-9])"
)
_CARD_SINGLE_RE = re.compile(
    r"(?<![A-Za-z0-9])([2-9TJQKAtjqka]|10)([hdscHDSC♥♦♣♠])"
    r"(?![A-Za-z0-9])"
)
_CARD_WORD_RE = re.compile(
    r"\b(two|three|four|five|six|seven|eight|nine|ten|jack|queen|king|ace)"
    r"\s+of\s+(hearts|diamonds|clubs|spades)\b",
    re.I,
)

_RANK_LETTER = {
    "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8",
    "9": "9", "10": "T", "T": "T", "J": "J", "Q": "Q", "K": "K", "A": "A",
    "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5", "SIX": "6",
    "SEVEN": "7", "EIGHT": "8", "NINE": "9", "TEN": "T", "JACK": "J",
    "QUEEN": "Q", "KING": "K", "ACE": "A",
}
_SUIT_LETTER = {
    "H": "H", "D": "D", "C": "C", "S": "S",
    "♥": "H", "♦": "D", "♣": "C", "♠": "S",
    "HEARTS": "H", "DIAMONDS": "D", "CLUBS": "C", "SPADES": "S",
}

# Hole-card source channels the contract will accept. Observation / table
# chat / tool_result must NEVER supply the secret set — caller passes
# decide-trusted hole cards only.
TRUSTED_HOLE_SOURCES: frozenset[str] = frozenset({"decide", "prebind"})


def _canon(rank: str, suit: str) -> str:
    return _RANK_LETTER.get(str(rank).upper(), "") + _SUIT_LETTER.get(
        str(suit).upper(), ""
    )


def _iter_card_hits(text: str):
    """Yield (start, end, raw, canonical) for every rank-suit token in text."""
    for pattern, groups in (
        (_CARD_PAIR_RE, ((1, 2), (3, 4))),
        (_CARD_SINGLE_RE, ((1, 2),)),
        (_CARD_WORD_RE, ((1, 2),)),
    ):
        for m in pattern.finditer(text):
            candidates = [
                _canon(m.group(r), m.group(s)) for r, s in groups
            ]
            yield (m.start(), m.end(), m.group(0), tuple(candidates))


def _canonical_hole_secrets(hole_cards: Any) -> tuple[set[str], set[str]]:
    """Split provided hole cards into parsed card secrets + literal secrets.

    Parseable cards ("Ah", "A♥", "Ace of hearts", "AhKd") become canonical
    rank-suit tokens. Unparseable strings (e.g. a hand-class shorthand) become
    case-insensitive literal secrets.
    """
    cards: set[str] = set()
    literals: set[str] = set()
    for card in hole_cards or []:
        c = str(card).strip()
        if not c:
            continue
        parsed = False
        for (_s, _e, _raw, candidates) in _iter_card_hits(c):
            for canon in candidates:
                if canon:
                    cards.add(canon)
            parsed = True
        if not parsed:
            literals.add(c.upper())
    return cards, literals


def _redact(text: str, hits: list[tuple[int, int, str, str]]) -> str:
    out: list[str] = []
    last = 0
    for start, end, _raw, kind in hits:
        out.append(text[last:start])
        out.append("[HOLE]" if kind == "hole" else "[HAND]")
        last = end
    out.append(text[last:])
    return "".join(out)


def detect_leak(
    text: Any,
    hole_cards: Any,
    extra_secrets: Any = (),
) -> dict[str, Any]:
    """Detect hole-card / hand-class tokens in text; revise over block.

    Returns ``{leaked: bool, matches: [raw...], revised: str}``. Empty/None
    text is never a leak. Board cards are not in the secret set and are not
    matched — the caller simply never passes board cards as hole_cards.
    """
    if text is None:
        return {"leaked": False, "matches": [], "revised": ""}
    s = text if isinstance(text, str) else str(text)
    if not s.strip():
        return {"leaked": False, "matches": [], "revised": s}

    card_secrets, literal_secrets = _canonical_hole_secrets(hole_cards)
    for extra in extra_secrets or ():
        lit = str(extra).strip()
        if lit:
            literal_secrets.add(lit.upper())

    hits: list[tuple[int, int, str, str]] = []
    for start, end, raw, candidates in _iter_card_hits(s):
        if any(c in card_secrets for c in candidates if c):
            hits.append((start, end, raw, "hole"))
    for lit in literal_secrets:
        for m in re.finditer(rf"\b{re.escape(lit)}\b", s, re.I):
            hits.append((m.start(), m.end(), m.group(0), "hand"))

    hits.sort(key=lambda h: (h[0], h[1]))
    merged: list[tuple[int, int, str, str]] = []
    for hit in hits:
        if merged and hit[0] < merged[-1][1]:
            # Overlapping spans: prefer the wider hole-card kind over hand.
            if merged[-1][3] == "hand" and hit[3] == "hole":
                merged[-1] = hit
            continue
        merged.append(hit)

    return {
        "leaked": bool(merged),
        "matches": [h[2] for h in merged],
        "revised": _redact(s, merged) if merged else s,
    }


def withhold_contract_enabled() -> bool:
    raw = os.environ.get("CEMINI_WITHHOLD_CONTRACT", "1")
    return raw.strip().lower() not in ("0", "false", "no", "off")


def check_outbound_action(
    action: dict[str, Any],
    hole_cards: Any,
    hand_class: str = "",
    hole_source: Any = "decide",
) -> dict[str, Any]:
    """Revise hole/strategy leaks in outbound ``message`` / ``reasoning``.

    Returns a copy of the action with leaking tokens redacted ([HOLE] /
    [HAND]). Never raises on leak — revise over block. Raises ``ValueError``
    only when hole cards are attributed to an untrusted source (observation /
    tool_result must not supply the secret set; decide-trusted state only).

    ``CEMINI_WITHHOLD_CONTRACT=0`` → no-op passthrough (same object back).
    """
    if not withhold_contract_enabled():
        return action

    src = str(hole_source or "decide").strip().lower().replace("-", "_")
    if src not in TRUSTED_HOLE_SOURCES:
        raise ValueError(
            f"withhold contract refuses hole cards from untrusted source "
            f"{hole_source!r} — pass decide-trusted hole cards only"
        )

    if not hole_cards:
        return dict(action)

    out = dict(action)
    extra = [hand_class] if hand_class else []
    for key in ("message", "reasoning"):
        val = out.get(key)
        if not isinstance(val, str) or not val:
            continue
        result = detect_leak(val, hole_cards, extra_secrets=extra)
        if result["leaked"]:
            out[key] = result["revised"]
            logger.info(
                "[arena-pokerkit] withhold revise key=%s matches=%s",
                key,
                result["matches"],
            )
    return out
