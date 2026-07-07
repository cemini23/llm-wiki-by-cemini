## Target

`agents/devfun-poker-arena/` — multimodal coaching pipeline.

## Summary

K148 **Extract** — steal `bradautomates/claude-video` (MIT, ~4.8k★) pattern for hand-history / coaching video → structured heuristics for `decide()`. Untrusted transcript immunization required.

**Shipped (2026-07-07):** `scripts/coaching_video_extract.py`, `scripts/sanitize_untrusted_text.py`, `scripts/run_coaching_extract_gate.sh`, `references/coaching-video-extract.md`. Tests: `tests/test_k148_coaching_extract.py`.

## Body

Read wiki first:

- `@entities/tools/claude-video.md`
- `@sources/eval-repository-revenue-integration-2026-07-07.md`

**Scope:** Offline batch only — extract sizing/frequency patterns from public coaching clips into `STRATEGY.md` candidates. Run through `references/agent-rules.md` untrusted-data rules before any `decide()` merge.

**Pair with:** `@sources/arxiv-policy-representation-2607.01498-2026-07-07.md` for opponent embedding axis (separate track).

## Sources

- `@sources/eval-repository-revenue-integration-2026-07-07.md`
- `@entities/tools/claude-video.md`
