---
title: "Stock Market and No-Dividend Stocks (Atmaz & Basak, 2021 — Journal of Finance)"
type: source
tags: [pdf, academic, quant-finance, asset-pricing, dividend-stocks, consumption-based-equilibrium, no-dividend-stocks]
clusters: [quant-finance]
keywords: [atmaz, basak, no-dividend-stocks, consumption-based-model, dynamic-asset-pricing, incomplete-information, market-risk-premium, equity-term-structure, purdue, london-business-school]
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

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; this paper provides a structural asset-pricing model explaining why dividend vs. non-dividend stock return characteristics differ, informing Cemini factor construction
- @entities/ticker-watchlist.md — Cemini watchlist; the no-dividend stock return characteristics (lower mean returns, higher vol/betas) inform dividend-status-based factor screening
- @concepts/portfolio-strategy.md — portfolio construction; the model's predictions about risk premium-volatility relation and term structure inform strategy allocation

## Raw Concept

- **Original title**: Stock Market and No-Dividend Stocks
- **Author(s)**: Adem Atmaz (Purdue, Krannert School of Management), Suleyman Basak (London Business School, CEPR)
- **Type**: PDF (academic paper, Journal of Finance forthcoming)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/stocks 3 4:5.pdf
- **Published**: June 2021 (SSRN Feb 2018, last revised Jun 2021)
- **External IDs**: SSRN 3116105; CEPR DP16224
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via scp + PyMuPDF extraction from librarian)
- **Length**: 60 pages
- **Read status**: deep-read

## Narrative

Atmaz and Basak develop the first general equilibrium model of the aggregate stock market featuring both dividend-paying and no-dividend stocks within a consumption-based framework. The paper shows that the presence of no-dividend stocks (historically ~35% of stocks, ~21% of US market cap) produces profound implications that resolve several empirical puzzles leading consumption-based models (habit-formation, long-run risk, rare disasters) struggle with.

### Key findings

1. **No-dividend stocks have distinct risk-return profiles**: No-dividend stocks command lower mean returns but have higher return volatilities and higher market betas than comparable dividend-paying stocks, consistent with empirical evidence [Source: stocks 3 4:5.pdf p.1-2].

2. **Lower stock market-consumption correlation**: The presence of no-dividend stocks reduces the correlation between aggregate stock market returns and consumption growth, because no-dividend stocks contribute to market return fluctuations without contributing to current aggregate consumption [Source: stocks 3 4:5.pdf p.2-3].

3. **Non-monotonic risk premium-volatility relation**: The model generates both negative and positive relations between conditional risk premium and volatility, reconciling the mixed empirical evidence (some papers find negative, others positive) [Source: stocks 3 4:5.pdf p.1].

4. **Downward sloping term structure of equity premia**: Consistent with van Binsbergen et al. (2012) and van Binsbergen & Koijen (2017) [Source: stocks 3 4:5.pdf p.1].

5. **Spillover effect**: Expected future dividend payment times of no-dividend stocks affect the prices of ALL stocks, including dividend-paying ones — this is because expected dividend payment times are when stochastic discount factor shocks change [Source: stocks 3 4:5.pdf p.2-3].

### Mechanism

No-dividend stocks introduce three features absent from standard models: (a) information incompleteness — investors must estimate eventual future dividends using Bayesian filtering, inducing additional volatility in the estimated pseudo-dividend; (b) additional uncertainty about future dividend payment periods (Poisson process); (c) no direct contribution to aggregate consumption or the stochastic discount factor. Closed-form solutions for all quantities of interest [Source: stocks 3 4:5.pdf p.1-4].

### Cemini relevance

- **Factor construction**: The structural difference between dividend-paying and no-dividend stock returns means dividend status should be a factor in the 34-dim feature vector — not just as a binary flag but as an interaction term with volatility and beta estimates
- **Regime awareness**: The model's risk premium-volatility relation is non-monotonic (context-dependent), supporting regime-conditional position sizing
- **Watchlist segmentation**: ~35% of stocks are no-dividend historically; their distinct return characteristics warrant separate treatment in screening pipelines

## Snippets

### S1 — Abstract

> "We develop a stationary model of the aggregate stock market featuring both dividend-paying and no-dividend stocks within a familiar, parsimonious consumption-based equilibrium framework. We find that such a simple feature leads to profound implications supporting several stock market empirical regularities that leading consumption-based asset pricing models have difficulty reconciling." [Source: stocks 3 4:5.pdf p.1]

### S2 — No-dividend stock characteristics

> "We also find that no-dividend stocks command lower mean returns but have higher return volatilities and higher market betas than comparable dividend-paying stocks, consistently with empirical evidence." [Source: stocks 3 4:5.pdf p.1]

### S3 — Spillover mechanism

> "The presence of no-dividend stocks generates a novel spillover effect in that the expected future dividend payment times of no-dividend stocks affect the prices of all stocks, including the stocks that pay dividends at all times." [Source: stocks 3 4:5.pdf p.2-3]
