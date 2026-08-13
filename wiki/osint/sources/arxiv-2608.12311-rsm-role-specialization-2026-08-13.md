---
title: "RSM — Role Specialization Model for Coordinating LLM-Based Tools"
type: source
tags: [arxiv, k235, multi-agent, role-specialization, se-30, ccc]
keywords: [2608.12311, RSM, role-specialization, LLM-tools, coordination, prompt-hardening, SE-3.0]
related:
  - concepts/role-specialization-model-rsm.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/role-specialization-model-rsm.md — synthesized pattern page
- @concepts/agent-toolkit-routing-research-backlog.md — K235 bump: RSM joins multi-agent backlog

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.12311 (2026-08-12) |
| Authors | Fernández-y-Fernández (UT Mixteca), Aguilar Cisneros (UPAEP) |
| sha256 | `098b13d34f2789315612cdb8bfe2d9916d0da727a5ebe9bcacb51c2a2468f02f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12311-the-role-specialization-model-rsm-coordinating-l.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Exploratory case study in Agentic Software Engineering (SE 3.0): the Role Specialization Model assigns traditional software-team roles (analyst, designer, programmer, reviewer) to LLM instances coordinating multiple tools. Main conclusions: **(a) role specialization is a valid design principle for multi-tool LLM coordination, but requires explicit scope boundaries** to prevent unintended overlaps between roles; **(b) prompt hardening via explicit negative constraints was critical** for agent output integrity; coordination strategies, context management, and human verification of agent-generated outputs remain required. Cites prior work that overly detailed project-rule files reduce task success rates and increase inference costs — a caution for rule-file bloat.

Routing: CCC multi-agent /route backlog (role-scope boundaries + negative-constraint hardening), not a product wire. No code artifact (paper-level study).

[Source: arXiv:2608.12311]

## Snippets

> "role specialization is a valid design principle for multi-tool LLM coordination but requires explicit scope boundaries to prevent unintended overlaps" [Source: arXiv:2608.12311 §6]
