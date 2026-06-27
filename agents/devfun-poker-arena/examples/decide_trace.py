"""Relaxed DecideTrace schema stub for poker decision traces.

This module stays dependency-free on purpose. The JSON Schema lives in
references/ for documentation and downstream consumers, while validation here
uses straightforward Python checks.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

ALLOWED_STREETS = frozenset({"preflop", "flop", "turn", "river", "showdown"})
ALLOWED_ACTION_CLASSES = frozenset({"fold", "check", "call", "bet", "raise", "all-in"})

_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "references" / "relaxed_decide_trace_schema.json"
RELAXED_DECIDE_TRACE_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))


@dataclass(slots=True)
class DecideTrace:
    street: str
    action_class: str
    sizing_intent: str | None = None
    rationale: str | None = None
    hero_stack: int | None = None
    villain_stack: int | None = None
    pot: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _require_non_empty_string(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _normalize_optional_string(name: str, value: Any) -> str | None:
    if value is None:
        return None
    return _require_non_empty_string(name, value)


def _normalize_optional_non_negative_int(name: str, value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer when provided")
    return value


def validate_decide_trace(trace: DecideTrace | Mapping[str, Any]) -> DecideTrace:
    """Validate a relaxed DecideTrace payload and return a normalized dataclass."""
    if isinstance(trace, DecideTrace):
        raw = trace.to_dict()
    elif isinstance(trace, Mapping):
        raw = dict(trace)
    else:
        raise TypeError("trace must be a DecideTrace or mapping")

    street = _require_non_empty_string("street", raw.get("street")).lower()
    if street not in ALLOWED_STREETS:
        allowed = ", ".join(sorted(ALLOWED_STREETS))
        raise ValueError(f"street must be one of: {allowed}")

    action_class = _require_non_empty_string("action_class", raw.get("action_class")).lower()
    if action_class not in ALLOWED_ACTION_CLASSES:
        allowed = ", ".join(sorted(ALLOWED_ACTION_CLASSES))
        raise ValueError(f"action_class must be one of: {allowed}")

    return DecideTrace(
        street=street,
        action_class=action_class,
        sizing_intent=_normalize_optional_string("sizing_intent", raw.get("sizing_intent")),
        rationale=_normalize_optional_string("rationale", raw.get("rationale")),
        hero_stack=_normalize_optional_non_negative_int("hero_stack", raw.get("hero_stack")),
        villain_stack=_normalize_optional_non_negative_int("villain_stack", raw.get("villain_stack")),
        pot=_normalize_optional_non_negative_int("pot", raw.get("pot")),
    )
