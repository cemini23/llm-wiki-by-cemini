---
title: "Playground S1a — retrospective snapshot (pre-S1b)"
type: brief
tags: [brief, poker, devfun-arena, retrospective, s1a, field-intel]
created: 2026-06-06
competition_id: cmpy2qy65002ud9ej6b7jjq0l
export: reports/exports/playground-s1-s1a-snapshot-2026-06-06/
status: HISTORICAL SNAPSHOT (2026-06-06) — live stats in @briefs/2026-06-03_playground-top20-qualification.md
---

## Target

S1a **build-mode** post-mortem for KO foundation — not S1b compete tuning yet.

## Summary

Snapshot pulled **2026-06-06 ~15:37 UTC** from prod export (site flaky; live re-export timed out after `recent-tables` — used last good prod bundle). **#1 @ 138,917 chips**, 1,873 hands, **9.0% win rate**, **12.3% VPIP / 4.3% PFR** — tight-passive shape validates chips-over-win-rate thesis. Field leaders below us are **loose-aggressive** (0xJeff, Grok cluster) — S1b exploit lane, not S1a width.

---

## Hero snapshot

| Metric | Value |
|--------|-------|
| Rank | **#1** |
| Chips | **138,917** |
| Hands | 1,873 |
| Won | 168 (~9.0%) |
| VPIP / PFR / 3b | 12.3% / 4.3% / 5.1% |
| Style label | tight-passive |
| Chips / hand | **74.2** |

**Compare #2** (0xJeff_ai): 117,592 chips, 984 hands, **119.5 chips/hand** but 40% VPIP — higher variance path.

**Compare old #1** (claude-sonnet-46, now #12): 49,999 chips, 1,380 hands, 18.2% VPIP — we run **~6pp tighter** with **2.8× chips**.

---

## Field composition (3,930 agents in roster; 1,876 table rows)

**Top 5:** avg VPIP **38.0%**, PFR **27.2%** — leaders are wide/aggressive, not nits.

**Top 50 styles:** loose-aggressive 12, balanced-passive 8, loose-measured 6 — **loose-heavy field**.

**Grok cluster:** **327** agents; 7 in top 50 with VPIP **64–75%**.

---

## Nemeses / tablemates (rolling export window)

| Opponent | Tables vs hero | Pots won vs hero | Notes |
|----------|----------------|------------------|-------|
| hunterguy102 | 87 | **18** | Primary repeat villain — prioritize HUD reads S1b |
| v_16 | 20 | 13 | High pot-win rate vs us |
| 0xJeff_ai | 42 | 10 | #2 on board — LAG |
| Thaddius | 69 | 10 | Volume regular |

---

## S1a arc (qualitative — from HL rounds + status logs)

| Phase | Approx | Rank / chips | Lesson |
|-------|--------|--------------|--------|
| Early S1a | Jun 3 | #4 → bleed to **~#215 @ 540** | Cold-start + SB/UTG trash nearly ended season (no rebuy) |
| HL R8–20 | Jun 4–6 | Recovery → **#1 @ 138k** | Regression library + protect modes + stagger locks |
| Patches landed | Jun 6 | — | BTN limp-trash fold (R20), nuts detect on prod |

**KO foundation takeaway:** first **50–200 hands** must assume **no rebuy** — chart-first, zero BTN limp-calls, slow join when ranked.

---

## Data limits (API)

- No street-by-street actions in export — **leak patches still from HL analyze**, not JSONL alone.
- Hero submission payouts in export are **≥0 only** — loss rows need prod analyze.
- `recent-tables` is rolling (~1,876 rows) — not full season replay.

---

## Patch backlog (ranked for KO / S1b)

| Priority | Theme | Evidence | Action |
|----------|-------|----------|--------|
| P0 | Early-bust prevention | Jun 3 rank 215 @ 540 | Cold-start guardrails doc'd in tournament foundation brief |
| P0 | BTN multiway limp | HL R20 #01 | **Shipped** — `prod_q9o_btn_vs_limp` |
| P1 | Nemesis reads | hunterguy102 18 pots | Seed HUD from `agents.jsonl` top tablemates S1b |
| P1 | vs LAG leaders | #2–#4 40–70% VPIP | S1b: `maniac_call_margin_delta` + **no preflop trash vs Grok open** |
| P2 | Width vs claude-sonnet | We 12% vs their 18% VPIP | **Do not widen in S1a**; optional +2–3pp steal vs loose-passive only |
| P2 | Nuts value | River folds | **Shipped** — `CEMINI_NUTS_DETECT=1` |

---

## Phased plan

| Phase | Status | Deliverable |
|-------|--------|-------------|
| **P0** Export | ✅ | `reports/exports/playground-s1-s1a-snapshot-2026-06-06/` |
| **P1** Field report | ✅ | `field_report.txt` in same dir |
| **P2** Premium model pass | ✅ v2 | 4-model merge → `2026-06-06_s1a-premium-retrospective-synthesis.md` (Cursor Grok + Codex + prior API) |
| **P3** S1b append | Jun 11 | Second export dir → diff section appended here |
| **P4** KO env table | Pre-KO | Compete protect + exploit profile from merged retrospective |

---

## P2 prompt stub (premium model — when operator runs)

```text
You are a poker bot strategist. No runtime LLM at decision time — output
structural guards for Python decide() only.

Inputs:
- S1a field report (tight hero #1 at 9% WR vs LAG field)
- HL worst-15 hands (preflop -100 cluster, SB/UTG/BTN)
- Goal: qualify + survive KO hour-one with no rebuy

Output:
1. Top 5 structural gaps (not hand-specific hero calls)
2. Cold-start policy (hands 1–N)
3. S1b exploit toggles vs LAG/Grok (when HUD warm)
4. What NOT to change (width, jackpot merge, etc.)
```

---

## Sources

- Export `reports/exports/playground-s1-s1a-snapshot-2026-06-06/` (prod 2026-06-06T15:37Z)
- @briefs/2026-06-04_playground-s1-competition-intel.md (Jun 4 — superseded by this snapshot for hero rank)
- @briefs/2026-06-06_discord-meta-tournament-foundation.md
- HL rounds 8–20 `reports/hl-loop/`

## Implementation status

| Field | Value |
|-------|-------|
| Status | **SNAPSHOT COMPLETE** |
| Next | P2 premium pass when operator wants; P3 after S1b |
| Blocked by | Site flake for live re-export (non-critical — snapshot fresh) |
