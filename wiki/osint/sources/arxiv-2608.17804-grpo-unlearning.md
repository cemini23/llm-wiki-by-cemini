---
title: "GRPO LLM unlearning — reward specification vs RWKU diagnostic sufficiency (2608.17804)"
type: source
tags: [arxiv, unlearning, grpo, rlvr, eval, k245]
keywords: [GRPO, RWKU, reward-hacking, unlearning, LoRA, Qwen2.5]
related:
  - entities/tools/grpo-llm-unlearning.md
  - concepts/harness-optimization-bench.md
maturity: draft
created: 2026-08-22
updated: 2026-08-22
read_status: skimmed
---

## Relations

- @entities/tools/grpo-llm-unlearning.md — Apache-2.0 Extract/REFERENCE; 0 Integrate GO
- @concepts/harness-optimization-bench.md — reward semantics select endpoints; benchmark score ≠ behavior

## Raw Concept

- **title:** An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning
- **author:** Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez (University of Valencia)
- **type:** arXiv paper
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.17804-an-empirical-study-of-reward-specification-and-b.pdf`
- **retrieved:** 2026-08-22
- **pages:** 32 (abstract + intro + method + results tables; figures 2–4 are training diagnostics)
- **read-status:** skimmed
- **arXiv:** 2608.17804
- **sha256:** `9424b6b6279416c4d0fcc06bfd2557fb4b4b138964cbf1d807b634a8dae0254e`
- **code:** https://github.com/rubenbalbastre/grpo-llm-unlearning

## Narrative

Diagnostic study, not a new unlearning algorithm. Practical LLM unlearning is usually scored as “forget target + keep utility.” In generative QA that underspecifies a third behavior: on a target-adjacent prompt that still admits a broader answer, the model should answer at that level instead of leaking, evading, or refusing.

Controlled LoRA-GRPO on RWKU with Qwen2.5-Instruct (0.5B–7B). Four repository-aligned rewards: **R0-Lex** (lexical suppression), **R1-AntiRefusal** (lex + anti-refusal via garak), **R2-Rubric** (LLM-judge useful broad-topic, no target leakage), **R4-Refusal** (contrastive: reward refusal). Cold-start vs SFT warm-start (policy-support intervention so GRPO can sample the intended completion).

**Main claim:** optimization success ≠ behavioral unlearning. RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics disagree. Same forget-overlap drop can be refusal collapse, classifier-aligned boilerplate, residual leakage, or genuine broad-topic answering.

Held-out endpoints (Table 2): 0.5B/1.5B cold R0-Lex → refusal 1.0, helpfulness 0 (refusal collapse). Warm R2-Rubric terminal rollouts (Table 3) reach median broad-topic helpfulness **0.812–0.906** with semantic leak ≤0.047 and refusal ≤0.031. RWKU forget-overlap drops similarly across all four 3B warm rewards — so the benchmark cannot rank endpoints. Fluency: 0.5B cold R0-Lex / R4-Refusal −2.138 / −2.650 vs R1 −0.068 and R2 +0.120.

Cemini steal: do not promote a reward, judge, or unlearning score without a held-out behavioral audit. CCC: do not swap `/route` or train GRPO unlearning in prod. Cyber: no exploit recipes — mechanism only.

Phase-0: companion repo **Apache-2.0** via `gh api` 2026-08-22; 0 stars; Extract/REFERENCE; no clone this wave.

## Snippets

> Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified. [Source: arxiv-2608.17804 p.1]

> The experiments show that optimization success is not equivalent to behavioral unlearning: RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics can point to different conclusions. [Source: arxiv-2608.17804 p.1]

> Warm-start R2-Rubric has the highest median broad-topic helpfulness at every model size, ranging from 0.812 at 0.5B to 0.906 at 3B. [Source: arxiv-2608.17804 p.7 Table 3]

Paper: https://arxiv.org/abs/2608.17804 [Source: URL (retrieved 2026-08-22)]
