"""K140 mechanical invariants gate tests."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
HELPERS = ROOT / "tests" / "helpers"

for path in (EXAMPLES, HELPERS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from cemini_tables import hu_sb_unopened  # noqa: E402

_IMPORT_ERROR: Exception | None = None
_INVARIANTS_MOD = None
try:
    _INVARIANTS_MOD = importlib.import_module("sandbox_mechanical_invariants")
except Exception as exc:  # pragma: no cover
    _IMPORT_ERROR = exc


def _require_module():
    if _INVARIANTS_MOD is None:
        pytest.fail(f"could not import examples/sandbox_mechanical_invariants.py: {_IMPORT_ERROR}")
    return _INVARIANTS_MOD


def _verify(**kwargs):
    mod = _require_module()
    fn = mod.verify_mechanical_invariants
    return fn(**kwargs)


def _table() -> dict[str, Any]:
    return hu_sb_unopened(["As", "Ah"])


def _allowed(table: dict[str, Any]) -> list[str]:
    return list(table["allowedActions"]["availableActions"])


def _payload(*, reasoning: str = '{vr: "hu:btn-open", ke: "AA strong", pp: "IP value"}') -> dict[str, Any]:
    return {
        "action": "raise",
        "amount": 4,
        "reasoning": reasoning,
        "reasoning_text": reasoning,
    }


def test_passes_valid_hu_table_and_legal_action():
    table = _table()
    result = _verify(
        table=table,
        action="raise",
        allowed_actions=_allowed(table),
        action_payload=_payload(),
    )
    assert result["pass"] is True
    assert result["hazards"] == []
    assert result["details"]["checks"]["agency"]["pass"] is True
    assert result["details"]["checks"]["state"]["pass"] is True
    assert result["details"]["checks"]["rules"]["pass"] is True
    assert result["details"]["checks"]["goals"]["pass"] is True


def test_agency_violation_for_illegal_action():
    table = _table()
    result = _verify(
        table=table,
        action="dance",
        allowed_actions=_allowed(table),
        action_payload=_payload(),
    )
    assert result["pass"] is False
    assert "invariant:agency_violation" in result["hazards"]
    assert result["hazard"] == "invariant:agency_violation"


def test_missing_state_when_table_absent():
    result = _verify(
        table=None,
        action="fold",
        allowed_actions=["fold", "call"],
        action_payload={"action": "fold"},
    )
    assert result["pass"] is False
    assert "invariant:missing_state" in result["hazards"]
    assert "invariant:missing_rules" in result["hazards"]
    assert "invariant:missing_hero" in result["hazards"]


def test_missing_state_when_seats_empty():
    table = {"potChips": 100, "allowedActions": {"availableActions": ["fold"]}, "selfSeatNumber": 1}
    result = _verify(
        table=table,
        action="fold",
        allowed_actions=["fold"],
        action_payload={"action": "fold"},
    )
    assert result["pass"] is False
    assert "invariant:missing_state" in result["hazards"]


def test_missing_rules_when_allowed_actions_block_absent():
    table = {
        "potChips": 100,
        "selfSeatNumber": 1,
        "seats": [{"seatNumber": 1, "stackChips": 500}],
    }
    result = _verify(
        table=table,
        action="fold",
        allowed_actions=["fold"],
        action_payload={"action": "fold"},
    )
    assert result["pass"] is False
    assert "invariant:missing_rules" in result["hazards"]


def test_empty_reasoning_when_field_present():
    table = _table()
    result = _verify(
        table=table,
        action="raise",
        allowed_actions=_allowed(table),
        action_payload={"action": "raise", "amount": 4, "reasoning": "   "},
    )
    assert result["pass"] is False
    assert "invariant:empty_reasoning" in result["hazards"]


def test_missing_hero_when_self_seat_unknown():
    table = _table()
    del table["selfSeatNumber"]
    result = _verify(
        table=table,
        action="raise",
        allowed_actions=_allowed(table),
        action_payload=_payload(),
    )
    assert result["pass"] is False
    assert "invariant:missing_hero" in result["hazards"]


def test_score_action_includes_mechanical_invariants_gate():
    verifier = importlib.import_module("sandbox_tri_verifier")
    table = _table()
    payload = _payload()
    good = verifier.score_action(
        action="raise",
        allowed_actions=_allowed(table),
        elapsed_s=0.2,
        deadline_s=1.0,
        action_payload=payload,
        table=table,
    )
    assert "mechanical_invariants" in good
    assert good["mechanical_invariants"]["pass"] is True
    assert "mechanical_invariants" in good["dimensions"]

    bad_table = dict(table)
    del bad_table["selfSeatNumber"]
    bad = verifier.score_action(
        action="raise",
        allowed_actions=_allowed(table),
        elapsed_s=0.2,
        deadline_s=1.0,
        action_payload=payload,
        table=bad_table,
    )
    assert bad["pass"] is False
    assert bad["mechanical_invariants"]["pass"] is False
    assert "invariant:missing_hero" in bad["mechanical_invariants"]["hazards"]
