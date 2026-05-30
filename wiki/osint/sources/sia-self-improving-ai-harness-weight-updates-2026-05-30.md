---
title: "SIA — Self Improving AI with Harness & Weight Updates (arXiv:2605.27276)"
type: source
tags: [source, arxiv, self-improving-agents, harness-engineering, hexo-labs, k84]
keywords: [sia, feedback-agent, harness-update, test-time-training, unified-self-improvement-loop]
related:
  - concepts/sia-unified-harness-weight-self-improvement.md
  - concepts/high-signal-paper-patterns.md
  - sources/agentic-harness-engineering.md
  - sources/sakana-conductor-rl-orchestration.md
  - concepts/conductor-orchestrator.md
maturity: draft
read_status: read
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/sia-unified-harness-weight-self-improvement.md — method synthesis
- @sources/agentic-harness-engineering.md — harness-only school vs SIA unified loop
- @sources/sakana-conductor-rl-orchestration.md — RL orchestration adjacent line

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SIA: Self Improving AI with Harness & Weight Updates |
| **Author** | Hebbar et al. (Hexo Labs + Oxford) |
| **Type** | arXiv preprint |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/2605.27276v2.pdf` |
| **arXiv** | 2605.27276 |
| **Retrieved** | 2026-05-30 |
| **Pages** | 15 |
| **Read status** | read (abstract + intro) |

## Narrative

Identifies two siloed research lines: (1) **harness-update** — meta-agent rewrites tools/prompts/retries while weights fixed; (2) **test-time training** — RL updates weights while harness fixed. **SIA** unifies them: a Feedback-Agent updates **both** harness and weights in one self-improving loop.

**Cemini read:** conceptual north star for conductor + analyst brain co-evolution — **not** near-term prod (weight updates on DeepSeek API are out of scope). Steal harness-feedback patterns for skill_audit / brief-audit loops first.

## Snippets

> "These two silos operate in isolation. We propose SIA, a self-improving loop in which a language-model agent (the Feedback-Agent) updates both the harness and the weights." [Source: 2605.27276v2.pdf p.1]
