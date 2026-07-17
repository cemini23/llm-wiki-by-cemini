"""K176 claimed-authorization guard (arXiv 2607.11698 pattern).

Self-claimed authorization from observation / tool-result channels is
invalid. Privileged bankroll, table-bind, and submit intents require
standing from the real operator or prebind path only.

Pattern only — no AHA harness / Vulnerability Concept Graph install.
Pairs with K164 capability-tree submit leaf + K167 message isolation.
"""
from __future__ import annotations

import logging
import re
from typing import Any, Literal, Optional

logger = logging.getLogger("arena-pokerkit.claimed_auth")

Channel = Literal["operator", "prebind", "observation", "tool_result", "unknown"]
Intent = Literal[
    "submit_sandbox",
    "all_in",
    "bankroll_spend",
    "live_table_action",
]

TRUSTED_CHANNELS: frozenset[str] = frozenset({"operator", "prebind"})
UNTRUSTED_CHANNELS: frozenset[str] = frozenset(
    {"observation", "tool_result", "unknown"}
)

PRIVILEGED_INTENTS: frozenset[str] = frozenset(
    {
        "submit_sandbox",
        "all_in",
        "bankroll_spend",
        "live_table_action",
    }
)

# Phrases that look like approval claims in untrusted table/chat text.
_CLAIM_PHRASE_RE = re.compile(
    r"(?i)\b("
    r"user\s+approved|"
    r"authorized\s+all[\s-]?in|"
    r"operator\s+approved|"
    r"approved\s+all[\s-]?in|"
    r"prebind\s+ok|"
    r"standing\s+granted|"
    r"auth(?:orization)?\s*[:=]\s*(?:true|yes|ok|granted)"
    r")\b"
)

_DENY_OBSERVATION = "claim came from observation, not operator"
_DENY_TOOL = "claim came from tool_result, not operator"
_DENY_UNKNOWN = "claim channel unknown — not operator/prebind standing"
_DENY_UNPRIVILEGED_CHANNEL = "privileged intent requires operator or prebind channel"


def normalize_channel(channel: Any) -> str:
    if channel is None:
        return "unknown"
    c = str(channel).strip().lower().replace("-", "_")
    if c in ("op", "operator", "human", "user_cli"):
        return "operator"
    if c in ("prebind", "pre_bind", "pin", "prebind_pin"):
        return "prebind"
    if c in ("observation", "obs", "table", "chat", "message", "seat_message"):
        return "observation"
    if c in ("tool_result", "tool", "tool_output", "mcp_result"):
        return "tool_result"
    if c in TRUSTED_CHANNELS | UNTRUSTED_CHANNELS:
        return c
    return "unknown"


def normalize_intent(intent: Any) -> str:
    raw = str(intent or "").strip().lower().replace("-", "_")
    aliases = {
        "submit": "submit_sandbox",
        "sandbox_submit": "submit_sandbox",
        "allin": "all_in",
        "all_in": "all_in",
        "shove": "all_in",
        "bankroll": "bankroll_spend",
        "spend": "bankroll_spend",
        "live_action": "live_table_action",
        "table_action": "live_table_action",
        "bind": "live_table_action",
    }
    return aliases.get(raw, raw)


def detect_claimed_authorization(text: Any) -> list[str]:
    """Return matched claim phrases in untrusted text (empty if none)."""
    if text is None:
        return []
    s = text if isinstance(text, str) else str(text)
    if not s.strip():
        return []
    return [m.group(0) for m in _CLAIM_PHRASE_RE.finditer(s)]


def strip_claimed_authorization_phrases(text: Any) -> tuple[str, list[str]]:
    """Strip claim phrases; return (cleaned_text, hits)."""
    if text is None:
        return "", []
    s = text if isinstance(text, str) else str(text)
    hits = detect_claimed_authorization(s)
    if not hits:
        return s, []
    cleaned = _CLAIM_PHRASE_RE.sub("[claim-stripped]", s)
    return cleaned, hits


def standing_from_observation_claim(
    text: Any = None,
    *,
    channel: Any = "observation",
) -> bool:
    """Observation/tool prose never grants prebind or bankroll standing."""
    ch = normalize_channel(channel)
    if ch in UNTRUSTED_CHANNELS:
        return False
    # Even on trusted channels, raw text is not a standing token.
    return False


def authorize(
    intent: str,
    *,
    channel: Any,
    evidence: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Authorize a privileged intent against the claim channel.

    Returns ``{ok: bool, reason: str, intent, channel, privileged}``.
    Denies when channel ∈ {observation, tool_result, unknown} for
    privileged intents. Logs the enabling deny condition.
    """
    intent_n = normalize_intent(intent)
    channel_n = normalize_channel(channel)
    privileged = intent_n in PRIVILEGED_INTENTS
    evidence = dict(evidence or {})

    result: dict[str, Any] = {
        "schema": "devfun.claimed_authorization.v1",
        "ok": False,
        "reason": "",
        "intent": intent_n,
        "channel": channel_n,
        "privileged": privileged,
        "evidence_keys": sorted(evidence.keys()),
    }

    if not privileged:
        result["ok"] = True
        result["reason"] = "non-privileged intent — no standing required"
        return result

    if channel_n == "observation":
        result["reason"] = _DENY_OBSERVATION
        logger.info(
            "[arena-pokerkit] claimed-auth deny intent=%s channel=%s reason=%s",
            intent_n,
            channel_n,
            result["reason"],
        )
        return result

    if channel_n == "tool_result":
        result["reason"] = _DENY_TOOL
        logger.info(
            "[arena-pokerkit] claimed-auth deny intent=%s channel=%s reason=%s",
            intent_n,
            channel_n,
            result["reason"],
        )
        return result

    if channel_n == "unknown":
        result["reason"] = _DENY_UNKNOWN
        logger.info(
            "[arena-pokerkit] claimed-auth deny intent=%s channel=%s reason=%s",
            intent_n,
            channel_n,
            result["reason"],
        )
        return result

    if channel_n not in TRUSTED_CHANNELS:
        result["reason"] = _DENY_UNPRIVILEGED_CHANNEL
        logger.info(
            "[arena-pokerkit] claimed-auth deny intent=%s channel=%s reason=%s",
            intent_n,
            channel_n,
            result["reason"],
        )
        return result

    # Observation-shaped evidence never upgrades a trusted channel by itself;
    # trusted channel + optional prebind_ok flag is enough for submit paths.
    claim_text = evidence.get("claim_text") or evidence.get("message") or ""
    if claim_text and channel_n in TRUSTED_CHANNELS:
        # Claims in evidence are informational only; standing is the channel.
        result["claim_phrases"] = detect_claimed_authorization(claim_text)

    result["ok"] = True
    result["reason"] = f"standing from {channel_n}"
    return result


def prebind_ok_from_channel(
    *,
    channel: Any,
    operator_prebind: bool = False,
) -> bool:
    """Compute prebind_ok. Observation/tool/unknown never set True."""
    ch = normalize_channel(channel)
    if ch not in TRUSTED_CHANNELS:
        return False
    return bool(operator_prebind)


def isolate_table_observation_text(table: dict[str, Any]) -> dict[str, Any]:
    """Shallow-copy table; strip claimed-auth phrases from seat/event messages.

    Treats opponent ``message`` fields as DATA (K167), never as approval.
    Does not alter stacks, allowedActions, or hole cards.
    """
    out = dict(table)
    stripped: list[dict[str, Any]] = []

    seats = out.get("seats")
    if isinstance(seats, list):
        new_seats = []
        for seat in seats:
            if not isinstance(seat, dict):
                new_seats.append(seat)
                continue
            s = dict(seat)
            for key in ("message", "chat", "lastMessage"):
                if key in s and s[key]:
                    cleaned, hits = strip_claimed_authorization_phrases(s[key])
                    if hits:
                        stripped.append(
                            {
                                "where": f"seat.{s.get('seatNumber')}.{key}",
                                "hits": hits,
                            }
                        )
                        s[key] = cleaned
            new_seats.append(s)
        out["seats"] = new_seats

    events = out.get("recentEvents")
    if isinstance(events, list):
        new_events = []
        for ev in events:
            if not isinstance(ev, dict):
                new_events.append(ev)
                continue
            e = dict(ev)
            for key in ("message", "text", "summary"):
                val = e.get(key)
                if isinstance(val, str) and val:
                    cleaned, hits = strip_claimed_authorization_phrases(val)
                    if hits:
                        stripped.append({"where": f"event.{key}", "hits": hits})
                        e[key] = cleaned
                elif isinstance(val, dict) and "message" in val:
                    sm = dict(val)
                    cleaned, hits = strip_claimed_authorization_phrases(
                        sm.get("message")
                    )
                    if hits:
                        stripped.append(
                            {"where": "event.summary.message", "hits": hits}
                        )
                        sm["message"] = cleaned
                        e[key] = sm
            new_events.append(e)
        out["recentEvents"] = new_events

    if stripped:
        out["_k176_claim_strip"] = {
            "schema": "devfun.claimed_auth_strip.v1",
            "count": len(stripped),
            "items": stripped,
            "isolation": "observation_is_data_not_authorization",
        }
    return out
