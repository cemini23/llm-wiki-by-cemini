---
title: "arXiv 2607.25904 — Interactive Reward Agent (IRA) GUI eval"
type: source
tags: [source, arxiv, gui-agent, reward, eval, ccc, k206]
keywords: [IRA, GUI-RewardBench, OSWorld, environment-state verification, VLM judge]
related:
  - sources/arxiv-2607.26041-desktop-delta-bench.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: skimmed
---

## Relations

- @sources/arxiv-2607.26041-desktop-delta-bench.md — complementary GUI transition bench

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification |
| arXiv | 2607.25904 |
| Filename | `arxiv-2607.25904-interactive-reward-agent-gui-task-evaluation-via.pdf` |
| sha256 | `86576a26eec6e0338498f3eb32c825812daf00863483ccf5c753b351adb3c03e` |
| Retrieved | 2026-07-29 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.25904-interactive-reward-agent-gui-task-evaluation-via.pdf` |
| Code | not public in paper (2026-07-29) |

## Narrative

Screenshot-only VLM judges miss environment-state success (files, configs, app settings). IRA = propose-then-verify: propose completion conditions, then invoke system/application/GUI tools. **GUI-RewardBench**: 321 trajectories, 10 Ubuntu desktop categories; **86.9%** accuracy (GPT-5.5); κ = 0.84. As RL reward: **34.0%** OSWorld vs **34.9%** ground-truth scripts — near oracle.

**Route:** CCC agent-eval cluster. Phase-0 deferred until code release.

## Snippets

> Environment-state verification is the practical path for scalable GUI-agent eval/training.

[Source: arXiv:2607.25904]
