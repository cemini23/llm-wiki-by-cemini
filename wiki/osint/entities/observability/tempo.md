---
title: Tempo
type: entity
tags: [observability, tracing, monitoring]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/observability/grafana.md
  - entities/observability/prometheus.md
  - entities/observability/loki.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/observability/grafana.md
- @entities/observability/prometheus.md
- @entities/observability/loki.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: observability.

## Narrative

Tempo is the Grafana-stack distributed-tracing backend. Cemini
instruments every inter-service call (FastAPI ↔ LangGraph ↔ Redis ↔
TimescaleDB ↔ venue adapters) with OpenTelemetry spans. `[RETRACTED 2026-04-24]`
Earlier phrasing included "↔ Ollama ↔" in the chain — Ollama is not
deployed on Cemini (see @entities/infrastructure/ollama.md).

The trace-stream has a secondary purpose beyond performance
debugging: each span's (trace_id, service, operation, attrs) tuple is
written into pg_tamperlog as an audit event, giving the Merkle-
anchored ledger a second independent signal of strategy execution.
This is called out in the 3-19 compliance research as a
'defense-in-depth' audit posture valued by institutional buyers.

## Snippets

*(populate as source stubs are deep-read.)*
