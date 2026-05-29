---
title: Shadow Trading Data Accumulation — Telemetry, Selection Bias, Dual-Track
type: source
tags: [source, shadow-trading, paper-trading, statistics, k77]
keywords: [shadow-trading, Heckman, IPW, dual-track, Almgren-Chriss, telemetry, R10]
related:
  - concepts/shadow-trading-telemetry-accumulation.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/lp-algorithm-live-promotion-gates.md
maturity: draft
read_status: read
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/shadow-trading-telemetry-accumulation.md
- @concepts/shadow-to-live-transition-engineering.md
- @concepts/lp-algorithm-live-promotion-gates.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Shadow Trading Data Accumulation Strategies |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Shadow Trading Data Accumulation Strategies.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Shadow mode must accumulate **unbiased** counterfactual fills:

- Log intended orders even when risk gate blocks — otherwise **selection bias** (Heckman / IPW correction)
- **Dual-track:** strict (production gates) vs relaxed (research telemetry) with shared market snapshot ID
- Almgren-Chriss framing for optimal shadow horizon vs capital lock

R10 PM×KL: 8422 spread obs but **0 stat-arb paper trades** — shadow telemetry gap; enable relaxed track for pair signals without capital.

## Snippets

> Shadow datasets that only record executed trades inherit the same selection bias as live PnL. [Source: Shadow Trading Data Accumulation Strategies.docx — paraphrase]
