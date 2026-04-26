---
title: US National Weather Service (weather.gov)
type: entity
tags: [data-source, weather, regulatory-primary-source, government]
keywords: [nws, noaa, weather-gov, forecast, alerts, observations, gridpoints]
related:
  - entities/data-sources/open-meteo.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @entities/data-sources/open-meteo.md — companion / complement: Open-Meteo gives global multi-model NWP ensembles (ECMWF + GFS + ICON + MetNo + JMA); NWS gives the single authoritative US-government forecast and observation feed. Use NWS as the tiebreaker when ensemble members disagree on a US-resolution Kalshi weather contract

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. Cemini's weather stack today is Open-Meteo-only; adding NWS gives a US-government primary source for any contract that resolves on official NWS observations.

## Narrative

The US National Weather Service REST API (NOAA-operated, weather.gov)
is the authoritative source for US weather forecasts, current
observations, alerts, and METARs. Every US weather event-contract on
Kalshi (NYC daily high temperature, Chicago snowfall accumulation,
etc.) ultimately resolves on NWS-published values, which makes this
the canonical reference for fair-value computation.

**Key endpoints**:

1. **Point forecast** — `api.weather.gov/points/{lat},{lon}` returns
   the metadata for the gridpoint covering that location, including
   the forecast URL.
2. **Forecast** — `api.weather.gov/gridpoints/{office}/{x},{y}/forecast`
   returns the 7-day forecast in 12-hour intervals; `forecast/hourly`
   returns hourly resolution.
3. **Observations** — `api.weather.gov/stations/{station}/observations`
   returns recent observations (temperature, dewpoint, wind, precip).
4. **Alerts** — `api.weather.gov/alerts/active` returns active
   warnings/watches/advisories — useful for regime-gating
   weather-sensitive strategies.

**Authentication**: none. A descriptive `User-Agent` header is
strongly encouraged (NWS may rate-limit or block missing UAs). No
published rate limit beyond "be reasonable."

**License**: works of the US Government, public domain. No commercial
restrictions.

**Cemini integration angle (not yet wired)**:

- Add NWS as a second ensemble member alongside Open-Meteo's existing
  multi-model fan-out for US-locality weather contracts.
- Use NWS as the resolution-truth source when computing realized P&L
  on settled Kalshi weather contracts (Open-Meteo's reanalysis is good
  but NWS observations are what actually settles the contract).
- Subscribe to alerts as a regime-gate input (severe weather watches
  → tighten risk on weather-correlated equities like utilities).

## Snippets

- API root: https://www.weather.gov/documentation/services-web-api
- Spec (OpenAPI 3.0): https://api.weather.gov/openapi.json
- Example point: `https://api.weather.gov/points/40.7128,-74.0060` (NYC)
