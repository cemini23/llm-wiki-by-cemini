"""P1-4 postflop telemetry rollup — pure fold-to-cbet + enriched log fields."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from cemini_decide import _log_postflop_decision  # noqa: E402
from postflop_telemetry import fold_to_cbet_rate  # noqa: E402


def _row(street="Flop", action="fold", facing_bet=True, hand_class=None, **kw):
    row = {"street": street, "action": action, "facing_bet": facing_bet}
    if hand_class:
        row["hand_class"] = hand_class
    row.update(kw)
    return row


def test_fold_to_cbet_rate_empty():
    assert fold_to_cbet_rate([]) == {
        "flop_facing": 0, "fold": 0, "call_raise": 0, "fold_to_cbet_rate": 0.0,
    }


def test_fold_to_cbet_rate_mixed():
    rows = [
        _row("Flop", "fold"),
        _row("Flop", "fold"),
        _row("Flop", "call"),
        _row("Flop", "raise"),
        _row("Turn", "fold", facing_bet=True),   # not flop — excluded
        _row("Flop", "check", facing_bet=False),  # not facing a bet — excluded
    ]
    out = fold_to_cbet_rate(rows)
    assert out["flop_facing"] == 4
    assert out["fold"] == 2
    assert out["call_raise"] == 2
    assert out["fold_to_cbet_rate"] == 0.5


def test_fold_to_cbet_rate_all_fold():
    rows = [_row("Flop", "fold"), _row("Flop", "fold")]
    assert fold_to_cbet_rate(rows)["fold_to_cbet_rate"] == 1.0


def test_enriched_log_row_fields(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    monkeypatch.delenv("CEMINI_POSTFLOP_LOG_PATH", raising=False)
    table = {
        "tableId": "t1",
        "street": "Turn",
        "potChips": 200,
        "boardCards": ["Ah", "7d", "2c", "Ks"],
        "selfSeatNumber": 0,
        "seats": [
            {"seatNumber": 0, "chips": 900, "position": "BB",
             "holeCards": ["Kd", "Qd"]},
            {"seatNumber": 1, "chips": 1000},
        ],
        "allowedActions": {"callChips": 40, "availableActions": ["fold", "call"]},
    }
    _log_postflop_decision(table, action="call", amount=40, equity=0.44, pot_odds=0.17)
    path = export / "postflop_decisions.jsonl"
    assert path.is_file()
    row = json.loads(path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["facing_bet"] is True
    assert row["board_len"] == 4
    assert row["hand_class"] == "KQs"
    assert row["equity"] == 0.44
    assert row["pot_odds"] == 0.17
    assert row["call_chips"] == 40
