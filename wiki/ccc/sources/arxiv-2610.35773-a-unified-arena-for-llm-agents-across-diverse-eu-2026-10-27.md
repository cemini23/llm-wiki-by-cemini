---
title: "DECE: A Unified Arena for LLM Agents across Eurogames"
type: source
tags: [source, arxiv, agent-evaluation, game-benchmark]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Unified Arena for LLM Agents across Diverse Eurogames |
| Authors | Fengrui Zhang, Xiang Li, Ruomeng Ding, Jiayi Yuan, Yuchen Huang, Zhaoyang Han, Xiaoliang Wang, Daoyuan Chen, Yaliang Li (Alibaba Group; Nanjing University; NUS; UNC; HKUST; Peking University) |
| arXiv | 2610.35773 |
| File | `arxiv-2610.35773-a-unified-arena-for-llm-agents-across-diverse-eu.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35773 |
| Read status | skimmed (abstract + intro) |

## Narrative

**DECE** (Diverse Eurogame Competitive Environments) is an arena of ten Eurogames under shared interfaces and evaluation protocols. The games share three properties: lasting strategic commitments, competition over shared resources, and multiple routes to victory.

Study scale: 12 model–harness configurations spanning nine models and four execution harnesses, in 480 three-player matches across ten games. Main and supplementary studies total 1,032 completed matches.

Findings:

- Cross-game ranking agreement is broad, with game-specific strengths on top.
- **The same model performs differently across execution harnesses.** This adds a source of variance that a model-only leaderboard hides.
- Performance advantages do not translate consistently into better token or cost efficiency.

**Why it matters.** This is a second independent confirmation, in this same wave, that the harness is part of the measured system. It also repeats the efficiency warning from the model-or-harness paper: a higher win rate does not imply lower cost.

## Snippets

> "Matched studies show that the same model can perform differently across execution harnesses, adding another source of variation to these profiles." [Source: `arxiv-2610.35773-a-unified-arena-for-llm-agents-across-diverse-eu.pdf` p.1 (arXiv 2610.35773), retrieved 2026-10-27]
