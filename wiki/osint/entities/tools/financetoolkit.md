---
title: FinanceToolkit — 150 Standardized Financial Metrics (MIT)
type: entity
tags: [financial-research, fundamental-analysis, risk-metrics, mit, adopted-tier, cemini-fastmcp]
keywords: [financetoolkit, dupont-analysis, garch, var, ulcer-index, fundamental-ratios, prediction-market-research]
related:
  - sources/links-2-5-4-tool-eval.md
  - entities/tools/riskfolio-lib.md
  - entities/infrastructure/yfinance.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 14, **Adopt** tier verdict
- @entities/tools/riskfolio-lib.md — companion Adopt-tier; FinanceToolkit for fundamentals + Riskfolio-Lib for sizing = full FastMCP analyst stack
- @entities/infrastructure/yfinance.md — FinanceToolkit's native Yahoo Finance integration must be force-replaced with Alpaca/FMP feeds per polygon-doctrine

## Raw Concept

Standardized financial-analysis library implementing 150 unique financial metrics, fundamental ratios, and complex risk indicators. Identified as **Adopt-tier** in the 2026-05-04 Gemini DR eval — Cemini production-stack integration.

## Narrative

- **URL**: https://github.com/JerBouma/FinanceToolkit
- **License**: MIT
- **Stack**: Python 100%, integrates with Financial Modeling Prep + Yahoo Finance
- **Maturity**: 4.7k stars, 1,001 commits, v2.0.7 released 2026-03-14
- **Symbol coverage**: 300,000+ symbols claimed

### Why Adopt for Cemini production

Standardizes financial-metric calculations across data vendors, eliminating discrepancies that would otherwise accumulate at the LLM-decision layer. Direct integration vector:

1. Wrap GARCH, Extended DuPont, VaR, Ulcer Index, etc. as `@mcp.tool` decorators in `services/llm_analyst/`
2. DeepSeek brain queries the toolkit during equity / event evaluation
3. Standardized output flows to LangGraph orchestrator for risk-weighted decision

### Healthcare equities + prediction-market applicability (per user notes 2026-05-04)

The library applies across **both halves** of Cemini's market scope:

1. **Healthcare/biotech equities** — biotech/pharma tickers (MRNA, NVAX, BIIB, large-cap pharma) are squarely in scope. Fundamental ratios feed ticker-research workflow alongside `aipoch/medical-research-skills` (5_4-links eval) for clinical-trial / FDA-approval analysis.
2. **Prediction markets on those same names** — FDA approval contracts on Kalshi/Polymarket reference the same biotech tickers; fundamentals + medical research skills feed both trade-execution destinations.

For sports / politics / weather prediction markets, the library is less directly applicable — those rely on event-specific data (sports stats, polling, weather forecasts) rather than corporate fundamentals.

### Critical caveat

Per polygon-doctrine (user-memory):

> "Polygon plan returns NOT_AUTHORIZED on same-day equity intraday; `polygon_ingestor.py` self-heals via yfinance EOD sweep after 16:01 ET."

FinanceToolkit defaults to Yahoo Finance as data backend. **In Cemini production, force-route data sources to Alpaca / FMP for primary, with yfinance as fallback only.** The library's calculation logic is sound; the data-source defaults are not.

### Open questions [NEEDS VERIFICATION 2026-05-04]

- Memory allocation for full 150-ratio pipeline on 10-year daily history (memory spikes during recursive GARCH)
- Whether the toolkit's data-fetching layer is decoupled enough to swap Yahoo for Alpaca cleanly
- Container build-time impact (heavy scipy / scikit-learn / statsmodels dependencies)

## Snippets

- **Scope**: "highly transparent, standardized calculations for over 150 unique financial metrics, fundamental ratios, and complex risk indicators... Extended DuPont Analysis... Value at Risk, GARCH volatility modeling, Ulcer Index." [Source: links 2 5_4.docx URL 14]

- **Standardization rationale**: "fundamentally standardizes the calculation of crucial financial metrics that often fluctuate wildly and unpredictably across different proprietary data vendors, ensuring analytical consistency." [Source: links 2 5_4.docx URL 14]

- **Recommendation tier**: "Adopt. The toolkit should be immediately installed and integrated into the Cemini FastMCP ecosystem to standardize fundamental analysis calculations and risk modeling across all LLM-driven agentic operations." [Source: links 2 5_4.docx URL 14]
