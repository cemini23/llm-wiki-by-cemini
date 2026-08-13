"""RSM helper role map tests (CCC K276 / Cybersec K277, arXiv 2608.12311)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from helper_roles import (  # noqa: E402
    assert_role,
    negative_constraints_for,
    normalize_action,
    normalize_role,
)


def test_decide_cannot_edit_env():
    r = assert_role("decide", "edit_env")
    assert r["ok"] is False
    assert "edit_env" in r["reason"] or "operator" in r["reason"]


def test_export_cannot_restart_lobby():
    r = assert_role("export", "restart_lobby")
    assert r["ok"] is False


def test_operator_can_durable():
    assert assert_role("operator", "edit_env")["ok"] is True
    assert assert_role("operator", "restart_lobby")["ok"] is True
    assert assert_role("operator", "write_wiki")["ok"] is True


def test_review_cannot_live_discord():
    # Even with operator confirmation — LIVE Discord is operator-only.
    r = assert_role("review", "live_discord", operator_confirmed=True)
    assert r["ok"] is False
    assert "operator" in r["reason"]


def test_operator_live_discord_needs_live_ok():
    assert assert_role("operator", "live_discord")["ok"] is False
    assert assert_role("operator", "live_discord", live_ok=True)["ok"] is True


def test_review_durable_needs_operator_confirmation():
    assert assert_role("review", "write_wiki")["ok"] is False
    r = assert_role("review", "write_wiki", operator_confirmed=True)
    assert r["ok"] is True
    assert "confirmation" in r["reason"]


def test_decide_may_table_actions():
    for action in ("fold", "call", "raise", "check"):
        assert assert_role("decide", action)["ok"] is True, action


def test_lobby_scope():
    assert assert_role("lobby", "join")["ok"] is True
    r = assert_role("lobby", "rewrite decide policy")
    assert r["ok"] is False
    assert r["action"] == "change_strategy"


def test_review_cannot_execute_table_actions():
    r = assert_role("review", "fold")
    assert r["ok"] is False
    assert "table actions" in r["reason"]


def test_export_cannot_change_strategy():
    r = assert_role("export", "change strategy")
    assert r["ok"] is False
    assert r["action"] == "change_strategy"


def test_unknown_role_and_action_fail_closed():
    assert assert_role("janitor", "fold")["ok"] is False
    assert assert_role("decide", "")["ok"] is False


def test_alias_normalization():
    assert normalize_role("Reviewer") == "review"
    assert normalize_role("human") == "operator"
    assert normalize_action("edit .env") == "edit_env"
    assert normalize_action("live discord") == "live_discord"
    # Broad tokens must not authorize LIVE / restart.
    assert normalize_action("live") == "live"
    assert normalize_action("restart") == "restart"
    assert normalize_action("systemd") == "systemd"


def test_bare_live_does_not_authorize_discord():
    r = assert_role("operator", "live", live_ok=True)
    assert r["ok"] is False


def test_negative_constraints_prompt_hardening():
    constraints = negative_constraints_for("decide")
    assert "restart systemd" in constraints
    assert "durable wiki" in constraints
    assert negative_constraints_for("operator") == []
