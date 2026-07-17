"""WP0 — wall-clock deadline guard + tight decide() path (no Arena)."""
from __future__ import annotations

import importlib
import os
import sys
import time
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
HARNESS = ROOT / "harness"
for _p in (str(EXAMPLES), str(HARNESS), str(ROOT)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from tests.helpers.cemini_tables import hu_table, _allowed  # noqa: E402

_LEGAL = frozenset({"fold", "check", "call", "bet", "raise", "all-in"})


def _hu_open_table() -> dict:
    """Minimal HU BTN open spot with legal fold/raise."""
    return hu_table(
        name="deadline_guard",
        hero_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=["As", "Kd"],
        hero_stack=980,
        hero_bet=10,
        villain_bets={2: 20},
        allowed=_allowed(
            can_fold=True,
            can_check=False,
            can_call=True,
            can_raise=True,
            call_chips=10,
            call_to=20,
            raise_range={"min": 40, "max": 980},
        ),
        button_seat=1,
    )


@pytest.fixture(autouse=True)
def _sandbox_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "cemini")
    monkeypatch.setenv("CEMINI_TABLE_FORMAT", "hu")
    monkeypatch.setenv("CEMINI_RESEARCHER_MODE", "1")
    monkeypatch.setenv("CEMINI_MAFP_CHART", "1")
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_TIGHT_DEADLINE_SIMS", "40")


def test_decide_returns_under_tight_deadline() -> None:
    from cemini_decide import decide

    table = _hu_open_table()
    # Warm caches (MAFP overlay + postflop buckets).
    decide(table, deadline_s=8.0)

    t0 = time.perf_counter()
    out = decide(table, deadline_s=2.5)
    elapsed = time.perf_counter() - t0
    assert isinstance(out, dict)
    assert out.get("action") in _LEGAL
    # Hot path must stay well under Arena static timeout after warmup.
    assert elapsed < 1.5, f"tight decide() too slow: {elapsed:.3f}s"


def test_tight_path_at_deadline_4_5(monkeypatch: pytest.MonkeyPatch) -> None:
    """Timeout harden v2: deadline_s=4.5 is inside the tight band (<5s)."""
    import cemini_decide as cd

    table = _hu_open_table()
    captured: dict = {}
    real_ctx = cd.retrieve_solver_context

    def capture_ctx(table, *, tight_deadline: bool = False):  # noqa: ANN001
        captured["tight_deadline"] = tight_deadline
        return real_ctx(table, tight_deadline=tight_deadline)

    monkeypatch.setattr(cd, "retrieve_solver_context", capture_ctx)
    out = cd.decide(table, deadline_s=4.5)
    assert out.get("action") in _LEGAL
    assert captured.get("tight_deadline") is True


def test_sim_ladder_env_and_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sim budget: >5→250/loose env; ≥3→150/med; <3→TIGHT env (default 40)."""
    import cemini_decide as cd

    table = _hu_open_table()
    seen: list[int] = []

    def fake_eq(hole, board, sims=200, deadline_s=10.0, **_kw):  # noqa: ANN001
        seen.append(int(sims))
        return 0.55

    monkeypatch.setattr(cd, "estimate_equity", fake_eq)
    monkeypatch.delenv("CEMINI_LOOSE_DEADLINE_SIMS", raising=False)
    monkeypatch.delenv("CEMINI_MEDIUM_DEADLINE_SIMS", raising=False)
    monkeypatch.setenv("CEMINI_TIGHT_DEADLINE_SIMS", "40")

    seen.clear()
    cd.decide(table, deadline_s=6.0)
    assert seen and seen[-1] == 250

    seen.clear()
    cd.decide(table, deadline_s=4.0)
    assert seen and seen[-1] == 150

    seen.clear()
    cd.decide(table, deadline_s=2.5)
    assert seen and seen[-1] == 40

    monkeypatch.setenv("CEMINI_TIGHT_DEADLINE_SIMS", "25")
    seen.clear()
    cd.decide(table, deadline_s=2.5)
    assert seen and seen[-1] == 25


def test_decide_emergency_under_sub2s() -> None:
    from cemini_decide import decide

    table = _hu_open_table()
    out = decide(table, deadline_s=1.0)
    assert out.get("action") in ("fold", "check", "call")


def test_mafp_and_buckets_no_reopen_after_warmup(monkeypatch: pytest.MonkeyPatch) -> None:
    import research_static_chart as rsc
    import postflop_buckets as pb

    rsc._reset_mafp_overlay_cache()
    pb._reset_bucket_cache()

    opens: list[str] = []
    real_open = open

    def counting_open(path, *args, **kwargs):  # type: ignore[no-untyped-def]
        p = str(path)
        if p.endswith(".json") and ("mafp" in p or "postflop" in p or "bucket" in p):
            opens.append(p)
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr("builtins.open", counting_open)
    # Path.read_text uses open under the hood on CPython.
    from cemini_decide import decide

    table = _hu_open_table()
    decide(table, deadline_s=8.0)
    n_after_warm = len(opens)
    decide(table, deadline_s=2.5)
    decide(table, deadline_s=2.5)
    # No additional research JSON opens after first warmup.
    assert len(opens) == n_after_warm, f"unexpected re-open: {opens[n_after_warm:]}"


def test_choose_action_emergency_on_zero_guard(monkeypatch: pytest.MonkeyPatch) -> None:
    """_run_decide_guarded with guard_s<=0 returns emergency without calling decide."""
    import strategy as strat_mod

    importlib.reload(strat_mod)

    table = _hu_open_table()
    table["actionDeadlineAt"] = time.time() - 10  # already expired

    called = {"n": 0}

    def boom(_table, deadline_s=10.0):  # noqa: ARG001
        called["n"] += 1
        raise AssertionError("decide must not run when guard is 0")

    monkeypatch.setattr(strat_mod, "_import_decide", lambda: boom)
    out = strat_mod.choose_action(table)
    assert called["n"] == 0
    if isinstance(out, dict):
        assert out.get("action") in ("fold", "check", "call")
    else:
        assert out in ("fold", "check", "call")


def test_run_decide_guarded_alarm_returns_emergency(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import strategy as strat_mod

    if not strat_mod._USE_SIGALRM:
        pytest.skip("SIGALRM unavailable on this platform")

    importlib.reload(strat_mod)
    table = _hu_open_table()
    # Make free check available so emergency is deterministic.
    table["allowedActions"] = _allowed(
        can_fold=True,
        can_check=True,
        can_call=False,
        can_raise=False,
    )

    def slow_decide(_table, deadline_s=10.0):  # noqa: ARG001
        time.sleep(2.0)
        return {"action": "raise", "amount": 60, "message": "too late"}

    # Trip immediately.
    out = strat_mod._run_decide_guarded(
        slow_decide, table, deadline_s=5.0, guard_s=0.05,
    )
    assert out.get("action") == "check"
    assert "wall-clock" in str(out.get("message") or "").lower()


def test_harness_choose_action_returns_legal() -> None:
    import strategy as strat_mod

    importlib.reload(strat_mod)
    table = _hu_open_table()
    # Absolute future deadline so floor path is not forced to emergency.
    table["actionDeadlineAt"] = time.time() + 30
    t0 = time.perf_counter()
    out = strat_mod.choose_action(table)
    elapsed = time.perf_counter() - t0
    if isinstance(out, dict):
        assert out.get("action") in _LEGAL
    else:
        assert out in _LEGAL
    assert elapsed < 5.0


def test_guard_s_tighter_v2() -> None:
    """SIGALRM guard trips earlier: cap 4.5s, 0.5s headroom, 0.6*deadline."""
    import strategy as strat_mod

    importlib.reload(strat_mod)
    assert strat_mod._guard_s(0.0) == 0.0
    assert strat_mod._guard_s(0.4) == 0.0
    g8 = strat_mod._guard_s(8.0)
    assert g8 <= 4.5
    assert g8 == pytest.approx(min(8.0 - 0.5, 4.5, 0.6 * 8.0), abs=1e-6)
    g45 = strat_mod._guard_s(4.5)
    assert g45 == pytest.approx(min(4.5 - 0.5, 4.5, 0.6 * 4.5), abs=1e-6)
    assert g45 < 4.5


def test_choose_action_returns_under_short_guard(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """choose_action must return a legal action even when wall budget is short."""
    import strategy as strat_mod

    importlib.reload(strat_mod)
    table = _hu_open_table()
    # ~1.2s remaining after harness padding → short guard, still legal.
    table["actionDeadlineAt"] = time.time() + 1.2
    t0 = time.perf_counter()
    out = strat_mod.choose_action(table)
    elapsed = time.perf_counter() - t0
    if isinstance(out, dict):
        assert out.get("action") in _LEGAL
    else:
        assert out in _LEGAL
    assert elapsed < 2.0, f"short-guard choose_action too slow: {elapsed:.3f}s"
