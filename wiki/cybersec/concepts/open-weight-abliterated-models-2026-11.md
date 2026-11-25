---
title: "Abliterated open-weight builds, November 2026 — what actually fits on a laptop"
type: concept
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/tools/artex.md
  - @image-gen-wiki/entities/models/inkling-2-mini.md
updated: 2026-11-22
maturity: draft
---
## Raw Concept

Five of the twenty URLs in the 2026-11-22 batch are decensored open-weight builds. The
question this page answers: **which ones can run on this machine, and what does
"abliterated" actually cost?**

Source: @osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md.

## Narrative

### The five, by footprint

| Model | Size | Fits 32 GB? | Licence | Tier |
|-------|------|-------------|---------|------|
| AtomicChat Inkling-2-Mini | 8.67–16.53 GB | **yes** | Apache-2.0 | Integrate |
| Nemotron-3.5-Super-VL-120B heretic | large A12B MoE | no | check | Watch |
| Kimi-K3-Uncensored | very large | no | check | Context |
| Qwen3-235B-A22B abliterated | ~120 GB+ | no | check | Context |
| MiniMax-M2.7-ultra-uncensored | 98.7–457 GB | no | **non-commercial** | Context |

Only the Inkling build is usable here. The rest are 100 GB and up, which puts them
outside a 32 GB machine and outside any laptop workflow.

### How the decensoring is done

MiniMax-M2.7 uses **Heretic v1.2.0 Arbitrary-Rank Ablation (ARA)**. That is the current
family name for the refusal-direction removal technique: find the direction in
activation space that separates refusing from complying, then ablate it.

The published numbers on the AtomicChat Inkling build are 0% English refusals, down from
100%, with 98% MMLU retention. [TENTATIVE — author-reported, not independently checked]

Treat retention figures as author claims. Ablation removes a direction, not a concept,
and the cost usually appears in tasks that resemble refusals — safety-adjacent reasoning,
not general knowledge. MMLU will not show it.

### The licence trap in this batch

**MiniMax-M2.7 ships a non-commercial licence.** Commercial use needs prior written
authorization from MiniMax. That is the first non-commercial licence in four batches,
and it is easy to miss because the model sits in the same list as MIT and Apache
builds.

A non-commercial model cannot enter any project that sells. That excludes every
Priority #1 project by definition, whatever the capability.

### What matters for the operator lab

The relevant question is not "how uncensored" but "does it call tools reliably at this
size". A 5.4B-effective-active looped MoE is fast enough to be a planner, and a
1M-token context is enough to hold an engagement. Those two properties decide fitness,
not the refusal rate.

The lab repository does not exist on this machine, so none of this is actionable today.
The page records the shortlist for when it does.

## Snippets

> Non-Commercial License (tagged other; MIT-style terms for non-commercial use only;
> commercial use requires prior written authorization from MiniMax).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 1]

> Author-reported 0% English refusals (down from 100%) and 98% MMLU retention.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 11]

## Dead Ends

- **Reading MMLU retention as "no capability loss".** Ablation damage shows up on
  refusal-adjacent tasks, which MMLU does not probe.
- **Placing a non-commercial model in a revenue project.** It is excluded by licence,
  not by performance.
