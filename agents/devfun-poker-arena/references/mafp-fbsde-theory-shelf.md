# MAFP / fictitious-play FBSDE — theory shelf (K170 + K157)

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

## Related

- Brief (K170): `briefs/2026-07-16_k170-fictitious-play-fbsde-theory.md`
- Brief (K157 shelf): `briefs/2026-07-16_k157-fbsde-fp-shelf.md` — **Shelf (done)** → this page
- Chart: `research/mafp_hu_chart.json` (`solver_family=mafp`; chart provenance may cite `2607.08861`)
- Master plan (K170): `briefs/2026-07-16_k170-timeout-v2-master-plan.md` WP1
- Master plan (K176/K157 wave): `briefs/2026-07-16_k176-k157-master-plan.md` WP1
- Gambling-wiki sources (federation):
  - `@gambling-wiki/sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md`
  - `@gambling-wiki/sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md`
