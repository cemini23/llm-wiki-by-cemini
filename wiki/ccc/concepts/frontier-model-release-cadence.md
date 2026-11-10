---
title: "Frontier model release cadence — read the eval, not the launch post"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md
  - sources/newsletter-rss-latent-space-2026-11-07-ainews-anthropic-ipo-whither-now.md
  - sources/newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md
  - entities/models/claude-fable-5-2.md
  - entities/models/inkling-2-small.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: how should the operator read one week of frontier model releases?

Synthesised from three AINews roundups (2026-11-06, 2026-11-07, 2026-11-10).

## Narrative

In one week the field shipped Inkling 2 Small (open weights promised), Kimi K3.1 Pro, ERNIE-5.5-Flash-Base, Tencent Hy4, a Meta Muse upgrade, and Claude Fable 5.2 with Mythos 5.2.

Four recurring patterns are worth keeping.

### 1. Token price and task cost diverge

Fable 5.2 cut prices 20% per token and raised cost per task 31% ($67.16 to $88.15 on SemiAnalysis GDPx). It wrote hundreds to thousands of test cases and spawned subagents to check its work. The cheaper unit price funded more checking.

Rule: **compare models on cost per solved task, never on cost per token.**

### 2. Effort level is a configuration, not a slider

Fable 5.2 at High matched Opus 5.5 at Max for about half the cost per task. Cursor advised starting at the new default rather than carrying over 5.1 settings, because effort levels behave differently.

Rule: effort settings do not transfer across model versions. Re-baseline after every model change.

### 3. Benchmark harness changes the score

ARC-AGI-3 gave Fable 5.2 81.2% under the standard harness and 97.7% under the provider adapter harness. The gap is larger than most model deltas.

Rule: a cross-model claim is only valid on one harness and one budget. See `@concepts/benchmark-maintenance-debt.md`.

### 4. Small models win on cost, not on everything

Inkling 2 Small scored 31 on the Intelligence Index at $1.18 per task. Sonnet 5.5 scored higher and used a fifth of the output tokens, at $10.02 per task. Inkling beat Sonnet on FrontierCode 2.0 (25% against 11%) and lost badly on Terminal-Bench 4.0 (13% against 30%).

Rule: benchmark strength is domain-specific. Pick the lane per task class, which is the premise of `/route`.

### Also recorded

Inkling 2 Small was found swearing in 50 of 2,655 Vals runs, clustered late in long runs after repeated failed recoveries. A behavioural symptom at the end of a long run is usually a context or harness symptom, not a personality.

## Snippets

> "Fable 5.1 cost $10 per million input tokens and $50 per million output tokens. Fable 5.2 costs $8 and $40. Yet on GDPx ... SemiAnalysis paid $88.15 per task, up from $67.16." [Source: newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md]
