---
title: Macro Weather regime
type: concept
tags: [concept, cemini-internal, risk, regime]
keywords: []
related:
  - concepts/xsp-lane-trading-framework.md
  - sources/macro-charts-paid-forward-2026-08-03-everything-is-about-to-change.md
  - sources/macro-charts-paid-forward-2026-08-02-everything-is-about-to-change.md
  - sources/substack-rss-klement-2026-07-13-when-regulation-is-good-for-business.md
  - sources/macro-charts-paid-forward-chat-2026-07-10.md
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
  - concepts/carry-trade.md
  - concepts/valuation-hypersensitivity-macro-liquidity.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/markov-regime-switching-models.md
  - concepts/gmm-factor-lens-regime-modeling.md
  - sources/two-sigma-gmm-regime-modeling-street-view-2021.md
  - concepts/macro-rotation-momentum-signals-2026-05.md
  - concepts/macro-charts-regime-signals.md
  - concepts/macro-charts-gold-reversal-thesis-2026-06.md
  - concepts/macro-charts-sox-tech-correction-watch-2026-06.md
  - concepts/capital-flows-sofr-conviction-framework.md
  - concepts/reviewer-passive-injection-corpus.md
  - sources/macro-charts-paid-forwards-vincent-2026-06-22-07-05.md
  - sources/trading-posts-compilation-16-2026-05-31.md
maturity: validated
created: 2026-04-23
updated: 2026-07-13
---

## Relations

- @concepts/xsp-lane-trading-framework.md — XSP dip lanes exception to portfolio Macro Weather Kelly gate
- @sources/macro-charts-paid-forward-2026-08-03-everything-is-about-to-change.md — K221 paid forward
- @sources/macro-charts-paid-forward-2026-08-02-everything-is-about-to-change.md — K218 RSS teaser (superseded)
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
- @concepts/carry-trade.md — carry trade sizing is gated by Macro Weather regime: disabled in RED, half-sized in YELLOW, full-sized in GREEN.
- @concepts/valuation-hypersensitivity-macro-liquidity.md — record-valuation sensitivity framing for regime transitions (K236)
- @concepts/reviewer-passive-injection-corpus.md — K37 reviewer bundle cites Macro Weather as **context**, not universal XSP entry gate
- @concepts/markov-regime-switching-models.md — sibling regime concept: Markov/HMM detects the regime statistically; Macro Weather is the macro-state framing
- @concepts/gmm-factor-lens-regime-modeling.md — K58 reference taxonomy (Crisis / Steady State / Inflation / WOI); not wired to prod Macro Weather without validation
- @sources/two-sigma-gmm-regime-modeling-street-view-2021.md — K58 source

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

### XSP lane exception (K37 reviewer / long-call playbook)

Macro Weather still gates **brain/orchestrator** paths and **Kelly fraction**
sizing at the portfolio level. **XSP long-call lanes are not universal
GREEN-only entry:**

| Lane | Regime posture |
|------|----------------|
| **Lane B (LEAPS)** | **Accumulate on dips** — entries may fire in **YELLOW/RED** when dip rubric triggers |
| **Lane A (tactical)** | Regime informs sizing/alerts; not a hard GREEN-only block |
| **K37 reviewer** | Must **not** refuse `place_order` solely because regime ≠ GREEN |

See @concepts/xsp-lane-trading-framework.md and `conductor/reviewer/policy.yaml`
`regime_entry_policy` block. Prod `agents/regime_gate.py` BUY blocks on
YELLOW/RED apply to **orchestrator** paths — XSP EMS manual/dip entries
use lane-specific YAML, not a blanket portfolio gate.

### External overlay — USDJPY yen-strength zone (K155)

Macro Charts Jul 10 chat (`@sources/macro-charts-paid-forward-chat-2026-07-10.md`) flags **USDJPY 162.25–162.50** as the clearest medium-term FX R/R zone amid Japan GPIF domestic-allocation / yen-strength narrative.

| Field | Posture |
|-------|---------|
| **Role** | **Advisory** macro-weather snapshot input — yen-strength / international macro context for **Lane B** dip framing |
| **Not** | A GREEN/YELLOW/RED gate substitute; does not block or permit XSP entries by itself |
| **Operator** | Log zone in `playbook_snapshot` comment block or trade journal when GPIF/yen headlines active |
| **CPI cluster** | Pair with Jul 15 CPI tighten on Lane A overnight size (`@concepts/macro-charts-gold-reversal-thesis-2026-06.md`) |

See also `@concepts/macro-charts-regime-signals.md` § Jul 10 2026.

## Snippets

*(populate as source stubs are deep-read.)*
