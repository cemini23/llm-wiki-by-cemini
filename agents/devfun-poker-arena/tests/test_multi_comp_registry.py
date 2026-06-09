"""Multi-comp oracle — config + deploy gate."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from multi_comp_registry import (  # noqa: E402
    CONFIG_SCHEMA,
    TIMESERIES_SCHEMA,
    all_comp_entries,
    default_config,
    deploy_allowed_from_oracle,
    load_config,
    primary_competition_id,
    write_config,
)


def test_default_config_primary_drives_deploy() -> None:
    cfg = default_config()
    assert cfg["schema"] == CONFIG_SCHEMA
    assert cfg["primary"]["drives_deploy"] is True
    assert cfg["secondary"][0]["drives_deploy"] is False


def test_primary_competition_id_from_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cfg = default_config()
    cfg["primary"]["competition_id"] = "cmp_tournament_s1"
    path = tmp_path / "multi_comp_config.json"
    path.write_text(json.dumps(cfg) + "\n")
    monkeypatch.setenv("CEMINI_MULTI_COMP_CONFIG", str(path))
    assert primary_competition_id() == "cmp_tournament_s1"
    assert len(all_comp_entries(load_config())) == 2


def test_deploy_gate_requires_primary_hands(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    ts = tmp_path / "multi_comp_timeseries.jsonl"
    row = {
        "schema": TIMESERIES_SCHEMA,
        "role": "s1_tournament",
        "drives_deploy": True,
        "hands": 40,
    }
    ts.write_text(json.dumps(row) + "\n")
    monkeypatch.setenv("CEMINI_MULTI_COMP_TIMESERIES", str(ts))

    ok, msg = deploy_allowed_from_oracle(min_primary_hands=80)
    assert not ok
    assert "40" in msg

    row["hands"] = 120
    ts.write_text(json.dumps(row) + "\n")
    ok, msg = deploy_allowed_from_oracle(min_primary_hands=80)
    assert ok
    assert "S1 primary" in msg


def test_write_config_roundtrip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_MULTI_COMP_CONFIG", str(tmp_path / "cfg.json"))
    path = write_config(default_config())
    assert path.is_file()
    assert load_config()["schema"] == CONFIG_SCHEMA
