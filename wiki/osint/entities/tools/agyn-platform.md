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
phase_0_verdict: REFERENCE 2026-06-02 — prod K8s agent ops; compare governance checklist vs Hetzner brief-driven deploy only
---

## Relations

- @sources/arxiv-agyn-agent-platform-2605.27575-2026-06-02.md
- @ccc-wiki/entities/tools/agyn.md — CCC REFERENCE verdict (aligned)

## Narrative

**Agyn** (arXiv 2605.27575) — open-source platform: signal-driven serverless agents on Kubernetes, Terraform “agent definition as code,” zero-trust access.

| Check | Verdict |
|-------|---------|
| CeminiSuite prod migration | **NO-GO** — Hetzner brief-driven stack is canonical |
| Governance checklist steal | **REFERENCE** — isolation, on-demand execution, privileged-tool boundaries vs prod-mcp |

**Conditional-GO:** Phase-0 doc compare only if prod topology review is scheduled — no install from this wiki session.

## Snippets

> "Operating agents at scale with proper isolation, governance, and security." [Source: arxiv-2605.27575…pdf via @sources/arxiv-agyn-agent-platform-2605.27575-2026-06-02.md]
