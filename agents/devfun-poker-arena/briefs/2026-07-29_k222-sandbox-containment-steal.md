---
title: K222 poker steal — capability sandbox containment
type: brief
tags: [brief, poker, k222, steal]
created: 2026-07-29
updated: 2026-07-29
status: shipped
---

## Target

dev.fun poker arena — LIVE / sandbox boundary

## Summary

Cyber-capable agents need containment of the eval environment itself. For poker: treat LIVE credentials, package/proxy paths, and sandbox objectives as one security system.

## Body

1. Isolate LIVE keys from researcher-sandbox agents
2. Do not let eval objectives conflict with sandbox boundaries (no silent LIVE escalate)
3. Content–code separation for any tool that can fetch untrusted table/state data

## Shipped

- `references/sandbox-live-containment.md`
- Pointer from `references/network-policy.md`
- `tests/test_k220_k222_k223_docs.py`

## Sources

- Cybersecurity wiki: `concepts/cyber-capable-agent-evaluation-containment.md`
- [Source: https://arxiv.org/abs/2607.25379 (retrieved 2026-07-29)]
