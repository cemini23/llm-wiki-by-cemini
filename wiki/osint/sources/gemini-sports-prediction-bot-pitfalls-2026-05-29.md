---
title: "Gemini DR — Sports prediction bot pitfalls & deployment checklist"
type: source
read_status: read
tags: [source, gemini-deep-research, prediction-markets, bot-architecture, sports, world-cup-2026, k82]
keywords: [adverse-selection, oracle-risk, partial-fill, cross-venue, regulatory, microstructure, retrovalix]
related:
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/cross-venue-arbitrage-pattern.md
  - sources/polymarket-nba-arbitrage-2605.00864.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/polymarket-updown-bot-taxonomy.md — RetroValix six bot archetypes referenced in report
- @sources/polymarket-nba-arbitrage-2605.00864.md — combinatorial arb depth caps (~15 shares median)
- @concepts/world-cup-advance-market-bot-v1.md — WC deployment matrix at end of report

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sports Prediction Bot Pitfalls and Checklist |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Sports Prediction Bot Pitfalls and Checklist.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

Exhaustive failure-mode catalog for automated bots on **Polymarket × Kalshi** sports markets, with **2026 World Cup deployment blueprint** closing section.

### Directional alpha fallacy

- NBA PM volume 17× YoY but **combinatorial arb median executable size ~15 shares**; theoretical 101 bps ≠ scalable jackpot.
- **Favorite-longshot bias** persistent; sub-10% tails realize ~14% — longshot bots bleed.
- Retail **72h overcorrection** after news — directional models mistake noise for edge.

### LP farming pitfalls

- Live-event **step-function** probability → passive limits picked off; blockchain latency widens window.
- **79% of PM traders never earned $1 in LP rewards** [TENTATIVE — Dune/on-chain citation in report].
- Quadratic scoring forces quotes **into** toxic zone; whale dilution collapses share.

### Cross-venue arb killers

1. **Oracle divergence** — UMA manipulation precedent (Ukraine minerals, Mar 2025).
2. **Contract misidentification** — 90-min vs extra-time winner definitions.
3. **Partial-fill orphans** — non-atomic legs; **sub-5s hedge timeout** then emergency flatten.
4. **Gas/fee compression** — micro-arbs negative after Polygon gas.

### Regulatory fragmentation [NEEDS VERIFICATION 2026-05-29]

- Third Circuit Kalshi preemption vs Ninth/Sixth skepticism; Arizona criminal charges Mar 2026 [TENTATIVE — verify before prod reliance].
- Bot must tolerate **geoblock + sudden liquidity evaporation**.

### WC 2026 blueprint (report DO/DON'T matrix)

| DO | DON'T |
|----|-------|
| Microstructure / repricing lag vs sportsbooks | Directional Elo/xG models at scale |
| Limit orders only; sub-5s cross-venue timeout | Market orders; passive quotes during live play |
| Verify resolution semantics per contract | Blind PM↔Kalshi hedge on headline match |
| Short capital lock (intra-match / advance repricing) | Multi-week winner futures as primary bankroll |
| Geo routing + kill switch | Ignore jurisdictional counterparty risk |

Aligns with **World Cup Bot v1** scope: LP + alert-only cross-venue, not match-level microstructure.

## Snippets

> "The transition from trading against traditional sportsbooks to navigating peer-to-peer central limit order books introduces unique microstructure challenges." [Source: Sports Prediction Bot Pitfalls and Checklist.docx]

> "A bot attempting to scale directional alpha or risk-free extraction is strictly confined to the retail scale." [Source: Sports Prediction Bot Pitfalls and Checklist.docx — citing NBA arb paper]
