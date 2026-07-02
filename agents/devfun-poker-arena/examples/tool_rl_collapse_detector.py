"""Tool-RL structural collapse detector for arena-tool bundle regression.

Detects format degeneration from pure RL on multi-step MCP loops (arXiv 2606.26027):
- **Polluted**: irrelevant control tokens / tool names leaking into reasoning
- **Collapsed**: empty, whitespace-only, or broken JSON-like tool stubs

Stdlib only — no external deps.
"""
from __future__ import annotations

import json
import re
from typing import Any

# Polluted: special/control tokens from RL-trained tool formats
_CONTROL_TOKEN_RE = re.compile(r"<\|[^|>]+\|>")

# Polluted: MCP tool identifiers that should not appear in player reasoning
_MCP_TOOL_NAMES = (
    "join_pve",
    "get_game_state",
    "submit_action",
    "get_session_status",
)

# Polluted: fenced tool/json blocks embedded in reasoning text
_FENCED_TOOL_BLOCK_RE = re.compile(
    r"```(?:json|tool|javascript)?\s*[\s\S]*?```",
    re.IGNORECASE,
)
_OPEN_FENCE_JSON_RE = re.compile(r"```json\b", re.IGNORECASE)

# Collapsed: broken JSON-like tool stubs (not arena YAML reasoning)
_TOOL_JSON_KEY_RE = re.compile(
    r'"(?:tool|tool_call|tool_calls|function|arguments|name)"\s*:',
    re.IGNORECASE,
)
_BROKEN_JSON_OBJECT_RE = re.compile(r"\{[^{}]*$", re.MULTILINE)


def _normalize_field(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def _collect_text_fields(action_payload: dict[str, Any]) -> dict[str, str]:
    return {
        "message": _normalize_field(action_payload.get("message")),
        "reasoning": _normalize_field(action_payload.get("reasoning")),
        "reasoning_text": _normalize_field(action_payload.get("reasoning_text")),
    }


def _is_whitespace_only(text: str) -> bool:
    return not text or not text.strip()


def _detect_control_tokens(text: str) -> list[str]:
    hazards: list[str] = []
    for match in _CONTROL_TOKEN_RE.finditer(text):
        token = match.group(0)
        hazards.append(f"polluted:control_token:{token}")
    return hazards


def _detect_mcp_tool_leakage(text: str) -> list[str]:
    hazards: list[str] = []
    lowered = text.lower()
    for tool_name in _MCP_TOOL_NAMES:
        if tool_name in lowered:
            hazards.append(f"polluted:mcp_tool_name:{tool_name}")
    return hazards


def _detect_fenced_tool_blocks(text: str) -> list[str]:
    hazards: list[str] = []
    if _FENCED_TOOL_BLOCK_RE.search(text):
        hazards.append("polluted:fenced_tool_block")
    elif _OPEN_FENCE_JSON_RE.search(text) and "```" not in text.split("```json", 1)[-1]:
        hazards.append("polluted:unclosed_json_fence")
    return hazards


def _looks_like_tool_json_stub(text: str) -> bool:
    stripped = text.strip()
    if not stripped.startswith("{"):
        return False
    if _TOOL_JSON_KEY_RE.search(stripped):
        return True
    # Heuristic: JSON object with "action" key but not arena YAML `{vr: ...}` style
    if stripped.startswith('{"action"') or stripped.startswith('{"tool"'):
        return True
    return False


def _detect_broken_json_stub(text: str) -> list[str]:
    hazards: list[str] = []
    stripped = text.strip()

    if stripped in ("{}", "[]", "null", '""'):
        hazards.append("collapsed:empty_json_structure")
        return hazards

    if not _looks_like_tool_json_stub(stripped):
        return hazards

    if _BROKEN_JSON_OBJECT_RE.search(stripped):
        hazards.append("collapsed:truncated_json_stub")
        return hazards

    try:
        json.loads(stripped)
    except json.JSONDecodeError:
        hazards.append("collapsed:invalid_json_stub")

    return hazards


def _detect_empty_or_whitespace(text: str) -> list[str]:
    if _is_whitespace_only(text):
        return ["collapsed:whitespace_only"]
    return []


def detect_collapse(text: str) -> dict[str, Any]:
    """Detect Tool-RL structural collapse in free-form text.

    Returns:
        Dict with keys ``mode`` (``ok`` | ``polluted`` | ``collapsed``),
        ``hazards`` (list of hazard codes), and ``details`` (diagnostics).
    """
    hazards: list[str] = []
    details: dict[str, Any] = {"text_len": len(text or "")}

    if text is None:
        text = ""

    hazards.extend(_detect_empty_or_whitespace(text))
    if not hazards:
        hazards.extend(_detect_broken_json_stub(text))
    hazards.extend(_detect_control_tokens(text))
    hazards.extend(_detect_mcp_tool_leakage(text))
    hazards.extend(_detect_fenced_tool_blocks(text))

    collapsed = [h for h in hazards if h.startswith("collapsed:")]
    polluted = [h for h in hazards if h.startswith("polluted:")]

    if collapsed:
        mode = "collapsed"
    elif polluted:
        mode = "polluted"
    else:
        mode = "ok"

    details["collapsed_count"] = len(collapsed)
    details["polluted_count"] = len(polluted)
    if hazards:
        details["sample"] = text.strip()[:120]

    return {"mode": mode, "hazards": hazards, "details": details}


def verify_action_payload_collapse(action_payload: dict[str, Any]) -> dict[str, Any]:
    """Check message, reasoning, and reasoning_text for collapse modes.

    Scans each non-empty field and the combined blob. Empty optional fields
    (e.g. missing ``reasoning`` when ``reasoning_text`` is present) do not
    trigger collapse on their own.
    """
    fields = _collect_text_fields(action_payload or {})
    combined = " ".join(value.strip() for value in fields.values() if value.strip())

    per_field: dict[str, dict[str, Any]] = {}
    all_hazards: list[str] = []

    if not combined:
        return {
            "mode": "collapsed",
            "hazards": ["combined:collapsed:whitespace_only"],
            "details": {
                "fields": {name: detect_collapse(value) for name, value in fields.items()},
                "combined": detect_collapse(""),
                "field_presence": {name: bool(value.strip()) for name, value in fields.items()},
            },
        }

    for name, value in fields.items():
        if not value.strip():
            continue
        result = detect_collapse(value)
        per_field[name] = result
        for hazard in result["hazards"]:
            if hazard == "collapsed:whitespace_only":
                continue
            tagged = f"{name}:{hazard}"
            if tagged not in all_hazards:
                all_hazards.append(tagged)

    combined_result = detect_collapse(combined)
    per_field["combined"] = combined_result
    for hazard in combined_result["hazards"]:
        tagged = f"combined:{hazard}"
        if tagged not in all_hazards:
            all_hazards.append(tagged)

    collapsed = [h for h in all_hazards if ":collapsed:" in h]
    polluted = [h for h in all_hazards if ":polluted:" in h]

    if collapsed:
        mode = "collapsed"
    elif polluted:
        mode = "polluted"
    else:
        mode = "ok"

    details: dict[str, Any] = {
        "fields": per_field,
        "combined": combined_result,
        "field_presence": {name: bool(value.strip()) for name, value in fields.items()},
    }

    return {"mode": mode, "hazards": all_hazards, "details": details}
