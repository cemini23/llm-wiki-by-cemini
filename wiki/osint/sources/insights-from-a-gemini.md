---
title: "Insights from a Gemini — The Attrition Protocol: Comprehensive Trading Framework Synthesis"
type: source
tags: [docx, gemini-deep-research, trading-framework, attrition-protocol, options, market-microstructure, risk-management, technical-analysis, ict, cemini-internal]
clusters: [market-microstructure, quant-finance, cemini-internal]
keywords: [attrition-protocol, gemini-deep-research, bowtied-bull, vcp, weinstein-stages, ict, inner-circle-trader, fair-value-gap, order-blocks, heatseeker, 0dte-credit-spreads, covered-calls, cash-secured-puts, vwap, volume-analysis, tape-reading, risk-sizing, tilt-control]
related:
  - concepts/market-microstructure.md
  - entities/platforms/kalshi.md
  - concepts/quant-finance.md
  - sources/signa.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub; this document extensively covers ICT liquidity paradigms, order blocks, and execution-level microstructure
- @entities/platforms/kalshi.md — primary Cemini prediction-market venue; the 0DTE credit-spread and options-selling strategies reference exchange microstructure
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; the risk-sizing (Zhawk RU system), barbell allocation, and capital preservation framework directly inform Cemini position-sizing logic
- @sources/signa.md — sibling Cemini intelligence report; the Weinstein Stage Analysis and Wyckoff phases from signa.docx are used throughout this framework

## Raw Concept

- **Original title**: Insights from a Gemini — STRATEGY SYNTHESIS: The Attrition-Based Wealth Generation Framework
- **Author(s)**: Gemini Deep Research (LLM synthesis); sources attributed to BowTied Bull, TheShortBear, Benjamin Graham, Stan Weinstein, SMB Capital, Deutsche Bank, Brent Donnelly, Mark Minervini, David Ryan, ICT (Inner Circle Trader), Heatseeker, Zhawk, and others
- **Type**: DOCX (Gemini Deep Research output)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/Insights from a Gemini.docx
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via `extract_docx.py` after `scp` from librarian)
- **Length**: 3,617 lines extracted text; multi-module framework with 30+ cited sources
- **Read status**: deep-read
- **Note**: Watermarked "CB invest" and "@yzab_eth on X" per document metadata

## Narrative

A Gemini Deep Research synthesis compiling a comprehensive active trading framework organized around the "Attrition Protocol" — a capital-preservation-first philosophy whose core thesis is: *"We do not gamble. We are the House. Survival > Growth."* The document integrates trading methodologies from 30+ practitioners into 7 modules, each building on the previous, culminating in a unified execution framework.

### Core philosophy

The Attrition Protocol prioritizes avoiding catastrophic losses ("never go to zero") over maximizing short-term gains. Capital allocation follows a barbell: 70% core (low-risk, index funds, no leverage) + 15-30% opportunistic (high-conviction trades, trend-following, options selling). The primary enemy is not the market but investor psychology — specifically greed and the impulse to chase euphoric moves.

### Seven modules

| Module | Domain | Key frameworks | Cemini relevance |
|--------|--------|---------------|------------------|
| 1. Foundational Philosophy | Capital preservation, compounding, barbell allocation | BowTied Bull (attrition), Benjamin Graham (margin of safety), TheShortBear (80/15 barbell) | Position-sizing guardrails for RL ensemble |
| 2. Macro & Market Structure | Stage analysis, institutional flows, regime shifts | Stan Weinstein (4-stage), Deutsche Bank (systematic vs. discretionary positioning), Brent Donnelly (regime shifts) | Market regime feature for MAPPO state vector |
| 3. Algorithmic Microstructure (ICT) | Liquidity paradigm, Power of Three, PD Arrays | ICT — Fair Value Gaps, Order Blocks, Breaker Blocks, Market Structure Shift, SMT Divergence | Microstructure alpha factors for 34-dim feature vector |
| 4. Tactical Execution | Specific A+ setups, playbook discipline | SMB PlayBook (consolidation breakout, opening drive), Minervini/Ryan VCP, 0DTE credit spreads | Strategy catalog for RL backtesting |
| 5. Precision Tools | Tape reading, volume analysis | Time & Sales (holding bid, lifting offers, speed), Volume spikes, low-volume rallies | Execution confirmation signals |
| 6. Risk Management | Quantitative position sizing, trade management | Zhawk Risk Units (1 RU = 1% of opportunistic capital), progressive exposure, base-hit philosophy | Direct input to Cemini Kelly/CVaR sizing |
| 7. Psychology & Process | Tilt control, process over outcome | Circuit breaker protocol, daily/weekly review discipline | Guardrails for autonomous execution |

### The Master Cheatsheet (Phase 1 — Execution)

An 8-row decision matrix mapping market speed/phases to specific setups, indicators, and entry rules:

| Phase | Indicator | Setup | Source |
|-------|-----------|-------|--------|
| 0. News/Catalyst | Gap Up >4% + massive volume | Episodic Pivot (blind buy) | Stockbee #013 |
| 1. Momentum (Ignition) | Elephant Bar off 20MA | Buy high of bar (stop at low) | O. Velez #021 |
| 2. Momentum (Resting) | Range high break after 2-3 quiet days | Momentum Burst | Stockbee #016 |
| 3. Precision (Coil) | VCP or Inside Bar | Buy stop at pivot | Minervini #022 |
| 4. Parabolic (Mania) | High Tight Flag + volume | Speed Breakout | Zanger #023 |
| 5. Trap (Reversal) | Breakout fails, closes below level | Short the failed move | Allstar #014 |
| 6. Defense (Trend) | Price touches Anchored VWAP | Buy the bounce | Shannon #020 |
| 7. Climax (Profit) | Price >25% above 50MA | Trim 30-50% | Revere #009 |
| 8. Kill Switch (Exit) | Close below 10MA or 20MA | Sell all | Qullamaggie #018 |

Guard condition: if SPY < 21-day EMA, Rows 1-4 are OFFLINE. Only Row 0 (Episodic Pivot) or Row 5 (Short Trap) permitted.

### ICT algorithmic microstructure (Module 3)

The framework transitions from classical technical analysis (Weinstein/O'Neil/Minervini) to an algorithmic, liquidity-based model. Core concepts:
- **Liquidity paradigm**: Support/resistance are pools of stop-loss orders (Buy-Side Liquidity / Sell-Side Liquidity). The algorithm sweeps these before reversing.
- **Power of Three (PO3)**: Accumulation → Manipulation (false move / sweep) → Distribution (true move). Trade only the Distribution leg.
- **Fair Value Gap (FVG)**: Three-candle imbalance where price moved too fast — price returns to "rebalance."
- **Order Block (OB)**: Last down-candle before strong up-move (institutional entry marker).
- **SMT Divergence**: When correlated indexes (ES/NQ) diverge — highest-conviction reversal signal.

### Risk management (Module 6 — Zhawk system)

Risk is defined in Risk Units (RU): 1 RU = 1% of opportunistic capital. Base trades: 2.5-5 RU. High conviction: up to 10 RU. Lotto/weekly: <2.5 RU. Trade management: sell 70-80% at conservative target (15-30% ROI or 1R), leave 20-30% to capture asymmetrical upside with stop at breakeven.

### Cemini integration pathways

1. The 8-phase Master Cheatsheet can be formalized as a market-regime classifier feeding the MAPPO state vector
2. ICT's Fair Value Gaps and Order Blocks provide microstructure-level alpha factors for the 34-dim feature vector
3. The Zhawk RU sizing system directly parallels Cemini's Kelly/CVaR position-sizing engine — cross-validate both approaches
4. The "Attrition" philosophy (defined risk, never naked, capital preservation first) maps directly to the SAE execution middleware proposed in `@sources/signa.md`

## Snippets

### S1 — Core philosophy

> "We do not gamble. We are the House. Survival > Growth: The goal is to be the last man standing. Sell, Don't Buy: We sell options to collect premium (Win Rate ~80%). We rarely buy options. Defined Risk: We never enter a trade without knowing the exact maximum loss."

### S2 — Attrition framework (BowTied Bull)

> "True wealth is generated by enduring rather than maximizing. The primary goal of a strategy must be the avoidance of catastrophic, leverage-induced losses, which is considered more critical than achieving peak returns during bull cycles. The most significant risk to a portfolio is the investor's own psychology—specifically, greed and the urge for rapid gains."

### S3 — ICT Power of Three

> "Price delivery typically follows a three-phase sequence to extract liquidity: Accumulation (price consolidates, building liquidity on both sides). Manipulation (a false, forceful move sweeps one side's liquidity, trapping traders). Distribution (the true, powerful expansionary move in the opposite direction of the manipulation). The goal is to trade the final phase."

### S4 — Risk unit sizing (Zhawk)

> "Risk Unit (RU): Define risk in units, not dollars. 1 RU = 1% of opportunistic capital. Base Trade: 2.5 - 5 RUs. High Conviction: Up to 10 RUs. Lotto/Weekly: < 2.5 RUs. Sell 70-80% of position at a conservative target (15-30% ROI or 1R). Leave 20-30% to capture asymmetrical upside with Stop Loss moved to Breakeven."
