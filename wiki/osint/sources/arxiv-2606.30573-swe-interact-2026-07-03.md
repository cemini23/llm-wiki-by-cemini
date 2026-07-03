---
title: "SWE-INTERACT — arXiv 2606.30573"
type: source
tags: [arxiv, agent-harness, coding-agents, swe-bench, k141, pdf]
keywords: [SWE-INTERACT, Scale AI, multi-turn, user simulator, goal discovery, workspace inspection]
related:
  - concepts/swe-interact-user-driven-coding-eval.md
  - entities/tools/swe-interact.md
  - sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md
maturity: draft
read_status: read
created: 2026-07-03
updated: 2026-07-03
clusters: [agent-harness, ccc, poker]
---

## Relations

- @concepts/swe-interact-user-driven-coding-eval.md — synthesis
- @entities/tools/swe-interact.md — Apache-2.0 harness repo

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions |
| **Authors** | Raghavendra et al. (Scale AI) |
| **arXiv** | 2606.30573v1 |
| **Repo** | https://github.com/scaleapi/SWE-Interact |
| **sha256** | `160d5700dd6ddf236ac739a8c8fdff9f5defaebe305ecbf8a0587290e9bd7345` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.30573-2606-30573v1-swe-interact-reimagining-swe-benchm.pdf` |
| **Retrieved** | 2026-07-03 |
| **Read status** | read |

## Narrative

**75 multi-turn tasks** adapted from SWE benchmarks with **persona-conditioned user simulator**: vague initial prompt → workspace inspection (rg, sed, git) → progressive requirement reveal.

### Key result

Best models ~**50%** single-turn vs ~**25%** SWE-INTERACT — strong single-turn SWE **does not transfer** to interactive goal discovery.

Failure modes: over-agentic coding, forgetting requirements, weak models give up under ambiguity.

**Cemini relevance:** Poker Arena researcher patches + CCC harness — partial-spec eval axis orthogonal to SWE-bench.

## Snippets

> "Strong performance on single-turn SWE tasks does not reliably transfer to multi-turn, user-driven workflows." [Source: arxiv-2606.30573 abstract (retrieved 2026-07-03)]
