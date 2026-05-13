"""Trigger-policy YAML loader, schema validator, and side-effecting lint pass.

This module owns the I/O surface that turns a YAML policy file into the
pure-Python :class:`Policy` consumed by :func:`classify`. It also owns the
operator-facing lint pass that surfaces likely misconfigurations at
startup time.

Behavior contract (per spec.md and tasks.md 2.4):

  - **Path exists, valid YAML, valid schema** -> :func:`load_policy`
    returns the parsed :class:`Policy`.
  - **Path exists, parse error or schema violation** -> raise
    :class:`PolicyParseError` (fail-closed; Conductor refuses to start).
  - **Path missing** -> :func:`load_policy` raises ``FileNotFoundError``;
    the higher-level :func:`load_policy_or_default` swallows that and
    returns an empty :class:`Policy` after emitting a single WARNING.
    (Empty policy + safe-default classify() routes every call to
    ALWAYS_REVIEW — non-regressive vs v1.)

The schema enforced here is documented inline in ``policy.yaml``.

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
Tasks: openspec/changes/reviewer-agent-selective-trigger/tasks.md (2.1 / 2.3 / 2.4)
"""

from __future__ import annotations

import fnmatch
import logging
from pathlib import Path
from typing import Any, Dict, List, Union

import yaml

from conductor.reviewer.trigger_policy import Bucket, Policy, ToolEntry

LOGGER = logging.getLogger(__name__)

# Glob-style patterns identifying tool-name shapes that are almost
# always side-effecting. A tool matching any pattern that is classified
# `skip-review` is flagged by :func:`lint_policy` as a likely
# misconfiguration. See spec.md "Risks / Trade-offs" + tasks.md 2.3.
SIDE_EFFECTING_PATTERNS = ("place_*", "withdraw_*", "cancel_*", "close_*")


class PolicyParseError(ValueError):
    """Raised on malformed policy YAML or schema violations.

    Conductor's startup sequence should let this propagate (fail-closed):
    a malformed policy means the operator intended a policy and got it
    wrong, so the safest action is to refuse to start.
    """


# --- Loading -----------------------------------------------------------------


def load_policy(path: Union[str, Path]) -> Policy:
    """Load + validate a trigger-policy YAML file into a :class:`Policy`.

    Args:
        path: Filesystem path to the YAML policy file.

    Returns:
        Parsed :class:`Policy`.

    Raises:
        FileNotFoundError: If ``path`` does not exist. Callers wanting
            graceful absent-file fallback should use
            :func:`load_policy_or_default` instead.
        PolicyParseError: On YAML syntax errors or schema violations
            (unknown bucket value, missing required field, threshold
            out of range, etc.).
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(str(path))

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise PolicyParseError(f"YAML parse error in {path}: {exc}") from exc

    return _parse_policy_dict(raw, source=path)


def load_policy_or_default(path: Union[str, Path]) -> Policy:
    """Production-ready load helper with absent-file fallback.

    Behavior:
      - Path missing -> emit single WARNING log entry; return empty
        :class:`Policy`. (Caller's classify() will safe-default every
        call to ALWAYS_REVIEW — non-regressive vs v1.)
      - Path exists -> delegate to :func:`load_policy`. Parse errors
        propagate (fail-closed).

    Args:
        path: Filesystem path to the YAML policy file.

    Returns:
        :class:`Policy` (possibly empty on missing-file fallback).

    Raises:
        PolicyParseError: On YAML syntax errors or schema violations.
    """
    path = Path(path)
    if not path.exists():
        LOGGER.warning(
            "trigger-policy file not found at %s; falling back to v1 "
            "always-review behavior for every tool call",
            path,
        )
        return Policy()
    return load_policy(path)


# --- Parsing -----------------------------------------------------------------


def _parse_policy_dict(raw: Any, source: Path) -> Policy:
    if raw is None:
        # Empty file is treated as "no tools enumerated" — classify()'s
        # safe-default routes every call to ALWAYS_REVIEW.
        return Policy()

    if not isinstance(raw, dict):
        raise PolicyParseError(
            f"{source}: top-level YAML must be a mapping, "
            f"got {type(raw).__name__}",
        )

    tools_raw = raw.get("tools")
    if tools_raw is None:
        return Policy()
    if not isinstance(tools_raw, dict):
        raise PolicyParseError(
            f"{source}: 'tools' must be a mapping, "
            f"got {type(tools_raw).__name__}",
        )

    tools: Dict[str, ToolEntry] = {}
    for tool_name, entry_raw in tools_raw.items():
        if not isinstance(tool_name, str):
            raise PolicyParseError(
                f"{source}: tool key must be string, "
                f"got {type(tool_name).__name__}",
            )
        tools[tool_name] = _parse_entry(tool_name, entry_raw, source)

    return Policy(tools=tools)


def _parse_entry(tool_name: str, raw: Any, source: Path) -> ToolEntry:
    if not isinstance(raw, dict):
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' entry must be a mapping, "
            f"got {type(raw).__name__}",
        )

    bucket_str = raw.get("bucket")
    if not isinstance(bucket_str, str):
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' missing required string field "
            f"'bucket'",
        )
    try:
        bucket = Bucket(bucket_str)
    except ValueError:
        valid = ", ".join(b.value for b in Bucket)
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' has unknown bucket "
            f"'{bucket_str}' (valid: {valid})",
        )

    threshold_raw = raw.get("uncertainty_threshold")
    threshold: "float | None"
    if threshold_raw is None:
        threshold = None
    else:
        if isinstance(threshold_raw, bool) or not isinstance(
            threshold_raw, (int, float),
        ):
            # bool is a subclass of int in Python; reject explicitly.
            raise PolicyParseError(
                f"{source}: tool '{tool_name}' uncertainty_threshold must "
                f"be numeric, got {type(threshold_raw).__name__}",
            )
        threshold = float(threshold_raw)
        if not (0.0 <= threshold <= 1.0):
            raise PolicyParseError(
                f"{source}: tool '{tool_name}' uncertainty_threshold "
                f"{threshold} must be in [0.0, 1.0]",
            )

    # Schema check: review-on-uncertainty REQUIRES a threshold.
    # (The classifier already escalates on missing-threshold as a
    # defense-in-depth guard, but rejecting at parse time gives a
    # clearer error to the policy author.)
    if bucket is Bucket.REVIEW_ON_UNCERTAINTY and threshold is None:
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' bucket is "
            f"'review-on-uncertainty' but no 'uncertainty_threshold' "
            f"was set (required for this bucket)",
        )

    notes = raw.get("notes")
    if notes is not None and not isinstance(notes, str):
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' notes must be string, "
            f"got {type(notes).__name__}",
        )

    # Reject unknown keys to catch policy-author typos early.
    allowed = {"bucket", "uncertainty_threshold", "notes"}
    unknown = set(raw.keys()) - allowed
    if unknown:
        raise PolicyParseError(
            f"{source}: tool '{tool_name}' has unknown field(s): "
            f"{sorted(unknown)} (allowed: {sorted(allowed)})",
        )

    return ToolEntry(bucket=bucket, threshold=threshold, notes=notes)


# --- Linting -----------------------------------------------------------------


def lint_policy(policy: Policy) -> List[str]:
    """Return a list of human-readable warnings for the loaded policy.

    Current checks (Task 2.3):
      - Side-effecting naming patterns (``place_*``, ``withdraw_*``,
        ``cancel_*``, ``close_*``) classified as ``skip-review`` are
        flagged as likely misconfigurations.

    Linting is non-fatal: the caller decides whether to log, fail-fast,
    or ignore. Conductor's startup should log every warning at WARNING
    level so the operator sees them.

    Args:
        policy: Parsed :class:`Policy`.

    Returns:
        List of warning strings. Empty list means policy is clean.
    """
    warnings: List[str] = []
    for tool_name, entry in policy.tools.items():
        if entry.bucket is not Bucket.SKIP_REVIEW:
            continue
        for pattern in SIDE_EFFECTING_PATTERNS:
            if fnmatch.fnmatch(tool_name, pattern):
                warnings.append(
                    f"tool '{tool_name}' matches side-effecting pattern "
                    f"'{pattern}' but is classified 'skip-review'; this "
                    f"silently bypasses the reviewer-agent for a likely "
                    f"side-effecting call",
                )
                break  # one warning per tool is enough
    return warnings
