---
title: Role Specialization Model (RSM) for Multi-Tool LLM Coordination
type: concept
tags: [concept, multi-agent, role-specialization, se-30, ccc, k235]
keywords: [RSM, roles, scope-boundaries, negative-constraints, prompt-hardening]
related:
  - sources/arxiv-2608.12311-rsm-role-specialization-2026-08-13.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - sources/x-clayul-ivan-nardini-claude-gcp-2026-08-13.md
  - concepts/persona-hat-claude-code-sdlc.md
maturity: draft
created: 2026-08-13
updated: 2026-08-15
---

## Relations

- @sources/arxiv-2608.12311-rsm-role-specialization-2026-08-13.md
- @concepts/agent-toolkit-routing-research-backlog.md — K235 backlog bump
- @sources/x-clayul-ivan-nardini-claude-gcp-2026-08-13.md — K238 live five-hat Claude Code demo
- @concepts/persona-hat-claude-code-sdlc.md — demo hats without RSM scope lock (security also deploys)

## Raw Concept

What this page answers: does assigning traditional software-team roles (analyst, designer, programmer, reviewer) to LLM instances improve multi-tool coordination, and where does it break? Synthesized from 2608.12311.

## Narrative

RSM is an exploratory case study in SE 3.0: role-specialized LLM instances coordinate over multiple tools. Findings, in order of transferability:

1. **Role specialization is a valid design principle — with explicit scope boundaries.** Unintended role overlap is the failure mode; roles without hard scope boundaries drift into each other's work.
2. **Prompt hardening via explicit negative constraints was critical for output integrity** — telling the agent what *not* to do mattered more than elaborating what to do.
3. **Human verification of agent-generated outputs remains required** — roles improve organization and architectural quality, not correctness guarantees.
4. **Rule-file bloat is counterproductive** (cited prior work): overly detailed project-rule files *reduce* task success rates and *increase* inference costs — a caution for this workspace's growing `.cursor/rules` surface.

Maps directly onto the CCC /route multi-agent backlog: role-scope boundaries + negative-constraint hardening as prompt-level counterparts to the policy-wire pattern this workspace already uses at the harness level.

**K238 live check:** Nardini's five-hat Claude Code demo (@concepts/persona-hat-claude-code-sdlc.md) is RSM-shaped (PM / UX / SWE / security / data) but **fails the scope-boundary test** — the security hat both reviews and deploys. Treat as a positive example of role *labels* and a negative example of role *locks*.

## Snippets

> "role specialization is a valid design principle for multi-tool LLM coordination but requires explicit scope boundaries to prevent unintended overlaps" [Source: arXiv:2608.12311 §6]
