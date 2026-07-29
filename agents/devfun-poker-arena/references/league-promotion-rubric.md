# League promotion rubric — yardstick + style gap (K153 + K160)

Advisory rubric for Researcher Round HU sandbox bundle promotion. **No hard
gate failures** on yardstick or style metrics.

## Regime scope (K160)

Paper yardstick figures (2607.06854) are **Gin Rummy + Leduc transfer** with a
fixed rule expert — **not** dev.fun HU NLHE TrueSkill. Treat Gin/Leduc win-rate
bands as single-regime ablations; NLHE promotion needs separate replication.

**Information-bound, not capacity-bound.** Prefer frozen yardsticks + trust-region
+ best-checkpoint over model-size escalation.

## Three advisory lanes (do not conflate)

| Lane | Schema | Env |
|------|--------|-----|
| Yardstick pool grade | `devfun.yardstick_pool_grade.v1` | HU NLHE sandbox |
| Style drift D_policy | `devfun.style_drift_d_policy.v1` | League archetype upgrade |
| Exploitability advisory | `devfun.exploitability_advisory.v1` | **FootsiesGym separate** |

FootsiesGym H2H skill vs yardstick disconnect is tagged
`env: footsiesgym_separate` in the league rubric — never mixed into NLHE
promotion score.

## Promotion gaps (advisory)

`compute_league_promotion_rubric_advisory()` surfaces:

- **yardstick_gap** — `pct_pass` below 1.0 on frozen pool
- **style_gap** — D_policy TV above `max_d_policy_tv_advisory`
- **forgetting_drift** — recency-weighted bb sag vs lifetime
- **footsiesgym_note** — present only when exploitability advisory flags disconnect

Stronger self-play or soft-field crush does **not** override style or yardstick
gaps.

## Verifier–deployment gap (K198)

Self-authored pytest / regret-loss improvement is **not** a promotion signal.
Require external yardsticks + play-adequacy fixtures. See
`references/verifier-deployment-gap.md` and
`references/swap-regret-training-notes.md`.
Evidential ceiling on modest clean boards: `references/eval-claim-ceiling.md` (K220).

## Confirmed helps / fails (K160)

| Helps | Fails |
|-------|-------|
| Trust-region / trajectory bound | Dense reward shaping |
| Rising opponent curriculum | Imitation / DAgger |
| Warm-start + keep best checkpoint | Live LLM train opponent |
| Sparse well-aimed reward | Capacity chase |

## Operator flow

1. HU gate harvest → yardstick pool grade + forgetting regret (K152)
2. Optional style dist inputs → style drift + league rubric (K153)
3. Leduc trial before NLHE league pool edits
4. Human GO on bundle promotion — rubric is input, not veto

## Artifacts

| Path | Purpose |
|------|---------|
| `config/hu_yardstick_pool.json` | Frozen yardstick opponents |
| `config/hu_style_preservation.json` | D_policy thresholds + β note |
| `references/mppo-style-preservation.md` | MPPO operator spec |
| `scripts/run_rlcard_style_drift_trial.sh` | Leduc stylized trial |
