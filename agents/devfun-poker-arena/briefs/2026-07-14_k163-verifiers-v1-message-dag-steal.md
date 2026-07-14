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

## Body

1. When writing HL/analyze traces, store messages once and reference — avoid duplicating full histories per turn.
2. Keep harness (`decide`/CLI) separate from taskset (scenarios) and runtime (Arena client).
3. Do **not** install Prime Intellect stack; Watch only.
4. Pair with K161 hierarchical memory caps.

## Sources

- @wiki/sources/newsletter-rss-latent-space-2026-07-14-ainews-codex-7m-verifiers-v1.md
