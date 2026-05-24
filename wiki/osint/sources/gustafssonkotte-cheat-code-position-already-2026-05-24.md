---
title: "@Gustafssonkotte — Updating the cheat code (position-already gate, not direction)"
type: source
tags: [source, trading-posts, polymarket, btc-updown, gustafssonkotte, k62]
keywords: [gustafssonkotte, btc-5min, direction-efficiency, position-already, dynamic-threshold, quadrant-deprecation, env-flag, k62]
related:
  - entities/people/gustafssonkotte.md
  - concepts/polymarket-btc-already-position-gate.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/polymarket-bot-architecture.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
maturity: validated
read_status: deep-read
created: 2026-05-24
updated: 2026-05-24
clusters: [polymarket, bot-architecture]
---

## Relations

- @entities/people/gustafssonkotte.md — author; third major architecture post (after K55 rewrite, K57 quadrant/blacklist)
- @concepts/polymarket-btc-already-position-gate.md — K62 synthesized concept
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — prior Q1/Q2/Q3 stack now **deprioritized** for direction vote
- @concepts/multi-module-bot-conflict-detector-pattern.md — K55 conflict-detector lineage
- @concepts/polymarket-updown-bot-taxonomy.md — 5-minute UpDown market class
- @concepts/polymarket-bot-architecture.md — guard-stripping / execution plumbing
- @sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md — K62 primary source
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — K55 Post 3 (conflict-detector rewrite)

## Raw Concept

- **Title**: UPDATING THE CHEAT CODE FOR POLYMARKET
- **Author**: @Gustafssonkotte (X)
- **Type**: operator architecture essay (~2 weeks after direction-chasing)
- **Location**: `research to be indexed/@Gustafssonkotte.docx` → `cemini-librarian:/opt/cemini-bulk/research/@Gustafssonkotte.docx`
- **Retrieved**: 2026-05-24
- **Read status**: deep-read

## Narrative

### Independent verification (2026-05-24)

| Claim | Status |
|-------|--------|
| n=330 direction ≈49% | **[TENTATIVE]** — author-reported only; no public `polymarket.com/@gustafssonkotte` profile (404); wallet not published in docx |
| Day-one 9 trades, 7–2, UP+DOWN | **[TENTATIVE]** — same; prod implementation should require Polymarket CSV export or resolved proxy wallet before sizing |

**Blocker for Cemini replay:** resolve Gustafsson proxy wallet (X bio / Parity / user export) or treat K62 stats as design hypothesis only.

### Empirical kill shot on “predict direction” [TENTATIVE — author-reported]

On **330 trades**, true outcome from realized BTC move vs bet:

| Signal family | Direction accuracy |
|---------------|-------------------|
| Aggregate / “true outcome” | **49%** |
| Trend, momentum, order book, regime | ~50% each |
| Order-book wall (68:1) | Still wrong side |

Author conclusion: **the market is efficient on the direction question** he kept asking.

### New primary question

> Not *where is the price going* — **where is the price already**.

- Implemented as a **single branch before everything else**
- Legacy **three quadrants** treated as coin-flip — **no vote** in the new path
- **Dynamic threshold**: fixed distance wrong; margin scales with **tape speed** (quiet morning vs violent afternoon)

### Execution plumbing fixes (why “brain was right, trade didn’t happen”)

Removed four legacy guards built for the old strategy:

1. Entry-price cap  
2. Pocket guard  
3. Slippage check  
4. Dropped flag between stages  

**One line** added to carry state across the pipeline — wall came down.

### Day-one results [TENTATIVE — n=9]

| Metric | Value |
|--------|-------|
| Trades | 9 |
| Wins / losses | 7 / 2 |
| Direction mix | **First day trading both UP and DOWN** |
| Loss pattern | Both losses at **edge of window** — tuning, not structural (author) |

### Ops

- Whole feature behind **single ENV flag** (instant kill switch)
- **Manual schedule**: on weekdays/day session; **off overnight** when liquidity thins
- Author explicitly: **9 trades = signal, not victory**

### Cemini relevance

- Portable pattern for any **short-horizon PM market** where strike vs spot is observable: ask *already positioned?* before stacking directional models
- Reinforces @concepts/polymarket-bot-architecture.md lesson: **remove filters that made sense for the last strategy**
- Complements (does not replace) K57 blacklist — subtractive filters vs new alpha branch

## Snippets

> "330 trades, true outcome from the BTC move: 49 percent." [Source: @Gustafssonkotte.docx, 2026-05-24]

> "The old quadrants were the coin flip, they get no vote here." [Source: same]

> "The bot now sizes its own margin from the speed of the market." [Source: same]
