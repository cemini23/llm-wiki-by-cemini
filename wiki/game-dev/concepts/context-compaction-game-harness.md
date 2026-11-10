---
title: Context compaction for the game-dev agent harness
type: concept
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-speccompact-context-compaction-2611.06876.md
updated: 2026-11-10
---

## Raw Concept

What happens to the history of a long agent session when it no longer fits in the context window. This page records the compaction method from SpecCompact (arXiv 2611.06876) and how it applies to the castle-sim agent harness. The question: how does a harness keep the state that later steps need, at a cost that does not stall the session?

## Narrative

### The problem in one sentence

A long-running code agent accumulates user requests, tool output, and past decisions. To stay inside the window, the agent folds this history into a summary. With a large model that summary is slow to write. Compaction then becomes the wait. [Source: arxiv-speccompact-context-compaction-2611.06876.md p.1]

### What SpecCompact claims

Agent frameworks already summarize into named fields, which the paper calls slots: Goal, Constraints and Preferences, Progress, Key Decisions, Next Steps, Critical Context. The paper's claim is that these slots do **not** need each other. Generate each one straight from the shared history, and the information survives. [Source: arxiv-speccompact-context-compaction-2611.06876.md pp.2-3]

If that holds, the slots can be written in parallel. A small fine-tuned drafter writes a slot. The large target model checks each line and writes a repair on rejection. Six streams run at once. Reported speedup against a Hermes-style single-stream route is 4.28–5.63× on one target model and 2.04–2.41× on another. [Source: arxiv-speccompact-context-compaction-2611.06876.md p.8]

### The honest cost

The speed comes with a task-score trade. On one target model the compacted runs lost 2.50 to 4.07 points of task goal completion. On the other they gained 0.83 to 4.76 points. The authors state that the method has no consistent accuracy advantage over plain target-model summarization. [Source: arxiv-speccompact-context-compaction-2611.06876.md p.6, p.7] [TENTATIVE — one paper, two models]

### What to take into the castle-sim harness

**1. Adopt the six-slot schema as the milestone state record.** The harness already keeps a per-milestone record. The six slots name the parts that matter: what the milestone wants, what bounds it, what is done, what was decided, what comes next, and what context a fresh agent cannot re-derive. A slot schema is a cheap change and it makes the record portable between sessions.

**2. Keep the raw record beside the compacted one.** This matches rule **H7** in @concepts/agent-harness-castle-project.md: complete records of actions and feedback beat summarised rules as a learning substrate. SpecCompact compresses for the window. It does not argue that the source history should be thrown away. Keep both.

**3. Treat the summary as lossy, not as truth.** This matches rule **H8**: inherited notes can be stale or wrong. A compaction summary is an inherited note. It should carry its generation time, and the harness should prefer the raw record when the question is exact. This is the same shape as the MEMENTO 3 replay gate in **H14**: keep the raw transitions, derive a revisable summary, admit edits only on a check.

**4. Use slots as the unit of parallel work, not as a claim about correctness.** The parallel slot claim is about information retention, not about task quality. SpecCompact itself measured a quality drop on one model. Parallel compaction is a latency tool, and the harness should measure quality after it switches, not assume it.

### Where the slots read from

The paper's discussion says Progress and Decisions draw evidence from across the whole history, while Goal, Constraints, and Next Steps depend mostly on the very start or the very end. If the harness uses a sliding window to cut cost, it should keep the head and the tail of the history and scan the middle. [TENTATIVE — discussion note in the paper, not a measured table]

### Scope boundary

This is domain-neutral mechanism work. The same note is a fair fit for @ccc-wiki, and the CCC domain owns the general harness primitives. This page exists in game-dev because the castle-sim harness is a listed active project and the six-slot record is the concrete artefact to build.

## Snippets

> "Compaction therefore requires balancing information retention against the latency of producing the summary." [Source: arxiv-speccompact-context-compaction-2611.06876.md p.1]

> "A durable ledger is not automatically an asset — it can encode a stale or self-defeating convention." [Source: concepts/agent-harness-castle-project.md, rule H8]

## Dead Ends

- Using compaction speed as a quality claim. The paper's own data shows a task-score drop on one model. Speed is the only measured gain.
