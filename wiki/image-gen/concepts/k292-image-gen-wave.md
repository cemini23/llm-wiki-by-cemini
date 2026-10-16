---
title: K292 image-gen wave — graded verifiers for visual generation
type: source-hub
tags: [k292, image-gen, verification, reward-models]
keywords: [OmniVerifier, graded verifier, decomposition, pairwise, GenEval, diffusion RL, Flux]
related:
  - sources/arxiv-omniverifier-c1-2610.22355-2026-10-16.md
  - concepts/decomposed-graded-verifier.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
wire_status: policy_wired
---

## Relations

- @sources/arxiv-omniverifier-c1-2610.22355-2026-10-16.md
- @concepts/decomposed-graded-verifier.md

## Raw Concept

**OSINT K292 image-gen wave, 2026-10-16.** One arXiv paper. **No clone. No install. Code only, no weights.**

## Narrative

`arXiv 2610.22355` — **OmniVerifier-C1** (Tsinghua / Amap, Alibaba).

**The idea:** stop scoring generated images True/False. **Decompose the prompt into K sub-questions, judge each 0/1, return `S = (# satisfied) / K`.** A fraction is dense, inspectable and order-preserving where a gate is none of those.

**Pairwise beats pointwise when a reference exists** — the error term for reasoning drops out entirely. Empirically Maze 67.8 → **85.3** and Sudoku 77.7 → **90.0**.

**Generator-side results:** GenEval SD3.5-medium 0.66 → **0.77** graded (discrete binary reaches 0.68); FLUX.1-dev 0.68 → **0.79**. CLIPScore 32.8 → 34.4.

**Trained with Decoupled RL** on Qwen3-VL-8B, 80 steps: one global-score sample plus K binary sub-question samples, with judgment and scoring optimised as separate reward terms.

**The warning:** **excessive decomposition adds redundant sub-questions** and dilutes the fraction. Decomposition quality is the constraint, not quantity.

**Generalisation caveat:** the paper's own evaluation is limited to game environments with unique ground truth.

→ `@concepts/decomposed-graded-verifier.md`

## Snippets

> we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores [Source: arXiv 2610.22355, abstract]
