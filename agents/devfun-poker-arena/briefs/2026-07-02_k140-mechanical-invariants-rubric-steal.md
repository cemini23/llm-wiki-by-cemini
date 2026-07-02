## Target

`agents/devfun-poker-arena/` — Researcher Round nine-axis eval rubric.

## Summary

Steal K140 **AI-native mechanical invariants** (2607.00527): goals · rules · state · feedback · pacing · agency — apply as **harness checklist** so open-ended `decide()` outputs stay scored against fixed sandbox invariants (not prose quality alone).

## Body

### P0 — rubric crosswalk

| Invariant (survey) | Arena analog |
|--------------------|--------------|
| Goals | Stack preservation / exploit objective |
| Rules | PokerKit legality + action enum |
| State | Observable cards, pot, stacks |
| Feedback | Axis scores + exploitability proxies |
| Pacing | Hand/time limits in sandbox |
| Agency | Legal action set only |

Document in researcher-guide.md § eval invariants.

### P1 — verifier gate

1. Reject `decide()` outputs that parse but violate state transition invariants before axis scoring.
2. Log invariant violations separately from strategic quality.

### Out of scope

- Building AI-native NLHE (Arena is not LLM-native core loop)

## Shipped (2026-07-02)

| Item | Artifact |
|------|----------|
| **P0 — doc / crosswalk** | `examples/sandbox_mechanical_invariants.py` — goals · rules · state · feedback · pacing (deferred) · agency; invariant hazard vocabulary |
| **P1 — verifier gate** | `verify_mechanical_invariants()` called in `sandbox_tri_verifier.score_action()` before Fara axis scoring; violations logged as `invariant:*` hazards (separate from strategic quality) |
| **Runner** | `scripts/run_sandbox_tri_verifier.sh` — optional `test_sandbox_mechanical_invariants.py` when present |

**Live sandbox:** pin `activeSubmissionId` `0175ce41-8b0a-4df6-b794-dbb6c7413022` (`replace:false`).

**Deferred:** `skills/sandbox/researcher-guide.md` § eval invariants prose (module doc is canonical for now).

## Sources

- @wiki/concepts/ai-native-games-taxonomy.md
- @wiki/concepts/poker-arena-multi-axis-cognitive-profile.md
