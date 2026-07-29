## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-22_blueprint-v3-escalate.md).

# Escalate — blueprint v3 live


## Summary

Operator brief: 2026-07-22 blueprint-v3-escalate. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-22_blueprint-v3-escalate.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Active

- Pin: `researcher-ladder-s1.blueprint-v3.2026-07-22`
- Bake: **90/90** spots · **540** keys · `texas_solver_blueprint_v3`
- Flags: `CEMINI_SOLVER_V3=1`, `CEMINI_SOLVER_HARD=0`
- Replace: `95d6e082-3092-4827-a8da-6fa83a4d9902` — **Continuous Active** (v3 bundle)
- Bundle SHA: `b2d3da52cf0981fb1d4d9c16a10149e01a1e72f2a44ffdc99029b993cdb30790`
- Bundle contains: `assets/solver_policy_v3.py` + `assets/research/postflop_hu_buckets_v3.json` + `CEMINI_SOLVER_V3=1`
- **2026-07-22 brief steals** (agreement gate / K182 / K144): code on prod disk + gate PASS; **Arena `--replace` blocked by daily limit (3/day)** — ship tomorrow to put steals in Active zip. Live ladder already on v3 policy.

## Jul 22 steals shipped (light)

| Steal | Status | Notes |
|-------|--------|-------|
| **WP1** Offline agreement gate | **shipped** | `examples/blueprint_v3_agreement_gate.py` + `tests/test_blueprint_v3_agreement.py` |
| **K182** Pin-hash on sandbox-pass claim | **shipped** | `claimed_authorization.py` — deny submit without matching `bundleSha256` / `CEMINI_PIN_BUNDLE_SHA` |
| **K144** `segment_select_cap` | **shipped** | `cemini_hl_brief.py` — advisory cap before brief expansion; audit via `CEMINI_HL_SEGMENT_AUDIT=1` |
| K203/K205 no-fit | skipped | — |
| K204 hardspot RL | lab only | — |
| K204/K205 HITL | docs reference | — |

## Agreement gate status

Run after bake or dump refresh:

```bash
uv run python examples/blueprint_v3_agreement_gate.py
```

Report: `reports/blueprint-v3-agreement.json`

| Metric | Bar |
|--------|-----|
| Mean TV (held-out dumps vs baked) | ≤ **0.25** |
| Free-node argmax agreement (combos≥20) | ≥ **0.55** |

**Replace:** not blocked by gate failure — gate is offline QA; live pin already on V3. Re-run gate before next bake-driven replace.

## What this is

Per-hand-bucket free/facing-split σ from TexasSolver — not soft-bias rollback, not mashed v2 hard-σ.

Key: `street|line|role|texture|spr|node|hand_bucket`

## Bars

| | μ |
|--|---|
| Target | **≥ 0** @ ≥3k |
| Rollback | ≤ **−50** @ ≥3k |

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
