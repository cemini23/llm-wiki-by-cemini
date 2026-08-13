"""CDH skill invocation budget tests (CCC K274, arXiv 2608.12273 pattern)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from skill_invocation_budget import (  # noqa: E402
    SkillBudget,
    estimate_tokens,
    normalize_skill_name,
)


def test_allowlist_unlimited():
    budget = SkillBudget(max_calls=3, max_tokens=4000)
    for _ in range(5):
        r = budget.allow("decide", tokens=50000)
        assert r["ok"] is True
        assert r["reason"] == "allowlisted"


def test_untrusted_fourth_call_denied():
    budget = SkillBudget(max_calls=3, max_tokens=4000)
    for i in range(3):
        r = budget.allow("table_chat_intel", tokens=10)
        assert r["ok"] is True, f"call {i + 1} should pass"
    r = budget.allow("table_chat_intel", tokens=10)
    assert r["ok"] is False
    assert r["reason"] == "budget_exceeded"


def test_token_cap_denied():
    budget = SkillBudget(max_calls=10, max_tokens=4000)
    assert budget.allow("table_chat_intel", tokens=3000)["ok"] is True
    r = budget.allow("table_chat_intel", tokens=1500)
    assert r["ok"] is False
    assert r["reason"] == "budget_exceeded"


def test_missing_skill_name_fail_closed():
    budget = SkillBudget()
    for skill in ("", None, "   "):
        r = budget.allow(skill)
        assert r["ok"] is False
        assert r["reason"] == "missing_skill"


def test_name_normalization_matches_allowlist():
    budget = SkillBudget(max_calls=1)
    r = budget.allow("Claimed-Authorization")
    assert r["ok"] is True
    assert r["skill"] == "claimed_authorization"
    assert normalize_skill_name("Claimed Authorization") == "claimed_authorization"


def test_per_skill_budgets_are_independent():
    budget = SkillBudget(max_calls=3, max_tokens=4000)
    for _ in range(3):
        assert budget.allow("table_chat_intel", tokens=1)["ok"] is True
    # A different untrusted skill still has its own budget.
    assert budget.allow("opponent_hud", tokens=1)["ok"] is True


def test_estimate_tokens_floor():
    assert estimate_tokens("12345678") == 2  # len // 4
    assert estimate_tokens("abc") == 1
    assert estimate_tokens(None) == 1
