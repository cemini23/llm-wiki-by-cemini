---
title: Multi-agent embodied autonomous driving (MAEAD) — shared world models survey
type: concept
tags: [concept, survey, autonomous-driving, world-model, k122]
keywords: [MAEAD, SWM, V2X, cooperative perception, embodied AI, survey]
related:
  - sources/arxiv-maead-shared-world-models-2606.13840-2026-06-18.md
  - sources/leworldmodel-2603.19312v2.md
maturity: draft
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @sources/arxiv-maead-shared-world-models-2606.13840-2026-06-18.md — 380+ paper survey
- @sources/leworldmodel-2603.19312v2.md — single-agent world model contrast

## Raw Concept

K122 catalog entry for arXiv **2606.13840** — survey framing autonomous driving as **multi-agent embodied** systems with **Shared World Models (SWMs)** maintained across agents and infrastructure.

## Narrative

**SWM definition:** predictive cross-agent representation — exchanged observations → aligned state → intent-aware interaction → coordinated action.

**Literature map:** V2X → collaborative perception → cognition → cooperative planning → end-to-end cooperative driving → sim/data engines.

**Limitations (authors):** sim-heavy eval; foundation-model coordination without open-road safety proofs.

**Cemini relevance:** **REFERENCE** taxonomy only. Weak analog to conductor multi-agent shared state (`intel:*` Redis) but no active AD stack — wiki-only unless user reopens.

## Snippets

> "Evaluation remains concentrated in simulation, curated benchmarks, and offline protocols." [Source: arXiv:2606.13840 abstract (retrieved 2026-06-18)]

## Dead Ends

- No prod brief — deprioritized per `active_project_brief_targets.yaml` legacy filter.
