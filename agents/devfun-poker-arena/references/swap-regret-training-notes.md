# Swap-regret / regret-loss training notes (K198)

**arXiv:** [2607.23333](https://arxiv.org/abs/2607.23333) — single-layer attention +
(swap) regret loss ≈ smoothed fictitious play / CE-seeking updates  
**Brief:** `briefs/2026-07-28_k198-swap-regret-verifier-gap-steal.md`  
**Shelf confirm:** `briefs/2026-07-29_k163-swap-regret-attention-shelf.md` (K163 — no runtime torch)  
**Wiki:** `@concepts/swap-regret-attention-fictitious-play.md` ·
`@gambling-wiki/concepts/swap-regret-attention-fictitious-play.md`

## Steal (theory only)

Regret-matching / MAFP-style lanes can treat **regret loss** (and optionally
**swap-regret** loss) as a training objective that induces smoothed fictitious
play asymptotics. Useful framing for offline bake / league opponent mix — **not**
a drop-in runtime model inside `cemini_decide()`.

## Operator rules this cycle

| Do | Do not |
|----|--------|
| Keep notes here for MAFP / regret bake experiments | Hard-gate sandbox submit on regret-loss score |
| Pair any regret bake with frozen yardsticks | Promote decide() because self-play regret ↓ |
| Prefer CE/CCE-seeking offline updates | Ship torch/attention at Arena zip runtime |

## Promotion coupling (required)

Self-improved regret objectives are **self-authored verifiers** if used alone.
See `references/verifier-deployment-gap.md` (K198) +
`references/league-promotion-rubric.md` + `references/expert-yardstick-pool.md`
+ `references/play-adequacy-gates.md`.

## Related

- `references/deepcfr-lite.md` — offline bake path (separate)
- `config/hu_yardstick_pool.json` — external grade surface
- `@gambling-wiki/sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md`
