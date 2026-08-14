---
title: Tournament S13 freeze entry — T12 autopsy + P1 checklist
type: brief
tags: [brief, poker, tournament-s13, freeze, pretournament]
created: 2026-08-14
updated: 2026-08-14
---

## Target

`agents/devfun-poker-arena/` — enter **Tournament S13** (`cmsrgknhz32e1117r3l2h3q7b`) from Playground S13 #13 ticket. Freeze only. No MON.

## Summary

Tournament S13 is **Active** (opened with Playground S14 at ~13:01 UTC). Last KO **T12 ended 0 chips** (94 hands, best rank 2, then bust). Dual audit + 6-max recap agree on one ship: **never go broke**, force 6max, no TAG_WIDEN leftover, no gin, no climb pack. P1 sticky protect + mild SB steal ship for playground; tournament posture is freeze.

## T12 autopsy (last tournament)

| Metric | Value |
|---|---|
| Comp | `cmslrboge8c2zmpfmv5adq4pd` Ended |
| Finish | **0 chips**, rank 32, bestRank **2** |
| Hands | 94 submissions / 14 wins |
| Logged preflop | 47 (fold 21 / raise 12 / call 14) |
| Entry | 0.01 MON (T12) |
| Export | `reports/exports/s12-tournament-live/` (thin — died fast) |

Root causes (already in `2026-08-10_tournament-stack-repair.md`): TAG_WIDEN leftover, `TABLE_FORMAT=auto` HU BB 3bet, polar/flat/chase. Freeze was playground-only until this slice — `_apply_competition_posture` only matched **s12_tournament**, so **S13 would have inherited playground TAG_WIDEN** if we swapped lobby without this patch.

Devfun 6-max recap (2026-08-14): AlphaHorizon won with 0 rebuys, 14% 3bet, 2:1 fold equity. That is **unlimited-rebuy 5/10 6-max**, not our KO. Do **not** copy 36% VPIP onto T13. Steal: survive + buy folds later, after freeze soaks.

## P1 checklist

- [x] Sticky bubble protect (`CEMINI_QUAL_STICKY_UNDER_CHIPS=250`, rank slack 1)
- [x] Mild SB steal QJo/KJo/ATo/KTo under TAG_WIDEN only (off in freeze)
- [x] Tournament freeze on **any** `sN_tournament` (not just s12)
- [x] `CEMINI_REFUSE_ENTRY_FEE=1` — no 402 MON pay; wait for sponsored ticket
- [x] `CEMINI_MAX_REBUYS=0`, gin kill, 6max, TAG_WIDEN=0, chase/polar/3bet off

## Do not

- Re-enable gin / T12 climb pack
- Pay MON if 402 (free ticket from P13 #13 / 13559 chips)
- Mid-event agent_version thrash
- Port AlphaHorizon LAG into KO

## Apply

```
CONFIRM=1 SEASON=13 OLD_PLAYGROUND_COMP=cmsrglcro33ttvijti3slinjh \
  ./scripts/tournament_freeze_prod_apply.sh cmsrgknhz32e1117r3l2h3q7b
```

## Sources

- Prod `/competition?competitionId=` T12/T13 2026-08-14
- Agent me: P13 #13 / 13559; T12 0/94
- `briefs/2026-08-10_tournament-stack-repair.md`
- `briefs/2026-08-12_p13-chip-qual-deep-dive-pre-tournament.md`
- https://x.com/devfun/status/2088249401949249743
