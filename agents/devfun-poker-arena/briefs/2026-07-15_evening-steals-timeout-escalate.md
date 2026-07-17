# Evening steals + timeout escalate — ship brief (2026-07-15)

## Target

CeminiSuite / Arena — Researcher HU ladder S1. **Cursor-owned `--replace` only** after review. Grok implementer: **no `--replace`**.

## Summary

Evening wave: timeout harden (WP0) + K156 risk-spectrum tags + K167 belief audit + K139 DeepSearch scaffold/staged reflection. Skipped K168/K169. Engine stays **cemini** (`CEMINI_SANDBOX_ENGINE=cemini`). No gin flip, no runtime LLM.

| Artifact | Result |
|----------|--------|
| Timeout harden | `deadline_s < 3` → sims=80, skip chat/HL I/O/jackpot hunt; SIGALRM emergency fold/check unchanged |
| K156 risk_spectrum | TEN high/low, maniac_shark medium/high on `research/opponents/*` |
| K167 belief_audit | `examples/belief_deviation_audit.py` + HL brief + JSONL path |
| K139 scaffold | `config/hu_deepsearch_trajectory_filter.json` + filter drop + HL template |
| Critical pytest | **60 passed** (deadline, mafp, postflop, risk, belief, deepsearch scaffold, HU guards, K161) |
| HU sandbox gate | **GATE_EXIT:1** — hard fail: `series_win_rate vs lag 40.0% < 45.0%` |
| Trajectory/axis | **PASS** (M8=0, hierarchical memory ok) |
| TEN advisory | +17 … +30.8 bb/100 (seed variance; ≥0 target) |
| maniac_shark advisory | −14 … +3.8 bb/100 (advisory only) |
| tight selfplay | +42.0 bb/100 |
| Bundle | `dist/sandbox-pvp-bundle.zip` build-only OK (includes `risk_spectrum`, `belief_deviation_audit`, tight `cemini_decide`) |
| `--replace` | **not run** — `NO_REPLACE=confirmed` |

### Timeout fix summary

1. **Audit:** MAFP overlay + postflop buckets already path/mtime-cached; fail-open. Test asserts no re-`open()` of research JSON after warmup.
2. **Tight path (`deadline_s < 3`):** equity sims → 80 (`CEMINI_TIGHT_DEADLINE_SIMS`); skip PokerSkill/HL style/chat intel; skip `maybe_hunt_action`; nuts enum requires `≥3s`.
3. **SIGALRM:** `harness/strategy.py` `_run_decide_guarded` still wraps cemini; emergency check/fold on alarm or `guard_s≤0`.
4. **Tests:** `tests/test_sandbox_deadline_guard.py` (choose_action + decide under short deadline + alarm).

### Risk spectrum profiles (K156)

| Profile | participation | proactiveness | vpip | pfr |
|---------|---------------|---------------|------|-----|
| TEN | high | low | 0.516 | 0.0 |
| maniac_shark | medium | high | 0.306 | 0.151 |

Helper: `examples/risk_spectrum.py`. Doc: `references/risk-spectrum-tags.md`. Tags only — no decide() aggression copy.

### Belief audit (K167)

- Module: `examples/belief_deviation_audit.py`
- JSONL: `reports/hl-loop/belief_deviation.jsonl`
- Wired into `cemini_hl_brief.py` + message-DAG `belief_audit` node
- Tags: `harmful_mistake` | `justified_override` | `strategic`
- Isolation: opponent `message` stripped from extra

### Scaffold config delta (K139)

`config/hu_deepsearch_trajectory_filter.json`:

- `scaffold_fields`: completed_list / todo_list / experience / information
- `drop_if` += `missing_experience_after_repeat_fails` (≥2 same-spot fails)
- `staged_reflection`: soft first fail → strong_grounded on repeat
- `advisory_only`: **true** (K161 `required_tags` unchanged as source of truth)

## Gate detail (bundle `reports/researcher-round/gate-hu-20260715T234422Z` + re-run)

| Check | Status |
|-------|--------|
| HU regression pytest | PASS |
| Substrate / K148 | PASS |
| Trajectory `--gate` | PASS |
| TEN advisory | PASS (≥0 on first full run) |
| maniac_shark advisory | variable (not hard gate) |
| maniac/lag series audit | **FAIL** lag series 40% &lt; 45% (deterministic under seed=42 on this tree) |
| build-only zip | PASS |

**Note:** Solver-bake escalate reported lag series 60% GATE PASS. This wave did **not** change decide aggression for full-deadline selfplay (`deadline_s=10`); lag series fail is residual / match-variance (2/5). Cursor should re-run gate once before `--replace`; do **not** micro-patch river guards to chase 45%.

## Proposed pin

`researcher-ladder-s1.evening-steals.2026-07-15`

## Live posture (pre-replace)

| Field | Value |
|-------|-------|
| Active/failed sub | `daf19c7e-9039-4252-a45d-c00227ae9b97` |
| Pin was | `researcher-ladder-s1.solver-bake.2026-07-15` |
| PvP fail | 422 static timeout @ 122 hands |

Success after Cursor replace: no 422 in first 500+ hands + μ trajectory after 2k.

## Hard confirmations

- `NO_REPLACE=confirmed` (Grok did not run `submit_sandbox_pvp.py --replace`)
- No gin engine flip
- No K169 runtime LLM / SLM
- No K168 tooling

## Sources

- `briefs/2026-07-15_evening-steals-timeout-master-plan.md`
- K156 / K167 / K139 steal briefs (same day)
- `references/risk-spectrum-tags.md`, `references/deepsearch-trajectory-filter.md`
