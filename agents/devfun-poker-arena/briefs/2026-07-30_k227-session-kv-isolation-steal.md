---
title: K227 poker steal — session memory KV isolation
type: brief
tags: [brief, poker, k227, steal]
created: 2026-07-30
---

## Target

dev.fun poker arena — session / opponent memory

## Summary

InferScale injects reusable KV for personalized memory. Steal the **isolation** requirement: never share injected memory KV across tables/sessions/users.

## Body

1. Per-session memory only — no cross-table KV bleed
2. Treat memory injection as privileged API (audit what enters decide())
3. Clear KV on session end / LIVE disconnect

## Sources

- Cybersecurity wiki: `concepts/inferscale-kv-injection-personalized-serving.md`
- [Source: https://arxiv.org/abs/2607.27090 (retrieved 2026-07-30)]

## Shipped

- `references/session-kv-isolation.md`
- Cross-link from `references/hierarchical-session-memory.md`
- `tests/test_k164_k221_k227_docs.py`
