"""Tests for session villain memory (Agent Memory Test → poker adaptation)."""
from session_memory import (
    exploit_from_memory,
    record_showdown_from_table,
    update_session_memory,
    villain_memory_for_table,
)


def test_villain_memory_abstains_without_samples():
    state = {"session_villain_memory": {}}
    table = {
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
        "street": "Flop",
        "actionHistory": [],
    }
    mem = villain_memory_for_table(state, table)
    assert mem.get("note") or not mem.get("villains")


def test_villain_memory_aggro_after_samples():
    state = {
        "session_villain_memory": {
            "v1": {"aggressive_acts": 6, "passive_acts": 1, "samples": 7},
        }
    }
    table = {
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
    }
    mem = villain_memory_for_table(state, table)
    assert mem["villains"]["v1"]["label"] == "aggro"
    margins = exploit_from_memory(mem)
    assert margins.get("fold_slack_delta", 0) > 0


def test_update_session_memory_records_bets():
    state = {}
    table = {
        "selfSeatNumber": 1,
        "street": "Flop",
        "seats": [
            {"seatNumber": 1, "agentId": "hero"},
            {"seatNumber": 2, "agentId": "v1"},
        ],
        "actionHistory": [
            {"street": "Flop", "action": "bet", "seatNumber": 2, "amount": 50},
        ],
    }
    update_session_memory(state, table)
    assert state["session_villain_memory"]["v1"]["aggressive_acts"] == 1


def test_showdown_queue_and_exploit_tighten_vs_repeat_winner():
    state: dict = {"showdown_tables_seen": []}
    hero = "hero"
    table = {
        "id": "t1",
        "winners": [{"agentId": "v1"}],
        "seats": [
            {"seatNumber": 1, "agentId": hero, "holeCards": ["2c", "3d"], "payoutChips": 0},
            {"seatNumber": 2, "agentId": "v1", "holeCards": ["As", "Ad"], "payoutChips": 200},
        ],
        "actionHistory": [
            {"street": "Preflop", "action": "raise", "seatNumber": 2, "amount": 60},
        ],
    }
    assert record_showdown_from_table(state, table, hero) is True
    rec = state["session_villain_memory"]["v1"]
    assert len(rec["showdowns"]) == 1
    assert rec["showdowns"][0]["villain_won"] is True
    assert rec["showdowns"][0]["villain_preflop_aggressive"] is True
    assert record_showdown_from_table(state, table, hero) is False

    state["session_villain_memory"]["v1"].update({
        "aggressive_acts": 6,
        "passive_acts": 1,
        "samples": 7,
        "showdowns": [
            {"hero_won": False, "villain_won": True, "villain_preflop_aggressive": True},
            {"hero_won": False, "villain_won": True, "villain_preflop_aggressive": False},
            {"hero_won": False, "villain_won": True, "villain_preflop_aggressive": True},
        ],
    })
    live = {
        "selfSeatNumber": 1,
        "seats": [
            {"seatNumber": 1, "agentId": hero},
            {"seatNumber": 2, "agentId": "v1"},
        ],
    }
    mem = villain_memory_for_table(state, live)
    margins = exploit_from_memory(mem)
    assert margins.get("fold_slack_delta", 0) > 0.03
