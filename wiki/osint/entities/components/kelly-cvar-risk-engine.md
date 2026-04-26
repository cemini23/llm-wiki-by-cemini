---
title: Kelly/CVaR risk engine
type: entity
tags: [component, cemini-internal, risk, position-sizing]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/trading-playbook-research.md
  - concepts/macro-weather-regime.md
  - concepts/ip-sale-readiness.md
  - concepts/dispersion-trading.md
  - concepts/game-of-attrition-doctrine.md
  - concepts/replacement-cost-valuation.md
  - sources/3-19-live-transition-checklist.md
  - sources/3-5-git-pt-2.md
  - sources/captum-re-4-3-2.md
  - sources/cost-effective-algorithmic-trading-api-stack.md
  - sources/crypto-13-4-11.md
  - sources/greeks-10-3-29.md
  - sources/greeks-2-3-29.md
  - sources/greeks-3-3-29.md
  - sources/greeks-4-3-29.md
  - sources/greeks-6-3-29.md
  - sources/greeks-7-3-29.md
  - sources/greeks-8-3-29.md
  - sources/greeks-9-3-29.md
  - sources/greeks1-3-29.md
  - sources/options-2-4-5.md
  - sources/options-4-5.md
  - sources/sort-5-4-3.md
  - sources/sort-7-4-3.md
  - sources/sortino-3-4-3.md
  - sources/ssrn-3247865.md
  - sources/stocks-2-4-5.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-19-compliance-research.md — Kalshi DCM "self-limit system load" mandate; Kelly/CVaR + TCP/IP congestion governor cited as the architectural mitigation
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/trading-playbook-research.md
- @concepts/macro-weather-regime.md
- @concepts/ip-sale-readiness.md
- @concepts/dispersion-trading.md
- @concepts/game-of-attrition-doctrine.md
- @concepts/replacement-cost-valuation.md

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: components.

## Narrative

The Kelly/CVaR risk engine is Cemini's position-sizing and
portfolio-risk module. It combines a **fractional-Kelly sizer**
(typically 0.1–0.3 Kelly to control drawdown variance) with a
**CVaR-95% cap** (the position is clipped if it would push expected
5%-tail loss above a configured threshold).

Invocation pattern across the corpus:
- Every strategy emits a target position + a signal-edge estimate.
- The risk engine computes Kelly-optimal size from the edge + the
  strategy-specific variance estimate.
- A portfolio-level CVaR recalc runs after each candidate position
  change; any candidate that breaches the portfolio CVaR budget is
  clipped or rejected.
- The Macro Weather regime gate sits **in front of** the risk engine:
  GREEN → full Kelly fraction; YELLOW → halved; RED → flat-or-hedge-
  only.

Flagged explicitly as Cemini-proprietary in the IP-sale research —
the combination of regime-gating + Kelly/CVaR + LangGraph-logged
reasoning is the piece institutional buyers cannot easily recreate
from open-source primitives, and so commands the premium valuation.

## Snippets

*(populate as source stubs are deep-read.)*
