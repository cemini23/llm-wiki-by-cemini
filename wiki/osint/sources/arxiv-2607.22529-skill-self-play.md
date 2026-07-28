---
title: "Skill Self-Play — co-evolving LLM skills (arXiv 2607.22529)"
type: source
tags: [source, arxiv, agent-skills, self-play, k196, ccc]
keywords: [skill self-play, co-evolving skills, verification, open-ended tasks]
related:
  - concepts/skill-regression-tax.md
  - concepts/code-as-agent-harness.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/arxiv-2607.22520-regression-tax-llm-skills.md
maturity: draft
read_status: skimmed
created: 2026-07-27
updated: 2026-07-27
clusters: [k196-ingest]
---

## Relations

- @concepts/skill-regression-tax.md
- @concepts/code-as-agent-harness.md
- @concepts/continual-harness-online-self-improvement.md
- @sources/arxiv-2607.22520-regression-tax-llm-skills.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.22529-skill-self-play-pushing-the-frontier-of-llm-capa.pdf` |
| **sha256** | `59ceb22a7620b98326f6a2430e1ab303e5b589eaf6d765463cd4c51bd69477cd` |
| **arXiv** | [2607.22529](https://arxiv.org/abs/2607.22529) |
| **Repo** | https://github.com/Qwen-Applications/skill-self-play |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.22529-skill-self-play-pushing-the-frontier-of-llm-capa.pdf` |

## Narrative

Self-evolution dilemma: env-bound methods verify well but narrow; open-ended generation diversifies but pollutes rewards. **Skills** as middle ground — deep verifiable execution per scenario + dynamic routing for variety. Skill Self-Play co-evolves skills to push capability frontier.

**Steal:** pair with Regression Tax — co-evolve only behind regression gates; no unsupervised skill farm into Atto/CCC allowlists.

## Snippets

> "agent skills as a powerful middle ground … each skill ensures deep, verifiable execution … while dynamic routing across skills maintains open-ended task variety"
