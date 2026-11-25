---
title: "A capability framework for evaluating agentic AI platforms in regulated enterprises"
type: source
related:
  - concepts/halo-effect-platform-evaluation.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/enterprise-mcp-adoption-practice.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises |
| Author | Abbas Raza Ali (Citigroup), Muhammad Ajmal Siddiqui (EY), Moona Zahid (NVIDIA) |
| Type | arXiv / MLSys 2027 proceedings, 2611.24039 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24039-a-capability-framework-for-evaluating-agentic-ai.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 14 |
| Read status | read |

## Narrative

This is a field report from an industrial "bakeoff" run by the innovation laboratory of a global bank. Ten agentic platforms — open-source frameworks, proprietary products, hyperscaler ecosystems — were scored by a cross-functional panel on nine capability dimensions across three workloads: counterparty credit risk, RAG, and process automation.

Three findings matter.

- **Scores separate into three tiers.** The tiers are stable under alternative weightings.
- **Workload-specific strengths disappear in aggregates.** A single total score hides them.
- **The dimensions are not independent.** Cronbach's α is 0.98 across nominally distinct dimensions, and rank correlation with the total is ≥ 0.93 for eight of nine. The authors call this a **halo effect**: demonstration-based scoring measures presentation as much as capability.

From these results the authors propose a **gate-then-score** protocol with four layers: capability, execution reliability, governance gates, and business value. They add trace-level reliability metrics over repeated runs, an autonomy-readiness scale, and a reproducibility protocol.

The halo effect is the finding to keep. If nine dimensions move together, the panel is measuring one impression. Cemini's own multi-model audits should check for the same collapse before reading nine scores as nine signals.

## Snippets

> "A secondary analysis finds Cronbach's α = 0.98 across nominally distinct dimensions and rank correlations ≥0.93 with the total for eight of nine: a halo effect indicating that demonstration-based scoring measures presentation as much as capability." [Source: arxiv-2611.24039-a-capability-framework-for-evaluating-agentic-ai.pdf p.1]
