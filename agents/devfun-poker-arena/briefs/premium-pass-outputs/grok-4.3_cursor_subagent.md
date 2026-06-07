# Playground S1a Retrospective — cemini_decide.py (Grok-4.3 Cursor Subagent Pass)

**Date:** 2026-06-06  
**Source data:** playground-s1-s1a-snapshot-2026-06-06 export + HL analyze (worst 15)  
**Prior passes:** grok-4.3_20260606T1556Z.md, deepseek-reasoner_20260606T1556Z.md  
**Adjudication base:** 2026-06-06_s1a-premium-retrospective-synthesis.md  
**Hero state:** #1 @ 138,917 chips (12.3% VPIP / 4.3% PFR / 5.1% 3b), 9% WR, 1873 hands. Recovered from rank ~215 @ 540. Shipped: BTN limp-trash fold (R20), CEMINI_NUTS_DETECT=1, stagger locks. KO = no rebuy.

Zero runtime LLM. Structural guards, env policies, regression spots only. Survival > vanity metrics.

## 1. Top 5 structural gaps (ranked, guard categories not hand heroics)

1. **SB/BB trash completion guard** — Automatic fold on non-premiums in blinds vs any open when HUD cold or vs LAG archetype. -100 avg delta on 36 blind hands in sample. Primary leak source.

2. **EP (UTG/MP) open leakage block** — Sub-premium opens (below 22+/AJs+/AQo) from UTG/MP must be hard-blocked regardless of position stack depth. 32 hands at -100 avg; highest risk position.

3. **Cold-start steal/3-bet defense** — No auto 3-bet or steal from CO/BTN until ≥10 hands observed per villain AND HUD archetype confirmed. Prevents early extraction by Grok cluster (65%+ VPIP) and hunterguy102.

4. **Short-stack join/sit gate (KO-specific)** — No table entry when hero stack < 2× buy-in (2000) or <18bb effective at table start. Extend retry timer to 3600s. One bust ends qualification.

5. **Nemesis HUD seeding + rock mode** — Seed permanent extra-tight policy vs hunterguy102 (18 pots / 87 tables) and Thaddius from export tablemates list. No calls wider than top-5% range vs these IDs.

## 2. Cold-start policy (hands 1-50, 51-200, flip trigger)

**Hands 1-50 (pre-HUD, survival lock):**
- VPIP cap ≤10%. Opens: UTG=TT+/AQs+/AKo only; MP=99+/AJs+/AQo+; CO/BTN=77+/ATs+/AQo+ (no isolation raises).
- No 3-bets except AA/KK vs raise. No blind defends vs any raise. No BTN/CO steals.
- BB: fold to 3×+ opens except TT+/AK. SB: complete only 22-66/Axs/54s+.
- Sit-out one orbit if stack <80bb after any pot. Join retry = 1800s if ranked.

**Hands 51-200 (partial HUD):**
- Ramp to chart-only VPIP 12%. Limited BB defend: chart pairs + Axs vs single raise from confirmed LAG only.
- No CO/BTN steals until ≥10 hands/villain. 3-bet only value (JJ+/AQ+) vs confirmed VPIP>45%.
- Normal join pace unless stack <2000 chips.

**Flip trigger (to controlled exploit / S1b):**
- ≥200 hands total AND ≥20 hands observed on ≥2 villains at current table AND stack ≥60bb AND current rank ≤20 with ≥10k chip buffer AND `qualification_protect` flag false.
- Once flipped, table-scoped toggles only (see §3). Revert to cold-start rules on any new table with <10 hands/villain.

## 3. S1b exploit toggles (HUD warm, table-scoped only)

Enable **only** when all conditions met: HUD archetype=maniac (VPIP>45% AND 3b%>30%) AND hands_observed≥20 on that villain AND hero stack>60bb AND not `qualification_protect` AND table has ≤2 other LAGs.

Toggles (value-only, stack-risk limited):
- `DEFEND_BB_VS_STEAL`: vs LAG steal, defend BB with top-40% (pairs, Ax, KTs+, suited connectors 54s+). Fold bottom 30%. Max call 30% stack.
- `THREE_BET_LAG_CO_BTN`: vs LAG open CO/BTN, 3-bet to 2.5× with TT+/AQ+/76s+ (semi only if nuts flag). Fold to 4-bet without AA/KK. Max 3-bet size 20% stack.
- `TRAP_AA_KK_VS_MANIAC`: vs maniac 3-bet (not 4-bet), call with AA/KK (check-raise flop). Only when >80bb effective.
- All other postflop (float, MDF, check-raise TPTK) deferred — high variance, needs replay proof.

Nemesis overrides (permanent, even post-flip):
- hunterguy102: rock mode — defend only top-40%, never 3-bet without AA/KK.
- Thaddius / 0xJeff_ai: fold more to flop barrels; increase 3-bet size to 3× vs 0xJeff.

All toggles frozen below 25bb or during hour-1 KO.

## 4. KO foundation (no rebuy)

Primary objective: never bust. All decisions subordinate to preserving 50bb+ through hour 1.

- **Minimum viable stack / sit-out:** Sit out immediately if stack <18bb at table start or <2× buy-in (2000) on join. Rejoin only after 3+ orbits or when table avg stack >35bb. Extend `CEMINI_FIRST_JOIN_RETRY_S` to 3600s when <buy-in.
- **Max playable fraction:** Never risk >12-15% of stack preflop without nuts flag (AA/KK/QQ only). Postflop: never call >50% stack unless nutted or CEMINI_NUTS_DETECT=1.
- **Table selection:** Avoid tables with 3+ HUD maniacs (VPIP>45%) when hero <40bb. Implement as join heuristic when roster exposed.
- **Hour-1 rule:** Regardless of chip lead or rank, all decisions default to cold-start row (§2) for first 60 minutes. No marginal +EV spots.
- **All-in survival:** Call all-in only with AA/KK (QQ borderline at >60bb). Fold any all-in that would drop below 40bb.
- **Blind stealing:** Never raise-fold from SB/BB. BTN/CO steals only when >60bb AND fold equity >70% (HUD confirmed).

## 5. Do NOT change (3-5 items)

1. Base VPIP/PFR targets (12.3%/4.3%) and tight-passive foundation — #1 rank proves chips > win rate. Any widening increases variance and KO bust risk.
2. Shipped patches: BTN limp-trash fold (R20), CEMINI_NUTS_DETECT=1 (gate all non-nut draws on paired boards), stagger locks on multiway, HL R8-20 patches.
3. Passive postflop style — no new bluff raises, delayed c-bets, or postflop aggression. Protects stack; recovery came from tightening, not heroics.
4. Cold-start strictness and no-rebuy mindset — even with fat stack, hour-1 = survival mode. Do not treat playground rebuy history as safety net.
5. Fold to 4-bet without AA/KK (even QQ too light). LAGs 4-bet wide; stack preservation paramount for qualification.

## 6. Patch backlog table (priority | guard | target | regression spot)

| priority | guard name                  | target function area          | regression spot idea                          |
|----------|-----------------------------|-------------------------------|-----------------------------------------------|
| P0       | cold_start_no_steal         | preflop decide()              | CO Q5o vs multiway limp (first 30 hands)      |
| P0       | blind_trash_fold            | preflop decide()              | SB 72o / 83o / A4o vs UTG limp or CO open     |
| P0       | ep_open_block               | range chart                   | UTG K9s / MP QTs at 30bb (any HUD state)      |
| P1       | join_gate_short_stack       | table_join / lobby            | Stack=1800 or <18bb effective → sitout 3600s  |
| P1       | nemesis_hud_rock            | archetype switch + HUD seed   | hunterguy102 open → fold A5s SB; Thaddius barrel → fold TPTK |
| P2       | maniac_3bet_value_only      | preflop 3bet (S1b only)       | vs grok_trips_prime 3b% >40% → 3bet JJ+ only  |
| P2       | trap_aa_kk_vs_maniac        | preflop response (S1b only)   | BB maniac 3b → call AA (not raise)            |
| P3       | stagger_lock_interaction    | preflop commit + nuts_detect  | Verify 15% stack cap still respected with new guards |

## 7. Regression test ideas (5-8 spots)

1. UTG 20bb, KTs vs unknown (first 10 hands) — must fold preflop.
2. SB 15bb, A9o vs BTN open (any HUD) — must fold.
3. BB 22bb, 65s vs CO limp from LAG (hands_observed<10) — must check-fold.
4. BTN 28bb, Q9o vs two LAG limpers (cold-start or qualification_protect) — must fold.
5. MP 35bb, AJs vs hunterguy102 3-bet — must fold (rock mode).
6. CO 40bb, 22 vs Grok LAG open (VPIP>60%, <20 hands observed) — must fold without nuts flag.
7. SB 50bb, AQo vs unknown 3-bet in first 80 hands — must fold.
8. Any position <25bb, non-premium vs 4-bet or all-in — must fold. Stack <18bb at table start → immediate sit-out.

## 8. Agreement with prior passes — bullet what you confirm from Grok+DeepSeek API runs

- Cold-start conservatism (≤8-10% VPIP hands 1-50, no blind defends, no early steals) is the correct recovery path from near-bust.
- EP/UTG trash open block and SB/BB trash complete guard are the highest-frequency, highest-risk leaks.
- Base VPIP/PFR (12.3%/4.3%) must remain locked — do not widen for vanity.
- Nemesis-specific rock mode vs hunterguy102 is required; seed from export tablemates.
- KO no-rebuy demands strict sit-out / join gates and max 12-15% stack commit preflop.
- CEMINI_NUTS_DETECT=1 + stagger locks are correct and should gate any new logic.
- BTN limp-trash fold (already shipped) should be mirrored to CO when short.
- Hour-1 = cold-start rules regardless of chip lead.

## 9. New insights — anything prior passes missed

- Explicit `qualification_protect` flag (or rank/buffer check) to gate **all** S1b toggles, not just cold-start — prevents accidental widening during KO hour-one even if HUD warm.
- Nemesis HUD seeding should be done at startup from the export tablemates list (hunterguy102 18 pots/87 tables is the clearest signal) rather than waiting for live observation.
- Stagger lock must be re-verified against new preflop guards (cold_start_no_steal, blind_trash_fold) to ensure 15% stack cap is never violated by combined logic.
- Join retry extension to 3600s when stack < buy-in prevents forced 409 loops that would otherwise leak blinds during recovery.
- Table-roster heuristic (avoid 3+ maniacs when <40bb) is implementable once API exposes seating; worth adding to run_cemini_lobby.py even if not in current decide().

## 10. Reject from prior passes — what you'd explicitly NOT implement and why

- DeepSeek's BB defend widening (K7o vs steal, 65s defend, etc.) and 3-bet 99 / float QT / check-raise TPTK vs LAG — **rejected for S1a + KO hour-one**. Recovery to #1 came from tightening, not defending wider. These increase variance and bust risk in a no-rebuy format. S1b conditional GO only after HUD warm + stack buffer + qualification_protect=false.
- Any postflop MDF or aggressive float policy on dry boards — deferred. High variance; needs full replay proof and would require new regression spots. Passive postflop is a strength.
- Global 3-bet range expansion or trap-calling AA/KK outside maniac tables — too wide for current field (Grok cluster 4-bets wide). Value-only, table-scoped, stack-gated only.
- Relaxing cold-start or hour-1 rules based on chip lead — explicitly rejected. KO has no rebuy; survival mindset must be absolute for first 60 minutes.

**Status:** Ready for HL round implementation. All patches table-scoped, regression-tested, and gated by qualification_protect where appropriate. No runtime LLM.