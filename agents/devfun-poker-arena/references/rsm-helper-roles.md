# RSM helper roles (CCC K276 / Cybersec K277)

**Dual-ID:**
- CCC K276 = RSM (2608.12311) ← this ref
- Cybersec K277 = RSM (same 2608.12311) ← this ref
- CCC K274 = CDH (2608.12273) → `references/cdh-skill-budget.md`
- CCC K275 = VAKRA (2608.12282) → `references/vakra-eval-axes.md`
- Cybersec K276 = withhold contract (2608.12292) → `references/withhold-contract.md`

**Code:** `examples/helper_roles.py`
**Tests:** `tests/test_helper_roles.py`

## Steal

Assign each helper an explicit capability-matched role with scope boundaries
— role drift (one helper silently absorbing another's job) is driven by
absent boundaries + functional overlap + context-switch inertia:

| Role | Domain | May | Must not |
|------|--------|-----|----------|
| `decide` | table action | fold/call/raise/check | edit `.env`, restart systemd, durable wiki |
| `lobby` | join/queue/rebuy policy | join/pace/protect | rewrite decide policy, LIVE Discord |
| `export` | telemetry | write jsonl under reports/exports | change strategy knobs |
| `review` | HITL / independent check | accept/reject durable patch | execute table actions |
| `operator` | human | all durable + LIVE with LIVE OK | n/a |

1. Durable actions (`write_wiki`, `edit_env`, `restart_lobby`,
   `live_discord`) require `operator` or `review` + an operator confirmation
   flag — `assert_role(role, action, operator_confirmed=...)`.
2. `live_discord` is operator-only and additionally needs `live_ok` (LIVE OK);
   review's confirmation flag does not extend to LIVE surfaces.
3. Prompt hardening: `negative_constraints_for(role)` returns the "must not"
   strings for injection into helper prompts.
4. Unknown roles/actions fail-closed (`unknown_role` / `unknown_action`).

Paper metrics ≠ poker EV — role discipline is a process control, not an edge.

## Do not

- Let one helper silently absorb another's domain.
- Let `review` confirm LIVE surfaces (operator + LIVE OK only).
- Omit the negative-constraint strings from helper prompts.

## Check

```bash
uv run pytest tests/test_helper_roles.py -q --tb=short
```
