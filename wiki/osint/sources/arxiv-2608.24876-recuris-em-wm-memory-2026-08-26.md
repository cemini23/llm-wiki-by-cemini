---
title: "Recuris — EM/WM recursive memory for long-horizon harnesses (arXiv 2608.24876, CCC K314)"
type: source
tags: [arxiv, memory, harness, ccc, k247, k314]
keywords: [Recuris, experiential-memory, working-memory, skill-selection, Gen-Verse]
related:
  - concepts/k247-agent-harness-wave.md
  - entities/tools/recuris.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.21230-agent-memory-poisoning.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/k247-agent-harness-wave.md — K247 harness cluster with StarHarness
- @entities/tools/recuris.md — Apache-2.0 REFERENCE; policy_wired K314
- @concepts/skill-misevolution.md — HITL before skill self-write
- @sources/arxiv-2608.21230-agent-memory-poisoning.md — memory poisoning limits (K304)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.24876, "Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses" |
| Authors | Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang |
| Retrieved | 2026-08-26 |
| File | `arxiv-2608.24876-recursive-experiential-working-memory-evolution.pdf` |
| sha256 | `dfa6f6d1174ad07dee26e5e3d310b750280fe3eaba16b371ef1e0d80bce8ae41` |
| Repo | https://github.com/Gen-Verse/Recuris (Apache-2.0) |
| Dual-ID | **OSINT K247** + **CCC K314** policy_wired. Runtime wont_wire. |

## Narrative

Long-horizon RSI fails when growing histories obscure task state and misalign skill invocation. Recuris couples **Working Memory** (live task state, skill selection) with **Experiential Memory** (skill bank) — grounding skill use in current needs rather than full history. Execution traces localize failures to specific memory components; a Meta-Agent applies **validation-gated** patches in a bounded loop.

Reported improvements in 35/37 completed model–benchmark pairs; τ²-Bench +17.8 pp claim for GPT-5.6 Sol. **HITL before any skill self-write** (pairs K237/K307/K309). `.local/adopts/Recuris` = GO REFERENCE only.

## Snippets

> "Working Memory tracks task progress and guides skill selection from Experiential Memory — grounding skill use in current needs instead of full history." [Source: arxiv-2608.24876-recursive-experiential-working-memory-evolution.pdf p.1]
