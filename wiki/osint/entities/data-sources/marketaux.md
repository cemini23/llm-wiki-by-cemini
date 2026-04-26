---
title: MarketAux
type: entity
tags: [data-source, news, sentiment, equities, alt-data]
keywords: [marketaux, news-api, stock-tagged, sentiment, ticker-news]
related:
  - entities/data-sources/finnhub.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @entities/data-sources/finnhub.md — companion / complement: Finnhub's news endpoints surface broad financial news; MarketAux differentiates by ticker-tagging at the article level + sentiment-by-default. Pair them for higher-recall ticker-event monitoring on the 30-symbol watchlist

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. The wiki currently has no dedicated news-aggregation source — research threads cite news inline via `[Source: ...]` URLs but don't have a programmatic feed. MarketAux fills that gap with a tickers-tagged-by-default API.

## Narrative

MarketAux is a financial-news aggregation API that tags every article
with the tickers it mentions and assigns sentiment scores per article
and per ticker. Coverage spans major financial wire services and a
long tail of business-news outlets.

**Why this is additive over Finnhub's news endpoints**:

- **Per-ticker monitoring** — MarketAux's `entities` parameter filters
  to articles mentioning a specific ticker symbol. Finnhub's news API
  is broader-by-default.
- **Sentiment as a first-class field** — every article carries a
  sentiment score (-1 to +1) per tagged entity. Useful as a feature
  for the LangGraph 4-analyst topology (Sentiment Analyst node).
- **Source diversity** — MarketAux pulls from 5,000+ outlets vs.
  Finnhub's smaller curated set.

**Cemini integration angle** (not yet wired):

1. Per-ticker monitoring loop — poll `entities=AAPL,GOOGL,...` every
   N minutes; deduplicate by `uuid`; route new articles into the
   per-ticker page's `## Snippets` block + the LangGraph sentiment
   analyst.
2. Macro-Weather regime gating — sudden sentiment shifts on macro
   tickers (XLF, IWM) feed the regime-gate decision alongside FRED
   prints and GDELT events.

**Authentication**: API key required. Free tier covers 100 req/day +
3 articles per request — workable for low-frequency per-ticker
monitoring but not high-frequency. Paid tiers start at $19/mo for
200 req/day with full article bodies.

**License**: news content licensed from publishers; commercial use
permitted under MarketAux terms. Verify per-article licensing if
republishing snippets externally.

## Snippets

- API root: https://www.marketaux.com/
- All news: `GET https://api.marketaux.com/v1/news/all?api_token=KEY&entities=AAPL`
- By ticker: `GET https://api.marketaux.com/v1/news/all?symbols=NVDA,AMD&filter_entities=true`
- Pricing: https://www.marketaux.com/pricing
