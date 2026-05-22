---
title: "Polymarket weather-trading strategy"
type: concept
tags: [concept, polymarket, weather-trading, prediction-markets, gamma-api, open-meteo, ensemble-forecasting, k41]
keywords: [polymarket-weather-bot, gamma-api-integration, weather-market-bins, open-meteo-bias-correction, station-coordinate-discovery, 3-model-ensemble, icon-gfs-ecmwf, 18-30-hr-entry-window]
related:
  - sources/x-docx-polymarket-claude-md-2026-04-23.md
  - sources/x2-docx-polymarket-theparuchh-2026.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - entities/people/alteregoeth.md
  - entities/people/theparuchh.md
  - entities/data-sources/open-meteo.md
  - entities/tools/hermes-agent.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/macro-weather-regime.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - entities/people/polymarketsuccubus.md
  - entities/tools/clawdbot.md
  - entities/tools/parity-polymarket-analytics.md
  - concepts/cme-settlement-mechanics-for-prediction-markets.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - entities/people/polydao-mr-buzzoni.md
maturity: draft
created: 2026-05-13
updated: 2026-05-22
---

## Relations

- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — K57 @polydao forecast-revision workflow
- @entities/people/polydao-mr-buzzoni.md — K57 author
- @sources/x-docx-polymarket-claude-md-2026-04-23.md — Section 1 by @AlterEgo_eth (Gamma API integration mechanics)
- @sources/x2-docx-polymarket-theparuchh-2026.md — full operational guide by @theparuchh
- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — K52 Post 5 (@0xMovez): a Hermes-Agent deployment path for the @AlterEgo_eth weatherbot
- @entities/people/alteregoeth.md — pseudonymous technical writer (Gamma API); author of the `weatherbot` repo Post 5 deploys
- @entities/people/theparuchh.md — pseudonymous bot operator (Mac Mini deployment)
- @entities/tools/hermes-agent.md — the Nous Research agent runtime used in the Post 5 deployment path
- @concepts/polymarket-bot-architecture.md — general Polymarket bot architecture parent
- @concepts/polymarket-market-making-architectures.md — sibling concept (parlay/AMM)
- @concepts/ensemble-weather-forecasting.md — weather-side methodology
- @concepts/macro-weather-regime.md — temperature regime backdrop
- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Post 5 (@polysuccubus) — Top-7 most-profitable Polymarket weather traders ranking; 7 independent operator profiles confirming the strategy
- @entities/people/polymarketsuccubus.md — author of the K55 Top-7 ranking
- @entities/tools/clawdbot.md — Claude-powered AI agent framework behind #1-ranked ColdMath (PnL +$124K)
- @entities/tools/parity-polymarket-analytics.md — analytics platform fronting the K55 Top-7 trader profiles

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

### Hermes-Agent deployment path (per @0xMovez, K52)

A third source — @0xMovez's K52 X post — documents a *deployment* recipe rather than new strategy edge. It runs a Polymarket weather bot on **@entities/tools/hermes-agent.md** (Nous Research's self-hosted agent) and explicitly reuses **@AlterEgo_eth's `weatherbot`** repo (`github.com/alteregoeth-ai/weatherbot.git`, a `py-clob-client` stack) as the trading logic — corroborating that @AlterEgo_eth's weather work shipped as runnable open source, not just an X thread.

The recipe is 7 natural-language prompts to the agent, no hand-coding:

1. **Clone + venv** — clone `weatherbot`, create a Python 3.12 venv, install `py-clob-client python-dotenv requests web3`.
2. **Generate wallet** — agent creates a fresh Polygon wallet via `eth_account`, writes `PK` / `WALLET` / `SIG_TYPE=0` to `weatherbot/.env`.
3. **Fund** (operator action) — send USDC.e (trading capital, \$10 min / \$50 recommended) + ~2 POL gas to the wallet.
4. **Approve contracts** — ERC-20 `approve` (max-uint) USDC.e for the 3 Polymarket spenders — CTF Exchange `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`, Neg-Risk Exchange `0xC5d563A36AE78145C45a50134d48A1215220f80a`, Router `0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296` — plus `setApprovalForAll` on the Conditional Tokens contract `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`. (USDC.e on Polygon = `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`, chain id 137.)
5. **Configure** — wire a **Visual Crossing** weather API key into `config.json`; set `balance`, `max_bet` (start \$2), `min_ev: 0.10` (10%+ edge), `mode: paper` then `live`.
6. **Test scan** — `python3 bot_v3.py scan` in paper mode first.
7. **Go live** — run continuous mode, scans every 60 min, self-learning on trades, Telegram reports.

This bot uses **Expected Value + Kelly Criterion** position sizing across ~20 cities / 4 continents with 3 forecast sources — the same EV/ensemble shape as the @theparuchh V3 strategy above. It is a *packaging* contribution: the edge sources are unchanged; what is new is a copy-paste, agent-driven install. The four Polymarket Polygon contract addresses are genuine and reusable for any Cemini Polymarket on-chain approval step.

**Caveat.** Handing a self-hosted agent a funded wallet's private key and running unattended live trading via pasted prompts is a high-trust setup; the PnL figures cited alongside it (`ColdMath $300→$219K`, `Sharky6999 99.3% WR`, `RN1 $1.2K→$7.3M`) are `[TENTATIVE]` creator marketing.

### Forecast-revision workflow (K57, @polydao) [TENTATIVE]

Independent promoter narrative reinforcing resolution discipline:

- **Edge question:** not "what will weather be?" but "where is Polymarket price stale vs latest forecast revision?"
- **Data:** hourly Open-Meteo snapshots + `detect_changes()` on **future hours only** (past hours = noise).
- **Resolution:** Weather Underground station history (whole °F, station-specific URL, post-finalization revisions excluded) — aligns with @AlterEgo_eth station-coordinate lesson.
- **Orchestration pattern:** parallel agents (market rules, Open-Meteo, NWS, NOAA baseline, Polymarket odds) — analogous to conductor multi-tool fan-out, not new alpha by itself.
- **Reference implementation cited:** `github.com/weather_scanner` [NEEDS VERIFICATION 2026-05-22 — repo health/license not audited in K57].

### Cemini posture

- **Strategy is portable** to Cemini's prediction-market stack; weather is a clean adjacency to existing macro/sports market exposure
- **Phase-0 audit required** before adoption: verify Open-Meteo `bias_correction` claim independently, validate station coordinates for any deployed city, treat @theparuchh's P&L as anecdotal at small sample
- **Cross-concept hook**: ensemble methodology applies cleanly to @concepts/macro-weather-regime.md research; weather-trading bot output is a useful sentinel for broader regime detection
- **Reviewer-agent fit**: this strategy is a high-quality test case for @concepts/reviewer-agent-inference-time-feedback.md — entry decisions are concrete, falsifiable, and easily backtestable

### Open questions

- Is `bias_correction=true` documented in Open-Meteo's official API reference? (verifiable via @entities/data-sources/open-meteo.md before production use)
- What's the true sample size behind the 18% → 30% win-rate claim? (3 days × 11 cities × ~144 scans/day = high frequency but low independent-event count)
- Does the 18-30 hr edge persist after publication, or does the X post itself close the gap?
