---
title: K161 — hierarchical memory + DeepSearch trajectory filter (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-13
updated: 2026-07-13
---

## Target

`agents/devfun-poker-arena/` — Researcher Round HU sandbox / HL analyst loop.

## Summary

Two steals: (1) **Ensemble QSP hierarchical memory** (2607.07666) — capped mid-term project-state + eviction so session context stays ~O(1) tokens; (2) **DeepSearch-Evolve** (2607.07820) — generate→filter→mix trajectories in a verifiable env without teacher distillation.

**Shipped (2026-07-13):** hierarchical session state + DeepSearch filter advisory; lobby injects bounded slice; gate echo. Advisory only — no hard submit gate. DeepSearch env remains Watch (loop shape only).

## Body

### P0 — hierarchical session memory

- Keep **short-term**: last N hands + scratchpad facts (stack, HUD tags).
- Keep **mid-term**: capped session JSON (active goals, last 3 session summaries, recent jobs) — **evict** completed drills.
- Keep **long-term**: strategy handbook / yardstick docs (already in `references/`).
- **Do not** dump full Arena trajectories into `decide()` or HL prompts.

### P1 — trajectory filter/mix (DeepSearch analogy)

- When mining sandbox failures: require **progress verification + grounded reflection + failure recovery** tags before mixing into training/eval sets.
- Drop ungrounded reflection / teacher-imitation-only traces.
- DeepSearch code release is **Watch** — steal the loop shape only until env lands.

### Out of scope

- Quantile DRL theory (2607.08444) — shelf
- Psychological competence (coach UX) — TipDrop/David lane

### Operator checklist

- [x] Short-term last N hands + scratchpad facts
- [x] Mid-term capped session JSON + eviction
- [x] Long-term via references/ pointers only
- [x] No full trajectories in decide()/HL prompts
- [x] DeepSearch generate→filter→mix advisory
- [x] Required tags before mix; drop teacher-imitation / ungrounded

## Shipped

| Artifact | Notes |
|----------|-------|
| `config/hu_hierarchical_memory.json` | Caps + eviction knobs |
| `config/hu_deepsearch_trajectory_filter.json` | Required tags + drop rules |
| `examples/hierarchical_session_state.py` | Bounded state + decide slice |
| `examples/run_cemini_lobby.py` | Inject `hierarchical_memory_slice` |
| `examples/researcher_trajectory_summary.py` | DeepSearch filter advisory |
| `references/hierarchical-session-memory.md` | Operator spec |
| `references/deepsearch-trajectory-filter.md` | Filter loop spec |
| `tests/test_k161_hierarchical_memory.py` | Ring/evict/budget |
| `tests/test_k161_deepsearch_trajectory_filter.py` | Tag filter |

```bash
uv run pytest tests/test_k161_hierarchical_memory.py tests/test_k161_deepsearch_trajectory_filter.py -q
```

## Sources

- `references/hierarchical-session-memory.md`
- `references/deepsearch-trajectory-filter.md`
- arXiv [2607.07666](https://arxiv.org/abs/2607.07666) / [2607.07820](https://arxiv.org/abs/2607.07820)
