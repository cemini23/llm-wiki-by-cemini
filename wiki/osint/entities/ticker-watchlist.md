---
title: CeminiSuite Ticker Watchlist
type: entity
tags: [reference, ticker, watchlist, cemini-suite, harvester-config]
keywords: [watchlist, tickers, equities, crypto, polygon, harvester, sp500]
related:
  - entities/tickers/aapl.md
  - entities/tickers/ada.md
  - entities/tickers/amd.md
  - entities/tickers/amzn.md
  - entities/tickers/asts.md
  - entities/tickers/avax.md
  - entities/tickers/avgo.md
  - entities/tickers/btc.md
  - entities/tickers/coin.md
  - entities/tickers/dis.md
  - entities/tickers/doge.md
  - entities/tickers/eth.md
  - entities/tickers/glw.md
  - entities/tickers/googl.md
  - entities/tickers/intc.md
  - entities/tickers/link.md
  - entities/tickers/meta.md
  - entities/tickers/msft.md
  - entities/tickers/mstr.md
  - entities/tickers/nflx.md
  - entities/tickers/nvda.md
  - entities/tickers/pl.md
  - entities/tickers/pltr.md
  - entities/tickers/smci.md
  - entities/tickers/sofi.md
  - entities/tickers/sol.md
  - entities/tickers/tsla.md
  - entities/platforms/polygon.md
  - entities/infrastructure/yfinance.md
  - concepts/equity-intraday-backfill-gap.md
  - concepts/crypto-asset-taxonomy.md
  - concepts/oracle-networks.md
maturity: core
created: 2026-04-23
updated: 2026-04-25
---

## Relations

Per-ticker entity pages (reports committed as of 2026-04-25):
- @entities/tickers/aapl.md — AAPL
- @entities/tickers/ada.md — ADA (added 2026-04-25)
- @entities/tickers/amd.md — AMD
- @entities/tickers/amzn.md — AMZN
- @entities/tickers/asts.md — ASTS (added 2026-04-24)
- @entities/tickers/avax.md — AVAX (added 2026-04-25)
- @entities/tickers/avgo.md — AVGO
- @entities/tickers/btc.md — BTC
- @entities/tickers/coin.md — COIN
- @entities/tickers/dis.md — DIS
- @entities/tickers/doge.md — DOGE (added 2026-04-24)
- @entities/tickers/eth.md — ETH
- @entities/tickers/glw.md — GLW (added 2026-04-24)
- @entities/tickers/googl.md — GOOGL
- @entities/tickers/intc.md — INTC (added 2026-04-24)
- @entities/tickers/link.md — LINK (added 2026-04-25)
- @entities/tickers/meta.md — META
- @entities/tickers/msft.md — MSFT
- @entities/tickers/mstr.md — MSTR
- @entities/tickers/nflx.md — NFLX
- @entities/tickers/nvda.md — NVDA
- @entities/tickers/pl.md — PL (added 2026-04-24)
- @entities/tickers/pltr.md — PLTR
- @entities/tickers/smci.md — SMCI
- @entities/tickers/sofi.md — SOFI (added 2026-04-24)
- @entities/tickers/sol.md — SOL (added 2026-04-24)
- @entities/tickers/tsla.md — TSLA

Cross-cutting concept pages organizing the watchlist:
- @concepts/crypto-asset-taxonomy.md — functional taxonomy of the 7 crypto-native assets (4 categories: store-of-value, programmable L1, memecoin/payments PoW, oracle middleware)
- @concepts/oracle-networks.md — deeper treatment of the oracle/middleware category (LINK is the canonical implementation)
- @concepts/equity-intraday-backfill-gap.md — equity intraday data-completeness caveat across all equity tickers (Polygon → yfinance EOD self-heal)

## Raw Concept

- **Source of truth**: `/opt/cemini/QuantOS/config/tickers.json` on the Hetzner server
- **Loaded by**: `QuantOS/core/tickers.py::load_watchlist()` at runtime
- **Pulled**: 2026-04-23
- **Consumers**: All CeminiSuite harvesters (Polygon equity ticks, Polygon crypto ticks, opportunity screener, etc.)

This list is read-only from this workspace. Updates happen on the server; re-pull the JSON when the canonical list changes.

## Narrative

The CeminiSuite dev stack baseline tracks **30 symbols** per the server's `tickers.json` snapshot below. As of 2026-04-24 this workspace rebalances the universe with an even **+5 / −5 swap**: **added** ASTS, GLW, INTC, PL, SOFI; **removed** MARA, JPM, BAC, GS, UBER. Net change is zero — wiki-tracked universe remains at **30 symbols** (23 equities + 7 crypto native), but category composition shifts: Financials sunset, Mega cap 6 → 7 (INTC), Crypto proxies 3 → 2 (MARA out), Consumer tech 3 → 2 (UBER out), plus new categories Space tech (ASTS, PL), Industrials (GLW), Fintech (SOFI). Server-side `tickers.json` edit is in progress in parallel; apply the combined diff below, then re-pull to restore parity.

### Totals
- **23 equities** — 3 indices + 7 mega cap (incl. INTC) + 5 high beta + 2 crypto proxies + 2 consumer tech + 2 space tech + 1 industrials + 1 fintech
- **7 crypto native**
- Financials category sunset as of 2026-04-24.

### Categories

| Category | Count | Symbols |
|---|---|---|
| Indices | 3 | SPY, QQQ, IWM |
| Mega cap | 7 | AAPL, MSFT, NVDA, AMZN, META, GOOGL, INTC |
| High beta | 5 | TSLA, AMD, SMCI, PLTR, AVGO |
| Crypto proxies | 2 | COIN, MSTR |
| Consumer tech | 2 | DIS, NFLX |
| Space tech | 2 | ASTS, PL |
| Industrials | 1 | GLW |
| Fintech | 1 | SOFI |
| Crypto native | 7 | BTC, ETH, SOL, DOGE, ADA, AVAX, LINK |

### Report status (Gemini Deep Research template)

Per-ticker equity research reports are being commissioned via the Gemini Deep Research prompt (stored elsewhere; not in this workspace). Report format: six sections — Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context. Indexed reports live at `wiki/entities/tickers/<symbol>.md`.

| Category | Symbol | Report |
|---|---|---|
| Indices | SPY | _pending_ |
| Indices | QQQ | _pending_ |
| Indices | IWM | _pending_ |
| Mega cap | AAPL | ✅ [aapl.md](tickers/aapl.md) (2026-04-23) |
| Mega cap | MSFT | ✅ [msft.md](tickers/msft.md) (2026-04-23) |
| Mega cap | NVDA | ✅ [nvda.md](tickers/nvda.md) (2026-04-23) |
| Mega cap | AMZN | ✅ [amzn.md](tickers/amzn.md) (2026-04-23) |
| Mega cap | META | ✅ [meta.md](tickers/meta.md) (2026-04-23) |
| Mega cap | GOOGL | ✅ [googl.md](tickers/googl.md) (2026-04-23) |
| High beta | TSLA | ✅ [tsla.md](tickers/tsla.md) (2026-04-23) |
| High beta | AMD | ✅ [amd.md](tickers/amd.md) (2026-04-23) |
| High beta | SMCI | ✅ [smci.md](tickers/smci.md) (2026-04-23) |
| High beta | PLTR | ✅ [pltr.md](tickers/pltr.md) (2026-04-23) |
| High beta | AVGO | ✅ [avgo.md](tickers/avgo.md) (2026-04-23) |
| Crypto proxies | COIN | ✅ [coin.md](tickers/coin.md) (2026-04-24) |
| Crypto proxies | MSTR | ✅ [mstr.md](tickers/mstr.md) (2026-04-24) |
| Consumer tech | DIS | ✅ [dis.md](tickers/dis.md) (2026-04-24) |
| Consumer tech | NFLX | ✅ [nflx.md](tickers/nflx.md) (2026-04-24) |
| Crypto native | BTC | ✅ [btc.md](tickers/btc.md) (2026-04-23) |
| Crypto native | ETH | ✅ [eth.md](tickers/eth.md) (2026-04-24) |
| Crypto native | SOL | ✅ [sol.md](tickers/sol.md) (2026-04-24) |
| Crypto native | DOGE | ✅ [doge.md](tickers/doge.md) (2026-04-24) |
| Crypto native | ADA | ✅ [ada.md](tickers/ada.md) (2026-04-25) |
| Crypto native | AVAX | ✅ [avax.md](tickers/avax.md) (2026-04-25) |
| Crypto native | LINK | ✅ [link.md](tickers/link.md) (2026-04-25) |
| Space tech | ASTS | ✅ [asts.md](tickers/asts.md) (2026-04-24) |
| Space tech | PL | ✅ [pl.md](tickers/pl.md) (2026-04-24) |
| Industrials | GLW | ✅ [glw.md](tickers/glw.md) (2026-04-24) |
| Mega cap | INTC | ✅ [intc.md](tickers/intc.md) (2026-04-24) |
| Fintech | SOFI | ✅ [sofi.md](tickers/sofi.md) (2026-04-24) |

**Progress**: 27 / 30 indexed (2026-04-25 ingest: ADA, AVAX, LINK added — completes the 7-coin crypto-native bench. Filename convention reminder: `<TICKER> <date>.docx`, not company-name or leading-underscore/parens forms; the regex in `scripts/index_tickers.py` expects a leading uppercase token. ADA dropped as `_(ADA)3_24.docx`, renamed in-place before re-running. Remaining pending: SPY, QQQ, IWM — the three index ETFs). 2026-04-24 watchlist rebalance (even +5 / −5 swap, size preserved at 30): **added** ASTS, GLW, INTC, PL, SOFI; **removed** MARA, JPM, BAC, GS, UBER (UBER's entity page deleted; source docx `UBER 3_24.docx` retained in `research for cemini/` as historical record). Drop new reports into `research to be indexed/` as `<SYMBOL> <date>.docx`, then ask Claude to index them. The ingest workflow: extract docx → create `wiki/entities/tickers/<symbol>.md` → flip this table's row → move source docx into `research for cemini/`.

### Notes

- `sp500_tickers.json` on the server is a broader reference list, **not** the active watchlist.
- Fallback list in `tickers.py` if the JSON load fails: SPY, QQQ, AAPL, NVDA, TSLA, BTC-USD. Only relevant if the config can't be read.
- **Equity intraday data-completeness caveat** (2026-04-24): Polygon plan-tier returns `NOT_AUTHORIZED` on same-day equity intraday requests. `polygon_ingestor.py` self-heals via a yfinance EOD sweep after 16:01 ET — see @concepts/equity-intraday-backfill-gap.md for the doctrine + 2026-04-24 incident record. Per-ticker intraday tick-level precision for the current day is unavailable until the plan upgrades; 1-min bars land by market-close + 1 minute. Crypto (Coinbase) path is unaffected.

## Snippets

### Raw config (live server state, 2026-04-24 post-rebalance)

```json
{
  "active_tickers": [
    "SPY", "QQQ", "IWM",
    "AAPL", "MSFT", "NVDA", "AMZN", "META", "GOOGL",
    "TSLA", "AMD", "SMCI", "PLTR", "AVGO",
    "COIN", "MSTR",
    "DIS", "NFLX",
    "INTC", "GLW", "PL", "ASTS", "SOFI",
    "BTC", "ETH", "SOL", "DOGE", "ADA", "AVAX", "LINK"
  ],
  "categories": {
    "indices": ["SPY", "QQQ", "IWM"],
    "mega_cap": ["AAPL", "MSFT", "NVDA", "AMZN", "META", "GOOGL"],
    "high_beta": ["TSLA", "AMD", "SMCI", "PLTR", "AVGO"],
    "crypto_proxies": ["COIN", "MSTR"],
    "consumer_tech": ["DIS", "NFLX"],
    "frontier": ["INTC", "GLW", "PL", "ASTS", "SOFI"],
    "crypto_native": ["BTC", "ETH", "SOL", "DOGE", "ADA", "AVAX", "LINK"]
  }
}
```

### Wiki-tracked divergence from server config — RESOLVED 2026-04-24

**Status**: ✅ closed. Server-side `tickers.json` was edited 2026-04-24 to apply the +5 / −5 swap. Re-pulled live below; both sides carry the same 30-symbol active list.

**Categorization variance (preserved as-is, not a bug)**: workspace split the 5 new tickers across mega_cap (INTC) + space_tech (ASTS, PL) + industrials (GLW) + fintech (SOFI); server collapsed all 5 into a single `frontier` category. Both encodings agree on the active-ticker set; they only differ in how the new additions are bucketed for downstream category-aware logic. Workspace's split is the human-readable taxonomy for librarian use; server's `frontier` is the operational tag for the harvester / strategy code paths. Not reconciling — different audiences, different optimal granularity.

#### Original 2026-04-24 diff (kept as record-of-action)

```json
{
  "add_to_active_tickers": ["ASTS", "GLW", "INTC", "PL", "SOFI"],
  "remove_from_active_tickers": ["MARA", "JPM", "BAC", "GS", "UBER"],
  "add_categories_workspace_view": {
    "mega_cap": ["INTC"],
    "space_tech": ["ASTS", "PL"],
    "industrials": ["GLW"],
    "fintech": ["SOFI"]
  },
  "add_categories_server_view": {
    "frontier": ["INTC", "GLW", "PL", "ASTS", "SOFI"]
  },
  "remove_from_categories": {
    "crypto_proxies": ["MARA"],
    "financials": ["JPM", "BAC", "GS"],
    "consumer_tech": ["UBER"]
  },
  "sunset_categories": ["financials"]
}
```

Rationale:
- `financials` sunset: JPM/BAC/GS were placeholders; no research was commissioned and the legacy-bank focus doesn't align with current Cemini strategy priorities (event-driven, macro-weather, crypto-proxy).
- SOFI added (workspace `fintech`, server `frontier`): replaces the Financials slot with a digital-native neobank/lending platform — keeps exposure to rates-sensitive credit dynamics without the legacy-bank overhang. If `fintech` ever needs to expand, candidates are ABNB, HOOD, AFRM.
- MARA removed: redundant with COIN + MSTR for crypto-proxy coverage.
- UBER removed: single-report coverage deemed insufficient signal-to-noise for consumer-tech category; DIS + NFLX retained as core consumer-tech reference set.
