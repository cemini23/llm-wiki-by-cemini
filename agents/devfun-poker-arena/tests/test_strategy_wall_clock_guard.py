"""Wall-clock guard + ladder PvP monitor tests (super-audit REWORK fixes)."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))
sys.path.insert(0, str(ROOT / "examples"))

from strategy import (  # noqa: E402
    _emergency_action,
    _guard_s,
    _run_decide_guarded,
    _USE_SIGALRM,
)
from researcher_sandbox_auto_submit import pvp_progress  # noqa: E402


def test_guard_s_zero_on_expired_deadline():
    assert _guard_s(0.0) == 0.0


def test_guard_s_v2_cap_and_scale():
    # Long deadline: hard-cap 4.5 (was up to 7.5).
    assert _guard_s(10.0) == pytest.approx(4.5)
    # Mid deadline: min(d-0.5, 4.5, 0.6*d)
    assert _guard_s(5.0) == pytest.approx(min(4.5, 0.6 * 5.0, 5.0 - 0.5))
    # Very short: no positive guard when headroom exhausted.
    assert _guard_s(0.3) == 0.0


def test_emergency_action_prefers_check_then_fold():
    table = {"allowedActions": {"availableActions": ["check", "fold"], "canCheck": True}}
    assert _emergency_action(table)["action"] == "check"
    table2 = {"allowedActions": {"availableActions": ["fold"], "canFold": True}}
    assert _emergency_action(table2)["action"] == "fold"


@pytest.mark.skipif(not _USE_SIGALRM, reason="SIGALRM unavailable")
def test_run_decide_guarded_returns_before_slow_decide():
    def slow_decide(_table, deadline_s=10.0):
        time.sleep(2.0)
        return {"action": "raise", "amount": 10}

    t0 = time.monotonic()
    out = _run_decide_guarded(slow_decide, {}, deadline_s=8.0, guard_s=0.2)
    elapsed = time.monotonic() - t0
    assert elapsed < 1.0
    assert out["action"] in ("check", "fold", "call")


def test_pvp_progress_prefers_pvp_status_over_bench_succeeded():
    rec = {
        "status": "Succeeded",
        "completedHands": 5,
        "targetHands": 5,
        "pvp": {
            "status": "Failed",
            "completedHands": 1677,
            "adjustedBbPer100": 51.9,
            "error": "static submission timed out",
        },
    }
    ch, th, status = pvp_progress(rec)
    assert status == "Failed"
    assert ch == 1677


def test_pvp_progress_bench_phase_without_pvp_block():
    rec = {"status": "Running", "completedHands": 2, "targetHands": 5, "pvp": None}
    _, _, status = pvp_progress(rec)
    assert status == "Running"


def test_poll_pinned_ladder_pvp_alerts_new_submission_same_failed_status(tmp_path, monkeypatch):
    import arena_monitor as am

    pin_file = tmp_path / "pin.json"
    sid = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    pin_file.write_text(
        json.dumps({"activeSubmissionId": sid, "competitionId": "comp1"}),
        encoding="utf-8",
    )
    monkeypatch.setattr(am, "_PIN_PATH", pin_file)
    (tmp_path / "monitor_state.json").write_text(
        json.dumps(
            {
                "ladder_pvp": {
                    "submissionId": "00000000-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "pvpStatus": "Failed",
                }
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "submit_sandbox_pvp.poll_submission",
        lambda submission_id: {
            "status": "Succeeded",
            "pvp": {
                "status": "Failed",
                "completedHands": 10,
                "error": "timeout again",
            },
        },
    )

    am.poll_pinned_ladder_pvp(reports=tmp_path)
    alerts = (tmp_path / "alerts.txt").read_text(encoding="utf-8")
    assert "LADDER PVP FAILED" in alerts
    assert sid[:8] in alerts
