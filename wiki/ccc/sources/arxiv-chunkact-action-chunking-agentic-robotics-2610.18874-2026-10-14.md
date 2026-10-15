---
title: "ChunkAct — Action Chunking for Agentic Robotics"
type: source
tags: [arxiv, agent, efficiency, cost, action-chunking]
keywords: [action chunking, LLM calls, token reduction, LIBERO-Pro, memory compilation]
related:
  - concepts/k291-ccc-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-ccc-wave.md — K291 ccc wave hub

## Raw Concept

Title: ChunkAct — Action Chunking for Agentic Robotics
Authors: Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang, Emilio Ferrara (USC, UCF, Stony Brook)
Type: arXiv preprint (2610.18874)
Location: `research to be indexed/ccc/arxiv-2610.18874-chunkact-action-chunking-for-agentic-robotics.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The inefficiency:** in agentic robotics every primitive requires a full LLM reasoning pass over the entire interaction history, so episode cost grows with the number of primitives.

**The observation:** this reasoning is **largely redundant**. Once a sub-goal is chosen, its primitives follow a routine that memory already prescribes.

**The fix:** offline, compile memory into **chunks**; online, one call launches a chunk of chained primitives that executes autonomously and **returns control only on failure**. The planner is reserved for decisions that need reasoning, so LLM computation scales with **decisions**, not primitives.

| Measure | Effect |
|---|---|
| LIBERO-Pro task success | **+5.0 points** over SOTA |
| LLM calls | **2.9× fewer** |
| Input tokens | **4.4× fewer** |
| Output tokens | **2.3× fewer** |

**Why it is filed here:** the transferable pattern is **compile the routine, do not re-derive it**. Any repeated agent workflow in this workspace pays the same tax.

## Snippets

> "Once a sub-goal is chosen, its primitives follow a routine already prescribed by memory." [Source: arxiv-2610.18874 p.1]

> "LLM computation therefore scales with the number of decisions rather than the number of primitives." [Source: arxiv-2610.18874 p.1]

## Dead Ends

- Reading this as a robotics-only result. The mechanism — compile a known routine into one dispatch — is domain-independent.
