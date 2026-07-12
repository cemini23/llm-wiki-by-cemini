# Expert yardstick pool — HU sandbox (K152)

Operator spec from arXiv **2607.06854** (lightweight game agents) + **2607.07078**
(forgetting-factor regret). Config: `config/hu_yardstick_pool.json`.

## Fixed expert outside train loop

Grade Researcher / HL checkpoints against a **frozen yardstick pool** — not
self-play win rate alone and not live ladder TrueSkill as a train target.

| Handle | `min_bb100` | Role |
|--------|-------------|------|
| `ten` | 0 | Wide-passive nemesis (K150 ladder) |
| `maniac_shark_lag` | 0 | Linear-aggro nemesis (K151 ladder) |
| `tight` | -5 | HU regression rock baseline |
| `lag` | -10 | Maniac/lag series advisory lane |

`never_train: true` — yardstick opponents are **eval-only**. Do not backprop,
tune, or HL-select against yardstick bb/100.

## Curriculum + keep-best (06854 ablations)

From lightweight-agent ablations (and adversarial-coevolution read-only notes):

| Helps | Skip |
|-------|------|
| Rising opponent curriculum | Dense short-term reward shaping |
| Warm-start + **keep best checkpoint** | Capacity chase (wider/deeper nets) |
| Trust-region / disciplined updates | Live LLM as train opponent |
| Well-aimed sparse reward | Imitation / DAgger (causal confusion) |

**Ceiling is information-bound, not capacity-bound.** Prefer tougher frozen
yardsticks + best-checkpoint discipline over MC sample-count or model-size
escalation.

## Forgetting-factor regret (07078)

When league / MAFP opponent mix drifts, log **recency-weighted** bb/100
alongside lifetime mean from HU trajectory `hand_result` rows.
`drift_flag` when recent performance sags vs lifetime — advisory for HL epoch
reviews, not a submit gate.

CLI: `--forgetting-decay` (default `0.95`) on `researcher_trajectory_summary.py`.

## What not to port

- Gin Rummy gold agent as NLHE opponent
- Live LLM opponent inside the training loop
- DAgger / heavy embedding stacks (paper negative results)
- `Nikelroid/adversarial-coevolution` code — **NO LICENSE** until SPDX added

## Leduc validation (pre-NLHE promotion)

Run RLCard tabular optimum sanity check on Leduc before claiming NLHE
promotion from yardstick passes alone. HU sandbox yardstick grade is
necessary but not sufficient.

**K153 style preservation:** before NLHE league pool upgrades, run
`bash scripts/run_rlcard_style_drift_trial.sh` and review D_policy TV vs
seed archetype (`references/mppo-style-preservation.md`). Pair with
`references/league-promotion-rubric.md` (K160).

## K160 regime scope

Gin Rummy / Leduc figures from 2607.06854 are **single-regime ablations** —
not NLHE TrueSkill calibration. FootsiesGym exploitability advisory stays a
**separate env** (`footsiesgym_separate` in league rubric).

## Implementation

| Artifact | Purpose |
|----------|---------|
| `config/hu_yardstick_pool.json` | Frozen pool spec |
| `compute_yardstick_pool_grade()` | `% pass` vs `min_bb100` per handle |
| `compute_forgetting_factor_regret()` | Recency-weighted bb drift |
| `scripts/run_hu_sandbox_gate.sh` | Advisory echo after TEN/shark audits |

## Related (gambling-wiki)

- `@gambling-wiki/sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md`
- `@gambling-wiki/sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md`
- `@gambling-wiki/entities/tools/adversarial-coevolution.md`
- `references/footsiesgym-raeth-axis-map.md` (K151 exploitability advisory)
- `briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steal.md`
