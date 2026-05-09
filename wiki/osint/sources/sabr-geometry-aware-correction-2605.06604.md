---
title: "A Geometry-Aware Residual Correction of Hagan's SABR Implied Volatility Formula"
type: source
tags: [sabr, implied-volatility, options-pricing, machine-learning, hybrid-model, quantitative-finance]
keywords: [SABR, Hagan formula, implied volatility, residual correction, geometry-aware, neural network, quantitative finance]
related:
  - concepts/market-microstructure.md
  - entities/tools/hftbacktest.md
  - sources/scaling-moe-inference-expert-activation-2026.md
maturity: draft
created: 2026-05-09
updated: 2026-05-09
---

## Relations

- @concepts/market-microstructure.md — volatility surface modeling is a core microstructure primitive; this paper provides ML-enhanced SABR calibration
- @entities/tools/hftbacktest.md — HFT backtester requires accurate vol surface; SABR correction improves pricing fidelity
- @sources/scaling-moe-inference-expert-activation-2026.md — fellow arXiv 2604.x paper; both represent ML-for-quant-finance trend

## Raw Concept

**Title**: A Geometry-Aware Residual Correction of Hagan's SABR Implied Volatility Formula
**Authors**: Adil Reghai, Lama Tarsissi, Gérard Biau, Alex Lipton
**Affiliation**: Abu Dhabi Investment Authority (ADIA); Sorbonne Université; ADIA Lab
**Date**: 2026-05-08 (arXiv v2)
**arXiv**: 2605.06604 [q-fin.CP]
**Canonical location**: `cemini-librarian:/opt/cemini-bulk/research/2605.06604_sabr-geometry-aware-correction.pdf`
**Retrieved**: 2026-05-09 via preingest pipeline
**Read status**: read (full paper, 8 pages + appendices)

**Why this matters for Cemini**: Hybrid ML-analytical approach to SABR calibration — directly relevant to any vol-surface-dependent pricing or hedging in Cemini's derivatives stack. The residual-correction architecture (preserving Hagan's analytical backbone + ML correction) is a pattern that could generalize to other analytical approximations in Cemini's toolkit.

## Narrative

### Paper Summary

A hybrid framework combining Hagan's closed-form SABR approximation with a neural-network residual correction. Instead of replacing the analytical formula with a black-box model, the approach:

1. Uses Hagan's formula as a baseline estimator
2. Trains a neural network to learn the **residual error** between the Hagan approximation and high-precision Monte Carlo ground truth
3. Enriches the network input with **geometry-aware features** derived from the SABR stochastic differential equations (Poincaré half-plane representation)

**Key innovation**: Multiplicative correction structure `σ_corrected = σ_Hagan × (1 + Δ_θ(x, Λ))` — preserves analytical structure while capturing higher-order effects.

### Quantitative Results

| Architecture | Global R² | ATM R² | ITM R² | OTM R² | Inference |
|-------------|-----------|--------|--------|--------|-----------|
| Naive Deep Network | 0.73 | 0.72 | 0.73 | 0.74 | 120 μs |
| Geometric NN (GeoNN) | 0.94 | 0.93 | 0.94 | 0.96 | 240 μs |
| Residual NN (ResNN) | 0.92 | 0.87 | 0.93 | 0.95 | 530 μs |
| **GeoResNN (proposed)** | **0.97** | **0.95** | **0.96** | **0.99** | **545 μs** |

- Training: ~2 minutes on CPU for 100 epochs
- 187,000 supervised samples from 17,000 Monte Carlo runs (100K paths each)
- 11 strikes × 15 maturities across 5 tenor buckets (1W–5Y)

### Geometry-Aware Features (Λ)

Four geometric quantities extracted from the SABR manifold:
1. **q** — CEV-flattened forward coordinate (removes state-dependent scaling)
2. **σ_min** — terminal volatility minimizing geodesic action
3. **d_ℍ** — hyperbolic geodesic distance (controls exponential decay of transition probabilities)
4. **σ₀** — leading-order implied volatility from large-deviation asymptotics

### Key Methodological Points

- Control variate (Black model with constant volatility) reduces Monte Carlo variance
- Ratio-based loss: `L = E[((σ_GeoResNN - σ_MC)/σ_Hagan)²]` — focuses learning on relative residual
- **No** stop-gradient, EMA, or pretrained encoders needed — fully end-to-end
- Positivity of corrected volatility empirically preserved (multiplicative correction around positive baseline)

### Applicability to Cemini

- If Cemini uses SABR for vol-surface calibration (swaptions, rates products), this hybrid approach provides a drop-in accuracy upgrade
- The ~10⁴× speedup over Monte Carlo at inference (545 μs vs ~5s+ for MC) makes it production-viable
- Architecture pattern (analytical backbone + ML residual) is transferable to other models where asymptotic approximations are used

## Snippets

- "The hybrid learning framework... is based on a Residual Neural Network (ResNN) that learns a multiplicative correction of the Hagan formula, thus preserving the analytical structure while learning only the missing higher-order effects" [Source: 2605.06604, Abstract]
- "On the held-out test set, the global coefficient of determination increases from approximately R²≈0.73 for the naive deep network to R²≈0.92 for the residual-only architecture and R²≈0.94 for the geometry-aware architecture, reaching R²≈0.97 for the proposed hybrid geometric–residual model." [Source: 2605.06604, Abstract]
- "the framework is well suited for real-time pricing and calibration in practical trading environments" [Source: 2605.06604, Abstract]
- "the model does not attempt to relearn implied volatility from scratch; instead, it focuses on approximating the residual between the true SABR-implied volatility and its asymptotic counterpart" [Source: 2605.06604, §1]

## Dead Ends

- Paper does not address negative-rate environments extensively (mentions positive shift but no detailed analysis)
- No code release mentioned — would need to contact authors for reproducibility
- Single-venue (interest rates) — applicability to equity/commodity vol surfaces would need validation
- GPU inference not benchmarked — production deployment might need optimization beyond the reported 545 μs CPU timing