# Super-audit prompt — Tournament S10 prod-ship

## Role
Readonly council audit. Report findings with evidence. Do not edit.

## Target
Live Cemini Poker Arena agent on **Tournament S10** (prize money / first place).
Pack artifacts + code paths below.

## Question
Are we configured and playing in the best way to win Tournament S10 prize money (top ~10 money / top ~25 bracket)? What will cause us to lose vs the last tournament winner's style? Rank P0/P1/P2 fixes.

## Constraints
- Readonly auditors
- Prod already entered: `cms7hr1il20ya13wjj29s1o8h`, role `s10_tournament`
- Wallet ~1.4 MON; entry was sponsored 0.01 MON (do not recommend 250 MON rebuy fantasies)
- Gin intentionally OFF; do not casually recommend gin ON without KO-specific evidence
- One lobby process — cannot dual-run Playground S11 while on T10

## Known facts (captured 2026-07-30 ~13:15 UTC)

### Live T10
- Comp: `cms7hr1il20ya13wjj29s1o8h` Active
- Us: **#21 @ 965 chips / 7 hands / 0 won** — early survival folds; field ~23
- Early leader `crimson_range` ~1276 / 14h, VPIP≈PFR≈0.36 (tiny sample)
- Posture: TOURNAMENT_MODE=1, gin OFF, KO_SURVIVAL=1 hands=60 min_stack=600, PRIZE_CUTOFF=10 QUAL=25, PLACEMENT_CHASE=1, join 25/60, NEMESIS includes S10 leaders + early T10

### Tournament S9 winner (Ended)
- **#1 halloran** 90273 chips / 5563 hands / 953 won (~17% win)
- Stats: VPIP **0.26**, PFR **0.11**, 3bet 0.041, AF **1.05**, WTSD 0.19, WSD 0.53, style **balanced**
- Chip/hand ≈ **16.2** vs #2 blacksite ≈3.9 — dominant accumulation, not ultra-nit
- #2–5: blacksite, kuma_zero, ronin, reaper (repeat KO names)

### Tournament S8 winner
- **#1 royal_79f44c** VPIP 0.18 PFR 0.14 AF **3.86** (balanced-aggressive / shark)

### Hypothesis to stress-test
Hour-one KO survival (60 hands / fold-heavy) may be **too nitty** vs halloran-style balanced accumulation and will lose blind tax before money bubble. Nemesis list may omit **halloran** / **royal_79f44c** / **vigilate** / **reaper**. Status script still prints Playground top-20 language for tournament comps (cosmetic).

## Read order
1. FACTS.md (this pack)
2. t10_env_ko.txt
3. t9_winner.txt
4. t10_status.txt
5. Code: run_cemini_lobby.py s10_tournament posture; KO survival in decide/lobby; s10_tournament_prod_apply.sh

## Output format
1. Verdict: SHIP / REWORK / REJECT for current T10 posture
2. Consensus risks (≥2 auditors would agree)
3. Unique findings
4. Ordered patch backlog (P0 must-fix now / P1 / P2)
5. Explicit: keep gin OFF or not — with evidence
