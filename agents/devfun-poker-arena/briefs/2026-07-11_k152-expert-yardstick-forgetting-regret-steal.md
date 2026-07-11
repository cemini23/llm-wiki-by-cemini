## Target

`agents/devfun-poker-arena/` — HU sandbox regression eval + self-play/league health metrics.

## Summary

K152 steals: **expert-yardstick grading** for imperfect-info RL (2607.06854) and **forgetting-factor regret** for non-stationary opponent pools (2607.07078).

**Shipped (2026-07-11):** `config/hu_yardstick_pool.json`; `references/expert-yardstick-pool.md`; `compute_yardstick_pool_grade` + `compute_forgetting_factor_regret` in `researcher_trajectory_summary.py` (CLI `--yardstick-pool`, `--forgetting-decay`); HU gate advisory echo in `run_hu_sandbox_gate.sh`; tests. **Advisory only** — no hard gate fail on yardstick pool. **No** adversarial-coevolution code borrow (NO LICENSE).

## Body

### Expert yardstick (06854)

1. Add regression gate: **% vs fixed exploit/expert pool**, not only self-play win rate or random crush.
2. Document curriculum + keep-best checkpoint pattern from adversarial-coevolution ablations.
3. Leduc validation on RLCard before NLHE promotion claims.
4. **Blocker:** `Nikelroid/adversarial-coevolution` has **no LICENSE** — read-only until SPDX added.

### What not to port

- Gin Rummy gold agent as NLHE opponent
- Live LLM opponent in training loop
- DAgger / heavy embedding stacks (paper negative results)

### Forgetting-factor regret (07078)

- When league/MAFP opponent mix drifts, log **recency-weighted exploitability/regret** alongside lifetime averages for HL epoch reviews.

### Operator checklist

- [x] Draft yardstick opponent spec for HU sandbox (frozen league slice or rule expert)
- [ ] Leduc: run RLCard baseline vs tabular optimum sanity check
- [x] Re-check adversarial-coevolution LICENSE before any code borrow — **NO LICENSE; read-only**

## Shipped

| Artifact | Notes |
|----------|-------|
| `config/hu_yardstick_pool.json` | ten, maniac_shark_lag, tight, lag thresholds; `never_train: true` |
| `references/expert-yardstick-pool.md` | Operator spec + what-not-to-port |
| `examples/researcher_trajectory_summary.py` | pool grade + forgetting regret; wired into manifest |
| `scripts/run_hu_sandbox_gate.sh` | Advisory echo after TEN/shark audits |
| `tests/test_researcher_trajectory_summary.py` | pool grade + forgetting regret tests |
| `tests/test_k152_yardstick_pool_config.py` | JSON load + required handles |

```bash
uv run pytest tests/test_researcher_trajectory_summary.py tests/test_k152_yardstick_pool_config.py -q
```

## Sources

- @gambling-wiki/sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
- @gambling-wiki/entities/tools/adversarial-coevolution.md
- @gambling-wiki/sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md
