---
title: Polymarket sports-market bot taxonomy (7 types)
type: concept
tags: [concept, polymarket, sports, microstructure, trading-bot, k69]
keywords: [retrovalix, cross-line-arb, stale-probability, sports-markets]
related:
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
maturity: draft
created: 2026-05-27
updated: 2026-05-29
---

## Relations

- @sources/trading-posts-compilation-20-2026-05-27.md — Post 14 (@RetroValix)
- @concepts/polymarket-updown-bot-taxonomy.md — K52 **crypto Up/Down** 6-type taxonomy (different market class)
- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — same author, prior Up/Down post
- @concepts/world-cup-advance-market-bot-v1.md — K82 advance-market LP is Type 2 (stale probability) + conviction overlay, not in-play microstructure

## Raw Concept

K69 @RetroValix: seven bot archetypes on **Polymarket sports** markets (not short-crypto Up/Down). Common thread: trade **microstructure** (stale lines, cross-market lag, book desync) — not sports outcome prediction.

## Narrative

| # | Type | Mechanism |
|---|------|-----------|
| 1 | Cross-line arb | Connected lines (ML, spread, O/U, BTTS) desync after live state change |
| 2 | Stale probability | PM price vs external fair line / model |
| 3–7 | (Author enumerates additional types in post) | Order-book / live-state lag patterns [TENTATIVE — read full post for labels] |

**Relation to K52:** @RetroValix also authored the 6-type **Up/Down crypto** taxonomy (@concepts/polymarket-updown-bot-taxonomy.md). This page covers **sports** only.

[TENTATIVE] — "1,000 profitable bots analyzed with Claude" is unverifiable; taxonomy is useful as a map, not as audited fact.

## Snippets

> "They do not make predictions on sports itself, but trade market microstructure: stale probability, lag between connected lines…" [Source: Posts.docx K69 Post 14, @RetroValix]
