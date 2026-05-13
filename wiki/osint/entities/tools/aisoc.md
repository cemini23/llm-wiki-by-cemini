---
title: "AiSOC — LangGraph SOC orchestrator (Steal-from, Cemini-direct + cybersec)"
type: entity
tags: [tool, langgraph, soc-orchestrator, investigation-ledger, mit, steal-from, cybersec-cross-route, gemini-eval-doc2]
keywords: [aisoc, beenuar, langgraph soc, investigation ledger, neo4j, 14 log sources, ci-gated eval harness, ip-sale-ready trade auditability]
related:
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/conductor-orchestrator.md
  - concepts/ip-sale-readiness.md
  - "@cybersecurity-wiki/entities/tools/aisoc.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc2_url: 26
phase_0_verdict: STEAL-FROM 2026-05-12 (Investigation Ledger pattern for trade auditability)
---

## Relations

- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — source eval (URL 26)
- `@concepts/conductor-orchestrator.md` — Cemini orchestrator integration target
- `@concepts/ip-sale-readiness.md` — trade-audit angle
- `@cybersecurity-wiki/entities/tools/aisoc.md` — cybersec primary (SOC orchestration)

## Raw Concept

- **Repo**: `github.com/beenuar/AiSOC`
- **License**: MIT
- **Tier**: Steal-from
- **Primary fit**: Cybersec wiki + Cemini financial (audit ledger)

## Narrative

Self-hosted AI Security Operations Center with ~600-line LangGraph orchestrator, Investigation Ledger in Neo4j, 14 log sources, public CI-gated eval harness with OpenAPI specs and Terraform/Helm packaging. Cemini steal-from: port the Investigation Ledger pattern to `agents/orchestrator.py` using existing PostgreSQL instead of Neo4j for **IP-sale-ready trade auditability** (a critical audit-log requirement). Cybersec wiki gets the primary entity for SOC-orchestration angle.

### Integration vector

Phase-0: read AiSOC's `agents/orchestrator.py` equivalent + ledger schema. Map fields onto Cemini trade event types. Write a Cemini-specific brief once schema mapping is verified.
