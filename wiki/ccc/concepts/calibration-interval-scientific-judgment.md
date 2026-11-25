---
title: "Calibration intervals — score the confidence, not only the answer"
type: concept
related:
  - sources/arxiv-sciresearch-eval-scientific-judgment-2611.21541.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/epistemic-humility-identify-solve-escalate.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: how do you test whether an agent knows when its answer is unreliable?

Synthesised from one source: `@sources/arxiv-sciresearch-eval-scientific-judgment-2611.21541.md` (SciResearch-Eval, 2611.21541).

## Narrative

SciResearch-Eval asks an agent to measure a material's thermal properties. The agent designs experiments and fits a heat-conduction simulator that may be under-resolved or physically wrong. It must report each property with a **95% interval**.

The benchmark can then score calibration: how often the interval contains the truth. A confident wrong answer fails; a wide interval that covers the truth passes on coverage but loses on width.

### Reported results

- When the simulator is missing physics, most models report wrong values while stating 95% confidence. Coverage is 20%–62%, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2.
- At default effort, failing Claude 5.5 models rarely diagnose the missing physics (Opus in 35% of episodes, against 66% for Astra).
- Astra and Fable avoid the trap partly by experiment design: they choose conditions where the flawed simulator is accurate, such as gentle heating.
- Asking for wider intervals does not help. Stating the strategy improves interval scores 1.6–2.5-fold, but coverage barely moves.
- An effort ablation shows the correction is latent: at maximum effort Opus improves more than tenfold and is no longer behind Astra at default, but uses 13–31 times more reasoning.

### Operating rule

Request an interval with the answer. An interval is a testable claim, and it separates "wrong" from "wrong and unaware". For Cemini, a backtest result should carry a range and the assumptions it depends on, not a single number.

Caveat: the intervals are scored against exact ground truth on a simulator. Real-world claims rarely have that. [TENTATIVE]

## Snippets

> "A good fit, in short, is not evidence of a right answer." [Source: arxiv-2611.21541-sciresearch-eval-evaluating-scientific-judgment.pdf p.1]

> "Their ranges contain the truth in 20%–62% of cases, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2." [Source: arxiv-2611.21541-sciresearch-eval-evaluating-scientific-judgment.pdf p.1]
