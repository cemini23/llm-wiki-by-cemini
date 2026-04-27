---
title: 'Master Trading Playbook: Institutional Frameworks for Algorithmic Execution and Risk Mitigation'
type: source
tags: [docx, rl-marl, quant-finance, crypto]
related:
  - concepts/dispersion-trading.md
  - concepts/game-of-attrition-doctrine.md
  - concepts/ip-sale-readiness.md
  - concepts/macro-weather-regime.md
  - concepts/quant-finance.md
  - entities/components/kelly-cvar-risk-engine.md
  - entities/frameworks/nautilustrader.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-23
clusters:
  - rl-marl
  - quant-finance
  - crypto
---

## Relations

- @concepts/dispersion-trading.md
- @concepts/game-of-attrition-doctrine.md
- @concepts/ip-sale-readiness.md
- @concepts/macro-weather-regime.md
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md
- @entities/frameworks/nautilustrader.md

## Raw Concept

- **Original title**: Master Trading Playbook: Institutional Frameworks for Algorithmic Execution and Risk Mitigation
- **Author(s)**: _unknown (stub — not yet read)_
- **Type**: DOCX
- **Location**: research for cemini/Trading Playbook Research.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: —
- **Read status**: deep-read
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, quant-finance, crypto

## Narrative

### Abstract
Binary, rule-based trading playbook split between Quantos (TradFi derivatives, quant algo execution) and Kashi (DeFi, margin, on-chain). Governing paradigm: 'The Game of Attrition' — mechanical, binary execution, no discretion. Macro Weather System (GREEN/YELLOW/RED based on SPY vs 21-EMA/50-SMA) gates all strategies. Alpha generation strategies: statistical arbitrage, volatility arbitrage / dispersion trading, tactical setups ('cheat codes'). Cross-asset weight of evidence (JNK vs TLT lead/lag) used as regime validation.

### Key findings
- Binary execution framework: losing trade by protocol = valid; profitable trade by discretion = failure
- GREEN: SPY > 21-EMA rising → aggressive breakout / full size
- YELLOW: SPY < 21-EMA, > 50-SMA → trim, no new accumulation
- RED: SPY < 50-SMA → cash + short; long-momentum disabled
- Cross-asset validation: if JNK fails to lead TLT on equity breakout, breakout statistically fails — SHORT on failure close
- Stat arb uses Ornstein-Uhlenbeck process + RL for dynamic thresholds, not static Z-score
- EMRT (Empirical Mean Reversion Time) > 90th percentile → kill execution (structural fracture)
- Dispersion trade: long single-stock vol / short index vol when implied correlation > realized; reverse-dispersion when crowded (Volmageddon-style tail)
- Intraday directional trading restricted to catalog of named tactical setups — anything else = noise

### Entities referenced
Quantos, Kashi, SPY, JNK, TLT, VIX, Ornstein-Uhlenbeck process, Kelly/CVaR risk engine, NautilusTrader

### Concepts covered
Game of Attrition doctrine, binary decision framework, Torso Bite (catastrophic drawdown), Macro Weather / Traffic Light regime, GREEN/YELLOW/RED state, weight of evidence, statistical arbitrage, mean reversion, Empirical Mean Reversion Time (EMRT), Mean Reversion Budgeting (MRB), volatility arbitrage, dispersion trading, implied vs realized correlation, reverse dispersion, Volmageddon tail risk, alpha decay (crowding), tactical setup catalog

## Snippets

*(None yet — populate on first deep read.)*
