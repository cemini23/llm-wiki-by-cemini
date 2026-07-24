---
title: K216 poker steal — public checks miss hidden failure modes
type: brief
tags: [brief, poker, k216, steal]
created: 2026-07-24
---

## Target

dev.fun poker arena — solver/unit-check gates before LIVE

## Summary

Steal CodeMonitor lesson: passing visible/public tests still leaves most hidden failures. Weak second-pass verifiers miss them at low FPR. Treat public smoke tests as necessary-but-insufficient before LIVE.

## Body

1. Keep hidden/oracle evals (solver EV checks) separate from public smoke
2. Do not let a weak reviewer override a failed hidden check
3. Stress generators that overfit the public harness

## Sources

- Cybersecurity wiki: `concepts/code-monitor-red-teaming-public-tests.md`
- [Source: https://arxiv.org/abs/2607.20852 (retrieved 2026-07-24)]
