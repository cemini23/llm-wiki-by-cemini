"""K37 reviewer-agent v2 — selective-trigger middleware.

Public surface:

  Classification (pure):
    Bucket, Policy, ToolEntry, classify

  Loading + linting (I/O + schema validation):
    load_policy, load_policy_or_default, lint_policy, PolicyParseError

  Cost-ceiling telemetry (recorder + offline aggregator):
    TelemetryWriter, record, aggregate

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
"""

from conductor.reviewer.cost_aggregator import aggregate
from conductor.reviewer.cost_telemetry import TelemetryWriter, record
from conductor.reviewer.policy_loader import (
    PolicyParseError,
    lint_policy,
    load_policy,
    load_policy_or_default,
)
from conductor.reviewer.trigger_policy import Bucket, Policy, ToolEntry, classify

__all__ = [
    "Bucket",
    "Policy",
    "PolicyParseError",
    "TelemetryWriter",
    "ToolEntry",
    "aggregate",
    "classify",
    "lint_policy",
    "load_policy",
    "load_policy_or_default",
    "record",
]
