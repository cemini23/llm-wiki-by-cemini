---
title: Boundary Inference for Mixed Fractional Models
type: source
tags: [pdf, quant-finance, options-derivatives, k49]
keywords: [Boundary, Inference, Mixed, Fractional, Models, High-Frequency, LAN, Score-Test, Hurst, rough-volatility, mfBm, mfOU]
clusters: [options-derivatives]
related:
  - concepts/quant-finance.md
  - concepts/options-derivatives.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives cluster hub (covers rough volatility, fractional models, FRTB-audit)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)

## Raw Concept

- **Original title**: Boundary Inference for Mixed Fractional Models under High-Frequency Observation: Critical LAN and Score Tests at H = 3/4
- **Author(s)**: Cai Chunhao (Sun Yat-Sen University), Shang Yiwu (Nankai University), Xiao Weilin (Zhejiang University), Zhang Cong (Zhejiang University)
- **Type**: PDF (arXiv 2603.22888)
- **Location**: research for cemini/mixed fractional models.pdf
- **Retrieved**: 2026-04-27
- **Length**: 32p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

This paper develops boundary statistical inference at the Hurst exponent `H = 3/4` for mixed fractional Brownian motion (mfBm) and mixed fractional Ornstein–Uhlenbeck (mfOU) processes observed at high frequency. The point `H = 3/4` matters because, per Cheridito (2001), it separates the regime where mfBm retains a semimartingale interpretation from the supercritical regime where that interpretation breaks down — so it is an econometric boundary, not just a mathematical edge case. Existing high-frequency LAN results (Brouste–Fukasawa for fractional Gaussian noise; Cai et al. for mfBm/mfOU off-boundary) explicitly exclude the critical point: at `H = 3/4` the off-boundary normalizations fail, leading traces pick up an extra logarithmic factor, and the raw `H`-score develops a singular coupling with the nuisance scale `σ`.

Three contributions. First, the authors identify the exact critical first-order scaling and show that once the explicit linear term is removed from the `H`-score, the transformed `(σ, H)` block is already non-degenerate. Second, they prove critical score CLTs and derive local asymptotic normality (LAN — genuinely LAN, not just LAMN) with fully explicit leading information constants for both models; the efficient `H`-information is `I_H^eff = 3σ⁴/64` in both mfBm and mfOU. Third, they build boundary-calibrated one-sided score tests for the hypothesis `H₀: H ≤ 3/4` vs `H₁: H > 3/4`, with a feasible plug-in version that estimates nuisance parameters under the restriction `H = 3/4`. Monte Carlo (1000 reps) shows correct directional power — the statistic's mean climbs from ≈0.01 at `H=0.75` to ≈1.42 at `H=0.90` — but a heavily conservative null calibration (5%-level rejection rates stay near 1–4% even at `n=512`), suggesting a finite-sample/bootstrap correction is needed. An intraday illustration on one-minute SPY data finds no persistent evidence for `H > 3/4`.

**Cemini relevance**: This sits squarely in rough-volatility / fractional-model estimation — directly relevant to volatility modeling. It supplies a rigorous, hypothesis-test-based diagnostic for whether high-frequency price data have crossed into a supercritical (non-semimartingale) persistence regime, a concrete tool for stress-testing the fractional/rough-vol assumptions Cemini's options work depends on.

## Snippets

> "We study boundary inference at H = 3/4 for mixed fractional Brownian motion and mixed fractional Ornstein–Uhlenbeck models under high-frequency observation. This boundary is economically important because it separates the critical and supercritical regimes of mixed fractional dynamics." [Source: mixed fractional models.pdf p.1]

> "The limiting information matrices Γcrit_m and Γcrit_o are deterministic and non-singular. Hence the critical experiments are genuinely LAN, not merely LAMN. In particular, the critical point is resolved by a single triangular local reparametrization." [Source: mixed fractional models.pdf p.18]

> "the feasible mfBm statistic is stable... but first-order Gaussian critical values still under-reject substantially at realistic sample sizes." [Source: mixed fractional models.pdf p.23]
