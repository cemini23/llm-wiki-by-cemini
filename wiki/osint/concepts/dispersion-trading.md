---
title: Dispersion trading
type: concept
tags: [concept, options, volatility, strategy]
keywords: []
related:
  - sources/trading-playbook-research.md
  - concepts/macro-weather-regime.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/trading-playbook-research.md
- @concepts/macro-weather-regime.md
- @entities/components/kelly-cvar-risk-engine.md

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RETRACTED — 2026-04-24 Track C audit]** Dispersion trading as named is **not implemented**. `grep` for `dispersion|spx_dispersion` across `.py` files (excl. `.worktrees/`) → 0 hits. General options-math utilities exist (`options_greeks/__init__.py`, `options_greeks/black_scholes.py`, `options_greeks/binary_greeks.py`, `cemini_contracts/options.py`, `tests/test_options_greeks.py`) but there is **no SPX constituent universe file, no vega-matching code, no short-index-long-names strategy module**. GREEN-gating exists for regime (see @concepts/macro-weather-regime.md) but no dispersion strategy is attached to it. Wiki synthesized research-doc language as if the strategy were shipped. No near-term ticket (P3 — build only if acquirer narrative requires it). Gap memo: `briefs/track-c-walk-results.md`.

Original claimed narrative retained below as retracted-claim-of-record.

---

**Dispersion trading** sells index-level implied volatility while buying
single-name implied volatility on the constituent basket. The P&L
source is the gap between implied index vol (usually rich, due to
correlation premium) and the realized dispersion across names.

### Cemini's implementation per the trading-playbook research
- Universe: SPX components via liquid options on the top ~50 weights.
- Weights: vega-matched; index-short leg sized to ~1% of NAV vega-
  weighted.
- Gating: **Macro Weather GREEN only**. In YELLOW/RED, correlations
  spike, dispersion collapses, and the trade bleeds theta without
  the usual realized-dispersion payoff. This gating is cited as the
  empirical distillation of why retail dispersion traders blow up in
  drawdowns — they don't gate on regime.
- Hedging: dynamic delta + vega re-hedge, driven by the scatter-
  gather analyst that digests FRED + GDELT + cross-asset cues and
  emits a regime-confidence score.

### Institutional interest
Dispersion is explicitly called out in the IP-sale research as one
of the **highest-value strategies** in the Cemini portfolio for the
institutional-buyer archetype — complex enough to demand real
options-vol infrastructure, simple enough to explain to a risk
committee, and capacity-scalable up to the buyer's own book size.

## Snippets

*(populate as source stubs are deep-read.)*
