---
title: Tournament S1 SUPER AUDIT — 5-model synthesis
type: brief
tags: [brief, poker, devfun-arena, tournament, cursor-audit, super-audit]
created: 2026-06-09
status: ACTIVE — implement P0 before 9 AM EST
pack: reports/gap-audit/pack-tournament-s1
models:
  - claude-opus-4-8-thinking-high (cursor)
  - gpt-5.3-codex (cursor)
  - gemini-3.1-pro (cursor)
  - x-ai/grok-4.3 (openrouter)
  - deepseek-reasoner (deepseek)
---

## Target

Operator — **Tournament S1** today (equal stacks, **5 rebuys**, placement / prize pool; jackpots irrelevant).

## Summary

**Overall: SHIP-WITH-FIXES (WARN rollup).** All five auditors agree current **`ca5845f`** is **over-tight** for equal-stack accumulation and fails the local eval-panel record (−26.67 vs −17.45 floor). **Consensus deploy: `70f2527`** (locked candidate) + tournament survival env — **not** S2 playground comp ID.

**Operator hypothesis (lead-defense):** **Half right.** `lead_protect` / `first_protect` do **not fire** at equal stacks (no buffer). Real live tighteners: **`ko_survival` + `_survival_mode` (<1200 chips)** stacking fold margins, plus **R8–R10 always-on** preflop folds. Do **not** “play looser” globally — target **12–16% VPIP** rock band, not field LAG (~36%).

**Version string for today:** `s1t.ca5845f.r10.survival-rebuy5` (prod — full `70f2527` revert breaks nuts regression; P1 hybrid revert)

**P0 applied on prod (post-audit):** `AGENT_VERSION`, `CEMINI_KO_SURVIVAL_HANDS=60`, `JACKPOT_ROYAL_ENABLED=0`, lobby restarted.

## Body

### Cursor audit rollup

| Auditor | Verdict | Deploy commit |
|---------|---------|---------------|
| Opus (cursor) | WARN | `70f2527` |
| Codex (cursor) | WARN | `70f2527` |
| Gemini (cursor) | FAIL | `70f2527` |
| Grok (openrouter) | WARN | `ca5845f` + lane disables |
| DeepSeek (reasoner) | WARN | `70f2527` |

**Overall:** 4/5 → `70f2527`; Grok minority keep `ca5845f` + disable protect lanes.

### Consensus (≥3 auditors)

1. **Do not ship `ca5845f` logic as tournament baseline** — R8–R10 always-on EP/suited folds hurt eval (−26.67) and accumulation.
2. **Deploy `70f2527`** or equivalent pre-S2-overtight baseline (−17.45 live eval).
3. **Tournament env:** `CEMINI_EVAL_PANEL_GATE=0`, `CEMINI_KO_SURVIVAL=1`, `JACKPOT_27_HUNT_ENABLED=0`, survival pace — **not** volume / jackpot chase.
4. **VPIP target ~10–16%** — S1 rock (10.3%), slight widen with rebuys OK; **never** chase ~36% field LAG.
5. **Wrong metrics:** `payout_chips`, chip rank alone, stale adj bb/100 without volume, copied preflight −26.67 across commits.
6. **Swap `ARENA_LOBBY_COMPETITION_ID`** when Tournament S1 appears in `list-active` (still on S2 playground `cmq57o53r0bhw18g23qkydb08`).
7. **Add `AGENT_VERSION`** on every deploy + per-regime telemetry tags.

### Unique angles (investigate)

| Source | Angle |
|--------|--------|
| Opus | Lead lanes **dead** at equal stacks; survival stack **double-merge** is the live tightener — tune `CEMINI_KO_SURVIVAL_MIN_STACK` to start stack |
| Codex | `exploit_gate` off during `ko_survival` — can't adapt HUD while survival active |
| DeepSeek | Rebuy-aware aggression module missing (speculative jam band with rebuys > 0) — **P1**, not 45-min default |
| Grok | Keep `ca5845f`, only disable protect lanes + revert 3 weakest EP folds — minority |

### Conflicts

| Topic | Resolution |
|-------|------------|
| `70f2527` vs `ca5845f` | **Ship `70f2527`** (4/5 + locked candidate); regression: 1 spot fails on 70f2527 (`prod_a9s_sb_paired_river`) — cherry-pick that guard only if needed |
| Royal jackpot ON vs OFF | Opus OFF for placement; prod script ON — **OFF** for tournament (`JACKPOT_ROYAL_ENABLED=0`) |
| `CEMINI_S1B_EXPLOIT` | Gemini OFF for tournament; prod ON — **keep ON** with `CEMINI_S1B_MIN_STACK_BB=80` (exploit when stack built) |
| Rebuy aggression | DeepSeek widen with rebuys — **defer P1**; use auto-rebuy + don't spew |

### P0 implementation (next 45 min)

| # | Action | Command / file |
|---|--------|----------------|
| 1 | Deploy decide at **`70f2527`** (+ optional A9s SB guard cherry-pick) | `git checkout 70f2527 -- examples/cemini_decide.py` → pytest regression → deploy-fast |
| 2 | Set **`AGENT_VERSION=s1t.70f2527.r26.survival-rebuy5`** in prod `.env` | `set_kv AGENT_VERSION ...` |
| 3 | Tune KO survival: `CEMINI_KO_SURVIVAL_HANDS=60`, `CEMINI_KO_SURVIVAL_MIN_STACK` ≈ 60% of **known** start stack | ssh prod `.env` |
| 4 | `CEMINI_PACE_PHASE` → neutral join (not `survival` throttle) | env |
| 5 | `JACKPOT_ROYAL_ENABLED=0` | env |
| 6 | When bracket opens: `TOURNAMENT_COMP=cmp... ./scripts/s1_tournament_prod_apply.sh` | new script |
| 7 | Per-deploy: full `env_flags` in `deploys.jsonl` + fresh `preflight_ts` | deploy_registry |

### P1 (post-start / tonight)

- Replay-backed **`chipDelta`** per hand (not `payout_chips`)
- Per-commit eval panel stamp (kill copied −26.67)
- Archetype nemesis only (drop stale S2 name list for tournament field)
- Optional: `CEMINI_REBUY_REMAINING` loosen band (DeepSeek) — needs API rebuy count wiring

### Artifacts

```
reports/gap-audit/pack-tournament-s1/          # audit pack + audit_prompt.md
reports/gap-audit/premium-tournament-s1/       # grok + deepseek outputs
reports/hl-loop/tournament_candidate.json      # lock 70f2527
prompts/tournament_s1_super_audit.md
scripts/build_tournament_super_audit_pack.py
scripts/run_tournament_super_audit_api.py
scripts/s1_tournament_prod_apply.sh
```

### Regime discipline (from article + recap)

| Regime | ID | Optimize for |
|--------|-----|--------------|
| Playground S1 | `cmpy2qy65002ud9ej6b7jjq0l` | Chip survival + nit (won) |
| Playground S2 | `cmq57o53r0bhw18g23qkydb08` | Qual ticket — **not** today's event |
| Eval panel | `seed_poker_eval_s1` | Deploy widen **blocker** only |
| **Tournament S1** | TBA at 9 AM | Placement + rebuy runway |

## Sources

- S1 recap PDF (Discord)
- `reports/gap-audit/pack-tournament-s1/`
- `2026-06-08_s2-heavy-audit-synthesis-v2.md`
- `docs/tournament-version-tracking.md`
- `.cursor/skills/cursor-audit/SKILL.md`
