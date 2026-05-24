---
title: PolyWeather — settlement-oriented weather quant stack (AGPL, reference-only)
type: entity
tags: [entity, tool, polymarket, weather-trading, reference-only, agpl-3, calibration, k60]
keywords: [polyweather, yangyuan-zhen, deb, emos, crps, taf, bucket-matching, agpl, k60]
related:
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/cemini-license-posture.md
  - concepts/ensemble-weather-forecasting.md
  - entities/data-sources/open-meteo.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — K60 URL cluster; methodology steal flagged on re-audit
- @concepts/polymarket-weather-trading-strategy.md — weather PM strategy parent
- @concepts/cemini-license-posture.md — **AGPL-3.0** poison pill for code import
- @concepts/ensemble-weather-forecasting.md — ensemble / calibration methodology overlap
- @entities/data-sources/open-meteo.md — forecast input layer (PolyWeather also ingests METAR/TAF/official obs networks)

## Raw Concept

K60 first pass rejected **`yangyuan-zhen/PolyWeather`** with the weather-bot batch. Re-audit: active production meteorology product (~69★, AGPL-3.0 from 2026-03-30) with **settlement-grade calibration** — steal **methodology**, not code.

## Narrative

- **Repo**: [github.com/yangyuan-zhen/PolyWeather](https://github.com/yangyuan-zhen/PolyWeather) (~69★, pushed 2026-05-23)
- **License**: **AGPL-3.0 only** (explicit open-core / commercial boundary in `docs/OPEN_CORE_POLICY.md`) — **NO-GO for code import** into proprietary Cemini stack [CONFIRMED]
- **Product**: Hosted dashboard + Telegram bot; 51 cities; subscription/onchain checkout — operator is selling SaaS, not donating MIT bot code

### Methodology worth stealing (reference-only)

| Idea | What it is | Why it matters for Cemini weather PM |
|------|------------|----------------------------------------|
| **DEB** | Dynamic Error Balancing across model highs | Better than naive 3-model average for station-specific bias |
| **EMOS / CRPS calibration** | Ensemble model output statistics → calibrated bucket probabilities | Direct upgrade path for `@concepts/polymarket-weather-trading-strategy.md` EV math |
| **Strict bucket matching** | Full `all_buckets` surface; exact/range/or-higher/or-lower direction checks | Reduces tail-bucket mis-map bugs (AlterEgo station-coordinate class) |
| **TAF + intraday rules** | Airport TAF parse (FM/TEMPO/BECMG); invalidation + confirmation rules | Airport-settled PM markets (NYC/London etc.) |
| **Official obs networks** | JMA AMeDAS, CMA/NMC, HKO, CWA, MGM overlays | Settlement anchor discipline beyond generic Open-Meteo grid |
| **Model–market delta** | `model probability − market-implied probability` as primary panel | Same “stale price vs forecast revision” frame as K57 @polydao |

### Verdict: **Reference-only (methodology Steal-from, zero code fork)**

Read README + `docs/` for calibration/settlement design patterns. Re-implement clean-room on prod if scoped. **Never** ship AGPL-derived code or run their hosted bot against Cemini wallets without separate legal review.

### Phase-0

Not required for reference-only posture. If calibration modules are ever considered for port: stop at AGPL boundary; compare against academic EMOS literature instead of copying source.

## Snippets

> "Calibrated model probability is now the primary probability panel… EMOS/CRPS calibration is wired and trainable, but production should stay on legacy or emos_shadow." [Source: github.com/yangyuan-zhen/PolyWeather README, retrieved 2026-05-24]

> "Licensed under GNU AGPL-3.0 only from 2026-03-30 onward." [Source: same, OPEN_CORE_POLICY.md reference]
