# Playground S11 end audit + S12 miss

## Target

Operator + lobby/decide posture for the next playground (S13+). Not a gin re-enable brief.

## Summary

S11 finished **#193 / 322 @ 856 chips** (best **#35**). Same nit that printed P10 **#6 @ 18743** bled once short. Then **Playground S12 ran 3.5 hours and ended while we 409-looped dead S11** — we never registered. No live playground exists now (only Eval S1). Highest-ROI fix is **auto-rollover**, then stop survival-nit + nemesis-tight on chip-qual.

## Regime disclosure

Single-board snapshots: Playground S11 / S12 / S10 and Tournament S10/S11 only. No cross-regime superiority claim.

## Scoreboard

| Board | Window (UTC) | Us | Notes |
|-------|--------------|----|-------|
| P10 | ended 2026-07-30 13:00Z when S11/T10 opened | **#6 / 18743** / 3814 subs | Nit printed on a full multi-day board |
| T10 | Jul 30 13:00 → Aug 4 13:05 | **0 chips / #58** (best #2) | 4 rebuys + gin-while-short; abandoned |
| P11 | Jul 30 13:00 → Aug 4 13:05 | **#193 / 856** (best #35) / 2081 subs / 179 won | Entered ~Aug 1; Aug 3 ~1482/#112 → Aug 4 856/#193 |
| T11 | Aug 4 13:05–16:35 | not entered | Parallel to S12 sprint |
| P12 | **Aug 4 13:05:48–16:35:28 (~3.5h)** | **absent** | #1 `antigravity9s` 2063 / 73 subs; **#20 @ 1102** |

S12 top-20 was “don’t bust + tiny plus.” Leaders printed ~20 hands/hour (1-table pace) for a few hours. Missing the window is an instant zero.

## S11 play leaks (ranked)

1. **Ops: lobby pin + no season watch.** After S11 `Ended`, join spam `competition_not_active`. S12 id `cmseo8d3e4fmh12qragnvqct6` never applied. Enter maps / lobby roles hardcoded through S11.
2. **Survival-nit death spiral.** `CEMINI_KO_SURVIVAL_MIN_STACK=700` on a 1000 buy-in stays ON after any dip under 700. Replay −26 chips/hand Aug 4. Blind tax while folding SB vs raise **86%** (posfix: SB facing_raise 50 fold / 8 call).
3. **Nemesis tight vs half the field.** P11 leaders (`flattened_v2`, lodestar, …) sit on `CEMINI_NEMESIS_HANDLES` + `CEMINI_NEMESIS_TIGHT=1` → premiums-only vs the bots we actually share tables with.
4. **Late entry + no volume edge.** Season ran ~5 days; we show up Aug 1 and grind 2k nit hands. P10 worked because we were on the board early and ran good, not because 8% VPIP is +EV forever.
5. **1-table account cap.** Journal `max_concurrent_tables`. Cannot multi-table the same agent. Sprint meta does not require 10 tables — it requires **being seated when the sprint starts**.
6. **Gin stays dead.** T10 already proved gin-on-while-short zeros the stack. Do not “fix VPIP” with gin.

Posfix preflop sample (182 rows, `tag-sb-v3.posfix`): fold 66% of decision points; BTN unopened vol 86%; SB facing_raise vol 14%; BB facing_raise vol 31%. TAG SB defend did fire on stable labels (44/KJo/K9s/AKo). The bot is a **tight TAG**, not broken-fold-everything — it still loses when short + survival + nemesis tight stack.

## What shipped after this audit

- In-lobby **Playground watcher** (`examples/playground_comp_watch.py`) — poll list-active/all, retarget `.env` + process env when a live playground appears.
- Chip-qual posture is **season-agnostic** (`sN_playground` / `CEMINI_PRIMARY_TRACK=playground`), not S11-only.
- Playground: `CEMINI_KO_SURVIVAL_MIN_STACK=400`, `CEMINI_NEMESIS_TIGHT=0`, gin still killed, TAG widen still on.
- S12 id recorded in enter/apply maps (ended — historical only).

## Explicit NO

- Do not re-enable gin
- Do not pay T10/T11 250 MON rebeys
- Do not pretend we can enter ended S12 for a climb
- Do not claim halloran-class VPIP until volume + chip/hand go positive on a live board

## Sources

- Arena `GET /competition/list-all` + `list-active` + leaderboards (2026-08-05)
- `reports/hl-loop/playground_timeseries.jsonl`
- `reports/exports/playground-s11-live/preflop_decisions.jsonl`
- journal `cemini-devfun-poker-lobby.service`
- `briefs/2026-08-01_tournament-s10-postmortem.md`
