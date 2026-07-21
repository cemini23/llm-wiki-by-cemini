---
title: K197 poker steal — defender-utility eval ranking
type: brief
tags: [brief, poker, k197, steal]
created: 2026-07-21
---

## Target

dev.fun poker arena — eval / rubric data selection

## Summary

Steal A-MESS idea: rank training/red-team spots by **downstream utility**, not raw fail rate (ASR analogue). Prefer compact high-utility subsets under budget.

## Body

1. Do not expand SFT on highest-fail spots alone
2. Attribute marginal utility (Shapley-style) when choosing which leaks to train

## Sources

- Cybersecurity wiki: `concepts/defender-centric-jailbreak-utility.md`
- [Source: https://arxiv.org/abs/2607.17152 (retrieved 2026-07-21)]
