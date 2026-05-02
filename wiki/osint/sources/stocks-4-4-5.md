---
title: "Crossing Stocks and the Positive Grassmannian I: The Geometry behind Stock Market (Racorean, 2014 — arXiv)"
type: source
tags: [pdf, arxiv, mathematical-finance, geometry, grassmannian, stock-crossings, permutation-diagrams, exotic-quant]
clusters: [quant-finance]
keywords: [racorean, positive-grassmannian, stock-market-polytope, permutation-diagrams, djia-components, positroid-decomposition, combinatorial-finance]
related:
  - concepts/quant-finance.md
  - entities/ticker-watchlist.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; Racorean's Grassmannian mapping is exotic mathematical finance — beautiful but no actionable Cemini signal
- @entities/ticker-watchlist.md — Cemini watchlist; the DJIA-component stock-crossing representation is a novel encoding of relative-price dynamics, but the geometric framework is too abstract for direct feature-vector integration

## Raw Concept

- **Original title**: Crossing Stocks and the Positive Grassmannian I: The Geometry behind Stock Market
- **Author(s)**: Ovidiu Sorin Racorean (Government of Romania)
- **Type**: PDF (arXiv preprint + SSRN)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/stocks 4 4:5.pdf
- **Published**: February 2014 (arXiv 1402.1281, v1 Feb 6, v2 Feb 9)
- **External IDs**: arXiv:1402.1281; SSRN 2512437
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via scp + PyMuPDF extraction from librarian)
- **Length**: 21 pages, 11 figures
- **Read status**: deep-read

## Narrative

Racorean maps the relative price dynamics of DJIA index components to the mathematical structure of the positive Grassmannian — a combinatorial-algebraic object also used in theoretical physics (on-shell scattering amplitudes in N=4 super Yang-Mills). The paper constructs a bridge between finance and algebraic geometry that is intellectually striking but operationally thin.

### Key findings

1. **Stock crossing = permutation**: When DJIA components are arranged in ascending price order, any price change that causes one stock to overtake another is a "crossing." The diagram of successive crossings forms a permutation diagram [Source: stocks 4 4:5.pdf p.1-3].

2. **Stock market polytope**: The permutation diagram of stock crossings maps to a geometrical object — the "stock market polytope" — associated with the positive Grassmannian G⁺(k,n) [Source: stocks 4 4:5.pdf p.1-2].

3. **Positroid decomposition**: The stock market polytope admits a decomposition into positroid cells, each corresponding to specific crossing patterns. This provides a combinatorial classification of relative-price dynamics [Source: stocks 4 4:5.pdf p.1].

4. **"Part I" implies planned sequels**: The paper's title includes "I" — the author planned follow-up work. No Part II appears to have been published on arXiv as of 2026.

### Cemini relevance

**Very low**. Beautiful mathematics, but the Grassmannian framework is too abstract for direct Cemini feature-vector integration. The core insight — that relative-price ordering of index components encodes information — could inspire a simpler permutation-based feature (e.g., rank correlation of component prices over time), but the full geometric machinery is not operationally useful.

## Snippets

### S1 — Abstract

> "It seems to be very unlikely that all relevant information in the stock market could be fully encoded in a geometrical shape. Still…the present paper will reveal the geometry behind the stock market transactions. The prices of market index (DJIA) stock components are arranged in ascending order from the smallest one in the left to the highest in the right... The stock market polytope is associated with the remarkable structure of positive Grassmannian." [Source: stocks 4 4:5.pdf p.1]

### S2 — Core mapping

> "Every time the price of a stock in an index go up or under its neighbor price... the two stocks permute." [Source: stocks 4 4:5.pdf p.3]
