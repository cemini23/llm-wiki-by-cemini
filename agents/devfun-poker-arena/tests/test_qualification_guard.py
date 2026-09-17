"""Qualification + lead protection gates for lobby decide()."""
from __future__ import annotations

from qualification_guard import (
    DEFAULT_BUFFER_CHIPS,
    DEFAULT_LEAD_BUFFER_CHIPS,
    fetch_qualification_status,
    qual_survival_mode,
    staggered_chip_lock,
    tournament_mode_enabled,
)


class _FakeClient:
    def __init__(self, me: dict, cutoff_score: int):
        self._me = me
        self._cutoff = cutoff_score

    def get(self, path: str) -> dict:
        if path == "/agent/me":
            return self._me
        if "leaderboard" in path and "offset=" in path:
            return {"data": [{"totalScore": self._cutoff}]}
        raise AssertionError(path)


def test_protect_when_rank_in_zone_and_buffer_ge_1000():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 10, "totalScore": 4538}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is True
    assert st["lead_protect"] is False
    assert st["buffer_chips"] == 2528


def test_lead_protect_top5_large_cushion():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 3, "totalScore": 9114}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["qualification_protect"] is True
    assert st["lead_protect"] is True
    assert st["first_protect"] is False
    assert st["buffer_chips"] == 7104


def test_first_protect_rank_one_only():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 2, "totalScore": 13378}]},
        cutoff_score=3625,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["lead_protect"] is True
    assert st["first_protect"] is False


def test_first_protect_rank_one():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 1, "totalScore": 12000}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["lead_protect"] is True
    assert st["first_protect"] is True
    assert st["buffer_chips"] == 9990


def test_legacy_flat_reserve_when_stagger_disabled(monkeypatch):
    """Optional CEMINI_CHIP_RESERVE on prod .env still works when stagger is off."""
    monkeypatch.setenv("CEMINI_STAGGER_LOCKS", "0")
    monkeypatch.setenv("CEMINI_CHIP_RESERVE", "50000")
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 1, "totalScore": 87443}]},
        cutoff_score=15000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["first_protect"] is True
    assert st["locked_chips"] == 50000
    assert st["max_playable_chips"] == 37443


def test_stagger_lock_dominant_rank_one(monkeypatch):
    monkeypatch.setenv("CEMINI_STAGGER_LOCKS", "1")
    lock = staggered_chip_lock(
        87443,
        15062,
        qual_buffer=1000,
        qualification_protect=True,
        lead_protect=True,
        first_protect=True,
    )
    assert lock["qual_floor_chips"] == 16062
    assert lock["lock_tier"] == "dominant"
    # 80% of surplus locked + 28% max playable cap — scales with stack, not fixed chips.
    assert lock["locked_chips"] >= int(16062 + (87443 - 16062) * 0.79)
    assert lock["playable_chips"] == 87443 - lock["locked_chips"]
    assert lock["playable_chips"] <= int(87443 * 0.29)


def test_stagger_lock_marginal_top20(monkeypatch):
    monkeypatch.setenv("CEMINI_STAGGER_LOCKS", "1")
    lock = staggered_chip_lock(
        18500,
        15062,
        qual_buffer=1000,
        qualification_protect=True,
        lead_protect=False,
        first_protect=False,
    )
    assert lock["lock_tier"] == "comfort_top20"
    assert lock["locked_chips"] >= 16000
    assert lock["playable_chips"] <= 3000


def test_p15_at_cutoff_does_not_zero_playable(monkeypatch):
    """P15 2026-08-19: rank 20 @ 964 vs cutoff 964 locked playable=0."""
    monkeypatch.setenv("CEMINI_STAGGER_LOCKS", "1")
    monkeypatch.setenv("CEMINI_QUAL_BUFFER_CHIPS", "0")
    lock = staggered_chip_lock(
        964,
        964,
        qual_buffer=0,
        qualification_protect=True,
        lead_protect=False,
        first_protect=False,
    )
    assert lock["lock_tier"] == "off"
    assert lock["playable_chips"] == 964
    assert lock["max_playable_chips"] is None
    lock_buf = staggered_chip_lock(
        964,
        964,
        qual_buffer=1000,
        qualification_protect=True,
    )
    assert lock_buf["playable_chips"] == 964
    fat = staggered_chip_lock(
        2000,
        964,
        qual_buffer=0,
        qualification_protect=True,
    )
    assert fat["playable_chips"] >= int(2000 * 0.12)
    assert fat["playable_chips"] < 2000


def test_qual_survival_mode_off_at_cutoff():
    assert qual_survival_mode(lead_protect=False, buffer_chips=0) is False
    assert qual_survival_mode(lead_protect=False, buffer_chips=-10) is False
    assert qual_survival_mode(lead_protect=False, buffer_chips=36) is True
    assert qual_survival_mode(lead_protect=True, buffer_chips=0) is True


def test_stagger_lock_scales_with_smaller_tournament(monkeypatch):
    """Same ratios produce sensible locks when chip scale is 10x smaller."""
    monkeypatch.setenv("CEMINI_STAGGER_LOCKS", "1")
    lock = staggered_chip_lock(
        8744,
        1506,
        qual_buffer=100,
        qualification_protect=True,
        lead_protect=True,
        first_protect=True,
    )
    assert lock["qual_floor_chips"] == 1606
    assert lock["lock_tier"] == "dominant"
    assert lock["locked_chips"] > lock["qual_floor_chips"]
    assert lock["playable_chips"] < 8744 * 0.30


def test_no_lead_protect_when_buffer_below_3000():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 8, "totalScore": 4500}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["qualification_protect"] is True
    assert st["lead_protect"] is False


def test_no_protect_when_buffer_below_threshold():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 15, "totalScore": 2800}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is False
    assert st["lead_protect"] is False
    assert st["buffer_chips"] == 790


def test_no_protect_when_rank_outside_top_20():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 25, "totalScore": 5000}]},
        cutoff_score=2010,
    )
    st = fetch_qualification_status(client, "comp1", buffer_chips=1000)
    assert st["qualification_protect"] is False
    assert st["lead_protect"] is False


def test_sticky_hold_rank_21_small_under():
    """Once in top-20, stay protect at #21 with a small chip dip (P13 overnight dropouts)."""
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 21, "totalScore": 11080}]},
        cutoff_score=11176,
    )
    st = fetch_qualification_status(
        client, "comp1", buffer_chips=0, previously_protect=True,
    )
    assert st["qualification_protect"] is True
    assert st["lock_tier"] == "sticky_top20"
    assert st["buffer_chips"] == -96


def test_sticky_does_not_arm_from_outside():
    """Never arm protect at #21 if we were not already in."""
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 21, "totalScore": 11080}]},
        cutoff_score=11176,
    )
    st = fetch_qualification_status(
        client, "comp1", buffer_chips=0, previously_protect=False,
    )
    assert st["qualification_protect"] is False


def test_sticky_releases_when_too_far_under():
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 21, "totalScore": 10800}]},
        cutoff_score=11176,
    )
    st = fetch_qualification_status(
        client, "comp1", buffer_chips=0, previously_protect=True,
    )
    assert st["buffer_chips"] == -376
    assert st["qualification_protect"] is False


def test_default_thresholds():
    assert DEFAULT_BUFFER_CHIPS == 1000
    assert DEFAULT_LEAD_BUFFER_CHIPS == 3000


def test_tournament_mode_disables_all_protect_lanes(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    assert tournament_mode_enabled()
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 1, "totalScore": 50000}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["rank"] == 1
    assert st["qualification_protect"] is False
    assert st["lead_protect"] is False
    assert st["first_protect"] is False
    # buffer/cutoff = 49.0 >= 0.35 default cushion → protect
    assert st["placement_protect"] is True
    assert st["placement_chase"] is False
    assert st["lock_tier"] == "tournament"
    assert st["max_playable_chips"] is None


def test_tournament_mode_no_placement_protect_below_cutoff(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 15, "totalScore": 5000}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["placement_protect"] is False
    assert st["placement_chase"] is True


def test_tournament_rank_19_chase_not_money_protect(monkeypatch):
    """Rank 19 outside top-10 prize — must not use top-20 placement protect."""
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 19, "totalScore": 8000}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["prize_cutoff_rank"] == 10
    assert st["placement_protect"] is False
    assert st["placement_chase"] is True


def test_tournament_thin_cushion_chase_not_protect(monkeypatch):
    """T12 #2@1000 — rank in money but buffer/cutoff < 35% → chase, not nit protect."""
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    monkeypatch.setenv("CEMINI_PRIZE_CUTOFF_RANK", "3")
    monkeypatch.delenv("CEMINI_PLACEMENT_PROTECT_BUFFER_PCT", raising=False)
    # rank 2, chips 1000, cutoff 900 → buffer 100 / 900 ≈ 0.11 < 0.35
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 2, "totalScore": 1000}]},
        cutoff_score=900,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["placement_protect"] is False
    assert st["placement_chase"] is True
    assert st["buffer_chips"] == 100


def test_tournament_thick_cushion_placement_protect(monkeypatch):
    """Inside prize cut with ≥35% cushion → placement_protect."""
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    monkeypatch.setenv("CEMINI_PRIZE_CUTOFF_RANK", "3")
    monkeypatch.setenv("CEMINI_PLACEMENT_PROTECT_BUFFER_PCT", "0.35")
    # rank 2, chips 2000, cutoff 1000 → buffer 1000 / 1000 = 1.0 >= 0.35
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 2, "totalScore": 2000}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["placement_protect"] is True
    assert st["placement_chase"] is False


def test_tournament_buffer_positive_but_below_pct_still_chase(monkeypatch):
    """buffer>0 alone must not arm protect (legacy false lock)."""
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    monkeypatch.setenv("CEMINI_PRIZE_CUTOFF_RANK", "10")
    monkeypatch.setenv("CEMINI_PLACEMENT_PROTECT_BUFFER_PCT", "0.35")
    # rank 1, chips 1100, cutoff 1000 → buffer 100 / 1000 = 0.10 < 0.35
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 1, "totalScore": 1100}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["placement_protect"] is False
    assert st["placement_chase"] is True
