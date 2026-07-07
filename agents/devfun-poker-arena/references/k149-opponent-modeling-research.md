# K149 opponent-modeling research lane

Offline research tooling. **Prod `decide()` is unchanged** — nothing here runs at Arena runtime.

## Policy-representation embedding (arXiv:2607.01498)

Clean-room of "learning representations of policies" — encode a policy by its
*behaviour* on a fixed probe battery, not by states.

- `scripts/policy_ssl_embedding.py`
- **License:** paper is CC BY 4.0; repo `VitamintK/ssl-project` has **no LICENSE** → methods-only, no upstream code copied.
- Embedding = normalized action frequencies bucketed by street × facing-bet (8 dims).
- Downstream evals:
  - **Aggression probe** — linear projection separates maniac/lag from passive archetypes (verified).
  - **NN payoff predictor** — leave-one-out nearest-neighbour vs global-mean baseline. Current finding: behavioural embedding **does not** beat baseline on hero exploit payoff (payoff is hero-counter-specific, high variance). Honest negative result; do not gate on it.

```bash
uv run python scripts/policy_ssl_embedding.py --no-payoff          # fast probe
uv run python scripts/policy_ssl_embedding.py --hands 200          # with payoff eval
```

## ADVENT predicate invention (arXiv:2607.01585)

Name a leak class as an interpretable predicate, verify with an executable check
over frozen HU regression spots, accumulate verified predicates in a private pool.

- `scripts/predicate_invention.py`, `scripts/run_predicate_gate.sh`
- A predicate = `applies_to(spot)` + `fires(spot, action)`.
- **Verified** = never fires on the current known-good `decide()` (leak already guarded).
- **Live leak** = fires → regression alert; `--gate` exits 1.
- Verified pool: `research/predicates/verified_predicates.json` (next-epoch knowledge).

Starter predicates: `folds_premium_bb_defend`, `opens_trash_sb_hu`, `calls_off_dominated_broadway_vs_shove`.

```bash
uv run python scripts/predicate_invention.py --gate
bash scripts/run_predicate_gate.sh
```

## Priors

| Layer | Prior |
|-------|-------|
| Leduc / offline baselines | K130 RLCard |
| Consistent OM theory | K118 BBR |
| Ganzfried NE literacy | K131–K134, K148 |
| Range probe (linear) | K129 `irumai_range_probe.py` |
