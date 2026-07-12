## Target

`agents/devfun-poker-arena/` — Researcher Round HU sandbox yardstick discipline.

## Summary

K160 inbox re-archive **deep-read** of 2607.06854: lightweight imperfect-info agents are **information-bound**, not capacity-bound. Reaffirm K151/K152 steals — fixed expert yardstick, trust-region + curriculum + best-checkpoint; reject imitation/DAgger and LLM train opponents.

## Body

### Regime disclosure

**Regime-conditioned scope:** all win-rate and ISMCTS figures below are from arXiv:2607.06854 **Gin Rummy** (+ Leduc transfer) with a fixed rule expert yardstick — **not** dev.fun HU NLHE TrueSkill or Arena leaderboard. Treat as single-regime card-game ablations; NLHE promotion requires separate Leduc/RLCard gate per K152.

### Confirmed helps (replicate in league promotion)

| Technique | Arena mapping |
|-----------|---------------|
| Trust-region updates | Stable policy steps in `cemini_decide` trajectory bound |
| Rising opponent curriculum + PFSP-style sampling | Nemesis ladder / MAFP pool |
| Warm-start + keep best checkpoint | Sandbox bundle promotion gate |
| Sparse well-aimed reward | Avoid dense shaping in HU eval |

### Confirmed fails (do not re-open without new evidence)

- Short/long reward shaping
- Imitation / DAgger (causal confusion)
- Live LLM as train opponent (too slow)
- Capacity chase (wider/deeper encoders)

### Yardstick discipline (regime scope)

Paper regime: **Gin Rummy** primary benchmark + **Leduc Hold'em** transfer; fixed rule-based expert yardstick never in training. Arena mapping is **analogy only** for HU NLHE sandbox — do not treat Gin/Leduc win-rate bands as NLHE calibration targets without separate replication.

Expert beats all trained agents 70–99%; self-play champion ~30–36% vs expert after stacking helps. Fair ISMCTS ~26% vs oracle ~85% — hidden information dominates **in card-game regime above**.

### Operator checklist

- [x] Document style-preservation / yardstick gap in league promotion rubric (pair K152 brief)
- [x] FootsiesGym exploitability advisory stays separate env — do not conflate with NLHE league metrics

## Shipped (2026-07-12)

Paired with K153: `references/league-promotion-rubric.md`, `compute_league_promotion_rubric_advisory()`, gate script advisory echo. See `briefs/2026-07-12_k153-mppo-style-opponent-steal.md`.

## Sources

- @wiki/sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md
- @wiki/sources/arxiv-footsiesgym-2607.06514-2026-07-09.md
- agents/devfun-poker-arena/briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steal.md
