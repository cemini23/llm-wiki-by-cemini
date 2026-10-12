---
title: "POrchestra: proactive agentic orchestration (arXiv 2610.13485)"
type: source
tags: [source, k289, arxiv, agents, orchestration, harness, rl]
keywords: [porchestra, opod, proactive-revision, harness-mismatch, on-policy-orchestration-distillation, process-reward]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/agent-harness-verification-bottleneck.md

## Raw Concept

| Title | Proactive Agentic Orchestration (POrchestra) |
| Authors | Xueyang Feng, Xiaohe Bo, Jiakai Tang, Xu Chen (Renmin / BAAI) et al. |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13485-proactive-agentic-orchestration.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13485v1 |
| Code | `github.com/XueyangFeng/POrchestra` |
| read-status | read |

## Narrative

**The problem: harness mismatch.** In a dynamic environment, the harness an orchestrator wrote at the start of a task stops fitting partway through — and a **sub-agent** is the one who notices, not the orchestrator.

### The mechanism

**POrchestra** lets **sub-agents proactively interrupt the orchestrator mid-task to request harness adjustments**, while keeping their local execution continuity. That is the inversion: the sub-agent, not the lead, detects the mismatch.

**On-Policy Orchestration Distillation (OPOD):** **hindsight feedback attributes each sub-agent revision request to the preceding orchestration decision**, producing **process supervision** combined with the final reward. So the orchestrator learns *which of its decisions caused the need to re-orchestrate*.

### Results

- **+9.1% average task success** over the strongest baseline.
- **+10.0% small-orchestrator success** with OPOD vs training baselines.
- **Pareto-optimal cost–performance.** Benchmarks: deep research, dynamic digital assistance, software engineering.

### Why it matters here

A direct counterpart to K289's **Anthropic dynamic workflows** and K288's orchestration thread — with a sharper idea: **let the executor trigger re-orchestration**, and **credit the orchestrator decision that caused it**. That is exactly the feedback the lead-agent model lacks. Route: CCC. **No `/route` swap.**

## Snippets

> "POrchestra lets sub-agents proactively interrupt the orchestrator mid-task to request harness adjustments while keeping local execution continuity." [Source: arxiv-2610.13485-proactive-agentic-orchestration.pdf]

> "+9.1% average task success vs. strongest baseline; +10.0% small-orchestrator success with OPOD." [Source: arxiv-2610.13485-proactive-agentic-orchestration.pdf]
