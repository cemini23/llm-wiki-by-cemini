# GenomeDiff backfill — last 3 shipped patches (2026-07-14)

K155 operator checklist: one backfill of Inherited / Mutated / Lost / Novel
for the last three shipped ladder/decide patches.

| Patch | Parent | Delta | Inherited | Mutated | Lost | Novel | Verification |
|-------|--------|-------|-----------|---------|------|-------|--------------|
| **S1 ladder HU guards** (2026-07-05) | 6-max `cemini_decide` preflop + pot-odds postflop | mutate | `CEMINI_SANDBOX_ENGINE=cemini`; pot-committed call guard | HU SB/BTN open rescue; BB defend margins | 6-max EP VPIP brain as HU default | `_hero_set_vulnerable_on_four_straight`; 4-flush / 4-straight OOP folds | `tests/test_cemini_hu_ladder_guards.py`; spots R1/R3/R6 |
| **K150 TEN nemesis** (2026-07-08) | `table_nemesis_pressure` + S1B exploit | mutate | Nemesis seed table; HU gate advisory | TEN → `wide_passive` branch + iso-vs-limp | TEN mislabeled as `linear_aggro` | `ten` seed; `bot_ten_wide_passive`; 72o trash-fold; 8 TEN HU spots | `tests/test_k150_ten_*.py`; HU gate |
| **K151 maniac_shark** (2026-07-09) | K150 nemesis + `linear_aggro` branch | mutate | `CEMINI_NEMESIS_LINEAR_AGGRO`; S1B BB defend / 3-bet vs aggro | Primary pairing → `maniac_shark_lite_2` | TEN-as-primary pairing assumption for ladder | `maniac_shark` profile JSON; 8 shark HU spots; selfplay villain | `tests/test_k151_maniac_shark_*.py`; deploy `bb2a7e5e` |

## Lineage notes

- K150→K151 is a **true mutate**: same nemesis pressure substrate, different
  archetype handle + exploit branch. Not a novel “opponent modeling paper”
  drop-in.
- Jul 05 ladder upgrade **lost** 6-max open frequency as the HU prior — that
  Lost field is the driver, not “imperfect-info RL.”

## Sources

- `briefs/2026-07-05_s1-ladder-upgrade-implementation-plan.md`
- `briefs/2026-07-08_k150-ten-nemesis-update.md`
- `briefs/2026-07-09_k151-maniac-shark-nemesis-update.md`
- arXiv 2607.08758
