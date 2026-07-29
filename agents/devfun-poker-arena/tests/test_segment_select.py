"""K144 segment_select_cap tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from cemini_hl_brief import segment_select_cap  # noqa: E402


def test_segment_select_cap_ranks_by_tag_overlap():
    segments = [
        {"id": "a", "tags": ["flop", "dry"], "text": "unrelated"},
        {"id": "b", "tags": ["turn", "leak"], "text": "turn barrel leak"},
        {"id": "c", "tags": ["turn"], "text": "minor note"},
    ]
    kept, dropped = segment_select_cap(segments, ["turn", "leak"], cap=2)
    assert len(kept) == 2
    assert len(dropped) == 1
    assert kept[0]["id"] == "b"
    assert dropped[0]["id"] in {"a", "c"}


def test_segment_select_cap_default_cap_eight():
    segments = [{"id": f"s{i}", "tags": [], "text": f"line {i}"} for i in range(12)]
    kept, dropped = segment_select_cap(segments, ["line"], cap=None)
    assert len(kept) == 8
    assert len(dropped) == 4


def test_segment_select_cap_keeps_all_when_under_cap():
    segments = [{"id": "x", "tags": ["leak"], "text": "one"}]
    kept, dropped = segment_select_cap(segments, ["leak"], cap=5)
    assert kept == segments
    assert dropped == []
