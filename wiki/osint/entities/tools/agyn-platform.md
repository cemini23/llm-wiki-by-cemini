---
title: Agyn — production agent platform (REFERENCE)
type: entity
tags: [entity, agent-platform, reference, k94]
keywords: [agyn, kubernetes, serverless, zero-trust, terraform, production-agents]
related:
  - sources/arxiv-agyn-agent-platform-2605-27575-2026-06-02.md
  - "@ccc-wiki/entities/tools/agyn.md"
  - concepts/librarian-server-architecture.md
maturity: draft
created: 2026-06-02
updated: 2026-06-02
phase_0_verdict: NO-GO install 2026-06-02 — AGPL-3.0 (agynio/platform); REFERENCE governance checklist vs Hetzner brief-driven deploy
---

## Relations

- @sources/arxiv-agyn-agent-platform-2605-27575-2026-06-02.md
- @ccc-wiki/entities/tools/agyn.md — CCC REFERENCE verdict (aligned)

## Narrative

**Agyn** (arXiv 2605.27575) — open-source platform: signal-driven serverless agents on Kubernetes, Terraform “agent definition as code,” zero-trust access.

| Check | Result [CONFIRMED 2026-06-02] |
|-------|-------------------------------|
| Repo | `github.com/agynio/platform` (+ `agynio/bootstrap` k3d/Terraform) |
| License | **AGPL-3.0** — network copyleft; **NO-GO** for CeminiSuite prod binary |
| Stars / push | ~185★; active May 2026 |
| Topology | Multi-service K8s — **not** current Hetzner VM + brief-driven deploy |
| CeminiSuite migration | **NO-GO** |
| Governance checklist steal | **REFERENCE** — prod brief `briefs/2026-06-02_k94-phase0-harness-steals-cemini-prod.md` maps controls → `agent_budget.py`, egress, HITL |

**Prod:** ship checklist doc only; no Agyn bootstrap on prod or egress.

## Snippets

> "Operating agents at scale with proper isolation, governance, and security." [Source: arxiv-2605.27575…pdf via @sources/arxiv-agyn-agent-platform-2605.27575-2026-06-02.md]
