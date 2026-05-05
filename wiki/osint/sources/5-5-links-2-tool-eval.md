---
title: "5_5 links 2 — Prediction Market and Algorithmic Trading Stack Components (32 tools)"
type: source
tags: [llm-agents, prediction-markets, kalshi, polymarket, algorithmic-trading, license-compliance, cemini-internal]
keywords: [tool-evaluation, gemini-deep-research, pykalshi, kalshi-llms-txt, kalshi-ai-trading-bot, prediction-market-analysis, polymarket-kalshi-arbitrage, polymarket-sports-analysis]
related:
  - sources/5-5-links-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/5-4-links-tool-eval.md
  - sources/links-2-5-4-tool-eval.md
  - concepts/cemini-license-posture.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/tools/pykalshi.md
  - entities/tools/kalshi-llms-txt.md
maturity: draft
read_status: deep-read
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-tool-eval.md, @sources/links-3-5-4-tool-eval.md, @sources/polymarket-5-5-tool-eval.md — companion 2026-05-05 / 2026-05-04 Gemini DR eval batches
- @entities/platforms/kalshi.md, @entities/platforms/polymarket.md — both venues directly affected by this batch's Adopts
- @entities/tools/pykalshi.md — Adopt-tier carry-forward; "the optima[l]" Kalshi client per eval, MIT
- @entities/tools/kalshi-llms-txt.md — Adopt-tier carry-forward; ingest llms.txt into wiki for LLM-readable Kalshi reference
- @concepts/cemini-license-posture.md — applied; no new patterns

## Raw Concept

- Original title: "Link Evaluation Brief: Prediction Market and Algorithmic Trading Stack Components" (Gemini Deep Research output)
- Author: Gemini Deep Research
- Type: docx — Cemini-internal architecture evaluation
- Location: cemini-librarian:/opt/cemini-bulk/research/5_5 links 2.docx
- Retrieved: 2026-05-05
- Length: ~84 KB, 32 candidates evaluated
- Read status: deep-read

## Narrative

Largest of the four 2026-05-05 Gemini DR batches at 32 evaluations. Prediction-market-heavy: Kalshi-specific tools, Polymarket clients, cross-venue arbitrage bots, sports-specific market analysis. Most operationally relevant of the four batches given Cemini's Kalshi-primary venue mix.

**Recommendation distribution:**

| Tier | Count | Highlight |
|------|-------|-----------|
| **Adopt** | 2 | URL 26 Kalshi API Documentation llms.txt (Proprietary ToS — Kalshi-published LLM-readable reference; ingest into wiki), URL 27 pykalshi (MIT — high-performance Kalshi client, replaces bloated official SDK) |
| **Steal-from** | 5 | URL 2 kalshi-ai-trading-bot (MIT), URL 4 Kalshi-Quant-TeleBot (MIT — microservices, Telegram-bot pattern), URL 6 prediction-market-analysis (MIT — historical-data Python framework), URL 8 Polymarket-Kalshi BTC Arbitrage Bot (MIT — first cross-doc duplicate signal w/ links-3-5-4 URL 17), URL 16 polymarket-sports-analysis (MIT — sports-prediction analytics) |
| **Defer** | 1 | License or maturity gating |
| **Reference-only** | 8 | Educational / docs / documentation-grade |
| **Reject** | 8 | License or stack mismatch |
| **Unavailable** | 7 | URL retrieval failed |
| **NoVerdict** | 1 | Eval inconclusive |

### Critical findings

#### 1. pykalshi — replace the official Kalshi SDK

> "An unofficial, high-performance Python client built from the ground up for the Kalshi API. It completely replaces the bloated official SDK." [Source: 5_5 links 2.docx URL 27]

Cemini's existing Kalshi integration uses the official Kalshi Python SDK (per `@entities/platforms/kalshi.md`). pykalshi is the Adopt-tier replacement. Direct integration target.

#### 2. Kalshi llms.txt — wiki-layer reference ingest

> "Official developer documentation for the Kalshi Exchange API." [Source: 5_5 links 2.docx URL 26]

Kalshi publishes an `llms.txt`-formatted version of their docs explicitly for LLM consumption. Adopt by ingesting into kb-server (or `wiki/concepts/kalshi-api-reference.md` synthesis page).

#### 3. Polymarket-Kalshi BTC Arbitrage Bot — cross-doc duplicate (signal)

This URL appears in **both** `5_5 links 2.docx` (URL 8) and `links 3 5_4.docx` (URL 17). Cross-doc duplicates are an explicit signal of high-relevance per the K8 + K9 ingest discipline (`@concepts/high-signal-paper-patterns.md`). Both evals reach Steal-from-tier verdict; runtime architecture is the load-bearing extract.

#### 4. prediction-market-analysis — historical data harness

> "Highly comprehensive Python framework designed to collect, index, and analyze massive amounts of historical data from prediction markets." [Source: 5_5 links 2.docx URL 6]

Direct extension to Cemini's existing market-dataset workflow. The historical-data analysis discipline is gettable via this MIT codebase; lift the indexing/aggregation patterns.

#### 5. polymarket-sports-analysis — direct prediction-market vertical

> "Highly structured Python-based data analytics suite tailored explicitly for tracking and analyzing sports prediction markets." [Source: 5_5 links 2.docx URL 16]

Per `@memory/prediction_market_scope`: Cemini's prediction-market scope explicitly covers sports. This is a direct in-domain Steal-from. Pairs with K28's Klaassen-Magnus Elo for tennis specifically.

### Architectural patterns worth extracting

- **pykalshi's high-performance client design** → wholesale adopt
- **Kalshi llms.txt** → ingest into wiki
- **Microservices + Telegram-bot pattern** (Kalshi-Quant-TeleBot) → operator-alert pattern (already covered by K28's probablyprofit kill-switch brief, but cross-validate)
- **Historical-data harness** (prediction-market-analysis) → lift indexing patterns
- **Cross-venue arbitrage scanner** (Polymarket-Kalshi BTC Arbitrage Bot) → reference architecture; Cemini's existing arbitrage logic should compare

## Snippets

- **pykalshi positioning** (URL 27): "An unofficial, high-performance Python client built from the ground up for the Kalshi API. It completely replaces the bloated official SDK." [Source: 5_5 links 2.docx URL 27]

- **Cross-doc duplicate** (URL 8 of 5_5 links 2 = URL 17 of links 3 5_4): "real-time arbitrage scanner specifically programmed to detect mathematically risk-free profit opportunities existing between the Polymarke[t] and Kalshi BTC markets." [Source: 5_5 links 2.docx URL 8]

- **prediction-market-analysis scope** (URL 6): "highly comprehensive Python framework designed to collect, index, and analyze massive amounts of historical data from prediction m[arkets]." [Source: 5_5 links 2.docx URL 6]

## Dead Ends

*(none yet — first ingest of this source.)*
