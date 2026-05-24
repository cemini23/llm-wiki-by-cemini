---
title: "Freqtrade — legacy open-source Python crypto algo-trading framework"
type: entity
tags: [entity, tool, algorithmic-trading, crypto, python, ccxt, gpl-3, hyperopt, k56]
keywords: [freqtrade, ccxt, hyperopt, conda, docker, telegram-bot, webui, 48k-stars, gpl-3, machine-learning-strategy-optimization]
related:
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - entities/tools/opentrader.md
  - concepts/cemini-license-posture.md
  - concepts/cemini-deployment.md
  - entities/tools/superalgos.md
maturity: draft
created: 2026-05-21
updated: 2026-05-24
phase_0_verdict: REFERENCE-ONLY — mature reference implementation for crypto algo-trading patterns; GPL-3 is incompatible with Cemini IP-sale perimeter so cannot be bundled, but strategies / Hyperopt patterns are public-domain learning material
---

## Relations

- @sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md — K63 URL 30 GPL Reject reaffirmed
- @sources/analyzing-github-projects-agentic-infra-2026-05-21.md — primary source (section "The Legacy vs Modern Frameworks: Freqtrade and OpenTrader")
- @entities/tools/opentrader.md — modern TypeScript counterpart
- @concepts/cemini-license-posture.md — GPL-3.0 is incompatible with IP-sale perimeter
- @concepts/cemini-deployment.md — Conda + Docker deployment patterns referenced

## Raw Concept

What prompted this page: K56 Analyzing GitHub Projects report. Freqtrade is the canonical legacy reference framework for open-source crypto algo-trading and is worth a dedicated entity page given (a) likelihood of cross-references in future K-batches and (b) the importance of its CCXT-backed exchange-normalization pattern.

- URL: `https://github.com/freqtrade/freqtrade`
- License: **GPL-3.0**
- Stars: ~48,100 (per source — would put it in the top-tier of open-source trading frameworks)
- Language: Python

## Narrative

**Freqtrade** is the long-standing dominant open-source Python algo-trading framework for crypto. The architecture is:

- **Strategy authoring**: Python class with `populate_indicators`, `populate_entry_trend`, `populate_exit_trend` callbacks. Heavy use of `ta-lib` / `pandas-ta` technical indicators.
- **Backtesting**: against historical tick / OHLCV data, with realistic order-fill modeling.
- **Hyperparameter optimization**: via **Hyperopt** (Bayesian optimization over strategy parameters). One of the framework's distinguishing features.
- **Live execution**: connected to ~100+ exchanges via **CCXT** (the cross-exchange API normalization library).
- **Control interface**: secure Telegram bot OR local WebUI.
- **Deployment**: Conda environments OR provided Docker Compose files.

### Known limitations (per source)

- **Exchange-specific API inconsistencies** — CCXT-noted: bitbank / bitforex / bithumb etc. suffer from missing `fetchMyTrades` / `fetchOrder` endpoints, requiring fallback to orderbook-parsing.
- **Configuration file pathing errors** — common operational pain reported in issues + StackOverflow.

### Cemini relevance

**Reference-only, not adoption target.**

- GPL-3.0 license blocks integration into Cemini's IP-sale bundle (per @concepts/cemini-license-posture.md).
- Cemini's existing algo-trading stack on cemini-prod is custom-built and Polymarket-focused, not crypto-spot-focused — Freqtrade's exchange coverage isn't directly applicable to our Polymarket/Hyperliquid surface.
- However, the **Hyperopt-driven strategy-optimization pattern** is instructive. If we ever ship a Cemini Polymarket strategy with tunable parameters (e.g., LP-range spacing, stop-loss thresholds), Freqtrade's Hyperopt patterns are a public-domain blueprint we can re-implement under a clean-room MIT/Apache-2.0 derivative.
- The CCXT pattern is independently relevant: pmxt is literally pitched as "CCXT for prediction markets" (@entities/tools/pmxt.md).

### Comparison vs OpenTrader

| Feature | Freqtrade | OpenTrader |
|---|---|---|
| Language | Python | TypeScript |
| License | **GPL-3.0** | **Apache-2.0** |
| Stars | ~48,100 | ~2,600 |
| Maturity | Mature (years) | Newer |
| Strategy optimization | Hyperopt (Bayesian) | Built-in GridBot/DCA/RSI |
| Control | Telegram + WebUI | Robust UI |
| Deployment | Conda / Docker | NPM (Node.js) |
| Exchange normalization | CCXT | CCXT |
| IP-sale compatibility | ❌ (GPL-3) | ✅ (Apache-2) |

For a future Cemini IP-sale-clean reference architecture, **OpenTrader is the structurally compatible choice** between the two — Freqtrade's GPL-3 disqualifies it regardless of merit.

## Dead Ends

- The source report's star counts are from May 2026; for a serious license / activity audit before any code-cribbing, run a fresh `gh api repos/freqtrade/freqtrade` lookup. Per K53/K54/K55 recurring pattern, secondary-source eval reports get license claims wrong ~10-15% of the time.
