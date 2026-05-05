---
title: FinanceDatabase — Offline 300k+ Financial Symbol Catalog (MIT)
type: entity
tags: [tool, financial-research, watchlist-expansion, mit, adopt-tier, offline-catalog]
keywords: [financedatabase, jerbouma, financial-symbols, offline-catalog, ticker-discovery, universe-expansion]
related:
  - sources/5-5-links-tool-eval.md
  - entities/tools/financetoolkit.md
  - entities/ticker-watchlist.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 18, **Adopt** tier
- @entities/tools/financetoolkit.md — companion library by same author (JerBouma); FinanceToolkit provides 150 metrics, FinanceDatabase provides the symbol-universe catalog. Together they form a complete fundamental-analysis toolkit.
- @entities/ticker-watchlist.md — Cemini's existing watchlist tracker; FinanceDatabase enables universe-expansion beyond the current curated list

## Raw Concept

Offline catalog of 300,000+ global financial symbols (equities, ETFs, indices, currencies, crypto, etc.) queryable via a Python library. MIT-licensed. Adopt-tier verdict in K30 5_5-links batch.

## Narrative

- **URL**: github.com/JerBouma/FinanceDatabase (per K30 eval URL 18)
- **License**: MIT
- **Stack**: Python; **completely offline** (no API dependency)
- **Scope**: 300,000+ symbols globally

### Why Adopt for Cemini

Cemini's existing `entities/ticker-watchlist.md` is a curated list (low hundreds of tickers). For:
- **Screening**: filter the 300k universe by sector / region / market-cap / dividend-yield / etc. to discover new tickers
- **Sanity-checking**: confirm a ticker symbol resolves to a real instrument before trading
- **Cross-reference**: enrich watchlist entries with sector / industry / country / currency metadata
- **Universe-expansion**: prediction-market contracts often reference companies outside the watchlist; FinanceDatabase lets the brain look up arbitrary mentioned tickers

The offline-catalog property is critical: no API rate limits, no network failures, no per-call cost. A monthly `pip install --upgrade financedatabase` keeps it current.

### Integration

Cemini-side use cases:

1. **Pre-trade ticker validation** — before placing an order, verify the symbol exists in FinanceDatabase
2. **Watchlist enrichment** — extend `entities/ticker-watchlist.md` rows with sector / industry / currency from FinanceDatabase
3. **FastMCP tool** — expose a `lookup_ticker_metadata(symbol)` tool that the brain can call
4. **Conductor taxonomy enrichment** — add a `ticker_lookup` taxonomy class that routes to a tiny model + this tool (very cheap path for symbol-resolution queries)

### Pairing with FinanceToolkit (K28)

Both libraries are by JerBouma, both MIT, both pure-Python:
- **FinanceDatabase** = "what symbols exist, and what are they?"
- **FinanceToolkit** = "given a symbol, calculate 150 metrics on it"

Together: brain says "tell me about NVDA" → FinanceDatabase returns sector/industry metadata → FinanceToolkit calculates Extended DuPont + GARCH volatility → brain has a complete fundamental picture.

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Disk footprint of the offline catalog (likely small — text data only)
- Update cadence (how often does the upstream package refresh?)
- Coverage gaps (does it have all Cemini's existing watchlist entries? Including crypto + options + futures?)
- Container build-time impact (small, but verify with FinanceToolkit's known scipy/scikit/statsmodels footprint)

### Adoption status

**Brief addendum staged 2026-05-05**: FinanceDatabase folded into the existing K28 quant-libs brief (`@briefs/2026-05-04_quant-libs-fastmcp-integration.md`) rather than a standalone brief. Title updated to "Riskfolio-Lib + FinanceToolkit + FinanceDatabase — FastMCP Integration". New section "FinanceDatabase FastMCP wrapper" defines 3 tools (`lookup_ticker_metadata`, `screen_universe`, `search_symbols`); offline catalog → no data-source guardrail needed (unlike FinanceToolkit's Yahoo-Finance default). Pairs symmetrically with FinanceToolkit (same author JerBouma): FinanceDatabase = "what symbols exist, and what are they?", FinanceToolkit = "given a symbol, calculate 150 metrics on it." Brief at `cemini-prod:/opt/cemini/briefs/2026-05-04_quant-libs-fastmcp-integration.md` (re-scp'd 2026-05-05).

## Snippets

- **Scope framing** (K30 eval): "exhaustive, completely offline catalog of over 300,000 global financial symbols organized and queried via a Python library." [Source: 5_5 links.docx URL 18]

- **Recommendation tier**: "Adopt. The tool should be [installed into the FastMCP layer]." [Source: 5_5 links.docx URL 18]
