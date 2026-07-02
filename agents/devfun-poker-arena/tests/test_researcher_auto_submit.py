"""Smoke tests for Researcher sandbox auto-submit wiring."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

AGENT_ROOT = Path(__file__).resolve().parents[1]


def test_pin_file_exists() -> None:
    pin = AGENT_ROOT / "config" / "researcher_sandbox_submit.pin.json"
    assert pin.is_file()
    text = pin.read_text(encoding="utf-8")
    assert "competitionId" in text
    assert "static-agent" in text
    data = json.loads(text)
    assert data.get("replace") is False


def test_auto_submit_script_uses_orchestrator() -> None:
    script = (AGENT_ROOT / "scripts" / "run_researcher_sandbox_auto_submit.sh").read_text(
        encoding="utf-8"
    )
    assert "researcher_sandbox_auto_submit.py" in script
    assert "verify_sandbox_bundle_layout.sh" in script
    assert "waiting_for_finish" in (
        AGENT_ROOT / "examples" / "researcher_sandbox_auto_submit.py"
    ).read_text(encoding="utf-8")


def test_orchestrator_module_exists() -> None:
    assert (AGENT_ROOT / "examples" / "researcher_sandbox_auto_submit.py").is_file()


def test_systemd_units_exist() -> None:
    assert (AGENT_ROOT / "deploy" / "cemini-researcher-sandbox-submit.service").is_file()
    assert (AGENT_ROOT / "deploy" / "cemini-researcher-sandbox-submit.timer").is_file()


def test_deploy_installs_auto_submit_units() -> None:
    deploy = (AGENT_ROOT / "deploy" / "deploy_to_cemini_prod.sh").read_text(encoding="utf-8")
    assert "cemini-researcher-sandbox-submit.service" in deploy
    assert "cemini-researcher-sandbox-submit.timer" in deploy


def test_find_active_when_benchflow_succeeded_pvp_still_active(monkeypatch) -> None:
    """Benchflow 5/5 Succeeded must not hide in-flight PvP season."""
    import sys

    sys.path.insert(0, str(AGENT_ROOT / "examples"))
    import researcher_sandbox_auto_submit as ras

    comp = "cmr0jmqlt08bi13n8neory9xb"
    sid = "8545120c-e3cd-4c1a-bb3c-d2d5254f18ca"
    fake = {
        "id": sid,
        "status": "Succeeded",
        "competitionId": comp,
        "pvp": {
            "status": "Active",
            "completedHands": 1378,
            "targetHands": 5000,
        },
    }

    monkeypatch.setattr(
        ras,
        "_poll_submission_safe",
        lambda submission_id: fake if submission_id == sid else None,
    )
    monkeypatch.setattr(ras, "fetch_agent_submissions", lambda _cid: [])

    pin = {"activeSubmissionId": sid, "competitionId": comp}
    active = ras.find_active_pvp_submission(comp, pin=pin, state=None)
    assert active is not None
    assert active["id"] == sid


@pytest.mark.parametrize(
    ("status", "ch", "th", "expected"),
    [
        ("Active", 100, 5000, False),
        ("paused", 100, 5000, False),
        ("Paused", 2500, 5000, False),
        ("queued", 0, 5000, False),
        ("finished", 5000, 5000, True),
        ("failed", 100, 5000, True),
        ("", 5000, 5000, True),
    ],
)
def test_pvp_is_finished_paused_and_queued_in_flight(
    status: str, ch: int, th: int, expected: bool
) -> None:
    import sys

    sys.path.insert(0, str(AGENT_ROOT / "examples"))
    import researcher_sandbox_auto_submit as ras

    rec = {"pvp": {"status": status, "completedHands": ch, "targetHands": th}}
    assert ras.pvp_is_finished(rec) is expected


def test_write_pin_atomic_and_sync(tmp_path: Path) -> None:
    import sys

    sys.path.insert(0, str(AGENT_ROOT / "examples"))
    import researcher_sandbox_auto_submit as ras

    pin_path = tmp_path / "submit.pin.json"
    pin = {
        "competitionId": "comp-test",
        "replace": False,
        "activeSubmissionId": "old-id",
        "watchSubmissionIds": ["old-id"],
        "agentVersion": "test-agent",
        "gitCommit": "abc1234",
    }
    ras.write_pin_atomic(pin_path, pin)
    assert pin_path.is_file()
    assert json.loads(pin_path.read_text())["activeSubmissionId"] == "old-id"

    updated = ras.sync_pin_from_submission(
        pin_path,
        pin,
        "new-submission-id",
        git_commit="def5678",
        agent_version="test-agent-v2",
    )
    on_disk = json.loads(pin_path.read_text(encoding="utf-8"))
    assert updated["activeSubmissionId"] == "new-submission-id"
    assert on_disk["activeSubmissionId"] == "new-submission-id"
    assert on_disk["gitCommit"] == "def5678"
    assert on_disk["agentVersion"] == "test-agent-v2"
    assert on_disk["watchSubmissionIds"][0] == "new-submission-id"


def test_heal_pin_on_active_detect(tmp_path: Path) -> None:
    import sys

    sys.path.insert(0, str(AGENT_ROOT / "examples"))
    import researcher_sandbox_auto_submit as ras

    pin_path = tmp_path / "submit.pin.json"
    pin = {
        "competitionId": "comp-test",
        "activeSubmissionId": "stale-id",
        "watchSubmissionIds": ["stale-id"],
    }
    ras.write_pin_atomic(pin_path, pin)
    active = {"id": "live-id", "pvp": {"status": "Active", "completedHands": 10, "targetHands": 5000}}
    healed = ras.heal_pin_on_active_detect(pin_path, pin, active)
    assert healed["activeSubmissionId"] == "live-id"
    assert json.loads(pin_path.read_text())["activeSubmissionId"] == "live-id"


def test_season_counters_increment_on_finished_prior() -> None:
    import sys

    sys.path.insert(0, str(AGENT_ROOT / "examples"))
    import researcher_sandbox_auto_submit as ras

    prev = {"finalizedSeasons": 2, "cumulativeHands": 10000}
    finished = {
        "id": "done-id",
        "pvp": {"status": "finished", "completedHands": 5000, "targetHands": 5000},
    }
    payload = ras._attach_season_counters({"status": "submitted"}, prev, increment_from=finished)
    assert payload["finalizedSeasons"] == 3
    assert payload["cumulativeHands"] == 15000

