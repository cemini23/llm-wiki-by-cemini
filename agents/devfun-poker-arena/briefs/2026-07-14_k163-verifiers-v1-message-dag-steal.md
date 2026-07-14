---
title: K163 — Prime Intellect verifiers v1 message-DAG steal (poker)
type: brief
target: Poker Arena
created: 2026-07-14
updated: 2026-07-14
---

## Target

`agents/devfun-poker-arena/` — HL loop / sandbox trajectory logging.

## Summary

Latent Space AINews: verifiers v1 stores rollouts as **message DAGs** (O(n) vs O(n²) full-history copies) and splits env into taskset/harness/runtime. Steal the logging shape for Arena failure traces — not the RL trainer.

**Shipped (2026-07-14):** `MessageDag` store + HL brief sibling `.dag.json`; taskset/harness/runtime layer tags; paired with K161 long-term refs. Watch only — no Prime Intellect install.

## Body

1. When writing HL/analyze traces, store messages once and reference — avoid duplicating full histories per turn.
2. Keep harness (`decide`/CLI) separate from taskset (scenarios) and runtime (Arena client).
3. Do **not** install Prime Intellect stack; Watch only.
4. Pair with K161 hierarchical memory caps.

## Shipped

| Artifact | Notes |
|----------|-------|
| `examples/message_dag_trace.py` | DAG store + `build_hl_failure_dag` |
| `examples/cemini_hl_brief.py` | Writes `*.dag.json` beside brief |
| `references/message-dag-trace.md` | Operator spec + env split |
| `config/hu_hierarchical_memory.json` | long_term_refs += message-dag + GenomeDiff |
| `tests/test_k163_message_dag.py` | Dedupe + roundtrip + size compare |

```bash
uv run pytest tests/test_k163_message_dag.py -q
```

## Sources

- @wiki/sources/newsletter-rss-latent-space-2026-07-14-ainews-codex-7m-verifiers-v1.md
- `references/hierarchical-session-memory.md` (K161)
