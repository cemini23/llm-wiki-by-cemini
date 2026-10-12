---
title: "Humanize MLE Agents: multi-agent session alternation (arXiv 2610.13494)"
type: source
tags: [source, k289, arxiv, agents, orchestration, ml-engineering, context]
keywords: [hma, context-reset-smdp, long-horizon-deceleration, harness-staleness, session-alternation, mle-bench]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/agentic-context-management.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/agentic-context-management.md

## Raw Concept

| Title | Humanize MLE Agents (HMA): Multi-Agent Session Alternation |
| Authors | Changye Li et al. (Tsinghua, NVIDIA, Zhejiang, MIT) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13494-humanize-mle-agents-multi-agent-session-alternat.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13494v1 |
| Code | `github.com/humanfia/hma` |
| read-status | read |

## Narrative

Names **two failure modes** and fixes them with **workflow-level session alternation**.

### The two failure modes

1. **Long-horizon deceleration** — reasoning tokens decline as gains shrink. The agent slows down its own thinking.
2. **Harness staleness** — a custom harness stops helping once a better base model arrives. **The harness is the thing that ages.**

### The mechanism

Models alternating sessions as a **context-reset semi-Markov decision process (CR-SMDP)**; proves **sufficient conditions for alternation to beat single-agent limits**, and derives an **experiment-budget bound**. **HMA alternates two agents on a shared workspace, caps each session at *k* experiments, and resets context** — **no task-specific harness.**

### Results

- **SOTA 78.2% any-medal on MLE-bench** (75 Kaggle tasks) — **+8.0 points over the best open-source baseline at ¼ the budget**.
- **+6.4 points average** across 6 configs / 5 heterogeneous pairs.
- A kernel case reached **878 cycles, within 1.6% of the leaderboard leader**.

### Why it matters here

**"Harness staleness" is the finding to keep** — a tuned harness decays as models improve, which argues against over-fitting a harness (the K289 CoTrace caution, from the other direction). And the **context-reset** result: a forced reset plus alternation beats a longer single session. Route: CCC. **No `/route` swap.**

## Snippets

> "long-horizon deceleration (reasoning tokens decline as gains shrink) and harness staleness (custom harnesses stop helping better base models)." [Source: arxiv-2610.13494-humanize-mle-agents-multi-agent-session-alternat.pdf]

> "HMA alternates two agents on a shared workspace, caps each session at k experiments, resets context — no task-specific harness." [Source: arxiv-2610.13494-humanize-mle-agents-multi-agent-session-alternat.pdf]
