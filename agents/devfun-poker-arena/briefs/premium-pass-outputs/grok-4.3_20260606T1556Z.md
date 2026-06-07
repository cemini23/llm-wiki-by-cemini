**## 1. Top 5 structural gaps**

1. **SB/BB trash completion** — Automatic folds on non-premiums in blinds when no prior action; current sample shows -100 avg delta on 36 hands.
2. **UTG/MP open range leakage** — Any hand below 22+/AJ+ opens from UTG/MP must be blocked; 32 hands at -100 avg.
3. **Cold 3-bet defense** — No auto-defense vs LAG 3-bets without HUD archetype confirmation; prevents hunterguy102-style extraction.
4. **BTN vs limp-fold expansion** — Already shipped, but extend guard to CO when stack <25bb to avoid marginal steals.
5. **Postflop continuation without nuts flag** — CEMINI_NUTS_DETECT=1 must also gate all non-nut draws on paired boards.

**## 2. Cold-start policy (hands 1–N)**

- Hands 1-50: Strict 8% VPIP cap. Only open 22+, AJ+ from any position. No 3-bets, no blind defends.
- Hands 51-200: HUD empty → treat all opponents as LAG. Reduce open range 15% further. No steals from BTN/CO until 3+ hands observed per villain.
- Flip trigger: After 200 hands or when any seat shows <15% VPIP, enable normal tight-passive chart. Survival priority overrides all EV.

**## 3. S1b exploit toggles (HUD warm)**

Enable only when archetype confirmed and stack >30bb:
- vs LAG (VPIP>35%): Tighten 3-bet range to value only; increase fold vs 3-bet to 85%.
- vs Grok cluster: Force stagger lock + CEMINI_NUTS_DETECT=1 on all streets.
- vs hunterguy102: Permanent rock mode — no calls wider than top 5% range.
All toggles frozen below 25bb. No widening of base ranges.

**## 4. KO foundation (no rebuy)**

- Minimum stack policy: Sit out if <18bb at table start. Rejoin only after 3+ orbits or when average stack >35bb.
- Max playable fraction: Never risk >12% of stack preflop without nuts flag.
- Hour-one rule: All decisions default to "preserve 50bb+" until 60 minutes elapsed. No marginal +EV spots.

**## 5. Do NOT change**

- Base VPIP/PFR targets (12.3%/4.3%).
- BTN trash vs limp-fold guard.
- CEMINI_NUTS_DETECT=1 logic.
- Stagger locks on multiway pots.
- HL R8-20 patches.

**## 6. Patch backlog (ranked)**

| priority | guard name              | target function area     | regression spot idea                  |
|----------|-------------------------|--------------------------|---------------------------------------|
| 1        | blind_fold_guard        | preflop decide()         | SB 72o vs UTG limp, BB 83o vs CO open |
| 2        | utg_open_block          | range chart              | UTG K9s, MP QTs at 30bb               |
| 3        | lag_3bet_defense        | archetype switch         | vs 0xJeff_ai 3-bet with AQo           |
| 4        | stack_sitout            | table join logic         | <18bb table entry                     |
| 5        | grok_cluster_lock       | HUD archetype            | 3-bet vs grok_trips_prime             |

**## 7. Regression / test ideas**

1. UTG 20bb, KTs — must fold preflop.
2. SB 15bb, A9o vs BTN open — must fold.
3. BB 22bb, 65s vs CO limp — must check-fold.
4. BTN 28bb, Q9o vs two LAG limpers — must fold (even post cold-start).
5. MP 35bb, AJs vs hunterguy102 3-bet — must fold.
6. CO 40bb, 22 vs Grok LAG open — must fold without nuts flag.
7. SB 50bb, AQo vs unknown 3-bet in first 80 hands — must fold.
8. Any position <25bb, non-premium vs 4-bet — must fold.