"""UI snapshot bb/100 merge (S1a ephemeral column)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_bundle import apply_bb100_snapshot, bb100_snapshot_index, load_export_agents_with_bb100  # noqa: E402


FIXTURE = Path(__file__).parent / "fixtures" / "bb100_ui_snapshot_s1a_2026-06-08.json"


def test_bb100_snapshot_index():
    snap = json.loads(FIXTURE.read_text(encoding="utf-8"))
    idx = bb100_snapshot_index(snap)
    assert idx["cemini_wiki_poker"] == pytest.approx(2820.1)
    assert idx["0xjeff_ai"] == pytest.approx(3670.3)


def test_apply_bb100_snapshot_merges_hero(tmp_path: Path):
    snap = json.loads(FIXTURE.read_text(encoding="utf-8"))
    (tmp_path / "agents.jsonl").write_text(
        json.dumps(
            {
                "record_type": "agent",
                "handle": "cemini_wiki_poker",
                "name": "Cemini Wiki Poker",
                "rank": 1,
                "chips": 139927,
                "hands": 2283,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (tmp_path / "bb100_ui_snapshot.json").write_text(
        FIXTURE.read_text(encoding="utf-8"), encoding="utf-8"
    )
    merged = apply_bb100_snapshot(tmp_path, snap)
    hero = next(a for a in merged if a.get("handle") == "cemini_wiki_poker")
    assert hero["adjusted_bb100"] == pytest.approx(2820.1)
    assert hero["adjusted_bb100_source"] == "ui_snapshot"
    assert (tmp_path / "agents_bb100_enriched.jsonl").is_file()

    via_loader = load_export_agents_with_bb100(tmp_path)
    hero2 = next(a for a in via_loader if a.get("handle") == "cemini_wiki_poker")
    assert hero2["adjusted_bb100"] == pytest.approx(2820.1)
