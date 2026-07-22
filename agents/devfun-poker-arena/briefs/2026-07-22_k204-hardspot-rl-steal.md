---
title: K204 poker steal — privileged guidance for hard spots
type: brief
tags: [brief, poker, k204, steal]
created: 2026-07-22
---

## Target

cemini_decide hard-spot SFT / RL

## Summary

OC-GRPO pattern: when zero correct rollouts, use privileged train-time guidance then importance-correct back to the real objective. Lab only.

## Body

1. Candidate for spots where policy never samples a win
2. Keep privileged hints out of live decide() prompts

## Sources

- Cybersecurity wiki: `entities/tools/oc-grpo.md`
- [Source: https://arxiv.org/abs/2607.19313 (retrieved 2026-07-22)]
