---
title: "Medusa — AI-First Security Scanner (Pantheon Security)"
type: entity
tags: [tool, security-scanner, agpl-3.0, reject, k38]
keywords: [medusa, pantheon, reject, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 8)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/Pantheon-Security/medusa`
- **Tier (per source brief)**: **Reject**
- **License**: **AGPL-3.0** — Cemini hard reject

## Narrative

Python AI-first security scanning engine. 9,600+ explicit detection patterns for ML models, agents, RAG, MCP servers. Meta-orchestrator coordinating 79 backend scanners (Bandit, PHPStan, Clippy, etc).

### Integration vector

**Reject** — **AGPL-3.0** is hard veto per Cemini license clean-list. Beyond deployment, even local workflow use risks IP contamination (AGPL pattern absorption).

### Risks

AGPL-3.0 infection risk; M&A-bound institutional architecture mandates total isolation from AGPL source.

[Source: Link Evaluation Brief Trading Stack.docx, URL 8]
