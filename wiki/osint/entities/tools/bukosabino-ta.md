---
title: "bukosabino/ta — Python Technical Analysis Library"
type: entity
tags: [tool, technical-analysis, python-library, mit, adopt-tier, 43-indicators, github-eval-2026-05-13]
keywords: [bukosabino-ta, technical-analysis-library, ta, python-ta, 43-indicators, rsi-macd-bollinger, mit-license, 5100-stars]
related:
  - sources/eval-github-repos-2026-05-13.md
  - concepts/polymarket-bot-architecture.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/eval-github-repos-2026-05-13.md — Phase-0 eval source (ADOPT verdict, May 13 2026)
- @concepts/polymarket-bot-architecture.md — bot playbook explicitly flags layered indicator stacks as failure mode; this is the tool, discipline is the user
- @entities/platforms/polymarket.md — typical consumer venue

## Raw Concept

What prompted this page: Phase-0 eval verdict (May 13 2026) flagged bukosabino/ta as ADOPT-tier. MIT-licensed, 5.1k stars, 43 indicators in pure Python. Direct adoption candidate for any Cemini strategy module that needs canonical technical-analysis primitives.

## Narrative

### Identity

- **Repo**: `bukosabino/ta` (GitHub)
- **License**: **MIT**
- **Stars**: 5,100+
- **Language**: Python
- **Dependency**: numpy + pandas only
- **Coverage**: 43 technical-analysis indicators

### Indicators included (selected)

| Category | Indicators |
|----------|------------|
| Momentum | RSI, Stochastic, Williams %R, Awesome Oscillator, KAMA, Stochastic RSI, TSI, Ultimate Oscillator, ROC |
| Volatility | Bollinger Bands, Average True Range (ATR), Donchian Channels, Keltner Channels, Ulcer Index |
| Trend | MACD, Aroon, ADX, CCI, DPO, KST, Mass Index, Parabolic SAR, Trix, Vortex |
| Volume | OBV, Chaikin Money Flow, Force Index, Money Flow Index, Negative Volume Index, On Balance Volume, VWAP, Volume Price Trend, Volume Weighted Average Price |
| Others | Daily Return, Daily Log Return, Cumulative Return |

### Adoption posture

**ADOPT** — direct upstream dependency, pinned to a known-good commit.

Cemini policy: pin to a release tag, not `main`. Re-pin on release cadence.

### Cemini integration target

`/opt/cemini/agents/strategies/lib/ta_indicators.py` — thin wrapper around `ta` calls, normalizes the pandas-Series interface to Cemini's internal data types. Strategy modules import the wrapper, not the upstream library directly.

### Important caveat — strategy discipline

`@concepts/polymarket-bot-architecture.md` (citing @0x_Punisher's playbook) explicitly flags **layered indicator stacks** (RSI + MACD + divergence) as a documented failure mode:

> "Avoid: layered indicator stacks (RSI + MACD + divergence). Every indicator adds a failure surface."

bukosabino/ta is the **tool**. The discipline is the user's responsibility. The library makes it easy to compute 5 indicators and worship the result; resist.

### Why MIT matters here

Per `@concepts/cemini-license-posture.md`, MIT is the cleanest license for IP-sale-readiness — no copyleft, no notice-on-distribution beyond attribution. Adopting MIT-licensed dependencies means the eventual buyer-of-Cemini-codebase inherits no licensing land mines.

## Snippets

> "5 of 5 ADOPTs are MIT-licensed. License-posture filter eliminates most candidates before maturity even matters." [Source: eval-github-repos-2026-05-13.docx]

## Dead Ends

- **Stacking 5+ indicators from this library into a single strategy** — see above. The library doesn't enforce discipline; the strategy code does.
- **Forking and modifying upstream** — unnecessary. MIT lets you keep a wrapper layer in Cemini and depend on upstream as-is. Forking creates a maintenance burden with no upside.
