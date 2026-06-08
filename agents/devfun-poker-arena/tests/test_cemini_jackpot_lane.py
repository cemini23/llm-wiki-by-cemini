"""27o hunt on claimed qual bot (cemini_decide), not a separate probe."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

import jackpot_27_state  # noqa: E402
import cemini_decide  # noqa: E402
from tests.helpers.jackpot_27_tables import btn_72o_unopened  # noqa: E402


def test_cemini_hunts_72o_btn_when_enabled():
    os.environ["JACKPOT_27_HUNT_ENABLED"] = "1"
    os.environ["JACKPOT_27_COMPETITION_ID"] = "cmq57o53r0bhw18g23qkydb08"
    jackpot_27_state.reset_session()
    table = btn_72o_unopened()
    table["competitionId"] = "cmq57o53r0bhw18g23qkydb08"
    ctx = cemini_decide.retrieve_solver_context(table)
    ctx["opponent_hud"] = {"mode": "rock", "coldStart": False}
    out = cemini_decide.decide(table, deadline_s=10.0, research_context=ctx)
    assert out["action"] == "bet"
    jackpot_27_state.reset_session()


def test_cemini_folds_72o_btn_when_hunt_off():
    os.environ.pop("JACKPOT_27_HUNT_ENABLED", None)
    jackpot_27_state.reset_session()
    table = btn_72o_unopened()
    ctx = cemini_decide.retrieve_solver_context(table)
    ctx["opponent_hud"] = {"mode": "rock", "coldStart": False}
    out = cemini_decide.decide(table, deadline_s=10.0, research_context=ctx)
    assert out["action"] in ("fold", "check", "call")
    assert out["action"] != "bet"
