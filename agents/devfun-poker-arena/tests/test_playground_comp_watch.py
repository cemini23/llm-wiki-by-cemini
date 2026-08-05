"""Playground season discovery — do not miss sprint boards like S12."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from playground_comp_watch import (  # noqa: E402
    discover_active_playground,
    apply_live_playground_env,
)


class _FakeClient:
    def __init__(self, active, all_rows):
        self.active = active
        self.all_rows = all_rows

    def get(self, path: str):
        if path.endswith("list-active"):
            return {"data": self.active}
        if path.endswith("list-all"):
            return {"data": self.all_rows}
        raise AssertionError(path)


def test_picks_newest_active_playground():
    client = _FakeClient(
        active=[
            {"id": "eval1", "name": "[Poker] Eval S1", "seasonNumber": 1, "status": "Active"},
            {"id": "pg13", "name": "[Poker] Playground S13", "seasonNumber": 13, "status": "Active"},
        ],
        all_rows=[
            {"id": "pg12", "name": "[Poker] Playground S12", "seasonNumber": 12, "status": "Ended"},
            {"id": "pg13", "name": "[Poker] Playground S13", "seasonNumber": 13, "status": "Active"},
            {"id": "t11", "name": "[Poker] Tournament S11", "seasonNumber": 11, "status": "Ended"},
        ],
    )
    hit = discover_active_playground(client)
    assert hit is not None
    assert hit["id"] == "pg13"
    assert hit["seasonNumber"] == 13


def test_ignores_ended_only_field():
    client = _FakeClient(
        active=[{"id": "eval1", "name": "[Poker] Eval S1", "seasonNumber": 1}],
        all_rows=[
            {"id": "pg12", "name": "[Poker] Playground S12", "seasonNumber": 12, "status": "Ended"},
            {"id": "pg11", "name": "[Poker] Playground S11", "seasonNumber": 11, "status": "Ended"},
        ],
    )
    assert discover_active_playground(client) is None


def test_apply_env_sets_role_and_export(tmp_path, monkeypatch):
    env = tmp_path / ".env"
    env.write_text("ARENA_LOBBY_COMPETITION_ID=old\nCEMINI_NEMESIS_TIGHT=1\n")
    monkeypatch.chdir(tmp_path)
    kv = apply_live_playground_env(
        {"id": "pg13", "seasonNumber": 13, "name": "[Poker] Playground S13"},
        env_path=env,
    )
    text = env.read_text()
    assert "ARENA_LOBBY_COMPETITION_ID=pg13" in text
    assert "CEMINI_LOBBY_ROLE=s13_playground" in text
    assert "S13_PLAYGROUND_COMP=pg13" in text
    assert "CEMINI_NEMESIS_TIGHT=0" in text
    assert kv["CEMINI_KO_SURVIVAL_MIN_STACK"] == "400"
