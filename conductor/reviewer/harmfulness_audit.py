"""Offline harmfulness-audit harness for the reviewer-agent v2 stack.

The harness replays held-out, independently-verified-correct base-agent
trajectories through the trigger-policy + reviewer stack and reports
the degradation rate introduced by reviewer intervention. It is an
**offline** tool — no runtime coupling, no latency impact on the
reviewer-agent critical path (see design.md Decision 5).

The replay is deterministic and pure:

    1. Parse trajectory JSON file(s) from input directory.
    2. For each trajectory:
       a. Run :func:`conductor.reviewer.trigger_policy.classify` to
          decide the bucket (``ALWAYS_REVIEW`` vs ``SKIP_REVIEW`` —
          ``classify`` resolves ``REVIEW_ON_UNCERTAINTY`` internally).
       b. If ``SKIP_REVIEW``: the base agent's output stands → outcome
          is ``UNCHANGED``.
       c. If ``ALWAYS_REVIEW``: invoke the injected reviewer callable
          → classify the reviewer's verdict against the known-correct
          expected output.
    3. Aggregate per-trajectory verdicts into a report with the
       harmfulness rate (``(revised_now_incorrect + refused) / total``)
       and the over-cautious-refusal sub-rate (``refused / total``).
    4. Optionally validate against a v1 baseline harmfulness rate;
       the CLI exits non-zero when ``v2_rate > baseline_rate``.

The reviewer is pluggable — the harness takes a callable so the same
analyzer can drive either a stub reviewer in tests or the production
DeepSeek-R1 client when wired into ``/opt/cemini``. Sprint 4 ships the
harness; production wiring lands at Sprint 5 (rollout).

Spec:  openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
Tasks: openspec/changes/reviewer-agent-selective-trigger/tasks.md (4.1 / 4.2 / 4.3 / 4.4)
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Union,
)

from conductor.reviewer.policy_loader import load_policy
from conductor.reviewer.trigger_policy import Bucket, Policy, classify


# --- Default-promotion gate ---------------------------------------------
#
# Task 4.4 fixes the minimum held-out sample at 50 trajectories. Smaller
# samples are too noisy for a go/no-go signal; the audit refuses to
# claim "passed" without it.
DEFAULT_MIN_TRAJECTORIES = 50


class Outcome(str, Enum):
    """Per-trajectory replay outcome (spec Requirement: Harmfulness audit)."""

    UNCHANGED = "unchanged"
    REVISED_STILL_CORRECT = "revised-still-correct"
    REVISED_NOW_INCORRECT = "revised-now-incorrect"
    REFUSED = "refused"


@dataclass(frozen=True)
class Trajectory:
    """One replay input: a base-agent tool call that was independently verified.

    Attributes:
        id: Stable identifier (filename stem if not provided in JSON).
        tool_name: Tool that the base agent called.
        tool_args: Arguments passed to the tool (kept for forward-compat with
            arg-conditional policies — see design.md Open Question 2).
        base_agent_output: What the v1 base agent produced for this call.
        expected_output: Ground-truth-correct output (the "independently
            verified" half). For known-correct trajectories this equals
            ``base_agent_output``.
        base_agent_confidence: Optional self-reported confidence; gates
            ``REVIEW_ON_UNCERTAINTY`` resolution inside :func:`classify`.
    """

    id: str
    tool_name: str
    tool_args: Mapping[str, Any]
    base_agent_output: Any
    expected_output: Any
    base_agent_confidence: Optional[float] = None


@dataclass(frozen=True)
class ReviewerVerdict:
    """What a reviewer returned for a single trajectory replay.

    Attributes:
        output: The (possibly-revised) tool output the reviewer endorses.
            Ignored when ``refused=True``.
        refused: ``True`` if the reviewer declined to endorse any output
            (an explicit "I cannot verify this" verdict — counted toward
            the over-cautious-refusal sub-rate).
    """

    output: Any = None
    refused: bool = False


# Reviewer callable contract. The harness invokes the reviewer only for
# trajectories the trigger-policy routed to ``ALWAYS_REVIEW``.
Reviewer = Callable[[Trajectory], ReviewerVerdict]


@dataclass(frozen=True)
class Verdict:
    """Per-trajectory replay result."""

    trajectory_id: str
    tool_name: str
    bucket: Bucket
    outcome: Outcome


def passthrough_reviewer(trajectory: Trajectory) -> ReviewerVerdict:
    """Stub reviewer that endorses the base-agent output unchanged.

    Useful for harness self-tests and operator smoke runs — produces a
    "no degradation" report against any trajectory set, which establishes
    that the analyzer + I/O paths work before the real reviewer is wired
    in. NOT a valid production reviewer.
    """
    return ReviewerVerdict(output=trajectory.base_agent_output, refused=False)


def audit_trajectories(
    trajectory_dir: Union[str, Path],
    policy: Policy,
    reviewer: Reviewer,
    *,
    baseline_rate: Optional[float] = None,
    min_trajectories: int = DEFAULT_MIN_TRAJECTORIES,
) -> Dict[str, Any]:
    """Replay every ``*.json`` trajectory in ``trajectory_dir``.

    Args:
        trajectory_dir: Directory of JSON trajectory files (one per file).
            Files are processed in sorted filename order for deterministic
            output. Non-``.json`` files are ignored.
        policy: Trigger-policy used to route each trajectory.
        reviewer: Callable invoked for trajectories routed to
            ``ALWAYS_REVIEW``. Must satisfy the :data:`Reviewer` contract.
        baseline_rate: Optional v1 harmfulness rate; if provided, the
            report's ``validation.passed`` is ``True`` iff
            ``harmfulness_rate <= baseline_rate`` AND
            ``total >= min_trajectories``.
        min_trajectories: Minimum sample size before validation can
            ``pass``. Default :data:`DEFAULT_MIN_TRAJECTORIES`. Smaller
            samples yield ``validation.insufficient_data = True``.

    Returns:
        Dict with:
            * ``trajectory_dir`` — input path (resolved string).
            * ``verdicts`` — per-trajectory list of dicts.
            * ``total`` — trajectory count.
            * ``by_outcome`` — count per :class:`Outcome` value.
            * ``harmfulness_rate`` — ``(revised_now_incorrect + refused) / total``.
            * ``over_cautious_refusal_rate`` — ``refused / total``.
            * ``by_bucket`` — per-bucket roll-up (sorted by bucket name).
            * ``by_tool`` — per-tool roll-up incl. per-tool harmfulness
              (sorted by tool name).
            * ``validation`` — gate decision block (always present; the
              ``baseline_rate``/``min_trajectories`` fields surface the
              inputs so the CLI exit code is auditable).

    Raises:
        FileNotFoundError: ``trajectory_dir`` does not exist.
        NotADirectoryError: ``trajectory_dir`` exists but is not a dir.
        ValueError: A trajectory file is malformed JSON or missing the
            required ``tool_name`` / ``base_agent_output`` /
            ``expected_output`` fields.
    """
    trajectory_dir = Path(trajectory_dir)
    if not trajectory_dir.exists():
        raise FileNotFoundError(
            f"trajectory directory not found: {trajectory_dir}",
        )
    if not trajectory_dir.is_dir():
        raise NotADirectoryError(
            f"trajectory path is not a directory: {trajectory_dir}",
        )

    verdicts: List[Verdict] = []
    for path in sorted(trajectory_dir.glob("*.json")):
        traj = _load_trajectory(path)
        bucket = classify(
            traj.tool_name, traj.tool_args, policy, traj.base_agent_confidence,
        )
        outcome = _replay_outcome(traj, bucket, reviewer)
        verdicts.append(Verdict(
            trajectory_id=traj.id,
            tool_name=traj.tool_name,
            bucket=bucket,
            outcome=outcome,
        ))

    return _build_report(
        trajectory_dir, verdicts, baseline_rate, min_trajectories,
    )


def _load_trajectory(path: Path) -> Trajectory:
    """Parse one trajectory JSON file with schema validation."""
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"malformed trajectory JSON at {path}: {exc}",
        ) from exc
    if not isinstance(raw, dict):
        raise ValueError(
            f"trajectory at {path} is not a JSON object",
        )

    tool_name = raw.get("tool_name")
    if not isinstance(tool_name, str) or not tool_name:
        raise ValueError(
            f"trajectory at {path} missing required 'tool_name' string",
        )
    if "base_agent_output" not in raw:
        raise ValueError(
            f"trajectory at {path} missing required 'base_agent_output'",
        )
    if "expected_output" not in raw:
        raise ValueError(
            f"trajectory at {path} missing required 'expected_output'",
        )

    tool_args = raw.get("tool_args") or {}
    if not isinstance(tool_args, Mapping):
        raise ValueError(
            f"trajectory at {path} field 'tool_args' must be an object",
        )

    confidence = raw.get("base_agent_confidence")
    if confidence is not None:
        # bool is an int subclass in Python — guard against it being
        # passed as a confidence score by accident.
        if isinstance(confidence, bool) or not isinstance(
            confidence, (int, float),
        ):
            raise ValueError(
                f"trajectory at {path} 'base_agent_confidence' must be numeric",
            )
        confidence = float(confidence)

    return Trajectory(
        id=str(raw.get("id") or path.stem),
        tool_name=tool_name,
        tool_args=dict(tool_args),
        base_agent_output=raw["base_agent_output"],
        expected_output=raw["expected_output"],
        base_agent_confidence=confidence,
    )


def _replay_outcome(
    trajectory: Trajectory,
    bucket: Bucket,
    reviewer: Reviewer,
) -> Outcome:
    """Compute the outcome for one trajectory.

    Per the spec Requirement "Bucket routing": ``classify`` returns a
    terminal bucket (``ALWAYS_REVIEW`` or ``SKIP_REVIEW``) —
    ``REVIEW_ON_UNCERTAINTY`` is resolved internally. If a bucket value
    ever reaches this function as ``REVIEW_ON_UNCERTAINTY``, the
    invariant has been violated upstream and we fail loud rather than
    silently treating it as either terminal value.
    """
    if bucket == Bucket.SKIP_REVIEW:
        # Reviewer never sees this call; the base agent's output stands.
        # The trajectory was independently verified correct, so by
        # definition this contributes zero harmfulness.
        return Outcome.UNCHANGED

    if bucket == Bucket.ALWAYS_REVIEW:
        verdict = reviewer(trajectory)
        return _classify_outcome(
            base_output=trajectory.base_agent_output,
            expected_output=trajectory.expected_output,
            verdict=verdict,
        )

    raise AssertionError(  # pragma: no cover -- guards a classifier invariant
        f"unexpected non-terminal bucket {bucket!r} from classify(); "
        f"trigger_policy must resolve REVIEW_ON_UNCERTAINTY internally",
    )


def _classify_outcome(
    base_output: Any,
    expected_output: Any,
    verdict: ReviewerVerdict,
) -> Outcome:
    """Compare a reviewer verdict to the base + expected outputs."""
    if verdict.refused:
        return Outcome.REFUSED
    if verdict.output == base_output:
        return Outcome.UNCHANGED
    if verdict.output == expected_output:
        # Reviewer changed the output and landed on the verified-correct
        # answer — net-positive intervention.
        return Outcome.REVISED_STILL_CORRECT
    return Outcome.REVISED_NOW_INCORRECT


def _build_report(
    trajectory_dir: Path,
    verdicts: List[Verdict],
    baseline_rate: Optional[float],
    min_trajectories: int,
) -> Dict[str, Any]:
    total = len(verdicts)
    by_outcome: Dict[str, int] = {o.value: 0 for o in Outcome}
    by_bucket_raw: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, **{o.value: 0 for o in Outcome}},
    )
    by_tool_raw: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, **{o.value: 0 for o in Outcome}},
    )

    for v in verdicts:
        by_outcome[v.outcome.value] += 1
        by_bucket_raw[v.bucket.value]["total"] += 1
        by_bucket_raw[v.bucket.value][v.outcome.value] += 1
        by_tool_raw[v.tool_name]["total"] += 1
        by_tool_raw[v.tool_name][v.outcome.value] += 1

    if total == 0:
        harmfulness_rate = 0.0
        over_cautious_rate = 0.0
    else:
        harmful = (
            by_outcome[Outcome.REVISED_NOW_INCORRECT.value]
            + by_outcome[Outcome.REFUSED.value]
        )
        harmfulness_rate = harmful / total
        over_cautious_rate = by_outcome[Outcome.REFUSED.value] / total

    # Sorted dicts for deterministic JSON output (dashboards diff these).
    by_bucket = {k: dict(by_bucket_raw[k]) for k in sorted(by_bucket_raw)}
    by_tool: Dict[str, Dict[str, Any]] = {}
    for tool in sorted(by_tool_raw):
        agg = by_tool_raw[tool]
        tool_total = agg["total"]
        tool_harmful = (
            agg[Outcome.REVISED_NOW_INCORRECT.value]
            + agg[Outcome.REFUSED.value]
        )
        by_tool[tool] = {
            **agg,
            "harmfulness_rate": (
                tool_harmful / tool_total if tool_total else 0.0
            ),
        }

    validation = _build_validation_block(
        total, harmfulness_rate, baseline_rate, min_trajectories,
    )

    return {
        "trajectory_dir": str(trajectory_dir.resolve()),
        "total": total,
        "by_outcome": by_outcome,
        "harmfulness_rate": round(harmfulness_rate, 6),
        "over_cautious_refusal_rate": round(over_cautious_rate, 6),
        "by_bucket": by_bucket,
        "by_tool": by_tool,
        "verdicts": [
            {
                "id": v.trajectory_id,
                "tool": v.tool_name,
                "bucket": v.bucket.value,
                "outcome": v.outcome.value,
            }
            for v in verdicts
        ],
        "validation": validation,
    }


def _build_validation_block(
    total: int,
    harmfulness_rate: float,
    baseline_rate: Optional[float],
    min_trajectories: int,
) -> Dict[str, Any]:
    """Compose the validation-gate decision block.

    The block is always present so consumers (dashboards, CI) can rely
    on a stable schema. ``passed`` is ``None`` when no baseline was
    provided — the harness is informational then, not gating.
    """
    insufficient = total < min_trajectories
    block: Dict[str, Any] = {
        "baseline_rate": baseline_rate,
        "min_trajectories": min_trajectories,
        "total_trajectories": total,
        "insufficient_data": insufficient,
        "harmfulness_rate": round(harmfulness_rate, 6),
    }
    if baseline_rate is None:
        block["passed"] = None
        block["delta"] = None
        return block
    delta = harmfulness_rate - baseline_rate
    block["delta"] = round(delta, 6)
    # Promotion criterion (Task 4.4): rate ≤ baseline AND adequate sample.
    block["passed"] = (not insufficient) and (
        harmfulness_rate <= baseline_rate
    )
    return block


def _resolve_reviewer(spec: str) -> Reviewer:
    """Resolve a reviewer-callable from a CLI ``--reviewer`` value.

    Forms:

      * ``"passthrough"`` — the built-in :func:`passthrough_reviewer`
        (smoke/sanity runs; not a production reviewer).
      * ``"module.path:callable"`` — dynamic import of an attribute.

    Raises:
        ValueError: Resolution fails (unknown module, missing attr,
            attr is not callable).
    """
    if spec == "passthrough":
        return passthrough_reviewer
    if ":" not in spec:
        raise ValueError(
            f"--reviewer must be 'passthrough' or 'module.path:callable', "
            f"got {spec!r}",
        )
    module_path, _, attr = spec.partition(":")
    try:
        module = importlib.import_module(module_path)
    except ImportError as exc:
        raise ValueError(
            f"--reviewer module {module_path!r} not importable: {exc}",
        ) from exc
    if not hasattr(module, attr):
        raise ValueError(
            f"--reviewer module {module_path!r} has no attribute {attr!r}",
        )
    candidate = getattr(module, attr)
    if not callable(candidate):
        raise ValueError(
            f"--reviewer target {spec!r} is not callable",
        )
    return candidate  # type: ignore[no-any-return]


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code.

    Exit codes:
        * ``0`` — audit ran; if ``--baseline-rate`` was set, the gate
          passed (or no baseline was provided — informational mode).
        * ``1`` — gate failed (``harmfulness_rate > baseline_rate``).
        * ``2`` — insufficient data (``total < --min-trajectories``)
          when a baseline was provided.
        * ``3`` — malformed input (bad trajectory JSON, missing dir,
          policy parse error, reviewer-resolution failure).
    """
    parser = argparse.ArgumentParser(
        prog="harmfulness_audit",
        description=(
            "Replay a directory of independently-verified trajectories "
            "through the reviewer-agent v2 stack and report the "
            "harmfulness rate vs a v1 baseline."
        ),
    )
    parser.add_argument(
        "trajectory_dir",
        type=Path,
        help="Directory of *.json trajectory files.",
    )
    parser.add_argument(
        "--policy",
        type=Path,
        required=True,
        help="Path to the trigger-policy YAML file.",
    )
    parser.add_argument(
        "--reviewer",
        type=str,
        default="passthrough",
        help=(
            "Reviewer callable: 'passthrough' (built-in stub) or "
            "'module.path:callable_name'. Default: passthrough."
        ),
    )
    parser.add_argument(
        "--baseline-rate",
        type=float,
        default=None,
        help=(
            "v1 harmfulness rate to gate against. If set, exit code is "
            "1 when v2 exceeds this; omit for informational-only mode."
        ),
    )
    parser.add_argument(
        "--min-trajectories",
        type=int,
        default=DEFAULT_MIN_TRAJECTORIES,
        help=(
            f"Minimum trajectory count for the gate to pass "
            f"(default: {DEFAULT_MIN_TRAJECTORIES})."
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output JSON path (default: stdout).",
    )
    args = parser.parse_args(argv)

    try:
        policy = load_policy(args.policy)
        reviewer = _resolve_reviewer(args.reviewer)
        report = audit_trajectories(
            args.trajectory_dir,
            policy=policy,
            reviewer=reviewer,
            baseline_rate=args.baseline_rate,
            min_trajectories=args.min_trajectories,
        )
    except (FileNotFoundError, NotADirectoryError, ValueError) as exc:
        print(f"harmfulness_audit: {exc}", file=sys.stderr)
        return 3

    json_str = json.dumps(report, indent=2, sort_keys=False)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json_str + "\n", encoding="utf-8")
    else:
        print(json_str)

    # Exit-code policy: only gate when a baseline was set.
    if args.baseline_rate is None:
        return 0
    validation = report["validation"]
    if validation["insufficient_data"]:
        return 2
    return 0 if validation["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
