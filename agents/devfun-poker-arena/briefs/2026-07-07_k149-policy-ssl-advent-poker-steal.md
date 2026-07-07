## Target

`agents/devfun-poker-arena/` — opponent modeling research lane + HL regression taxonomy.

## Summary

K149 poker research steals: **policy SSL embeddings** on Kuhn/Leduc (2607.01498) for opponent representation; **ADVENT** LLM+Prolog predicate invention (2607.01585) for interpretable offline spot features.

**Shipped (2026-07-07):** `scripts/policy_ssl_embedding.py` (clean-room, methods-only — repo no LICENSE), `scripts/predicate_invention.py` + `scripts/run_predicate_gate.sh` (3 verified predicates, pool `research/predicates/verified_predicates.json`), `references/k149-opponent-modeling-research.md`. Tests: `tests/test_k149_policy_om.py` (4). Aggression probe separates aggressive vs passive; NN payoff predictor is an honest negative (no gate). Prod `decide()` unchanged.

## Body

### Policy SSL (01498)

1. Build Leduc opponent-policy dataset from RLCard / arena selfplay exports.
2. Train basic SSL embedding (paper compares multiple — start simplest).
3. Evaluate downstream: cluster opponents; predict payoff from embedding.
4. **Blocker:** `VitamintK/ssl-project` has no LICENSE — methods-only until cleared.

### ADVENT pattern (01585)

1. For a recurring `analyze` leak class, LLM proposes a **named predicate** (e.g. `overfolds_to_3bet_oop`).
2. Verify on frozen regression spots via executable check (Prolog or pytest equivalent).
3. Accumulate verified predicates in private knowledge pool for next HL epoch.

### Pairing

| Layer | Prior |
|-------|-------|
| Leduc baselines | K130 RLCard |
| Consistent OM theory | K118 BBR |
| Ganzfried NE literacy | K131–K134, K148 |

**Prod `decide()` unchanged.**

## Sources

- [Source: arXiv:2607.01498, 2607.01585 (retrieved 2026-07-07)]
- @wiki/sources/arxiv-policy-representation-2607.01498-2026-07-07.md
- @wiki/sources/arxiv-advent-predicate-invention-2607.01585-2026-07-07.md
