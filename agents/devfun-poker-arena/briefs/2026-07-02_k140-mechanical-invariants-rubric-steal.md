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

## Sources

- @wiki/concepts/ai-native-games-taxonomy.md
- @wiki/concepts/poker-arena-multi-axis-cognitive-profile.md
