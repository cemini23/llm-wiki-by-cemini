---
title: "Braided and Knotted Stocks (topological finance)"
type: source
tags: [pdf, portfolio-strategy, time-series]
clusters: [portfolio-strategy, time-series]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- Original title: Braided and Knotted Stocks (or similar — SSRN paper, exact title truncated in stub)
- Authors: Ovidiu Racorean
- Affiliation: SSRN-posted independent work
- Type: PDF, SSRN preprint
- Location: research for cemini/stocks 2 4:5.pdf
- Length: ~20 pages
- Retrieved: 2026-04-23
- Publication date: SSRN preprint (abstract=2524847 generation)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: portfolio-strategy, time-series
- Flag: **fringe / speculative** — topological approach to stock cross-sections has no empirical trading track record and the paper provides none.

## Narrative

Racorean applies knot theory and braid-group formalism to stock price cross-sections: treat price paths of multiple stocks as strands in a braid, compute Alexander-Conway and Jones polynomials to classify topological invariants of the resulting "knot," and claim that knot-class transitions correspond to regime changes / rotation events in the equity cross-section. The paper develops the math and shows some pictorial examples on small stock baskets.

The work is **fringe**. There is no backtest, no out-of-sample evaluation, no comparison to standard cross-sectional factor models, and no operational framework for turning Jones-polynomial classifications into actionable positions. Topological data analysis has legitimate applications in finance (persistent homology of correlation matrices, for example), but braid/knot invariants for stock paths is a niche framing with essentially no empirical literature behind it.

For Cemini: **do not cite as methodology**. The paper is kept in the library as an example of a speculative framing, and may be useful as a source on topological-finance terminology if that ever comes up in a conversation, but it should not inform system design. The formal math is correct; the financial claims are unvalidated.

## Key findings

- Applies knot theory (Alexander-Conway, Jones polynomials) and braid groups to multi-stock price paths.
- Claims knot-class transitions correspond to equity regime changes / rotations.
- No backtest, no out-of-sample evaluation, no comparison to standard factor models.
- Fringe framing; topological-finance literature does not use braids/knots as a standard tool.
- Do not use for Cemini methodology — keep as a curiosity, not evidence.

## Snippets

- **abstract** — "We apply knot theory to classify cross-sectional price path topologies" — framing.
- **methodology** — Standard braid-group and Jones-polynomial construction applied to price paths.
- **gap** — No empirical validation, no comparison to existing cross-sectional methods — fringe flag stands.
