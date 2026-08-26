---
title: "StarHarness — stratified harness evolution (arXiv 2608.24804, CCC K313)"
type: source
tags: [arxiv, harness, ccc, k247, k313]
keywords: [StarHarness, stratified-search, harness-evolution, ServiceNow]
related:
  - concepts/k247-agent-harness-wave.md
  - entities/tools/starharness.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.19013-harness-continual-learning-2026-08-20.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/k247-agent-harness-wave.md — K247 harness cluster
- @entities/tools/starharness.md — MIT REFERENCE clone; policy_wired K313
- @concepts/skill-misevolution.md — do not auto-evolve `.cursor/skills`
- @sources/arxiv-2608.19013-harness-continual-learning-2026-08-20.md — HCL sibling pattern

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.24804, "StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments" |
| Authors | Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav, Sai Rajeswar, et al. (ServiceNow / Mila / UdeM) |
| Retrieved | 2026-08-26 |
| File | `arxiv-2608.24804-starharness-evolving-harnesses-with-stratified-s.pdf` |
| sha256 | `a9cacb200fbbc90dd5f9fc8ac65d8235147eb719ebd7a18e1262df7ccc444505` |
| Repo | https://github.com/ServiceNow/StarHarness (MIT) |
| Dual-ID | **OSINT K247** + **CCC K313** policy_wired. Trainer runtime wont_wire. |

## Narrative

StarHarness evolves environment-specific agent harnesses with **model weights fixed**. Evolved artifacts include prompts, tool interfaces, skills, MCP providers, subagent structure, and loop config. Key discipline: stratify tasks by baseline failure mode; separate proposer-visible search tasks from proposer-hidden selection tasks; reserve held-out tasks for generalization.

Reported +20–35 pp full-benchmark gains after 4–12 accepted changes per environment on ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance. Gains transfer across GPT and Qwen without re-evolution. **Never optimize pass criteria** (pairs K162/K281/K292). `.local/adopts/StarHarness` = GO REFERENCE only.

## Snippets

> "StarHarness constructs a compact evolution pool by stratifying tasks by baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization." [Source: arxiv-2608.24804-starharness-evolving-harnesses-with-stratified-s.pdf p.1]
