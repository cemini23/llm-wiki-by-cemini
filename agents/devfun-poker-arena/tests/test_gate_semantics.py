import importlib
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))


def _mod():
    return importlib.import_module("cemini_selfplay_audit")


def test_gate_semantics_note_exists():
    note = getattr(_mod(), "GATE_SEMANTICS_NOTE", None)
    assert isinstance(note, str) and note.strip()


def test_gate_semantics_note_disclaims_nash():
    note = _mod().GATE_SEMANTICS_NOTE.lower()
    # Affirms what the gate IS ...
    assert "trueskill" in note
    assert "regression" in note or "kpi" in note
    # ... and explicitly disclaims what it is NOT.
    assert "not" in note
    assert "nash" in note or "exploitability" in note


def test_gate_semantics_note_points_to_real_solver():
    note = _mod().GATE_SEMANTICS_NOTE
    assert "kuhn3p_solver" in note
