---
title: Game-of-Attrition doctrine
type: concept
tags: [concept, strategy, risk-philosophy, cemini-internal]
keywords: []
related:
  - sources/trading-playbook-research.md
  - concepts/macro-weather-regime.md
  - concepts/ip-sale-readiness.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/trading-playbook-research.md
- @concepts/macro-weather-regime.md
- @concepts/ip-sale-readiness.md
- @entities/components/kelly-cvar-risk-engine.md

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[TENTATIVE — 2026-04-24 Track C audit]** Two of the three ordering rules are enforced in code; the third (CVaR cap) is computed and displayed but **not enforced as a gate**. The ordering as built is **regime → Kelly → (display-only CVaR)**, not a three-way gate. Ticket (**P1**): *Promote CVaR-95 from display metric to pre-trade gate* — `risk_governor/governor.py` (176 lines, kill-switch primitives) is the right place to add the gate, or a new middleware layer. Closes the biggest gap in the acquirer doctrine narrative. Gap memo: `briefs/track-c-walk-results.md`.

The **Game of Attrition doctrine** is the risk-philosophy framing that
runs through the trading-playbook research: in an infinite-horizon
compounding game, survival dominates expected return. The doctrine
prescribes three operating rules:

1. **Regime gate before signal** `[CONFIRMED 2026-04-24]` — the Macro Weather classifier
   decides whether the portfolio trades at all before any strategy-
   specific signal is evaluated. Losing strategies survive RED by
   being flat; a winning strategy in the wrong regime is still a
   losing strategy. *Real: `agents/regime_gate.py` + `agents/orchestrator.py:16-22`. See @concepts/macro-weather-regime.md.*
2. **Fractional Kelly by default** `[CONFIRMED 2026-04-24]` — never full Kelly. 0.1–0.3
   Kelly reduces expected growth modestly but slashes drawdown
   volatility enough that the LLN grinds in your favor over
   realistic sample paths. *Real: `core/sae_middleware.py:203` reads `SAE_KELLY_FRACTION` env var (default 0.25); referenced in `core/ems/router.py`; used in `agents/orchestrator.py:327` (`kelly_factor` logged).*
3. **CVaR cap on top** `[TENTATIVE 2026-04-24]` — ~~even fractional Kelly can pick up tail risk
   the sizer doesn't see. The portfolio CVaR-95% cap bounds the
   worst-case outcome per bet independent of the Kelly math.~~ *CVaR-95/99 is **computed and surfaced** (via `cemini_mcp/readers.py:131`, `cemini_mcp/server.py:182` tool #3 `get_risk_metrics`, `ui/performance.py:669`, `ui/replay.py:220`) but is **not enforced as a pre-trade gate**. `risk_governor/governor.py` explicitly states "ZERO dependencies on: the brain / LangGraph / the playbook … Only knows about: hard limits, current P&L, order counts, and time" — it's a kill-switch, not a CVaR-clip. The third leg of the doctrine is currently observational. See P1 ticket above.*

### Why it's Cemini's North Star
The doctrine is explicitly positioned in the trading-playbook research
as the organizing principle that makes Cemini defensibly different
from strategy-first prop shops. An acquirer's risk committee reads
"regime → Kelly → CVaR" at the top of the stack and immediately
understands that blow-up scenarios are structurally bounded — which is
the single biggest unlock for the IP-sale price ceiling.

## Snippets

*(populate as source stubs are deep-read.)*
