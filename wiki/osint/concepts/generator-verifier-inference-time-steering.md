---
title: Generator-verifier inference-time steering (VERITAS pattern)
type: concept
tags: [concept, verifier, self-improvement, inference-time, k123]
keywords: [VERITAS, Best-of-N, generator-verifier, gradient-free verifier, D_auto, policy steering]
related:
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md
  - sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
  - concepts/rlvf-verifier-feedback-training.md
  - concepts/relaxed-nfl-auto-formalization.md
  - concepts/non-markov-belief-state-benchmarks.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/llm-agent-systems.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/code-as-agent-harness.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
maturity: draft
created: 2026-06-18
updated: 2026-06-26
---

## Relations

- @sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md — VERITAS robotics paper (K123)
- @sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md — trajectory risk bounds (K125)
- @concepts/probabilistic-agent-policy-verification.md — DRO global bound vs pointwise Best-of-N
- @concepts/continual-harness-online-self-improvement.md — harness self-edit vs external verifier
- @concepts/code-as-agent-harness.md — static harness tests as verifier substrate
- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-axis scores as verifier signals
- @concepts/devfun-poker-agent-challenge-2026.md — Cemini deployment context

## Raw Concept

K123 ingest of arXiv **2606.18247**. Separates **action generation** from **action verification** at inference: generator proposes N candidates; verifier picks best **without gradient updates**; verified trajectories feed offline improvement (**D_auto** flywheel).

## Narrative

### VERITAS loop (robotics)

1. **Generator** — frozen generalist policy samples N action candidates per step.
2. **Verifier** — gradient-free visual scorer ranks candidates; execute argmax.
3. **D_auto** — log verified trajectories; behavior-clone generator → persistent gain.

### Poker / Cemini mapping [TENTATIVE]

| VERITAS role | Cemini analog |
|--------------|---------------|
| Generator | `cemini_decide.py` heuristic / gin lane |
| Verifier | Legality + `test_cemini_regression.py` oracle + MC equity floor + M₈/M₉ axis checks |
| Best-of-N | Sample {fold, call, raise sizes} when ambiguous; pick highest verifier score |
| D_auto | Researcher trajectory export → HL analyst loop patches |

Distinct from **Raeth nine-axis** (post-hoc eval) — verifier runs **before** action submit. Distinct from **continual harness** (2605.09998) — VERITAS does not edit prompts/harness; it filters generator outputs.

**K125 extension:** arXiv 2606.20510 adds **trajectory-level** conservative risk bounds when individual verifier predicates are noisy/correlated — stack under K123 pointwise gates for multi-street hands.

**K131 extension:** **RLVF** (2606.23913) trains toward verifier-pass trajectories; **Relaxed NFL** (2606.24443) adds two-stage informal→elaborated→verified pipeline — complements inference-time Best-of-N.

**Posture:** REFERENCE until VERITAS / Google code licenses verified. Poker briefs stage Best-of-N (K123) + trajectory bound spike (K125) + Relaxed NFL trace schema (K131) for Researcher Round.

## Snippets

> "Inference-time verification consistently outperforms vanilla generalists without training on additional demonstration data." [Source: arXiv:2606.18247 abstract (retrieved 2026-06-18)]

## Dead Ends

- Pixel visual verifier does not transfer to NLHE — need symbolic/state verifier design.
- Best-of-N at Arena latency may blow action timeout budget [NEEDS VERIFICATION 2026-06-26] — profile on `--dry-run` first.
