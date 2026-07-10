"""Unit tests for ``conductor.reviewer.policy_loader``.

Covers loading, schema validation, fail-closed parse errors, fail-open
missing-file fallback, and the side-effecting lint pass — plus an
integration check that the bundled ``policy.yaml`` parses cleanly and
passes lint.

See spec.md "Declarative policy file" requirement and tasks.md 2.1 / 2.3 / 2.4.
"""

from __future__ import annotations

import logging
import tempfile
import textwrap
import unittest
from pathlib import Path

from conductor.reviewer.policy_loader import (
    SIDE_EFFECTING_PATTERNS,
    PolicyParseError,
    lint_policy,
    load_policy,
    load_policy_or_default,
)
from conductor.reviewer.trigger_policy import Bucket, Policy, ToolEntry


def _write_yaml(content: str) -> Path:
    """Write YAML content to a NamedTemporaryFile and return its Path."""
    f = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, encoding="utf-8",
    )
    try:
        f.write(textwrap.dedent(content))
    finally:
        f.close()
    return Path(f.name)


class LoadPolicyHappyPathTests(unittest.TestCase):
    """Valid YAML → expected Policy."""

    def test_minimal_valid_policy_parses(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order:
                bucket: always-review
            """
        )
        try:
            policy = load_policy(path)
        finally:
            path.unlink()
        self.assertIn("place_order", policy.tools)
        self.assertIs(policy.tools["place_order"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIsNone(policy.tools["place_order"].threshold)
        self.assertIsNone(policy.tools["place_order"].notes)

    def test_all_three_buckets_parse(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order:
                bucket: always-review
                notes: side-effecting
              get_price:
                bucket: skip-review
                notes: read-only
              submit_research_query:
                bucket: review-on-uncertainty
                uncertainty_threshold: 0.7
                notes: cost-bearing
            """
        )
        try:
            policy = load_policy(path)
        finally:
            path.unlink()
        self.assertIs(policy.tools["place_order"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIs(policy.tools["get_price"].bucket, Bucket.SKIP_REVIEW)
        rou = policy.tools["submit_research_query"]
        self.assertIs(rou.bucket, Bucket.REVIEW_ON_UNCERTAINTY)
        self.assertEqual(rou.threshold, 0.7)
        self.assertEqual(rou.notes, "cost-bearing")

    def test_empty_file_parses_as_empty_policy(self) -> None:
        path = _write_yaml("")
        try:
            policy = load_policy(path)
        finally:
            path.unlink()
        self.assertEqual(dict(policy.tools), {})

    def test_tools_key_omitted_parses_as_empty_policy(self) -> None:
        path = _write_yaml(
            """
            # tools key intentionally omitted; valid YAML but empty schema
            schema_version: 1
            """
        )
        try:
            policy = load_policy(path)
        finally:
            path.unlink()
        self.assertEqual(dict(policy.tools), {})

    def test_integer_threshold_coerced_to_float(self) -> None:
        path = _write_yaml(
            """
            tools:
              t:
                bucket: review-on-uncertainty
                uncertainty_threshold: 1
            """
        )
        try:
            policy = load_policy(path)
        finally:
            path.unlink()
        self.assertEqual(policy.tools["t"].threshold, 1.0)
        self.assertIsInstance(policy.tools["t"].threshold, float)


class LoadPolicyMissingFileTests(unittest.TestCase):
    """load_policy raises; load_policy_or_default falls back + warns."""

    def test_load_policy_missing_file_raises(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_policy("/nonexistent/path/policy.yaml")

    def test_load_policy_or_default_missing_file_returns_empty_policy(self) -> None:
        # assertLogs captures the WARNING. Empty policy is correct fallback.
        with self.assertLogs(
            "conductor.reviewer.policy_loader", level="WARNING",
        ) as cm:
            policy = load_policy_or_default("/nonexistent/path/policy.yaml")
        self.assertEqual(dict(policy.tools), {})
        # Verify the warning message mentions fallback behavior.
        self.assertTrue(
            any("v1 always-review" in msg for msg in cm.output),
            f"expected fallback warning, got: {cm.output}",
        )


class LoadPolicyParseErrorTests(unittest.TestCase):
    """Malformed YAML / schema violations → PolicyParseError (fail-closed)."""

    def test_malformed_yaml_raises_parse_error(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order
                bucket: always-review  # missing colon above
            """
        )
        try:
            with self.assertRaises(PolicyParseError):
                load_policy(path)
        finally:
            path.unlink()

    def test_top_level_non_mapping_raises(self) -> None:
        path = _write_yaml(
            """
            - this
            - is
            - a list
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "top-level YAML must be a mapping"):
                load_policy(path)
        finally:
            path.unlink()

    def test_tools_non_mapping_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              - place_order
              - get_price
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "'tools' must be a mapping"):
                load_policy(path)
        finally:
            path.unlink()

    def test_missing_bucket_field_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order:
                notes: forgot the bucket
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "missing required string field 'bucket'"):
                load_policy(path)
        finally:
            path.unlink()

    def test_invalid_bucket_value_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order:
                bucket: maybe-review
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "unknown bucket 'maybe-review'"):
                load_policy(path)
        finally:
            path.unlink()

    def test_review_on_uncertainty_without_threshold_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              ambig:
                bucket: review-on-uncertainty
                # missing uncertainty_threshold
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "no 'uncertainty_threshold' was set"):
                load_policy(path)
        finally:
            path.unlink()

    def test_threshold_out_of_range_raises(self) -> None:
        for bad in (-0.1, 1.1, 2.0):
            path = _write_yaml(
                f"""
                tools:
                  t:
                    bucket: review-on-uncertainty
                    uncertainty_threshold: {bad}
                """
            )
            try:
                with self.subTest(threshold=bad):
                    with self.assertRaisesRegex(PolicyParseError, "must be in"):
                        load_policy(path)
            finally:
                path.unlink()

    def test_non_numeric_threshold_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              t:
                bucket: review-on-uncertainty
                uncertainty_threshold: "high"
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "must be numeric"):
                load_policy(path)
        finally:
            path.unlink()

    def test_bool_threshold_rejected(self) -> None:
        # bool is an int subclass in Python; we explicitly reject it.
        path = _write_yaml(
            """
            tools:
              t:
                bucket: review-on-uncertainty
                uncertainty_threshold: true
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "must be numeric"):
                load_policy(path)
        finally:
            path.unlink()

    def test_unknown_field_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              place_order:
                bucket: always-review
                priority: critical  # typo / unknown field
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "unknown field"):
                load_policy(path)
        finally:
            path.unlink()

    def test_non_string_notes_raises(self) -> None:
        path = _write_yaml(
            """
            tools:
              t:
                bucket: always-review
                notes: 123
            """
        )
        try:
            with self.assertRaisesRegex(PolicyParseError, "notes must be string"):
                load_policy(path)
        finally:
            path.unlink()


class LintPolicyTests(unittest.TestCase):
    """Side-effecting lint pass surfaces likely misconfigurations."""

    def test_clean_policy_yields_no_warnings(self) -> None:
        clean = Policy(
            tools={
                "place_order": ToolEntry(bucket=Bucket.ALWAYS_REVIEW),
                "get_price": ToolEntry(bucket=Bucket.SKIP_REVIEW),
                "submit_research_query": ToolEntry(
                    bucket=Bucket.REVIEW_ON_UNCERTAINTY, threshold=0.7,
                ),
            }
        )
        self.assertEqual(lint_policy(clean), [])

    def test_place_order_as_skip_review_warns(self) -> None:
        bad = Policy(
            tools={"place_order": ToolEntry(bucket=Bucket.SKIP_REVIEW)}
        )
        warnings = lint_policy(bad)
        self.assertEqual(len(warnings), 1)
        self.assertIn("place_order", warnings[0])
        self.assertIn("place_*", warnings[0])
        self.assertIn("skip-review", warnings[0])

    def test_each_side_effecting_pattern_detected(self) -> None:
        # One representative tool per pattern.
        bad = Policy(
            tools={
                "place_market_order": ToolEntry(bucket=Bucket.SKIP_REVIEW),
                "withdraw_funds": ToolEntry(bucket=Bucket.SKIP_REVIEW),
                "cancel_pending": ToolEntry(bucket=Bucket.SKIP_REVIEW),
                "close_all_positions": ToolEntry(bucket=Bucket.SKIP_REVIEW),
            }
        )
        warnings = lint_policy(bad)
        self.assertEqual(len(warnings), 4)
        # All four patterns should be referenced across the warnings.
        joined = " ".join(warnings)
        for pattern in SIDE_EFFECTING_PATTERNS:
            self.assertIn(pattern, joined)

    def test_skip_review_for_non_matching_tool_does_not_warn(self) -> None:
        ok = Policy(
            tools={"get_price": ToolEntry(bucket=Bucket.SKIP_REVIEW)}
        )
        self.assertEqual(lint_policy(ok), [])

    def test_side_effecting_as_always_review_does_not_warn(self) -> None:
        # The lint pass only fires on skip-review + matching pattern;
        # always-review for a side-effecting tool is the correct config.
        ok = Policy(
            tools={"place_order": ToolEntry(bucket=Bucket.ALWAYS_REVIEW)}
        )
        self.assertEqual(lint_policy(ok), [])

    def test_side_effecting_as_review_on_uncertainty_does_not_warn(self) -> None:
        # ROU is also acceptable for side-effecting tools (operator's
        # call); lint only flags the silent-skip case.
        ok = Policy(
            tools={
                "place_order": ToolEntry(
                    bucket=Bucket.REVIEW_ON_UNCERTAINTY, threshold=0.95,
                ),
            }
        )
        self.assertEqual(lint_policy(ok), [])


class BundledPolicyIntegrationTests(unittest.TestCase):
    """The bundled default ``policy.yaml`` must load + lint cleanly."""

    BUNDLED = Path(__file__).parent / "policy.yaml"

    def test_bundled_policy_exists(self) -> None:
        self.assertTrue(
            self.BUNDLED.exists(),
            f"expected bundled policy at {self.BUNDLED}",
        )

    def test_bundled_policy_loads(self) -> None:
        policy = load_policy(self.BUNDLED)
        # Sanity-check a few canonical tools from tasks.md 2.2.
        self.assertIs(policy.tools["place_order"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIs(policy.tools["withdraw"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIs(policy.tools["close_position"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIs(policy.tools["cancel_order"].bucket, Bucket.ALWAYS_REVIEW)
        self.assertIs(policy.tools["get_price"].bucket, Bucket.SKIP_REVIEW)
        self.assertIs(policy.tools["get_regime_status"].bucket, Bucket.SKIP_REVIEW)
        self.assertIs(policy.tools["get_playbook_snapshot"].bucket, Bucket.SKIP_REVIEW)
        notify = policy.tools["notify_operator"]
        self.assertIs(notify.bucket, Bucket.ALWAYS_REVIEW)

    def test_bundled_policy_passes_lint(self) -> None:
        policy = load_policy(self.BUNDLED)
        self.assertEqual(
            lint_policy(policy), [],
            "bundled policy.yaml must not produce lint warnings",
        )


if __name__ == "__main__":
    # Suppress the WARNING from load_policy_or_default test during
    # normal stdout reading; assertLogs in that test still captures it.
    logging.disable(logging.CRITICAL)
    unittest.main()
