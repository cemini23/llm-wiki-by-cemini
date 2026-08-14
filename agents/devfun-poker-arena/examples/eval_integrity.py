"""Eval integrity (CCC K277 + light K280 + light K281, arXiv methodology only).

Dual-ID:
- CCC K277 = Labels ≠ endpoints / measurement integrity (2608.12880)  <- this module
- CCC K278 = InterSAGE (2608.13030)                                  -- SKIP poker
- CCC K279 = MARC-v1 (2608.13476)                                    -- SKIP poker (clinical OOD)
- CCC K280 = Vero (2608.13522)                                       <- this module (light joint outcome+verification)
- CCC K281 = AutoDesign (2608.13560)                                 <- this module (light external/HITL pass criteria)
- Cybersec K277 = RSM (2608.12311)                                   -> examples/helper_roles.py (already wired)
- Cybersec K278 = ATOBench (2608.12996)                              -> examples/verification_chain.py

Treatment-blind grading + labels ≠ endpoints. A label ("win", "attack",
"qualified") is **not** a behavioral endpoint: bind the five Integrity Chain
links before interpreting a label. Scope honesty: campaign counts are not
population EV / model-ranking claims.

Do **NOT** clone Vero, MARC-v1, AutoDesign, InterSAGE, or download their
repos. Offline, pure helpers only — no network, no runtime decide() wire.
Paper metrics ≠ poker chip EV.
"""
from __future__ import annotations

from typing import Any

TREATMENT_KEYS: frozenset[str] = frozenset(
    {
        "treatment",
        "treatment_id",
        "arm",
        "condition",
        "label_source",
        "is_attack",
        "is_treatment",
        "baseline_vs_changed",
        "native_vs_ato",
    }
)

ENDPOINT_FIELDS: tuple[str, ...] = (
    "treatment_bytes",
    "executed_behavior",
    "authorization",
    "outcome_rule",
    "analysis_unit",
)

# Fields that accept a non-empty collection as well as a non-empty string.
_COLLECTION_OK: frozenset[str] = frozenset({"treatment_bytes", "executed_behavior"})

_EXTERNAL_OWNERS: frozenset[str] = frozenset({"hitl", "external"})
_CLOSED_LOOP_OWNERS: frozenset[str] = frozenset({"harness", "self", "optimizer"})

_SELF_REPORT_STRINGS: frozenset[str] = frozenset({"yes", "self-report", "self report"})


def _nonempty_endpoint_value(field: str, val: Any) -> bool:
    if field in _COLLECTION_OK:
        if isinstance(val, str):
            return val.strip() != ""
        if isinstance(val, (list, tuple, set, frozenset, dict)):
            return len(val) > 0
        return False
    return isinstance(val, str) and val.strip() != ""


def _has_treatment_key(obj: Any) -> bool:
    """Recursive scan for any TREATMENT_KEYS key, at any depth (fail-closed)."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in TREATMENT_KEYS:
                return True
            if _has_treatment_key(value):
                return True
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            if _has_treatment_key(item):
                return True
    return False


def strip_treatment(record: dict[str, Any]) -> dict[str, Any]:
    """Shallow copy without TREATMENT_KEYS; nested ``grader_input`` also stripped.

    Does not mutate the original. Garbage input -> ``{}`` (fail-open).
    """
    if not isinstance(record, dict):
        return {}
    out = {k: v for k, v in record.items() if k not in TREATMENT_KEYS}
    grader_input = out.get("grader_input")
    if isinstance(grader_input, dict):
        out["grader_input"] = {
            k: v for k, v in grader_input.items() if k not in TREATMENT_KEYS
        }
    return out


def bind_endpoint(record: dict[str, Any]) -> dict[str, Any]:
    """Bind the five Integrity Chain links before interpreting a label.

    ``{ok, missing, bound}``. ``ok`` is True only when all five
    ``ENDPOINT_FIELDS`` are present as non-empty strings (or non-empty
    collections for ``treatment_bytes`` / ``executed_behavior``). A record
    that only has ``label`` is not ok.
    """
    if not isinstance(record, dict):
        record = {}
    missing: list[str] = []
    bound: dict[str, Any] = {}
    for field in ENDPOINT_FIELDS:
        value = record.get(field)
        if _nonempty_endpoint_value(field, value):
            bound[field] = value
        else:
            missing.append(field)
    return {"ok": not missing, "missing": missing, "bound": bound}


def grade_treatment_blind(record: dict[str, Any], outcome_class: str) -> dict[str, Any]:
    """Grade treatment-blind: class assignment must not be gated on treatment keys.

    Builds the grader view via ``strip_treatment``; if any ``TREATMENT_KEYS``
    survive anywhere in the view, returns ``{ok: False, reason: "treatment_leak"}``
    (fail-closed). Otherwise ``{ok: True, grader_view, outcome_class}`` with
    ``outcome_class`` attached **after** the strip. Relabeling ``arm`` on an
    otherwise identical ``executed_behavior`` must not change ``grader_view``.
    """
    if not isinstance(record, dict):
        record = {}
    grader_view = strip_treatment(record)
    if _has_treatment_key(grader_view):
        return {"ok": False, "reason": "treatment_leak"}
    return {"ok": True, "grader_view": grader_view, "outcome_class": outcome_class}


def joint_score(
    outcome: Any,
    verification: Any,
    *,
    self_report: Any = None,
) -> dict[str, Any]:
    """K280 light — joint outcome + verification (self-report is not verification).

    ``{ok, outcome_ok, verification_ok, notes}``. ``ok`` is True only when
    both ``outcome`` and ``verification`` are truthy **and** ``verification``
    is not solely ``self_report``. Self-report = the string ``"yes"`` /
    ``"self-report"``, or the same object as ``self_report`` (identity).
    Outcome-only and verification-only are both not ok.
    """
    notes: list[str] = []
    outcome_ok = bool(outcome)

    is_self_report = False
    if verification is self_report and verification is not None:
        is_self_report = True
    if isinstance(verification, str):
        if verification.strip().lower() in _SELF_REPORT_STRINGS:
            is_self_report = True

    verification_ok = False
    if not outcome_ok:
        notes.append("no_outcome")
    if not verification:
        notes.append("no_verification")
    elif is_self_report:
        verification_ok = False
        notes.append("self-report is not verification")
    else:
        verification_ok = True

    return {
        "ok": outcome_ok and verification_ok,
        "outcome_ok": outcome_ok,
        "verification_ok": verification_ok,
        "notes": notes,
    }


def assert_external_pass_criteria(criteria: dict[str, Any]) -> dict[str, Any]:
    """K281 light — keep the pass bar external / HITL, no closed self-rewrite.

    ``{ok, reason}``. ``criteria["owner"]`` must be ``"hitl"`` or
    ``"external"``. Rejects ``"harness"`` / ``"self"`` / ``"optimizer"``
    (``reason: closed_loop``) and a missing owner (``reason: missing_owner``).
    If ``mutated_by`` equals ``scorer_id`` (same process rewriting its own
    pass bar), reject ``reason: self_rewrite``. Unknown owners fail-closed.
    """
    if not isinstance(criteria, dict):
        return {"ok": False, "reason": "missing_owner"}

    owner = criteria.get("owner")
    if owner is None or (isinstance(owner, str) and not owner.strip()):
        return {"ok": False, "reason": "missing_owner"}

    owner_n = str(owner).strip().lower()
    if owner_n in _CLOSED_LOOP_OWNERS:
        return {"ok": False, "reason": "closed_loop"}

    if owner_n not in _EXTERNAL_OWNERS:
        return {"ok": False, "reason": "closed_loop"}

    if "mutated_by" in criteria and "scorer_id" in criteria:
        if criteria["mutated_by"] == criteria["scorer_id"]:
            return {"ok": False, "reason": "self_rewrite"}

    return {"ok": True, "reason": "external_pass_criteria"}
