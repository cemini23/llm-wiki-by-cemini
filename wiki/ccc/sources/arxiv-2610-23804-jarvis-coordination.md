---
title: "Jarvis — a separate model for agent coordination"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models
Authors: Yuxiang Wang and colleagues (CUHK Shenzhen; Tencent Hunyuan; Amphion)
Type: arXiv preprint (2610.23804)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.23804-jarvis-coordination-deserves-a-brain-of-its-own.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract and figure)

## Narrative

Interactive models hand slow reasoning to a back model and leave a front model on the live turn. The user can change the request while the back model is still working, and the scene can change while nobody speaks. Jarvis is a third model whose only job is that handoff.

With the front model and the back end held fixed, replacing Qwen Audio Agent with Jarvis raises τ-Voice task success from **29 to 192 of 278** tasks. The gain holds on every benchmark and front model in the paper. Jarvis-Audio reaches **69%** Pass@1 on Full-Duplex-Bench v3 with an open 9B front model, versus **60%** for GPT-Realtime. On a controller deadline of 3.5 seconds, JEV is correct **94.4%** of the time, versus **80.7%** for DeepSeek-V4-Flash on the same options.

The lesson is architectural. Coordination is not free residual capacity in the front model or the back model. **No `/route` swap. No install.**

## Snippets

> "These results suggest that how the two brains are coordinated matters as much as how strong they are." [Source: arxiv-2610.23804 abstract]
