## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-hard-escalate.md).

# Escalate — texas-solver-hard-v1 (audit-fixed)


## Summary

Operator brief: 2026-07-21 texas-solver-hard-escalate. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-hard-escalate.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Active

- Competition: `cmr3n8tft01nilecm1u5jlny7`
- Pin: `researcher-ladder-s1.texas-solver-hard-v1.auditfix.2026-07-21`
- Gate: `gate-hu-20260721T132055Z` PASS (lag series 40%)
- Bundle SHA: `036a53ecd8212a95927a6c3a3e399c872917ae480c90cf547dfa707652ad071d`
- Replace submission: `93dfd8e2-ff1e-46b0-ab3d-7e611544edd7` → **Active continuous** (smoke 5h adj −60 noise; PvP live)

## What shipped

1. **Hard mixed-strategy sampling** (`CEMINI_SOLVER_HARD=1` default) — play σ from bake freqs, not soft equity nudge.
2. **Audit fixes (super-audit REWORK):**
   - Free postflop: hard σ **before** Gin `try_postflop_free` when freqs exist.
   - Facing: hard σ **after** leak-fold library (S28/Q6/etc.).
   - `allin` / `all-in` alias in sampler + facing raise path.
3. Engine stays `cemini`. DeepCFR / opponent modes off.

## Honest competitive posture

- **Not** top-of-LB ready. Densify bake incomplete (TexasSolver hangs on new grid spots).
- Still `texas_solver_v1` provenance on most keys; pin says hard-v1 not v2 densify.
- Success bar: μ **better than −37.6** @ ≥3k hands. Stretch ≤−28. Rollback if ≤−43.
- Top-15 probability remains <<5% until real dense solver blueprint lands.

## Super-audit (2026-07-21)

- Mode: security · Cursor: Opus + Kimi + GLM · API: Fusion
- Consensus: **REWORK** then patched above → re-gate + replace.
- Remaining backlog (do not claim done): densify bake, per-key provenance, size_pot_frac diversity.

## Poll

```bash
ssh cemini-prod 'cd /opt/devfun-poker-arena && . venv/bin/activate && \
  python3 examples/submit_sandbox_pvp.py --poll <ACTIVE_ID>'
```

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
