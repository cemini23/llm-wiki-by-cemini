"""K156 risk-spectrum tags for opponent cards."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from risk_spectrum import (  # noqa: E402
    attach_risk_spectrum_to_hud,
    band_participation,
    band_proactiveness,
    build_risk_spectrum,
    default_opponent_profile_paths,
    load_profile_risk_spectrum,
    validate_risk_spectrum,
)


def test_bands():
    assert band_participation(0.516) == "high"
    assert band_participation(0.30) == "medium"
    assert band_participation(0.10) == "low"
    assert band_proactiveness(0.151) == "high"
    assert band_proactiveness(0.08) == "medium"
    assert band_proactiveness(0.0) == "low"


def test_build_and_validate():
    block = build_risk_spectrum(0.516, 0.0, source="arena_stats")
    assert block["participation"] == "high"
    assert block["proactiveness"] == "low"
    assert validate_risk_spectrum(block) == []


def test_ten_and_maniac_profiles_have_spectrum():
    paths = default_opponent_profile_paths(ROOT)
    assert len(paths) == 2
    by_name = {p.name: load_profile_risk_spectrum(p) for p in paths}

    ten = by_name["ten-ladder-s1-profile.json"]
    assert ten["participation"] == "high"
    assert ten["proactiveness"] == "low"
    assert ten["source"] == "arena_stats"
    assert abs(ten["vpip"] - 0.516) < 1e-6

    shark = by_name["maniac-shark-ladder-s1-profile.json"]
    assert shark["participation"] == "medium"
    assert shark["proactiveness"] == "high"
    assert abs(shark["pfr"] - 0.151) < 1e-6

    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        assert "risk_spectrum" in data
        assert validate_risk_spectrum(data["risk_spectrum"]) == []


def test_hud_attach_does_not_rewrite_mode():
    hud = {"mode": "maniac", "vpip": 0.40, "pfr": 0.12}
    out = attach_risk_spectrum_to_hud(hud)
    assert out["mode"] == "maniac"
    assert out["risk_spectrum"]["participation"] == "medium"
    assert out["risk_spectrum"]["proactiveness"] == "medium"
