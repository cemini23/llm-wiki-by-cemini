## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — Researcher Round (Jun 21 beta).

## Summary

Steal **VERITAS** generator-verifier pattern (arXiv 2606.18247): keep `decide()` as generator, add a **gradient-free verifier stack** at inference to steer actions before Arena submit — no weight updates, optional trajectory flywheel into HL loop.

## Body

### Scope / regime disclosure

| Dimension | VERITAS paper (2606.18247) | Cemini target |
|-----------|------------------------------|---------------|
| Domain | Robot manipulation (visual) | **6-max NLHE** symbolic state [TENTATIVE operator] |
| Generator | π₀ generalist | `cemini_decide.py` heuristic |
| Verifier | Visual outcome scorer | Legality + regression + MC equity + axis proxies |
| N candidates | Action chunks (robot) | {fold, call, raise sizes} per decision point |

Architecture is **regime-conditioned** steal — do not claim robot benchmark numbers transfer to poker LB.

### P0 — verifier stack (pre Jun 21)

1. **Hard gates (always on):** illegal action reject; reasoning YAML ≤150 chars; amount semantics.
2. **Regression oracle:** if spot matches `regression_spots.py` fixture, force oracle action (existing path).
3. **MC equity floor:** block high-variance bluff lines below configurable equity threshold on river [TENTATIVE threshold — calibrate on Playground].
4. **M₈ factual:** reject actions whose reasoning YAML cites impossible hand/pot facts (regex + treys cross-check).

### P1 — Best-of-N spike (optional)

When primary `decide()` returns marginal spot (e.g., borderline steal / thin value):

- Sample N ∈ {2, 3} legal alternatives (fold / call / min-raise / pot).
- Score each with verifier sum: legality + regression match bonus + MC equity + positional VPIP guard.
- Submit argmax — profile latency on `pokerkit run --dry-run --max-hands 10`.

**Timeout risk:** Arena action deadlines — BoN only runs on marginal postflop with ≤2 alt actions (no extra MC). Default **on** with `CEMINI_TRAJECTORY_BOUND=1`; set `CEMINI_VERIFIER_BON=0` to disable.

### P2 — D_auto flywheel

- Export verified submits only (verifier accepted action) to trajectory JSONL.
- HL loop consumes verified trajectories preferentially over raw lobby noise.
- Pairs with K122 multi-axis brief — verifier enforces M₈/M₉ floor pre-submit; axis_summary post-submit.

### Out of scope

- Visual/camera verifier (robotics-specific).
- LLM-as-judge verifier at runtime (Level 5) — Researcher track fixes base LLM [CONFIRMED per PR].

## Sources

- [Source: arXiv:2606.18247 (retrieved 2026-06-18)]
- @wiki/concepts/generator-verifier-inference-time-steering.md
- @wiki/sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
- @wiki/concepts/poker-arena-multi-axis-cognitive-profile.md
