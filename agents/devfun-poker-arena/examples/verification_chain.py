"""Verification-chain eval (Cybersec K278 ATOBench, arXiv 2608.12996 pattern only).

Dual-ID:
- Cybersec K278 = ATOBench (2608.12996)                           <- this module
- Cybersec K277 = RSM (2608.12311)                                -> examples/helper_roles.py (already wired)
- CCC K277 = Labels ≠ endpoints (2608.12880)                      -> examples/eval_integrity.py
- CCC K278 = InterSAGE (2608.13030)                               -- SKIP poker
- CCC K279 = MARC-v1 (2608.13476)                                 -- SKIP poker (clinical OOD)
- CCC K280 = Vero (2608.13522)                                    -> examples/eval_integrity.py (light)
- CCC K281 = AutoDesign (2608.13560)                              -> examples/eval_integrity.py (light)

Evaluate the **evidence path**, not the final chip/win outcome. Deceptive
observations (bluffs, injected noise, opponent messages) can keep an agent
busy after the evidence path has broken — activity ≠ verification.

ATOBench GitHub is a placeholder — do **NOT** clone. Authorized-lab / offline
traces only. No live-target applications. Paper metrics ≠ poker chip EV.
"""
from __future__ import annotations

from typing import Any


def _action_key(step: Any) -> Any:
    """Extract the comparable action identity from a trace step."""
    if isinstance(step, dict):
        return step.get("action", step.get("action_class"))
    return step


def attach_evidence(action: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    """Attach an evidence locator to an action (journal-style list-of-dicts).

    Returns a copy of ``action`` with ``evidence`` attached plus a sidecar
    ``_evidence_ok`` bool (True iff ``evidence["locator"]`` is a non-empty
    string). Missing locator still returns the copy, just ``_evidence_ok=False``.
    """
    action = dict(action) if isinstance(action, dict) else {}
    evidence = dict(evidence) if isinstance(evidence, dict) else {}
    locator = evidence.get("locator")
    evidence_ok = isinstance(locator, str) and bool(locator.strip())
    out = dict(action)
    out["evidence"] = evidence
    out["_evidence_ok"] = evidence_ok
    return out


def evidence_intact(step: Any, observed_state: dict[str, Any] | None = None) -> bool:
    """True iff a non-empty locator is present and observed state is consistent.

    When ``observed_state`` is provided, ``evidence["observed"]`` (if set) must
    agree with it on overlapping keys (equality only — no poker engine).
    """
    if not isinstance(step, dict):
        return False
    evidence = step.get("evidence")
    if not isinstance(evidence, dict):
        return False
    locator = evidence.get("locator")
    if not isinstance(locator, str) or not locator.strip():
        return False

    if observed_state is not None:
        observed = evidence.get("observed")
        if observed is not None:
            if not isinstance(observed, dict):
                return False
            for key, value in observed.items():
                if key in observed_state and observed_state[key] != value:
                    return False
    return True


def score_trace(steps: list[dict[str, Any]]) -> dict[str, Any]:
    """Score a trace on the evidence path, not the win/loss.

    Returns ``{activity, repetitions, grounded_count, ungrounded_count,
    first_break_index, busy_after_break, activity_ne_verification,
    evidence_intact}``.
    """
    steps = list(steps or [])

    grounded_count = 0
    ungrounded_count = 0
    first_break_index: int | None = None

    for idx, step in enumerate(steps):
        if evidence_intact(step):
            grounded_count += 1
        else:
            ungrounded_count += 1
            if first_break_index is None:
                first_break_index = idx

    repetitions = 0
    for idx in range(1, len(steps)):
        prev = _action_key(steps[idx - 1])
        cur = _action_key(steps[idx])
        if prev is not None and cur == prev:
            repetitions += 1

    activity = len(steps)
    busy_after_break = first_break_index is not None and first_break_index < activity - 1
    activity_ne_verification = busy_after_break or (
        ungrounded_count > 0 and activity >= 2
    )
    evidence_intact_all = ungrounded_count == 0 and activity > 0

    return {
        "activity": activity,
        "repetitions": repetitions,
        "grounded_count": grounded_count,
        "ungrounded_count": ungrounded_count,
        "first_break_index": first_break_index,
        "busy_after_break": busy_after_break,
        "activity_ne_verification": activity_ne_verification,
        "evidence_intact": evidence_intact_all,
    }


def _terminal_field(trace: list[dict[str, Any]]) -> tuple[Any, bool]:
    for step in reversed(trace):
        if isinstance(step, dict):
            for key in ("outcome", "win"):
                if key in step:
                    return step[key], True
    return None, False


def pair_traces(native: list[dict[str, Any]], treatment: list[dict[str, Any]]) -> dict[str, Any]:
    """Pair a native vs treatment trace; diff evidence paths, not win/loss.

    Aligns at the first output divergence (first index where ``action`` /
    ``action_class`` differs, or length mismatch). Returns ``first_divergence``
    (int or None), ``native_score`` / ``treatment_score``, ``outcome_same``
    (None if no terminal outcome/win field on either side), and
    ``evidence_path_same`` (both ``evidence_intact`` flags equal AND both
    ``first_break_index`` equal). ``outcome_same=True`` is **not**
    verification — a pair can share a win/loss and still have
    ``evidence_path_same=False``.
    """
    native = list(native or [])
    treatment = list(treatment or [])

    first_divergence: int | None = None
    common = min(len(native), len(treatment))
    for idx in range(common):
        if _action_key(native[idx]) != _action_key(treatment[idx]):
            first_divergence = idx
            break
    if first_divergence is None and len(native) != len(treatment):
        first_divergence = common

    native_score = score_trace(native)
    treatment_score = score_trace(treatment)

    native_outcome, native_has = _terminal_field(native)
    treatment_outcome, treatment_has = _terminal_field(treatment)
    if native_has and treatment_has:
        outcome_same: bool | None = native_outcome == treatment_outcome
    else:
        outcome_same = None

    evidence_path_same = (
        native_score["evidence_intact"] == treatment_score["evidence_intact"]
        and native_score["first_break_index"] == treatment_score["first_break_index"]
    )

    return {
        "first_divergence": first_divergence,
        "native_score": native_score,
        "treatment_score": treatment_score,
        "outcome_same": outcome_same,
        "evidence_path_same": evidence_path_same,
    }
