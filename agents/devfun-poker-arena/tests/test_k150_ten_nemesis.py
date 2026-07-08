"""K150 TEN ladder nemesis seed tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from nemesis_seed import linear_aggro_nemesis_handles, nemesis_handles  # noqa: E402


def test_ten_in_default_nemesis_handles():
    assert "ten" in nemesis_handles()


def test_ten_not_in_linear_aggro_nemesis():
    assert "ten" not in linear_aggro_nemesis_handles()


def test_ten_profile_archetype_is_wide_passive():
    profile = json.loads(
        (ROOT / "research/opponents/ten-ladder-s1-profile.json").read_text(encoding="utf-8")
    )
    assert profile["archetype"] == "wide_passive"
    assert profile["nemesis_actions"]["add_to_linear_aggro"] is False
    assert profile["h2h_vs_cemini_recent_100"]["hero_bb_per_100"] < -100
