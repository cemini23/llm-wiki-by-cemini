# Super-audit fixes — implementation plan (Opus)

## Target

claude.ai / operator — sandbox HU bot before next Arena submit.

## Summary

Five-model super-audit P0/P1 patches for maniac/LAG exploit, bundle parity, and gate validation before `--replace` submit.

**Source:** 5-model super-audit 2026-06-08 (3 Cursor + GLM 5.2 + Fusion)

## P0 — ship blockers

| # | Patch | File | Owner |
|---|-------|------|-------|
| 1 | Bundle `trajectory_bound_config.json` | `submit_sandbox_pvp.py` | exec-1 |
| 2 | Defer gin preflop on HU BB facing bet → S1B/chart defend | `gin_style.py` | exec-2 |
| 3 | Fix HU 3-bet sizing (`pot` not `pot+call_chips`) | `s1b_exploit.py` | exec-2 |

## P1 — maniac/LAG lift

| # | Patch | File | Owner |
|---|-------|------|-------|
| 4 | Flip HU maniac margins (less call-station, more raise) | `cemini_decide.py` | exec-3 |
| 5 | Lower postflop `raise_bar` vs maniac/LAG | `cemini_decide.py` | exec-3 |
| 6 | Widen HU 3-bet stack cap 22%→32%; fix LAG 3-bet mult | `s1b_exploit.py` | exec-2 |
| 7 | HU iso: allow BB/SB positions | `s1b_exploit.py` | exec-2 |

## P2 — bundle/runtime parity

| # | Patch | File | Owner |
|---|-------|------|-------|
| 8 | Harness deadline from table; sanitize reasoning | `harness/strategy.py` | exec-1 |
| 9 | Fix audit pack path doubling | `build_audit_pack.py` | exec-1 |

## Validation

1. `uv run pytest tests/test_garip_mixture.py tests/test_trajectory_bound.py -q` (focused)
2. `CEMINI_TABLE_FORMAT=hu bash scripts/run_hu_sandbox_gate.sh --hands 200`
3. Target: maniac series_win ≥ 30% (stretch 38%); gate PASS
4. Rebuild bundle + `submit --build --replace`

## Submit

After validation + re-audit WARN or better: `uv run python examples/submit_sandbox_pvp.py --build --replace`

## Sources

- [Source: agents/devfun-poker-arena/briefs/2026-06-08_sandbox-super-audit-synthesis.md]
- [Source: agents/devfun-poker-arena/reports/researcher-round/gate-hu-20260623T225411Z/]
