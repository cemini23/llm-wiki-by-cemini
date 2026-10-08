---
title: "Before They Can Solve: predicting post-training coding-agent performance (arXiv 2610.10478)"
type: source
tags: [source, k285, arxiv, agents, evals, coding]
keywords: [base-model-screening, decisive-step, decisive-action-bpb, patch-mcq, swe-bench, spearman, nvidia]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/agents-last-exam-benchmark.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/agents-last-exam-benchmark.md

## Raw Concept

| Title | Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models |
| Authors | Tan Yu, Alexander Bukharin, Khushi Bhardwaj, Jiantao Jiao et al. (NVIDIA; Univ. of Minnesota; UC Berkeley) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10478-before-they-can-solve-predicting-post-training-c.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10478v1 |
| read-status | read |

## Narrative

Which base checkpoint is **worth** agentic post-training? This paper predicts that **without running the model as an agent** — the expensive part — by using successful post-trained trajectories as a **lookahead signal**.

### The decisive step

Find `T* = min{T ∈ C : V(P_{≤T}) = 1}` — the first step whose cumulative patch flips the verifier from FAIL to PASS. Then three cheap probes:

1. **Decisive-Action BPB** — byte-normalised NLL of the *golden* action.
2. **Patch MCQ** — select the golden action among verifier-rejected distractors by answer-letter likelihood.
3. **Prefix-conditioned pass@K** — sample K continuations, verify.

### Results (ten base checkpoints)

- **Decisive-Action BPB Rank-Spearman ρ = 0.964** (vs 0.915 for all-step BPB); SWE-Multilingual **0.976**.
- Patch MCQ ρ = 0.867; prefix pass@K ρ = 0.951.
- **Bounded code benchmarks fail:** HumanEval ρ = **−0.394**, MBPP ρ = 0.091.

### Why it matters here

Two transferable points: (1) **a base model's rank on SWE-bench can be screened cheaply** from the *decisive* step, not the whole agent run; (2) **bounded benchmarks anti-correlate** with agentic performance (HumanEval ρ = −0.394) — another reason not to trust a small benchmark for an agent decision. **© NVIDIA, all rights reserved; no code.** Route: CCC/cyber.

## Snippets

> "Decisive-Action BPB Spearman ρ 0.964 (vs 0.915 all-step BPB)." [Source: arxiv-2610.10478-before-they-can-solve-predicting-post-training-c.pdf]

> "Bounded code benchmarks fail: HumanEval ρ=−0.394, MBPP ρ=0.091." [Source: arxiv-2610.10478-before-they-can-solve-predicting-post-training-c.pdf]
