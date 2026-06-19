"""Table format resolution for Researcher dual-readiness."""
from __future__ import annotations

import os

from table_format_utils import active_player_count, resolve_table_format


def test_resolve_hu_from_two_seats():
    table = {"seats": [{"seatNumber": 1, "status": "Active"}, {"seatNumber": 2, "status": "Active"}]}
    assert active_player_count(table) == 2
    assert resolve_table_format(table) == "hu"


def test_resolve_6max_from_six_seats(monkeypatch):
    monkeypatch.delenv("CEMINI_TABLE_FORMAT", raising=False)
    table = {
        "seats": [{"seatNumber": i, "status": "Active"} for i in range(1, 7)],
    }
    assert resolve_table_format(table) == "6max"


def test_env_forces_hu(monkeypatch):
    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    table = {"seats": [{"seatNumber": i, "status": "Active"} for i in range(1, 7)]}
    assert resolve_table_format(table) == "hu"
