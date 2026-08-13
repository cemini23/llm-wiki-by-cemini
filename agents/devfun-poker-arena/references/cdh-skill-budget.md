# CDH skill invocation budget (CCC K274)

**Dual-ID:**
- CCC K274 = CDH (2608.12273) ← this ref
- CCC K275 = VAKRA (2608.12282) → `references/vakra-eval-axes.md`
- CCC K276 = RSM (2608.12311) → `references/rsm-helper-roles.md`
- Cybersec K276 = withhold contract (2608.12292) → `references/withhold-contract.md`
- Cybersec K277 = RSM (same 2608.12311) → `references/rsm-helper-roles.md`

**Code:** `examples/skill_invocation_budget.py`
**Tests:** `tests/test_skill_invocation_budget.py`

## Steal

Enforce token/invocation budgets on untrusted skill calls — **trajectory
necessity**, not just output correctness:

1. Count invocations (and optional token estimate `len(text) // 4`) **per
   skill name** — the budget is per untrusted skill, not global.
2. Skills outside the allowlist
   (`decide`, `lobby`, `export`, `claimed_authorization`, `withhold_contract`)
   get `SkillBudget(max_calls=3, max_tokens=4000)`; exceeding either →
   `{ok: False, reason: "budget_exceeded"}`.
3. Allowlisted skills carry their own standing — no cap.
4. **Fail-closed on missing skill name** (`missing_skill`) — CDH is a
   supply-chain control, not a convenience gate.

In-memory only (process lifetime), no network.

## Do not

- Fail-open on empty/unknown skill names.
- Apply the budget to allowlisted skills (decide/lobby/export keep standing).
- Treat the budget as a substitute for output correctness checks.

## Check

```bash
uv run pytest tests/test_skill_invocation_budget.py -q --tb=short
```
