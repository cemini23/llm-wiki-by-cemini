---
title: "Timeout cascade — small model first, escalate on failure"
type: concept
related:
  - sources/arxiv-timeout-cascades-coding-agent-inference-cost-2611.24324.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/decision-model-hybrid-agent-routing.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - sources/newsletter-rss-pragmatic-engineer-2026-11-17-inference-engineering-for-software-engineers.md
  - entities/skills/route.md
  - concepts/control-flow-tax-agent-routing.md
  - concepts/frontier-led-slm-delegation.md
  - sources/arxiv-delegent-multi-agent-harness-cost-2611.33098.md
  - sources/arxiv-control-flow-tax-decision-routing-2611.32365.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

Question this page answers: how much money does a cheap-first routing rule save, and does it cost accuracy?

Synthesised from one source: `@sources/arxiv-timeout-cascades-coding-agent-inference-cost-2611.24324.md` (2611.24324).

## Narrative

The paper measures 36 open-weight models on SWE-bench Verified under one fixed scaffold. The small–large accuracy gap is not uniform: small models are competitive on easy and medium tasks and weak on hard tasks.

That shape supports a **timeout cascade**:

1. Run the small model.
2. Escalate to the large model only if the small model fails or times out.
3. Score the result.

Reported effect: up to 33% less total GPU-hour cost, and 16.4% across all SWE-bench Verified tasks, with no accuracy loss. The simple cascade nearly matches an oracle router.

### Why the simple version wins

A learned difficulty classifier needs training data, a serving path and upkeep. The cascade needs a timeout and a retry. The paper's own comparison says the extra machinery buys little.

### Where it fits Cemini

`/route` already sends easy work to DeepSeek Flash and keeps stronger lanes for hard work. The missing piece is a **failure-triggered escalation**: if the cheap lane fails, retry once on the next lane before reporting failure. That is cheap, and it does not require a classifier.

Two cautions. The measurement is vendor-authored by AMD researchers, and GPU-hour cost is not the same as token cost. [TENTATIVE]

## Snippets

> "By utilizing a hybrid inference strategy that tries a small model first and escalates to a large one only when needed, we can achieve up to 33% reduction in total GPU-hour costs and 16.4% on all tasks from SWE-bench Verified, without sacrificing accuracy." [Source: arxiv-2611.24324-reducing-inference-cost-of-coding-agents-with-ti.pdf p.1]

> "This simple cascade nearly matches an oracle-style task router." [Source: arxiv-2611.24324-reducing-inference-cost-of-coding-agents-with-ti.pdf p.1]
