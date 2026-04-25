---
title: yfinance (equity EOD fallback)
type: entity
tags: [infrastructure, data-library, fallback-source, equities, python]
keywords: [yfinance, yahoo-finance, eod, 1-min-bars, backfill, fallback]
related:
  - entities/platforms/polygon.md
  - entities/ticker-watchlist.md
  - concepts/equity-intraday-backfill-gap.md
maturity: validated
created: 2026-04-24
updated: 2026-04-24
---

## Relations

- @entities/platforms/polygon.md — the primary equity feed yfinance falls back for
- @entities/ticker-watchlist.md — per-ticker equity completeness depends on this fallback when Polygon refuses
- @concepts/equity-intraday-backfill-gap.md — the doctrine that invokes yfinance after 16:01 ET

## Raw Concept

Stub page. `yfinance` is the Python library for Yahoo Finance EOD data. Added to the Cemini stack 2026-04-24 as the **equity-session EOD fallback** when Polygon returns `NOT_AUTHORIZED` on same-day intraday requests. Consumers: `scripts/backfill_yfinance.py` (one-shot point-fix) and `polygon_ingestor.py` (EOD-sweep doctrine fix). Added to `Dockerfile` in the same 2026-04-24 commit pair.

## Narrative

*Expand as more is learned. Known as of 2026-04-24:*

- **Role in stack**: equity-only fallback for the same-day intraday window the Polygon plan refuses. 1-minute bar granularity; 390 bars per full session per symbol.
- **Consumers in code**:
  - `scripts/backfill_yfinance.py` — one-shot backfill script (ran 2026-04-24 for 13,258-bar recovery).
  - `polygon_ingestor.py` — post-close EOD sweep (fires after 16:01 ET if Polygon session is missing).
- **Not used for**: crypto (Coinbase handles that directly), same-day tick-level granularity (yfinance is bar-level), real-time streaming (EOD sweep only).
- **No auth / rate-limit known issues yet**; public Yahoo endpoint. If rate-limiting surfaces, upgrade path TBD.

## Snippets

*(populate when specific rate-limit numbers, error surfaces, or gotchas are worth inlining.)*
