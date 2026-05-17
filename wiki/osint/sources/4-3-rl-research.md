---
title: "CEMINI FINANCIAL SUITE — Research Report: RL Retraining Pipeline Hardening for April 2026 Retrain Window"
type: source
tags: [docx, rl-marl, cemini-internal, k49]
clusters: [rl-marl]
related:
  - concepts/rl-marl-research.md
  - concepts/rl-retrain-pipeline-hardening.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus
- @concepts/rl-retrain-pipeline-hardening.md — concept page promoted from this source; the 11 findings as a reusable pre-retrain hardening checklist

## Raw Concept

- **Original title**: CEMINI FINANCIAL SUITE — Research Report: RL Retraining Pipeline Hardening for April 2026 Retrain Window
- **Author(s)**: Cemini internal research (commissioned RL-pipeline hardening review)
- **Type**: DOCX
- **Location**: research for cemini/4_3 RL research.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: ~4,200 words; 11 numbered findings + Go/No-Go checklist
- **Read status**: deep-read
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl

## Narrative

Internal hardening review of the CeminiSuite **MAPPO** retraining pipeline ahead of the **April 14–17, 2026 retrain window**. The 5-agent MARL setup (MacroForecaster, BullAdvocate, BearAdvocate, RiskAssessor, Trader; ~151,000 total parameters — ~85k actor across 5 agents + ~66k centralized critic) is judged architecturally sound but carrying critical vulnerabilities in data scaling, objective optimization, and state normalization. Eleven findings, each tagged Confirm / Refine plus an effort estimate and an IP-sale license filter (all CLEAR):

1. **Gradient accumulation** (effective batch 128 from physical 8) — valid, but advantage normalization must be computed over the *full global batch*, not per micro-batch, or GAE variance becomes skewed and destabilizes the centralized critic.
2. **Scalar logging** — append `loss.item()`, never raw loss tensors; retained autograd graphs leak memory and OOM-kill the 128GB box. Detach actor and critic losses separately.
3. **Safetensors checkpointing** — replace insecure pickle `.pt`; caveat: clone optimizer-state tensors to contiguous memory (`v.clone().contiguous()`) to avoid the shared-buffer `RuntimeError`. Apache-2.0, IP-clean.
4. **Lagrangian CVaR risk constraint** — turns the MDP into a CMDP; compatible with `MaskedCategorical` action masking; the dual variable λ must be updated **per epoch**, never per batch (per-batch updates cause severe policy oscillation).
5. **Multiplicative observation noise** — superior to additive for low-SNR financial data, but exclude regime flags, boolean intel signals, action masks, and portfolio allocations to preserve the Markov property.
6. **Dimensionless state scaling** — eradicate all absolute price levels from the 34-dim feature vector; scale new `intel_stream_log` features (`conviction_composite` via expanding-window Z-score, `debate_conviction_delta` via tanh, `pattern_match_bullish_pct` via min-max to [-1,1]).
7. **Data readiness gate — NO-GO trigger:** the current ~5,000 BTC-USD + ~2,300 SPY rows are far too sparse; the 10x rule demands the dataset be expanded (block bootstrapping / GBM simulation / synthetic augmentation) to a **minimum 100,000 transition tuples** before retraining.
8. **Two-phase curriculum learning** — 30-day stationary warm-up → full 60-day complexity; <50 lines of pure PyTorch, advance when critic explained-variance stabilizes.
9. **Checkpoint validation** — surrogate loss is insufficient; require offline metrics (explained variance, action diversity) before promotion.
10. **Weight warm-starting — rejected:** the prior checkpoint has a data-duplication bug (memorized ~30 states); warm-starting risks negative transfer and plasticity loss — mandate a **cold start** with orthogonal init and a fully cleared Adam state.
11. **Go/No-Go checklist:** 5 conditions — ≥100k tuples, dimensionless scaling verified, global advantage normalization, epoch-level Lagrangian updates, total cold-start init.

## Snippets

> "The April 14–17 retrain should NOT proceed with only 5,000 rows of data... If historical data for the intel_stream_log is limited to 7 days, synthetic data augmentation techniques... must be employed to expand the dataset to a minimum of 100,000 transition tuples before initiating the MAPPO retrain." [Source: 4_3 RL research.docx, §7 Data Readiness Gate]

> "Attempting to warm-start from this corrupted checkpoint—even partially, such as loading only the centralized critic's weights—introduces an extreme risk of Negative Transfer and Loss of Plasticity... The retrain must be a strict Cold Start." [Source: 4_3 RL research.docx, §10 Weight Warm-Starting vs. Cold Start]

> "Updating the dual variable λ every batch is a fatal anti-pattern. Micro-batch estimates of CVaR are extremely noisy, especially in fat-tailed financial time series... The mathematically sound approach is to update λ every epoch." [Source: 4_3 RL research.docx, §4 Lagrangian Dual Variables]
