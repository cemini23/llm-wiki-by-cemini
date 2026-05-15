---
title: "A-Stock-Data Toolkit — Chinese Market Data Ingestion Pipeline"
type: entity
tags: [tool, market-data, china-a-shares, data-ingestion, financial-data, python]
keywords: [a-stock-data, simonlin1212, mootdx, akshare, chinese-market-data, northbound-flows, institutional-capital-tracking, apache-license, adopt]
related:
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - concepts/quant-finance.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @sources/multi-wiki-link-eval-v4-2026-05-15.md — evaluated in v4 link-eval (Adopt tier)
- @concepts/quant-finance.md — extends market data ingestion capabilities for Chinese equities
- @entities/platforms/polymarket.md — complementary data source for macro event positioning

## Raw Concept

Promoted from the v4 multi-wiki link evaluation (2026-05-15). Tier: **Adopt**. Primary fit: Cemini financial.

URL: https://github.com/simonlin1212/a-stock-data
License: Apache-2.0
Stars: 825 | Last commit: 2026-05-12 (3 days ago) | Open issues: 3
Stack: Python / Markdown / mootdx / akshare

## Narrative

A 6-layer architecture for Chinese A-share market data ingestion, tapping into mootdx via TCP 7709 (domestic broker data) and Tencent Finance via HTTP. Provides 21 distinct data endpoints including:

- **Minute-level Northbound fund flow tracking** — institutional capital flows between mainland China and Hong Kong (Stock Connect), a critical macro signal
- **Localized historical caching** — bypasses external API rate limits via local HDF5/flat-file caching
- **v2.1 F10 truncation** — token-optimized fundamental data summaries designed for LLM consumption
- **Embedded Python-in-Markdown SKILL.md** — the repository's documentation doubles as a deployable Claude Code skill file

The toolkit directly augments the /opt/cemini trading stack's market data ingestion layer. Key constraint: mootdx TCP 7709 connections require domestic Chinese IP — must be stress-tested from Cemini's primary network layer.

## Cross-wiki routing

- **@ccc-wiki** — stub documenting the embedded Python-in-Markdown SKILL.md formatting technique for tool documentation.
- **@osint-wiki** — entity page tracking institutional capital flow monitoring (Northbound flows as macro regime indicator).
