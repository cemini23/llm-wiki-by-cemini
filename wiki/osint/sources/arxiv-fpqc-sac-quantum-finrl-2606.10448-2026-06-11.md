---
title: FPQC-SAC — low-SNR financial RL via quantum representations (arXiv 2606.10448)
type: source
tags: [source, arxiv, financial-rl, sac, low-snr, quantum, portfolio]
keywords: [2606.10448, FPQC-SAC, financial-entropy-trap, parameterized-quantum-circuit, portfolio-management]
related:
  - concepts/llm-guided-financial-rl-interface.md
  - entities/tools/fpqc-sac.md
maturity: draft
read_status: skimmed
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/llm-guided-financial-rl-interface.md — low-SNR FinRL cluster
- @entities/tools/fpqc-sac.md — Phase-0 NO-GO (NOASSERTION license)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations |
| **arXiv** | 2606.10448 |
| **Repo** | https://github.com/ZeyuLIU-UST/FPQC-SAC-main |
| **sha256** | `91703a00bbd2bb9e362075654bfb98e288576ce2662d17dcb49f1e614fca0e1b` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.10448-mitigating-bias-in-low-snr-financial-reinforceme.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | skimmed — abstract, Financial Entropy Trap framing |

## Narrative

Proposes **FPQC-SAC**: compact **Parameterized Quantum Circuit (PQC)** before actor/critic to constrain feature propagation at the representation layer — addressing the **Financial Entropy Trap** (noisy states → unreliable Q estimates → bootstrapping amplification in max-entropy off-policy RL).

Claims: +66.89% cumulative return vs unconstrained SAC; ~+27% vs best continuous-control DRL baseline on portfolio tasks `[TENTATIVE — paper headline; not independently backtested]`.

Contrasts with output-side Q regularization (too late) and rigid input filters (erase weak signals).

**Cemini mapping:** REFERENCE for **representation-bottleneck** thinking in low-SNR equity/PM research — not a prod adoption path (quantum sim overhead, NOASSERTION license, unverified OOS). Pair with K110/K111 interface-design papers as complementary stabilization axes.

## Snippets

> "We refer to this critical failure mode of maximum-entropy RL in financial decision-making as the Financial Entropy Trap."

> — [Source: arxiv-2606.10448-mitigating-bias-in-low-snr-financial-reinforceme.pdf §1, retrieved 2026-06-11]
