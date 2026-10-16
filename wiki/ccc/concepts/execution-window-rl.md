---
title: Execution-window RL — assign credit at the checkpoint where the world answers back
type: concept
tags: [agents, rl, training, harness, k292]
keywords: [WIRL, execution window, outcome-guided SFT, learner waiting fraction, experiment tree, invalidate node, credit assignment]
related:
  - sources/arxiv-mlexpert-2610.22344-2026-10-16.md
  - concepts/k292-ccc-wave.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @sources/arxiv-mlexpert-2610.22344-2026-10-16.md — the paper
- @concepts/k292-ccc-wave.md

## Raw Concept

**The question this page answers:** in a long-horizon agent run, where should the reward be assigned?

Source: MLExpert (arXiv 2610.22344, Shanghai AI Lab / ECNU), ingested 2026-10-16.

## Narrative

### The problem

A long MLE run contains many costly experiments, and the feedback from any one of them reflects several preceding decisions. Per-token credit is too fine. Per-trajectory credit arrives too late. The paper's answer is to pick the boundary where the world answers back.

### The method

**Windowed Interaction RL (WIRL).** The multi-turn decisions **between two successive `execute_code` results** form an **execution window**. The whole window receives **one shared reward** from that experiment's outcome. A local trend reward and token-level policy correction support asynchronous collection. **Infrastructure-error windows are excluded from training.**

**The ablation is the evidence:** base 37.9 → general SFT 47.0 → MLE SFT 62.1 → **WIRL 72.7** on MLE-Bench Lite medal rate.

**The efficiency result is the striking one.** **Learner waiting fraction falls from 87.6% under GRPO to 39.3% under WIRL — a 48.3-point drop.** Because credit is assigned at a boundary that actually completes, the learner stops stalling on unfinished rollouts. Reward shape and throughput are usually discussed separately; here one design fixes both.

### Why the boundary is the right place

Every other finding in this wave points the same way:

- The **VEPA** evidence gate (K290) decides when a rule may fire, using accumulated outcomes.
- The **OpenGCUA** `todo` state (`pending` / `changed_unverified` / `claimed_verified`) is a checkpoint marker.
- The **DistressBench** lesson (K290) is to score what the system did, not what it withheld.

An execution boundary is exactly where "did the action work" becomes observable. Assigning credit there is not a training trick; it is the same discipline applied to optimisation.

### The harness primitives worth taking

MLExpert runs a ReAct loop over an **experiment tree** — each node is candidate code plus logs plus metadata, parent-linked for backtracking. Two tools stand out:

- **`invalidate_node`** — an explicit action to exclude an overfit or leaky candidate, rather than silently keeping it. A harness that can mark its own bad work is rarer than it should be.
- **`analyze`** — a sub-agent with its own context that returns only a summary. Context isolation as a first-class tool.

Organisation rules: keep a running submission candidate, revise from execution feedback, compress early history.

### The caveat

**The model is 35B MoE and reports no limitations section.** MLE-Bench Lite is 22 tasks; frontier numbers are single runs while only same-scale models get three. The checkpoint is not runnable here — the recipe is the artefact.

## Snippets

> Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. [Source: arXiv 2610.22344, abstract]

> Asynchronous collection and policy correction support policy updates before the trajectory ends. [Source: arXiv 2610.22344, abstract]
