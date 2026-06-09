---
title: "Gemini DR — WC 2026 knockout market map v2 (phase router backlog)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, knockout, polymarket, kalshi, phase-router, k99]
keywords: [kxwcgame, kxwcround, match-moneyline, round-of-32, liquidity-rewards, june-28-transition]
related:
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md
  - sources/gemini-wc-tournament-phase-router-architectural-spec-2026-05-31.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/tools/world-cup-bot.md
  - sources/gemini-wc2026-prediction-markets-inventory-2026-06-09.md
maturity: validated
created: 2026-06-05
updated: 2026-06-09
---

## Relations

- @sources/gemini-wc-knockout-market-map-2026-05-30.md — prior K85 map; this Jun 5 report adds LP priority stack + calendar anchors
- @concepts/world-cup-tournament-phases-lp-strategy.md — consumer for `market_phases.yaml` / phase router
- @entities/tools/world-cup-bot.md — **not** Module 6 v1 scope; backlog for post–Jun 27 transition

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 Knockout Market Map |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/gemini-wc2026-knockout-market-map-2026-06-05.docx` |
| Retrieved | 2026-06-05 |
| Read status | deep-read |

## Narrative

Architectural spec for **post–group-stage** bot expansion (advance LP + cross-venue v2). Supersedes K85 detail on match-level priority and phase calendar.

### Scanner / LP priority stack

1. Match-level 90-min 1X2 (PM vs / Kalshi `KXWCGAME`) — highest volume + ~$30k/match LP rewards
2. Advance / R32 qualifiers
3. R16 / QF / SF reach (`KXWCROUND`)
4. Final / winner futures
5. Props (penalties, team goals)

### Phase transition calendar [CONFIRMED]

| Phase | Dates (2026 UTC) | Bot action |
|-------|------------------|------------|
| Group stage | Jun 11 – Jun 27 | Advance regex + group qualify |
| Round of 32 | Jun 28 – Jul 3 | Stop advance scan; pivot match ML |
| R16 | Jul 4 – Jul 7 | R16 reach markets |
| QF | Jul 9 – Jul 11 | QF reach + match books |
| SF | Jul 14 – Jul 15 | SF reach; Kalshi elim grading rules |
| Final | Jul 19 | Winner / reach-final settle |

### Resolution traps

- PM match ML: **90 min only** — ET → Draw wins 1X2
- Kalshi stage-of-elimination: SF loser graded at SF regardless of third-place match
- Postponement / oracle dispute — cross-venue hedge capital lock

### Module 6 v1 scope

**Out of scope until phase router ships** — document for ROADMAP / `OPEN-GAPS.md`; do not auto-add `KXWCGAME` pairs without rules_hash review.

## Snippets

> "The bot must possess a rigid internal scheduling mechanism that halts the scanning of advance to the knockout stages regex patterns precisely on June 28." [Source: World Cup 2026 Knockout Market Map.docx]

> "Match-level markets generate the highest daily trading volume and receive the largest allocation of liquidity incentives from the protocol." [Source: World Cup 2026 Knockout Market Map.docx]
