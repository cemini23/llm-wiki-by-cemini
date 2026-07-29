# Blueprint v3 — per-hand-bucket TexasSolver policy

**Status:** bake offline; runtime gated on `CEMINI_SOLVER_V3` + coverage.

## Key schema

```
{street}|{line}|{role}|{texture}|{spr}|{node}|{hand_bucket}
```

| Field | Values |
|-------|--------|
| street | flop, turn, river |
| line | srp (v1) |
| role | ip, oop |
| texture | dry, wet, paired |
| spr | le2 (≤2), 2to5 (2–5), gt5 (>5) |
| node | free **or** vs_small / vs_mid / vs_big / vs_over / vs_raise |
| hand_bucket | air, weak_pair, mid_pair, tp_weak, tp_good, overpair, two_pair_plus, nutted, draw_weak, draw_strong, combo_draw |

**Critical:** FREE and FACING never share one frequency vector. `node=free` uses check/bet_033/bet_075/allin; facing nodes use fold/call/raise_060/allin.

## Bake

```bash
uv run python examples/bake_blueprint_v3.py --max-spots 4 --timeout 180   # smoke
uv run python examples/bake_blueprint_v3.py --timeout 900                 # full grid (90 spots)
```

- Grid: `research/texassolver_spot_grid_v3.json`
- Output: `research/postflop_hu_buckets_v3.json`
- Dumps: `/tmp/cemini-texassolver-dumps-v3`
- Solver: TexasSolver v0.2.0, `thread_num=1`, `use_isomorphism=0`
- Bet sizes: 33%, 75%, allin; raise 60%, allin
- Aggregation: **per combo → hand_bucket** (not range-average)

## Runtime

| Env | Effect |
|-----|--------|
| `CEMINI_SOLVER_V3=1` | Enable v3 lookup + sample when coverage OK |
| `CEMINI_BLUEPRINT_V3_PATH` | Override JSON path |
| `CEMINI_SOLVER_HARD=0` | Keep off (v1 mashed keys failed μ≈−69) |

Fail-open only: missing key or low coverage → soft-bias / Gin / equity heuristics.

### Decide wiring (`cemini_decide.py`)

- **Free:** before Gin `try_postflop_free` when coverage hits
- **Facing:** after leak-fold library when coverage hits

Engine stays **cemini** (`harness/strategy.py` setdefaults `CEMINI_SOLVER_V3=1` after v3 bake).

## Offline agreement gate

Before treating bake as production-ready, run held-out dump vs baked JSON check:

```bash
uv run python examples/blueprint_v3_agreement_gate.py
```

- Hold-out: last ~20% of grid spots **or** spots with `_gt5` suffix (with dumps)
- PASS: mean TV ≤ **0.25** AND free-node argmax agreement ≥ **0.55** (combos≥20)
- Report: `reports/blueprint-v3-agreement.json`
- Exit 0 = PASS, 1 = FAIL

## Success metric

- Offline: held-out solver agreement gate before harness default-on
- Arena: **μ ≥ 0 @ ≥3k hands** — not “recover −37” soft floor

See `briefs/2026-07-22_blueprint-v3-master-plan.md`.
