"""K37 reviewer-agent v2 — selective-trigger middleware.

Public surface for the trigger-policy classifier. The classifier resolves
a provisional tool call into a terminal routing decision (ALWAYS_REVIEW
or SKIP_REVIEW) before any reviewer-agent invocation.

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
"""

from conductor.reviewer.trigger_policy import Bucket, Policy, ToolEntry, classify

__all__ = ["Bucket", "Policy", "ToolEntry", "classify"]
