---
title: Master plan — opponent modes + deeper TexasSolver bake
type: brief
target: Poker Arena
created: 2026-07-19
updated: 2026-07-19
---

## Target

`agents/devfun-poker-arena/` — Grok implements; Cursor gate + **`--replace`** (real policy delta).

## Summary

Close the μ gap vs S1 field (#178/261, μ≈−38 on Active `a7a677b7`):

1. **Opponent-conditioned modes** — map K156 risk-spectrum / HUD VPIP·PFR → bounded best-response overlays (`nit` / `lag` / `wide_passive` / `balanced`).
2. **Deeper solver bake** — expand HU spot grid (~30→≥42), re-aggregate `texas_solver_v1`, keep O(1) hot path.

Today's brief `2026-07-19_k174-no-fit.md`: **no decide steal** — ignore for ship.


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Non-goals

- No gin flip / DeepCFR / runtime LLM / runtime TexasSolver
- No new river-guard micro-patches as primary ship
- Do not copy frontier-LLM *aggression spectra* into decide — only **best-response** modes vs tagged foes
- No Arena `--replace` from Grok (Cursor owns)

## Baseline (replace metric)

| | Value |
|--|-------|
| Active | `a7a677b7` |
| hands | ~13.7k |
| μ | ≈ −38 |
| score | ≈ −56.5 |
| rank | ~178/261 |

Success after replace: μ **better than −38** over ≥3k hands on new Active (primary). Rank exit from bottom third is stretch.

---

## WP1 — Opponent modes (Phase 2)

**Files**

- `examples/opponent_modes.py` (new)
- `examples/cemini_decide.py` — wire after HUD enrich
- `examples/risk_spectrum.py` — allow `mode_from_spectrum` import path (no band retune unless tests require)
- `harness/strategy.py` — `CEMINI_OPPONENT_MODES=1` setdefault
- `tests/test_opponent_modes.py` (new)
- `references/opponent-modes.md` (new)
- Update `references/risk-spectrum-tags.md` — modes are best-response, still not “copy GPT VPIP”

**Mode map** (from participation × proactiveness):

| participation | proactiveness | mode |
|---------------|---------------|------|
| low | low/medium | `nit` |
| high | high | `lag` |
| high | low/medium | `wide_passive` |
| else | else | `balanced` |

Cold-start / missing HUD → `balanced` (no overlay).

**Bounded overlays** (clamp each delta ±0.06; stack with existing margins, do not replace private HUD exploits):

| mode | intent | deltas (approx) |
|------|--------|-----------------|
| `nit` | steal more, bluff more, fold to aggression | lower bet_bar (−0.04), raise fold_slack (+0.04), lower open equity bar |
| `lag` | tighten calls, fewer bluffs, trap | higher bet_bar (+0.04), lower fold_slack (−0.03), higher call_margin |
| `wide_passive` | value bet / iso more | lower bet_bar (−0.05), lower call_margin slightly |
| `balanced` | zero | — |

Wire: derive spectrum via `attach_risk_spectrum_to_hud` / HUD vpip·pfr → `resolve_opponent_mode` → merge into `margins` dict used by postflop/preflop paths. Flag off → byte-identical (test).

**Acceptance**

```bash
uv run pytest tests/test_opponent_modes.py -q --tb=line
# flag off parity fixture + at least one mode changes action vs balanced on a fixture table
```

---

## WP2 — Deeper TexasSolver bake

**Files**

- `research/texassolver_spot_grid.json` — add ≥12 spots (4 flop dry/wet/paired mix + 4 turn + 4 river); keep street-scoped trees; dumps under `/tmp/cemini-texassolver-dumps`
- `examples/bake_texassolver_buckets.py` — already street-scoped; no path-with-spaces
- `examples/postflop_buckets.py` — bump texas_solver bias: clamp **±0.16**, free_mult **0.18**, facing ~1.2× current solver scale
- Re-run bake (cache hits + new solves)
- `research/postflop_hu_buckets.json` stays `generator=texas_solver_v1`, `spots_solved≥42`

**Acceptance**

```bash
uv run python examples/bake_texassolver_buckets.py --timeout 180
python -c "import json;d=json.load(open('research/postflop_hu_buckets.json'));m=d['meta'];assert m['generator']=='texas_solver_v1';assert m['spots_solved']>=42;assert len(d['buckets'])>=90"
uv run pytest tests/test_postflop_buckets.py -q --tb=line
```

---

## WP3 — Gate + escalate (Grok writes brief; Cursor replace)

```bash
uv run pytest tests/test_opponent_modes.py tests/test_postflop_buckets.py tests/test_mafp_chart_wire.py -q --tb=line
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only
```

Escalate: `briefs/2026-07-19_opponent-modes-deeper-bake-escalate.md`  
Pin: `researcher-ladder-s1.opp-modes-bake-v2.2026-07-19`

**Cursor after green:** rsync → prod `--build-only` → `--replace --competition-id cmr3n8tft01nilecm1u5jlny7` → poll Active continuous.

---

## Grok paste

See `briefs/2026-07-19_opponent-modes-deeper-bake-grok-prompt.md`.

## Sources

- Live: Active `a7a677b7` μ≈−38 @13.7k; rank ~178/261
- K156 risk spectrum; K174 no-fit; prior texas_solver bake briefs
