---
title: "Drone scheduling for victim search — no SEO link, recorded for inventory"
type: source
tags: [source, arxiv, out-of-scope, agents, optimisation, routing]
related:
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: read
created: 2026-11-14
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions |
| Authors | Yinghao Zhang, Yalin Liu, Hong-Ning Dai, Yan Zhang, Qubeijian Wang, Bishenghui Tao, Yaohan Li (Hong Kong Metropolitan University; HKBU; UESTC; Northwestern Polytechnical University) |
| arXiv | 2611.16524 |
| Pages | 8 |
| Location | `research to be indexed/seo/arxiv-2611.16524-a-joint-llm-and-optimization-agent-solution-for.pdf` |
| Retrieved | 2026-11-13 |
| Read status | read |

## Narrative

**No SEO link.** This is a multi-drone scheduling problem for wilderness search and rescue. It has no connection to search engines, retrieval, citation or local ranking. The page exists for inventory honesty, and it is linked from @concepts/corpus-overflow-out-of-scope.md.

### What the paper does

A ground control station runs an agent that coordinates ten drones over repeated search cycles. The agent splits each decision in two stages. An LLM reasons about **where** to search, using unstructured clues such as a distress call. An optimizer then decides **how** to dispatch drones under an energy constraint. The first stage ranks high-priority cells. The second stage selects cells and minimises assignment time. [Source: arxiv-2611.16524 p.1-2]

Clue text in the simulation names group composition and a last sighting. The LLM uses a child's limited walking range to exclude distant destinations. That is the reasoning the design claims an optimizer cannot do alone. [Source: arxiv-2611.16524 p.5]

### Reported results

Over five runs, the joint system found **5.0 ± 0.0** victims and completed **5/5** missions. Direct LLM scheduling found 4.0 ± 1.2 and completed **2/5**. All six non-LLM baselines completed **0/5**. [Source: arxiv-2611.16524 p.6]

Cost and reliability differ more than the success count:

| Variant | Mission complete | Cycles | Time (s) | Tokens per run | Illegal actions |
|---------|------------------|--------|----------|----------------|-----------------|
| Joint LLM + optimizer | 5/5 | 3.8 ± 1.8 | 4661 ± 457 | 32k ± 16k | 26.3% |
| LLM direct | 2/5 | 28.0 ± 11.0 | 6223 ± 1083 | 273k ± 127k | 52.1% |
| No knowledge retrieval | 4/5 | 9.6 ± 12.5 | 4654 ± 264 | 95k ± 130k | 38.8% |
| No mobility reasoning | 1/5 | 26.0 ± 12.5 | 4682 ± 0 | 289k ± 162k | 33.8% |

[Source: arxiv-2611.16524 p.6]

The paper reports cross-backbone results for five models. Three of them complete 5/5. Qwen Flash completes 0/5 and takes 566k tokens per run. [Source: arxiv-2611.16524 p.6]

### The one analogy, clearly marked

The division of labour is a general pattern: a model proposes candidates, and a deterministic layer enforces a hard constraint. Content planning can use the same shape — a model ranks candidate topics, and a fixed budget or fact set decides which ones ship. This is an analogy, not a finding. `[TENTATIVE]` No part of the paper supports it.

## Snippets

> "the agent applies a scheduling policy that combines a large language model (LLM) for reasoning about where to search with an optimizer for determining how to dispatch the drones under energy constraints." [Source: arxiv-2611.16524 p.1]

## Dead Ends

- **Searching this wiki for "drone" or "scheduling" to find an SEO use.** There is none.
- **Quoting the success rate as an agent result for content work.** The task and the metric are search and rescue.
