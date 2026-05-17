---
title: "RL Retrain Pipeline Hardening — MAPPO retrain checklist (Cemini)"
type: concept
tags: [concept, rl-marl, mappo, cemini-internal, retrain-pipeline, risk-constrained-rl, k49]
keywords: [mappo-retrain, gradient-accumulation, gae-advantage-normalization, lagrangian-cvar, cmdp, dimensionless-state-scaling, data-readiness-gate, cold-start, curriculum-learning, safetensors, go-no-go-checklist]
related:
  - sources/4-3-rl-research.md
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- @sources/4-3-rl-research.md — anchor source: the internal RL-retrain hardening review this page synthesizes into reusable methodology
- @concepts/rl-marl-research.md — RL/MARL corpus-index hub

## Raw Concept

Promoted from `@sources/4-3-rl-research.md` (the internal "RL Retraining Pipeline Hardening for April 2026 Retrain Window" review). The source page holds provenance + the per-finding detail; this concept page lifts the 11 findings into a **reusable pre-retrain hardening checklist** for the CeminiSuite MAPPO pipeline — applicable to any future retrain window, not just April 2026.

## Narrative

The CeminiSuite trading brain is a **5-agent MAPPO** system — MacroForecaster, BullAdvocate, BearAdvocate, RiskAssessor, Trader (~151k params: ~85k actor across 5 agents + ~66k centralized critic). The architecture is sound; what breaks retrains is **data scaling, objective optimization, and state normalization**. This page is the hardening checklist that gates a retrain.

### The four failure surfaces

1. **Data readiness** — the dominant gate. A MAPPO retrain needs roughly 10× the parameter count in transition tuples; **≥100,000 tuples** is the floor. Sparse data (the April review found only ~5,000 BTC-USD + ~2,300 SPY rows) is an automatic NO-GO. Mitigations: block bootstrapping, GBM simulation, synthetic augmentation.
2. **Objective optimization** — GAE advantage normalization must be computed over the **full global (accumulated) batch**, not per micro-batch, or critic variance is skewed. The Lagrangian dual variable λ (CVaR risk constraint) must update **per epoch, never per batch** — micro-batch CVaR estimates are too noisy in fat-tailed series and cause policy oscillation.
3. **State normalization** — the 34-dim feature vector must be **dimensionless**: no absolute price levels. New `intel_stream_log` features get explicit scalers (expanding-window Z-score, tanh, min-max to [-1,1]).
4. **Checkpoint hygiene** — never warm-start from a corrupted checkpoint; validate with offline metrics, not surrogate loss.

### The hardening checklist (11 findings → operational rules)

| # | Rule | Why |
|---|------|-----|
| 1 | Global-batch advantage normalization | per-micro-batch normalization skews GAE variance, destabilizes the centralized critic |
| 2 | Log `loss.item()`, detach actor/critic losses separately | retained autograd graphs leak memory → OOM on the 128GB box |
| 3 | Safetensors checkpoints (not pickle `.pt`); `v.clone().contiguous()` optimizer state | security + avoids shared-buffer `RuntimeError`. Apache-2.0, IP-clean |
| 4 | Lagrangian CVaR → CMDP; update λ **per epoch**; compatible with `MaskedCategorical` | per-batch λ updates cause severe policy oscillation |
| 5 | Multiplicative observation noise — but exclude regime flags, boolean intel, action masks, allocations | preserves the Markov property; multiplicative beats additive for low-SNR data |
| 6 | Dimensionless state scaling — eradicate absolute price levels from the 34-dim vector | absolute levels destroy generalization across regimes |
| 7 | **Data readiness gate** — ≥100,000 transition tuples before retrain | the NO-GO trigger; the 10× rule vs. ~151k params |
| 8 | Two-phase curriculum: 30-day stationary warm-up → full 60-day complexity | <50 lines pure PyTorch; advance when critic explained-variance stabilizes |
| 9 | Checkpoint validation via offline metrics (explained variance, action diversity) | surrogate loss alone is insufficient for promotion |
| 10 | **Cold start** — orthogonal init, cleared Adam state | prior checkpoint has a data-duplication bug (~30 memorized states); warm-start risks negative transfer + plasticity loss |
| 11 | **Go/No-Go checklist** — see below | five conditions, all must hold |

### Go/No-Go gate (all five required)

1. ≥100,000 transition tuples in the training set.
2. Dimensionless state scaling verified (no absolute price levels).
3. Global (accumulated-batch) advantage normalization in place.
4. Epoch-level Lagrangian λ updates.
5. Total cold-start init (orthogonal weights, cleared optimizer state).

### Status / caveats

- `[TENTATIVE 2026-05-16]` The April 14–17 2026 retrain window referenced in the source has passed; the **checklist is window-agnostic** and applies to the next retrain. Whether the April retrain proceeded, and under what data conditions, is not recorded in this wiki — server-side state. Flagged to cemini-prod via `briefs/2026-05-16_rl-retrain-hardening-flag.md`.
- The checkpoint data-duplication bug (finding 10) is a concrete defect in a *prior* CeminiSuite checkpoint — server-Claude owns confirming it is fixed before any warm-start is reconsidered.

## Snippets

> "The April 14–17 retrain should NOT proceed with only 5,000 rows of data... synthetic data augmentation techniques... must be employed to expand the dataset to a minimum of 100,000 transition tuples before initiating the MAPPO retrain." [Source: 4_3 RL research.docx, §7]

> "The retrain must be a strict Cold Start." [Source: 4_3 RL research.docx, §10]
