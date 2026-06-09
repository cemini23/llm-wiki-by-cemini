---
title: Tournament S1 SUPER AUDIT — 5-model synthesis
type: brief
tags: [brief, poker, devfun-arena, tournament, cursor-audit, super-audit]
created: 2026-06-09
updated: 2026-06-09
status: SHIPPED — superseded P0 deploy table; see current posture below
pack: reports/gap-audit/pack-tournament-s1
ship_commit: 4a6df45
models:
  - claude-opus-4-8-thinking-high (cursor)
  - gpt-5.3-codex (cursor)
  - gemini-3.1-pro (cursor)
  - x-ai/grok-4.3 (openrouter)
  - deepseek-reasoner (deepseek)
---

## Target

Operator — **Tournament S1** (equal stacks, **5 rebuys**, placement / prize pool; jackpots irrelevant).

## Summary

**Audit rollup (2026-06-09 morning):** 4/5 auditors recommended reverting S2 over-tightening to **`70f2527`** (−17.45 eval-panel floor). **What shipped instead:** hybrid **lane-gate** on **`4a6df45`** — `lane_tight` (first/qual/lead/eval_panel) keeps R8–R10 EP/suited folds; **tournament baseline** (`CEMINI_TOURNAMENT_MODE=1`) does not.

**Current prod posture (post-ship):**

| Item | Value |
|------|--------|
| Git | `4a6df45` on `main`, deployed `cemini-prod` |
| `AGENT_VERSION` | `s1t.4a6df45.tournament-s1` (via `s1_tournament_prod_apply.sh`) |
| Tournament mode | `CEMINI_TOURNAMENT_MODE=1`, eval panel gate off |
| KO survival | `CEMINI_KO_SURVIVAL_HANDS=60`, min stack tuned for start stack |
| Jackpots | `JACKPOT_ROYAL_ENABLED=0`, `JACKPOT_27_HUNT_ENABLED=0` |
| Preflight | Tournament posture **−9.37** bb/100 (150h); eval_panel lane **−26.67** (expected — lane_tight on) |
| VPIP target | **12–16%** rock band — do not chase field LAG (~36%) |
| Lobby | Swap when bracket opens: `TOURNAMENT_COMP=cmp... ./scripts/s1_tournament_prod_apply.sh` |
| Oracle | S1 primary for deploy; S2 intel-only (`multi_comp_registry`) |

**Follow-up shipped same day:** open-spot preflop routing — `is_preflop_open_spot()` (not `call_chips==0`) so UTG first-in opens instead of limp path → PFR recovery. See `@agents/devfun-poker-arena/briefs/2026-06-09_open-spot-pfr-preflop-audit.md`.

**Operator hypothesis (lead-defense):** Half right — `lead_protect` / `first_protect` do not fire at equal stacks. Live tighteners were KO survival margins + always-on R8–R10; tournament mode + lane-gate addresses without full `70f2527` revert (nuts regression on full revert).

## Body

### Cursor audit rollup (historical)

| Auditor | Verdict | Deploy commit (audit) |
|---------|---------|------------------------|
| Opus (cursor) | WARN | `70f2527` |
| Codex (cursor) | WARN | `70f2527` |
| Gemini (cursor) | FAIL | `70f2527` |
| Grok (openrouter) | WARN | `ca5845f` + lane disables |
| DeepSeek (reasoner) | WARN | `70f2527` |

**Ship decision:** lane-gate hybrid on `4a6df45` — not raw `70f2527` checkout (regression: `prod_a9s_sb_paired_river`).

### Consensus (≥3 auditors) — still valid

1. Do not run S2 over-tight baseline as tournament default.
2. Tournament env: eval panel gate off, KO survival on, jackpots off, neutral pace.
3. VPIP **~12–16%** — S1 rock; rebuy runway via auto-rebuy, not spew.
4. Wrong metrics: `payout_chips`, chip rank alone, stale adj bb/100 without volume.
5. `AGENT_VERSION` + per-regime telemetry on every deploy.

### P0 (completed)

| # | Action | Status |
|---|--------|--------|
| 1 | Lane-gate decide + tournament env | **Done** `4a6df45` |
| 2 | `s1_tournament_prod_apply.sh` + multi-comp oracle | **Done** |
| 3 | Eval panel smoke + tournament preflight in metrics | **Done** |
| 4 | Open-spot preflop routing fix | **Done** (same session) |
| 5 | Bracket lobby swap when S1 comp live | **Pending** — run apply script |

### P1 (open)

- Replay-backed `chipDelta` per hand (export path has `chip_delta`; prod telemetry wiring)
- Per-commit eval panel stamp (avoid copied −26.67 across commits)
- Archetype nemesis only for tournament field
- Optional rebuy-aware aggression (DeepSeek) — needs API rebuy count

### Artifacts

```
reports/gap-audit/pack-tournament-s1/
reports/gap-audit/premium-tournament-s1/
reports/hl-loop/tournament_candidate.json   # updated to 4a6df45
scripts/s1_tournament_prod_apply.sh
scripts/run_s1_tournament_hl_cycle.sh
examples/multi_comp_registry.py
```

### Regime discipline

| Regime | ID | Optimize for |
|--------|-----|--------------|
| Playground S1 | `cmpy2qy65002ud9ej6b7jjq0l` | Chip survival + nit (won) |
| Playground S2 | `cmq57o53r0bhw18g23qkydb08` | Qual ticket — intel only |
| Eval panel | `seed_poker_eval_s1` | Deploy widen blocker only |
| **Tournament S1** | TBA at bracket | Placement + rebuy runway |

## Sources

- S1 recap PDF (Discord)
- `reports/gap-audit/pack-tournament-s1/`
- `2026-06-08_s2-heavy-audit-synthesis-v2.md`
- `docs/tournament-version-tracking.md`
