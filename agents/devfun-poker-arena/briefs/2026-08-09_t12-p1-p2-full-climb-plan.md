---
title: T12 full climb — P1/P2 detailed plan (post-P0)
type: brief
tags: [brief, poker, tournament-s12, p1, p2]
created: 2026-08-09
---

## Target

`agents/devfun-poker-arena/` — live Tournament S12 climb (gin stays killed)

## Summary

P0 shipped in `d8153fe` (placement cushion, blind defend, SB chase, posture, postflop log). This brief is the **complete remaining backlog** from Fable / GPT-SOL / Kimi / GLM. Implement **all P1 then all P2** via claude-ds. No gin. No large rebuys.

## Regime disclosure

**Single-regime** scope: Arena Playground S13 / Tournament S12 chip-score leaderboards only (not cash EV, not other sites). Per-regime: do not treat WR/cps gaps as transferable EV. Paper / multi-model audit metrics are not poker EV. Apply knobs inside existing Cemini playground/tournament postures only.

## P0 status (done — do not re-litigate)

| Item | Status |
|---|---|
| placement_protect ≥35% cushion | shipped |
| TAG_BLIND_DEFEND | shipped |
| SB chase opens | shipped |
| T12 posture knobs | shipped + prod env |
| postflop_decisions.jsonl | shipped |
| playground watch skip on tournament | shipped |

## Evidence still driving P1/P2

- Facing-raise **3bet rate 6.3%** (too low — call-heavy entries)
- WR 8.6% vs leaders ~20% → conversion / initiative gap
- Named nemesis tight can over-fold even when archetype evidence is thin
- Short-stack path still coarse after 12bb threshold
- Postflop log exists but no fold-to-cbet rollup yet
- Dozens of one-off fold guards in `cemini_decide.py` may block chase/defend (Fable)

---

## P1 — implement fully (high EV, testable)

### P1-1 Named-nemesis vs archetype split

**Problem:** `CEMINI_NEMESIS_TIGHT=1` (or handle list alone) forces tight folds vs stale names; T12 already sets tight=0 but code paths may still treat *any* nemesis handle as tight.

**Plan:**
1. Add `CEMINI_NAMED_NEMESIS_TIGHT` (default `0`). When `0`, listed handles do **not** alone force tight margins.
2. Keep archetype tight (`CEMINI_NEMESIS_ARCHETYPE=1` + linear_aggro / premium_nit / etc.) evidence-based.
3. Wire in `cemini_decide.py` wherever `_nemesis_tight` / handle membership forces fold/margin.
4. Tests: named handle alone → not tight; archetype flag → tight.

**Files:** `cemini_decide.py`, `nemesis_seed.py` (if needed), `tests/test_*nemesis*` or new.

### P1-2 Facing-raise 3bet / initiative tier

**Problem:** 6.3% 3bet when facing raise; call-heavy → OOP postflop bleed.

**Plan:**
1. Add helper `try_tournament_value_3bet(...)` (or extend existing trap/3bet helpers) gated by `CEMINI_TOURNAMENT_3BET=1` (on in s12 posture).
2. When facing raise ≤3.5bb, IP or BB, stack >12bb: 3bet value set = `{QQ+, AK, AQs, AJs, KQs, JJ, TT}` (tune to existing chart classes).
3. Prefer 3bet over call for that set; do **not** add polar bluff 3bets in P1 (Kimi polar is P2).
4. Cap: call_chips after 3bet sizing must be ≤35% stack; else call/fold by existing logic.
5. Tests for QQ/AKs 3bet IP; trash still folds; gin still off.

**Files:** `cemini_decide.py` and/or `blind_pressure.py` / small `tournament_3bet.py`, tests.

### P1-3 Short-stack jam tiers (≤8 / 8–12 bb)

**Problem:** Single `SHORT_STACK_BB=12` still may jam too wide near 11–12bb or too passive ≤8.

**Plan:**
1. In `short_stack.py`: split bands:
   - `≤8bb`: jam-or-fold only (existing push/fold chart, slightly wider BTN/SB)
   - `8–12bb`: selective raise/jam — premiums + suited broadway; fold trash opens
   - `>12bb`: not short-stack path
2. Env: `CEMINI_SHORT_STACK_JAM_BB=8` (default), keep `CEMINI_SHORT_STACK_BB=12`.
3. Tests at 7.9, 8, 11.9, 12, 19 bb boundaries.

**Files:** `short_stack.py`, `tests/test_short_stack*.py`.

### P1-4 Postflop telemetry rollup + richer log fields

**Problem:** jsonl alone doesn't diagnose fold-to-cbet.

**Plan:**
1. Enrich `_log_postflop_decision` fields: `pot_odds`, `equity` (if cheap), `facing_bet`, `board_len`, `hand_class` if known.
2. Add `examples/postflop_telemetry.py` with pure `fold_to_cbet_rate(rows) -> dict` (flop cbet face → fold%).
3. Optional script `scripts/summarize_postflop_log.py` reading export jsonl → print rates.
4. Tests on synthetic rows.

**Files:** `cemini_decide.py`, `examples/postflop_telemetry.py`, `tests/test_postflop_decision_log.py`.

### P1-5 Blind-defend initiative (3bet over call for strong)

**Problem:** Blind defend lane may flat too much with JJ+/AK.

**Plan:**
1. Inside `try_tag_blind_defend` (or decide wire): if hand in `{JJ+, AK, AQs}` and raise ≤3bb and stack≥15bb → return **raise** (3bet) not call when raise in available.
2. Keep call for medium defend set.
3. Tests: AKs BB vs 2.5bb → raise; 87s → call; 72o → None/fold.

**Files:** `tag_widen.py`, `tests/test_tag_widen.py`.

### P1-6 Early KO survival soften (tournament only)

**Problem:** Survival latch at mid stacks converts playable stacks into blind-out (Kimi/Fable).

**Plan:**
1. For `_s12_tournament` posture: `CEMINI_KO_SURVIVAL_HANDS=30` (was 60), keep `MIN_STACK=250`.
2. Document: survival is early-hand cold-start only, not permanent nit.
3. No playground change.

**Files:** `run_cemini_lobby.py` posture dict.

---

## P2 — implement fully after P1 (still this session)

### P2-1 Polar IP 3bet bluff slice (gated, small)

**Plan:** Under `CEMINI_TOURNAMENT_3BET_POLAR=1` (default **0** in prod until metrics; set **1** in s12 posture only if P1-2 tests green): add thin bluff 3bet set IP vs CO/BTN opens only — e.g. `A2s–A5s`, `K9s–KTs` — size small; fold to 4bet. Tests required. If unsure, ship helper + default off + posture sets 1.

### P2-2 Flat-dominate vs leader opens (IP)

**Plan:** When opener handle matches nemesis/leader prefixes and we are BTN/BB with medium strength: prefer **call** over fold/3bet for continue-range (`AT+, KQ, 55–JJ, suited connectors`). Gate `CEMINI_FLAT_DOMINATE=1` on in s12. Tests.

### P2-3 Fold-guard ledger (audit hook)

**Plan:**
1. Add `examples/fold_guard_ledger.py`: registry of named guard ids → when a guard forces fold, append fail-open jsonl `fold_guards.jsonl` with `{guard_id, hand_class, position, spot}`.
2. Instrument 5–10 highest-suspicion fold early-returns in `_preflop_open` / facing-raise path (ones that mention QJo, chart-trash, CO steal blocks).
3. No behavior change except logging — enables next audit.
4. Tests that ledger write is fail-open.

### P2-4 Session stop-win governor (optional, default off)

**Plan:** `CEMINI_STOP_WIN_MULT=0` default. If `>0` (e.g. 2.2) and tournament chips ≥ start×mult for `CEMINI_STOP_WIN_HANDS=20` consecutive, slow join retry to 600s (bank variance). **Default stays 0** on prod — code + tests only unless env set. Document in brief.

### P2-5 Persist villain open% sketch

**Plan:** Lightweight: append-only `reports/exports/<slug>/villain_actions.jsonl` lines `{handle, street, action, spot}` fail-open from decide when villain acts known. No full range_ledger ML. Helper to compute open% by handle from file. Tests with temp dir.

---

## Posture env additions (after deploy — LIVE OK for these keys only)

```
CEMINI_NAMED_NEMESIS_TIGHT=0
CEMINI_TOURNAMENT_3BET=1
CEMINI_SHORT_STACK_JAM_BB=8
CEMINI_KO_SURVIVAL_HANDS=30
CEMINI_FLAT_DOMINATE=1
CEMINI_TOURNAMENT_3BET_POLAR=1
CEMINI_STOP_WIN_MULT=0
```

Gin remains `CEMINI_GIN_KILL=1`. Max rebuys `0`.

## Implementation order (claude-ds)

1. P1-1 → P1-6 (tests each)
2. P2-1 → P2-5 (tests each)
3. Update this brief + parent postmortem with `## Filed` sections
4. Run:  
   `cd agents/devfun-poker-arena && PYTHONPATH=examples python -m pytest tests/test_qualification_guard.py tests/test_tag_widen.py tests/test_blind_pressure.py tests/test_postflop_decision_log.py tests/test_short_stack.py tests/test_nemesis*.py -q --tb=line`  
   (create/extend tests as needed; all new must pass)

## Do not

- Gin / gin_v2
- Pay rebuys
- Massive chart rewrites unrelated to above
- Break playground chip-qual stagger defaults when `PRIMARY_TRACK=playground`

## Filed (2026-08-09 — claude-ds)

### P1
- P1-1 `CEMINI_NAMED_NEMESIS_TIGHT` — `cemini_decide.py` + `tests/test_nemesis_split.py`
- P1-2 value 3bet — `examples/tournament_3bet.py` + wire + `tests/test_tournament_3bet.py`
- P1-3 short-stack tiers — `short_stack.py` + `tests/test_short_stack_tiers.py`
- P1-4 postflop telemetry — `postflop_telemetry.py`, `scripts/summarize_postflop_log.py`, tests
- P1-5 blind-defend initiative — `tag_widen.py` 3bet JJ+/AK/AQs
- P1-6 `CEMINI_KO_SURVIVAL_HANDS=30` in s12 posture

### P2
- P2-1 polar 3bet — `tournament_3bet.py` + `CEMINI_TOURNAMENT_3BET_POLAR=1` s12
- P2-2 flat-dominate — `flat_dominate.py` + tests
- P2-3 fold-guard ledger — `fold_guard_ledger.py` + instrumented guards
- P2-4 stop-win — `stop_win_governor.py` (default mult 0)
- P2-5 villain_actions — `villain_action_log.py` + tests
- Posture knobs in `run_cemini_lobby.py`; `tests/test_t12_posture.py`
- Verify: **105 passed** (P0+P1+P2 targeted suites)

## Success criteria

- [x] All P1 items coded + tested
- [x] All P2 items coded + tested (stop-win default off)
- [x] s12 posture sets new env knobs
- [x] Briefs updated `## Filed`
- [x] Pytest for touched modules green
- [x] Gin still killed

## Sources

- `@agents/devfun-poker-arena/briefs/2026-08-09_p13-postmortem-t12-number-one-plan.md`
- Multi-model fan-out 2026-08-09 (Fable / GPT-SOL / Kimi / GLM)
