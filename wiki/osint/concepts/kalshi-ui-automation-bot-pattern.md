---
title: Kalshi UI automation bot pattern — Night Shark OCR on 15-min crypto markets
type: concept
tags: [concept, kalshi, trading-bot, ui-automation, ocr, retail-promo, k80]
keywords: [night-shark, processoverprofit, screen-scraping, kalshi-crypto-15min, trigger-price, time-gate, retry-fill, anti-pattern]
related:
  - sources/youtube-kalshi-bots-batch-2026-05-29.md
  - concepts/kalshi-api-reference.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/polymarket-updown-15min-execution-latency.md
  - entities/tools/pykalshi.md
  - entities/platforms/kalshi.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
clusters: [kalshi, trading-bot, retail-promo]
---

## Relations

- @sources/youtube-kalshi-bots-batch-2026-05-29.md — K80 ProcessOverProfit videos 1 + 6
- @concepts/kalshi-api-reference.md — **preferred** Cemini integration path (REST/WebSocket via pykalshi)
- @concepts/polymarket-updown-bot-taxonomy.md — same market class (15-min crypto up/down) on Polymarket; taxonomy applies to Kalshi crypto books by analogy
- @concepts/polymarket-updown-15min-execution-latency.md — latency + fill-retry lessons transfer to any click-path bot
- @entities/tools/pykalshi.md — official API client Cemini adopted (K30)
- @entities/platforms/kalshi.md — venue

## Raw Concept

K80 YouTube ingest of ProcessOverProfit's "Kalshi bot in 10 minutes" series (v2 + v3). Documents a **retail UI-automation stack** (Night Shark browser extension + screen-region OCR + synthetic clicks) targeting Kalshi **15-minute crypto** markets — not the Kalshi Trade API.

## Narrative

### Stack architecture

```
Kalshi web UI (15-min BTC/ETH)
    ↑ OCR read (price, time remaining)
Night Shark scripts (HUD + trading bot)
    ↑ synthetic click (Buy Up / Buy Down / Sell)
Browser DOM regions mapped by user-drawn rectangles
```

Optional v3 additions: KuCoin API keys stored locally (for spot reference / hedge — exact coupling unclear from transcript); Git dependency install for OCR accuracy.

### Strategy parameters (v2/v3)

| Parameter | Meaning |
|-----------|---------|
| **Trigger price** (e.g. 70–90¢) | Enter whichever side first reaches deep ITM probability |
| **Exit / reversal price** (e.g. 40¢) | Stop if price mean-reverts |
| **Trigger minute** (e.g. 5–12 min remaining) | Bot only active in late session — "high probability farmer" |
| **Order size** | Dollar amount (v2) or contract count (v3) |
| **Retries** | Up to ~3 click attempts if fill fails |

The edge claim is **late-session momentum / sticky probability** on binary crypto strikes — structurally similar to Type-3/5 microstructure bots in @concepts/polymarket-updown-bot-taxonomy.md, but implemented without order-book access.

### Failure modes [TENTATIVE — single creator]

- **Price jumps** between OCR read and click (demo: 71¢ → 92¢ fill).
- **OCR dependency** — requires flickering digit overlay; breaks on UI redesign.
- **No slippage preview** — unlike API bots (@sources/youtube-kalshi-bots-batch-2026-05-29 video 3).
- **Terms-of-service / automation policy** — `[CONFIRMED 2026-05-29]` Kalshi Data Terms prohibit scraping, bulk harvesting, non-standard browsers, scripts, and automated website navigation [Source: https://kalshi-public-docs.s3.amazonaws.com/kalshi-data-terms-of-service.pdf]. UI OCR bots (Night Shark pattern) are **high ToS risk**. **API-based automation is the supported path** — Kalshi documents REST/WebSocket for programmatic trading [Sources: Kalshi API docs, third-party guides citing official API access (retrieved 2026-05-29)].

### Cemini posture: **NO-GO for production**

Cemini already routes Kalshi through **pykalshi + WebSocket** (@entities/tools/pykalshi.md). Adopting Night Shark OCR would reintroduce brittle latency, no audit trail, and venue-policy risk. **Steal-from only:** late-session time gate + reversal exit as *strategy knobs* testable via API backtest on Kalshi crypto series.

## Snippets

> "The Night Shark is reading the areas. If you don't get it … install this dependency … restart the Night Shark, then you should be able to see those numbers flickering." [Source: https://www.youtube.com/watch?v=m9dD0XlpFF0 (retrieved 2026-05-29)]

> "We entered … it jumped from 71 to 90. So that was … weird behavior on the Kalshi part … actual fill price is 90." [Source: https://www.youtube.com/watch?v=Y8tcbq1hS5o (retrieved 2026-05-29)]
