---
title: Pyth Terminal — public browse layer for Pyth price feeds
type: entity
tags: [entity, tool, oracle, market-data, pyth, k67]
keywords: [pyth-terminal, app-pyth-com, pyth-network, csv-export, metamorphicc, prediction-market-verification]
related:
  - sources/trading-posts-compilation-38-2026-05-26.md
  - entities/tools/chainlink-data-streams.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — K67 Post 28 review
- @entities/tools/chainlink-data-streams.md — alternate oracle path on Polymarket UpDown bots

## Raw Concept

**Pyth Terminal** (`app.pyth.com/explore`, launched 2026-05-19 per K67) — free UI to browse **3,000+** Pyth feeds (crypto, equities, FX, commodities), compare publishers/benchmarks, export **CSV** without API key. Gateway to **Pyth Pro** paid tiers ($500–$10k/mo cited [TENTATIVE]).

## Narrative

Community tester path: CSV + local analyzer (`github.com/metamorphicc/PythTerminalCSV`) as sanity check before Pro subscription. Positioned alongside Polymarket collaboration as **verification layer** for prediction traders.

**Phase-0 for Cemini:** confirm license/terms for prod redistribution of Pyth data; Terminal is evaluation UI not execution feed.

## Snippets

> "See the data before you pay for it. That's the whole pitch." [Source: Posts.docx K67 Post 28, @morpphhhaw]
