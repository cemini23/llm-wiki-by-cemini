"""Unit tests for ``conductor.reviewer.harmfulness_audit``."""

from __future__ import annotations

import json
import tempfile
import textwrap
import unittest
from pathlib import Path
from typing import Any, Dict, List

from conductor.reviewer.harmfulness_audit import (
    DEFAULT_MIN_TRAJECTORIES,
    Outcome,
    ReviewerVerdict,
    Trajectory,
    audit_trajectories,
    main,
    passthrough_reviewer,
)
from conductor.reviewer.trigger_policy import (
    Bucket,
    Policy,
    ToolEntry,
)


# --- Test fixtures ------------------------------------------------------


def _write_trajectory(
    directory: Path,
    name: str,
    *,
    tool_name: str,
    tool_args: Dict[str, Any] = None,
    base_output: Any = "ok",
    expected_output: Any = "ok",
    confidence: float = None,
    traj_id: str = None,
) -> Path:
    """Write one trajectory JSON file; return the path."""
    payload: Dict[str, Any] = {
        "tool_name": tool_name,
        "tool_args": tool_args or {},
        "base_agent_output": base_output,
        "expected_output": expected_output,
    }
    if traj_id is not None:
        payload["id"] = traj_id
    if confidence is not None:
        payload["base_agent_confidence"] = confidence
    path = directory / f"{name}.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _policy_with(
    *entries: tuple,
) -> Policy:
    """Build an inline Policy: ``_policy_with(("place_order","always-review",None), ...)``."""
    tools: Dict[str, ToolEntry] = {}
    for name, bucket_value, threshold in entries:
        tools[name] = ToolEntry(
            bucket=Bucket(bucket_value),
            threshold=threshold,
        )
    return Policy(tools=tools)


# --- Outcome-classification tests ---------------------------------------


class OutcomeClassificationTests(unittest.TestCase):
    """All four Outcome classes (spec Requirement: Audit harness runs on sample)."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        # `place_order` -> always-review; `get_price` -> skip-review.
        self.policy = _policy_with(
            ("place_order", "always-review", None),
            ("get_price", "skip-review", None),
        )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_skip_review_yields_unchanged(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="get_price",
            base_output={"price": 100}, expected_output={"price": 100},
        )

        def reviewer_should_not_run(_traj: Trajectory) -> ReviewerVerdict:
            raise AssertionError(
                "reviewer must NOT be invoked for SKIP_REVIEW bucket",
            )

        report = audit_trajectories(
            self.path, self.policy, reviewer_should_not_run,
        )
        self.assertEqual(report["total"], 1)
        self.assertEqual(report["by_outcome"]["unchanged"], 1)

    def test_reviewer_agrees_yields_unchanged(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output={"status": "ok"}, expected_output={"status": "ok"},
        )
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
        )
        self.assertEqual(report["by_outcome"]["unchanged"], 1)
        self.assertEqual(report["harmfulness_rate"], 0.0)

    def test_reviewer_revises_to_correct_yields_revised_still_correct(self) -> None:
        # Setup: base agent was WRONG; reviewer fixes it to expected.
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output={"status": "wrong"},
            expected_output={"status": "ok"},
        )

        def fixing_reviewer(traj: Trajectory) -> ReviewerVerdict:
            return ReviewerVerdict(output=traj.expected_output)

        report = audit_trajectories(self.path, self.policy, fixing_reviewer)
        self.assertEqual(report["by_outcome"]["revised-still-correct"], 1)
        # revised-still-correct does NOT count toward harmfulness.
        self.assertEqual(report["harmfulness_rate"], 0.0)

    def test_reviewer_revises_to_wrong_yields_revised_now_incorrect(self) -> None:
        # Base agent was correct; reviewer breaks it.
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output={"status": "ok"}, expected_output={"status": "ok"},
        )

        def breaking_reviewer(_t: Trajectory) -> ReviewerVerdict:
            return ReviewerVerdict(output={"status": "now-broken"})

        report = audit_trajectories(self.path, self.policy, breaking_reviewer)
        self.assertEqual(report["by_outcome"]["revised-now-incorrect"], 1)
        self.assertEqual(report["harmfulness_rate"], 1.0)
        self.assertEqual(report["over_cautious_refusal_rate"], 0.0)

    def test_reviewer_refuses_counts_to_both_rates(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )

        def refusing_reviewer(_t: Trajectory) -> ReviewerVerdict:
            return ReviewerVerdict(refused=True)

        report = audit_trajectories(self.path, self.policy, refusing_reviewer)
        self.assertEqual(report["by_outcome"]["refused"], 1)
        # Refusal counts as harmfulness AND as over-cautious sub-rate.
        self.assertEqual(report["harmfulness_rate"], 1.0)
        self.assertEqual(report["over_cautious_refusal_rate"], 1.0)


# --- Aggregate / report-shape tests -------------------------------------


class AggregateReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        self.policy = _policy_with(
            ("place_order", "always-review", None),
            ("get_price", "skip-review", None),
        )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_empty_directory_yields_zero_report(self) -> None:
        report = audit_trajectories(self.path, self.policy, passthrough_reviewer)
        self.assertEqual(report["total"], 0)
        self.assertEqual(report["harmfulness_rate"], 0.0)
        self.assertEqual(report["over_cautious_refusal_rate"], 0.0)
        self.assertEqual(report["verdicts"], [])

    def test_non_json_files_are_ignored(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        # Drop a non-JSON file in the same directory.
        (self.path / "readme.txt").write_text("not a trajectory")
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
        )
        self.assertEqual(report["total"], 1)

    def test_verdicts_sorted_by_filename(self) -> None:
        _write_trajectory(
            self.path, "z-last", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        _write_trajectory(
            self.path, "a-first", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        _write_trajectory(
            self.path, "m-middle", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
        )
        ids = [v["id"] for v in report["verdicts"]]
        self.assertEqual(ids, ["a-first", "m-middle", "z-last"])

    def test_per_tool_breakdown(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        _write_trajectory(
            self.path, "t2", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        _write_trajectory(
            self.path, "t3", tool_name="get_price",
            base_output={"p": 1}, expected_output={"p": 1},
        )
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
        )
        # Sorted by tool name.
        self.assertEqual(list(report["by_tool"].keys()), ["get_price", "place_order"])
        self.assertEqual(report["by_tool"]["place_order"]["total"], 2)
        self.assertEqual(report["by_tool"]["get_price"]["total"], 1)
        self.assertEqual(report["by_tool"]["place_order"]["harmfulness_rate"], 0.0)

    def test_per_bucket_breakdown(self) -> None:
        _write_trajectory(
            self.path, "t1", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )
        _write_trajectory(
            self.path, "t2", tool_name="get_price",
            base_output="ok", expected_output="ok",
        )
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
        )
        self.assertEqual(
            list(report["by_bucket"].keys()), ["always-review", "skip-review"],
        )
        self.assertEqual(report["by_bucket"]["always-review"]["total"], 1)
        self.assertEqual(report["by_bucket"]["skip-review"]["total"], 1)

    def test_mixed_outcomes_compute_rates_correctly(self) -> None:
        # 4 always-review trajectories. Pre-decide outcomes per trajectory_id.
        _write_trajectory(self.path, "t1", tool_name="place_order",
                          base_output="ok", expected_output="ok", traj_id="t1")
        _write_trajectory(self.path, "t2", tool_name="place_order",
                          base_output="ok", expected_output="ok", traj_id="t2")
        _write_trajectory(self.path, "t3", tool_name="place_order",
                          base_output="ok", expected_output="ok", traj_id="t3")
        _write_trajectory(self.path, "t4", tool_name="place_order",
                          base_output="ok", expected_output="ok", traj_id="t4")

        def mixed_reviewer(traj: Trajectory) -> ReviewerVerdict:
            if traj.id == "t1":
                return ReviewerVerdict(output="ok")             # unchanged
            if traj.id == "t2":
                return ReviewerVerdict(output="now-broken")     # revised-now-incorrect
            if traj.id == "t3":
                return ReviewerVerdict(refused=True)            # refused
            return ReviewerVerdict(output="ok")                  # unchanged

        report = audit_trajectories(self.path, self.policy, mixed_reviewer)
        self.assertEqual(report["total"], 4)
        self.assertEqual(report["by_outcome"]["unchanged"], 2)
        self.assertEqual(report["by_outcome"]["revised-now-incorrect"], 1)
        self.assertEqual(report["by_outcome"]["refused"], 1)
        # harmfulness = (1 incorrect + 1 refused) / 4 = 0.5
        self.assertEqual(report["harmfulness_rate"], 0.5)
        # over-cautious sub-rate = 1 refused / 4 = 0.25
        self.assertEqual(report["over_cautious_refusal_rate"], 0.25)

    def test_review_on_uncertainty_resolves_via_classify(self) -> None:
        # `submit_research_query` -> review-on-uncertainty, threshold 0.7.
        # Confidence 0.5 < 0.7 -> escalates to ALWAYS_REVIEW.
        policy = _policy_with(
            ("submit_research_query", "review-on-uncertainty", 0.7),
        )
        _write_trajectory(
            self.path, "t1", tool_name="submit_research_query",
            confidence=0.5, base_output="ok", expected_output="ok",
        )
        report = audit_trajectories(self.path, policy, passthrough_reviewer)
        # Bucket recorded should be the resolved terminal bucket.
        self.assertEqual(report["verdicts"][0]["bucket"], "always-review")


# --- Validation-gate tests ----------------------------------------------


class ValidationGateTests(unittest.TestCase):
    """Task 4.4 — harmfulness rate ≤ v1 baseline on ≥50 trajectories."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        self.policy = _policy_with(("place_order", "always-review", None))

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _make_n_trajectories(self, n: int) -> None:
        for i in range(n):
            _write_trajectory(
                self.path, f"t{i:03d}", tool_name="place_order",
                base_output="ok", expected_output="ok",
            )

    def test_no_baseline_means_informational_only(self) -> None:
        self._make_n_trajectories(2)
        report = audit_trajectories(self.path, self.policy, passthrough_reviewer)
        self.assertIsNone(report["validation"]["passed"])
        self.assertIsNone(report["validation"]["delta"])
        self.assertEqual(report["validation"]["baseline_rate"], None)

    def test_insufficient_data_flagged(self) -> None:
        self._make_n_trajectories(10)
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
            baseline_rate=0.1, min_trajectories=50,
        )
        self.assertTrue(report["validation"]["insufficient_data"])
        self.assertFalse(report["validation"]["passed"])

    def test_passes_when_under_baseline_and_enough_samples(self) -> None:
        self._make_n_trajectories(50)
        # All `unchanged` -> harmfulness = 0; baseline 0.05 -> pass.
        report = audit_trajectories(
            self.path, self.policy, passthrough_reviewer,
            baseline_rate=0.05, min_trajectories=50,
        )
        self.assertFalse(report["validation"]["insufficient_data"])
        self.assertTrue(report["validation"]["passed"])
        self.assertEqual(report["validation"]["delta"], -0.05)

    def test_passes_at_exact_baseline_boundary(self) -> None:
        # 1 of 50 wrong -> harmfulness 0.02; baseline 0.02 -> ≤ is pass.
        self._make_n_trajectories(50)

        def reviewer(traj: Trajectory) -> ReviewerVerdict:
            if traj.id == "t000":
                return ReviewerVerdict(output="broken")
            return ReviewerVerdict(output=traj.base_agent_output)

        report = audit_trajectories(
            self.path, self.policy, reviewer,
            baseline_rate=0.02, min_trajectories=50,
        )
        self.assertEqual(report["harmfulness_rate"], 0.02)
        self.assertTrue(report["validation"]["passed"])

    def test_fails_when_above_baseline(self) -> None:
        self._make_n_trajectories(50)

        def reviewer(_t: Trajectory) -> ReviewerVerdict:
            return ReviewerVerdict(refused=True)

        report = audit_trajectories(
            self.path, self.policy, reviewer,
            baseline_rate=0.05, min_trajectories=50,
        )
        self.assertEqual(report["harmfulness_rate"], 1.0)
        self.assertFalse(report["validation"]["passed"])
        self.assertEqual(report["validation"]["delta"], 0.95)


# --- Malformed-input tests ----------------------------------------------


class MalformedTrajectoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        self.policy = _policy_with(("place_order", "always-review", None))

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_missing_directory_raises(self) -> None:
        missing = Path(self._tmp.name) / "does_not_exist"
        with self.assertRaisesRegex(FileNotFoundError, "trajectory directory"):
            audit_trajectories(missing, self.policy, passthrough_reviewer)

    def test_path_is_file_raises(self) -> None:
        f = self.path / "not_a_dir.json"
        f.write_text("{}")
        with self.assertRaisesRegex(NotADirectoryError, "not a directory"):
            audit_trajectories(f, self.policy, passthrough_reviewer)

    def test_malformed_json_raises(self) -> None:
        (self.path / "bad.json").write_text("this is not json")
        with self.assertRaisesRegex(ValueError, "malformed trajectory JSON"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)

    def test_json_array_root_rejected(self) -> None:
        (self.path / "bad.json").write_text("[1,2,3]")
        with self.assertRaisesRegex(ValueError, "not a JSON object"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)

    def test_missing_tool_name_rejected(self) -> None:
        (self.path / "bad.json").write_text(json.dumps({
            "base_agent_output": "ok", "expected_output": "ok",
        }))
        with self.assertRaisesRegex(ValueError, "'tool_name'"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)

    def test_missing_base_output_rejected(self) -> None:
        (self.path / "bad.json").write_text(json.dumps({
            "tool_name": "place_order", "expected_output": "ok",
        }))
        with self.assertRaisesRegex(ValueError, "'base_agent_output'"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)

    def test_missing_expected_output_rejected(self) -> None:
        (self.path / "bad.json").write_text(json.dumps({
            "tool_name": "place_order", "base_agent_output": "ok",
        }))
        with self.assertRaisesRegex(ValueError, "'expected_output'"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)

    def test_bool_confidence_rejected(self) -> None:
        # `bool` is an int-subclass — must be explicitly rejected.
        (self.path / "bad.json").write_text(json.dumps({
            "tool_name": "place_order",
            "base_agent_output": "ok", "expected_output": "ok",
            "base_agent_confidence": True,
        }))
        with self.assertRaisesRegex(ValueError, "'base_agent_confidence'"):
            audit_trajectories(self.path, self.policy, passthrough_reviewer)


# --- CLI integration ----------------------------------------------------


class CLITests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.workdir = Path(self._tmp.name)
        self.trajdir = self.workdir / "trajectories"
        self.trajdir.mkdir()
        self.policy_path = self.workdir / "policy.yaml"
        self.policy_path.write_text(textwrap.dedent("""\
            tools:
              place_order:
                bucket: always-review
              get_price:
                bucket: skip-review
        """))
        self.output = self.workdir / "report.json"
        _write_trajectory(
            self.trajdir, "t1", tool_name="place_order",
            base_output="ok", expected_output="ok",
        )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_cli_runs_and_writes_output(self) -> None:
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "passthrough",
            "--output", str(self.output),
        ])
        self.assertEqual(rc, 0)
        report = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertEqual(report["total"], 1)
        self.assertEqual(report["by_outcome"]["unchanged"], 1)
        # No baseline -> passed is None.
        self.assertIsNone(report["validation"]["passed"])

    def test_cli_exit_2_on_insufficient_data(self) -> None:
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "passthrough",
            "--baseline-rate", "0.10",
            "--min-trajectories", "50",
            "--output", str(self.output),
        ])
        self.assertEqual(rc, 2)

    def test_cli_exit_1_on_gate_failure(self) -> None:
        # Stub reviewer that refuses everything -> guaranteed gate failure.
        reviewer_module = self.workdir / "fake_reviewer.py"
        reviewer_module.write_text(textwrap.dedent("""\
            from conductor.reviewer.harmfulness_audit import ReviewerVerdict
            def reject(_traj):
                return ReviewerVerdict(refused=True)
        """))
        import sys as _sys
        _sys.path.insert(0, str(self.workdir))
        try:
            rc = main([
                str(self.trajdir),
                "--policy", str(self.policy_path),
                "--reviewer", "fake_reviewer:reject",
                "--baseline-rate", "0.10",
                "--min-trajectories", "1",  # tiny sample to bypass insufficient
                "--output", str(self.output),
            ])
        finally:
            _sys.path.remove(str(self.workdir))
            # Drop the module from the import cache so other tests are
            # not influenced.
            _sys.modules.pop("fake_reviewer", None)
        self.assertEqual(rc, 1)
        report = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertFalse(report["validation"]["passed"])

    def test_cli_exit_3_on_bad_input(self) -> None:
        (self.trajdir / "bad.json").write_text("not-json")
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "passthrough",
            "--output", str(self.output),
        ])
        self.assertEqual(rc, 3)

    def test_cli_exit_3_on_unresolvable_reviewer(self) -> None:
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "nonexistent.module:fn",
            "--output", str(self.output),
        ])
        self.assertEqual(rc, 3)

    def test_cli_exit_3_on_bad_reviewer_spec_format(self) -> None:
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "no-colon-here",
            "--output", str(self.output),
        ])
        self.assertEqual(rc, 3)

    def test_cli_creates_output_parent_directories(self) -> None:
        nested = self.workdir / "reports" / "daily" / "out.json"
        rc = main([
            str(self.trajdir),
            "--policy", str(self.policy_path),
            "--reviewer", "passthrough",
            "--output", str(nested),
        ])
        self.assertEqual(rc, 0)
        self.assertTrue(nested.exists())


if __name__ == "__main__":
    unittest.main()
