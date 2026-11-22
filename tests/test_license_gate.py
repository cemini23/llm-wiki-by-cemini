"""Tests for scripts/license_gate.py.

The module is loaded by path so the test does not depend on `scripts/` being on
sys.path.
"""

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODULE_PATH = REPO / "scripts" / "license_gate.py"

spec = importlib.util.spec_from_file_location("license_gate_under_test", MODULE_PATH)
license_gate = importlib.util.module_from_spec(spec)
# dataclasses resolves annotations through sys.modules, so register first.
sys.modules[spec.name] = license_gate
spec.loader.exec_module(license_gate)


def test_minimax_noncommercial_blocks_integrate():
    result = license_gate.gate("MiniMax-M2.7 Non-Commercial", "integrate")
    assert result.verdict == "BLOCK"
    assert result.exit_code == 2


def test_agpl_blocks_integrate_but_reviews_paper_only():
    integrate = license_gate.gate("AGPL-3.0", "integrate")
    assert integrate.verdict == "BLOCK"
    assert integrate.exit_code == 2

    paper_only = license_gate.gate("AGPL-3.0", "paper-only")
    assert paper_only.verdict == "REVIEW"
    assert paper_only.exit_code == 0


def test_mit_allows():
    result = license_gate.gate("MIT", "integrate")
    assert result.verdict == "ALLOW"
    assert result.exit_code == 0


def test_lgpl_is_review_not_blocked():
    assert license_gate.classify("LGPL-3.0") == "review"
