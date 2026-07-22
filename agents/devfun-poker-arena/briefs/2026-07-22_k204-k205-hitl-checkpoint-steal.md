---
title: K204/K205 poker steal — HITL checkpoint + deploy verification
type: brief
tags: [brief, poker, k204, k205, steal]
created: 2026-07-22
---

## Target

dev.fun poker arena — high-risk money decisions and LIVE deploy gates

## Summary

Steal CCC HITL / Wild-deploy recipe: interrupt+checkpoint before acting on money decisions; repair loops on tool failure (no invented EV); verification pipeline + fallback before LIVE tables; evidence-gate strategy writeups that claim tool-backed analysis.

## Body

1. High-risk / money decisions: interrupt + checkpoint before acting; resume after review
2. Repair loops on tool failure (solver/API) — do not invent EV
3. Deployment checklist: verification pipeline + fallback before LIVE tables
4. Evidence-gate strategy writeups that claim tool-backed analysis

## Sources

- CCC ingest 2607.19297 / 2607.19336 (HITL checkpoint + agents-in-the-wild deploy)
- [Source: https://arxiv.org/abs/2607.19297 (retrieved 2026-07-22)]
- [Source: https://arxiv.org/abs/2607.19336 (retrieved 2026-07-22)]
