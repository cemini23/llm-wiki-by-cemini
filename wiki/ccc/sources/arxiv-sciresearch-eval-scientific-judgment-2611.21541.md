---
title: "SciResearch-Eval — calibrated intervals and scientific judgment"
type: source
related:
  - concepts/calibration-interval-scientific-judgment.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/eval-integrity-minimum-standards.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents |
| Author | Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora (LLNL) |
| Type | arXiv paper (cs.AI), 2611.21541 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.21541-sciresearch-eval-evaluating-scientific-judgment.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 28 |
| Read status | read |

## Narrative

The benchmark asks an agent to measure a material's thermal properties by designing experiments and fitting a heat-conduction simulator. The simulator may be under-resolved or physically wrong. The agent must report each property with a 95% interval.

Held-out split: 93 tasks, 9 models, 2,511 episodes. The design deliberately separates a good fit from a correct answer.

Results:

- Models handle procedural traps well.
- When the simulator is missing physics, most models report wrong values while stating 95% confidence. Their intervals contain the truth in 20%–62% of cases, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2.
- At default effort the failing Claude 5.5 models rarely diagnose the missing physics (Opus in 35% of episodes, against 66% for Astra).
- Astra and Fable design experiments where the flawed simulator is accurate, such as gentle heating. This keeps Astra calibrated even when it cannot name the cause.
- Asking for wider intervals does not help. Stating the strategy improves interval scores 1.6–2.5-fold, but coverage barely moves.
- A pre-registered effort ablation shows the correction is latent in Claude 5.5 models: at maximum effort Opus improves more than tenfold and is no longer detectably behind Astra at default, but with 13–31 times more reasoning. Older and open-weight models gain nothing.

The transferable point for Cemini is the **calibration** measure. An agent that says "95% sure" gives a testable claim. A bare answer does not. This paper scores the interval, not just the value.

## Snippets

> "A good fit, in short, is not evidence of a right answer." [Source: arxiv-2611.21541-sciresearch-eval-evaluating-scientific-judgment.pdf p.1]

> "Their ranges contain the truth in 20%–62% of cases, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2." [Source: arxiv-2611.21541-sciresearch-eval-evaluating-scientific-judgment.pdf p.1]
