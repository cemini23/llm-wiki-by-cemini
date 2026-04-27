---
title: Constrained Policy Optimization for Provably Fair Order Matching (CPO-FOAM)
type: source
tags: [pdf, rl-marl, market-microstructure, crypto, constrained-mdp, fairness, on-chain-verification, rigorous-academic]
related:
  - concepts/market-microstructure.md
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - rl-marl
  - market-microstructure
  - crypto
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Constrained Policy Optimization for Provably Fair Order Matching
- **Author(s)**: Zehua Cheng, Jiahao Sun, Yang Yang, Yue Liu, Zhongyi Zhang, Dong Yan, Thomas Hartvigsen, Wen Xiao, Peilin Zhao (Oxford / FLock.io / Manchester / HKUST / deluthium.ai / affiliated labs — cross-institutional RL + market-microstructure collaboration)
- **Type**: PDF (arXiv preprint)
- **Location**: research for cemini/crypto 2 4:11.pdf
- **Length**: 18p
- **Retrieved**: 2026-04-23 (download date)
- **Publication date**: April 2026 (arXiv:2604.06522v1 [cs.GT])
- **Read status**: read-skim
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, market-microstructure, crypto

## Narrative

Rigorous methods paper proposing **CPO-FOAM** (Constrained Policy Optimization with Feedback-Optimized Adaptive Margins) — a two-loop RL algorithm for learning order-matching policies that are provably fair under a Constrained Markov Decision Process (CMDP) formulation. The inner loop runs an analytic trust-region step on the Fisher information manifold (second-order natural-gradient update, CPO-style); the outer loop adjusts per-constraint safety margins via a PID controller driven by observed constraint-violation frequency (CVF). This replaces the static Lagrangian λ of vanilla constrained RL with a control-theoretic feedback law, which the authors argue both stabilizes training and gives calibrated worst-case guarantees under distribution shift.

Fairness is instantiated through three formal constraints baked into the CMDP: demographic parity (matched-fill probabilities should equalize across participant cohorts), equalized odds (conditional on order-arrival state), and Lipschitz fairness (policy outputs bounded in total variation as feature perturbations are bounded — enforced via spectral normalization on policy layers). The paper proves (Thm 3.1–3.4) that under mild regularity on the environment the PID law converges to a fixed point at the CVF target, with bounded bias relative to the offline-optimal fair policy. Evaluation is empirical and multi-venue: LOBSTER NASDAQ equity LOBs and a crypto LOB dataset (BTC/ETH/SOL/DOGE/SHIB/PEPE via Tardis.dev + Kaiko snapshots), plus Safety-Gymnasium for ablations. Headline numbers: ~95.9% reward recovery vs unconstrained PPO on TradFi, ~98.4% on DeFi, at CVF 2.5% / 3.2% respectively — i.e. the fairness tax is ~1.6–4.1% of reward, with CVF an order of magnitude below Lagrangian baselines.

The final third of the paper sketches an **on-chain verification** scheme: each trained policy checkpoint commits (model hash, training-data Merkle root, fairness-certificate hash) to a smart contract; bulk artifacts live on IPFS/Arweave/EigenDA with content addresses referenced from the anchor. A zero-knowledge attestation (Halo2-style, described but not fully implemented) lets the operator prove CVF ≤ budget on a sampled window without exposing order-level PII. This is the only crypto-native contribution of the paper; the rest is squarely quant-ML/RL.

Who should care: this is a **real methods contribution** — CMDP + natural-gradient + PID-adaptive margins is a clean recipe, and the empirical scope (dual venue, six assets, Safety-Gym ablations) is well above the junior-paper bar. The on-chain layer is more gesture than system (no gas costs, no proving-time budget, no adversarial game against operators who might switch checkpoints between attestation windows), but it is not hand-waved either. Treat the reward-recovery numbers as upper-bound estimates — the LOB simulator is queue-reactive, not fully agent-based, so real-world slippage and adverse selection are under-modeled. Flag: **rigorous-academic**, **RL-methods-primary**, **crypto-adjacent** (the on-chain piece is a capstone, not the core).

## Key findings

- **CPO-FOAM algorithm**: inner-loop analytic trust-region update on Fisher information manifold (CPO-style natural gradient) + outer-loop PID controller on safety-margin thresholds keyed to observed CVF. Replaces static Lagrange multiplier with feedback control.
- **Fairness triple**: demographic parity, equalized odds, and Lipschitz fairness (enforced via spectral normalization on policy MLP layers); all three encoded as CMDP cost constraints.
- **Convergence theorems (3.1–3.4)**: PID-adaptive margin law converges to target CVF fixed point under bounded-environment-shift assumptions, with bias ≤ O(1/√T) against offline-optimal fair policy.
- **Empirical results**: LOBSTER NASDAQ + crypto LOB (BTC, ETH, SOL, DOGE, SHIB, PEPE via Tardis.dev + Kaiko) + Safety-Gymnasium ablations. 95.9% reward retention on TradFi at 2.5% CVF, 98.4% on DeFi at 3.2% CVF — outperforms PPO-Lagrangian, CPO, and FOCOPS baselines on the CVF/reward Pareto.
- **On-chain verification layer**: model-hash + training-Merkle-root + fairness-certificate commitment to smart contract, with IPFS/Arweave/EigenDA for blob storage and a sketched Halo2 ZK-attestation for window-level CVF compliance.

## Snippets

- **Abstract** — "We formulate provably fair order matching as a Constrained Markov Decision Process and propose CPO-FOAM (Constrained Policy Optimization with Feedback-Optimized Adaptive Margins), combining an analytic trust-region step on the Fisher information manifold with a PID-controlled adaptive safety-margin mechanism."
- **§3 (formulation)** — Fairness constraints: demographic parity |E[A=1|g=0] − E[A=1|g=1]| ≤ ε_dp; equalized odds (same, conditional on state); Lipschitz fairness ‖π(·|s) − π(·|s′)‖_TV ≤ L·d(s,s′).
- **§4 (algorithm)** — "The adaptive margin update follows δ_{t+1} = δ_t + K_p · e_t + K_i · Σe + K_d · Δe, where e_t = CVF_observed − CVF_target." PID-controlled safety margin replaces fixed Lagrangian.
- **§5 (experiments)** — "Across LOBSTER NASDAQ equity limit-order-book replay and a multi-venue crypto LOB dataset (BTC, ETH, SOL, DOGE, SHIB, PEPE; Tardis.dev and Kaiko), CPO-FOAM attains 95.9% / 98.4% of unconstrained PPO reward at 2.5% / 3.2% CVF respectively." Key headline number.
- **§6 (on-chain attestation)** — "Commitments (H(θ), H(D_train), H(ξ_fair)) are anchored to an EVM smart contract; blob storage uses IPFS/Arweave/EigenDA; a Halo2-style attestation proves CVF ≤ budget over a sampled evaluation window without disclosing order-level data." Only crypto-native mechanism in the paper.
