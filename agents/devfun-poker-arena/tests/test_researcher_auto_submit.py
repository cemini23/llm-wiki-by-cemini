"""Smoke tests for Researcher sandbox auto-submit wiring."""
from __future__ import annotations

from pathlib import Path

AGENT_ROOT = Path(__file__).resolve().parents[1]


def test_pin_file_exists() -> None:
    pin = AGENT_ROOT / "config" / "researcher_sandbox_submit.pin.json"
    assert pin.is_file()
    text = pin.read_text(encoding="utf-8")
    assert "competitionId" in text
    assert "static-agent" in text


def test_auto_submit_script_uses_orchestrator() -> None:
    script = (AGENT_ROOT / "scripts" / "run_researcher_sandbox_auto_submit.sh").read_text(
        encoding="utf-8"
    )
    assert "researcher_sandbox_auto_submit.py" in script
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
