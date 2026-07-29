"""K199/K201 solver context prune + grounded tag."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from solver_context_prune import assert_solver_grounded, prune_solver_context  # noqa: E402


def test_prune_caps_keys_and_strings():
    big = {f"k{i}": "x" * 1000 for i in range(30)}
    out = prune_solver_context(big, max_keys=5, max_str=50)
    assert isinstance(out, dict)
    assert len([k for k in out if not k.startswith("_")]) == 5
    assert "_truncated" in out
    sample = next(v for k, v in out.items() if k != "_truncated")
    assert isinstance(sample, str) and sample.endswith("...")


def test_solver_grounded_trusted_source():
    g = assert_solver_grounded({"ev": 0.12}, source="postflop_hu_buckets")
    assert g["trusted"] is True
    assert assert_solver_grounded({"ev": 0.1}, source="llm")["trusted"] is False
