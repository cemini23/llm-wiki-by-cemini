---
title: SEC EDGAR Data API
type: entity
tags: [data-source, equities, fundamentals, regulatory-primary-source, government]
keywords: [sec, edgar, 10-K, 10-Q, 8-K, S-1, XBRL, companyfacts, submissions]
related:
  - entities/ticker-watchlist.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @entities/ticker-watchlist.md — primary use case: every US-domiciled ticker on the 30-symbol watchlist has an SEC CIK; EDGAR is the canonical source for 10-K / 10-Q / 8-K / S-1 / DEF 14A filings cited in per-ticker reports

## Raw Concept

Added 2026-04-25 from a librarian-hygiene pass against the [public-apis](https://github.com/public-apis/public-apis) curated list. Not yet wired into the Cemini stack — entry created so future per-ticker research can cite EDGAR as the canonical primary source rather than paraphrasing from secondary aggregators.

## Narrative

The SEC EDGAR REST API exposes every filing made by every US-domiciled
public company since the system's inception. Three high-value endpoints
for systematic use:

1. **Submissions by CIK** — `data.sec.gov/submissions/CIK##########.json`
   returns the full filing history for an issuer (form types, accession
   numbers, filing dates, primary documents). Ideal for monitoring
   8-K material-event filings on the 30-ticker watchlist.
2. **Company facts (XBRL)** — `data.sec.gov/api/xbrl/companyfacts/
   CIK##########.json` returns standardized US-GAAP and IFRS line items
   pulled from filed financial statements. Skips the parse-the-PDF
   step that secondary providers charge for.
3. **Full-text search** — `efts.sec.gov/LATEST/search-index?q=...` over
   the full filing corpus.

**Authentication**: none. SEC mandates a `User-Agent` header
identifying the requester (org name + contact email) per
[fair-use guidance](https://www.sec.gov/os/accessing-edgar-data); rate
limit is 10 req/sec.

**License**: filings are works of the US Government, public domain. No
commercial restriction — clean for IP-sale-readiness inheritance.

**Why this beats what we have**: Finnhub's free tier paraphrases EDGAR
fundamentals via opaque normalization; Polygon doesn't carry 10-K
texts; yfinance returns Yahoo's edited summaries, not source documents.
For acquirer-narrative work and per-ticker forensic reads, only the
primary source counts.

## Snippets

- API root: https://www.sec.gov/edgar/sec-api-documentation
- Submissions: `https://data.sec.gov/submissions/CIK0000320193.json` (AAPL example)
- Company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json`
- Fair-use guidance: https://www.sec.gov/os/accessing-edgar-data
