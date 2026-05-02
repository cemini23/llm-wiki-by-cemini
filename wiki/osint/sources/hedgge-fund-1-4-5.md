---
title: "Do Hedge Funds Prefer Safe Stocks? Revisiting Hedge Fund Preferences for Stock Characteristics (Cao, Green & Li, 2014)"
type: source
tags: [pdf, academic, hedge-funds, stock-characteristics, factor-investing, quant-finance, cross-sectional-returns, risk-management]
clusters: [quant-finance]
keywords: [hedge-fund-holdings, stock-characteristics, safe-stocks, return-volatility, cross-section-of-returns, firm-characteristics, institutional-holdings, factor-investing, flight-to-safety]
related:
  - concepts/quant-finance.md
  - entities/ticker-watchlist.md
  - concepts/portfolio-strategy.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; this paper directly challenges the "smart money chases alpha" narrative with evidence of safety preference
- @entities/ticker-watchlist.md — Cemini watchlist; hedge fund stock-preference characteristics inform factor-based screening
- @concepts/portfolio-strategy.md — portfolio construction and strategy allocation; the safety-preference finding has implications for defensive strategy weighting

## Raw Concept

- **Original title**: Do Hedge Funds Prefer Safe Stocks? Revisiting Hedge Fund Preferences for Stock Characteristics
- **Author(s)**: Charles Cao (Penn State, Smeal College of Business), Jeremiah Green (Texas A&M, Department of Accounting), Jiahan Li (University of Notre Dame)
- **Type**: PDF (academic paper)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/hedgge fund 1 4:5.pdf
- **Published**: 2014-06-12
- **External IDs**: SSRN 2449165; DOI 10.2139/ssrn.2449165
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via Exa crawling_exa + PyMuPDF extraction from librarian)
- **Length**: 50 pages
- **Read status**: deep-read
- **Metrics**: 239 downloads, 2,160 abstract views; SSRN rank 273,363; 2 citations, 30 references

## Narrative

This paper reexamines hedge fund preferences for stock characteristics using aggregate quarterly hedge fund holdings and a comprehensive set of 90 firm characteristics. The authors compare coefficients from hedge fund holding regressions with return prediction regressions to infer whether hedge funds prefer characteristics that predict future returns.

### Key findings

1. **Safety preference dominates**: Hedge fund holdings reveal a strong preference for "safe stocks" — characteristics that predict low return volatility — NOT characteristics that predict higher returns. This contradicts the common assumption that sophisticated investors chase alpha factors.

2. **Little return-predictive preference**: With only a few exceptions, hedge funds show little evidence of preferring stock characteristics that predict higher returns. The exceptions are characteristics that capture economic and accounting fundamentals (not momentum, technical, or sentiment-based signals).

3. **Safety preference is strongest during recessions**: The preference for low-volatility stocks intensifies during bad times, suggesting a "flight to safety" dynamic in institutional portfolios even among supposedly alpha-seeking hedge funds.

4. **Expanded characteristic set matters**: Using 90 firm characteristics (from Green, Hand, and Zhang 2014) rather than the narrow sets used in prior research is important — the expanded set explains 80.4% (mean adjusted R²) of variation in quarterly hedge fund holdings.

5. **Persistence dominates**: Lagged hedge fund holdings are the single most important explanatory variable — aggregate hedge fund holdings are generally static quarter-to-quarter.

### Firm characteristic categories analyzed

The 90 characteristics span: accruals, balance sheet ratios, earnings innovations, fundamental risk, industry structure, long-run growth, stock volatility, momentum, operating strategy, profitability, size/liquidity, and stock trading-related measures.

### Implications for Cemini

- **Strategy selection**: The safety-preference finding suggests that strategies targeting low-volatility, high-quality stocks may have persistent institutional demand — relevant for the MAPPO ensemble's reward function design
- **Regime-aware allocation**: The finding that safety preference intensifies during recessions supports regime-conditional position sizing (consistent with the Weinstein/Wyckoff phase classification in `@sources/signa.md`)
- **Factor relevance**: Of 90 characteristics, only 43 are significant in explaining hedge fund holdings — a useful filter for selecting which factors to include in the 34-dim Cemini feature vector
- **Counter-narrative**: This paper provides evidence that institutional capital does NOT systematically chase the same alpha factors that academic research identifies — important context for evaluating any strategy's capacity constraints

## Snippets

### S1 — Abstract

> "We reexamine hedge fund preferences for stock characteristics using aggregate quarterly hedge fund holdings and a large set of firm characteristics. We find that the expanded set of firm characteristics is important in explaining variation in quarterly hedge fund holdings. Consistent with prior research, we find little evidence that hedge funds prefer stock characteristics that predict higher returns except among characteristics that capture economic and accounting fundamentals. In contrast, we find that hedge fund holdings reveal a strong preference for safe stocks, i.e. stock characteristics that predict low return volatility, that is strongest during bad times (recessions)."

### S2 — Explanatory power

> "Our quarterly cross-sectional regressions have a mean adjusted R-squared of 80.4%. The most important explanatory variable of hedge fund holdings is lagged hedge fund holdings, showing that at least in aggregate, hedge fund holdings are generally static. However, 43 of the 90 firm characteristics that we study are also significant in explaining the cross-section of hedge fund returns."

### S3 — Safety over alpha

> "With only a few exceptions and even with the large number of firm characteristics, we find little evidence that hedge fund holdings reflect preferences for characteristics that predict higher returns. These findings are consistent with prior research that finds little evidence that hedge funds understand or exploit return predictability."

### S4 — Comparison methodology

> "We explore the return forecasting abilities of the same set of firm characteristics, and compare the mean estimated coefficients from the hedge fund holding regressions with the mean coefficients from return prediction regressions as a means of inferring whether hedge funds exhibit preferences for firm characteristics that predict future returns."
