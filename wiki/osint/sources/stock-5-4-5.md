---
title: "Extreme Stock Market Performers, Part II: Do Technology Stocks Dominate? (Bessembinder, 2020)"
type: source
tags: [pdf, academic, quant-finance, extreme-performers, technology-stocks, long-horizon-returns, sector-analysis, shareholder-wealth]
clusters: [quant-finance]
keywords: [bessembinder, extreme-stock-performers, technology-stocks, decade-horizon-returns, shareholder-wealth-creation, sector-composition, crsp, asu]
related:
  - concepts/quant-finance.md
  - entities/ticker-watchlist.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; Bessembinder's extreme-performer trilogy is the canonical reference on long-horizon stock return concentration — directly relevant to factor selection and watchlist construction
- @entities/ticker-watchlist.md — Cemini watchlist; the sector-composition findings (Tech overrepresented among worst performers, Healthcare/Energy among best) inform sector-based screening priors

## Raw Concept

- **Original title**: Extreme Stock Market Performers, Part II: Do Technology Stocks Dominate?
- **Author(s)**: Hendrik Bessembinder (W.P. Carey School of Business, Arizona State University)
- **Type**: PDF (academic paper, SSRN)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/stock 5 4:5.pdf
- **Published**: July 2020
- **External IDs**: SSRN 3657609
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via scp + PyMuPDF extraction from librarian)
- **Length**: 15 pages
- **Read status**: deep-read
- **Note**: Part II of a trilogy. Part I (SSRN 3657604) covers drawdowns; Part III (SSRN 3657611) covers observable characteristics of extreme performers.

## Narrative

Bessembinder examines the industry composition of the best- and worst-performing stocks at the decade horizon, using 26,285 firm/decades from 1950 onward (CRSP + Compustat data). The paper is the second in a trilogy that began with the finding that just 83 firms (0.32%) accounted for half of all net shareholder wealth creation from 1926-2019 ($47 trillion).

### Key findings

1. **Technology stocks disappoint in aggregate**: Despite stellar performance of AAPL, AMZN, MSFT, and GOOGL, Technology stocks as a group are more likely to appear on the list of WORST rather than best performers at the decade horizon. Hundreds of tech firms have disappointed shareholders [Source: stock 5 4:5.pdf p.1-3].

2. **Best-performing sectors**: Healthcare/Pharmaceutical, Energy, and Telecommunications firms are disproportionately represented among the best decade-horizon stock returns [Source: stock 5 4:5.pdf p.1].

3. **Telecommunications dual**: Telecom stocks are also overrepresented among the WORST performers — a dual outcome pattern [Source: stock 5 4:5.pdf p.1].

4. **Methodology**: 11 industry groups based on SIC codes (Kenneth French definitions + Finance broken out separately). "Top 200" and "Bottom 200" by decade, measured by both cumulative shareholder returns and dollar wealth creation — 1,400 observations each across 7 decades [Source: stock 5 4:5.pdf p.2-3].

5. **Context**: The original Bessembinder (2018) finding — that the entire net wealth creation of the US stock market is attributable to ~4% of stocks — provides the backdrop. This Part II examines which industries those extreme performers come from.

### Cemini relevance

- **Sector screening**: The finding that Healthcare/Pharma and Energy dominate best-performers while Tech dominates worst-performers is a prior for sector-based screening in the watchlist
- **Survivorship bias awareness**: The publicity around a few tech giants masks the poor aggregate performance of the tech sector — relevant when evaluating any strategy that overweights tech
- **Concentration risk**: Reinforces the Bessembinder (2018) concentration finding — extreme outcomes are the norm, not the exception; diversification is essential

## Snippets

### S1 — Core finding

> "Despite the stellar performance of investments in firms such as Apple, Amazon, and Microsoft, Technology stocks as a group are more likely to appear on a list of the worst rather than best performers. Telecommunications, Healthcare/Pharmaceutical, and Energy firms are disproportionately represented among those with the best decade-horizon stock returns." [Source: stock 5 4:5.pdf p.1]

### S2 — Concentration context

> "Just eighty-three firms (0.32% of total) accounted for half, and five firms (0.02% of the total) accounted for 11.9%, of net shareholder wealth improvement during this 94-year period." [Source: stock 5 4:5.pdf p.1]
