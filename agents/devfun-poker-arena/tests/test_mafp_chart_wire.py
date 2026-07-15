"""WP1 — CEMINI_MAFP_CHART runtime wire for research_static_chart."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from research_static_chart import (  # noqa: E402
    _reset_mafp_overlay_cache,
    load_mafp_chart_ranges,
    research_static_chart,
    resolve_mafp_chart_path,
)


def _hu_table(hole: list[str], *, seat: int = 1, street: str = "Preflop") -> dict:
    """Minimal HU table: seat 1 = BTN, seat 2 = BB."""
    return {
        "street": street,
        "selfSeatNumber": seat,
        "buttonSeatNumber": 1,
        "smallBlindChips": 10,
        "bigBlindChips": 20,
        "seats": [
            {"seatNumber": 1, "holeCards": hole if seat == 1 else ["2c", "3d"], "status": "Active"},
            {"seatNumber": 2, "holeCards": hole if seat == 2 else ["7h", "2s"], "status": "Active"},
        ],
        "tableFormat": "hu",
    }


@pytest.fixture(autouse=True)
def _isolate_mafp_env(monkeypatch):
    """Reset cache + clear MAFP env between tests."""
    monkeypatch.delenv("CEMINI_MAFP_CHART", raising=False)
    monkeypatch.delenv("CEMINI_MAFP_CHART_PATH", raising=False)
    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    _reset_mafp_overlay_cache()
    yield
    _reset_mafp_overlay_cache()
    monkeypatch.delenv("CEMINI_MAFP_CHART", raising=False)
    monkeypatch.delenv("CEMINI_MAFP_CHART_PATH", raising=False)


def test_flag_off_static_chart_unchanged(monkeypatch):
    monkeypatch.setenv("CEMINI_MAFP_CHART", "0")
    # 32s is fold on static BTN; MAFP raises it — flag off must stay fold.
    out = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    assert out["preflop_action"] == "fold"
    assert out["hand_class"] == "32s"
    assert "mafp" not in out.get("source", "")


def test_flag_on_temp_chart_flips_cell(monkeypatch, tmp_path):
    chart_path = tmp_path / "mafp_hu_chart.json"
    chart_path.write_text(
        json.dumps(
            {
                "schema": "mafp-hu-chart-v1",
                "ranges": {"BTN": {"32s": "raise"}},
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(chart_path))
    _reset_mafp_overlay_cache()

    flipped = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    assert flipped["preflop_action"] == "raise"
    assert flipped["hand_class"] == "32s"

    # Unrelated strong hand still raise (overlay only touches listed cells for action change).
    aa = research_static_chart(_hu_table(["As", "Ah"], seat=1))
    assert aa["preflop_action"] == "raise"


def test_flag_on_fold_overlay(monkeypatch, tmp_path):
    """Overlay can demote a raise cell to fold."""
    chart_path = tmp_path / "mafp_fold.json"
    chart_path.write_text(
        json.dumps({"ranges": {"BTN": {"K4s": "fold"}}}),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(chart_path))
    _reset_mafp_overlay_cache()

    # Static BTN K4s is raise; overlay fold → fold.
    out = research_static_chart(_hu_table(["Ks", "4s"], seat=1))
    assert out["preflop_action"] == "fold"


def test_missing_file_fail_open(monkeypatch, tmp_path):
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(tmp_path / "does_not_exist.json"))
    _reset_mafp_overlay_cache()

    out = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    assert out["preflop_action"] == "fold"  # static baseline
    # No exception; still returns a well-formed dict.
    assert out["hand_class"] == "32s"


def test_unparseable_file_fail_open(monkeypatch, tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not json", encoding="utf-8")
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(bad))
    _reset_mafp_overlay_cache()

    out = research_static_chart(_hu_table(["As", "Ks"], seat=1))
    assert out["preflop_action"] == "raise"
    assert load_mafp_chart_ranges(bad) is None


def test_loader_idempotent(monkeypatch, tmp_path):
    chart_path = tmp_path / "mafp.json"
    chart_path.write_text(
        json.dumps({"ranges": {"BTN": {"32s": "raise"}}}),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(chart_path))
    _reset_mafp_overlay_cache()

    a = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    b = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    c = research_static_chart(_hu_table(["3s", "2s"], seat=1))
    assert a == b == c
    assert a["preflop_action"] == "raise"


def test_truthy_flag_variants(monkeypatch, tmp_path):
    chart_path = tmp_path / "mafp.json"
    chart_path.write_text(
        json.dumps({"ranges": {"BTN": {"32s": "raise"}}}),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(chart_path))
    for val in ("1", "true", "YES", "on"):
        monkeypatch.setenv("CEMINI_MAFP_CHART", val)
        _reset_mafp_overlay_cache()
        out = research_static_chart(_hu_table(["3s", "2s"], seat=1))
        assert out["preflop_action"] == "raise", val


def test_resolve_path_prefers_env_override(monkeypatch, tmp_path):
    p = tmp_path / "custom.json"
    p.write_text('{"ranges": {}}', encoding="utf-8")
    monkeypatch.setenv("CEMINI_MAFP_CHART_PATH", str(p))
    assert resolve_mafp_chart_path() == p
