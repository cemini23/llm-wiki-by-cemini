# Session memory KV isolation (K227)

**arXiv:** [2607.27090](https://arxiv.org/abs/2607.27090) (InferScale KV
injection — isolation pattern only)  
**Brief:** `briefs/2026-07-30_k227-session-kv-isolation-steal.md`  
**Wiki:** `@cybersecurity-wiki/concepts/inferscale-kv-injection-personalized-serving.md`

## Steal

Personalized / injected memory is a **privileged surface**. Never share injected
session “KV” (villain HUD, hierarchical mid-term, HL sequential tags) across
tables, competitions, agents, or users.

## Cemini wiring (already)

| Store | Scope | Clear on |
|-------|-------|----------|
| `session_villain_memory` | Current lobby competition | Competition board change (`_sync_competition_scope` in `run_cemini_lobby.py`) |
| Hierarchical mid-term | Same | `reset_mid_term` on competition change |
| Hierarchical long-term | Doc pointers only | Never inlined into decide |
| Sequential HL tags (K146) | Same table/session brief thread | Wipe between unrelated briefs |

## Operator rules

| Do | Do not |
|----|--------|
| Treat memory injection into `research_context` as audited privileged API | Reuse villain HUD / mid-term across competitions or agent IDs |
| Clear session stores on LIVE disconnect / lobby stop | Persist injected memory into sandbox zip as shared state |
| Keep decide slice O(1) (`build_memory_slice_for_decide`) | Dump full transcripts as “KV” |

## Related

- `references/hierarchical-session-memory.md` (K161 / K146)
- `references/sandbox-live-containment.md` (K222)
- `references/tool-output-instruction-hierarchy.md` (K223)
- Code: `examples/session_memory.py`, `examples/hierarchical_session_state.py`
