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
