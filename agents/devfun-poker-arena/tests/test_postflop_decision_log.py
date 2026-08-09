"""Fail-open postflop decision jsonl logger."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import _log_postflop_decision  # noqa: E402


def test_postflop_log_writes_jsonl(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    monkeypatch.delenv("CEMINI_POSTFLOP_LOG_PATH", raising=False)
    table = {
        "tableId": "t1",
        "competitionId": "c1",
        "street": "Flop",
        "potChips": 120,
        "selfSeatNumber": 0,
        "buttonSeatNumber": 5,
        "seats": [
            {"seatNumber": 0, "chips": 900, "position": "BB"},
            {"seatNumber": 1, "chips": 1000},
        ],
        "allowedActions": {"callChips": 40, "availableActions": ["fold", "call"]},
    }
    _log_postflop_decision(table, action="fold", amount=None)
    path = export / "postflop_decisions.jsonl"
    assert path.is_file()
    row = json.loads(path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["street"] == "Flop"
    assert row["action"] == "fold"
    assert row["pot"] == 120
    assert row["call_chips"] == 40
    assert row["stack_chips"] == 900
    assert row["tableId"] == "t1"


def test_postflop_log_skips_preflop(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    _log_postflop_decision(
        {"street": "Preflop", "tableId": "t2", "allowedActions": {}},
        action="fold",
    )
    assert not (export / "postflop_decisions.jsonl").exists()


def test_postflop_log_fail_open_no_export(monkeypatch):
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    monkeypatch.delenv("CEMINI_POSTFLOP_LOG_PATH", raising=False)
    # Must not raise
    _log_postflop_decision({"street": "Turn"}, action="check")
