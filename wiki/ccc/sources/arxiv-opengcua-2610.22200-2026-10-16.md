---
title: "OpenGCUA — an open harness for generalist computer-use agents (arXiv 2610.22200)"
type: source
tags: [agents, computer-use, harness, source, k292]
keywords: [OpenGCUA, computer use, OSWorld, code execution per step, observe act organize, harness-to-model decision transfer, qwen, gpt-6 astra]
related:
  - concepts/computer-use-agent-harness.md
  - concepts/k292-ccc-wave.md
  - concepts/agentic-context-management.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/computer-use-agent-harness.md — the pattern this paper establishes
- @concepts/k292-ccc-wave.md — K292 ccc wave hub
- @concepts/agentic-context-management.md

## Raw Concept

Title: OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use
Authors: Hanzhang Zhou et al. (MAI-UI Team), Alibaba Token Hub, Alibaba Group
Type: arXiv 2610.22200v1 [cs.CV], 40 pages, 15 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.22200-opengcua-toward-a-fully-open-stack-for-generalis.pdf`
Retrieved: 2026-10-16
Artifacts: `github.com/Tongyi-MAI/OpenGCUA` · `tongyi-mai.github.io/OpenGCUA/`
Read status: read

## Narrative

**This is a harness paper with no model.** The authors train nothing; the gains come from giving existing frontier models **code execution inside the computer-use loop**. Read it that way.

**The definition.** A *generalist computer-use agent* is a system where **the model decides how to observe, act, and organise its work** across visual and programmatic interfaces. GUI-only agents, CLI agents, and batched GUI+CLI hybrids are each special cases that freeze one of those decisions in the harness.

**The two mechanisms.**

1. **One guarded Python program per step.** Instead of one GUI action per model call, the model emits a program over PyAutoGUI + `bash()` + the AX tree, with loops, branches and asserts inside a single call. Five reusable patterns are named: cross-interface composition, loop-based execution, result-dependent execution, observation preparation (tiling N views into a contact sheet), and executable verification.
2. **Harness-to-model decision transfer.** Observations and task-state decisions move from fixed harness rules to the model — including **on-demand screenshots** and a `todo` state tracking `pending` / `changed_unverified` / `claimed_verified`.

**Results on OSWorld-v2 (82-task offline subset, partial score 0-100):**

- Mean partial score **45.3 → 64.9**, **+19.6 points**.
- **Steps per task −53.0%**; output tokens −27.2% for 6 of 8 models.

| Model | Batched GUI → OpenGCUA | Steps/task |
|---|---|---|
| GLM-5.3-Flash | 29.6 → **64.9** (+35.2) | 190.8 → 75.5 |
| DeepSeek-V4.1-Flash | 28.0 → 57.7 (+29.8) | — |
| Qwen3.8-Flash | 38.9 → 60.5 (+21.6) | — |
| Kimi K3 | 40.7 → 59.2 (+18.5) | — |
| Gemini 3.8 Flash | 50.1 → 67.0 (+16.9) | — |
| Claude Opus 5 | 60.7 → 70.1 (+9.4) | 103.1 → 61.4 |
| GPT-6 Astra | 67.1 → **75.7** (+8.7) | 102.1 → **33.5** (−67.2%) |

**The pattern in the table is the finding: weaker models gain most.** GLM-5.3-Flash gains 35 points; GPT-6 Astra gains 8.7. Code execution substitutes for capability the weaker model lacked. Against a strong batched GUI+CLI baseline the gain narrows to +4.4 to +9.1 points, so part of the headline is the harness, part is the baseline's weakness.

**Code-execution ablation:** **+15.5 to +33.6 points**, steps **−55.3% to −63.1%**.

**Context-management details worth stealing:** on-demand screenshot raises cache hit by **+10.5pp** (Qwen) and **+14.4pp** (DeepSeek); a rolling screenshot buffer adds **+16.0 / +13.4pp**; **micro-compaction lowers it** (to 68.6 / 58.9). That last one is a concrete counterexample to aggressive compaction.

**Cost:** Qwen3.8-Flash 60.5 at about **$0.38 per task** against GPT-6 Astra 75.7 at about **$15.26 per task**.

**Limitations, and the comparison is the finding.** No trained model — the release is code, prompts, trajectories from eight models, a **preliminary** real-device harness and a cross-device SDK, **no weights**. The authors state the GCUA model is a later release. Real-device evidence is **four macOS tasks, one run per model**, and they explicitly frame it as characterising configurations rather than ranking models. In those four tasks GPT-6 Astra used 34.5 steps and **$18.29**, while Qwen3.8-Max used 50.8 steps and **$1.49** — but **19.4× the reported reasoning tokens**. **Take the OSWorld numbers; treat the macOS numbers as a smoke test.**

### Why it matters here

The copyable pattern is the whole point, and it maps onto Claude Code directly: **one guarded program per step**, **ask for the observation rather than always taking it**, keep an explicit `todo` state with a `changed_unverified` field, and **do not micro-compact**. The `changed_unverified` distinction is particularly good — it separates "I edited it" from "I checked it worked".

The second lesson is a caution: **the model-versus-harness split must be reported.** Here the harness is the product, and the authors say so. Compare `@concepts/agent-harness-verification-bottleneck.md`.

**No install. No clone. No trade.**

## Snippets

> We also propose harness-to-model decision transfer, moving selected observations and task-state decisions from fixed harness rules to the model. [Source: arXiv 2610.22200, abstract]

> Code execution is a key feature of our agent design: it lets intermediate results determine subsequent operations and enables models to apply their existing programming capabilities directly to computer interaction. [Source: arXiv 2610.22200, abstract]

> Across four real macOS tasks under our real-device harness, selected Qwen3.8-Max runs use 19.4 times as many reported reasoning tokens as GPT-6 Astra. [Source: arXiv 2610.22200, abstract]
