---
title: "Beyond Weight Updates — evolving agent harnesses for domain specialization"
type: source
related:
  - concepts/harness-adapter-frozen-policy-specialization.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/curated-vs-self-generated-skills.md
  - entities/tools/harvo.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization |
| Author | BoHao Chen (independent) |
| Type | arXiv paper (cs.AI), 2611.25380 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.25380-beyond-weight-updates-evolving-agent-harnesses-f.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 13 |
| Read status | read |

## Narrative

The paper frames agent specialization as two paths: move the weights (RL or SFT), or move the harness and keep the policy frozen. It studies the second path with **GEPA**, a reflective evolutionary optimizer, over the system prompt, tool schemas, skill library and planning scaffolding.

The output is a **harness adapter**: a portable artifact, loaded per vertical domain, that plays the same role as a LoRA delta. No GPU training is needed, and the adapter composes with weight-based RL.

Experiments use Codev, a Claude Code-style coding agent, on SWE-bench Verified, OfficeBench and Terminal-Bench. The pattern is consistent:

- Weight updates give the strongest single-path gain.
- Harness evolution recovers most of that gain at a small fraction of the compute.
- Combining both paths is best overall.

The paper also reports a failure mode of SFT specialization. After fine-tuning a Qwen3.5-4B policy, reasoning truncation rises from 8.8% to 13.2% and format-rescue success falls from 1.2% to 0.0%. Reasoning chains become much shorter. The authors argue that harness adapters avoid this stability–plasticity trade-off by construction, because the policy never moves.

This is a useful counterweight to the usual "specialize the model" instinct. For Cemini the cheap experiment is a harness adapter per lane — for example a `/route` worker profile — before any weight work. [TENTATIVE] single source.

## Snippets

> "Weight updates give the strongest single-path gains, harness evolution recovers most of those gains at a small fraction of the compute, and combining both paths is best overall." [Source: arxiv-2611.25380-beyond-weight-updates-evolving-agent-harnesses-f.pdf p.1]

> "After fine-tuning a Qwen3.5-4B policy, reasoning truncation rises from 8.8% to 13.2% and format-rescue success falls from 1.2% to 0.0%." [Source: arxiv-2611.25380-beyond-weight-updates-evolving-agent-harnesses-f.pdf p.1]
