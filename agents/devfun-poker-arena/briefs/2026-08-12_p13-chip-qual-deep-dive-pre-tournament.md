---
title: Playground S13 chip-qual deep dive — keep / improve before free tournament
type: brief
tags: [brief, poker, playground-s13, chip-qual, pre-tournament-gate]
created: 2026-08-12
updated: 2026-08-12
---

## Target

`agents/devfun-poker-arena/` — operator + lobby · **address before next free tournament entry**

## Summary

Playground S13 climbed from ~#30 (−1339 vs #20) after the Aug 10 stack-repair deploy to **#10 (~9580 chips, +1932 over cut)** with qualification protect ON (`strong_top20`). What worked: chip-qual TAG + gin kill + no mid-grind thrash + protect-at-cut (`QUAL_BUFFER=0`). What to fix before free tournament: sticky bubble protect, mild SB steal widen, equity-logger audit for flop peels, confirm tournament freeze posture on entry. Do not port the T12 climb pack onto playground. Canvas: `p13-chip-qual-deep-dive`.

## Regime disclosure

**Single-regime** Arena Playground S13 / upcoming free Tournament chip-score only. Metrics are not cash EV. Per-regime: playground TAG widen stays for chip-qual; tournament must keep freeze from `2026-08-10_tournament-stack-repair.md` (same briefs folder).

## Snapshot (2026-08-12 ~12:15 UTC)

| Metric | Value |
|---|---|
| Rank / chips | #10 / ~9580 |
| vs #20 cut | +1932 (`strong_top20`) |
| Preflop / postflop logged | ~2220 / ~403 |
| Hands acted (process) | ~2115 |
| Protect on/off transitions (72h) | 8 |
| First post-repair lock | Aug 11 21:14 · #17 · +75 |

## What we are doing well

1. **Regime separation** — playground chip-qual (TAG widen, 6max, rebuy≤2) without tournament polar/flat/auto-HU bleed-through.
2. **Gin stayed killed** — stacks 1000 → ~9600; no T10-style zero spiral in the decision log.
3. **TAG opens where it pays** — unopened raise CO ~79%, BTN ~76%, MP ~45%; raise classes JJ/AA/KK/TT/AK/QQ-heavy.
4. **Protect-at-cut** — `QUAL_BUFFER=0` armed at top-20 even at +75; now fat cushion (~1.3k playable above lock floor).
5. **Process discipline** — same lobby process since repair deploy; volume pace; no mid-event agent thrash.
6. **Value betting** — bet/raise logged equity ~0.81–0.84; undercalls (eq ≪ pot odds) = 0 in sample.

## What to improve (pre-tournament checklist)

### P1 — before free tournament entry

- [ ] **Sticky bubble protect** — 4× overnight dropouts #20→#21 at buf≈0. Stay protect until −N under cut (or tiny positive sticky buffer once in).
- [ ] **Mild SB steal widen** — unopened SB raise only **15.6%** / fold 84.4%; fold_guards `sb_chart_trash` ×92. Steal band only — not gin.
- [ ] **Confirm tournament freeze on entry** — `TABLE_FORMAT=6max`, `TAG_WIDEN=0`, polar/flat/chase/blind-defend off, gin kill, `MAX_REBUYS=0`. See stack-repair brief. Do not re-arm climb pack.

### P2 — offline / if climb stalls

- [ ] **Flop overfold audit** — 45 folds with logged eq > pot_odds+5pp (mostly flop; KQo/AQo/small pairs). Validate equity helper first (some samples look model-suspicious) before widening peels.
- [ ] **Optional blind value 3bet** — SB/BB facing-raise 3bet ~3% vs IP ~20–29%. Value-only QQ+/AK if outside top 15 again — not polar.

### P3 — telemetry hygiene

- [ ] Villain log is raise-only; preflop raise `reason` often null — enrich when next touching decide logging.

## Do not

- Re-enable gin on playground or tournament
- Port T12 climb pack (polar / flat / auto-HU / permanent chase) onto chip-qual
- Mid-cushion protect/pace thrash while `strong_top20`
- Pay MON for a tournament seat this cycle if free entry is available

## Pre-tournament gate (operator)

**Before joining the next free tournament from this P13 ticket, re-read this brief + `2026-08-10_tournament-stack-repair.md` and clear the P1 checklist.** Prefer shipping sticky protect + SB steal on playground first if time allows; tournament entry itself must at minimum apply the freeze posture.

## Success criteria

- [x] Deep dive filed as brief + canvas referenced
- [x] ROADMAP / hot.md remind before tournament entry
- [ ] P1 sticky protect + SB steal addressed (or explicitly deferred with operator note)
- [ ] Freeze posture verified on tournament lobby start
- [ ] No climb-pack re-arm without a new audit

## Sources

- Prod journal `cemini-devfun-poker-lobby` (72h protect path)
- `reports/exports/playground-s13-live/` preflop/postflop/fold_guards
- Canvas `p13-chip-qual-deep-dive`
- `briefs/2026-08-10_tournament-stack-repair.md`
- `briefs/2026-08-09_p13-postmortem-t12-number-one-plan.md`
