---
title: "Halo effect in platform evaluation — nine dimensions that measured one impression"
type: concept
related:
  - sources/arxiv-capability-framework-agentic-ai-enterprises-2611.24039.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/enterprise-mcp-adoption-practice.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/low-cost-cross-vendor-behavior-assays.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: a panel scored ten platforms on nine dimensions. Did it measure nine things?

Synthesised from one source: `@sources/arxiv-capability-framework-agentic-ai-enterprises-2611.24039.md` (2611.24039).

## Narrative

A global bank's innovation lab ran a "bakeoff" of ten agentic platforms. A cross-functional panel scored them on nine capability dimensions across three workloads: counterparty credit risk, RAG and process automation.

The headline result looks good. Scores separate into three tiers that hold under alternative weightings, and workload-specific strengths appear.

The secondary analysis undercuts it. Cronbach's α is **0.98** across nominally distinct dimensions, and rank correlation with the total is **≥ 0.93** for eight of nine. When every dimension moves together, the panel is measuring one overall impression — a halo effect. Demonstration-based scoring measures presentation as much as capability.

### What the authors propose instead

A **gate-then-score** protocol with four layers:

1. Capability.
2. Execution reliability.
3. Governance gates.
4. Business value.

Plus trace-level reliability metrics over repeated runs, an autonomy-readiness scale, and a reproducibility protocol. Gates decide pass or fail; scores rank only what passed.

### Operating rule for Cemini

Before treating a multi-dimension score as multiple signals, check the correlations. If the dimensions move together, report one score and say so. The audit-council pattern has the same risk: five reviewers who read the same diff may produce one opinion five times.

Caveat: one enterprise field report, one bank. [TENTATIVE]

## Snippets

> "Cronbach's α = 0.98 across nominally distinct dimensions and rank correlations ≥0.93 with the total for eight of nine: a halo effect indicating that demonstration-based scoring measures presentation as much as capability." [Source: arxiv-2611.24039-a-capability-framework-for-evaluating-agentic-ai.pdf p.1]
