---
title: "ClawGym II — black-box RL on agent harness (arXiv 2608.16798)"
type: source
tags: [arxiv, ccc, harness, rl, k241]
keywords: [ClawGym, black-box-RL, mix-harness, GRPO, PPO]
related:
  - concepts/claw-swe-bench-harness-evaluation.md
  - concepts/harness-optimization-bench.md
  - sources/arxiv-2608.16859-harnesseval-w-2026-08-18.md
  - sources/arxiv-2608.16112-strategic-technical-debt-2026-08-18.md
  - entities/tools/cursor-route.md
  - sources/substack-rss-outlier-weekly-2026-08-18-cursor-route.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @concepts/claw-swe-bench-harness-evaluation.md — prior Claw/SWE harness eval
- @concepts/harness-optimization-bench.md — harness-level measurement
- @sources/arxiv-2608.16859-harnesseval-w-2026-08-18.md — same-day visual-world harness eval
- @sources/arxiv-2608.16112-strategic-technical-debt-2026-08-18.md — cheap harness experiments
- @entities/tools/cursor-route.md — do not swap `/route` worker because of this paper
- @sources/substack-rss-outlier-weekly-2026-08-18-cursor-route.md — same-day public MIT CLI

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.16798, "ClawGym II: Exploring Black-Box RL on Agent Harness" |
| Authors | Huatong Song, Fei Bai, et al. (RUC / IQuest) |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.16798-clawgym-ii-exploring-black-box-rl-on-agent-harne.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.16798-clawgym-ii-exploring-black-box-rl-on-agent-harne.pdf` |
| Type | cs.CL preprint |
| Dual-ID | **OSINT K241**. CCC brief. Do not collapse onto any CCC K241 number. |

## Narrative

Agent harnesses (system prompts, tools, context, retries) improved long-horizon tasks, but RL *through* an opaque harness was unexplored. ClawGym II is a **unified black-box RL** stack: sandbox-isolated concurrent rollouts; a serving proxy at the **model boundary** that captures calls without opening the harness; captured calls rebuilt into **prefix trees**; critic PPO and critic-free GRPO adapted to the tree; training–inference consistency held; **mix-harness training** so one model is jointly optimized by heterogeneous harnesses.

**Concrete claim `[TENTATIVE]`:** with Qwen3-30A3B, black-box RL improves Pass@1 on ClawGym-Bench by **+9.98** (OpenClaw) and **+14.81** (Claude Code), stable over 200–400 steps, with gains on JobBench and OfficeQA.

**CCC steal:** optimize the model *through* the harness without forking the harness. Do **not** replace PATH `claude-ds` or swap the `/route` worker. Sandbox isolation + prefix-tree credit assignment is the pattern to watch.

## Snippets

> "black-box RL improves Pass@1 on ClawGym-Bench by 9.98 and 14.81 points through OpenClaw and Claude Code, respectively, while remaining stable over 200–400 optimization steps." [Source: arxiv-2608.16798 abstract]
