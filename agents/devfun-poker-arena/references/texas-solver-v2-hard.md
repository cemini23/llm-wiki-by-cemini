# Texas Solver v2 — dense bake + hard σ

## Runtime

`CEMINI_SOLVER_HARD=1` (harness default): sample action from bake freqs when
postflop bucket resolves. Fail-open to soft bias / heuristics.

## Bake (v2)

- Grid: `research/texassolver_spot_grid.json` (90 spots)
- Output: `research/postflop_hu_buckets.json` · `meta.generator=texas_solver_v2` when ≥60 spots succeed
- Defaults: `thread_num=2`, `use_isomorphism=0`
- Abort recovery: on crash, retry with `thread=1` / `iso=0`
  (TexasSolver v0.2.0 SIGABRT exit 134 on some boards with 8 threads + iso)

```bash
uv run python examples/bake_texassolver_buckets.py --timeout 180
```

## Decide order

1. Free: hard σ **before** Gin `try_postflop_free` when freqs exist
2. Facing: leak-fold library first, then hard σ
3. Soft bias remains fail-open path

## Engine

`CEMINI_SANDBOX_ENGINE=cemini` only. DeepCFR / opponent modes off for this pin.
