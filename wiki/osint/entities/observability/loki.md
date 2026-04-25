---
title: Loki
type: entity
tags: [observability, logs, monitoring]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/observability/grafana.md
  - entities/observability/prometheus.md
  - entities/observability/tempo.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/observability/grafana.md
- @entities/observability/prometheus.md
- @entities/observability/tempo.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: observability.

## Narrative

Loki is the Grafana-stack log aggregator — label-indexed, not full-text
indexed, which keeps storage costs low. Cemini ships structured JSON
logs from every container through Promtail into Loki; the LangGraph
orchestrator emits run-id / node-id / tool-call labels so logs join
cleanly with traces in Tempo.

Explicit IP-sale note: the log schema is documented as part of the
milestone ledger deliverable so the acquirer can reproduce any
incident investigation on their own Loki deployment.

## Snippets

*(populate as source stubs are deep-read.)*
