"""Unit tests for ``conductor.reviewer.trigger_policy``.

Covers the six scenarios enumerated in the spec
(``openspec/changes/reviewer-agent-selective-trigger/specs/.../spec.md``)
plus three defensive invariants:

  1. Side-effecting tool (always-review bucket) -> ALWAYS_REVIEW
  2. Read-only tool (skip-review bucket) -> SKIP_REVIEW
  3. Unclassified tool -> ALWAYS_REVIEW (safe-default)
  4. Review-on-uncertainty, confidence >= threshold -> SKIP_REVIEW
  5. Review-on-uncertainty, confidence <  threshold -> ALWAYS_REVIEW
  6. Review-on-uncertainty, confidence missing      -> ALWAYS_REVIEW (safe-default)

Defensive invariants:
  - classify() never returns REVIEW_ON_UNCERTAINTY (terminal-route guarantee)
  - tool_args is structurally accepted but does not affect routing
  - REVIEW_ON_UNCERTAINTY without a threshold escalates (misconfig guard)
"""

from __future__ import annotations

import unittest

from conductor.reviewer.trigger_policy import Bucket, Policy, ToolEntry, classify


def _make_default_policy() -> Policy:
    """Reference policy mirroring the default Polymarket tool surfaces.

    See Task 2.2 in tasks.md for the canonical default bucket assignments.
    """
    return Policy(
        tools={
            # Side-effecting -> always-review
            "place_order": ToolEntry(bucket=Bucket.ALWAYS_REVIEW),
            "withdraw": ToolEntry(bucket=Bucket.ALWAYS_REVIEW),
            "close_position": ToolEntry(bucket=Bucket.ALWAYS_REVIEW),
            "cancel_order": ToolEntry(bucket=Bucket.ALWAYS_REVIEW),
            # Read-only -> skip-review
            "get_price": ToolEntry(bucket=Bucket.SKIP_REVIEW),
            "get_orderbook": ToolEntry(bucket=Bucket.SKIP_REVIEW),
            "get_news": ToolEntry(bucket=Bucket.SKIP_REVIEW),
            # Ambiguous -> review-on-uncertainty with 0.7 threshold
            "submit_research_query": ToolEntry(
                bucket=Bucket.REVIEW_ON_UNCERTAINTY,
                threshold=0.7,
            ),
        }
    )


class TriggerPolicyScenarioTests(unittest.TestCase):
    """Six scenarios enumerated by the trigger-policy spec."""

    def setUp(self) -> None:
        self.policy = _make_default_policy()

    # --- Scenario 1: side-effecting tool always reviewed ---------------------

    def test_scenario_1_place_order_routes_to_always_review(self) -> None:
        self.assertIs(
            classify("place_order", None, self.policy, base_agent_confidence=0.99),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_1_withdraw_routes_to_always_review(self) -> None:
        self.assertIs(
            classify("withdraw", None, self.policy, base_agent_confidence=None),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_1_close_position_routes_to_always_review(self) -> None:
        self.assertIs(
            classify("close_position", None, self.policy, base_agent_confidence=0.5),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_1_cancel_order_routes_to_always_review(self) -> None:
        self.assertIs(
            classify("cancel_order", None, self.policy, base_agent_confidence=1.0),
            Bucket.ALWAYS_REVIEW,
        )

    # --- Scenario 2: read-only tool skipped ----------------------------------

    def test_scenario_2_get_price_routes_to_skip_review(self) -> None:
        self.assertIs(
            classify("get_price", None, self.policy, base_agent_confidence=0.5),
            Bucket.SKIP_REVIEW,
        )

    def test_scenario_2_get_orderbook_skips_even_with_low_confidence(self) -> None:
        # Skip-review tools bypass review regardless of confidence value.
        self.assertIs(
            classify("get_orderbook", None, self.policy, base_agent_confidence=0.01),
            Bucket.SKIP_REVIEW,
        )

    def test_scenario_2_get_news_skips_with_missing_confidence(self) -> None:
        self.assertIs(
            classify("get_news", None, self.policy, base_agent_confidence=None),
            Bucket.SKIP_REVIEW,
        )

    # --- Scenario 3: unclassified tool defaults to always-review -------------

    def test_scenario_3_unclassified_tool_routes_to_always_review(self) -> None:
        self.assertIs(
            classify("brand_new_tool", None, self.policy, base_agent_confidence=0.99),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_3_unclassified_default_independent_of_confidence(self) -> None:
        # Even with maxed confidence, unknown tools never silently skip.
        self.assertIs(
            classify("unknown", None, self.policy, base_agent_confidence=1.0),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_3_unclassified_with_missing_confidence(self) -> None:
        self.assertIs(
            classify("unknown", None, self.policy, base_agent_confidence=None),
            Bucket.ALWAYS_REVIEW,
        )

    # --- Scenario 4: review-on-uncertainty with confidence >= threshold ------

    def test_scenario_4_confidence_above_threshold_skips(self) -> None:
        # threshold=0.7, confidence=0.85 -> SKIP
        self.assertIs(
            classify(
                "submit_research_query",
                None,
                self.policy,
                base_agent_confidence=0.85,
            ),
            Bucket.SKIP_REVIEW,
        )

    def test_scenario_4_confidence_at_threshold_skips(self) -> None:
        # Strict-less-than escalation: confidence == threshold -> SKIP.
        self.assertIs(
            classify(
                "submit_research_query",
                None,
                self.policy,
                base_agent_confidence=0.7,
            ),
            Bucket.SKIP_REVIEW,
        )

    # --- Scenario 5: review-on-uncertainty with confidence < threshold -------

    def test_scenario_5_confidence_below_threshold_escalates(self) -> None:
        # threshold=0.7, confidence=0.5 -> ALWAYS_REVIEW
        self.assertIs(
            classify(
                "submit_research_query",
                None,
                self.policy,
                base_agent_confidence=0.5,
            ),
            Bucket.ALWAYS_REVIEW,
        )

    def test_scenario_5_confidence_just_below_threshold_escalates(self) -> None:
        # Boundary case: confidence one epsilon below threshold -> ALWAYS_REVIEW.
        self.assertIs(
            classify(
                "submit_research_query",
                None,
                self.policy,
                base_agent_confidence=0.69,
            ),
            Bucket.ALWAYS_REVIEW,
        )

    # --- Scenario 6: review-on-uncertainty with missing confidence -----------

    def test_scenario_6_missing_confidence_escalates(self) -> None:
        # Spec safe-default: absent confidence treated as below-threshold.
        self.assertIs(
            classify(
                "submit_research_query",
                None,
                self.policy,
                base_agent_confidence=None,
            ),
            Bucket.ALWAYS_REVIEW,
        )


class TriggerPolicyInvariantTests(unittest.TestCase):
    """Defensive invariants beyond the six spec scenarios."""

    def setUp(self) -> None:
        self.policy = _make_default_policy()

    def test_classify_never_returns_review_on_uncertainty(self) -> None:
        """``classify`` always reduces REVIEW_ON_UNCERTAINTY to a terminal route."""
        confidences = (None, 0.0, 0.3, 0.69, 0.7, 0.71, 1.0)
        tools = (
            "place_order",
            "get_price",
            "submit_research_query",
            "unknown_tool",
        )
        for tool in tools:
            for confidence in confidences:
                with self.subTest(tool=tool, confidence=confidence):
                    result = classify(
                        tool, None, self.policy, base_agent_confidence=confidence,
                    )
                    self.assertIn(
                        result,
                        {Bucket.ALWAYS_REVIEW, Bucket.SKIP_REVIEW},
                        msg=f"classify returned non-terminal {result!r}",
                    )

    def test_tool_args_does_not_affect_routing(self) -> None:
        """``tool_args`` is reserved for arg-conditional rules; currently no-op."""
        no_args = classify(
            "get_price", None, self.policy, base_agent_confidence=0.5,
        )
        with_args = classify(
            "get_price",
            {"ticker": "AAPL", "size": 100},
            self.policy,
            base_agent_confidence=0.5,
        )
        self.assertIs(no_args, with_args)

    def test_review_on_uncertainty_without_threshold_escalates(self) -> None:
        """Misconfigured policy (ROU bucket, no threshold) must NOT silently skip."""
        misconfigured = Policy(
            tools={
                "ambiguous_tool": ToolEntry(
                    bucket=Bucket.REVIEW_ON_UNCERTAINTY,
                    threshold=None,
                ),
            }
        )
        # Even with max confidence, ROU-without-threshold escalates.
        self.assertIs(
            classify(
                "ambiguous_tool",
                None,
                misconfigured,
                base_agent_confidence=0.99,
            ),
            Bucket.ALWAYS_REVIEW,
        )

    def test_empty_policy_routes_every_tool_to_always_review(self) -> None:
        """Empty policy must behave as v1 always-review for every tool."""
        empty = Policy()
        for tool in ("place_order", "get_price", "anything"):
            with self.subTest(tool=tool):
                self.assertIs(
                    classify(tool, None, empty, base_agent_confidence=0.99),
                    Bucket.ALWAYS_REVIEW,
                )

    def test_bucket_enum_string_values_match_yaml_representation(self) -> None:
        """Bucket string values must round-trip with the YAML policy file."""
        self.assertEqual(Bucket.ALWAYS_REVIEW.value, "always-review")
        self.assertEqual(Bucket.REVIEW_ON_UNCERTAINTY.value, "review-on-uncertainty")
        self.assertEqual(Bucket.SKIP_REVIEW.value, "skip-review")


if __name__ == "__main__":
    unittest.main()
