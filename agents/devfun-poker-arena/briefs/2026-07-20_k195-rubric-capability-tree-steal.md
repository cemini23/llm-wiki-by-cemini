---
title: K195 poker steal — rubric capability-tree diagnosis
type: brief
tags: [brief, poker, k195, steal, rubric]
created: 2026-07-20
---

## Target

cemini_decide / Researcher Round eval rubrics (dev.fun poker arena)

## Summary

When decide() / nine-axis eval fails, cluster **rubric criteria** (not whole spots) into a capability tree and fix the weakest clear nodes before rewriting prompts or collecting SFT trajectories. Pattern from Scale AI CRAFT (arXiv 2607.16122); no public code — steal method only.

## Body

1. Prefer criterion-level diagnosis over category averages ("weak on river")
2. Do not mix diagnostic rubric spots into held-out TrueSkill benches
3. After generating new training trajectories, risk-filter before SFT (DataShield / equivalent)

## Sources

- Cybersecurity wiki: `concepts/rubric-capability-tree-diagnosis.md` (arXiv 2607.16122 CRAFT)
- Prod: `cemini-prod:/opt/cemini/briefs/2026-07-20_k195-craft-capability-diagnosis-prod.md`
- [Source: https://arxiv.org/abs/2607.16122 (retrieved 2026-07-20)]
