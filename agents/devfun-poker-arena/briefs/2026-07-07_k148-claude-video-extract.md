## Target

`agents/devfun-poker-arena/` — multimodal coaching pipeline.

## Summary

K148 **Extract** — steal `bradautomates/claude-video` (MIT, ~4.8k★) pattern for hand-history / coaching video → structured heuristics for `decide()`. Untrusted transcript immunization required.

## Body

Read wiki first:

- `@entities/tools/claude-video.md`
- `@sources/eval-repository-revenue-integration-2026-07-07.md`

**Scope:** Offline batch only — extract sizing/frequency patterns from public coaching clips into `STRATEGY.md` candidates. Run through `references/agent-rules.md` untrusted-data rules before any `decide()` merge.

**Pair with:** `@sources/arxiv-policy-representation-2607.01498-2026-07-07.md` for opponent embedding axis (separate track).

## Sources

- `@sources/eval-repository-revenue-integration-2026-07-07.md`
- `@entities/tools/claude-video.md`
