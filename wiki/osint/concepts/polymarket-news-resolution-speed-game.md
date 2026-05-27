---
title: Polymarket news-resolution speed game (PMV capture)
type: concept
tags: [concept, polymarket, microstructure, news-trading, latency, k69]
keywords: [pmv, pre-news-mispriced-value, fomc, bls, cpi, earnings, 0xkeshav]
related:
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/polymarket-updown-15min-execution-latency.md
  - concepts/polymarket-bot-architecture.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/trading-posts-compilation-20-2026-05-27.md — Post 10 (@0xkeshav_)
- @concepts/polymarket-updown-15min-execution-latency.md — complementary latency discipline
- @concepts/polymarket-bot-architecture.md
- @entities/platforms/polymarket.md

## Raw Concept

K69 @0xkeshav_ empirical study: event-resolved Polymarket categories (FOMC, BLS unemployment, CPI, earnings) where resolution timestamp is known. Measures **Pre-news Mispriced Value (PMV)** on the ask side and how fast wallets capture it after the headline.

## Narrative

### PMV definition

PMV = Σ (1 − price_i) × size_i over all ask levels — max profit if bought immediately before news and held to $1 resolution.

### Findings [TENTATIVE — single author, $4M flow sample]

- **95.5%** of capturable PMV taken within **30 seconds** of headline (aggregate claim)
- FOMC markets often have **smallest** pre-news window (efficient pre-pricing)
- Top cited wallet **$145k+** lifetime PnL on this activity class
- Bots monitor **official source websites** for resolution text faster than human traders

### Cemini / prod implications

- Not the same edge class as UpDown window bots — requires **news wire + CLOB snapshot** infrastructure
- Egress-fi answers on "can retail copy this?" → **no** without sub-second ingestion and co-located execution
- Aligns with maker/taker latency lessons in @concepts/polymarket-updown-15min-execution-latency.md

## Snippets

> "Six-figure profits captured by the fastest traders… 95.5% capturable value gone within 30s." [Source: Posts.docx K69 Post 10, @0xkeshav_]
