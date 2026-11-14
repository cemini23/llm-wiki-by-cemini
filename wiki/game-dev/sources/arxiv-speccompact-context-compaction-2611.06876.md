---
title: "SpecCompact — slot-parallel speculative context compaction for LLM agents"
type: source
related:
  - concepts/context-compaction-game-harness.md
  - concepts/agent-harness-castle-project.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification |
| Author | Yulu An, Yifei Feng, Xiangyang Yin (New York University) |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf` |
| Pages | 12 |
| arXiv | 2611.06876v1, 4 Nov 2026 |
| Read status | read |

## Narrative

A long-running agent collects user requests, tool output, and past decisions. To stay inside the context window, the agent compacts this history into a summary. Summarizing a long history with a large model costs real time, so compaction becomes the bottleneck.

The paper reports one structural observation. Agent frameworks such as OpenClaw and Hermes already summarize into fields: Goal, Constraints, Progress, Key Decisions, Next Steps, Critical Context. The authors call these fields **slots**. Their preliminary study finds that a slot generated **without** the other slots still keeps the needed information [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.2]. Independent slot generation scored 4.73 out of 5 (mean adequacy) against 4.44 for one-shot monolithic generation. Reversing the slot order changed the score by at most 0.03. [TENTATIVE — single study, 100 trajectories]

**How it works.** A small fine-tuned drafter (Qwen3-0.6B in the experiments) writes each slot from the shared history. A larger target model checks each proposed line and either accepts it or writes a replacement. The six slot streams run in parallel. Each slot depends only on its own accepted prefix. The system optimizations are shared-prefix caching, draft buffering, line-aware stopping, and slot scheduling. [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf pp.3-5]

**Results.** Against Hermes-style summarization, the paper reports 4.28–5.63× speedup on agent workloads with Gemma4-31B-IT, and 2.04–2.41× with Qwen3.5-122B-A10B [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.8]. A user study inside the Hermes code base reports a median compaction drop from 63.74 s to 7.28 s, a median paired speedup of 8.68× [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.7].

**The cost.** Speed is not free. Against Hermes, Gemma4 lost 2.98 and 4.07 percentage points of task goal completion on the two AppWorld splits, and 2.50 points on τ3. Qwen3.5 **gained** 4.76 and 1.68 points on AppWorld, and 0.83 points on τ3 [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.6]. The authors state plainly that the method gives no consistent accuracy advantage over target-model summarization [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.7].

**Second finding — slots read from different places.** Progress and Decisions draw evidence from across the whole history. Goal, Constraints, and Next Steps depend mostly on the start or the end. [TENTATIVE — authors give this as a discussion observation, not a measured table]

**Why this belongs in game-dev.** The paper is general agent systems work. Its direct use here is the **agent harness for game dev**, not the game itself. A castle-sim harness runs long planning and implementation sessions, and the compacted context shapes what the next agent step knows. The six-slot schema is a ready template for a milestone state record (@concepts/context-compaction-game-harness.md). A cross-reference to @ccc-wiki would also be correct, because the mechanism is domain-neutral. The concrete harness lever is the one that earns the page here.

## Snippets

> "We observe that structured summary slots can retain information when generated independently." [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.1]

> "Slots generated without other slots' outputs can still preserve relevant information. This supports generating slots in parallel from the shared history." [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.3]

> "It does not offer a consistent accuracy advantage over target-model summarization." [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.7]

> "Progress and Decisions use evidence spread throughout the context, while Goal, Constraints, and Next Steps mainly rely on beginning or end." [Source: arxiv-2611.06876-speccompact-accelerating-llm-agent-context-compa.pdf p.7]
