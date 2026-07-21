---
title: K200 poker steal — trajectory context pruning
type: brief
tags: [brief, poker, k200, steal]
created: 2026-07-21
---

## Target

cemini_decide long trajectories / tool-output bloat

## Summary

SWE-Pruner Pro pattern: prune redundant tool/context lines using model-internal signals; save tokens without separate classifier. Lab-only until LICENSE file confirmed.

## Body

1. Candidate for HUD/tool dump bloat in long decide() sessions
2. Measure decide quality after prune, not only tokens

## Sources

- Cybersecurity wiki: `entities/tools/swe-pruner-pro.md`
- [Source: https://arxiv.org/abs/2607.18213 (retrieved 2026-07-21)]
