---
title: "VeriFine: scaling verification for self-improvement in embodied reasoning (arXiv 2610.08761)"
type: source
tags: [source, k284, arxiv, agents, verification, evals, self-improvement]
keywords: [verifine, rubric-judge, grpo, coactive-calibration, judge-distillation, autonomous-driving]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/agent-tool-use-verification.md

## Raw Concept

| Title | VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning |
| Authors | Zewei Zhou et al. (NVIDIA; UCLA; UC Berkeley; Stanford) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08761-verifine-scaling-verification-for-self-improveme.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08761v1 |
| Site | `veri-fine.github.io` |
| read-status | read |

## Narrative

A harness that **scales verification** for embodied reasoning (autonomous driving, robot navigation) by **co-evolving three things: policy, curriculum, and judge.**

### Method — two coupled loops

**Policy Improvement Loop.** A **reference-free rubric judge** `Jϕt(xi, ŷi) = (si, zi, ei)` diagnoses failures, builds an adaptive curriculum `Dt = CurriculumSelect(U, πθt, Jϕt)`, and optimises with GRPO:

    R(θ) = E[si − β · D_KL(πθ ‖ πref)]

**Judge Improvement Loop.** Activates on plateau, detected by `Gt = |ΔRjudge_t − ΔPt|`, using **coactive calibration** on informative failures. A teacher–student judge distillation keeps the judge improving.

### Results

- Driving reasoning score **60.56 → 71.61 (+18.2%)**; reference-free score **68.05 → 83.13 (+22.2%)**.
- minADE6 **1.049 → 1.029**.
- **Judge–human Pearson correlation rises 0.53 → 0.82** across three rounds — the judge gets *closer to humans* as it scales.
- Beats LingoJudge baselines.

### Why it matters here

The reusable claim: **a judge is not fixed — it co-evolves with the policy, and human agreement rises with scale.** Extends the `llm-as-a-verifier` and `agent-tool-use-verification` threads, and pairs with the K283 CLIFT result. **"© 2026 NVIDIA. All rights reserved." — no code repo stated.**

## Snippets

> "Judge–human Pearson correlation rises 0.53 → 0.82 across 3 rounds." [Source: arxiv-2610.08761-verifine-scaling-verification-for-self-improveme.pdf]

> "Gt = |ΔRjudge_t − ΔPt| — the judge-improvement loop activates on plateau." [Source: arxiv-2610.08761-verifine-scaling-verification-for-self-improveme.pdf]
