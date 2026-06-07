"""Regression tests for S2 jackpot satellite (jackpot_27_decide)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

import jackpot_27_decide  # noqa: E402
import jackpot_27_state  # noqa: E402
from tests.helpers.cemini_tables import mp_unopened  # noqa: E402
from tests.helpers.jackpot_27_tables import (  # noqa: E402
    btn_72o_facing_raise,
    btn_72o_multiway_limp,
    btn_72o_unopened,
)


def _rock_ctx(table: dict) -> dict:
    ctx = jackpot_27_decide.retrieve_solver_context(table)
    ctx["opponent_hud"] = {"mode": "rock", "coldStart": False}
    return ctx


def _run(table: dict, *, ctx: dict | None = None) -> dict:
    jackpot_27_state.reset_session()
    if ctx is None:
        ctx = _rock_ctx(table)
    out = jackpot_27_decide.decide(table, deadline_s=10.0, research_context=ctx)
    legal = set(table["allowedActions"]["availableActions"])
    assert out["action"] in legal
    assert len(out.get("reasoning", "")) <= 150
    return out


def test_72o_utg_no_hunt():
    out = _run(mp_unopened(["7d", "2h"]))
    assert out["action"] in ("fold", "call")


def test_72o_btn_unopened_hunt_bets():
    os.environ["JACKPOT_27_HUNT_ENABLED"] = "1"
    out = _run(btn_72o_unopened())
    assert out["action"] == "bet"
    assert out.get("amount") is not None


def test_72o_btn_vs_raise_aborts():
    out = _run(btn_72o_facing_raise())
    assert out["action"] == "fold"


def test_72o_multiway_no_hunt():
    table = btn_72o_multiway_limp()
    ctx = _rock_ctx(table)
    out = jackpot_27_decide.decide(table, deadline_s=10.0, research_context=ctx)
    assert out["action"] in ("fold", "call")
    assert out["action"] != "bet"


def test_session_cap_blocks_fourth_hunt():
    os.environ["JACKPOT_27_HUNT_ENABLED"] = "1"
    os.environ["JACKPOT_27_MAX_ATTEMPTS"] = "3"
    jackpot_27_state.reset_session()
    ctx_base = {"opponent_hud": {"mode": "rock", "coldStart": False}}
    for i in range(3):
        t = btn_72o_unopened()
        t["tableId"] = f"tbl_cap_{i}"
        t["id"] = t["tableId"]
        out = jackpot_27_decide.decide(t, research_context=ctx_base)
        assert out["action"] == "bet"
    t4 = btn_72o_unopened()
    t4["tableId"] = "tbl_cap_4"
    t4["id"] = t4["tableId"]
    out = jackpot_27_decide.decide(t4, research_context=ctx_base)
    assert out["action"] != "bet"
    assert out["action"] in ("fold", "call", "check")
    jackpot_27_state.reset_session()


def test_hunt_disabled_by_default():
    os.environ.pop("JACKPOT_27_HUNT_ENABLED", None)
    jackpot_27_state.reset_session()
    out = jackpot_27_decide.decide(
        btn_72o_unopened(),
        research_context=_rock_ctx(btn_72o_unopened()),
    )
    assert out["action"] != "bet"


def test_prod_deploy_excludes_jackpot_creds():
    deploy = (ROOT / "deploy" / "deploy_to_cemini_prod.sh").read_text()
    assert ".arena-credentials.jackpot-27" in deploy or ".arena-credentials.*" in deploy
    jackpot_deploy = ROOT / "deploy" / "deploy_jackpot_27_prod.sh"
    assert jackpot_deploy.is_file()
    text = jackpot_deploy.read_text()
    assert "cemini-devfun-poker-lobby" not in text or "jackpot-27-lobby" in text


def test_safety_detects_qual_bot_at_table():
    import jackpot_27_safety  # noqa: E402

    table = btn_72o_unopened()
    table["seats"].append({
        "seatNumber": 4,
        "agentId": "cmpy4lcyi001y11vnekn1zlo3",
        "agentHandle": "cemini_wiki_poker",
        "status": "Active",
    })
    assert jackpot_27_safety.table_has_blocked_agent(table, self_agent_id="probe123")


def test_safety_detects_sibling_probe():
    import jackpot_27_safety  # noqa: E402

    table = btn_72o_unopened()
    table["seats"].append({
        "seatNumber": 4,
        "agentId": "other_probe",
        "agentHandle": "arena_probe_egr-b",
        "status": "Active",
    })
    assert jackpot_27_safety.table_has_blocked_agent(table, self_agent_id="probe123")


def test_join_disabled_by_default():
    import jackpot_27_safety  # noqa: E402

    os.environ.pop("JACKPOT_27_JOIN_ENABLED", None)
    assert jackpot_27_safety.join_enabled() is False
