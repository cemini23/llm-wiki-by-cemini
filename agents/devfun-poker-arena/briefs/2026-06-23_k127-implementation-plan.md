# K127 implementation plan (2026-06-23)

## Target

`agents/devfun-poker-arena/` — offline HU chart refinement (GARIP P0).

## Summary

Implement K127 GARIP running-average villain mixture anchor alongside K124 MAFP: Polyak μ̄_t best-response, deploy telemetry (`garip_alpha`, `mixture_l2_drift`), tests and smoke script. CeminiDFS / castle sim / PM are out of scope for this plan.

**Author:** Opus planning pass · **Execute:** poker worker only (this repo).

## Scope (this session)

| Track | Where |
|-------|--------|
| **GARIP (P0)** | `agents/devfun-poker-arena` — **here** |
| CeminiDFS sportsdataverse | Separate session |
| Castle sim | Separate session |
| PM Agentic TM | Not in scope |

**Out of scope:** prod flip (`researcher_jun21_beta_apply.sh`), MARSHAL-Kuhn HF training (NO LICENSE).

---

## Track 1 — GARIP chart refinement (P0)

### Goal

Replace K124 MAFP’s per-round instantaneous mixture μ_t with Polyak running average μ̄_t as the best-response anchor (GARIP magnet). Log `garip_alpha`, `mixture_l2_drift` each round to `deploys.jsonl`.

### Design

1. **`examples/garip_mixture.py`**
   - `polyak_update_mixtures(prev, current, alpha)` — same nested dict shape as `aggregate_stance_mixtures`.
   - `mixture_l2_drift(a, b)` — L2 on fold/call/raise vectors across stance×position×bucket keys.
   - `snapshot_mixtures(mixes)` — deep copy for R-NaD ablation baseline.

2. **`examples/garip_chart_refinement.py`**
   - Reuse K124: `collect_preflop_audit`, `best_response_chart_update`, `write_mafp_chart`.
   - Loop: audit → μ_t → μ̄_t ← (1−α)μ̄_{t−1} + α μ_t → BR(μ̄_t).
   - CLI: `--garip-alpha` (default 0.3), `--max-rounds`, `--aggregate-hands`.
   - Deploy notes JSON: `garip_alpha`, `mixture_l2_drift`, `garip_round`, `chart_changes`, `delta_ev`.

3. **P1 ablation (same script)**
   - `--r-nad-snapshot-every N` — also compute BR against snapshot μ_t every N audit hands; log `r_nad_delta_ev_gap` vs GARIP path in notes (no second chart write).

4. **`scripts/run_garip_chart_refinement.sh`** — uv runner, `--no-write` default for CI smoke.

5. **Tests** — `tests/test_garip_mixture.py` (polyak convergence, drift monotonicity on constant mix).

### Acceptance

- `uv run pytest tests/test_garip_mixture.py tests/test_mafp_chart_refinement.py` pass.
- `bash scripts/run_garip_chart_refinement.sh` completes ≤3 min on laptop.
- `deploys.jsonl` row with `source=garip_chart_refinement` includes `garip_alpha` + `mixture_l2_drift`.

### Dependencies

- K124 MAFP (`mafp_chart_refinement.py`) — shared helpers, no fork.
- K125 trajectory bound — orthogonal; enable on submit path only.

## Execution order

1. GARIP P0 (offline chart before HU PvP announce).
2. Wiki filing after tests pass.

## Risk

| Risk | Mitigation |
|------|------------|
| GARIP α too high → stale magnet | Default α=0.3; log drift; tune in P1 |

## Sources

- [Source: arXiv:2606.22688 (retrieved 2026-06-23)]
- @wiki/concepts/garip-running-average-self-play.md
- `briefs/2026-06-23_k127-garip-running-average-self-play-steal.md`
