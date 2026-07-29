## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-22_blueprint-v3-master-plan.md).

# Master plan — Blueprint v3 (play like the field)

**Created:** 2026-07-22  
**Goal:** Competitive HU ladder policy — offline CFR blueprint with per-hand-bucket σ, not soft-bias recovery.


## Summary

Operator brief: 2026-07-22 blueprint-v3-master-plan. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-22_blueprint-v3-master-plan.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Why rollback is not the plan

Soft-bias μ≈−37 / rank ~200 never won. Hard-σ on mashed 90-key averages hit μ≈−69.  
Rolling back stops bleeding; **it is not how we get to the top.**

Tops: **blueprint abstraction + play mixed strategy from real info sets.**  
We build the feasible laptop version of that.

## Architecture (v3)

| Piece | Spec |
|-------|------|
| Key | `street\|line\|role\|texture\|spr\|node\|hand_bucket` |
| Free vs facing | Separate `node` — never one mashed vector |
| Aggregation | Per combo → hand_bucket at each solver node |
| Sizes | bet 33/75/allin; raise 60/allin |
| Runtime | O(1) lookup + sample when coverage≥τ; soft-bias fail-open only |
| Solve | TexasSolver thread=1 iso=0; street-scoped trees |

## Success (not “back to −37”)

1. Offline: held-out solver agreement gate before harness default on  
2. Online: **μ ≥ 0 @ ≥3k hands** (stretch: top half). Soft floor only for fail-open.

## Soft Active

Keep current soft rollback live as floor while v3 bakes. Flip `CEMINI_SOLVER_V3=1` only after smoke + agreement gate.

## Files (2026-07-22)

| Path | Role |
|------|------|
| `examples/solver_policy_v3.py` | O(1) lookup + sample |
| `examples/bake_blueprint_v3.py` | Offline TexasSolver bake |
| `research/texassolver_spot_grid_v3.json` | 90 spots (30 boards × 3 SPR) |
| `research/postflop_hu_buckets_v3.json` | Baked blueprint (generated) |
| `references/blueprint-v3.md` | Canon |
| `tests/test_blueprint_v3.py` | Unit tests |

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
