"""K244/K245 — clarify-before-solver preflight + redundant-dump skip."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from solver_preflight import (  # noqa: E402
    observation_hash,
    should_skip_redundant_table_dump,
    solver_inputs_ready,
)


def _seat(num: int, chips: int | None = None) -> dict:
    s = {"seatNumber": num, "status": "Active"}
    if chips is not None:
        s["stackChips"] = chips
    return s


def test_missing_street():
    table = {"selfSeatNumber": 1, "seats": [_seat(1, 1000), _seat(2, 1000)]}
    missing = solver_inputs_ready(table)
    assert "street" in missing


def test_missing_stack_when_no_hero_seat():
    table = {"street": "Preflop", "selfSeatNumber": 1, "seats": []}
    missing = solver_inputs_ready(table)
    assert "stack" in missing


def test_ready_table_reports_empty():
    table = {
        "street": "Preflop",
        "selfSeatNumber": 1,
        "buttonSeatNumber": 2,
        "tableFormat": "hu",
        "seats": [_seat(1, 1000), _seat(2, 1000)],
    }
    assert solver_inputs_ready(table) == []


def test_skip_dump_after_solver_ok_same_hash():
    last = observation_hash({"street": "Flop", "board": ["Ah", "7d", "2c"]})
    same = observation_hash({"street": "Flop", "board": ["Ah", "7d", "2c"]})
    changed = observation_hash({"street": "Flop", "board": ["Ah", "7d", "2c", "Ks"]})
    assert should_skip_redundant_table_dump(last, same, solver_ok=True) is True
    assert should_skip_redundant_table_dump(last, same, solver_ok=False) is False
    assert should_skip_redundant_table_dump(last, changed, solver_ok=True) is False


def test_docs_mention_arxiv_ids():
    refs = Path(__file__).resolve().parent.parent / "references"
    clarify = (refs / "clarify-before-solver.md").read_text(encoding="utf-8")
    adoption = (refs / "tool-adoption-gap.md").read_text(encoding="utf-8")
    assert "2608.03018" in clarify
    assert "2608.03327" in adoption
