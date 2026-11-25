---
title: "Harness adapter — specialise the harness, freeze the policy"
type: concept
related:
  - sources/arxiv-beyond-weight-updates-evolving-agent-harnesses-2611.25380.md
  - entities/tools/harvo.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/curated-vs-self-generated-skills.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: is a weight update the only way to specialise an agent for a domain?

Synthesised from one source: `@sources/arxiv-beyond-weight-updates-evolving-agent-harnesses-2611.25380.md` (2611.25380, Harvo).

## Narrative

The paper treats the harness as the object of optimization and keeps the policy frozen. An outer loop observes failed trajectories, reflects in natural language, edits prompts, tool schemas, skills or exemplars, and keeps variants that improve a fitness score. The optimizer is GEPA. The output is a **harness adapter**: a portable artifact loaded per vertical domain.

The analogy the authors use is LoRA. Specialisation arrives as a small composable delta, not a new checkpoint.

### Results on Codev

- SWE-bench Verified, OfficeBench and Terminal-Bench, all show the same pattern.
- Weight updates give the strongest single-path gain.
- Harness evolution recovers most of that gain at a small fraction of the compute.
- Both together are best.

### The failure it avoids

SFT specialisation moved a Qwen3.5-4B policy off its pretrained distribution. Reasoning truncation rose from 8.8% to 13.2%, and format-rescue success fell from 1.2% to 0.0%. Reasoning chains got shorter. A frozen policy cannot suffer this, because nothing moves.

### Cost shape

A harness adapter needs no GPU training. It needs trajectories and an optimizer run. That is cheap enough for a laptop, which makes it a realistic first step for `/route` lane tuning before any fine-tune.

Caveat: one independent author, 13 pages, self-reported. [TENTATIVE]

## Snippets

> "Weight updates give the strongest single-path gains, harness evolution recovers most of those gains at a small fraction of the compute, and combining both paths is best overall." [Source: arxiv-2611.25380-beyond-weight-updates-evolving-agent-harnesses-f.pdf p.1]

> "The specialization path does not move the weights at all." [Source: arxiv-2611.25380-beyond-weight-updates-evolving-agent-harnesses-f.pdf p.1]
