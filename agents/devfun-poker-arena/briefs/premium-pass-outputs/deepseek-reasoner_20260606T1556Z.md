## 1. Top 5 Structural Gaps

Ranked by chip‑risk × frequency (based on HL analyze and field profile).

| Rank | Gap | Mechanism | Risk Source | Fix Area |
|------|-----|-----------|-------------|----------|
| 1 | **SB/BB blind defence vs LAG steals** | Fold too often to BTN/CO opens from high‑VPIP seats. 80% of worst-15 hands are BTN/SB/BB – many are folds pre‑flop. LAGs win small pots repeatedly. | hunterguy102 (18 pots), Grok cluster (65%+ VPIP) | Defend BB with A‑high, suited connectors, pairs. Fold only bottom 30% vs persistent stealers. |
| 2 | **Cold‑start early‑position folding** | First 50 hands: folds to any raise from UTG/MP with marginal hands (e.g., A6s, KJo). Weakens stack vs LAGs who open wide. | Pre‑HUD period – opponents accumulate chips before reads exist. | Pre‑populated “default LAG” rules: open UTG/MP only top 12%, but call a single raise with top 30% from MP vs BTN steal. |
| 3 | **Zero 3‑bet vs high‑VPIP CO/BTN** | PFR=4.3% (almost only AA/KK). LAGs open 40%+ from CO/BTN – we never punish. They profit on fold equity and post‑flop bluffs. | Grok cluster (3b=45–55%) will 4‑bet shove often → we must avoid being trapped. | 3‑bet vs CO/BTN with JJ+, AQ+ when HUD shows VPIP > 45%. Fold to 4‑bet without AA/KK. Lock stack limit: never 3‑bet > 80% of starting stack. |
| 4 | **Post‑flop continuation fold vs aggressive lines** | In worst-15 hands, many show folds on flop/turn after calling pre (e.g., 9cQs BTN board 6s8h2c). LAGs float often and barrel. | LAGs like 0xJeff_ai (VPIP=40%, PFR=26%) have high cbet frequency. | Add “don’t fold to single cbet on dry boards when we have a pair or draw” – implement a minimum defence frequency (MDF) of 40% on flop. |
| 5 | **No trap‑calling vs wild 3‑bettors** | Grok cluster 3b rate 45–55% – they 3‑bet wide. We fold too often (5.1% 3b), losing value. Our strong hands (QQ+, AK) only raise, never call to trap. | Grok_trips_prime (VPIP=70%, 3b=55%) will 5‑bet shove when we 4‑bet → we fold. Trapping 3‑bet with KK/AA yields huge payoff. | When BB, 3‑bet frequency>30% on HUD, slow‑play AA/KK by calling the 3‑bet ≥ 75% of the time. Standard: raise all other strong hands. |

## 2. Cold‑Start Policy (Hands 1–N)

**Objective**: survive first 50 hands without leaking chips to LAGs. Use conservative rules that assume all opponents are aggressive until HUD confirms otherwise.

### First 50 hands (pre‑HUD)
- **VPIP target**: ≤ 10% (only top 10%: 77+, ATs+, AJo+, KQs)
- **PFR target**: ≤ 3% (only AA/KK/QQ, AK)
- **Position‑based folding**:
  - UTG: fold everything except TT+, AQs+, AKo
  - MP: fold everything except 99+, AJs+, AQo+
  - CO: same as MP; do **not** isolate limpers (no raise without premium)
  - BTN: call cheap completes only with pairs 22–77, suited connectors 65s+; raise only with JJ+, AQ+
  - SB: complete only with pairs 22–66, Axs, suited connectors 54s+; fold all else
  - BB: defend vs minraise with same SB list + all Ax, KTs+, QJs; fold to 3×+ raises except with TT+/AK
- **No 3‑betting** at all (except AA/KK vs a raise)
- **No post‑flop bluff raising** – only bet for value when top pair good kicker or better
- **Sit out** one orbit if stack falls below 80 BB (join next table after 1 blind cycle)

### Hands 50–200 (partial HUD)
- HUD warm: populate opponent stats. Use a **dedicated HUD update every 10 hands**.
- If any opponent shows VPIP > 40% (LAG flag), enable exploit toggles (see §3).
- Ramp VPIP slowly to 12% (current avg) by adding: low suited connectors from CO/BTN, medium pairs from MP.
- Continue to fold ATo, KJo from early positions.

### After 200 hands
- Full HUD active. Use archetype‑specific rules (see §3).
- Flip from survival to **controlled exploitation**: target LAGs with 3‑bets and trap‑calls, but never risk more than 15% of stack unless holding AA/KK.

## 3. S1b Exploit Toggles (HUD Warm)

Enable **only** when seated at table with a **LAG** (VPIP > 40%, PFR > 25%) or **Grok cluster** (name contains “grok_” or “Grok”). Toggles are locked for non‑LAG tables.

| Toggle | Condition | Action | Edge | Stack Risk Limit |
|--------|-----------|--------|------|------------------|
| **DEFEND_BB_VS_STEAL** | BTN/CO open from LAG with VPIP>45% | Call with all pairs, Ax, Kx, suited connectors (54s+), fold bottom 30% | Stop LAGs from stealing 1.5BB per orbit | Never call with > 30% of stack |
| **THREE_BET_LAG** | LAG opens from CO/BTN (VPIP>45%, PFR>30%) | 3‑bet to 2.5× open with TT+, AQ+, 76s+ (semi‑bluff) | Punish wide range; LAGs fold > 60% to 3‑bet | Max 3‑bet size = 20% of stack; fold to 4‑bet without AA/KK |
| **TRAP_CALL_LAG** | LAG 3‑bets from blinds (3b%>30) | Call with AA/KK only (check‑raise flop) | Induce shove on flop; LAGs barrel wide | Must have > 80 BB to trap |
| **FLOAT_FLOP** | LAG c-bets flop (cbet%>70) and board is dry (no draws) | Call with any pair, any gutshot, backdoor flush; fold only bottom air | LAGs give up on turn 40%+; win pot with small investment | Max call = 25% of pot |
| **CHECK_RAISE_FLOP** | LAG c-bets flop with high continuation (cbet%>75) and we have top pair+ | Check‑raise 3× their bet | LAGs fold to raise > 50% on connected boards | Only when hand strength > top pair |

**Nemesis specific** (hunterguy102, Thaddius, 0xJeff_ai):  
- Against hunterguy102 (18 pots won vs us), **reduce steal defence**: defend BB only with top 40% of hands (not 70%), because he steals with value range. Also **never 3‑bet** him without AA/KK – his 4‑bet range is narrow.  
- Against Thaddius (10 pots won), **fold more to flop bets** – he has high turn aggression.  
- Against 0xJeff_ai (VPIP=40%, PFR=26%), **use normal LAG toggles but increase 3‑bet size** to 3× because he calls 3‑bets often.

## 4. KO Foundation (No Rebuy)

**Primary objective**: never bust. All decisions subordinate to survival.

| Policy | Rule | Rationale |
|--------|------|-----------|
| **Minimum Viable Stack** | Never let stack drop below 40 BB. If < 40 BB, **sit out** all hands until blind resets to 20 BB (sit out one orbit). | Avoids forced calls / shoves with weak hands. |
| **Max Playable Fraction** | Never commit > 25% of current stack pre‑flop unless holding AA/KK. Post‑flop, never call a bet > 50% of stack unless nutted. | Preserves stack for future orbits. |
| **Table Join / Sit‑Out** | Only join tables with at least 50 BB effective (based on table average stack). If seated at a table with > 3 LAGs (VPIP>45%) and chip leader < 100 BB, sit out and request new table. | Avoids being squeezed by multiple aggressors. |
| **All‑In Survival** | Call all‑in only with AA/KK (even QQ is borderline). Fold any all‑in if it would reduce stack below 40 BB. | One bust ends qualification. |
| **Blind Stealing** | Never raise‑fold from SB/BB. Only steal from BTN/CO when stack > 60 BB and fold equity > 70% (i.e., opponents have folded to steal > 70% in HUD). Otherwise, fold. | Blind steals are high‑variance; survival first. |

## 5. Do NOT Change

1. **Current VPIP (12.3%) and PFR (4.3%)** – these are the foundation of #1 rank. Widening would increase variance and risk of marginal confrontations. Only adjust specific LAG exploits (see §3) that are table‑scoped.
2. **Passive post‑flop style** – the bot rarely bluffs post‑flop, which protects stack. Introducing bluff raises or delayed c-bets would leak chips without proven edge.
3. **Tight UTG range** – UTG is the highest risk position (avg -100 chips). Do not add any hands below TT/AQs/AKo. This position is strictly for survival.
4. **Fold to 4‑bet without AA/KK** – even QQ is too light. LAGs 4‑bet wide but our stack preservation is paramount.
5. **No rebuy mode** – never deviate from “survival first” mindset even if chip lead grows. Tournament is top‑heavy; a fat stack does not justify looseness.

## 6. Patch Backlog (Ranked)

| Priority | Guard Name | Target Function Area | Regression Spot Idea |
|----------|------------|----------------------|----------------------|
| P0 | **BB_DEFEND_VS_LAG_STEAL** | `decide()` → preflop → blind defence | SB opens 2× from LAG (VPIP=50%), BB holds K7o. Action: **call** (currently fold). |
| P0 | **THREE_BET_LAG_FROM_CO** | `decide()` → preflop → 3bet | CO LAG (VPIP=45%) opens 2.5×, hero on BTN holds 99. Action: **3‑bet to 6×** (currently fold). |
| P1 | **TRAP_AA_VS_3BET** | `decide()` → preflop → response to 3bet | BB Grok agent (3b=50%) 3‑bets hero’s BTN open, hero holds AA. Action: **call** (currently raise). |
| P1 | **FLOAT_FLOP_DRY** | `decide()` → postflop → call cbet | Flop J♠7♣2♥, hero holds Q♣T♣ (gutshot). LAG c-bets 75% pot. Action: **call** (currently fold). |
| P2 | **CHECK_RAISE_TPTK** | `decide()` → postflop → check‑raise | Flop K♠9♦3♣, hero holds K♥Q♥ (top pair good kicker), LAG c-bets 50%. Action: **check‑raise to 3×** (currently call). |
| P2 | **NEMESIS_HUNTERG102_DEFENCE** | `decide()` → preflop vs specific opponent | BTN hunterguy102 opens 2.5×, hero SB holds A♠5♠. Action: **fold** (current: call). |
| P3 | **COLD_START_BB_DEF** | `decide()` → preflop → early hands | First 10 hands, UTG raises 3×, hero BB holds 88. Action: **fold** (currently call). |
| P3 | **SIT_OUT_THRESHOLD** | `table_join.py` → stack management | Stack = 38 BB after losing a pot. Action: **sit out next two orbits** (currently none). |

## 7. Regression / Test Ideas

Frozen spots to verify after each patch.

1. **UTG with AJo against unknown opponent, first 10 hands**  
   Action: **Fold**. (Never open AJo UTG cold‑start.)

2. **BTN with 72o, SB completes, BB checks**  
   Action: **Fold**. (Do not complete from SB with trash.)

3. **BB with K7o vs SB minraise (LAG flag active)**  
   Action: **Call**. (Defend vs LAG steal.)

4. **CO with 99 vs BTN open 2.5× (LAG flag, VPIP 50%)**  
   Action: **3‑bet to 6×**. (Punish wide range.)

5. **BB with AA vs SB 3‑bet (opponent 3b% > 30%)**  
   Action: **Call**. (Trap – do not 4‑bet.)

6. **Flop J♠7♣2♥, hero Q♣T♣, LAG c‑bet 75%**  
   Action: **Call**. (Float with gutshot.)

7. **Stack = 35 BB, mid‑position, hero holds JJ**  
   Action: **Fold to any raise** (sit out one orbit first). (Survival – never commit with stack < 40 BB.)

8. **All‑in from big stack (100 BB) vs hero’s QQ, hero stack = 45 BB**  
   Action: **Fold**. (Only AA/KK calls all‑in with < 50 BB.)

Each test must be deterministic and have a single correct action in the current codebase. Run after any change to `decide()`.