"""VAKRA eval-axis checklist (CCC K275, arXiv 2608.12282 methodology only).

Dual-ID:
- CCC K275 = VAKRA (2608.12282)                        <- this module
- CCC K274 = CDH (2608.12273)                          -> examples/skill_invocation_budget.py
- CCC K276 = RSM (2608.12311)                          -> examples/helper_roles.py
- CCC K277 = Labels ≠ endpoints (2608.12880)           -> examples/eval_integrity.py
- Cybersec K276 = withhold contract (2608.12292)       -> examples/withhold_contract.py
- Cybersec K277 = RSM (same 2608.12311)                -> examples/helper_roles.py
- Cybersec K278 = ATOBench (2608.12996)                -> examples/verification_chain.py

Do **NOT** clone IBM/vakra — the repo/dataset is CC-BY-NC-SA 4.0; HF dataset
is WATCH-only, never downloaded. This module is a local, offline checklist
that scores an eval record against the five VAKRA axes so a helper-eval claim
must state them explicitly. Paper metrics ≠ poker chip EV.

Axes:
- ``api_paradigm``         "endpoint" | "compositional"
- ``reasoning_hops``       int 2-5 (else flagged)
- ``multi_source``         bool
- ``nl_policy_constraint`` bool
- ``reexec_verified``      bool — re-execution verified, NOT self-report
  (a string like "yes" is invalid: the value must be a real bool)
"""
from __future__ import annotations

from typing import Any

AXES: tuple[str, ...] = (
    "api_paradigm",
    "reasoning_hops",
    "multi_source",
    "nl_policy_constraint",
    "reexec_verified",
)

API_PARADIGMS: frozenset[str] = frozenset({"endpoint", "compositional"})

HOPS_MIN = 2
HOPS_MAX = 5

# A complete helper-eval claim must include policy-constrained / unanswerable
# query coverage (at least one of the two lists non-empty).
_QUERY_KEYS: tuple[str, ...] = (
    "policy_constrained_queries",
    "unanswerable_queries",
)


def score_eval(record: dict[str, Any]) -> dict[str, Any]:
    """Score an eval record against the VAKRA axes.

    Returns ``{complete: bool, missing: [axis...], notes: [str...]}``.
    ``missing`` lists axes absent or invalid; ``complete`` is True only when
    every axis validates AND policy-constrained / unanswerable query coverage
    is present. Pure function — no network, no HF download.
    """
    record = dict(record or {})
    missing: list[str] = []
    notes: list[str] = []

    paradigm = record.get("api_paradigm")
    if not isinstance(paradigm, str) or paradigm not in API_PARADIGMS:
        missing.append("api_paradigm")
        notes.append("api_paradigm must be 'endpoint' or 'compositional'")

    hops = record.get("reasoning_hops")
    if isinstance(hops, bool) or not isinstance(hops, int):
        missing.append("reasoning_hops")
        notes.append("reasoning_hops must be an int")
    elif not (HOPS_MIN <= hops <= HOPS_MAX):
        missing.append("reasoning_hops")
        notes.append(
            f"reasoning_hops {hops} out of range {HOPS_MIN}-{HOPS_MAX}"
        )

    for axis in ("multi_source", "nl_policy_constraint", "reexec_verified"):
        value = record.get(axis)
        if not isinstance(value, bool):
            missing.append(axis)
            notes.append(
                f"{axis} must be a real bool (reexec_verified is "
                f"re-execution evidence, not self-report)"
            )

    has_queries = any(
        isinstance(record.get(key), list)
        and any(isinstance(q, str) and q.strip() for q in record.get(key) or [])
        for key in _QUERY_KEYS
    )
    if not has_queries:
        missing.append("policy_constrained_queries")
        notes.append(
            "policy-constrained / unanswerable queries must be present for "
            "a complete helper-eval claim"
        )

    return {"complete": not missing, "missing": missing, "notes": notes}
