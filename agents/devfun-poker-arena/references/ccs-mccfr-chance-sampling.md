# CCS-MCCFR correlated chance sampling (K164)

**arXiv:** [2607.27035](https://arxiv.org/abs/2607.27035) — Correlated Chance
Sampling MCCFR (persistent Weyl stream per concrete chance node)  
**Briefs:** `briefs/2026-07-30_k164-ccs-mccfr-chance-sampling-steal.md` ·
Watch twin `briefs/2026-07-30_k213-ccs-mccfr-watch.md`  
**Wiki:** `@gambling-wiki/sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md`

## Steal (offline bake only)

If External Sampling MCCFR (OpenSpiel / TexasSolver / blueprint bake) still draws
chance **i.i.d.**, evaluate a **persistent randomized Weyl stream per chance
node** as a drop-in sampler. Paper reports large Kuhn/Leduc exploitability cuts;
compose preferably with **Linear CFR**. No new hyperparameters; **no author repo**.

## Operator rules this cycle

| Do | Do not |
|----|--------|
| Keep this note next to DeepCFR / swap-regret shelves | Wire CCS into live `cemini_decide()` |
| Trial on Kuhn/Leduc before assuming HUNL endgame transfer | Treat CCS score as a sandbox submit gate |
| Prefer Linear CFR × CCS cells when comparing samplers | Interrupt Playground / Active measurement windows for this alone |

## Related

- `references/deepcfr-lite.md` — tabular HU bake path
- `references/swap-regret-training-notes.md` (K198) — regret-loss shelf
- `references/blueprint-v3.md` — offline agreement gate
- `references/texas-solver-v2-hard.md` — solver bake (separate)
