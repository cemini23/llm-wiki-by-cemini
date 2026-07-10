"""Tests for conductor.reviewer.corpus.build_context_bundle."""

from __future__ import annotations

import unittest
from pathlib import Path

from conductor.reviewer.corpus.build_context_bundle import (
    CORPUS_DIR,
    build_bundle,
)

BUNDLE_PATH = CORPUS_DIR / "context_bundle.md"


class BuildContextBundleTests(unittest.TestCase):
    def test_build_writes_bundle_with_all_manifest_ids(self) -> None:
        bundle, _ = build_bundle()
        self.assertIn("[trigger_policy]", bundle)
        self.assertIn("[reviewer_rubric]", bundle)
        self.assertIn("[ems_p0_gaps]", bundle)
        self.assertIn("[xsp_lane_framework]", bundle)
        self.assertIn("[xsp_regime_gate]", bundle)
        self.assertIn("[agent_guardrail_failure_modes]", bundle)
        self.assertIn("Permission laundering", bundle)
        self.assertIn("[igac_intent_scope]", bundle)
        self.assertIn("[mcp_execution_invariants]", bundle)
        self.assertIn("lane_id_contract", bundle)
        self.assertIn("refuse_only", bundle)
        self.assertIn("Helpfulness", bundle)
        self.assertTrue(bundle.startswith("<!-- bundle_sha256_prefix:"))

    def test_committed_bundle_matches_manifest(self) -> None:
        if not BUNDLE_PATH.is_file():
            self.skipTest("context_bundle.md not generated yet")
        expected, _ = build_bundle()
        actual = BUNDLE_PATH.read_text(encoding="utf-8")
        self.assertEqual(expected, actual, "context_bundle.md is stale — run build_reviewer_context.sh")


if __name__ == "__main__":
    unittest.main()
