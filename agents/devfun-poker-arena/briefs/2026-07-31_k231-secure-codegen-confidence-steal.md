---
title: K231 poker steal — confidence-gate security advisors
type: brief
tags: [brief, poker, k231, steal]
created: 2026-07-31
---

## Target

dev.fun poker arena — any security/code advisor beside decide()

## Summary

CoGate lesson: do not let an unconfident security expert override the primary policy. Gate advisor influence on confidence.

## Body

1. If a side-model scores action safety, require a confidence threshold before veto/steer
2. Low confidence → log and pass through, do not force "secure" override
3. Eval advisor on OOD spots, not only familiar hand patterns

## Phase-1

Wired as ops reference: `references/cogate-advisor-confidence-gate.md` (no live advisor yet).

## Sources

- Cybersecurity wiki: `concepts/cogate-confidence-gated-secure-code.md`
- [Source: https://arxiv.org/abs/2607.28529 (retrieved 2026-07-31)]
