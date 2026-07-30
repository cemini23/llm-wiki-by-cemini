---
title: K226 poker steal — self-play red team vs decide()
type: brief
tags: [brief, poker, k226, steal]
created: 2026-07-30
---

## Target

dev.fun poker arena — decide() robustness

## Summary

GPT-Red lesson: attack a **population** of co-evolving defenders with inference-time search. For poker agents: red-team decide() against varied system/tool harnesses, not one fixed prompt.

## Body

1. Maintain a defender population (prompt/tool variants) for attacker self-play
2. Budget multi-turn attack search before claiming robustness
3. Feed successful attacks back into adversarial training / gates

**Status (2026-07-30):** shelf — not implemented this cycle (chip-qual priority).
Pair later with claimed-auth / play-adequacy adversarial fixtures.

## Sources

- Cybersecurity wiki: `concepts/gpt-red-self-play-red-teaming.md`
- [Source: https://arxiv.org/abs/2607.26115 (retrieved 2026-07-30)]
