---
title: "arXiv 2607.29600 — HAM-VLN hierarchical agentic memory for zero-shot VLN"
type: source
tags: [source, arxiv, agent-memory, vln, k219]
keywords: [2607.29600, HAM-VLN, hierarchical-memory, world-graph, zero-shot]
related:
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/agentic-navigation-memory-strategy.md
  - concepts/agent-memory-critique.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
read_status: skimmed
---

## Relations

- @concepts/hierarchical-bounded-agent-memory.md
- @concepts/agentic-navigation-memory-strategy.md
- @concepts/agent-memory-critique.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation |
| arXiv | https://arxiv.org/abs/2607.29600 |
| Filename | `arxiv-2607.29600-ham-vln-harnessing-hierarchical-agentic-memory-f.pdf` |
| sha256 | `3ca98eeb21a309f971d549f0a4d776b4e5dcd35fb43dfd0f0c97b706f90df2d0` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.29600-ham-vln-harnessing-hierarchical-agentic-memory-f.pdf` |
| read_status | skimmed |

## Narrative

Training-free VLN: multimodal LLM plans next action while authoring a **depth-grounded world graph** (room type, objects, progress, failure notes) in the same call. Claims **>65% context cut** vs raw image/map streams; reported SR **61% / 52.7% / 79.7%** across VLN benchmarks.

Maps to Cemini hierarchical/bounded memory + navigation-memory concepts — pattern reference for agent memory design, not a robot deploy.

## Snippets

> We present HAM-VLN, a decision-coupled, agent-authored memory that equips the robot with a persistent, depth-grounded world graph. [Source: arXiv:2607.29600]
