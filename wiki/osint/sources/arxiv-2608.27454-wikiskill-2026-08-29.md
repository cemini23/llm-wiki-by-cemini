---
title: "WikiSkill — compiling agent experience into persistent knowledge (arXiv 2608.27454)"
type: source
tags: [arxiv, skills, ccc, k250]
keywords: [WikiSkill, skill-evolution, wiki-layer, Google-Research]
related:
  - concepts/k250-skill-evolution-wave.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
read_status: read
---

## Relations

- @concepts/k250-skill-evolution-wave.md — K250 skill cluster
- @concepts/skill-misevolution.md — HITL lifecycle gates
- @sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md — reasoning-memory sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.27454, "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution" |
| Authors | Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu (Google) |
| File | `2608.27454v1.pdf` |
| Retrieved | 2026-08-29 |
| Repo | NO public SPDX clone at Phase-0 |

## Narrative

WikiSkill co-evolves **agent skills** with a persistent **wiki** knowledge base. Three layers: Raw (immutable traces), Wiki (failure patterns, strategies, rejected proposals), Skill (executable procedures). Loop: Inference Agent → Wiki Maintainer → Skill Proposer → **gating/rollback** on validation.

Ablation: removing persistent wiki drops average performance substantially (reported 63.7% → 48.7%). Skills transfer across model families; smaller models + skills can beat larger models without. Pairs **K324 validation ratchet** and **K237 skill misevolution** — never unattended `.cursor/skills` auto-evolve.

## Snippets

> "Skill evolution complements model scaling: smaller models with skills can outperform substantially larger models without them." [Source: arxiv 2608.27454 abstract]
