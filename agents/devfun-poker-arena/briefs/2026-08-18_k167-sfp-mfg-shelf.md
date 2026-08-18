# K167 — Self-fictitious-play MFG shelf

**Date:** 2026-08-18 · **Batch:** K167 · **Lanes:** theory shelf (continuous ergodic MFG self-fictitious-play)

OSINT arena: `agents/devfun-poker-arena/briefs/2026-08-18_k167-sfp-mfg-shelf.md`

## Target

`agents/devfun-poker-arena/` — MAFP / fictitious-play literature shelf only. No live betting.

## Summary

arXiv 2608.15258 (Bai, Laurière, Ren, Wang) proves self-fictitious-play on monotone potential ergodic MFG is contractive; Wasserstein distance to Nash is **O(√λ)**. **Shelf only** — do not import that rate into discrete MAFP / `decide()` budgets (same posture as K157). Dual-ID: poker K167/K241 = this paper; CCC K241 = no raw LLM tabular.

## Takeaway (2608.15258 — Bai, Laurière, Ren, Wang)

- **Self-fictitious-play (SFP)** on **monotone potential ergodic** mean-field games: the state follows the optimal feedback for the current belief, and the belief updates from the player's **own empirical occupation measure** `d m_t = λ (δ_{X_t} − m_t) dt` — **not** the population McKean–Vlasov law `m_t = Law(X_t)`.
- On the torus `T^d`, SFP is **contractive** with a unique invariant law `ρ_λ`; Wasserstein distance to the MFG Nash `m*` → neighborhood of order **O(√λ)** (belief-update rate). LQ example (§4.1) shows the rate is **sharp**.
- Proof: uniform-in-time ergodic HJB regularity + Lasry–Lions divergence energy + **reflection coupling** (not entropy/gradient arguments).
- Distinguish from Perrin et al. NeurIPS 2020 — that is **population** fictitious play, not this self-interacting scheme.

## Operator action

**None for decide()/HL this cycle.** Continuous-time torus MFG ≠ discrete HU poker MAFP — do **not** retune `decide()` / MAFP from `O(√λ)` / contractivity rates (same posture as K157 FBSDE-FP). Shelf next to K157 (continuous FP), K166 (FTRL/FP literacy), K124 (discrete MAFP). Phase-1: `wont_wire`.

## Skip

- Local FOSS adopt — no accompanying code (GitHub search 0 repos; PDF has no code URL)
- Atto, GuruWatcher, CeminiDFS, TipDrop, prod scp

## Shelved

Folded into `references/mafp-fbsde-theory-shelf.md` (K170 + K157 + K167/K241 SFP). Do not import `O(√λ)` / contractivity into discrete MAFP budgets; no `decide()` / MAFP loop retune this cycle. Dual-ID: poker K167/K241 = 2608.15258; CCC K241 = no raw LLM tabular (not this paper).

## Sources

- @wiki/sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
- @wiki/sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md
- @wiki/sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
- @wiki/sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
