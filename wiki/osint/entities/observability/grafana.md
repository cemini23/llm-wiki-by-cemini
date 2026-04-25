---
title: Grafana
type: entity
tags: [observability, dashboards, monitoring]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/observability/prometheus.md
  - entities/observability/loki.md
  - entities/observability/tempo.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/observability/prometheus.md
- @entities/observability/loki.md
- @entities/observability/tempo.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: observability.

## Narrative

Grafana is the unified dashboard layer over Prometheus metrics, Loki
logs, and Tempo traces. Cemini ships a curated dashboard set:
per-strategy P&L, per-venue fill latency, LangGraph-run traces, risk-
engine state, and a macro-weather regime panel.

Dashboards are **committed as JSON** alongside the code so every
dashboard change is version-controlled and included in the IP-sale
handoff — no click-ops configuration to reconstruct post-acquisition.

## Snippets

*(populate as source stubs are deep-read.)*
