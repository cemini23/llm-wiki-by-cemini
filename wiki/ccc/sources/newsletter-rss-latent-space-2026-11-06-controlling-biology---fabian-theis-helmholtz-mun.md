---
title: "Latent Space — Controlling Biology with Fabian Theis"
type: source
related:
  - concepts/baseline-and-metric-calibration.md
  - concepts/auto-researcher-human-similarity.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Controlling Biology - Fabian Theis, Helmholtz Munich |
| Author | Latent Space (interview) |
| Type | newsletter / podcast notes (RSS) |
| Location | `research to be indexed/newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-06 |
| Read status | read |

## Narrative

An interview with Fabian Theis on Virtual Cell modelling and the $1.8B Biohub data effort. The ccc-relevant content is the evaluation argument, not the biology.

The 2025 Arc Virtual Cell Challenge produced a negative result. Constant baselines, not even linear models, often beat sophisticated models on perturbation prediction. One follow-up paper showed that many evaluation metrics are poorly calibrated. Such metrics can reward an uninformative mean prediction because most genes barely change. With better-calibrated metrics, deep models beat the mean baseline.

Theis's own reading is stronger. Perturbation prediction on the current datasets is not a hard enough problem to justify complex algorithms. The hard problem is multi-scale prediction across molecule, cell, niche, tissue, organ, and organism, and the data for that does not exist yet. Biohub is the attempt to build it.

The transferable lesson for any agent eval: **a baseline that looks trivial is often a metric defect, not a model result.** Check the metric before you accept the ranking, and check whether the task is hard enough to separate methods at all.

## Snippets

> "a slew of papers pointed out that constant baselines (not even linear!) often beat sophisticated models for 'Perturbation Prediction'." [Source: newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md]

> "many existing evaluation metrics are poorly calibrated: they can reward an uninformative mean prediction because most genes barely change." [Source: newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md]
