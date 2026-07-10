"""Unit tests for conductor.reviewer.lane_contract."""

from __future__ import annotations

import unittest
from pathlib import Path

from conductor.reviewer.lane_contract import (
    LaneContractError,
    LaneAutomationPosture,
    default_lane_contract,
    extract_lane_id,
    load_lane_contract_from_policy,
    validate_provisional_call,
)

POLICY = Path(__file__).parent / "policy.yaml"


class LaneContractTests(unittest.TestCase):
    def test_policy_yaml_lane_contract_loads(self) -> None:
        contract = load_lane_contract_from_policy(POLICY)
        self.assertEqual(contract.version, 1)
        self.assertIn("lane_a", contract.allowed_ids())
        self.assertIn("smb_put_credit", contract.allowed_ids())

    def test_extract_lane_id_aliases(self) -> None:
        self.assertEqual(extract_lane_id({"lane_id": "lane_a"}), "lane_a")
        self.assertEqual(extract_lane_id({"strategy_track": "lane_b"}), "lane_b")
        self.assertIsNone(extract_lane_id({}))

    def test_missing_lane_id_on_place_order_raises(self) -> None:
        with self.assertRaises(LaneContractError) as ctx:
            validate_provisional_call("place_order", {})
        self.assertIn("requires lane_id", str(ctx.exception))

    def test_unknown_lane_id_raises(self) -> None:
        with self.assertRaises(LaneContractError):
            validate_provisional_call("place_order", {"lane_id": "lane_z"})

    def test_lane_a_automated_place_order_refused_at_contract(self) -> None:
        with self.assertRaises(LaneContractError) as ctx:
            validate_provisional_call("place_order", {"lane_id": "lane_a"})
        self.assertIn("exit monitor only", str(ctx.exception))

    def test_lane_b_automated_place_order_refused(self) -> None:
        with self.assertRaises(LaneContractError) as ctx:
            validate_provisional_call("place_order", {"lane_id": "lane_b"})
        self.assertIn("manual entry", str(ctx.exception))

    def test_smb_put_credit_place_order_refused(self) -> None:
        with self.assertRaises(LaneContractError) as ctx:
            validate_provisional_call("place_order", {"lane_id": "smb_put_credit"})
        self.assertIn("not automated", str(ctx.exception))

    def test_lane_a_close_position_allowed(self) -> None:
        definition = validate_provisional_call(
            "close_position", {"lane_id": "lane_a"},
        )
        self.assertEqual(definition.lane_id, "lane_a")
        self.assertIs(definition.automation_v1, LaneAutomationPosture.EXIT_ONLY)

    def test_get_price_skips_lane_requirement(self) -> None:
        validate_provisional_call("get_price", None)

    def test_manual_place_order_allowed(self) -> None:
        definition = validate_provisional_call(
            "place_order", {"lane_id": "manual"},
        )
        self.assertEqual(definition.lane_id, "manual")

    def test_reviewer_mandate_non_empty(self) -> None:
        contract = default_lane_contract()
        self.assertGreaterEqual(len(contract.reviewer_mandate), 5)


if __name__ == "__main__":
    unittest.main()
