"""RSM helper role map (CCC K276 / Cybersec K277, arXiv 2608.12311 pattern).

Dual-ID:
- CCC K276 = RSM (2608.12311)                          <- this module
- Cybersec K277 = RSM (same 2608.12311)                <- this module
- CCC K274 = CDH (2608.12273)                          -> examples/skill_invocation_budget.py
- CCC K275 = VAKRA (2608.12282)                        -> examples/vakra_eval_axes.py
- Cybersec K276 = withhold contract (2608.12292)       -> examples/withhold_contract.py

Explicit capability-matched roles for helper agents — role drift (one helper
silently absorbing another's job) is driven by absent boundaries + functional
overlap. Durable actions require the operator, or review + an operator
confirmation flag. ``negative_constraints_for`` returns the "must not"
strings for prompt hardening.

Pattern only — no RSM dataset install. Paper metrics ≠ poker EV.
"""
from __future__ import annotations

from typing import Any

ROLE_SPECS: dict[str, dict[str, Any]] = {
    "decide": {
        "domain": "table action",
        "may": "fold/call/raise/check",
        "must_not": ["edit `.env`", "restart systemd", "durable wiki"],
    },
    "lobby": {
        "domain": "join/queue/rebuy policy",
        "may": "join/pace/protect",
        "must_not": ["rewrite decide policy", "LIVE Discord"],
    },
    "export": {
        "domain": "telemetry",
        "may": "write jsonl under reports/exports",
        "must_not": ["change strategy knobs"],
    },
    "review": {
        "domain": "HITL / independent check",
        "may": "accept/reject durable patch",
        "must_not": ["execute table actions"],
    },
    "operator": {
        "domain": "human",
        "may": "all durable + LIVE with LIVE OK",
        "must_not": [],
    },
}

ROLES: frozenset[str] = frozenset(ROLE_SPECS)

# Actions that change durable state — operator, or review + operator
# confirmation flag.
DURABLE_ACTIONS: frozenset[str] = frozenset(
    {"write_wiki", "edit_env", "restart_lobby", "live_discord"}
)

_ROLE_MAY: dict[str, frozenset[str]] = {
    "decide": frozenset({"fold", "call", "raise", "check"}),
    "lobby": frozenset({"join", "pace", "protect", "rebuy"}),
    "export": frozenset({"write_export", "write_jsonl", "export_telemetry"}),
    "review": frozenset({"accept_patch", "reject_patch"}),
    "operator": frozenset(),
}

_ROLE_MUST_NOT_TOKENS: dict[str, frozenset[str]] = {
    "decide": DURABLE_ACTIONS,
    "lobby": frozenset({"change_strategy", "live_discord"}),
    "export": frozenset({"change_strategy"}),
    "review": frozenset({"fold", "call", "raise", "check", "table_action"}),
    "operator": frozenset(),
}

KNOWN_ACTIONS: frozenset[str] = (
    DURABLE_ACTIONS
    | frozenset().union(*_ROLE_MAY.values())
    | frozenset().union(*_ROLE_MUST_NOT_TOKENS.values())
)

_ACTION_ALIASES: dict[str, str] = {
    "edit.env": "edit_env",
    "edit .env": "edit_env",
    "env edit": "edit_env",
    "restart systemd": "restart_lobby",
    "lobby restart": "restart_lobby",
    "wiki write": "write_wiki",
    "write wiki": "write_wiki",
    "durable wiki": "write_wiki",
    "live discord": "live_discord",
    "join table": "join",
    "queue": "join",
    "pace table": "pace",
    "protect": "protect",
    "write jsonl": "write_export",
    "export jsonl": "write_export",
    "telemetry": "write_export",
    "change strategy": "change_strategy",
    "strategy knobs": "change_strategy",
    "knobs": "change_strategy",
    "rewrite decide policy": "change_strategy",
    "accept patch": "accept_patch",
    "reject patch": "reject_patch",
    "accept": "accept_patch",
    "reject": "reject_patch",
    "table action": "table_action",
}

_ROLE_ALIASES: dict[str, str] = {
    "decider": "decide",
    "decision": "decide",
    "exporter": "export",
    "reviewer": "review",
    "human": "operator",
    "op": "operator",
    "user": "operator",
}


def normalize_role(role: Any) -> str:
    if role is None:
        return ""
    r = str(role).strip().lower().replace("-", "_")
    return _ROLE_ALIASES.get(r, r)


def normalize_action(action: Any) -> str:
    if action is None:
        return ""
    a = str(action).strip().lower()
    a = a.replace("-", "_")
    return _ACTION_ALIASES.get(a, a)


def assert_role(
    role: Any,
    action: Any,
    operator_confirmed: bool = False,
    live_ok: bool = False,
) -> dict[str, Any]:
    """Assert a helper role may take an action. Returns ``{ok, reason}``.

    Durable actions (``write_wiki``, ``edit_env``, ``restart_lobby``,
    ``live_discord``) require ``operator`` — or ``review`` with
    ``operator_confirmed=True``, except ``live_discord`` which is
    operator-only and additionally requires ``live_ok`` (LIVE OK).

    Unknown roles/actions fail-closed (``unknown_role`` / ``unknown_action``).
    """
    role_n = normalize_role(role)
    action_n = normalize_action(action)

    result: dict[str, Any] = {
        "ok": False,
        "reason": "",
        "role": role_n,
        "action": action_n,
        "domain": ROLE_SPECS.get(role_n, {}).get("domain", ""),
    }

    if role_n not in ROLES:
        result["reason"] = f"unknown_role: {role!r}"
        return result
    if not action_n:
        result["reason"] = "unknown_action: empty action"
        return result
    if action_n not in KNOWN_ACTIONS:
        result["reason"] = f"unknown_action: {action!r}"
        return result

    def _deny(reason: str) -> dict[str, Any]:
        result["reason"] = reason
        return result

    # LIVE Discord is operator-only and needs LIVE OK — review's
    # operator-confirmation flag does not extend to LIVE surfaces.
    if action_n == "live_discord":
        if role_n == "operator" and live_ok:
            result["ok"] = True
            result["reason"] = "operator + LIVE OK"
            return result
        return _deny("live_discord requires operator with LIVE OK")

    if action_n in DURABLE_ACTIONS:
        if role_n == "operator":
            result["ok"] = True
            result["reason"] = "operator"
            return result
        if role_n == "review" and operator_confirmed:
            result["ok"] = True
            result["reason"] = "review + operator confirmation"
            return result
        return _deny(
            f"{action_n} requires operator (or review + operator confirmation)"
        )

    if role_n == "operator":
        result["ok"] = True
        result["reason"] = "operator"
        return result

    if action_n in _ROLE_MUST_NOT_TOKENS[role_n]:
        return _deny(
            f"role {role_n} must not {action_n} "
            f"({'; '.join(ROLE_SPECS[role_n]['must_not'])})"
        )
    if action_n in _ROLE_MAY[role_n]:
        result["ok"] = True
        result["reason"] = f"in {role_n} scope"
        return result
    return _deny(f"action {action_n} outside {role_n} scope")


def negative_constraints_for(role: Any) -> list[str]:
    """"Must not" strings for injection into helper prompts (RSM hardening)."""
    role_n = normalize_role(role)
    return list(ROLE_SPECS.get(role_n, {}).get("must_not", []))
