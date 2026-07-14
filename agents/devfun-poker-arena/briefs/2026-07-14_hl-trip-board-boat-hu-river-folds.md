---
title: HL patch — trip-board boat + HU river air folds (2026-07-14)
type: brief
target: Poker Arena
created: 2026-07-14
updated: 2026-07-14
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — Researcher ladder S1 HU.

## Summary

Fresh ladder analyze vs **drake**: fold FH (K7 on 9995K), pay underpair/air on trips, call rivers with QTo air on 4-straight and AQo ace-high on paired boards. Plus 6-max BB 99 stack-off tighten (Playground Chaos −840).

## GenomeDiff (K155)

| Field | Value |
|-------|-------|
| Parent mechanism | `_hero_boat_or_quads_on_paired_board` + river showdown fold guards + `_preflop_stackoff_should_fold` |
| Delta | `mutate` |
| Inherited | Existing paired-board underpair folds; HU BB stackoff exempt; OOP 4-straight river fold |
| Mutated | Boat detect now covers board-trips + hole pairs singleton kicker; never-fold boat path before MC showdown; mid-pair stackoff bar 0.18 in 6-max (0.25 HU) |
| Lost | Blind trust that `river_unbeatable` alone protects boats (MC path still folded 91% FH) |
| Novel | `_board_has_trips` / `_hero_vulnerable_on_trip_board`; IP air on 4-straight river; ace-high paired river fold |
| Verification | `tests/test_cemini_hu_ladder_guards.py` (11); spots in `helpers/cemini_tables.py` |

## Body

### Live evidence (ladder `cmr3n8tft01nilecm1u5jlny7`)

| Hand | Leak | Fix |
|------|------|-----|
| K7s on 9995K (−96) | Folded kings full to 88 raise | Boat detect + never-fold |
| 88 on 9995K (−40) | Paid trip board with underpair | Trip-board underpair fold |
| QTo on 78256 (−50) | Called river air on straight | IP 4-straight air fold |
| AQo on 7T7J9 (−50) | Called ace-high on paired river | Ace-high paired river fold |
| Playground 99 BB (−840) | Mid-pair vs large 6-max shove | Stackoff bar 0.18 non-HU |

### Active season before replace

`406f9734` ~1282h · adj bb/100 **+26.6** · μ≈−28.9 — replace only because this is an explicit strategy patch (not methodology).

## Sources

- Ladder analyze 2026-07-14 (drake H2H)
- `references/patch-genome-diff.md`
- `references/genome-diff-backfill-2026-07-14.md`
