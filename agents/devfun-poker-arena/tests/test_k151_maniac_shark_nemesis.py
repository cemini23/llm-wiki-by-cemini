"""K151 maniac_shark_lite_2 ladder nemesis seed tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from nemesis_seed import linear_aggro_nemesis_handles, nemesis_handles  # noqa: E402


def test_maniac_shark_in_default_nemesis_handles():
    assert "maniac_shark_lite_2" in nemesis_handles()


def test_maniac_shark_in_linear_aggro_nemesis():
    assert "maniac_shark_lite_2" in linear_aggro_nemesis_handles()


def test_maniac_shark_profile_archetype_is_linear_aggro():
    profile = json.loads(
        (
            ROOT / "research/opponents/maniac-shark-ladder-s1-profile.json"
        ).read_text(encoding="utf-8")
    )
    assert profile["archetype"] == "linear_aggro"
    assert profile["nemesis_actions"]["add_to_linear_aggro"] is True
    assert profile["h2h_vs_cemini_recent_50_replays"]["hero_bb_per_100"] < -100
