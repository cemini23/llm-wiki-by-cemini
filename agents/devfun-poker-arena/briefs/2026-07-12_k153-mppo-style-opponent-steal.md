## Target

`agents/devfun-poker-arena/` — stylized opponent league / MAFP pool improvement.

## Summary

K153 steal: **MPPO** (2506.16995) — improve suboptimal stylized opponents without erasing play-style diversity.

**Shipped (2026-07-12):** `config/hu_style_preservation.json`; `references/mppo-style-preservation.md`; `references/league-promotion-rubric.md`; `compute_d_policy_tv` + `compute_style_drift_d_policy` + `compute_league_promotion_rubric_advisory` in `researcher_trajectory_summary.py`; `examples/rlcard_style_drift_trial.py` + `scripts/run_rlcard_style_drift_trial.sh`; tests. **Advisory only** — no hard gate. **No** MPPO fork (NO LICENSE).

## Body

### MPPO pattern

1. League bots start as **stylized suboptimal archetypes** (not pure Nash self-play).
2. Upgrade with **mixed online PPO + offline style demonstrations** (paper β≈0.05).
3. Before promotion: measure **style drift** (D_policy or action-distribution distance vs seed demonstrator).
4. Pair with K152 **expert-yardstick** regression — stronger ≠ homogenized.

### Blocker

- `AMysteriousBeing/MPPO` — **no LICENSE** (1★). Read paper + requirements; no code fork.

### Operator checklist

- [x] Document style-preservation metric for league promotion gate
- [x] Trial on Leduc/RLCard stylized bot before NLHE league changes

## Shipped

| Artifact | Notes |
|----------|-------|
| `config/hu_style_preservation.json` | β=0.05, max TV 0.25, archetypes |
| `references/mppo-style-preservation.md` | D_policy operator spec |
| `references/league-promotion-rubric.md` | K160 yardstick/style gap rubric |
| `examples/rlcard_style_drift_trial.py` | Leduc trial (isolated venv) |
| `scripts/run_rlcard_style_drift_trial.sh` | Wrapper |
| `tests/test_k153_style_preservation.py` | TV + config |
| `tests/test_k160_league_promotion_rubric.py` | Rubric gaps |

```bash
uv run pytest tests/test_k153_style_preservation.py tests/test_k160_league_promotion_rubric.py -q
bash scripts/run_rlcard_style_drift_trial.sh --episodes 50  # after setup_rlcard_venv.sh
```

## Sources

- `references/mppo-style-preservation.md`
- `references/league-promotion-rubric.md`
- `briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steal.md`
- arXiv [2506.16995](https://arxiv.org/abs/2506.16995) — gambling-wiki federation (`entities/tools/mppo.md`)
