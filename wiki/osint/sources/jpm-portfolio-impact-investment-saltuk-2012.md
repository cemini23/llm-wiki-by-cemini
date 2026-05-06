---
title: "A Portfolio Approach to Impact Investment (J.P. Morgan, Saltuk + El Idrissi, 2012)"
type: source
tags: [methodology-reference, portfolio-management, impact-investing, off-domain-methodology, financial-research]
keywords: [impact-investing, portfolio-theory, three-dimensional-mapping, target-profile, aggregate-portfolio, jp-morgan-social-finance, ESG-portfolio]
related:
  - concepts/prediction-market-historical-analysis.md
  - entities/tools/riskfolio-lib.md
  - entities/tools/financetoolkit.md
maturity: validated
read_status: skimmed
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @concepts/prediction-market-historical-analysis.md — JP Morgan's 3-D mapping pattern (target profile → individual investments → aggregate vs target) is a venue-agnostic portfolio-management framework that could supplement Cemini's eventual prediction-market backtest pipeline if a third axis (impact / conviction / regime exposure) becomes load-bearing
- @entities/tools/riskfolio-lib.md — Cemini's existing convex portfolio optimization library; covers traditional 2-D (return × risk) cleanly. JPM's 3-D framing is the next conceptual step IF a third axis emerges.
- @entities/tools/financetoolkit.md — companion fundamentals library; pairs with this paper's "define financial parameters" step

## Raw Concept

- Original title: A Portfolio Approach to Impact Investment — A Practical Guide to Building, Analyzing and Managing a Portfolio of Impact Investments
- Authors: Yasemin Saltuk, Ali El Idrissi
- Publisher: J.P. Morgan Securities plc, Global Social Finance
- Date: 01 October 2012 (older paper; methodology has evolved since but the framework is conceptually timeless)
- Pages: 48
- Location: cemini-librarian:/opt/cemini-bulk/research/121001_A_Portfolio_Approach_to_Impact_Investment.pdf
- Retrieved: 2026-05-05
- Read status: skimmed (executive summary + section structure + key frameworks; deep-read deferred — this is reference material)

## Narrative

A practical guide for building, analyzing, and managing **impact-investment portfolios** — i.e., portfolios where investors target social/environmental impact alongside financial return. JPM's research draws on their own portfolio + interviews with 23 institutional impact investors. The load-bearing innovation: **3-dimensional portfolio analysis** (impact + return + risk) where traditional portfolio theory uses 2 dimensions (return + risk).

### Why this paper is in the corpus despite being off-domain

Cemini's primary research focus is prediction-market and equity trading (per `@memory/prediction_market_scope`: sports / healthcare / politics / weather / economic indicators). Impact investing / ESG is a different vertical. **However**, the paper's methodology has transfer value:

1. **3-D portfolio mapping framework** — venue-agnostic. Cemini could repurpose the third axis as `conviction-tier` or `regime-exposure` or `thesis-coherence` for prediction-market portfolio analysis. The framing (target profile → individual investments → aggregate vs target → identify gaps) is reusable.

2. **Risk-management taxonomy** — JPM categorizes risk into structural features + friction-between-impact-and-return. The "friction" concept generalizes: anywhere two competing portfolio objectives exist, the friction-management techniques apply. Cemini's existing risk discipline (kill-switch + position-sizing per `@briefs/2026-05-04_probablyprofit-pattern-extraction.md`) maps onto the structural-features side.

3. **Hub-spoke organizational pattern** — for managing multi-instrument portfolios via a centralized impact team partnering with various portfolio managers across instrument types. Could inform Cemini's eventual multi-strategy bundling architecture (per `@concepts/polymarket-market-making-architectures.md` Posture 4).

4. **Sourcing-deals discipline** — section on iterative deal sourcing maps onto Cemini's K-series ingest discipline at the meta-level (curating a pipeline of candidate research / tools / patterns).

### Section structure

| § | Topic |
|---|-------|
| 1 | Portfolio Theory for Impact Investment (extending traditional 2-D theory) |
| 2 | Building an Impact Investment Portfolio (find a home, define impact thesis, financial parameters, focus + diversification, sourcing) |
| 3 | Framework for Impact, Return & Risk (target profile mapping, individual mapping, aggregate mapping + comparison) |
| 4 | Financial & Impact Risk Management (risk taxonomy, structural features, friction management, diversification) |
| 5 | Looking Forward |
|   | Appendices + Acknowledgements |

### Cemini-side application — speculative + deferred

This paper does NOT trigger a near-term Cemini workstream. Treatment: **reference shell** like `@sources/rl-overview-murphy-2412-05265.md` (Murphy RL Overview from K30). The 3-D mapping framework would only become operationally useful if/when:
- Cemini's prediction-market portfolio crosses into ESG-themed event contracts (e.g., climate / carbon / social-impact contracts on Polymarket or Kalshi)
- Cemini's portfolio-management discipline needs a third axis beyond return/risk — e.g., when conviction-tier diversification or regime-exposure mapping becomes a load-bearing concern

If either trigger fires, deep-read § 3 (Framework for Impact, Return & Risk) and re-derive the mapping for Cemini's specific axes.

### What we don't take

- The specific impact-investing examples (clean water, affordable housing, etc.) are off-domain
- The institutional-investor interview synthesis is JPM's competitive insight from 2012; no direct Cemini relevance
- The financial parameters discussion is conventional public/private-equity portfolio sizing — Cemini's prediction-market sizing already lives in `@entities/tools/riskfolio-lib.md` (Kelly + HRP) and `@briefs/2026-05-04_probablyprofit-pattern-extraction.md` (ensemble consensus)

### Status: cited but unread

Per `@sources/rl-overview-murphy-2412-05265.md`'s chapter-promotion-discipline pattern: this stub is intentionally a reference shell. Promote § 3 to deep-read status only when an operational trigger fires (see "Cemini-side application" above). Until then, the paper sits in the corpus as a citable foundation for portfolio-management discussions.

## Snippets

- **3-D framing** (Executive Summary): "This research presents a tool to analyze impact investments across the three dimensions that determine the performance of these assets: impact, return and risk." [Source: jpm-portfolio-impact-investment-saltuk-2012.pdf p.4]

- **Hub-spoke organizational pattern** (Executive Summary): "Some investors establish a separate portfolio with its own management team while others employ a 'hub-spoke' strategy where a centralized impact team partners with various portfolio managers across instrument types (such as fixed income and equity) to manage the portfolio's multiple dimensions." [Source: jpm-portfolio-impact-investment-saltuk-2012.pdf p.4]

- **Iterative-process framing**: "Today, impact portfolio construction is an iterative process." [Source: jpm-portfolio-impact-investment-saltuk-2012.pdf §2 — exact page TBD on deep-read]

- **Risk taxonomy (§4)**: structural features vs friction-between-impact-and-return. The friction concept generalizes to any two-competing-objectives portfolio. [Source: jpm-portfolio-impact-investment-saltuk-2012.pdf §4]

## Dead Ends

*(none yet — reference material; deep-read deferred per chapter-promotion discipline.)*
