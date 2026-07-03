"""K141 partial-spec trajectory eval tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
HELPERS = ROOT / "tests" / "helpers"
for path in (EXAMPLES, HELPERS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from cemini_tables import hu_sb_unopened  # noqa: E402
from output_sanitize import FALLBACK_REASONING  # noqa: E402
from sandbox_partial_spec_eval import (  # noqa: E402
    load_scenario,
    verify_partial_spec_trajectory,
    verify_rework_detection,
    verify_requirement_memory,
)
from sandbox_tri_verifier import score_trajectory  # noqa: E402


def _good_reasoning() -> str:
    return '{vr: "hu:btn-open", ke: "AA strong", pp: "IP value", sr: "2.0x open"}'


def _action(action: str, *, amount: int | None = None, reasoning: str | None = None) -> dict:
    payload = {
        "action": action,
        "message": action,
        "reasoning": reasoning or _good_reasoning(),
        "reasoning_text": reasoning or _good_reasoning(),
    }
    if amount is not None:
        payload["amount"] = amount
    return payload


def _allowed_actions(table: dict) -> list[str]:
    return list(table["allowedActions"]["availableActions"])


def _make_row(table: dict, action: dict, *, elapsed_s: float = 0.2) -> dict:
    return {
        "action": action["action"],
        "allowed_actions": _allowed_actions(table),
        "elapsed_s": elapsed_s,
        "deadline_s": 10.0,
        "payload": action,
        "table": table,
        "poll_loops": 0,
    }


def test_load_default_scenario() -> None:
    sc = load_scenario()
    assert sc["reveal_at_action"] == 2
    assert "correctness" in sc["phase1_dimensions"]


def test_partial_spec_passes_clean_trajectory() -> None:
    table1 = hu_sb_unopened(["As", "Ah"])
    table2 = hu_sb_unopened(["Kd", "Kc"])
    table2["street"] = "Flop"
    table2["boardCards"] = ["2h", "7d", "9c"]
    events = [
        _make_row(table1, _action("raise", amount=4)),
        _make_row(table2, _action("call")),
    ]
    result = verify_partial_spec_trajectory(events)
    assert result["partial_spec_pass"] is True


def test_vague_start_allows_generic_before_reveal() -> None:
    table1 = hu_sb_unopened(["As", "Ah"])
    table2 = hu_sb_unopened(["Kd", "Kc"])
    table2["street"] = "Flop"
    events = [
        _make_row(table1, _action("raise", amount=4, reasoning=FALLBACK_REASONING)),
        _make_row(table2, _action("call", reasoning=_good_reasoning())),
    ]
    scored = score_trajectory(events)
    memory = verify_requirement_memory(events, scored["actions"], load_scenario())
    assert memory["pass"] is True
    assert memory["violations"] == 0


def test_requirement_memory_fails_generic_after_reveal() -> None:
    table1 = hu_sb_unopened(["As", "Ah"])
    table2 = hu_sb_unopened(["Kd", "Kc"])
    table2["street"] = "Flop"
    events = [
        _make_row(table1, _action("raise", amount=4)),
        _make_row(table2, _action("call", reasoning=FALLBACK_REASONING)),
    ]
    scored = score_trajectory(events)
    memory = verify_requirement_memory(events, scored["actions"], load_scenario())
    assert memory["pass"] is False
    assert memory["violations"] == 1


def test_rework_detection_flags_flip_flops() -> None:
    table = hu_sb_unopened(["As", "Ah"])
    table["street"] = "Flop"
    table["boardCards"] = ["2h", "7d", "9c"]
    events = [
        _make_row(table, _action("raise", amount=4)),
        _make_row(table, _action("call")),
        _make_row(table, _action("fold")),
        _make_row(table, _action("call")),
    ]
    rework = verify_rework_detection(events, load_scenario())
    assert rework["pass"] is False


def test_score_trajectory_attaches_partial_spec() -> None:
    table1 = hu_sb_unopened(["As", "Ah"])
    table2 = hu_sb_unopened(["Kd", "Kc"])
    table2["street"] = "Flop"
    events = [
        _make_row(table1, _action("raise", amount=4)),
        _make_row(table2, _action("call")),
    ]
    result = score_trajectory(events)
    assert "partial_spec" in result
    assert "partial_spec_pass" in result["partial_spec"]
