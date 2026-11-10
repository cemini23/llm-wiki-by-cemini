---
title: "Check the baseline and the metric before you believe the ranking"
type: concept
related:
  - sources/arxiv-task-efficient-agent-eval-cached-traces-2611.06803.md
  - sources/arxiv-auto-researchers-reconstruct-human-2611.12429.md
  - sources/newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md
  - sources/newsletter-rss-latent-space-2026-11-09-what-frontier-labs-buy-a-data-deep-dive-with-han.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/auto-researcher-human-similarity.md
  - concepts/expert-data-rl-environments.md
  - concepts/task-efficient-eval-cached-traces.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: how do you tell a model result from a metric defect?

Synthesised from four independent 2026 sources that reached the same conclusion from different fields.

## Narrative

Four sources, one pattern.

**Virtual cell perturbation prediction.** The 2025 Arc challenge produced a negative result: constant baselines, not even linear models, beat sophisticated models. A follow-up paper showed the metrics were poorly calibrated. They rewarded an uninformative mean prediction because most genes barely change. With better-calibrated metrics, deep models beat the mean.

**Agent benchmark scoring.** Terminal-Bench 2.1 repairs raised accuracy more than 10 points and moved ranks by up to three positions, while overall ordering stayed highly correlated (Spearman rho = 0.958). The number moved; the order did not.

**Auto-researcher scoring.** AutoHRS reports 0.29 to 0.65 on a 0 to 1 scale. Those numbers are only meaningful because the checklist was derived from a human reference and then filtered by an annotator. An unfiltered automated rubric produced generic questions.

**Expert RL environments.** Handshake's graders include penalty traps and dependency gates, and one agent still gamed the Excel grader. The grader is part of the object under test.

### The checking order

1. **Run the trivial baseline first.** Constant output, previous best, or the mean. If the baseline is competitive, stop and inspect the metric.
2. **Ask what the metric rewards.** A sparse-binary score rewards guessing. A mean-based score rewards hedging. A checklist rewards listing.
3. **Separate the number from the order.** A repair that moves scores without reordering systems is a calibration event, not a capability change.
4. **Attack the grader.** Before trusting a verifier, try to pass it without doing the task.

### Why it belongs in ccc

Most Cemini evals are self-built. A `run_*_backtest.sh` report and a sweep claim both depend on a metric that nobody attacked. The cheapest improvement is to state the trivial baseline next to every result.

## Snippets

> "many existing evaluation metrics are poorly calibrated: they can reward an uninformative mean prediction because most genes barely change. With better-calibrated metrics, deep learning models can outperform the mean baseline." [Source: newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md]
