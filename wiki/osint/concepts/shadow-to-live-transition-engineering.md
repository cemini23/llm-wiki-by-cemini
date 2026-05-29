---
title: Shadow-to-live transition engineering — rate limits, canary, and state replication
type: concept
tags: [concept, cemini-internal, live-trading, deployment, infrastructure, k76]
keywords: [shadow-execution, canary, HTTP-429, preflight, token-bucket, Aeron, logic_version]
related:
  - sources/algorithmic-trading-live-transition-strategies-2026-05-28.md
  - sources/3-19-live-transition-checklist.md
  - sources/3-10-live-trading-research.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/pnl-attribution-versioning.md
  - concepts/production-trading-blind-spots.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/cemini-repository-topology.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - concepts/clob-rate-limit-mitigation-strategies.md
  - concepts/shadow-trading-telemetry-accumulation.md
  - sources/quant-bot-lp-live-promotion-criteria-2026-05-28.md
  - concepts/polymarket-lp-rewards-farming.md
  - sources/clob-rate-limit-mitigation-strategies-2026-05-28.md
  - sources/shadow-trading-data-accumulation-strategies-2026-05-28.md
maturity: validated
created: 2026-05-28
updated: 2026-05-29
---

## Relations

- @sources/algorithmic-trading-live-transition-strategies-2026-05-28.md — primary source (K76 deep-read)
- @sources/3-19-live-transition-checklist.md — earlier internal checklist (skim)
- @sources/3-10-live-trading-research.md — execution state amnesia audit
- @concepts/lp-algorithm-live-promotion-gates.md — LP shadow incubation uses same pipeline
- @concepts/pnl-attribution-versioning.md — bump `logic_version` at live cutover
- @concepts/production-trading-blind-spots.md — Knight / 429 as deployment blind spots
- @concepts/trading-bot-logging-discipline.md — log quota headers + shadow intent timestamps
- @concepts/cemini-repository-topology.md — prod monorepo deploy; briefs → `/opt/cemini/briefs/`
- @concepts/clob-rate-limit-mitigation-strategies.md — WS-first + 429 preflight (K77)
- @concepts/shadow-trading-telemetry-accumulation.md — dual-track counterfactual logging (K77)

## Raw Concept

K76 ingest synthesis: how to promote strategies from **shadow** (real feeds, no capital) to **live** without rate-limit death or state divergence. Complements K75 PnL versioning — transition is both **operational** (API quotas) and **attribution** (registry bump).

## Narrative

### Shadow vs paper

| Mode | Data | Orders | Measures |
|------|------|--------|----------|
| Backtest | Historical | Simulated fills | Alpha hypothesis |
| Paper | Often delayed/synthetic | Sim matcher | UX / rough PnL |
| **Shadow** | Live feeds | Suppressed or dry-run | Request rate, latency, state parity |
| Live | Live feeds | Real capital | PnL + risk |

Cemini should treat PM/Kalshi **paper** paths as shadow-capable: record `would_send_at` + quota headers even when not posting.

### Promotion pipeline (minimal)

1. **Shadow window** — minimum duration + event coverage (include volatile days).
2. **429 preflight** — parse venue weight headers; simulate token-bucket from shadow POST rate; block cutover if p99 utilization > safety margin.
3. **Canary / dual-run** — candidate vs incumbent on same tick stream until order-intent parity (or bounded divergence documented).
4. **Registry bump** — new `version_id` in `cemini_contracts/strategy_logic_versions.py` at live switch (@concepts/pnl-attribution-versioning.md).
5. **Kill switch drill** — fire before live, not after first loss.

### Rate-limit engineering

- Prefer **batch/coalesce** (LMAX Disruptor pattern) over naive per-tick REST when venue supports batch endpoints.
- Honor **Retry-After** on 429; never spin — Binance-class venues escalate to IP ban (418).
- Log `X-MBX-*` or venue analog on every shadow response for preflight dashboards.

### When *not* to go live

- Shadow order rate exceeds quota at expected live size.
- State machine diverges from incumbent on same replay log.
- Zero-trade abort domain unknown (@concepts/zero-trade-edge-signal-diagnostics.md).

## Snippets

> Knight Capital 2012: improperly decommissioned code paths → $440M-class loss in ~30 minutes — deployment failure, not alpha failure. [Source: algorithmic-trading-live-transition-strategies-2026-05-28.docx]

> HTTP 429 during defensive sells in a flash crash — correct signal, rejected orders. [Source: algorithmic-trading-live-transition-strategies-2026-05-28.docx — [TENTATIVE] anecdote]
