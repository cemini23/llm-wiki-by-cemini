---
title: "OpenTrader (Open-Trader/opentrader) — modern TypeScript open-source crypto algo-trading framework"
type: entity
tags: [entity, tool, algorithmic-trading, crypto, typescript, ccxt, apache-2, gridbot, dca, rsi, k56]
keywords: [opentrader, open-trader, ccxt, gridbot, dca, rsi, typescript-trading-framework, apache-2-license, ip-sale-clean, node-js, pino-logger-issue]
related:
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - entities/tools/freqtrade.md
  - concepts/cemini-license-posture.md
  - entities/tools/superalgos.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
phase_0_verdict: REFERENCE-ELIGIBLE — Apache-2 license is IP-sale-clean; not currently a Cemini adoption target (we don't trade crypto spot), but qualifies as a structural reference for any future Cemini IP-sale-clean algo-trading framework
---

## Relations

- @sources/analyzing-github-projects-agentic-infra-2026-05-21.md — primary source
- @entities/tools/freqtrade.md — legacy Python counterpart
- @concepts/cemini-license-posture.md — Apache-2.0 clears the IP-sale perimeter

## Raw Concept

What prompted this page: K56 Analyzing GitHub Projects report. OpenTrader is positioned as the modern (TypeScript) counterpart to Freqtrade (Python). License-clean for IP-sale.

- URL: `https://github.com/Open-Trader/opentrader`
- License: **Apache-2.0**
- Stars: ~2,600 (per source)
- Language: TypeScript / Node.js
- Install: NPM

## Narrative

**OpenTrader** is the TypeScript-native open-source crypto algo-trading framework. It positions itself against Freqtrade (Python, GPL-3) on three axes: language ecosystem (Node.js vs Python), license (Apache-2 vs GPL-3), and built-in strategies (GridBot / DCA / RSI ready-to-run vs Freqtrade's "bring-your-own-strategy" + Hyperopt).

### Architecture (per source)

- Robust user-friendly management UI
- Cross-exchange arbitrage support
- Event-based strategy execution
- CCXT for exchange normalization (~100+ venues)
- Built-in **GridBot**, **DCA** (dollar-cost averaging), and **RSI** strategies

### Known limitations (per source)

- **Pino logger issue**: asynchronous `worker.js` artifacts affect the `pino` logger, complicating bundling. Issue #46 references replacing pino with an alternative.

### Cemini relevance

**Reference-eligible** under three conditions:

1. **License**: Apache-2.0 clears the @concepts/cemini-license-posture.md IP-sale gate.
2. **Stack alignment**: TypeScript is consistent with cemini-egress-fi's gateway implementation pattern. (Cemini-prod's bot stack is mostly Python, but cross-language interop via JSON-RPC is precedent.)
3. **Strategy reusability**: GridBot logic in OpenTrader maps cleanly onto Polymarket LP-range placement (@concepts/polymarket-lp-rewards-farming.md) — the multi-price-level position pattern is structurally similar. Worth a clean-room read if we ever extend the LP-farming strategy to multi-market dynamic rebalancing.

Not currently an adoption target — Cemini's Polymarket focus is the binding constraint, not exchange-side strategy maturity. But if the scope ever extends to Hyperliquid spot or perpetuals execution, OpenTrader's CCXT-derived adapters and GridBot patterns are the natural reference.

### Comparison vs Freqtrade

See @entities/tools/freqtrade.md for the table. Summary: OpenTrader wins on license + stack alignment; Freqtrade wins on strategy ecosystem depth and Hyperopt sophistication.

### Phase-0 follow-ups (deferred — no immediate adoption)

If OpenTrader becomes a serious adoption candidate:

1. Verify Apache-2.0 license via `gh api repos/Open-Trader/opentrader/license` (per K53/K54/K55 pattern of secondary-source license-detection unreliability).
2. Audit the CCXT version pin — CCXT itself is MIT but its transitive dependencies vary.
3. Inspect maintainer activity / bus-factor; pmxt's "single-maintainer bus-factor-1" condition (@entities/tools/pmxt.md) is a precedent we apply broadly.

## Dead Ends

- Star count and license are secondary-source; verify before any serious adoption work.
- Without Hyperopt-equivalent, OpenTrader's strategy-tuning story is weaker than Freqtrade's. If we need parameter optimization (LP-range spacing, stop-loss thresholds, etc.), we'd either build it ourselves or borrow from Freqtrade (clean-room re-implementation, given the license incompatibility).
