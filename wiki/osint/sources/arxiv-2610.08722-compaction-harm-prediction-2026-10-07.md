---
title: "Does an agent's history tell you when compaction will hurt? (arXiv 2610.08722)"
type: source
tags: [source, k284, arxiv, agents, memory, compaction, eval, ccc]
keywords: [compaction, trace, appworld, paired-replay, auroc, context-window, salesforce]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/agentic-context-management.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/agentic-context-management.md

## Raw Concept

| Title | Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus |
| Authors | Egor Pakhomov, Erik Nijkamp (Salesforce AI Research) |
| Type | arXiv preprint (cs.AI) — NeurIPS 2026 IAB Workshop |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08722-does-an-agent-s-history-tell-you-when-compaction.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08722v1 |
| Data | `github.com/nokia-applied-research/Trace` |
| read-status | read |

## Narrative

**Compaction** is summarising an agent's context when it hits the window limit. It can help or hurt. This paper asks: **does the pre-compaction history predict when it will hurt?**

### Method

Replays **590 harness-triggered AppWorld compaction boundaries** (275 of 294 trajectories, 147 tasks; agent + compressor = **minimax-m3**, 4,096-token window). Each boundary runs from a re-executed prefix under **PRE** (raw prefix) and **POST** (summary). Burden channels: **blocked** (error), **refetch** (repeat call), union. Primary outcome **dU@3**. Trains interpretable triggers (a stump, a depth-2 tree, a 2-feature logistic) plus boosted models.

### Results — the honest headline is "modest"

- Best **frozen interpretable trigger avoids 21% of harmful boundaries** while keeping **84% of compaction opportunities.**
- Extension protocol reaches **AUROC 0.66** vs a same-boundary replicate **0.72** (interpretable policies 0.55–0.62).
- A prespecified placement contrast is a **wide null**: −0.062 [−0.209, +0.079].
- The "has-written" label actually measures **trajectory phase**, not the thing it names.

### Why it matters here

A **calibrated negative result** — the wiki values those. The signal exists but is weak and bounded; **history alone is not a reliable compaction gate.** Feeds `agentic-context-management` and the agent-memory threads. **No license** on the underlying TRACE corpus.

## Snippets

> "Best frozen interpretable trigger avoids 21% of harmful boundaries while keeping 84% of compaction opportunities." [Source: arxiv-2610.08722-does-an-agent-s-history-tell-you-when-compaction.pdf]

> "Prespecified placement contrast: a wide null (−0.062 [−0.209, +0.079])." [Source: arxiv-2610.08722-does-an-agent-s-history-tell-you-when-compaction.pdf]
