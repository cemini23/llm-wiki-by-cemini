"""K250/K253 — canary trap classification + persist/pivot decisions."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from canary_tool_diagnosis import (  # noqa: E402
    TRAP_CAPABILITY_MIRAGE,
    TRAP_GRANULARITY_TRAP,
    TRAP_PARAMETER_TRAP,
    TRAP_PREREQUISITE_BLINDNESS,
    TRAP_SEMANTIC_DECOY,
    TRAP_TEMPORAL_DECOY,
    classify_trap,
)
from persist_pivot import should_persist, should_pivot  # noqa: E402


def test_classify_semantic_decoy():
    assert classify_trap("tool named like the real solver but is a decoy") == TRAP_SEMANTIC_DECOY


def test_classify_parameter_trap():
    assert classify_trap("right tool but wrong parameter settings") == TRAP_PARAMETER_TRAP


def test_classify_capability_mirage():
    assert classify_trap("premium advanced solver overclaims its capability") == TRAP_CAPABILITY_MIRAGE


def test_classify_prerequisite_blindness():
    assert classify_trap("solver requires a missing dependency before running") == TRAP_PREREQUISITE_BLINDNESS


def test_classify_temporal_decoy():
    assert classify_trap("deprecated stale version of the helper") == TRAP_TEMPORAL_DECOY


def test_classify_granularity_trap():
    assert classify_trap("granularity too coarse for this street") == TRAP_GRANULARITY_TRAP


def test_classify_unknown_fail_open():
    assert classify_trap("") is None
    assert classify_trap(None) is None
    assert classify_trap("some unrelated description") is None


def test_should_persist_only_when_both_ok():
    assert should_persist(True, True) is True
    assert should_persist(False, True) is False
    assert should_persist(True, False) is False
    assert should_persist(False, False) is False


def test_should_pivot_on_evidence_failure():
    assert should_pivot(False) is True
    assert should_pivot(True) is False


def test_docs_mention_k_ids():
    refs = Path(__file__).resolve().parent.parent / "references"
    canary = (refs / "canary-tool-selection.md").read_text(encoding="utf-8")
    persist = (refs / "persist-pivot-review.md").read_text(encoding="utf-8")
    assert "K250" in canary
    assert "K253" in persist
