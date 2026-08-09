---
title: P13 postmortem → Tournament S12 #1 plan (multi-model)
type: brief
tags: [brief, poker, playground-s13, tournament-s12, postmortem]
created: 2026-08-09
---

## Target

dev.fun Poker Arena — live Tournament S12 (`cmslrboge8c2zmpfmv5adq4pd`) + future playgrounds

## Summary

Playground S13: **#20 / ~162 @ 4086 chips**, WR **8.6%**, cps **1.10**, volume fine (3717). Leaders print WR **18–25%** and cps **3–5**. Multi-model fan-out (Fable / GPT-SOL / Kimi / GLM) + log falsification → ship a T12 climb pack **without** re-enabling gin.

## Evidence (P13)

| Metric | Us | #1 flattened_v2_guard_04 | #2 marlowe |
|---|---|---|---|
| Chips | 4086 | 16282 | 14018 |
| WR | 8.6% | 19.8% | 24.8% |
| cps | 1.10 | 5.03 | 3.82 |
| Subs | 3717 | 3237 | 3665 |

Preflop export `playground-s13-live` n=1474: vol 33.7%; CO/BTN open wide (70–79%); **BB defend vs raise 27.8%** (fold 72%); **SB defend 23.3%** (fold 77%); facing-raise 3bet only **6.3%**. Steal-fold after our CO/BTN opens mostly falsified (11% fold when matched) — leak is **blind defense + low 3bet + likely postflop**, not open-and-dump.

Ops: protect-off near bubble earlier; `QUAL_BUFFER=0` later; missed entire P12 historically (watcher now fixed). T12 entered 0.01 MON; lobby on tournament; gin kill ON; max rebuy 0.

## Multi-model consensus

| Source | Unique angle | Keep |
|---|---|---|
| **Fable** | Passive call-heavy entries + fold-guard accretion; SB dead money; initiative/3bet tier | Gin dead, rebuy 0 |
| **GPT-SOL** | Concrete levers: `TAG_BLIND_DEFEND`, placement cushion %, SB forced opens, short-stack 12bb, named-nemesis split | Testable patches |
| **Kimi** | Steal-fold hyp (partly falsified); survival-nit EV; stop-win sessions; flat-dominate vs leaders | Experiments first |
| **GLM** | Telemetry-before-patch; control arm; closed-loop 6h cadence | Measure then ship |

## Root causes (ranked)

1. **Blind defense too tight** — BB/SB fold ~72–77% facing raise → free chips to field every orbit.
2. **Premature tournament `placement_protect`** — code arms at `rank≤prize_cut AND buffer>0` → at T12 #2@1000 we may already be in protect/nit mode.
3. **WR collapse vs leaders** — we enter pots but convert poorly (8.6% vs ~20%); postflop/telemetry gap.
4. **SB first-in too nitty** — unopened SB folds QJo-class; steal equity left on table.
5. **Named nemesis tight** — may over-fold vs handles that print by taking our blinds.
6. **Short-stack 20bb jam band** — no-rebuy T12: too wide all-ins / wrong threshold.
7. **Protect/ops on P13** — unlocked at thin buffer then over-locked; rank bled while chips rose slower than #20 line.

## P0 ship (T12 #1) — implement now

1. **Delay placement_protect** — require `buffer/cutoff >= CEMINI_PLACEMENT_PROTECT_BUFFER_PCT` (default **0.35**); else `placement_chase` when outside money or thin cushion. File: `qualification_guard.py` + tests.
2. **Tournament blind defend lane** — `CEMINI_TAG_BLIND_DEFEND=1` independent of full TAG widen; BB/SB defend vs ≤3bb opens; call ≤10% stack. Files: `tag_widen.py`, `cemini_decide.py`, `_apply_competition_posture` for s12_tournament.
3. **SB chase opens** — under `placement_chase`, force-open SB subset (QJo, KTo+, A9o+, pairs, suited broadway) before equity gate. File: `blind_pressure.py` / `cemini_decide.py`.
4. **T12 posture env** — `CEMINI_NEMESIS_TIGHT=0`, `CEMINI_SHORT_STACK_BB=12`, `CEMINI_KO_SURVIVAL_MIN_STACK=250`, keep `CEMINI_GIN_KILL=1`, `CEMINI_MAX_REBUYS=0`, `CEMINI_PLACEMENT_CHASE=1`.
5. **Postflop decision log** — jsonl street/bet/action/pot (fail-open) so next loop can see fold-to-cbet. File: lobby/decide export path under `s12-tournament-live/`.
6. **Tests** for 1–3; pytest green.

## Prod `.env` posture knobs (P0-4 — LIVE OK after code ship + lobby restart)

Upsert on cemini-prod for Tournament S12 lobby process only (no gin / rebuy flips):

```
CEMINI_NEMESIS_TIGHT=0
CEMINI_SHORT_STACK_BB=12
CEMINI_KO_SURVIVAL_MIN_STACK=250
CEMINI_TAG_BLIND_DEFEND=1
CEMINI_PLACEMENT_PROTECT_BUFFER_PCT=0.35
CEMINI_GIN_KILL=1
CEMINI_MAX_REBUYS=0
CEMINI_PLACEMENT_CHASE=1
```

Code path: `run_cemini_lobby._apply_competition_posture` for `_s12_tournament` already sets these on process start. Prefer restart lobby after deploy so process env applies; optional explicit `.env` upsert for survival across non-posture restarts.

Also ensure `CEMINI_EXPORT_DIR` points at the live export folder so `postflop_decisions.jsonl` lands next to preflop logs.

## Do not

- Re-enable gin / gin_v2 without a gated evidence brief + dry-run.
- Pay large MON rebuys.
- Disable stagger on playground qual (separate track).
- Thrash charts mid-orbit without telemetry.

## Success criteria (T12)

- Not in `placement_protect` at start (#2 / ~1000 / thin field).
- BB defend vs raise → **≥38%** over next 200 logged hands.
- Survive with stack ≥ start after 100 hands OR finish top-3 if field tiny.
- cps trending up vs first 50 hands baseline.
- Gin remains killed.

## Sources

- Prod leaderboards P13/T12 2026-08-09
- `reports/exports/playground-s13-live/preflop_decisions.jsonl`
- Fan-out: [Fable](ef4d211e-de11-4610-9a80-25ec43592ede) · [GPT-SOL](a7fc420e-8b5b-43a4-85d1-6f6b357b3c2c) · [Kimi](5bc65f62-a343-40f7-b588-e28bb01e8038) · [GLM](3c7c88ae-9a00-440d-9df0-04ee4aa843e4)
