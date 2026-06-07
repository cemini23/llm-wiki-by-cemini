## 1. Top 5 structural gaps

1. **Cold-start overexposure to blind bleed and marginal spots**  
   Early S1a near-bust confirms that the first 50-200 hands need a hard survival envelope before any exploit logic.
2. **Incomplete CO mirror of shipped BTN limp-trash guard**  
   BTN R20 is shipped, but similar low-EV CO limp/call paths still need explicit structural denial.
3. **Blind defense policy is under-specified by phase**  
   Current logic needs explicit phase gates so S1a/KO hour-one remains fold-heavy, while S1b can conditionally defend vs proven maniacs only.
4. **Exploit toggles lack strict activation contract**  
   Deep exploit ideas (3-bet value vs LAG, selective BB defend, trap AA/KK) require hard HUD+stack+rank constraints to avoid drift into widening.
5. **KO stack preservation rules are not codified as a unified foundation**  
   No-rebuy demands explicit minimum viable stack, preflop commit caps, and join/sit pacing controls independent of temporary leaderboard position.

## 2. Cold-start policy

**Hands 1-50 (hard lockdown):**
- VPIP cap: 8-10%; no curiosity calls, no speculative steals.
- No CO/BTN opportunistic steals unless table data exists (minimum 10 observed hands per relevant villain).
- No blind defense vs raises except clear top-chart exceptions already in survival chart.
- No exploit toggles, no widening by opponent name alone.

**Hands 51-200 (controlled warmup):**
- Maintain base tight profile (around current 12.3/4.3 trajectory, not above it).
- Enable only chart-consistent actions plus shipped guards (BTN limp-trash R20, nuts detect, stagger locks).
- Continue fold-first in SB/BB unless HUD proves a maniac seat and stack/risk criteria are satisfied.

**Flip condition from survival to exploit (S1b-only lane):**
- At least 20 observed hands on >=2 villains at table.
- Hero stack >= 60bb.
- Not in qualification-protect mode.
- Exploit remains table-scoped, not global range widening.

## 3. S1b exploit toggles

Enable these only when `HUD warm + stack >= 60bb + maniac-confirmed table`:

- **`THREE_BET_LAG_VALUE_ONLY`**: vs CO/BTN opens from VPIP > 45% / high PFR villains, use value-heavy 3-bet lane (JJ+, AQ+), fold to strong 4-bet pressure without top tier.
- **`DEFEND_BB_VS_STEAL_CONDITIONAL`**: allow bounded BB defend expansion versus repeated stealers; never convert into broad defend-default policy.
- **`TRAP_AA_KK_VS_HIGH_3BET`**: optional slowplay line only against confirmed high 3-bet maniacs; off by default in S1a/KO hour-one.
- **`NEMESIS_EXTRA_TIGHT`**: against hunterguy102 profile, tighten further vs opens rather than entering ego pots.

Frozen until KO-safe / S1b condition:
- Broad postflop MDF float expansions.
- Aggressive check-raise bluff layers.
- Any global VPIP/PFR lift.

## 4. KO foundation

- **No rebuy posture:** survival has strict precedence over theoretical exploit EV.
- **Minimum viable stack posture:** when stack is stressed, shift to protection/join pacing instead of forcing volume.
- **Preflop risk cap:** keep stagger-lock discipline and hard cap normal preflop commit fraction; only top-tier exceptions bypass.
- **Hour-one rule:** run cold-start lockdown regardless of recent leaderboard success.
- **Table selection bias:** avoid high-maniac concentration when stack is vulnerable; prioritize low-volatility seat quality.

## 5. Do NOT change

1. Core survival identity: tight-passive baseline that produced rank #1 outcome.
2. Base profile anchor: roughly current 12.3% VPIP / 4.3% PFR regime.
3. Shipped `BTN limp-trash R20` behavior.
4. Shipped `CEMINI_NUTS_DETECT=1` safety gating.
5. Shipped stagger lock and HL R8-20 patch philosophy.

## 6. Patch backlog table

| priority | guard name | target function area | regression spot idea |
|---|---|---|---|
| P0 | `COLD_START_NO_STEAL_UNTIL_DATA` | preflop cold-start gate | BTN 98s, first 10 hands unopened -> must fold |
| P0 | `CO_LIMP_TRASH_MIRROR_R20` | CO limp/call filter | CO Q5o vs multi-limp -> fold |
| P0 | `SB_COMPLETE_TRASH_BLOCK` | SB complete branch | SB 72o in limped spot -> no complete |
| P1 | `JOIN_PACE_STACK_PROTECT` | lobby/join pacing guard | stack < buy-in posture -> longer retry / protect mode |
| P1 | `NEMESIS_HUNTER_TIGHTEN` | villain-specific preflop response | SB A5s vs hunterguy102 open -> fold |
| P2 | `THREE_BET_LAG_VALUE_ONLY` | S1b exploit preflop module | JJ+ / AQ+ vs VPIP>45 CO open -> controlled 3-bet |
| P2 | `TRAP_AA_KK_VS_HIGH3B` | S1b exploit response-to-3bet | AA vs maniac 3-bet -> trap-call lane |
| P3 | `POSTFLOP_MDF_DRYBOARD_DEFERRED` | postflop anti-cbet layer | dry-board float tests gated and off by default |

## 7. Regression test ideas

1. **Cold-start BTN no-steal:** first 10 hands, BTN 98s unopened -> forbidden action: open-raise.
2. **CO limp-trash mirror:** CO Q5o after limp(s) -> forbidden action: complete/iso/call.
3. **SB trash complete block:** SB 72o in limped pot -> forbidden action: voluntary complete.
4. **Nemesis tighten:** vs hunterguy102 open, SB A5s -> forbidden action: defend call.
5. **S1a blind lockdown:** unknown villain steals early; BB K7o -> forbidden action: exploit defend when HUD not warm.
6. **S1b toggle gate:** maniac-like action but hero <60bb -> forbidden action: activate `THREE_BET_LAG_VALUE_ONLY`.
7. **Trap gate integrity:** AA vs normal reg 3-bet -> forbidden action: trap-call line (should remain standard unless high-3b condition met).
8. **KO risk cap:** non-premium facing large preflop commitment -> forbidden action: commit beyond cap.

## 8. Agreement with prior passes

- **With Grok:** fully aligned on survival-first, no base widening, and preserving shipped structural guards that stabilized S1a.
- **With DeepSeek:** aligned that selective S1b exploitation can exist, but only as strict table-scoped toggles with hard activation gates.
- **With synthesis brief:** aligned to adjudication that S1a/KO hour-one remains lockdown; S1b gets conditional exploit lanes only.

## 9. New insights

1. The key failure mode is not "lack of aggression" globally; it is **phase confusion** (exploit logic appearing before risk budget permits).
2. A clean two-lane architecture (Survival Lane vs Conditional Exploit Lane) is the safest way to absorb DeepSeek value without violating Grok survival thesis.
3. Nemesis handling should be **tightening-first**, not counter-aggression-first, to avoid ego-volatility in no-rebuy contexts.
4. KO policy should be implemented as invariant guards, not operator mood or rank-dependent overrides.
5. Regression suite should test forbidden actions explicitly; disallowing bad branches is more important than adding many new aggressive branches.

## 10. Reject from prior passes

- Reject any recommendation to widen base VPIP/PFR in S1a or KO hour-one.
- Reject broad BB defend expansion as default behavior.
- Reject generalized postflop float/check-raise aggression rollout without replay-proven stability.
- Reject any exploit activation that does not satisfy HUD warmth + stack + qualification-protect gates.
- Reject "leaderboard vanity" adjustments that increase variance while already holding qualification-leading chips.
