---
title: "Beneath the VIX: Probability, Severity, and Uncertainty Shocks (arXiv 2610.03849)"
type: source
tags: [source, k283, arxiv, volatility, options, macro, quant]
keywords: [vix, downside-protection-premium, dpp, put-call-parity, breeden-litzenberger, uncertainty-shock, nber-recession]
related:
  - concepts/k283-arxiv-wave.md
  - concepts/xsp-vol-regime-gates.md
  - concepts/fomc-iv-surface-dynamics.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: deep-read
---

## Relations

- @concepts/k283-arxiv-wave.md
- @concepts/xsp-vol-regime-gates.md
- @concepts/fomc-iv-surface-dynamics.md

## Raw Concept

| Title | Beneath the VIX: Probability, Severity, and Uncertainty Shocks |
| Author | Todd B. Walker (Indiana University, Dept. of Economics) |
| Type | arXiv preprint (econ.GN) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.03849-beneath-the-vix-probability-severity-and-uncerta.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.03849v1 |
| Replication | doi:10.5281/zenodo.23106238 |
| read-status | deep-read |

## Narrative

The VIX is one number. This paper splits it into two: how **likely** a fall is, and how **big** the fall is when it comes. It calls the instrument the **Downside Protection Premium (DPP)**.

### The decomposition

Define the normalised at-the-money forward put χ_t(τ) ≡ P^AtM_t(τ)/S_t. By put–call parity the carry-adjusted premium splits:

    a_t = q_t · m_t

where **q_t** is the risk-neutral shortfall probability and **m_t** is the conditional severity. Recover the parts from the Breeden–Litzenberger strike slope:

    q_t = e^{rτ} · ∂P_t(K,τ)/∂K |_{K=F}

The lognormal scale benchmark is R̃ = 1 + s_t Z, with severity elasticity η_m = 1/(1+a_t).

### Results

- **DPP tracks VIX.** Monthly correlation 0.992; daily 0.990.
- **Severity dominates.** Severity elasticity 1.032 [0.994, 1.071]; probability elasticity only −0.032 [−0.071, 0.006].
- Of the recession log premium, **severity is 91.5%** [86.7, 96.3].
- A common scale is excluded in **352/405 months (86.9%)**. The varying-probability version is still excluded in 112/405 (27.7%).
- Realised-volatility and volatility-news innovations both reprice through **severity**, but they differ: the 12-month manufacturing-employment contrast is −0.628 (100×log); at equal impact, severity is −0.065.

### Why it matters here

This is a **desk-level instrument for the vol lane**. When VIX rises, this decomposition says whether the move is a *probability* shift or a *severity* shift. Severity-led moves are the ones that hurt short-vol positioning. It gives an option-implied, real-time read on macro tail risk — a natural input to the `xsp-vol-regime-gates` family and to GuruWatcher macro watches.

**No license stated.** An AI-use declaration (ChatGPT-6.1 / 6.0) is present. Treat the replication package as the source of truth.

## Snippets

> "Severity accounts for 91.5% [86.7, 96.3] of the recession log premium." [Source: arxiv-2610.03849-beneath-the-vix-probability-severity-and-uncerta.pdf]

> "The DPP–VIX correlation is 0.992 monthly and 0.990 daily." [Source: arxiv-2610.03849-beneath-the-vix-probability-severity-and-uncerta.pdf]
