# MAFP / fictitious-play FBSDE — theory shelf (K170 + K157 + K167/K241 SFP)

**arXiv:** [2607.08861](https://arxiv.org/abs/2607.08861)  
**Title (short):** fictitious play for fully coupled FBSDEs in finite-player stochastic differential games  
**Shelf date:** 2026-07-16  
**K-batch cross-link:** **K157** (thin shelf merge) + **K170** (primary Arena shelf)

## What it backs

- Convergence analysis of **fictitious play (FP)** under coupling (geometric → super-exponential under structure). Han–Hu–Long extension of continuous-time Nash FBSDE FP.
- Theoretical support for continuing **MAFP chart bake** offline (`research/mafp_hu_chart.json`, solver family `mafp`).
- Complements prior MAFP stance provenance (K124) — FP iteration can converge even when dynamics are coupled.

## Arena / decide() posture (hard)

| Allowed | Forbidden |
|---------|-----------|
| Cite in docs / `solver_provenance.notes` | Online FBSDE or PDE solvers on the Arena clock |
| Offline MAFP chart bake + static overlay | Any FBSDE numerics inside `decide()` / harness hot path |
| Theory justification for FP-style bake | Runtime LLM, gin flip, DeepCFR “because paper” |
| Link continuous-time FP rates in this shelf | **Do not** import geometric / super-exponential rates into discrete MAFP / HL / sandbox self-play **iteration budgets** |

**Explicit:** no FBSDE on Arena clock / `decide()`. Charts stay O(1) JSON lookups.

**K157 hard rule:** continuous-time geometric rates from 2607.08861 **must not** change `mafp_chart_refinement.py` round counts, eps, or self-play schedules. Shelf / provenance only.

## SFP — self-fictitious-play MFG (K167 + K241)

**arXiv:** [2608.15258](https://arxiv.org/abs/2608.15258) — Bai, Laurière, Ren, Wang (Bai et al.)
**Shelf date:** 2026-08-18
**K-batch cross-link:** **K167** (primary SFP shelf) + **K241** (MAFP-family steal note, researcher track)

### What it is

- **Self-fictitious-play (SFP)** on **monotone potential ergodic** mean-field games: the state follows the optimal feedback for the current belief, and the belief updates from the player's **own empirical occupation measure** `d m_t = λ (δ_{X_t} − m_t) dt` — **not** the population McKean–Vlasov law `m_t = Law(X_t)`.
- On the torus `T^d`, SFP is **contractive** with a unique invariant law `ρ_λ`; Wasserstein distance to the MFG Nash `m*` reaches a neighborhood of order **O(√λ)** (equivalently **√ε**, ε = belief-update rate). LQ example (§4.1) shows the rate is **sharp**.
- Proof machinery: uniform-in-time ergodic HJB regularity + Lasry–Lions divergence energy + **reflection coupling** (not entropy/gradient arguments).
- **Distinguish:** Perrin et al. NeurIPS 2020 is *population* fictitious play; Shen et al. stance-entangled MAFP (2606.19308) is a multi-agent scheme. SFP is the **single-trajectory / own-path** variant — the belief is your own occupation measure, not the field's.

### Dual-ID (resolve by file+wiki, not bare K#)

| ID | Meaning |
|----|---------|
| **Poker K167** | SFP MFG (2608.15258) — this shelf |
| **Poker K241** | Same paper, MAFP-family steal note (researcher track) — this shelf |
| **CCC K241** | No raw LLM tabular prediction — **NOT** 2608.15258; do not collapse with poker K241 |
| **CCC K167** | Do not assume; do not collapse with poker K167 |

### Arena / decide() posture (hard)

| Allowed | Forbidden |
|---------|-----------|
| Cite in docs / `solver_provenance.notes` | Online MFG / ergodic-HJB numerics on the Arena clock |
| Researcher-track literacy for black-box HU (own path as belief) | **Do not** import `O(√λ)` / `√ε` into discrete MAFP / HL / sandbox self-play **iteration budgets** |
| Keep belief-update rate (λ / ε) small | Live tournament wire; runtime belief-chasing at fast λ |

**Explicit:** SFP is theory / researcher-track literacy only. No code this batch. Do **not** retune `decide()` / MAFP from `O(√λ)` / contractivity (same posture as K157 FBSDE-FP and K166 FTRL/FP literacy).

## Related

- Brief (K167 SFP shelf): `briefs/2026-08-18_k167-sfp-mfg-shelf.md` — **Shelved** → this page
- Brief (K241 SFP steal note): `briefs/2026-08-18_k241-self-fictitious-play-mfg.md` — **Shelved** → this page
- Paper: [arXiv 2608.15258](https://arxiv.org/abs/2608.15258) (Bai, Laurière, Ren, Wang)
- Brief (K170): `briefs/2026-07-16_k170-fictitious-play-fbsde-theory.md`
- Brief (K157 shelf): `briefs/2026-07-16_k157-fbsde-fp-shelf.md` — **Shelf (done)** → this page
- Chart: `research/mafp_hu_chart.json` (`solver_family=mafp`; chart provenance may cite `2607.08861`)
- Master plan (K170): `briefs/2026-07-16_k170-timeout-v2-master-plan.md` WP1
- Master plan (K176/K157 wave): `briefs/2026-07-16_k176-k157-master-plan.md` WP1
- Gambling-wiki sources (federation):
  - `@gambling-wiki/sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md`
  - `@gambling-wiki/sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md`
