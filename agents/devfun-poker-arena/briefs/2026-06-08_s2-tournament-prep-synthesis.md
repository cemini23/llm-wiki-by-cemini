---
title: S2 tournament prep — S1 tournament + S2 playground retrospective
type: brief
created: 2026-06-08
updated: 2026-06-08
competition_s2_tournament: cmqggiv9k37am11ydmppz466e
status: SHIPPED — s2_tournament_prod_apply.sh + nemesis expansion
---

## Target

CeminiSuite / operator — **Tournament S2** (`cmqggiv9k37am11ydmppz466e`, free entry from Playground S2 qual). S1 tournament busted; S2 playground ended.

## Summary

**Do not repeat S1 tournament nit posture (11% VPIP / 2% PFR).** Win with **TAG 18–25% VPIP / 8–15% PFR** + **archetype exploits** (not field LAG ~36%). **Amplify:** gin lane + stack-off guards (R24–R26), nemesis archetypes, placement_chase steals, ISO vs loose-passive. **Fix:** `CEMINI_NEMESIS_TIGHT=0`, no eval-panel gate in tournament, no HL fold-only rounds. **Steal** top-field patterns from niceh / Thaddius / tight-measured TAGs; **exploit** LAG stations and phoenix/holonomic farms.

## Body

### What we did well

| Signal | Evidence | Keep |
|--------|----------|------|
| Late playground recovery | Gin deploy + R25/R26; chips 842 → ~3k+; HL R26 analyze clean (BTN +, mega −6 worst) | `CEMINI_GIN_STYLE_GATE=1`, stack-off guards |
| Showdown quality when contesting | S2 pack WSD ~67% when engaged; AA spike hands | Value-heavy stack-offs, not auto-fold |
| Archetype exploit framework | premium_nit / wide_passive / linear_aggro shipped | All `CEMINI_NEMESIS_*` toggles ON |
| Regression discipline | R24 AK, R25 99 BTN, R25 A9s, R26 K4o SB | Gate before every deploy |

### What we did poorly (S1 tournament + early S2)

| Failure | Evidence | Fix |
|---------|----------|-----|
| Field mismatch | S1 hero **11.4% VPIP / 1.97% PFR** vs top-20 **28% / 18%** | Gin + placement_chase width; target 18–25% / 8–15% |
| Nemesis-tight blanket | S1 apply had `CEMINI_NEMESIS_TIGHT=1` | **Set to 0** — use archetype lanes only |
| Mega showdown losses | ~99% zero-delta hands; net −21213 mega vs +17549 spikes | Keep paired-river / marginal-ace guards |
| HL fold stacking | Many HL rounds added folds on nit base | **No deploy from fold-only analyze**; widen via gin |
| Export metric confusion | payout_chips proxy ≠ chip rank | Use Arena `score` + HL `chipDelta` |
| MON rebuy waste | ~1,250 MON on S1 rebuys | **No rebuys** unless policy changes |

### Field steal table (S1 tournament export)

| Handle | Rank | VPIP | PFR | Style | Steal |
|--------|------|------|-----|-------|-------|
| niceh | #1 | 25% | 4.7% | balanced-passive | **Steal blinds**; fold to big raises (premium_nit) |
| friend | #2 | 48% | 25% | loose-measured | Fold to 3b/4b; **3b value** vs opens; don't bluff |
| Thaddius | #3 | 24% | 21% | balanced-aggressive | **Defend IP**; linear_aggro nemesis |
| agents_are_the_product | #4 | 45% | 27% | loose-measured | LAG 3b value; exploit lane |
| ed_209_charlie | #5 | 43% | 19% | loose-measured | Same |
| nomindart | #11 | 38% | 10% | loose-passive | **ISO + thin value** |
| stariy_physe | #8 | 26% | 20% | balanced-aggressive | Nemesis defend; don't fold suited broadway |
| kaivan69 / tilt_hazard | top | 16–19% | 13–15% | tight-aggressive | Respect raises; steal when folded |

### Field exploit table (S2 playground pack)

| Handle / cluster | VPIP | PFR | Exploit |
|------------------|------|-----|---------|
| 0xJeff_ai | 41% | 27% | Jeff 4b overlay; linear_aggro defend |
| jagoan_neon | 43% | 35% | Nemesis; 3b value IP |
| holonomic-* | 53% | 18% | **wide_passive ISO** (prefix `holonomic-`) |
| phoenix-rises-* | 26–29% | 8–10% | Phoenix cluster; steal + fold to heat |
| fefou_v2 / alnitak / einstein / long_tu | 7–14% | 2–5% | **premium_nit** — steal blinds, fold marginal calls |
| friend (S2 sample) | 51% | 29% | loose-measured — value not bluff |

### Field mistakes we must not copy

- **High VPIP + low PFR** calling stations (nomindart class) — bleed without accumulation
- **Chasing 36% field VPIP** — rejected in 3-model S2 audit
- **Optimizing payout_chips proxy** — mis-ranks nit bots
- **Blanket nemesis fold** — folds profitable defends vs linear aggro

### Deploy posture (Tournament S2)

```bash
uv run python scripts/regression_gate.py
uv run python scripts/gin_style_gate.py
./scripts/s2_tournament_prod_apply.sh cmqggiv9k37am11ydmppz466e
```

Key env vs S1 tournament apply: `CEMINI_NEMESIS_TIGHT=0`, `CEMINI_EVAL_PANEL_GATE=0`, archetype toggles ON, gin gate ON.

### HL discipline

- Primary comp = Tournament S2 only
- Deploy patches after **≥50 hands** + analyze shows structural leak (not fold-only)
- Target Arena stats **18–25% VPIP / 8–15% PFR** before more code churn

## Sources

- Prod export S1 tournament `agents.jsonl` + hero submissions (1778 hands)
- Prod export S2 audit pack `agents.jsonl` (4981 agents)
- Prior `2026-06-08_s2-heavy-audit-synthesis-v2.md`
- Arena `competition/list-all` — Tournament S2 `cmqggiv9k37am11ydmppz466e` status Upcoming
