---
title: Prometheus
type: entity
tags: [observability, metrics, monitoring]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/observability/grafana.md
  - entities/observability/loki.md
  - entities/observability/tempo.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/observability/grafana.md
- @entities/observability/loki.md
- @entities/observability/tempo.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: observability.

## Narrative

Prometheus is the metrics scraper in Cemini's observability stack. Pulls
/metrics endpoints from every FastAPI service, the LangGraph
orchestrator, TimescaleDB, Redis, and per-strategy exporters that
surface P&L, position, and risk-engine state.

Documented cardinality discipline per the compliance research: labels
are **venue + symbol + strategy_id** — no per-order labels — so series
count stays bounded. Long-term retention offloads to a Thanos sidecar
(reference, not mandatory for the IP-sale demo).

## Snippets

*(populate as source stubs are deep-read.)*
