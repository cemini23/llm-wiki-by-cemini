## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (Jun 21 beta).

## Summary

Extend K123 verifier stack with **probabilistic trajectory bounds** (arXiv 2606.20510): conservative upper bound on cumulative policy-violation risk across a hand when individual gates (legality, MC equity, M₈) are treated as noisy predicates — block submit when bound exceeds threshold.

## Body

### Scope / regime disclosure

| Dimension | Google paper (2606.20510) | Cemini target |
|-----------|---------------------------|---------------|
| Domain | Terminal/tool agent taint (Datalog) | **NLHE** symbolic hand trajectory |
| Predicates | PII/declassifier error rates | Legality ε≈0; MC equity estimator variance; M₈ regex FP rate |
| Output | Allow/block + global risk certificate | Pre-submit gate on `decide()` action chain |

Regime-conditioned steal — do not claim terminal benchmark numbers transfer to poker LB.

### P0 — trajectory bound prototype (offline)

1. Assign per-street **failure upper bounds** uᵥ to verifier predicates (calibrate from regression suite + selfplay logs).
2. Compose hand as **Merge/Propagate** chain (each street action inherits prior violation risk).
3. Compute conservative **R\*** upper bound (independent-bound baseline first; correlation-aware DRO optional spike).
4. If R\* > τ (start τ=0.05), fall back to safest legal action (check/fold) or regression oracle.

### P1 — pair with K123 Best-of-N

| Layer | Role |
|-------|------|
| K123 pointwise | Argmax legal candidate per decision |
| K125 trajectory | Veto entire line if cumulative bound exceeds τ before final submit |
| K124 MAFP | Offline chart refinement (no runtime cost) |

### P2 — Memory Gap pairing (2606.19338)

On trajectory export, tag spots where bound breach correlates with **F6 memory off** vs mis-decide with memory on — feeds HL loop priority queue.

### Out of scope

- Google Datalog monitor install
- Runtime LLM verifier judges

## Sources

- [Source: arXiv:2606.20510 (retrieved 2026-06-21)]
- @wiki/concepts/probabilistic-agent-policy-verification.md
- @wiki/sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
- @agents/devfun-poker-arena/briefs/2026-06-18_k123-verifier-inference-steering.md
