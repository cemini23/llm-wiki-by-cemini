# DeepCFR-lite (Phase 3)

Offline tabular regret-matching over the existing HU postflop bucket
infosets (`street|role|texture|strength_bin`). Not full open_spiel NLHE
DeepCFR — that stays deferred (GPU week).

## Artifacts

| Path | Role |
|------|------|
| `examples/deepcfr_lite_train.py` | Offline trainer |
| `research/deepcfr_hu_buckets.json` | Baked average strategy (`generator=deepcfr_lite_v1`) |
| `research/postflop_hu_buckets.json` | Prior / fallback (`texas_solver_v1`) |

## Flags

- `CEMINI_DEEPCFR=1` — prefer DeepCFR bake for `solver_frequencies` lookups
- `CEMINI_DEEPCFR_PATH` — override path (tests)
- Requires `CEMINI_POSTFLOP_BUCKETS=1`
- Researcher harness setdefaults `CEMINI_DEEPCFR=1`; **does not** enable opponent modes

## Bias

`deepcfr_lite_v1` and `texas_solver_v1` share Phase-1 solver scale:
clamp ±0.14, free 0.15, facing 0.18/0.15/0.225.

## Retrain

```bash
uv run python examples/deepcfr_lite_train.py --iters 50000 --seed 7 --force
```
