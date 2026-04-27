---
title: "Predicting Country Instability Using Bayesian Deep Learning and Random Forest"
type: source
tags: [pdf, ml-methods, time-series]
clusters: [ml-methods, time-series]
related:
  - entities/data-sources/gdelt.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/data-sources/gdelt.md

## Raw Concept

- Original title: Predicting Country Instability Using Bayesian Deep Learning and Random Forest
- Authors: Adam Zebrowski, Haithem Afli
- Affiliation: ADAPT Centre, Munster Technological University, Cork, Ireland
- Type: PDF, conference paper (IEEE template)
- Location: research for cemini/gdelt 1 3:29.pdf
- Length: short conference paper
- Retrieved: 2026-04-23
- Publication date: 2024/2025 (IEEE conference-template, unlabeled year)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: ml-methods, time-series

## Narrative

The paper trains a Bayesian deep learning model plus a Random Forest on GDELT event data (CAMEO codes, Goldstein-scale averages, event counts) to predict country-level "instability" episodes. Evaluated on Pakistan, the model claims 85% accuracy. The feature set is standard GDELT aggregation — counts, tone averages, Goldstein scores binned by time window — and the label is a handcrafted "instability" indicator derived from thresholding event intensities.

Rigor is thin relative to the top papers in this batch: single-country evaluation (Pakistan), single label construction (no sensitivity analysis to instability threshold), no comparison to simple persistence baselines, limited discussion of temporal leakage. The 85% accuracy figure is also hard to interpret without a base-rate disclosure — for imbalanced time-series the number can be trivially hit by a "predict stable" majority classifier.

That said, the paper is useful as a *reference implementation* for a GDELT → instability pipeline that could feed a broader geopolitical alt-data signal for Cemini. It documents specific CAMEO code aggregations and Goldstein-scale feature engineering choices that are reproducible. Treat the accuracy number skeptically; the value is in the feature-engineering recipe, not the headline metric.

## Key findings

- Bayesian DL + Random Forest on GDELT CAMEO/Goldstein features; 85% accuracy on Pakistan instability prediction.
- Feature engineering: CAMEO event-code aggregation, Goldstein-scale time-windowed means, event counts.
- Single-country evaluation — not demonstrated to transfer.
- Missing base-rate / persistence-baseline disclosure, so accuracy is hard to interpret.
- Reference value is in the pipeline recipe (GDELT → features → label), not the headline number.

## Snippets

- **abstract** — "We achieve 85% accuracy on instability prediction for Pakistan using GDELT event features" — the headline claim, taken with skepticism on base rates.
- **methodology** — Feature engineering relies on CAMEO code aggregation and Goldstein scale averaging at configurable time windows — reproducible recipe.
- **limitations** — Single-country, single-threshold evaluation — rigor gap flagged for any re-use.
