## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (equilibrium baseline literacy).

## Summary

Steal K136 Nash-solver literacy (2606.28308 + 2606.29169): document **which solver family** produced any toy-game baseline; use **FP burn-in → PED-style refinement** on three-player Kuhn spikes only — not interchangeable CFR+ vs regularized outputs when the Nash set is non-singleton.

## Body

### Scope / regime disclosure

| Dimension | Papers (28308 / 29169) | Cemini target |
|-----------|------------------------|---------------|
| Games | Tabular 2p0s + 3p Kuhn poker | **NLHE** dev.fun — no tabular NE |
| Solvers | CFR+, FP, R-NaD, PED | Offline chart / toy baselines only |
| Claim | Algorithm selects equilibrium **member** | Provenance + hedge vs flawed villains |

Do not claim Kuhn max-entropy dominance transfers to 6-max without measurement.

### P0 — solver provenance in baselines

1. Tag any existing CFR+/toy solver output with `solver_family=` in chart metadata (`deploys.jsonl` or chart JSON sidecar).
2. When comparing baselines, refuse to diff profiles unless same family **or** document known Nash-polytope asymmetry.

### P1 — FP→PED spike on 3p Kuhn (optional)

1. Implement minimal 3p Kuhn env (deck size ≤6) — separate from NLHE `decide()`.
2. Run FP/CFR for N iterations → switch to exploitability-descent refinement (PED pattern: monotonic late improvement).
3. Log exploitability curve; compare to CFR-only at equal iteration budget.
4. **Stop:** literacy spike — results inform whether late-stage refinement helps multiway toy games before stealing to chart space.

### Pairing with K124/K136 cluster

| Layer | Role |
|-------|------|
| K124 MAFP | Stance fictitious play in chart space |
| K136 28308 | Max-entropy vs CFR-face selection in 2p0s |
| K136 29169 | FP-PED hybrid for 3p imperfect-info |
| K122 axes | M₇ entropy floor after equilibrium refinement |

### Out of scope

- Installing PED reference code (no public repo)
- Multiplayer NLHE equilibrium solver on Arena clock

## Sources

- [Source: arXiv:2606.28308 (retrieved 2026-06-30)]
- [Source: arXiv:2606.29169 (retrieved 2026-06-30)]
- @wiki/concepts/nash-equilibrium-solver-selection.md
- @wiki/concepts/projected-exploitability-descent.md
- @wiki/concepts/kuhn-poker-sft-curriculum-reference.md
