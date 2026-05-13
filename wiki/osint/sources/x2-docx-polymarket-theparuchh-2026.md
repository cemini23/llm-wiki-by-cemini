---
title: "x 2.docx — @theparuchh Polymarket Weather Bot Full Guide ($130 bankroll, +45.9% ROI / 3 days, late April 2026)"
type: source
tags: [x-thread, polymarket-weather-trading, open-meteo-api, weather-station-coordinates, kelly-criterion, mac-mini-deployment, multi-model-ensemble, k41]
keywords: [theparuchh, polymarket-weather-bot, open-meteo-bias-correction, hartsfield-jackson-katl, station-coordinates-vs-city-center, hong-kong-observatory-lantau, tokyo-narita-haneda, seoul-incheon-rksi, 18-30-hour-entry-window, icon-dwd-gfs-noaa-ecmwf-three-model-ensemble, 3-bin-coverage, kelly-criterion-bankroll, mac-mini-bedroom-deployment]
related:
  - entities/people/theparuchh.md
  - concepts/polymarket-weather-trading-strategy.md
  - sources/x-docx-polymarket-claude-md-2026-04-23.md
  - concepts/polymarket-market-making-architectures.md
  - entities/data-sources/open-meteo.md
maturity: draft
read_status: read
created: 2026-05-13
updated: 2026-05-13
clusters: [prediction-markets, automation]
---

## Relations

- @entities/people/theparuchh.md — author
- @concepts/polymarket-weather-trading-strategy.md — primary concept page that this source feeds (with @sources/x-docx-polymarket-claude-md-2026-04-23.md Section 1)
- @sources/x-docx-polymarket-claude-md-2026-04-23.md — companion technical breakdown by @AlterEgo_eth; this source = operational guide, that source = API mechanics
- @concepts/polymarket-market-making-architectures.md — sibling architectural pattern; weather-bot is a domain-specific operational instance
- @entities/data-sources/open-meteo.md — primary upstream API used (free, supports `bias_correction=true`)

## Raw Concept

- **Title**: "HOW I BUILT A POLYMARKET WEATHER BOT THAT PRINTS MONEY"
- **Author handle**: @theparuchh (Paruchh)
- **Length**: ~16,148 bytes / one long-form X post
- **Source platform**: x.com
- **Date**: late April 2026 (references "first article" at x.com/theparuchh/status/2044089761699102827)
- **File location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/x-2-theparuchh-polymarket-weather-bot-2026.docx`
- **sha256**: `5cb935a152781a30...` (preingest verdict: NEW)
- **Size**: 16,148 bytes
- **Read status**: read (full document)
- **Discovered via**: user drop into `research to be indexed/` 2026-05-12

## Narrative

### The setup

- 11 cities across 4 continents
- 3 weather models running in parallel
- Mac Mini deployed in bedroom (24/7)
- $130 bankroll
- Bot scans Polymarket every 10 minutes

### Version-by-version P&L arc

- **V1** lost $40 — 5 US cities, GFS ensemble only, Kelly Criterion sizing
- **V2** lost $23 — added Asia, hoped for noise reduction
- **V3** made +$43 in last 3 days — after fixes described below; +45.9% ROI over 3 days

> "The difference wasn't in the models, not in the strategy, not in the bankroll. The difference was in one line of code 50 kilometers from where I thought I should be looking."

### Discovery #1 — Weather station coordinates vs city centers (the load-bearing fix)

Each Polymarket weather market resolves to a **specific weather station**, not the city center. Example resolution rule:

> "This market will resolve to the temperature range that contains the highest temperature recorded at the Hartsfield-Jackson International Airport Station in degrees Fahrenheit on 2 May."

Author audit of 11 city/station mappings:

| City | Resolves to | Author was pulling | Distance / impact |
|------|-------------|-------------------|-------------------|
| NYC | LaGuardia KLGA | Manhattan | Different microclimate |
| Atlanta | Hartsfield KATL | Center | Lucky — close |
| Miami | Miami Intl KMIA | Center | Lucky |
| Chicago | O'Hare KORD (far west) | Downtown | Different |
| Dallas | Love Field KDAL | Center | Lucky |
| **Tokyo** | **Haneda RJTT (south Tokyo, bay)** | **Narita** | **60 km off; airport in fields, no urban heat island** |
| **Seoul** | **Incheon RKSI (west, sea)** | **Downtown Seoul** | **50 km off; sea proximity = 1.5°C cooler** |
| **Hong Kong** | **HK Observatory** (NOT airport) | **Lantau** | **30 km off; 2-3°C cooler (sea, wind, island)** |
| Singapore | Changi WSSS | Center | Lucky |
| London | London City EGLC | Center | Lucky |
| **Paris** | **Le Bourget LFPB (N suburbs)** | **Charles de Gaulle** | **Different** |

**5 of 11 cities had wrong coordinates.** Polymarket bins are 2°F (~1°C) wide, so a 1-3°C station-vs-center mismatch = the entire bet missing.

### Discovery #2 — Open-Meteo `bias_correction=true` parameter

Default Open-Meteo response = general regional forecast. With `bias_correction=true`:

> "Accuracy improves by 30 to 40%. It's free, you just add it to the URL."

Applies local correction for specific weather station (urban heat island, coastal effects, elevation, surface type).

### Discovery #3 — Entry window 18-30 hours pre-resolution

Author's V1 window was 6-12 hours pre-resolution; YES prices already at 50¢+ (market had priced in latest forecasts; edge squeezed). 18-30 hours pre-resolution: prices 10-30¢ on same bins (market hasn't reacted to fresh models). Switching window rewrote half the bets.

### Discovery #4 — Multi-model ensemble with consensus rule

V1 used GFS ensemble only. V3:

- **ICON** (DWD Germany)
- **GFS** (NOAA USA)
- **ECMWF** (Europe)

Decision rule:
- If 2 models agree (within 1°C of each other) → third is outlier; trade
- If all three diverge by >3°C → skip the market

### Discovery #5 — 3-bin coverage replaces single-bin

V1 bet on single best bin: hit = win, miss by 1°C = full loss. V3: covers 3 adjacent bins simultaneously (center of consensus + one on each side, or two above if outlier is up). Stake grew $2 → $6 per event but **win rate jumped 18% → 30%**.

Gate conditions:
- Sum of 3 bin prices ≤ 95¢ (math edge guaranteed)
- Each bin ≥ 1¢ (skip resolved markets)
- Each bin ≤ 45¢ (skip overpriced markets)

If any condition fails → skip event.

### Cemini relevance

- **Operational manual** for adding Polymarket weather-market coverage to Cemini's prediction-market stack. Maps cleanly to existing tradingagents architecture: data-source layer (Open-Meteo), market-resolution layer (Polymarket Gamma API per @sources/x-docx-polymarket-claude-md-2026-04-23.md), strategy layer (3-model consensus + 3-bin coverage), risk layer (Kelly Criterion + gate conditions).
- **Station-coordinates discovery is the kind of error Cemini's reviewer-agent (@concepts/reviewer-agent-inference-time-feedback.md) should catch**: a resolution-rule mismatch that ran for 9 days losing money. Reviewer-agent reading the market resolution text against the bot's data source coordinates would have flagged before deployment.
- **Multi-model consensus + outlier rejection** is a portable pattern beyond weather: applies to **any prediction-market strategy with multiple upstream forecasters**.
- **`bias_correction` parameter discipline** generalizes: there is almost always a free accuracy improvement available in the upstream API that nobody reads the docs to find. Operational lesson is read-the-API-thoroughly, not weather-specific.
- **Track record signal**: $130 bankroll @ +45.9%/3 days is **not statistically significant** — too small, too short. Treat author's track record as anecdotal, the methodology as portable.
- **Audit posture for adoption**: GitHub repo for the bot is not stated in this source; before any Cemini implementation work, search for upstream code repo and run Phase-0 audit (license, maturity signals, mischaracterization check) per Cemini standard.

## Snippets

> "After 9 days the bankroll was down $63. And I got stuck on one question: If the models are on average correct, why am I losing every single day? The answer was in a line I had never read. At the bottom of the market page on Polymarket. In small print." [Source: x 2.docx, @theparuchh]

> "This market will resolve to the temperature range that contains the highest temperature recorded at the Hartsfield-Jackson International Airport Station in degrees Fahrenheit on 2 May. Hartsfield-Jackson Airport Station — Not 'Atlanta', not 'city center', a specific weather station at a specific airport." [Source: x 2.docx, @theparuchh]

> "If 2 models agree (within 1°C of each other), the third is treated as an outlier. If all three diverge by more than 3°C, we skip the market entirely. The models don't know what's coming, so we don't either." [Source: x 2.docx, @theparuchh]

## Dead Ends

- Did NOT pull author's "first article" at x.com/theparuchh/status/2044089761699102827 — referenced but not in this source
- Did NOT verify Open-Meteo `bias_correction=true` parameter behavior or the +30-40% accuracy claim independently. Flag `[NEEDS VERIFICATION 2026-05-13]` before relying on the magnitude.
- Did NOT pull GitHub or other code repo for the bot; author claims Mac Mini deployment but no source link captured in this document
