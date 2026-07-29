---
title: K220 poker steal — eval claim evidential ceiling
type: brief
tags: [brief, poker, k220, steal]
created: 2026-07-29
updated: 2026-07-29
status: shipped
---

## Target

dev.fun poker arena — researcher LB / TrueSkill claims

## Summary

Steal evidential-ceiling: a clean sheet on a small eval does not certify rare failure modes. State what your sandbox LB result actually licenses.

## Body

1. Before claiming strategy dominance from N sessions, state the harm/failure rate the sample can certify
2. One reproduced catastrophic failure can outweigh a clean modest board below the crossing rate
3. Prefer discrimination metrics (did we separate hypotheses?) over raw win-rate for gates

## Shipped

- `references/eval-claim-ceiling.md`
- Linked from `league-promotion-rubric.md`, `play-adequacy-gates.md`, `cognitive-security-deploy.md`
- `tests/test_k220_k222_k223_docs.py`

## Sources

- Cybersecurity wiki: `concepts/ai-redteam-evidential-ceiling.md`
- [Source: https://arxiv.org/abs/2607.21735 (retrieved 2026-07-29)]
