"""Rule-based XSP relevance scoring — no LLM calls."""

from __future__ import annotations

from typing import Any

# Keywords from the ops-loop spec (case-insensitive substring match)
XSP_KEYWORDS: tuple[str, ...] = (
    "sox",
    "semiconductor",
    "semis",
    "rates",
    "yields",
    "oil",
    "yen",
    "cpi",
    "inflation",
    "nvidia",
    "tsmc",
    "asml",
    "fed",
    "fomc",
    "regime",
    "breadth",
    "risk-on",
    "risk-off",
)

# High-signal names / sectors for priority boost
HIGH_PRIORITY_KEYWORDS: tuple[str, ...] = (
    "nvidia",
    "tsmc",
    "asml",
    "sox",
    "semiconductor",
    "semis",
    "fomc",
)

MEDIUM_PRIORITY_KEYWORDS: tuple[str, ...] = (
    "rates",
    "yields",
    "cpi",
    "inflation",
    "fed",
    "regime",
    "breadth",
    "risk-on",
    "risk-off",
    "oil",
    "yen",
)


def _haystack(post: dict[str, Any]) -> str:
    parts = [
        str(post.get("title") or ""),
        str(post.get("excerpt") or ""),
        str(post.get("url") or ""),
        " ".join(post.get("regime_tags") or []),
    ]
    return " ".join(parts).lower()


def matched_keywords(post: dict[str, Any]) -> list[str]:
    text = _haystack(post)
    return [k for k in XSP_KEYWORDS if k in text]


def triage_post(post: dict[str, Any]) -> dict[str, Any]:
    """Return priority, action, and matched keywords for a post.

    action:
      - packet — clear XSP relevance, emit research packet
      - watch  — some macro relevance but weak XSP link
      - skip   — no keyword hits
    priority: high | med | low
    """
    hits = matched_keywords(post)
    if not hits:
        return {
            "priority": "low",
            "action": "skip",
            "matched_keywords": [],
            "reason": "no XSP keywords",
        }

    high_hits = [k for k in hits if k in HIGH_PRIORITY_KEYWORDS]
    med_hits = [k for k in hits if k in MEDIUM_PRIORITY_KEYWORDS]

    if high_hits:
        priority = "high"
        action = "packet"
        reason = f"high-signal: {', '.join(high_hits)}"
    elif med_hits:
        priority = "med"
        action = "packet"
        reason = f"macro-XSP: {', '.join(med_hits)}"
    else:
        # keyword hit but only low-weight (e.g. lone 'oil' already in MEDIUM)
        priority = "low"
        action = "watch"
        reason = f"weak match: {', '.join(hits)}"

    # Single weak hit → watch instead of full packet
    if action == "packet" and len(hits) == 1 and not high_hits and hits[0] in ("oil", "yen"):
        action = "watch"
        priority = "low"
        reason = f"single weak keyword: {hits[0]}"

    return {
        "priority": priority,
        "action": action,
        "matched_keywords": hits,
        "reason": reason,
    }
