---
title: Anticipatory workspace curation — building the filesystem before the question
type: concept
tags: [agents, context, retrieval, wiki, k292]
keywords: [anticipatory curation, workspace construction MDP, builder agent, answerability probe, amortization, GRPO, when to bypass]
related:
  - sources/arxiv-librarian-agents-2610.22273-2026-10-16.md
  - concepts/k292-osint-wave.md
  - concepts/agentic-context-management.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @sources/arxiv-librarian-agents-2610.22273-2026-10-16.md — the paper
- @concepts/k292-osint-wave.md
- @concepts/agentic-context-management.md

## Raw Concept

**The question this page answers:** when is it worth building a structured workspace in advance, instead of retrieving on demand?

Source: Librarian Agents (arXiv 2610.22273, Stanford/CMU), ingested 2026-10-16.

## Narrative

### The asymmetry

Agents are good at **navigating** a filesystem to answer the question in front of them. They are rarely trained to **build** a workspace that answers questions not yet asked. This wiki is a hand-built instance of the second behaviour — hierarchical files, a `related:` graph, and raw-source pointers, all organised for future queries.

### The mechanism

**A builder agent rewrites a flat corpus into a hierarchical filesystem of synthetic files plus reference links back to the originals — before any query arrives.** Construction is a finite-horizon **MDP**: `CreateFile`, `MergeFiles`, `Delete`, `Stop`. Trained with **GRPO** against a **frozen** downstream answering agent. Raw documents are never deleted, so provenance survives.

**The reward design is the reusable part.** Dense reward comes from **answerability probes every 8 turns** — score the intermediate artefact by how answerable it leaves the questions it has not seen — plus terminal correctness. This is a general instrument: it scores a knowledge artefact on its future usefulness rather than its current completeness.

### The arithmetic that governs whether to do it

| Method | Accuracy | Tokens to build |
|---|---|---|
| GraphRAG | 0.36 | 11,923 |
| AutoCompaction | 0.04 | 501,637 |
| Builder without fine-tuning | 0.28 | 127,683 |
| **Librarian (trained)** | **0.77** | 178,926 |

Build costs about **179,000 tokens**. The answerer then reads ~9,346 tokens per query; at 20 queries per document set the amortised cost is about **18,000 tokens per query**. **Net: 33.8% fewer tokens per correct answer** (ratio 0.662, 95% CI [0.504, 0.836]).

**So the break-even is roughly 20 queries.** Below that, plain retrieval wins. Above it, the built workspace wins, and keeps winning. A wiki read for years is far above the line; a one-off document question is far below it.

### Two design details worth copying

- **Structure increases, it does not decrease.** The trained builder produces **53.4 files, 45.4 clusters, 8.0 merges** against the base model's 4.8 / 4.2 / 0.6. More organisation, not summarisation.
- **RL is load-bearing.** The same architecture untrained reaches 0.28 where the trained builder reaches 0.77. The MDP is not the contribution; the reward is.

### The stated gap is ours too

The authors name two open problems: **static corpora only** — drift and updating are unsolved — and **when to bypass the synthetic layer is unknown.** Both apply here. This wiki's `read_status`, `[NEEDS VERIFICATION YYYY-MM-DD]` tags and `updated:` dates are partial answers to the first; nothing systematically answers the second. The compression risk is real too: the paper warns that **compression can discard needle-in-a-haystack detail**, which is exactly what a hub page does.

## Snippets

> while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use [Source: arXiv 2610.22273, abstract]

> Compression may discard needle-in-a-haystack details; when to bypass the synthetic filesystem remains a challenge. [Source: arXiv 2610.22273, limitations]
