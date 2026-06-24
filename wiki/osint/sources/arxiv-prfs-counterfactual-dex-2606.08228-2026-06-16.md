---
title: "Post-Rejection Follow-up Sampling — counterfactual DEX filter measurement (arXiv 2606.08228)"
type: source
tags: [source, arxiv, algorithmic-trading, dex, counterfactual, filter-calibration, k119]
keywords: [2606.08228, prfs, counterfactual, rejection-sampling, dex, zenodo]
related:
  - concepts/post-rejection-follow-up-sampling.md
  - concepts/event-based-prediction-market-ml.md
  - concepts/quant-finance.md
  - concepts/llm-agent-systems.md
  - concepts/cl-amm-dynamic-fees-lvr.md
  - sources/arxiv-cl-amm-dynamic-fees-lvr-2606.23070-2026-06-24.md
updated: 2026-06-24
clusters: [quant-finance, crypto, prediction-markets]
---

## Relations

- @concepts/post-rejection-follow-up-sampling.md — K119 methodology page
- @concepts/event-based-prediction-market-ml.md — rejection-criteria / silent-backtest failure modes
- @concepts/quant-finance.md — corpus hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading |
| **Author** | Arati Uday Kamat (independent) |
| **arXiv** | 2606.08228 |
| **DOI** | 10.5281/zenodo.20043516 |
| **sha256** | `27ce587050bd10c5d268f6d70bfbeb3f0077995ba08ac2954c5dec55fafc2f2c` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.08228-tier2-sweep.pdf` |
| **Retrieved** | 2026-06-16 (Tier-2 sweep Q4/Q5) |
| **Read status** | read (abstract + dataset summary) |

## Narrative

**PRFS** tracks **rejected** DEX token candidates forward (price + liquidity, up to 24h) to measure counterfactual outcomes — filter precision against **actual** post-rejection paths, not synthetic backtests.

**Companion dataset (paper):** ~67k forward-observation rows; 2,997 rejection events; 457 mints; 8-day window (2026-04-10–19 UTC). ~55% of events get ≥1 observation; binding constraint is **per-event horizon density** (median 2 samples/event, bimodal distribution).

**Generalization claim:** any system where rejections ≫ executions (PM scanners, conviction filters, cross-venue gates).

**Cemini posture:** **REFERENCE** — methodology for PM/Kalshi **filter false-negative audit** when prod logs rejections without follow-up. No prod install; Zenodo dataset is DEX-specific.

## Snippets

> "The counterfactual outcome of rejected candidates… is rarely measured." [Source: arxiv-2606.08228-tier2-sweep.pdf abstract]

> "PRFS is dataset-independent. It generalises to any algorithmic decision system in which rejections substantially outnumber executions." [Source: arxiv-2606.08228-tier2-sweep.pdf abstract]
