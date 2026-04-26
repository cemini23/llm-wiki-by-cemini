---
title: Nasdaq Data Link (formerly Quandl)
type: entity
tags: [data-source, alt-data, market-data, fundamentals, macro]
keywords: [nasdaq-data-link, quandl, alt-data, datasets, marketplace, sharadar, zacks]
related:
  - entities/data-sources/finnhub.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @entities/data-sources/finnhub.md — companion / complement: Finnhub serves real-time + recent fundamentals via a single API; Nasdaq Data Link is a marketplace of curated historical datasets (Sharadar fundamentals, Zacks estimates, Wiki EOD legacy series, alt-data publishers)

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. Cemini's `market dataset/` corpus (1.6G of historical files) covers EOD prices but doesn't include curated fundamentals or alt-data; Nasdaq Data Link has been the institutional standard for that for ~15 years (originally as Quandl, acquired by Nasdaq in 2018).

## Narrative

Nasdaq Data Link is the marketplace formerly known as Quandl —
arguably the longest-running curated source of alt-data and historical
fundamentals datasets in quant. Both free and paid datasets are
exposed through the same REST API, with a unified query interface.

**Notable free datasets**:

- **FRED** mirror (we already have @entities/data-sources/fred.md
  natively, but the NDL wrapper provides a consistent interface
  across macro + market data).
- **Wiki EOD prices** (legacy free historical EOD; deprecated for new
  data but still useful as a 1990-2018 baseline).
- **Zacks Earnings Calendar** (free tier).
- Various central bank data series (BoE, ECB, BoJ).

**Notable paid datasets** (premium, $50-$500/mo each):

- **Sharadar Core US Fundamentals** — point-in-time fundamentals for
  every US-listed ticker; ~30 years history. Industry-standard for
  factor backtesting.
- **Zacks Equity Research** — sell-side estimates + revisions.
- **Continuous Futures** — adjusted continuous-contract series for
  every futures market.
- Various alt-data publishers (satellite imagery aggregations,
  consumer transaction panels, etc.).

**Cemini integration angle** (not yet wired):

1. Use the free FRED mirror as a fallback path when our direct FRED
   integration hits rate limits.
2. Evaluate the Sharadar trial dataset as a candidate for
   factor-backtesting infrastructure; the per-ticker reports could
   pull standardized fundamentals from there rather than re-deriving
   from EDGAR XBRL.
3. Monitor the alt-data marketplace for low-cost candidates that
   complement GDELT + Telethon + (eventual) MarketAux on the
   alt-data axis.

**Authentication**: free API key (sign up at data.nasdaq.com). Free
tier covers ~50 req/day on free datasets. Paid datasets carry their
own per-dataset subscription pricing.

**License**: per-dataset; varies widely. Free datasets are typically
CC-BY or public domain; paid datasets are commercial-use licensed
(important for IP-sale-readiness — verify per-dataset terms before
inheriting at acquisition).

## Snippets

- API root: https://docs.data.nasdaq.com/
- Time-series query: `GET https://data.nasdaq.com/api/v3/datasets/{db}/{ds}/data.json?api_key=KEY`
- Tables query (Sharadar etc.): `GET https://data.nasdaq.com/api/v3/datatables/{table}.json?api_key=KEY`
- Browse datasets: https://data.nasdaq.com/search
