---
title: "Red Queen Gödel Machine — co-evolving agents and evaluators (2606.26294)"
type: source
tags: [source, arxiv, self-improvement, verifier, k134]
keywords: [RQGM, controlled utility evolution, co-evolution, godel machine, non-stationary utility]
related:
  - concepts/red-queen-controlled-utility-evolution.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/code-as-agent-harness.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/llm-agent-systems.md
  - concepts/wiki-tooling-evaluation.md
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
maturity: draft
read_status: read
created: 2026-06-29
updated: 2026-06-29
clusters: [agent-harness, verifier, poker-arena]
---

## Relations

- @concepts/red-queen-controlled-utility-evolution.md — synthesis page
- @concepts/generator-verifier-inference-time-steering.md — VERITAS Best-of-N cluster extended
- @concepts/poker-arena-multi-axis-cognitive-profile.md — nine-axis evaluators as co-evolving utilities

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators |
| **Authors** | Iacob et al. (Cambridge MLSys Lab, NVIDIA, Flower Labs, …) |
| **arXiv** | [2606.26294](https://arxiv.org/abs/2606.26294) |
| **sha256** | `8bfaede03121444d0507e57f20c64eddf4d2c3bb29904f64d7cb6de5023fc748` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.26294-2606.26294v1-the-red-queen-g-del-machine-co-evol.pdf` |
| **Retrieved** | 2026-06-29 |
| **Read status** | deep-read (abstract + Sec. 3–5 + poker mapping) |

## Narrative

**RQGM** extends Darwin/Huxley/Hyper Gödel Machines by **co-evolving task agents and learned evaluators** under **controlled utility evolution**: search runs in **epochs** with a **frozen evaluator** grading task agents; at epoch boundaries a challenger evaluator replaces the incumbent only if it wins on a **ground-truth anchor** (ε-best-belief score). **Selective erasure** drops utility records tied to the displaced evaluator so prior self-improvement guarantees hold per epoch while the objective evolves across epochs.

### Empirical headline results [TENTATIVE — preprint]

| Domain | Result |
|--------|--------|
| Polyglot coding | 71.7% pass vs HGM-H 69.9%; **1.35×–1.72×** fewer search tokens via cheap code-review evaluator |
| Paper writing | Acceptance **1.78×–1.86×** vs prior SOTA under diverse judge panel |
| Paper reviewing | Adversarial epoch corrects **1.91×** over-acceptance of AI papers |
| Proof grading | Co-evolved grader **+9%** GT accuracy vs static baselines |

### Cemini / poker mapping

| RQGM mechanism | Researcher Round analog |
|----------------|-------------------------|
| Frozen epoch evaluator | Fixed nine-axis rubric + harness legality for one sandbox submit generation |
| Challenger promotion on GT anchor | Hold-out spot suite + PokerKit oracle — promote new axis weights only if GT pass rate ↑ |
| Selective erasure | Drop trajectory scores computed under old rubric when rubric version bumps |
| Adversarial reviewer epoch | Bias correction when LLM judge over-calls “good” reasoning YAML |

**Posture:** REFERENCE — no public code license at ingest. Steal **epoch + selective erasure + GT-gated evaluator promotion** for poker verifier stack (K134 brief); do not mount full RQGM tree search on prod.

## Snippets

> "Self-improvement guarantees hold per epoch as the objective evolves across them." [Source: arXiv:2606.26294 abstract (retrieved 2026-06-29)]

> "At an epoch boundary, a challenger replaces the frozen evaluator only if it statistically outperforms the incumbent on ground truth." [Source: arXiv:2606.26294 §3 (retrieved 2026-06-29)]

## Dead Ends

- Full archive tree search (Thompson sampling over clades) — out of scope for Arena latency and compute budget.
- Scientific-paper reviewing domain — no direct prod hook; steal debiasing epoch pattern only.
