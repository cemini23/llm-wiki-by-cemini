# Defender-utility eval ranking (K197)

Steal from A-MESS (defender-centric utility): when selecting training / red-team / leak spots, rank by **downstream utility** under budget — not raw fail rate alone.

## Rules

1. Do not expand SFT / bake effort on highest-fail spots alone.
2. Prefer compact high-utility subsets (marginal lift vs cost).
3. Attribute utility simply when choosing which leaks to fix next.

Helper: `examples/eval_spot_utility.py` → `rank_spots_by_utility`.

Advisory only — not a hard submit gate.
