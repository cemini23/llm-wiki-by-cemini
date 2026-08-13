"""CDH skill invocation budget (CCC K274, arXiv 2608.12273 pattern).

Dual-ID:
- CCC K274 = CDH (2608.12273)                          <- this module
- CCC K275 = VAKRA (2608.12282)                        -> examples/vakra_eval_axes.py
- CCC K276 = RSM (2608.12311)                          -> examples/helper_roles.py
- Cybersec K276 = withhold contract (2608.12292)       -> examples/withhold_contract.py
- Cybersec K277 = RSM (same 2608.12311)                -> examples/helper_roles.py

Enforce invocation + token budgets on untrusted skill calls — trajectory
necessity, not just output correctness. Skills outside the allowlist get
``max_calls`` / ``max_tokens`` per skill name (process lifetime, in-memory,
no network). Supply-chain control: fail-closed on missing skill names.

Pattern only — no CDH dataset / harness install. Paper metrics ≠ poker EV.
"""
from __future__ import annotations

from typing import Any

# Skills that carry their own standing — not subject to the untrusted budget.
ALLOWLIST: frozenset[str] = frozenset(
    {"decide", "lobby", "export", "claimed_authorization", "withhold_contract"}
)


def normalize_skill_name(name: Any) -> str:
    if name is None:
        return ""
    return str(name).strip().lower().replace("-", "_").replace(" ", "_")


def estimate_tokens(text: Any) -> int:
    """Token estimate for a skill payload (len // 4, floor 1)."""
    n = len(str(text or "")) // 4
    return max(1, n)


class SkillBudget:
    """Per-skill invocation + token budget for untrusted skill calls."""

    def __init__(
        self,
        max_calls: int = 3,
        max_tokens: int = 4000,
        allowlist: Any = ALLOWLIST,
    ) -> None:
        self.max_calls = max_calls
        self.max_tokens = max_tokens
        self.allowlist: frozenset[str] = frozenset(
            normalize_skill_name(s) for s in allowlist if normalize_skill_name(s)
        )
        self._calls: dict[str, int] = {}
        self._tokens: dict[str, int] = {}

    def allow(self, skill: Any, tokens: int = 0) -> dict[str, Any]:
        """Allow or deny one skill invocation.

        Returns ``{ok, reason, skill, calls, tokens}`` where calls/tokens are
        the skill's totals *after* this invocation (or current totals when
        denied). Deny reasons: ``missing_skill``, ``budget_exceeded``.
        """
        name = normalize_skill_name(skill)
        calls_used = self._calls.get(name, 0)
        tokens_used = self._tokens.get(name, 0)
        spend = max(0, int(tokens or 0))

        if not name:
            return {
                "ok": False,
                "reason": "missing_skill",
                "skill": "",
                "calls": 0,
                "tokens": 0,
            }

        if name in self.allowlist:
            # Allowlisted skills carry their own standing — no cap.
            self._calls[name] = calls_used + 1
            self._tokens[name] = tokens_used + spend
            return {
                "ok": True,
                "reason": "allowlisted",
                "skill": name,
                "calls": self._calls[name],
                "tokens": self._tokens[name],
            }

        if calls_used >= self.max_calls:
            return {
                "ok": False,
                "reason": "budget_exceeded",
                "skill": name,
                "calls": calls_used,
                "tokens": tokens_used,
            }
        if tokens_used + spend > self.max_tokens:
            return {
                "ok": False,
                "reason": "budget_exceeded",
                "skill": name,
                "calls": calls_used,
                "tokens": tokens_used,
            }

        self._calls[name] = calls_used + 1
        self._tokens[name] = tokens_used + spend
        return {
            "ok": True,
            "reason": "within_budget",
            "skill": name,
            "calls": self._calls[name],
            "tokens": self._tokens[name],
        }

    def allow_text(self, skill: Any, text: Any) -> dict[str, Any]:
        """Convenience: budget a skill call by its payload text."""
        return self.allow(skill, tokens=estimate_tokens(text))
