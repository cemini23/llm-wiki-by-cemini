---
title: Computer-use agent harness — observe, act, organise, with code execution per step
type: concept
tags: [agents, computer-use, harness, k292]
keywords: [observe act organize, code execution per step, guarded program, on-demand screenshot, todo state, rolling buffer, micro-compaction counterexample, harness-to-model transfer]
related:
  - sources/arxiv-opengcua-2610.22200-2026-10-16.md
  - concepts/k292-ccc-wave.md
  - concepts/agentic-context-management.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @sources/arxiv-opengcua-2610.22200-2026-10-16.md — the paper
- @concepts/k292-ccc-wave.md
- @concepts/agentic-context-management.md

## Raw Concept

**The question this page answers:** what does a modern computer-use harness look like, and which parts are worth copying?

Source: OpenGCUA (arXiv 2610.22200, Alibaba Token Hub), ingested 2026-10-16.

## Narrative

### The definition

A **generalist computer-use agent** is one where **the model chooses how to observe, act and organise its work** across visual and programmatic interfaces. GUI-only agents, CLI agents and batched GUI+CLI hybrids are each special cases that move one decision back into the harness.

### The three decisions

1. **Observe.** The model requests what it needs — screenshot, accessibility tree, or nothing. `qt ⊆ {screenshot, AX}`.
2. **Act.** The model emits **one guarded Python program per step** over PyAutoGUI, `bash()` and the AX tree, with loops, branches and asserts inside a single call. Five named patterns: cross-interface composition, loop-based execution, result-dependent execution, observation preparation (tile N views into a contact sheet), and **executable verification**.
3. **Organise.** A `todo` state with three values — **`pending`**, **`changed_unverified`**, **`claimed_verified`** — plus a decision about what context to keep.

**`changed_unverified` is the sharp detail.** It separates "I edited it" from "I confirmed it worked", which is precisely the distinction most agent loops blur.

### What the numbers say

On OSWorld-v2: mean partial score **45.3 → 64.9 (+19.6 points)**, steps per task **−53.0%**. But the distribution matters more than the mean:

| Model | Gain |
|---|---|
| GLM-5.3-Flash | **+35.2** |
| DeepSeek-V4.1-Flash | +29.8 |
| Qwen3.8-Flash | +21.6 |
| Claude Opus 5 | +9.4 |
| GPT-6 Astra | +8.7 |

**Weaker models gain most.** Code execution substitutes for capability the weak model lacked. Against a strong batched GUI+CLI baseline the gain narrows to +4.4 to +9.1 points, so part of the headline is the baseline's weakness — the code-execution ablation alone is **+15.5 to +33.6 points** and −55% to −63% steps.

### Context management, with one counterexample

- **On-demand screenshots** raise cache hit by **+10.5pp** (Qwen) and **+14.4pp** (DeepSeek).
- A **rolling screenshot buffer** adds **+16.0 / +13.4pp**.
- **Micro-compaction lowers cache hit** to 68.6 / 58.9.

That last line is a concrete counterexample to aggressive compaction, and it sits opposite the K290 harness-design finding that **rule-based elision before LLM summarisation is the strongest efficiency path**. The reconciliation is that eliding what you have already extracted helps; repeatedly rewriting the live context does not.

### The reporting rule this paper models

**No model was trained.** The release is code, prompts and trajectories. The authors say so plainly, cap their real-device evidence at four macOS tasks with one run each, and frame those as characterising configurations rather than ranking models. When a harness paper reports a harness gain, that is the standard to hold it to.

## Snippets

> We also propose harness-to-model decision transfer, moving selected observations and task-state decisions from fixed harness rules to the model. [Source: arXiv 2610.22200, abstract]

> Code execution is a key feature of our agent design: it lets intermediate results determine subsequent operations. [Source: arXiv 2610.22200, abstract]
