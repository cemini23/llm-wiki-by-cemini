---
title: "Gemini DR — World Cup 2026 cross-venue arbitrage dynamics"
type: source
tags: [source, gemini-deep-research, world-cup-2026, polymarket, kalshi, cross-venue, module-6, k83]
keywords: [contract-mapping, kalshi-ticker, conditional-token-framework, fee-model, semantic-equivalence]
related:
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md
  - sources/gemini-wc2026-market-probability-gaps-2026-06-05.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md — live May 29 verification supersedes book-implied gaps for group-winner pairs
- @concepts/world-cup-advance-market-bot-v1.md — Module 6 alert-only scanner

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FIFA World Cup Market Arbitrage Analysis |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/FIFA World Cup Market Arbitrage Analysis.docx` |
| Retrieved | 2026-05-29 |
| Read status | skimmed (reference architecture; live pairs in market-gap source) |

## Narrative

Long-form **PM × Kalshi** architecture for WC 2026: regulatory split (CFTC Kalshi vs crypto-native PM), contract taxonomy, fee friction, and ticker naming patterns. Implementation reference for Module 6 — **not** auto-execution.

### Contract taxonomy (Kalshi)

| Stage | Example ticker pattern |
|-------|------------------------|
| Round of 16 qualify | `KXWCROUND-26RO16` |
| Group qualifiers (R32) | `KXWCGROUPQUAL-26{b}` |
| Group winner | `KXWCGROUPWIN-26{b}` |
| Match winner | `KXWCGAME-26JUN12…` |

### Equivalence rules [CONFIRMED]

- **Group winner ≠ advance** — third-place teams can advance without winning group.
- **Group qualify ≠ R16 qualify** — sequential knockout stages.
- **Fee floor:** Kalshi ~7% on profit → gross gap must exceed ~5pp for net positive arb.

### Bot implication

Alert-only v1: poll read-only APIs, human review on ≥5pp **after** rules-hash match. Ticker map lives in `world-cup-bot/config/cross_venue.yaml`.

## Snippets

> "Polymarket functions as an offshore, crypto-native DEX… Kalshi operates strictly within the United States under CFTC purview." [Source: FIFA World Cup Market Arbitrage Analysis.docx]
