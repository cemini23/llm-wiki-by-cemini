"""K152 yardstick pool config smoke tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from researcher_trajectory_summary import load_yardstick_pool_config  # noqa: E402

POOL_PATH = ROOT / "config" / "hu_yardstick_pool.json"
REQUIRED_HANDLES = ("ten", "maniac_shark_lag", "tight", "lag")


def test_hu_yardstick_pool_json_loads():
    data = json.loads(POOL_PATH.read_text(encoding="utf-8"))
    assert data["schema"] == "devfun.hu_yardstick_pool.v1"
    assert data["never_train"] is True


def test_hu_yardstick_pool_required_handles():
    cfg = load_yardstick_pool_config(POOL_PATH)
    opponents = cfg.get("opponents") or {}
    for handle in REQUIRED_HANDLES:
        assert handle in opponents, f"missing yardstick handle: {handle}"
        assert "min_bb100" in opponents[handle]


def test_hu_yardstick_pool_notes_license_blocker():
    cfg = load_yardstick_pool_config(POOL_PATH)
    notes = str(cfg.get("notes") or "").lower()
    assert "no license" in notes
    assert "never_train" in cfg and cfg["never_train"] is True
