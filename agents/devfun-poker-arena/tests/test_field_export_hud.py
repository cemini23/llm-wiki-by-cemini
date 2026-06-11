"""Tests for field export HUD overlay."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from field_export_hud import (  # noqa: E402
    lookup_export_agent,
    overlay_export_field_stats,
)
from villain_archetype import enrich_hud_from_table  # noqa: E402


def _write_export(tmp_path: Path) -> Path:
    export_dir = tmp_path / "export"
    export_dir.mkdir()
    row = {
        "agent_id": "a1",
        "handle": "vector_ai",
        "rank": 5,
        "chips": 9000,
        "hands": 400,
        "stats": {
            "sample_size": 400,
            "vpip": 0.28,
            "pfr": 0.19,
            "three_bet_pct": 0.08,
            "playing_style": "LAG",
        },
    }
    (export_dir / "agents.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
    return export_dir


def test_overlay_when_live_stats_missing(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    export_dir = _write_export(tmp_path)
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_DIR", str(export_dir))
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_HUD", "1")
    merged = overlay_export_field_stats("vector_ai", {})
    assert merged.get("vpip") == 0.28
    assert merged.get("pfr") == 0.19
    assert merged.get("field_export_overlay") is True


def test_trust_live_when_sample_large(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    export_dir = _write_export(tmp_path)
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_DIR", str(export_dir))
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_MIN_LIVE_SAMPLE", "8")
    live = {"vpip": 0.12, "pfr": 0.08, "sampleSize": 50}
    merged = overlay_export_field_stats("vector_ai", live)
    assert merged["vpip"] == 0.12
    assert "field_export_overlay" not in merged


def test_enrich_hud_uses_export(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    export_dir = _write_export(tmp_path)
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_DIR", str(export_dir))
    table = {
        "selfSeatNumber": 1,
        "bigBlindChips": 20,
        "seats": [
            {"seatNumber": 1, "stackChips": 5000, "currentBetChips": 0},
            {
                "seatNumber": 3,
                "agentHandle": "vector_ai",
                "currentBetChips": 60,
                "stackChips": 5000,
            },
        ],
    }
    hud = enrich_hud_from_table({}, table)
    assert hud.get("vpip") == 0.28
    assert hud.get("field_export_seats", {}).get("vector_ai", {}).get("vpip") == 0.28


def test_lookup_disabled(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    export_dir = _write_export(tmp_path)
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_DIR", str(export_dir))
    monkeypatch.setenv("CEMINI_FIELD_EXPORT_HUD", "0")
    assert lookup_export_agent("vector_ai") is None
