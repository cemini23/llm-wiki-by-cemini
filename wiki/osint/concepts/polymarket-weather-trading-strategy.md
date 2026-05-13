---
title: "Polymarket weather-trading strategy"
type: concept
tags: [concept, polymarket, weather-trading, prediction-markets, gamma-api, open-meteo, ensemble-forecasting, k41]
keywords: [polymarket-weather-bot, gamma-api-integration, weather-market-bins, open-meteo-bias-correction, station-coordinate-discovery, 3-model-ensemble, icon-gfs-ecmwf, 18-30-hr-entry-window]
related:
  - sources/x-docx-polymarket-claude-md-2026-04-23.md
  - sources/x2-docx-polymarket-theparuchh-2026.md
  - entities/people/alteregoeth.md
  - entities/people/theparuchh.md
  - entities/data-sources/open-meteo.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/macro-weather-regime.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/x-docx-polymarket-claude-md-2026-04-23.md — Section 1 by @AlterEgo_eth (Gamma API integration mechanics)
- @sources/x2-docx-polymarket-theparuchh-2026.md — full operational guide by @theparuchh
- @entities/people/alteregoeth.md — pseudonymous technical writer (Gamma API)
- @entities/people/theparuchh.md — pseudonymous bot operator (Mac Mini deployment)
- @concepts/polymarket-bot-architecture.md — general Polymarket bot architecture parent
- @concepts/polymarket-market-making-architectures.md — sibling concept (parlay/AMM)
- @concepts/ensemble-weather-forecasting.md — weather-side methodology
- @concepts/macro-weather-regime.md — temperature regime backdrop

## Raw Concept

What prompted this page: K41 ingest of two complementary sources documenting an end-to-end Polymarket weather-trading bot — @AlterEgo_eth's clean Gamma API technical breakdown + @theparuchh's full operational guide with debugging findings. Together they form a complete recipe; this concept page is the synthesized strategy.

## Narrative

### Market structure (per @AlterEgo_eth)

Polymarket "highest temperature in {city} on {date}" markets resolve to one of N temperature bins. Two API endpoints govern access:

1. `GET /events?slug=highest-temperature-in-{city}-on-{month}-{day}-{year}` — returns event metadata + array of child market IDs (one per bin)
2. `GET /markets/{id}` — per-bin pricing + orderbook

**Slug pattern**: lowercase hyphenated city (`new-york-city`, `los-angeles`, etc.) + ISO date words. Sentinel values `-999` (below-lowest-bin) and `999` (above-highest-bin) cap the distribution.

**Bin regex** for parsing market titles: `(\d+(?:\.\d+)?)°` patterns with above/below modifiers.

### Edge sources (per @theparuchh, V3 +45.9% ROI on $130 bankroll, 3-day window, anecdotal)

Five compounding edges documented:

1. **Station-coordinate fix**: 5 of 11 cities had wrong API coordinates (city-center geocode vs official weather-station coordinates the market resolves against). Single largest accuracy gain.
2. **Open-Meteo `bias_correction=true`**: under-documented API parameter; claimed +30-40% accuracy. [NEEDS VERIFICATION 2026-05-13]
3. **3-model ensemble**: ICON + GFS + ECMWF consensus with outlier rejection. Replaces single-model reliance.
4. **3-bin coverage**: bet adjacent bins (high-mid-low likelihood) instead of single bin. Win rate 18% → 30% claimed.
5. **18-30 hr entry window**: priced inefficiently relative to 6-12 hr window. Edge appears not yet priced in.

### Operational stack

- **Compute**: Mac Mini in bedroom, 24/7 (per @theparuchh)
- **Scan cadence**: every 10 minutes
- **Coverage**: 11 cities × 4 continents
- **Cost basis**: $130 starting bankroll (V3 reported)

### Cemini posture

- **Strategy is portable** to Cemini's prediction-market stack; weather is a clean adjacency to existing macro/sports market exposure
- **Phase-0 audit required** before adoption: verify Open-Meteo `bias_correction` claim independently, validate station coordinates for any deployed city, treat @theparuchh's P&L as anecdotal at small sample
- **Cross-concept hook**: ensemble methodology applies cleanly to @concepts/macro-weather-regime.md research; weather-trading bot output is a useful sentinel for broader regime detection
- **Reviewer-agent fit**: this strategy is a high-quality test case for @concepts/reviewer-agent-inference-time-feedback.md — entry decisions are concrete, falsifiable, and easily backtestable

### Open questions

- Is `bias_correction=true` documented in Open-Meteo's official API reference? (verifiable via @entities/data-sources/open-meteo.md before production use)
- What's the true sample size behind the 18% → 30% win-rate claim? (3 days × 11 cities × ~144 scans/day = high frequency but low independent-event count)
- Does the 18-30 hr edge persist after publication, or does the X post itself close the gap?
