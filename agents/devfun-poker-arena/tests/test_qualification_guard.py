"""Qualification + lead protection gates for lobby decide()."""
from __future__ import annotations

from qualification_guard import (
    DEFAULT_BUFFER_CHIPS,
    DEFAULT_LEAD_BUFFER_CHIPS,
    fetch_qualification_status,
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
    assert st["placement_protect"] is True
    assert st["lock_tier"] == "tournament"
    assert st["max_playable_chips"] is None


def test_tournament_mode_no_placement_protect_below_cutoff(monkeypatch):
    monkeypatch.setenv("CEMINI_TOURNAMENT_MODE", "1")
    monkeypatch.setenv("CEMINI_QUAL_CUTOFF_RANK", "10")
    client = _FakeClient(
        {"leaderboard": [{"arenaId": "comp1", "rank": 15, "totalScore": 5000}]},
        cutoff_score=1000,
    )
    st = fetch_qualification_status(client, "comp1")
    assert st["placement_protect"] is False
