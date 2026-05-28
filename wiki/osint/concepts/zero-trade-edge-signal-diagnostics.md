---
title: Zero-trade edge signal diagnostics — three-domain abort framework
type: concept
tags: [concept, debugging, trading-bot, alternative-data, observability, k76]
keywords: [zero-trade, ingest-latency, falsification, liquidity, OpenTelemetry, abort-reason]
related:
  - sources/algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.md
  - concepts/trading-model-failure-diagnostics.md
  - concepts/production-trading-blind-spots.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/polymarket-bot-architecture.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/polymarket-weather-trading-strategy.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.md — primary source
- @concepts/trading-model-failure-diagnostics.md — model-side vs execution-side triage (K77)
- @concepts/production-trading-blind-spots.md — row #13 zero-trade silence
- @concepts/trading-bot-logging-discipline.md — OTel span naming for domain A
- @concepts/polymarket-bot-architecture.md — domain B thin-book context
- @concepts/shadow-to-live-transition-engineering.md — don't promote if abort domain unknown
- @concepts/polymarket-weather-trading-strategy.md — domain A weather ingest latency

## Raw Concept

When bots log **no trades** despite strong signals, run this **three-domain triage** before tuning alpha. K76 framework from pipeline failure analysis source.

## Narrative

### Diagnostic flow

```
High-conviction signal → zero actionable trades
  ├─ A) Latency?     → OTel trace: ingest_complete_ts vs market_window_close
  ├─ B) Liquidity?   → FOK/FAK reject, TCA slippage, book depth
  └─ C) Falsification? → shield logs, Z-score, STL / causality check
```

### Domain A — Ingest latency

- Weather / alt-data: GRIB parse, API rate limits, p99 tail — not visible in mean latency metrics.
- **Fix:** OTel context propagation webhook→signal→router; hard deadline abort with `abort_reason=latency_window_closed`.

### Domain B — Liquidity

- Polymarket / niche contracts: signal correct, book too thin or slippage > max.
- **Fix:** Pre-trade TCA; log `abort_reason=liquidity` with intended size vs available depth.

### Domain C — Falsification

- Safety shields deliberately suppress trades on malformed or revision-prone alt data.
- **Fix:** Distinguish true negative (saved capital) vs false negative (threshold miscalibration) via labeled counterexamples.

### Cemini prod requirement

Every skip path should emit structured log:

```json
{"event": "trade_aborted", "abort_reason": "latency|liquidity|falsification", "strategy_key": "...", "logic_version": "..."}
```

Silent no-ops are a blind spot (@concepts/production-trading-blind-spots.md).

## Snippets

> "The absence of a trade is often a protective mechanism, albeit one that requires intense scrutiny to determine whether the suppression was a true negative or a false negative." [Source: algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.docx]
