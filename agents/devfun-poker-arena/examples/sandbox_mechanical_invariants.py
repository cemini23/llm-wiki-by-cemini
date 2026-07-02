"""K140 mechanical invariants gate for sandbox decide() outputs.

AI-native games survey (arXiv 2607.00527) defines six invariants — goals, rules,
state, feedback, pacing, agency — that make open-ended agent outputs interpretable
and consequential. This module enforces the subset applicable to Poker Arena
static-agent bundle eval before tri-verifier axis scoring.

No external deps beyond stdlib.
"""
from __future__ import annotations

from typing import Any, Optional


def _norm_action(action: str) -> str:
    return action.lower().strip()


def _hero_seat_number(table: dict[str, Any]) -> Optional[int]:
    for key in ("selfSeatNumber", "heroSeatNumber", "heroSeat"):
        val = table.get(key)
        if val is not None:
            try:
                return int(val)
            except (TypeError, ValueError):
                continue
    return None


def _seat_has_stack(seat: dict[str, Any]) -> bool:
    stack = seat.get("stackChips")
    if stack is None:
        stack = seat.get("stack")
    if stack is None:
        return False
    try:
        int(stack)
        return True
    except (TypeError, ValueError):
        return False


def _non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def verify_mechanical_invariants(
    table: Optional[dict[str, Any]],
    action: str,
    allowed_actions: list[str],
    action_payload: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Verify K140 mechanical invariants before strategic axis scoring.

    Checks:
      - agency: action is in allowed_actions
      - state: table has seats, pot, and per-seat stacks
      - rules: allowedActions block present on table
      - feedback: non-empty reasoning when payload includes a reasoning field
      - goals (proxy): hero seat identifiable via selfSeatNumber / heroSeat*

    Returns:
        Dict with pass (bool), hazards (list[str]), and details (dict).
    """
    hazards: list[str] = []
    details: dict[str, Any] = {
        "action": action,
        "checks": {},
    }
    payload = action_payload or {}

    # --- agency ---
    agency_ok = True
    if not allowed_actions:
        agency_ok = False
        hazards.append("invariant:agency_violation")
        details["checks"]["agency"] = {"pass": False, "reason": "empty_allowed_actions"}
    else:
        norm_action = _norm_action(action)
        norm_allowed = [_norm_action(a) for a in allowed_actions]
        if norm_action not in norm_allowed:
            agency_ok = False
            hazards.append("invariant:agency_violation")
            details["checks"]["agency"] = {
                "pass": False,
                "action": action,
                "allowed": allowed_actions,
            }
        else:
            details["checks"]["agency"] = {"pass": True, "action": action}

    # --- state ---
    state_ok = True
    if not isinstance(table, dict):
        state_ok = False
        hazards.append("invariant:missing_state")
        details["checks"]["state"] = {"pass": False, "reason": "table_missing_or_not_dict"}
    else:
        seats = table.get("seats")
        if not isinstance(seats, list) or not seats:
            state_ok = False
            hazards.append("invariant:missing_state")
            details["checks"]["state"] = {"pass": False, "reason": "missing_or_empty_seats"}
        else:
            pot = table.get("potChips")
            if pot is None:
                pot = table.get("pot")
            if pot is None:
                state_ok = False
                hazards.append("invariant:missing_state")
                details["checks"]["state"] = {
                    "pass": False,
                    "reason": "missing_pot",
                    "seat_count": len(seats),
                }
            elif not all(isinstance(s, dict) and _seat_has_stack(s) for s in seats):
                state_ok = False
                hazards.append("invariant:missing_state")
                details["checks"]["state"] = {
                    "pass": False,
                    "reason": "missing_seat_stacks",
                    "seat_count": len(seats),
                }
            else:
                details["checks"]["state"] = {
                    "pass": True,
                    "seat_count": len(seats),
                    "potChips": pot,
                }

    # --- rules ---
    rules_ok = True
    if not isinstance(table, dict):
        rules_ok = False
        hazards.append("invariant:missing_rules")
        details["checks"]["rules"] = {"pass": False, "reason": "table_missing_or_not_dict"}
    else:
        allowed_block = table.get("allowedActions")
        if not isinstance(allowed_block, dict) or not allowed_block:
            rules_ok = False
            hazards.append("invariant:missing_rules")
            details["checks"]["rules"] = {"pass": False, "reason": "missing_allowed_actions_block"}
        else:
            available = allowed_block.get("availableActions")
            details["checks"]["rules"] = {
                "pass": True,
                "availableActions": available,
            }

    # --- feedback ---
    feedback_ok = True
    reasoning_fields = ("reasoning", "reasoning_text")
    present_fields = [f for f in reasoning_fields if f in payload]
    if present_fields:
        empty_fields = [f for f in present_fields if not _non_empty_text(payload.get(f))]
        if empty_fields:
            feedback_ok = False
            hazards.append("invariant:empty_reasoning")
            details["checks"]["feedback"] = {
                "pass": False,
                "empty_fields": empty_fields,
            }
        else:
            details["checks"]["feedback"] = {"pass": True, "fields": present_fields}
    else:
        details["checks"]["feedback"] = {"pass": True, "skipped": "no_reasoning_fields"}

    # --- goals proxy (hero seat identifiable) ---
    goals_ok = True
    if not isinstance(table, dict):
        goals_ok = False
        hazards.append("invariant:missing_hero")
        details["checks"]["goals"] = {"pass": False, "reason": "table_missing_or_not_dict"}
    else:
        hero_seat = _hero_seat_number(table)
        if hero_seat is None:
            goals_ok = False
            hazards.append("invariant:missing_hero")
            details["checks"]["goals"] = {"pass": False, "reason": "hero_seat_not_identifiable"}
        else:
            seats = table.get("seats") or []
            hero_row = next(
                (s for s in seats if isinstance(s, dict) and s.get("seatNumber") == hero_seat),
                None,
            )
            if hero_row is None:
                goals_ok = False
                hazards.append("invariant:missing_hero")
                details["checks"]["goals"] = {
                    "pass": False,
                    "reason": "hero_seat_not_in_seats",
                    "heroSeatNumber": hero_seat,
                }
            else:
                details["checks"]["goals"] = {
                    "pass": True,
                    "heroSeatNumber": hero_seat,
                }

    all_pass = agency_ok and state_ok and rules_ok and feedback_ok and goals_ok

    # Primary hazard for dimension consumers expecting a single hazard key
    primary_hazard = hazards[0] if hazards else None

    return {
        "pass": all_pass,
        "hazard": primary_hazard,
        "hazards": hazards,
        "details": details,
    }
