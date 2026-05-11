---
title: Riskfolio-Lib — Convex Portfolio Optimization (BSD-3-Clause)
type: entity
tags: [financial-research, portfolio-optimization, convex-optimization, kelly-criterion, hrp, bsd-3-clause, adopted-tier, cemini-fastmcp]
keywords: [riskfolio-lib, convex-optimization, kelly-criterion, hrp, hierarchical-risk-parity, black-litterman, var, cvxpy, mosek, prediction-market-sizing]
related:
  - sources/links-2-5-4-tool-eval.md
  - entities/tools/financetoolkit.md
  - entities/tools/probablyprofit.md
  - entities/tools/hftbacktest.md
  - sources/jpm-portfolio-impact-investment-saltuk-2012.md
maturity: draft
created: 2026-05-04
updated: 2026-05-11
---

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 12, **Adopt** tier verdict
- @entities/tools/financetoolkit.md — companion Adopt-tier from same batch; complementary integration vector (Riskfolio-Lib for sizing, FinanceToolkit for fundamentals)
- @entities/tools/probablyprofit.md — Steal-from-tier (5_4-links URL 12); probablyprofit's Kelly implementation is one possible alternative to Riskfolio-Lib's; Riskfolio's BSD-3-Clause is cleaner than probablyprofit's wholesale extraction

## Raw Concept

Academic-grade portfolio optimization library — convex math implementations of 24 risk measures (HRP, Black-Litterman, Kelly, VaR, CVaR, Drawdown, etc.). Identified as **Adopt-tier** in the 2026-05-04 Gemini DR eval — Cemini production-stack integration.

## Narrative

- **URL**: https://github.com/dcajasn/Riskfolio-Lib
- **License**: BSD-3-Clause (clean for IP-sale); auxiliary `LICENSE-XL.txt` flagged for verification
- **Stack**: C++ (80.2%) + Fortran (8.3%) + Python (5.3%) bound via Python 3.9+ + numpy/scipy/pandas/cvxpy
- **Solvers**: MOSEK (commercial), CLARABEL, CVXPY (open-source default)
- **Maturity**: 4.1k stars, 390 commits, citations through 2026

### Why Adopt for Cemini production

24 convex risk measures cover everything Cemini needs at the position-sizing decision point. Direct integration vector (per Gemini DR):

1. Wrap modules as `@mcp.tool` decorators in `services/llm_analyst/`
2. DeepSeek brain proposes tentative trades via LangGraph
3. Tools query Riskfolio-Lib for HRP / Kelly / Black-Litterman position-sizing
4. Risk-adjusted orders route to Alpaca / Hyperliquid / **Kalshi / Polymarket**

### Prediction-market applicability (per user note 2026-05-04)

Cemini targets Kalshi + Polymarket which span sports, healthcare/biotech, politics, weather, economic indicators. Riskfolio-Lib's risk measures generalize directly to prediction-market position sizing:

- **Kelly criterion** is the canonical bet-sizing framework for prediction markets (binary contracts with known win probability + payout)
- **HRP** handles correlated event clusters (e.g., correlated election contracts)
- **CVaR / Drawdown** measures protect against catastrophic single-contract loss

The library is venue-agnostic — same math works for equities, crypto, and prediction-market binary contracts.

### Open questions [NEEDS VERIFICATION 2026-05-04]

- `LICENSE-XL.txt` contents — does it override or supplement BSD-3-Clause?
- HRP matrix-inversion RAM spike on 7 GB EPYC host under live load
- MOSEK / GUROBI commercial-solver dependencies — confirm only CVXPY/CLARABEL get installed in Cemini's Docker container

## Snippets

- **24 convex risk measures**: "ranging from basic standard deviation and Maximum Drawdown to highly advanced concepts like the Kelly Criterion and Hierarchical Risk Parity (HRP)." [Source: links 2 5_4.docx URL 12]

- **License-clean for IP-sale**: "The core BSD-3-Clause license sits perfectly on the project's clean list, completely insulating the system against IP-sale legal risks, pending a final clearance of the secondary LICENSE-XL.txt file." [Source: links 2 5_4.docx URL 12]

- **Recommendation tier**: "Adopt. The library should be actively integrated into the Cemini stack as the primary mathematical engine for dynamically calculating position sizing and portfolio risk weighting prior to live execution." [Source: links 2 5_4.docx URL 12]
