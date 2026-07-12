---
title: Gold-standard study of lightweight game-playing agents (2607.06854)
type: source
tags: [source, arxiv, game-ai, poker, castle-sim, k151]
keywords: [lightweight agent, game-playing, benchmark, ablation, curriculum, information-bound]
related:
  - sources/arxiv-footsiesgym-2607.06514-2026-07-09.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: validated
read_status: deep-read
created: 2026-07-09
updated: 2026-07-12
---

## Relations

- @sources/arxiv-footsiesgym-2607.06514-2026-07-09.md — paired imperfect-info env steal
- @concepts/poker-arena-multi-axis-cognitive-profile.md — compute-budget / yardstick discipline for Researcher eval

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.06854](https://arxiv.org/abs/2607.06854) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.06854-a-gold-standard-study-of-what-makes-a-lightweigh.pdf` |
| **Domain** | Gin Rummy (+ Leduc Hold’em transfer); imperfect-info card games |

## Narrative

Controlled ablation of what makes a **lightweight** imperfect-info agent strong, graded against a **fixed expert yardstick that never enters training**. Relevant to Cemini HU sandbox compute budget and nemesis curriculum — not a call to train RL.

### What helps vs fails

| Helps | Fails |
|-------|-------|
| Trust-region updates | Dense short-/long-term reward shaping |
| Rising opponent curriculum (+ PFSP-style sampling) | Live LLM as train opponent (too slow) |
| Warm-start + keep best checkpoint | Imitation / DAgger (causal confusion) |
| Well-aimed sparse reward | Capacity chase (wider/deeper / fancy encoders) |

### Ceiling finding

Win-rate vs expert stays in a narrow band across MLP / conv / Deep Sets / attention / LSTM — **information-bound, not capacity-bound**. Fair ISMCTS (hidden cards re-dealt) stayed weak (~26%); oracle search with true hidden cards jumped (~85%). The gap is the value of hidden information.

**Cemini steal (K151):** prefer tougher yardstick villains + best-checkpoint discipline over raising MC sample counts; document in FootsiesGym→Raeth map. Pair with FootsiesGym exploitability advisory.

## Snippets

> "A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong" [Source: arXiv:2607.06854 title]

> "Evidence that the ceiling is information-bound, not capacity-bound." [Source: arXiv:2607.06854 abstract]

> "We never train against [the fixed expert]." [Source: arXiv:2607.06854 Introduction]
