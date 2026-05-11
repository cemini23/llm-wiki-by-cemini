---
title: "Agent Security Bench (ASB) — ICLR 2025"
type: entity
tags: [tool, agent-security, academic, iclr-2025, threat-model, k37]
keywords: [asb, agent, security, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 14)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/agiresearch/ASB`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] ICLR 2025 academic codebase — likely MIT/Apache; verify LICENSE.

## Narrative

Academic evaluation framework formalizing adversarial vulnerabilities in LLM-based agents. Codebase for an ICLR 2025 paper. 10 high-stakes operational scenarios incl. financial investment. Covers memory_defense + Plan-of-Thought Backdoors.

### Integration vector

Steal-from: audit theoretical attack models (memory_defense + Plan-of-Thought Backdoors) and map them onto Cemini's LangGraph orchestrator. Do NOT deploy — academic harness coupled to AIOS abstractions.

### Risks

Tight structural coupling to AIOS — porting tests to LangGraph requires extensive refactoring. Academic-research code rot risk.

[Source: Evaluating Urls System Integration.docx, URL 14]
