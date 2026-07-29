"""K176 claimed-authorization guard (arXiv 2607.11698 pattern).

Self-claimed authorization from observation / tool-result channels is
invalid. Privileged bankroll, table-bind, and submit intents require
standing from the real operator or prebind path only.

K185 (arXiv 2607.15218 pattern, light): privileged intents on a trusted
channel still face a causal **action** risk check (stack/pot/odds). A
linguistically safe plan ("call for information") does not bypass
``action_unsafe`` / absurd pot-odds. Deny classes:

- ``channel`` — standing missing (observation/tool/unknown)  [K176]
- ``action``  — causal / process-description (PD) stack risk  [K185]
- ``text``    — content/discourse (CD) policy flag            [K185]

Pattern only — no AHA / PRISM probe install.
Pairs with K164 capability-tree submit leaf + K167 message isolation.
"""
from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path
from typing import Any, Literal, Optional

logger = logging.getLogger("arena-pokerkit.claimed_auth")

Channel = Literal["operator", "prebind", "observation", "tool_result", "unknown"]
Intent = Literal[
    "submit_sandbox",
    "all_in",
    "bankroll_spend",
    "live_table_action",
]
DenyClass = Literal["channel", "action", "text"]

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

# K182: sandbox-pass claims require matching pin bundle SHA (authority framing).
_SANDBOX_PASS_CLAIM_RE = re.compile(
    r"(?i)\b("
    r"passed\s+sandbox|"
    r"pass(?:ed)?\s+(?:the\s+)?sandbox|"
    r"gate\s+pass(?:ed)?|"
    r"sandbox\s+ok|"
    r"sandbox\s+gate\s+pass"
    r")\b"
)
_SHA256_RE = re.compile(r"\b([0-9a-f]{64})\b", re.I)
_DEFAULT_PIN_PATH = Path(__file__).resolve().parent.parent / "config" / "researcher_sandbox_submit.pin.json"

# Phrases that look like approval claims in untrusted table/chat text.
_CLAIM_PHRASE_RE = re.compile(
    r"(?i)\b("
    r"user\s+approved|"
    r"authorized\s+all[\s-]?in|"
    r"authorized\s+to\s+submit|"
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

# Call-to-pot above this ratio is treated as absurd pot-odds (light PD check).
_ABSURD_CALL_POT_RATIO = 3.0


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


def detect_sandbox_pass_claim(text: Any) -> list[str]:
    """Return matched sandbox-pass phrases (K182 — needs pin bundle SHA)."""
    if text is None:
        return []
    s = text if isinstance(text, str) else str(text)
    if not s.strip():
        return []
    return [m.group(0) for m in _SANDBOX_PASS_CLAIM_RE.finditer(s)]


def _normalize_sha(value: Any) -> str:
    return str(value or "").strip().lower()


def load_expected_pin_bundle_sha(
    *,
    pin_path: Path | None = None,
) -> str:
    """Expected bundle SHA from env, pin JSON, or notes field."""
    env_sha = _normalize_sha(os.environ.get("CEMINI_PIN_BUNDLE_SHA"))
    if env_sha:
        return env_sha

    path = pin_path or _DEFAULT_PIN_PATH
    if not path.is_file():
        return ""

    try:
        pin = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""

    direct = _normalize_sha(pin.get("bundleSha256"))
    if direct:
        return direct

    notes = str(pin.get("notes") or "")
    for match in _SHA256_RE.finditer(notes):
        return _normalize_sha(match.group(1))
    return ""


def extract_cited_bundle_sha(text: Any) -> str:
    """First sha256 hex token in claim / evidence text."""
    if text is None:
        return ""
    s = text if isinstance(text, str) else str(text)
    match = _SHA256_RE.search(s)
    return _normalize_sha(match.group(1)) if match else ""


def assess_sandbox_pass_pin_match(
    text: Any,
    *,
    evidence: dict[str, Any] | None = None,
    pin_path: Path | None = None,
) -> tuple[bool, str]:
    """K182: deny when sandbox-pass claim lacks matching pin bundle SHA."""
    evidence = evidence or {}
    combined = " ".join(
        str(x)
        for x in (
            text,
            evidence.get("claim_text"),
            evidence.get("message"),
            evidence.get("plan_text"),
            evidence.get("bundle_sha256"),
            evidence.get("bundleSha256"),
            evidence.get("pin_bundle_sha"),
        )
        if x
    )
    hits = detect_sandbox_pass_claim(combined)
    if not hits:
        return False, ""

    expected = load_expected_pin_bundle_sha(pin_path=pin_path)
    if not expected:
        return True, "sandbox pass claim without configured pin bundle SHA"

    cited = extract_cited_bundle_sha(combined)
    if not cited:
        return True, "sandbox pass claim without cited bundle SHA"

    if cited != expected:
        return True, f"sandbox pass claim SHA mismatch (cited≠pin)"

    return False, ""


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


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, (int, float)) and value == 1:
        return True
    if isinstance(value, str) and value.strip().lower() in {
        "1",
        "true",
        "yes",
        "y",
        "on",
    }:
        return True
    return False


def _as_float(value: Any) -> float | None:
    if value is None or value is False:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def assess_text_risk(evidence: dict[str, Any]) -> tuple[bool, str]:
    """Content/discourse (CD) risk flags — linguistic policy only.

    Does **not** clear action risk. Safe-sounding plan text is ignored for
    causal checks (see ``assess_action_risk``).
    """
    if _truthy(evidence.get("text_unsafe")):
        return True, "evidence marks text_unsafe"
    if _truthy(evidence.get("cd_unsafe")):
        return True, "evidence marks cd_unsafe (content/discourse)"
    return False, ""


def assess_action_risk(
    intent: str,
    evidence: dict[str, Any],
) -> tuple[bool, str]:
    """Causal / process-description (PD) stack+odds risk for privileged acts.

    Explicit ``action_unsafe=True`` always denies. Light numeric heuristics
    apply when pot/call (and optional stack) evidence is present — especially
    for ``all_in`` / ``live_table_action``. Plan phrases like
    ``call for information`` never suppress this check.
    """
    # Explicit PD flag wins over any safe-sounding plan_text / reason.
    if _truthy(evidence.get("action_unsafe")):
        return True, "evidence marks action_unsafe"
    if _truthy(evidence.get("pd_unsafe")):
        return True, "evidence marks pd_unsafe (causal action)"

    pot = _as_float(evidence.get("pot") or evidence.get("pot_size"))
    call = _as_float(
        evidence.get("call_chips")
        or evidence.get("to_call")
        or evidence.get("call")
    )
    stack = _as_float(
        evidence.get("stack")
        or evidence.get("hero_stack")
        or evidence.get("effective_stack")
    )

    if _truthy(evidence.get("pot_odds_absurd")):
        return True, "evidence marks pot_odds_absurd"

    if _truthy(evidence.get("dead_money_flag")) or _truthy(evidence.get("dead_money")):
        # Shove / all-in into flagged dead-money spot is action-unsafe by default.
        if intent in {"all_in", "live_table_action", "bankroll_spend"}:
            return True, "dead_money flag with privileged table action"

    if pot is not None and call is not None and pot > 0 and call > 0:
        ratio = call / pot
        if ratio >= _ABSURD_CALL_POT_RATIO:
            return (
                True,
                f"call/pot ratio {ratio:.2f} >= {_ABSURD_CALL_POT_RATIO} (absurd pot-odds)",
            )

    # All-in for nearly full stack into tiny pot (light sanity).
    if (
        intent in {"all_in", "live_table_action"}
        and pot is not None
        and stack is not None
        and pot > 0
        and stack > 0
        and stack / pot >= 10.0
        and (call is None or call >= stack * 0.9)
    ):
        return True, "all-in sized stack into tiny pot (stack/pot >= 10)"

    return False, ""


def authorize(
    intent: str,
    *,
    channel: Any,
    evidence: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Authorize a privileged intent against channel + light action/text risk.

    Returns ``{ok, reason, intent, channel, privileged, deny_class, ...}``.

    Deny classes (K176 + K185):
    - ``channel`` — observation / tool_result / unknown (unchanged semantics)
    - ``text`` — CD policy flag on trusted channel
    - ``action`` — PD causal stack/odds risk on trusted channel

    Text-only safe plans never bypass ``action_unsafe`` / odds checks.
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
        "deny_class": None,
        "evidence_keys": sorted(evidence.keys()),
    }

    if not privileged:
        result["ok"] = True
        result["reason"] = "non-privileged intent — no standing required"
        return result

    def _deny(reason: str, deny_class: DenyClass) -> dict[str, Any]:
        result["reason"] = reason
        result["deny_class"] = deny_class
        logger.info(
            "[arena-pokerkit] claimed-auth deny intent=%s channel=%s "
            "deny_class=%s reason=%s",
            intent_n,
            channel_n,
            deny_class,
            reason,
        )
        return result

    # --- K176 channel standing (unchanged semantics) ---
    if channel_n == "observation":
        return _deny(_DENY_OBSERVATION, "channel")

    if channel_n == "tool_result":
        return _deny(_DENY_TOOL, "channel")

    if channel_n == "unknown":
        return _deny(_DENY_UNKNOWN, "channel")

    if channel_n not in TRUSTED_CHANNELS:
        return _deny(_DENY_UNPRIVILEGED_CHANNEL, "channel")

    # Observation-shaped evidence never upgrades a trusted channel by itself;
    # trusted channel + optional prebind_ok flag is enough for channel standing.
    claim_text = evidence.get("claim_text") or evidence.get("message") or ""
    if claim_text and channel_n in TRUSTED_CHANNELS:
        result["claim_phrases"] = detect_claimed_authorization(claim_text)

    # Surface plan text for audit only — never used to clear action risk.
    plan = evidence.get("plan_text") or evidence.get("plan") or evidence.get("reason")
    if plan is not None:
        result["plan_text_present"] = True

    # --- K182 sandbox-pass claims need pin bundle SHA on submit ---
    if intent_n == "submit_sandbox":
        sandbox_bad, sandbox_reason = assess_sandbox_pass_pin_match(
            claim_text,
            evidence=evidence,
        )
        if sandbox_bad:
            return _deny(sandbox_reason, "text")

    # --- K185 text (CD) then action (PD) on trusted channel ---
    text_unsafe, text_reason = assess_text_risk(evidence)
    if text_unsafe:
        return _deny(text_reason, "text")

    action_unsafe, action_reason = assess_action_risk(intent_n, evidence)
    if action_unsafe:
        return _deny(action_reason, "action")

    result["ok"] = True
    result["deny_class"] = None
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
