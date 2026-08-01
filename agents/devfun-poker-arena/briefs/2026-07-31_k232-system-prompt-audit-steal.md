---
title: K232 poker steal — system-prompt AISPA audit
type: brief
tags: [brief, poker, k232, steal]
created: 2026-07-31
---

## Target

dev.fun poker arena — decide() system prompts

## Summary

Audit decide() system prompts span-by-span for protective vs problematic instructions (AISPA pattern).

## Body

1. Inventory every instruction in decide() system prompts
2. Flag problematic spans (manipulation, hidden objectives, user-hostile rules)
3. Track protective-instruction density as a release gate

## Phase-1

Inventory filed: `references/aispa-decide-prompt-audit.md` — primary decide has no LLM system prompt; AISPA gate applies when hybrid LLM path is added.

## Sources

- Cybersecurity wiki: `concepts/aispa-system-prompt-assurance-audit.md`
- [Source: https://arxiv.org/abs/2607.28617 (retrieved 2026-07-31)]
