# MPPO style preservation — league promotion (K153)

Operator spec from arXiv **2506.16995** (Mixed PPO). Config:
`config/hu_style_preservation.json`.

## Pattern (read-only — no MPPO fork)

`AMysteriousBeing/MPPO` has **no LICENSE** (Phase-0 2026-07-12). Steal
**requirements** only:

1. League stylized bots start as **suboptimal archetypes** (not Nash self-play).
2. Upgrade path mixes online self-play with offline style demos (**β ≈ 0.05**).
3. Before NLHE league promotion: measure **D_policy** (total-variation distance
   between action distributions vs seed demonstrator).
4. Pair with K152 **expert-yardstick** grade — **stronger ≠ homogenized**.

## D_policy metric

Total variation over action buckets `{fold, check, call, raise}`:

```
D_policy = 0.5 * sum_a |p_seed(a) - p_candidate(a)|
```

| TV | Interpretation |
|----|----------------|
| 0 | Identical style |
| 1 | Disjoint support |
| ≤ `max_d_policy_tv_advisory` (default 0.25) | Advisory pass |

Computed by `compute_style_drift_d_policy()` in
`examples/researcher_trajectory_summary.py`. **Advisory only** — never a hard
submit gate.

## Leduc / RLCard trial (pre-NLHE)

Run stylized archetype histograms on Leduc before changing NLHE MAFP/league pool:

```bash
bash scripts/setup_rlcard_venv.sh          # once
bash scripts/run_rlcard_style_drift_trial.sh --episodes 100
```

Output: `reports/rlcard-style-drift/summary.json`. Exit 0 always (advisory).

## Pair with K152 + K160

| Lane | Role |
|------|------|
| Yardstick pool grade | Fixed expert outside train loop |
| Style drift D_policy | Homogenization guard on league upgrade |
| FootsiesGym exploitability advisory | **Separate env** — never NLHE league score |
| Forgetting-factor regret | Recency drift when opponent mix shifts |

See `references/league-promotion-rubric.md` and `references/expert-yardstick-pool.md`.

## What not to do

- Fork or vendor `AMysteriousBeing/MPPO`
- Add `rlcard` to `pyproject.toml` core deps
- Hard-fail HU submit on style TV alone
- Promote NLHE league members from Leduc pass without separate replication

## Related

- `briefs/2026-07-12_k153-mppo-style-opponent-steal.md`
- `briefs/2026-07-12_k160-lightweight-yardstick-deep-read-steal.md`
- `@gambling-wiki/sources/arxiv-2506.16995-mppo-style-preserving-game-agents-2026-07-12.md`
