"""Trigger-policy classifier for K37 reviewer-agent v2 (selective-trigger gating).

Resolves provisional tool calls into a terminal routing decision before the
reviewer-agent is invoked. Three policy buckets map to two terminal routes:

  - ALWAYS_REVIEW (policy)        -> ALWAYS_REVIEW (terminal)
  - SKIP_REVIEW (policy)          -> SKIP_REVIEW   (terminal)
  - REVIEW_ON_UNCERTAINTY (policy) -> ALWAYS_REVIEW or SKIP_REVIEW
        depending on the base-agent's confidence score vs the per-tool
        uncertainty threshold.

Safe defaults (per K37 concept-doc safety posture):
  - Tools not enumerated in the policy fall through to ALWAYS_REVIEW.
    A new tool surface added without a policy update never silently
    bypasses the reviewer.
  - REVIEW_ON_UNCERTAINTY with a missing confidence score escalates to
    ALWAYS_REVIEW (treats missing-as-low rather than missing-as-high).

The ``classify`` function is the single public entry point. It is pure
(no I/O, no globals) so the harmfulness audit harness can replay
trajectories deterministically.

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
Tasks: openspec/changes/reviewer-agent-selective-trigger/tasks.md (1.1 + 1.2)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional


class Bucket(Enum):
    """Policy-level + terminal classification for a provisional tool call.

    REVIEW_ON_UNCERTAINTY is a *policy-config* value only. :func:`classify`
    never returns it — the resolver always reduces it to ALWAYS_REVIEW or
    SKIP_REVIEW based on the base-agent's confidence vs the per-tool
    threshold (see :func:`classify` docstring for the rule order).

    String values match the YAML policy-file representation (see Task 2.1
    in tasks.md).
    """

    ALWAYS_REVIEW = "always-review"
    REVIEW_ON_UNCERTAINTY = "review-on-uncertainty"
    SKIP_REVIEW = "skip-review"


@dataclass(frozen=True)
class ToolEntry:
    """Per-tool policy entry parsed from the YAML policy file.

    Attributes:
        bucket: One of the three :class:`Bucket` values.
        threshold: Required iff ``bucket`` is ``REVIEW_ON_UNCERTAINTY``;
            must lie in ``[0.0, 1.0]``. A misconfigured entry (review-
            on-uncertainty with ``threshold=None``) escalates at classify
            time rather than silently skipping the reviewer.
        notes: Free-form policy-author annotation, ignored at runtime.
    """

    bucket: Bucket
    threshold: Optional[float] = None
    notes: Optional[str] = None


@dataclass(frozen=True)
class Policy:
    """In-memory representation of the loaded trigger-policy YAML file.

    The ``tools`` map keys are tool-name strings that must match the
    Conductor tool registry exactly. Tools absent from the map fall
    through to ALWAYS_REVIEW at classification time (safe-default for
    unclassified surfaces).
    """

    tools: Mapping[str, ToolEntry] = field(default_factory=dict)


def classify(
    tool_name: str,
    tool_args: Optional[Mapping[str, Any]],
    policy: Policy,
    base_agent_confidence: Optional[float],
) -> Bucket:
    """Return the terminal routing bucket for a provisional tool call.

    Resolution rules (evaluated in order, first match wins):

    1. ``tool_name`` not in ``policy.tools``           -> ALWAYS_REVIEW
       (safe-default: unknown tools never silently bypass review)
    2. Policy bucket is ``ALWAYS_REVIEW``              -> ALWAYS_REVIEW
    3. Policy bucket is ``SKIP_REVIEW``                -> SKIP_REVIEW
    4. Policy bucket is ``REVIEW_ON_UNCERTAINTY``:
        a. ``threshold`` is None (misconfig)           -> ALWAYS_REVIEW
        b. ``base_agent_confidence`` is None           -> ALWAYS_REVIEW
           (spec safe-default: missing confidence treated as low)
        c. ``base_agent_confidence < threshold``       -> ALWAYS_REVIEW
        d. ``base_agent_confidence >= threshold``      -> SKIP_REVIEW
           (strict-less-than escalation semantic; confidence at exactly
           the threshold passes through without review)

    The ``tool_args`` parameter is accepted but currently unused, reserved
    for the deferred arg-conditional policy rules (design.md Open
    Question 2).

    Args:
        tool_name: Provisional tool call's name (matches policy key).
        tool_args: Provisional tool call's argument map (reserved).
        policy: The loaded :class:`Policy`.
        base_agent_confidence: Optional confidence score, typically in
            ``[0.0, 1.0]``. ``None`` triggers the safe-default escalation
            for ``REVIEW_ON_UNCERTAINTY`` entries.

    Returns:
        Terminal :class:`Bucket`. Always one of ``ALWAYS_REVIEW`` or
        ``SKIP_REVIEW``; never ``REVIEW_ON_UNCERTAINTY``.
    """
    del tool_args  # forward-compat placeholder; see design.md Open Question 2

    entry = policy.tools.get(tool_name)
    if entry is None:
        # Rule 1: unclassified tool -> safe-default to ALWAYS_REVIEW.
        return Bucket.ALWAYS_REVIEW

    if entry.bucket is Bucket.ALWAYS_REVIEW:
        # Rule 2: explicit always-review tool.
        return Bucket.ALWAYS_REVIEW

    if entry.bucket is Bucket.SKIP_REVIEW:
        # Rule 3: explicit skip-review tool.
        return Bucket.SKIP_REVIEW

    # Rule 4: REVIEW_ON_UNCERTAINTY — resolve against confidence vs threshold.
    if entry.threshold is None:
        # Rule 4a: policy author forgot to set a threshold for a
        # review-on-uncertainty bucket. Fail toward review rather than
        # silently skip; the lint pass (Task 2.3) will surface this.
        return Bucket.ALWAYS_REVIEW

    if base_agent_confidence is None:
        # Rule 4b: spec safe-default — missing confidence escalates.
        return Bucket.ALWAYS_REVIEW

    if base_agent_confidence < entry.threshold:
        # Rule 4c: below-threshold -> escalate.
        return Bucket.ALWAYS_REVIEW

    # Rule 4d: at-or-above-threshold -> skip.
    return Bucket.SKIP_REVIEW
