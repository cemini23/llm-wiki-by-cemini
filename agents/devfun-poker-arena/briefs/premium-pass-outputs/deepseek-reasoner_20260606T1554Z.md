## 1. Top 5 Structural Gaps

| Rank | Gap | Chip Risk × Frequency | Guard Category |
|------|-----|----------------------|----------------|
| 1 | **Blind defense too narrow vs LAG steals** | SB/BB avg -100 over 36 hands (36% of sample). Many folds to minraises from BTN/CO cost 1-2 BB each. vs LAG (VPIP>35), folding >80% in SB/BB is -EV. | SB/BB defend threshold vs steal |
| 2 | **UTG/MP hand selection too weak** | UTG -100 avg, MP -99 avg. Only 16-16 hands each, but hero plays very few from these positions, so losses come from the few played. Playing KQo, AJo, 66-88 from UTG loses to LAG 3-bets or multiway. | UTG/MP tight range + fold to 3b |
| 3 | **BTN overfold to preflop raises** | 19 BTN hands avg -98. Worst hands #1, #6, #14, #15 all show board but hero folded postflop or called then folded. Hero is playing Q9o, TQo, KTo from BTN vs unknown – too loose. Should fold all but top 8% vs CO open. | BTN cold-call vs CO open range |
| 4 | **Postflop passivity with strong hands** | Only 3 pots won in 100-hand sample (AA, AA, 6h5d). Hero rarely bets for value or protection. When holding top pair, check-folding too often on wet boards vs LAGs. | Value bet threshold / turn barrel logic |
| 5 | **3-bet frequency too low vs maniacs** | 5.1% 3b vs field avg ~25%+. Hero never 3-bets from SB/BB vs high-VPIP stealers, letting them see flops cheaply. Losing 12-18 pots to nemesis hunterguy102. | Blind 3-bet vs LAG steal (SB vs BTN, BB vs CO) |

**Detail for #1 (Blind Defense):**  
Current policy folds SB to BTN raise with hands like 22-66, A2s-A5s, KJs, QTs. vs LAG (VPIP>40) these are +EV calls because of implied odds and fold equity on later streets. Guard: enable `LAG_DEFEND` only when opponent VPIP >= 38% and hero stack > 30BB.

## 2. Cold-Start Policy (Hands 1–N)

### First 50 Hands (Empty HUD)
- **VPIP target:** 8-10% (tighter than baseline). Open only from CO/BTN with Pairs 77+, ATs+, AQo+.
- **Blind defense:** Fold entirely to any raise. Only play in BB when open-limp missed – trap with premium.
- **3-bet:** Only with AA/KK/AKs (push if raised).
- **No limp-call.** Use limp-folds only if ante structure forces.
- **Table join pace:** Join tables with stack >= 15BB. If below 15BB, wait until blinds pass (if possible) or fold all but AA.

### Hands 51–200 (Partial HUD building)
- If stack > 80BB, gradually open to 12% VPIP. If stack < 40BB, stay at 10%.
- Use static opponent model: treat all as LAG with VPIP=40% for steal defense.
- Enable blind defense vs BTN/CO only when holding pairs 77+ or Axs.
- **No bluffing** into opponents who have seen fewer than 20 hands.

### Flip from Survival to Exploit (After ~200 hands)
- Flip condition: stack >= average field stack (from HUD) AND >= 60BB. Then allow:
  - Widen BTN steal to 25% vs tight blinds (VPIP<15)
  - Call wider in BB vs LAG steals (suited connectors, small pairs)
  - Increase 3-bet vs maniacs to 8-10%

## 3. S1b Exploit Toggles (HUD Warm)

Enable only when opponent hand count >= 50 and specific profile matches.

| Toggle | Trigger | Action | Margin |
|--------|---------|--------|--------|
| **LAG_DEFEND** | Opponent VPIP > 38% AND 3bet% > 10% | Call BTN/CO opens wider from SB/BB (any pair, Axs, KJs, QTs). Don't 3-bet back. | +2-3 BB/100 vs maniacs. Keep frozen if hero stack < 40BB. |
| **GROK_3BET** | Opponent is Grok cluster (VPIP>60%) AND in CO/BTN | 3-bet to 3.5x with TT+, AJs+ from blinds. Fold to 4-bet unless AA/KK. | +5 BB/100 when hit. Use only when stack > 80BB. |
| **NEMESIS_FOLD** | Opponent = hunterguy102 or any who won >10 pots vs hero | Tighten all ranges by 50%: only play pairs 99+, ATs+, AQo+ from any position. Never defend blinds. | Avoid 18-pot deficits. Keep frozen until stack >= 60BB and other tables positive. |
| **SHORT_STACK_TRAP** | Any opponent stack < 25BB | Call their all-in with any pair 33+, A9s+, KQs. Do not raise. | Picks up extra equity vs push charts. |

**Frozen flags** (never change regardless of HUD):
- `CEMINI_NUTS_DETECT` – keep=1
- `PLAY_UPPER_DECK` – never run bluffs on dry boards (bot lacks aggression profile)
- `REBUY_OFF` – never risk > 20% stack on non-premium hand

## 4. KO Foundation (No Rebuy)

| Rule | Detail |
|------|--------|
| **Minimum viable stack for play** | 15BB. Below 15BB, fold all but AA/KK/AKs shove (any position). If stack=10BB, wait for SB to be in BB if possible. |
| **Max playable fraction** | Never commit more than 15% of stack on a single hand unless holding AA/KK. This includes preflop raises, calls, and postflop bets. |
| **Stack recovery threshold** | If stack < 30BB, tighten to 5% VPIP (only pairs TT+, AQs+, AKo). No blind defense. |
| **Survival timeline** | First 60 minutes: stack must stay >= 30BB. If dropping, skip hands 2-3 tables and only play premiums. After 60 min, if stack >= 80BB, begin exploit phase. |
| **Table join logic** | Only join tables where hero stack > 25BB AND table average stack > 20BB. Avoid tables with >2 Grok agents (high variance). |
| **Sit-out policy** | Never sit out. Instead, fold unattractive hands quickly. If tilted (2 consecutive big losses), fold all for 5 hands to reset. |

**Hour-one specific:** no rebuy means chip preservation. Accept that early VPIP may be 6-8% – it's okay. The bots that bust are too loose. Our tightness is our advantage.

## 5. Do NOT Change

1. **Overall VPIP (12.3%)** – Raising it would expose us to maniac 3-bets and bad beats. The current win rate (9.0%) is sustainable because we play few hands but win bigger when we do. Leaderboard #1 proves it.

2. **CO play (+175 avg)** – Already profitable. If we widen CO range, we risk dilution. Keep as is.

3. **Preflop 3-bet frequency (5.1%)** – Increasing it without HUD confidence leads to costly 4-bet folds vs LAGs who 4-bet wide. Only 3-bet with AA/KK/AKs preflop unless exploit toggle active.

4. **Bluffing postflop** – Our aggressive opponents (Grok, LAGs) call too often. Bluffing is -EV. Stick to value betting thin. Only bluff with absolute nuts detection and dry boards.

5. **Blind defense vs UTG opens** – UTG ranges of opponents are tighter. Continuing with wide ranges from blinds vs UTG raise is a leak (our #2 worst position). Keep that frozen.

## 6. Patch Backlog (Ranked)

| Priority | Guard Name | Target Function Area | Regression Spot Idea |
|----------|------------|----------------------|----------------------|
| P1 | LAG_STEAL_DEFEND_SB | `decide_preflop_sb` – increase call range vs BTN/CO open when opponent VPIP > 38% and stack > 30BB. Add: pairs 22-66, A2s-A5s, KJs, QTs, T9s as calls (not 3-bets). | Spot: SB with 44 vs BTN (VPIP 50%) open – must call, not fold. |
| P2 | UTG_TIGHTEN_RANGE | `decide_preflop_utg` – only play pairs 77+, ATs+, AQo+. Remove KQo, AJo, 66- from UTG range. | Spot: UTG with AJo facing LAG raise from MP – must fold. |
| P3 | BTN_COLD_CALL_FILTER | `decide_preflop_btn` – vs CO open, only call with TT+, AJs+, KQs. Fold suited connectors, small pairs. | Spot: BTN with 98s vs CO open (VPIP unknown) – must fold. |
| P4 | BLIND_3BET_VS_STEAL | `decide_preflop_bb` – add 3-bet with TT+, AQs+ when facing BTN minraise from known maniac (3b% >15%). | Spot: BB with AQs vs BTN maniac – must 3-bet to 3.5x. |
| P5 | POSTFLOP_VALUE_BET | `decide_postflop_turn` – with top pair top kicker or overpair on dry board, bet 50-70% pot on