---
title: Trading bot logging discipline — structured events without drowning signal
type: concept
tags: [concept, observability, logging, operations, trading-bot, cemini-prod, k75]
keywords: [structured-logging, structlog, json-logs, over-logging, hot-path, queue-handler, loki, grafana, event-names, correlation-id]
related:
  - concepts/production-trading-blind-spots.md
  - concepts/pnl-attribution-versioning.md
  - concepts/polymarket-bot-architecture.md
  - entities/infrastructure/cemini-stack.md
  - concepts/trading-dashboard-api-wiring.md
  - sources/x-polymarket-bot-playbook-punisher-2026-05.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/production-trading-blind-spots.md — row 8 (over-logging); logging must carry `logic_version` on PnL events
- @concepts/pnl-attribution-versioning.md — version tags belong in structured log fields
- @concepts/polymarket-bot-architecture.md — "log everything" without structure failed operators in the field
- @entities/infrastructure/cemini-stack.md — Grafana + Loki + Prometheus stack (10 observability containers)
- @concepts/trading-dashboard-api-wiring.md — metrics/dashboards complement logs; not a substitute
- @sources/x-polymarket-bot-playbook-punisher-2026-05.md — reconciliation events worth logging

## Raw Concept

What prompted this page: months lost debugging PnL partly because **volume of logs obscured attribution bugs**. Cemini prod runs Loki/Grafana but many services still use plain `logging` (e.g. `pnl_attribution`, `kalshi_paper_pnl`). This page codifies what to log, what to skip, and how to stay debuggable without GB/day noise.

## Narrative

### The anti-pattern

Trading systems that log every tick, every health check, and every successful HTTP 200 produce:

- GB/day files where `grep` takes hours [@osquant monitoring paper]
- Loki costs and disk pressure on cemini-prod (already 90% disk [2026-05-03 probe])
- False confidence ("we log everything") with no path to **PnL reconciliation events**

Structured JSON without discipline has the same failure mode.

### What Cemini prod does today (2026-05-28 audit)

| Component | Logging style | Notes |
|-----------|---------------|-------|
| `services/pnl_attribution.py` | stdlib INFO/WARNING/ERROR | Daily batch; low volume — acceptable |
| `scripts/kalshi_paper_pnl.py` | `%(message)s` only | CLI report — OK |
| `core/equity_valuation.py` | DEBUG for FMP/EDGAR misses | Correct level for noisy paths |
| `cemini_mcp/ui_routes.py` | WARNING on API failures | Good — errors only |
| Stack-wide | Loki + Alloy scrape | Ingestion exists; **event schema not uniform** |

Gap: hot-path executors should emit **stable JSON events** with `logic_version`, `order_id`, `symbol`, `event` — not prose paragraphs.

### Rules (prod-oriented)

**Log (INFO or ERROR, structured):**

- Order submit / ack / fill / partial / cancel / reject
- Reconciliation delta (expected vs actual position)
- PnL attribution row written (with `logic_version`, `strategy_key`, `pnl_usd`)
- Kill switch / risk governor trip
- Strategy gate SKIP with reason code (not full feature dump)
- Version banner at process start

**Do not log in production hot path:**

- Successful health checks (use Prometheus scrape)
- Every quote/tick (sample at 1% if needed)
- DEBUG stack traces on expected misses (FMP 404 → DEBUG only)
- Duplicate fill without dedup (fix formatter first — QuantPython challenge)

**Hot-path mechanics:**

- Async queue handler — never block execution on disk I/O
- Dedicated listener thread for file writes
- `put_nowait()` back-pressure — if queue full, logging is the bottleneck (explicit signal)

### Stable `event=` names (recommended schema)

```json
{
  "event": "order_fill",
  "symbol": "AAPL",
  "order_id": "abc-123",
  "logic_version": "brain_playbook_v2",
  "strategy_key": "brain_equity",
  "pnl_usd": 12.34,
  "correlation_id": "run-20260528-001",
  "timestamp": "2026-05-28T14:00:00Z"
}
```

Grafana/Loki queries become `event="order_fill" | logic_version="brain_playbook_v2"` — not regex on free text.

### Four-question gate (before adding a log line)

1. Will this help debug a **production** incident?
2. Can I find it with a field query?
3. Will it fire >1M times/day? → sample or skip
4. Does it include `logic_version` / `order_id` if PnL-relevant?

### Monitoring vs logging

| Use monitoring (Prometheus) | Use logging (Loki) |
|----------------------------|-------------------|
| Rates, latencies, queue depth | Why a specific order failed |
| Daily PnL gauge | Reconciliation diff narrative |
| Health up/down | Audit trail for compliance |

`pnl_attribution` exposes `PNL_PROMETHEUS_PORT=8010` — metrics for batch job; per-trade detail stays in Postgres + structured logs.

### Research references

- [osquant — monitoring trading systems](https://osquant.com/papers/monitoring-trading-systems/) — JSON + time-series beats grep
- RustyBT audit logging — trade/strategy/system event taxonomy
- QuantPython Day 7 — QueueHandler + JSON Lines trade journal + duplicate fill dedup

## Snippets

> "I've come across trading systems that spew out 10s of gigabytes of logs per day. When something goes wrong, some poor intern would have to grep through these log files to figure out why it broke — sometimes for days." [Source: osquant.com/papers/monitoring-trading-systems/]

> "P&L attribution Redis write failed (non-fatal)" — batch job treats downstream fan-out as best-effort; headline write is Postgres. [Source: cemini-prod `services/pnl_attribution.py`, retrieved 2026-05-28]

## Dead Ends

- **Streamlit as log viewer** — not deployed on prod; Grafana is the path.
- **Logging every MCP tool call at INFO** — context-window noise; tier-0 reads are high volume.
