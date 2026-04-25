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
maturity: validated
created: 2026-04-23
updated: 2026-04-24
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
