---
title: Macro Weather regime
type: concept
tags: [concept, cemini-internal, risk, regime]
keywords: []
related:
  - sources/trading-playbook-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-compliance-research.md
  - concepts/ip-sale-readiness.md
  - concepts/game-of-attrition-doctrine.md
  - entities/data-sources/fred.md
  - entities/components/kelly-cvar-risk-engine.md
  - concepts/dispersion-trading.md
  - entities/platforms/oanda.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/trading-playbook-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-compliance-research.md
- @concepts/ip-sale-readiness.md
- @concepts/game-of-attrition-doctrine.md
- @entities/data-sources/fred.md
- @entities/components/kelly-cvar-risk-engine.md
- @concepts/dispersion-trading.md
- @entities/platforms/oanda.md
- @entities/platforms/kalshi.md

## Raw Concept

Synthesized across 3 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[CONFIRMED — 2026-04-24 Track C audit]** Regime gate is real and enforced at the top of the stack. Evidence:
- `agents/regime_gate.py` — exports `REGIME_THRESHOLDS`, `CATALYST_PATTERNS`, `CATALYST_BONUS`, `_regime_gate`, `_REGIME_FALLBACK`.
- `cemini_contracts/regime.py` — typed Pydantic contract.
- `agents/orchestrator.py:16-22` imports the regime symbols and calls regime evaluation **before** signal processing.
- `intel:playbook_snapshot` Redis key (published by `trading_playbook/runner.py`) carries regime state; consumed by `cemini_mcp/server.py` tool #1 `get_regime_status`, `services/conviction_aggregator.py`, RL training, and regression tests.
- `tests/test_regime_gate.py` — coverage.
- Three-regime threshold structure observable at `regime_gate.py` lines 44–46: BUY/SELL/SHORT thresholds vary per regime.

No ticket required.

The **Macro Weather regime** is Cemini's simple, auditable portfolio-
gate classifier. It uses two signals on SPY — the 21-EMA and the
50-SMA — cross-referenced with a small set of FRED macro series, to
produce one of three regime states:

- **GREEN**: SPY > 21-EMA AND SPY > 50-SMA. Permissive regime. Full
  Kelly fraction allowed; new risk may be added.
- **YELLOW**: price between 21-EMA and 50-SMA (either side). Defensive.
  Kelly fraction halved; no new uncorrelated risk; existing positions
  tightened.
- **RED**: SPY < 21-EMA AND SPY < 50-SMA. Flat-or-hedge-only. All
  directional risk flattened or hedged; only market-making style
  strategies (Kalshi AS-in-logit, forex scalping) continue.

### Why these two moving averages
The trading-playbook research argues, and several RL-based regime
classifiers confirm in ablations, that 21-EMA captures ~1-month trend
and 50-SMA captures ~2.5-month trend; their crossover vs price
together identifies three distinct drawdown-risk regimes without
over-fitting.

### Why it sits at the top of the stack
The regime classifier is evaluated **before** the Kelly/CVaR risk
engine, which is evaluated **before** the strategy-specific signal.
This inverts the usual strategy-first → risk-second ordering and is
framed in the corpus as the **Game of Attrition doctrine**: survive
first, compound second. The regime flag is cheap to compute,
auditable, and caps all downstream risk — which is exactly what an
IP-sale buyer wants to see at the top of the stack.

## Snippets

*(populate as source stubs are deep-read.)*
