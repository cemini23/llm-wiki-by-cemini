---
title: K164 — CCS-MCCFR correlated chance sampling steal
type: brief
target: Poker Arena
created: 2026-07-30
updated: 2026-07-30
---

## Target

`agents/devfun-poker-arena/` — offline MCCFR / blueprint / TexasSolver research only.

## Summary

arXiv 2607.27035 (Li / Chen / Huang): **CCS-MCCFR** replaces i.i.d. chance draws with a **persistent randomized Weyl stream per concrete chance node**. Large Kuhn/Leduc exploitability cuts; Linear CFR + CCS best in paper’s grid. Drop-in, no new hyperparameters. **No author repo.**

## Body

### Do

1. Add research note: if offline External Sampling MCCFR (OpenSpiel / TexasSolver bake) still uses i.i.d. chance, evaluate CCS sampler as one-line change.
2. Prefer composing with **Linear CFR** when testing update×sampler cells.
3. Validate on Kuhn/Leduc first; re-measure before assuming HUNL endgame transfer (paper muted there).

### Do not

- Touch live `decide()` / Playground Active / interrupt DeepCFR or blueprint measurement windows for this steal alone
- Treat CCS as a submit gate
- FOSS adopt / prod scp / Atto / TipDrop / CeminiDFS (none)

## Sources

- arXiv 2607.27035 — [https://arxiv.org/abs/2607.27035](https://arxiv.org/abs/2607.27035)
- `@sources/arxiv-2607.27035-correlated-chance-sampling-mccfr-2026-07-30.md`
- Gambling twin (external): `Gambling wiki/wiki/sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md`

## Shipped

- `references/ccs-mccfr-chance-sampling.md`
- Cross-links from `deepcfr-lite.md`, `swap-regret-training-notes.md`
- Watch twin remains shelf: `briefs/2026-07-30_k213-ccs-mccfr-watch.md`
- `tests/test_k164_k221_k227_docs.py`
