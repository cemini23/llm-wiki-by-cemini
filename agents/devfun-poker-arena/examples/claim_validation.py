"""K259 — MCP claim validation + parameter grounding (fail-open).

Light steal from CASCADE (bio OOD — pattern only, no install): when Arena
helpers surface solver/tool reports, catalog membership ("looks like a known
line") is not the same as validating the directional claim the agent will
repeat. Harden NL -> tool-arg grounding for seat/street/solver id: refuse or
skip ambiguous args, resolve informal names through server-side code alias
maps, never silent-default.

All functions are pure and never raise on bad input. Advisory only — not a
production gate.
"""
from __future__ import annotations

from typing import Any

MEMBERSHIP_SCHEMA = "devfun.membership.v1"
CLAIM_SCHEMA = "devfun.claim_validation.v1"
ARG_SCHEMA = "devfun.arg_grounding.v1"

_DIRECTIONAL_KEYS = (
    "suggested_action",
    "action",
    "direction",
    "line_direction",
    "dominant_action",
    "freq_action",
)

# Action / direction tokens -> canonical direction (hand-history notation).
_ACTION_ALIASES = {
    "fold": "fold",
    "folds": "fold",
    "f": "fold",
    "check": "check",
    "checks": "check",
    "x": "check",
    "call": "call",
    "calls": "call",
    "c": "call",
    "bet": "bet",
    "bets": "bet",
    "lead": "bet",
    "b": "bet",
    "raise": "raise",
    "raises": "raise",
    "r": "raise",
    "3b": "raise",
    "3-bet": "raise",
    "all-in": "raise",
    "allin": "raise",
    "shove": "raise",
    "mixed": "mixed",
}

# Server-side code alias maps — never trust raw model strings for these.
_STREET_ALIASES = {
    "preflop": "preflop",
    "pre-flop": "preflop",
    "pre": "preflop",
    "pf": "preflop",
    "flop": "flop",
    "turn": "turn",
    "river": "river",
}
# Ambiguous single-letter street tokens — clarify/refuse, never default.
_AMBIGUOUS_STREET = frozenset({"f", "t", "r"})

_SEAT_LABEL_ALIASES = {
    "btn": "button",
    "button": "button",
    "bu": "button",
    "sb": "small_blind",
    "small blind": "small_blind",
    "bb": "big_blind",
    "big blind": "big_blind",
    "utg": "utg",
    "utg1": "utg1",
    "utg2": "utg2",
    "ep": "ep",
    "lj": "lj",
    "hj": "hj",
    "mp": "mp",
    "mp1": "mp1",
    "mp2": "mp2",
    "co": "cutoff",
    "cutoff": "cutoff",
    "hero": "hero",
    "self": "hero",
}

_SOLVER_ID_ALIASES = {
    "static": "static_chart",
    "static_chart": "static_chart",
    "static chart": "static_chart",
    "chart": "static_chart",
    "mafp": "mafp",
    "texas": "texassolver",
    "texas solver": "texassolver",
    "texassolver": "texassolver",
    "pokerskill": "pokerskill",
    "poker skill": "pokerskill",
    "poker-skills": "pokerskill",
    "postflop buckets": "postflop_buckets",
    "postflop_buckets": "postflop_buckets",
    "buckets": "postflop_buckets",
}


# ---------------------------------------------------------------------------
# 1. Catalog membership vs directional claim validation
# ---------------------------------------------------------------------------


def membership_match(line: Any, catalog: Any) -> dict[str, Any]:
    """Classify a report/line against a known catalog (membership only).

    ``membership="match"`` means "looks like a known line / report shape" —
    it never authorizes repeating the directional claim.
    """
    result: dict[str, Any] = {
        "schema": MEMBERSHIP_SCHEMA,
        "membership": "unknown",
        "reason": "no_input",
    }
    token = _line_token(line)
    if token is None:
        result["reason"] = "unparsable"
        return result
    try:
        known = {str(c).strip().lower() for c in catalog if c is not None}
    except Exception:
        result["reason"] = "catalog_unparsable"
        return result
    if token in known:
        result["membership"] = "match"
        result["reason"] = "catalog_hit"
    else:
        result["membership"] = "no_match"
        result["reason"] = "not_in_catalog"
    return result


def validate_directional_claim(claim: Any, report: Any) -> dict[str, Any]:
    """Validate the directional assertion (action/line direction) vs evidence.

    ``repeat_ok`` is True only when ``claim_status == "validated"`` — i.e.
    claim direction agrees with an independent directional field on the
    report. Missing/malformed evidence -> ``unvalidated``/``skipped``, never
    a crash.
    """
    result: dict[str, Any] = {
        "schema": CLAIM_SCHEMA,
        "membership": "unknown",
        "claim_status": "skipped",
        "direction": None,
        "reason": "no_claim",
        "repeat_ok": False,
    }
    if not isinstance(claim, dict) or not isinstance(report, dict):
        result["reason"] = "invalid_input"
        return result
    if _has_directional_shape(report):
        result["membership"] = "match"
    claim_dir = _claim_direction(claim)
    if claim_dir is None:
        result["claim_status"] = "skipped"
        result["reason"] = "no_claim_direction"
        return result
    result["direction"] = claim_dir
    report_dir, has_dir = _report_direction(report)
    if not has_dir:
        result["claim_status"] = "unvalidated"
        result["reason"] = "no_independent_evidence"
        return result
    if report_dir == claim_dir:
        result["claim_status"] = "validated"
        result["repeat_ok"] = True
        result["reason"] = "direction_agrees"
    else:
        result["claim_status"] = "conflict"
        result["reason"] = f"direction_conflict:{claim_dir}!={report_dir}"
    return result


# ---------------------------------------------------------------------------
# 2. Ambiguous tool args — clarify/refuse, no silent defaults
# ---------------------------------------------------------------------------


def ground_tool_args(raw: Any) -> dict[str, Any]:
    """Ground NL seat/street/solver-id args via code alias maps.

    Refuses unknown tokens, clarifies ambiguous short forms and seat labels
    that need a table layout. Never invents defaults (no seat 1 / preflop /
    static_chart).
    """
    result: dict[str, Any] = {
        "schema": ARG_SCHEMA,
        "ok": False,
        "seat": None,
        "seat_label": None,
        "street": None,
        "solver_id": None,
        "ambiguous": [],
        "action": "refuse",
    }
    if not isinstance(raw, dict):
        result["reason"] = "invalid_input"
        return result
    ambiguous: list[str] = []
    notes: list[str] = []
    refused = False

    street = raw.get("street")
    if street is not None and street != "":
        resolved = _resolve_street(street)
        if resolved is None:
            if str(street).strip().lower() in _AMBIGUOUS_STREET:
                ambiguous.append("street")
                notes.append("street_ambiguous")
            else:
                refused = True
                notes.append("street_unknown")
        else:
            result["street"] = resolved

    seat = raw.get("seat")
    if seat is not None and seat != "":
        seat_num, seat_label = _resolve_seat(seat)
        if seat_num is not None:
            result["seat"] = seat_num
        elif seat_label is not None:
            result["seat_label"] = seat_label
            ambiguous.append("seat")
            notes.append("seat_needs_layout")
        else:
            refused = True
            notes.append("seat_unknown")

    solver_id = raw.get("solver_id")
    if solver_id is not None and solver_id != "":
        resolved = _resolve_solver_id(solver_id)
        if resolved is None:
            refused = True
            notes.append("solver_unknown")
        else:
            result["solver_id"] = resolved

    result["ambiguous"] = list(ambiguous)
    if notes:
        result["reason"] = ";".join(notes)
    if refused:
        result["action"] = "refuse"
    elif ambiguous:
        result["action"] = "clarify"
    else:
        result["action"] = "accept"
        result["ok"] = True
    return result


# ---------------------------------------------------------------------------
# 3. Advisory tag for solver context (light wire target)
# ---------------------------------------------------------------------------


def tag_solver_context_claims(ctx: Any) -> Any:
    """Tag solver context with claim-validation / arg-grounding advisory.

    Fail-open: returns ctx unchanged when there's nothing to tag or input is
    malformed. Never raises, never blocks decide.
    """
    if not isinstance(ctx, dict):
        return ctx
    out = dict(ctx)
    tagged = False

    claim_src, claim = _find_claim(ctx)
    if claim is not None:
        ev_src, report = _find_evidence(ctx, exclude=claim_src)
        result = validate_directional_claim(claim, report)
        result["claim_source"] = claim_src
        result["evidence_source"] = ev_src
        if not ev_src:
            result["claim_status"] = "unvalidated"
            result["repeat_ok"] = False
            result["reason"] = "no_independent_evidence"
        out["claim_validation"] = result
        tagged = True
    elif _has_catalog_identity(ctx):
        out["claim_validation"] = {
            "schema": CLAIM_SCHEMA,
            "membership": "match",
            "claim_status": "unvalidated",
            "direction": None,
            "reason": "membership_only",
            "repeat_ok": False,
        }
        tagged = True

    raw_args = ctx.get("tool_args")
    if isinstance(raw_args, dict) and raw_args:
        out["arg_grounding"] = ground_tool_args(raw_args)
        tagged = True

    return out if tagged else ctx


# ---------------------------------------------------------------------------
# Internal helpers (pure)
# ---------------------------------------------------------------------------


def _line_token(line: Any) -> str | None:
    if line is None:
        return None
    if isinstance(line, str):
        return line.strip().lower() or None
    if isinstance(line, dict):
        for key in ("line", "id", "name", "report_id", "tool"):
            val = line.get(key)
            if val is not None:
                token = str(val).strip().lower()
                return token or None
        return None
    token = str(line).strip().lower()
    return token or None


def _claim_direction(claim: dict[str, Any]) -> str | None:
    for key in ("action", "direction", "suggested_action"):
        if key in claim:
            return normalize_action(claim[key])
    return None


def _report_direction(report: dict[str, Any]) -> tuple[str | None, bool]:
    for key in _DIRECTIONAL_KEYS:
        if key in report:
            direction = normalize_action(report[key])
            if direction is not None:
                return direction, True
    return None, False


def _has_directional_shape(report: dict[str, Any]) -> bool:
    return any(key in report for key in _DIRECTIONAL_KEYS)


def normalize_action(token: Any) -> str | None:
    """Canonicalize an action/direction token (list -> mixed)."""
    if token is None:
        return None
    if isinstance(token, (list, tuple)):
        normed = {normalize_action(t) for t in token}
        normed.discard(None)
        if len(normed) > 1:
            return "mixed"
        return next(iter(normed), None)
    key = str(token).strip().lower()
    if not key:
        return None
    return _ACTION_ALIASES.get(key)


def _find_claim(ctx: dict[str, Any]) -> tuple[str | None, dict[str, Any] | None]:
    chart = ctx.get("preflop_chart")
    if isinstance(chart, dict) and chart.get("suggested_action"):
        return "preflop_chart", {"action": chart["suggested_action"]}
    if ctx.get("suggested_action") is not None:
        return "suggested_action", {"action": ctx["suggested_action"]}
    if ctx.get("direction") is not None:
        return "direction", {"direction": ctx["direction"]}
    claim = ctx.get("claim")
    if isinstance(claim, dict) and claim:
        return "claim", dict(claim)
    return None, None


def _find_evidence(
    ctx: dict[str, Any], exclude: str | None
) -> tuple[str | None, dict[str, Any]]:
    candidates: list[tuple[str, dict[str, Any]]] = []
    if exclude != "solver_frequencies":
        sf = ctx.get("solver_frequencies")
        if isinstance(sf, dict):
            candidates.append(("solver_frequencies", sf))
    if exclude != "pokerskill":
        ps = ctx.get("pokerskill")
        if isinstance(ps, dict):
            candidates.append(("pokerskill", ps))
    for name, frag in candidates:
        if _first_directional(frag) is not None:
            return name, {
                key: val for key, val in frag.items() if key in _DIRECTIONAL_KEYS
            }
    top = {
        key: val
        for key, val in ctx.items()
        if key not in ("preflop_chart", "claim") and key != exclude
    }
    if _first_directional(top) is not None:
        return "top_level", {
            key: val for key, val in top.items() if key in _DIRECTIONAL_KEYS
        }
    return None, {}


def _first_directional(frag: dict[str, Any]) -> Any:
    for key in _DIRECTIONAL_KEYS:
        if key in frag and frag[key] is not None:
            return frag[key]
    return None


def _has_catalog_identity(ctx: dict[str, Any]) -> bool:
    return any(key in ctx for key in ("preflop_chart", "solver_frequencies", "pokerskill"))


def _resolve_street(token: Any) -> str | None:
    key = str(token).strip().lower()
    if key in _AMBIGUOUS_STREET:
        return None
    return _STREET_ALIASES.get(key)


def _resolve_seat(token: Any) -> tuple[int | None, str | None]:
    key = str(token).strip().lower()
    if key.isdigit():
        return int(key), None
    cleaned = key.removeprefix("seat").strip()
    if cleaned.isdigit():
        return int(cleaned), None
    label = _SEAT_LABEL_ALIASES.get(key)
    if label is not None:
        return None, label
    return None, None


def _resolve_solver_id(token: Any) -> str | None:
    return _SOLVER_ID_ALIASES.get(str(token).strip().lower())
