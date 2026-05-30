---
title: "World Cup 2026 — tournament phases LP strategy (group → final)"
type: concept
tags: [concept, world-cup-2026, polymarket, knockout, lp-bot, tournament-phases, k85]
keywords: [knockout-round, reach-final, in-play, lineup-injury, phase-router, market-phases]
related:
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - entities/tools/world-cup-bot.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-05-29
updated: 2026-05-30
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — v1 scope = group advance only; this page plans v2 through final
- @concepts/polymarket-sports-lp-operating-rules.md — cancel window, fill handler invariants apply to all phases
- @sources/gemini-wc-knockout-market-map-2026-05-30.md — DR 08 market inventory + calendar
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — DR 09 pregame/in-play/knockout gates
- @entities/tools/world-cup-bot.md — `config/market_phases.yaml`; phase router DR 10 pending

## Raw Concept

User requirement (K85): comprehensive World Cup bot through finals, not group-stage-only. **DR 08 + 09 ingested 2026-05-30.** v1 ships group advance LP (Issue 3); v2 adds knockout via phase router after DR 10.

## Narrative

### Market taxonomy (DR 08 ingested)

| Phase | PM market type | LP v1 | LP v2 |
|-------|----------------|-------|-------|
| Group | Advance to knockout (= **R32** in 48-team) | **IN** | Keep |
| Knockout | Reach R16 / QF / SF / Final | OUT | **IN** (milestone LP) |
| Knockout | Match 90-min moneyline | OUT | OUT (hard halt at 90′) |
| Knockout | Match To Advance (ET/pens) | OUT | Research only |
| Long | WC winner (immediate No on KO exit) | OUT | Alert only |
| Props | Golden boot, specials | OUT | OUT |

Kalshi **`KXWCSTAGEOFELIM`** pairs to PM Reach markets with **inverted** logic — Module 6 must flip probabilities.

### FIFA 2026 calendar triggers

| Date | Event | Bot action |
|------|-------|------------|
| 2026-06-11–27 | Group stage | `active_phase: group_advance` |
| **2026-06-27** | Final group MD + third-place math | **Zero-day risk** — precompute bracket; expect R32 market surge |
| 2026-06-28–07-03 | Round of 32 | Activate R32 scanner; Reach-R16 ≈ To Advance parity |
| 2026-07-04+ | R16 → Final | Roll regex priority QF → SF → Final; deprecate prior round patterns |
| 2026-07-09–11 | QF rest window | Widest spreads OK — lowest adverse-selection KO epoch |

### Issue matrix (DR 09 ingested)

| Category | v1 posture | v2 target |
|----------|------------|-----------|
| Pregame XI / injury | T-10h cancel; leak → **human_review**; confirmed XI → **full skip** | Webhook book-pull + re-enter after 5–60m |
| In-play goals | **Hard halt** at Live | Opta auto-halt + optional wide-spread taker mode |
| Cross-group contagion | Manual flat before MD3 concurrent kicks | 48-team advancement matrix |
| 90-min vs To Advance | N/A (no match LP) | `resolution_class` tag + separate scanners |
| Ghost quote (KO exit) | Manual cancel | Auto cancel team futures T-5min before expected end |
| Elimination cascade | Manual cancel | `cancel --team` all phases |
| Phase transition | Manual YAML | Phase router (DR 10) |

### Cancel-window by phase (DR 09 — v2 config)

| Phase | Hours before kickoff |
|-------|---------------------|
| Friendlies / early group | 10 (v1 live today) |
| Final group concurrent MD3 | 12 |
| Knockout R32 → Final | 24 |

### Config + research status

| Artifact | Status |
|----------|--------|
| `config/market_phases.yaml` | Populated from DR 08 (research stubs for KO phases) |
| DR 10 phase router | Pending user run (~2:40) — **use prose + JSON appendix**, not JSON-only |
| `conviction-staleness` DR | Due 2026-06-06 LP safety cadence |

### Milestones

| When | What |
|------|------|
| 2026-06-03 | v1 launch (group advance) |
| 2026-06-06 | LP safety DR + conviction refresh |
| Post-group | Phase router implementation (~4d est. from DR 08) |

## Snippets

> Zero-day transition 2026-06-27: all remaining advance markets resolve as third-place math finalizes while R32 match markets open. [Source: gemini-wc-knockout-market-map-2026-05-30.md]

> v1: never quote Live; never chase live LP reward tiers. [Source: gemini-wc-inplay-pregame-lp-risks-2026-05-30.md]
