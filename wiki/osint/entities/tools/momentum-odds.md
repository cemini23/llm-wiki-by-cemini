---
title: MomentumOdds — sportsbook signal feed for prediction-market bots
type: entity
tags: [entity, tool, kalshi, sports-trading, signal-feed, webhook, k80]
keywords: [momentum-odds, momentumods, sportsbook-correlation, webhook-signals, n8n, chatgpt-vibe-code, kalshi-sports-bot]
related:
  - sources/youtube-kalshi-bots-batch-2026-05-29.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/gambling-wiki-federation.md
maturity: draft
created: 2026-05-29
updated: 2026-05-31
---

## Relations

- @sources/youtube-kalshi-bots-batch-2026-05-29.md — K80 Odds channel tutorial (`qPRY5ws3h60`)
- @concepts/sports-prediction-consensus-agent.md — architectural cousin (multi-source consensus → entry gate); MomentumOdds is a **commercial signal API** variant
- @concepts/polymarket-copy-trading-strategy.md — both are taker-side "follow external alpha" patterns
- @entities/platforms/kalshi.md — primary execution venue in tutorial
- @entities/platforms/polymarket.md — same signal stack may route to Polymarket sports books

## Raw Concept

Promoted in a May 2026 YouTube walkthrough as **momentumods.com** — subscription terminal delivering sports-betting **signals** (sportsbook correlation across 60+ books) with webhook/API docs for a locally hosted **Kalshi executor bot**. Creator workflow: paste API docs into ChatGPT → generate Python folder structure → fetch signals → risk checks → Kalshi order placement.

## Narrative

### Architecture (as described)

```
MomentumOdds API (signals, scores, sportsbook correlation)
        ↓ webhook / poll
Local signal engine (MacBook — filter, exposure, risk)
        ↓
Execution layer → Kalshi wallet (API keys in env vars)
```

Tutorial emphasizes **environment variables** for Kalshi/Telegram keys and a guided "vibe code" setup rather than open-source repo.

### Signal type highlighted

**Sportsbook correlation** — when 60+ sportsbooks align on a game direction, terminal surfaces actionable side; user maps to equivalent Kalshi NBA/playoff contract.

### Cemini evaluation [TENTATIVE]

| Dimension | Assessment |
|-----------|------------|
| **Overlap** | Partial overlap with @concepts/sports-prediction-consensus-agent.md (consensus-as-signal) but closed feed vs Firecrawl open scrape |
| **License / audit** | Commercial SaaS; no code adoption |
| **Edge durability** | **`[TENTATIVE 2026-05-29]`** — SMB pedagogy steal-from; prod sleeve gated on backtest/promotion checklist (internal gate). — line-divergence vs Kalshi may compress as books add PM/Kalshi hedging |
| **Verdict** | **Reference only** — useful as competitor surface for sports PM bots; not an Adopt candidate |

## Snippets

> "Go to momentumods.com … hit the open terminal button … we have a webhook … put this into ChatGPT and tell it to vibe code you a bot to run and hold your Kalshi wallet." [Source: https://www.youtube.com/watch?v=qPRY5ws3h60 (retrieved 2026-05-29)]
