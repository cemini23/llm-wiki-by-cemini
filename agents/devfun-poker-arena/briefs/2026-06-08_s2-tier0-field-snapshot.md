---
title: S2 Tier-0 field snapshot — top 20 + nemesis adds
type: brief
tags: [brief, poker, devfun, s2, tier0, nemesis, qualification]
created: 2026-06-08
updated: 2026-06-08
target: CeminiSuite operator — S2 qual climb
competition_id: cmq57o53r0bhw18g23qkydb08
---

## Target

CeminiSuite / operator — **S2 playground qual** (`cmq57o53r0bhw18g23qkydb08` → Tournament S2). Tier-0 = leaderboard + API stats only; no export steal-audit (hero ~47h, field samples 4–92h).

## Summary

**Hero:** rank **#60**, **1,072** chips, **47** hands — **+917** to #20 floor (**1,989** @ `wasted_tokens`). **Do not** copy LAG lanes (#2 `range_ledger` 70% VPIP, #15 `arjun_c` 68%). Respect TAG leaders (#1 `den_zel21` 25% VPIP, #4 `long_ngu_poker` 21% AF 2.2). **Nemesis adds:** `range_ledger`, `arjun_c`, `rvkkv1`, `long_ngu_poker`, `damon` (append to prod list; keep exploit lane on).

**HL:** S2 round 1 patch shipped — **22 CO** ace-paired river (`prod_22_co_paired_river`). **Next HL analyze at ≥95 hands** (state: `reports/hl-loop/state.json`, `rerun_delta=50`).

## Body

### Qual posture (2026-06-08 API)

| Metric | Value |
|--------|-------|
| Field | 290 ranked |
| #20 cutoff | 1,989 chips / 21h (`wasted_tokens`) |
| Hero | #60 / 1,072 / 47h / 7 won |
| Gap | +917 chips |
| Jackpots | 72o **10/10 claimed** (hunt off); royal **5/5** @ 13,600 MON (showdown on) |
| Pace | `CEMINI_PACE_PHASE=volume` |

### Top 20 by chips (Tier-0 stats)

| # | Handle | Chips | H | VPIP | PFR | 3B | AF | Archetype | Steal vs exploit |
|---|--------|------:|--:|-----:|----:|---:|---:|-----------|------------------|
| 1 | den_zel21 | 7,623 | 68 | 25% | 12% | 5% | 1.2 | TAG volume | Respect — do not widen to match |
| 2 | range_ledger | 4,312 | 84 | **70%** | 38% | 24% | 1.1 | LAG maniac | **Nemesis** — fold trash vs open; no float |
| 3 | tayleigh_v3 | 3,988 | 57 | 30% | 2% | 0% | 1.2 | Passive fit-or-fold | Ignore steals; punish passivity IP |
| 4 | long_ngu_poker | 3,632 | 92 | 21% | 8% | 0% | **2.2** | TAG shark | **Nemesis** — tight vs; no bluff-catch marginal |
| 5 | claude-sonnet-46 | 3,523 | 61 | 34% | 5% | 0% | 0.5 | Passive caller | Free cards OK; don't pay rivers light |
| 6 | damon | 3,456 | 54 | 41% | 35% | 0% | **9.8** | Hyper-aggro | **Nemesis** — trap premiums; fold weak vs barrels |
| 7 | ebay | 3,170 | 79 | 44% | 4% | 4% | 0.8 | Loose passive | Iso-raise value; no bluff thin |
| 8 | float_engine | 3,007 | 51 | 49% | 35% | 0% | 1.5 | LAG (S1 EV ref) | Watch — optional nemesis if shared table bleed |
| 9 | Snaggletooth | 2,848 | 76 | 18% | 13% | 5% | 5.7 | Nit aggro | Respect — steal dead buttons only |
| 10 | ZeroDay | 2,648 | 9 | — | — | — | — | Small sample | Ignore until ≥40h |
| 11 | adah_rain | 2,469 | 90 | 30% | 17% | 0% | 1.4 | Standard TAG | Neutral |
| 12 | ranged_river_bot | 2,322 | 61 | 13% | 3% | 0% | 0.7 | Ultra-nit | Don't bluff; value bet thin |
| 13 | Ryan_C | 2,315 | 14 | 86% | 0% | — | 0.6 | Micro-sample LAG | Ignore until volume |
| 14 | null_hypothesis_v14 | 2,313 | 45 | 13% | 9% | 8% | 4.0 | Nit 3-bet | Fold dominated broadway vs 3b |
| 15 | arjun_c | 2,282 | 57 | **68%** | 39% | 8% | 0.9 | LAG station | **Nemesis** — same as range_ledger |
| 16 | felt_theorem | 2,131 | 38 | 13% | 3% | 7% | 2.2 | Nit | Respect |
| 17 | rvkkv1 | 2,101 | 67 | **67%** | 9% | 0% | 0.5 | Calling station | **Nemesis** — value wide; no bluff |
| 18 | lucky_gull | 2,009 | 6 | — | — | — | — | Micro sample | Ignore |
| 19 | stoneheron61 | 2,006 | 4 | — | — | — | — | Micro sample | Ignore |
| 20 | wasted_tokens | 1,989 | 21 | 48% | 38% | — | 2.0 | Loose agg (low n) | Cutoff anchor — pass with volume + discipline |

VPIP/PFR/AF from `/texas/agent-stats` per agent [TENTATIVE — sample 4–92h].

### Recommended nemesis handle adds

**Current prod:** `hunterguy102,thaddius,v_16,0xJeff_ai` + `CEMINI_NEMESIS_EXPLOIT=1`

**Append (Tier-0 evidence):**

```
range_ledger,arjun_c,rvkkv1,long_ngu_poker,damon
```

**Proposed full string:**

```
hunterguy102,thaddius,v_16,0xJeff_ai,range_ledger,arjun_c,rvkkv1,long_ngu_poker,damon
```

| Handle | Why |
|--------|-----|
| range_ledger | #2, 70% VPIP / 24% 3b — field LAG template; never copy width |
| arjun_c | #15, 68% VPIP — same lane |
| rvkkv1 | #17, 67% VPIP / 9% PFR — station; value-only |
| long_ngu_poker | #4, 21% VPIP AF 2.2 — competent TAG; tighten opens vs, trap value |
| damon | #6, AF 9.8 — barrel-heavy; fold marginal SDV |

**Defer:** `float_engine` (optional 6th), micro-sample ranks 10/13/18/19. **Not nemesis:** `den_zel21`, `Snaggletooth`, `ranged_river_bot` — play straight TAG.

### HL patch this session

| Analyze row | Patch | Regression |
|-------------|-------|------------|
| #01 22 CO −9 `A88xA` | Lower IP underpair threshold for 22–99 on paired boards (0.12; 0.08 if ace-paired) | `prod_22_co_paired_river` |

### Next HL hand threshold

| Field | Value |
|-------|-------|
| Competition | `cmq57o53r0bhw18g23qkydb08` |
| HL round | 1 → 2 after deploy |
| Last analyze | **45** hands |
| **Next HL rerun** | **≥95 hands** (`CEMINI_HL_RERUN_DELTA=50`) |
| Command | `ARENA_LOBBY_COMPETITION_ID=cmq57o53r0bhw18g23qkydb08 HL_ROUND=2 ./examples/cemini_hl_loop.sh --from-prod` |

## Sources

- API leaderboard + agent-stats 2026-06-08
- `reports/hl-loop/latest_analyze.txt` (45h S2 R1)
- @agents/devfun-poker-arena/briefs/2026-06-08_s2-heavy-audit-synthesis.md
