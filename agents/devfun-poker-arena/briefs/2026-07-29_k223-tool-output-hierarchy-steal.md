---
title: K223 poker steal — tool-output instruction hierarchy
type: brief
tags: [brief, poker, k223, steal]
created: 2026-07-29
updated: 2026-07-29
status: shipped
---

## Target

dev.fun poker arena — tool/HUD/MCP inputs to decide()

## Summary

S≻U strength does not imply U≻T. Tool/HUD outputs that inject conflicting instructions can hijack decide() even when system prompts hold against user pressure.

## Body

1. Treat HUD/API/tool payloads as untrusted instruction surfaces
2. Eval tool-conflict fixtures separately from user-jailbreak suites
3. Block subtle tool-injected instruction overrides (not only overt bet/size commands)

## Shipped

- `references/tool-output-instruction-hierarchy.md`
- Cross-link from `claimed-authorization-guard.md`
- HUD subtle-instruction fixture in `tests/test_claimed_authorization.py`
- `tests/test_k220_k222_k223_docs.py`

## Sources

- Cybersecurity wiki: `concepts/instruction-hierarchy-conflict-benchmark.md`
- [Source: https://arxiv.org/abs/2607.25987 (retrieved 2026-07-29)]
