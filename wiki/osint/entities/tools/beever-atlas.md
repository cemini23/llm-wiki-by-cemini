---
title: "Beever Atlas — LLM-first Wiki Knowledge Base"
type: entity
tags: [tool, wiki-architecture, semantic-store, rag, k37]
keywords: [beever, atlas, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 15)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/Beever-AI/beever-atlas`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License not stated; only architectural patterns to lift, no code — license-clean per Cemini IP-sale policy.

## Narrative

Enterprise-scale LLM-first Wiki KB architecture. Monitors corporate chat platforms (Slack/Discord/Teams) and distills unstructured conversation into a 3-tier semantic store: channel layer → topic layer → atomic fact layer. Decouples raw ingestion from query-time retrieval via intermediate structured distillation.

### Integration vector

Steal-from: lift the **3-tier semantic store** design and **decoupled ingestion → distillation → retrieval** pipeline into Cemini's `llm-wiki-compiler` MCP server. Do NOT deploy — distributed infra is prohibitively heavy for Hetzner CPX21 (4 GB envelope vs Beever's bloated stack).

### Risks

Beever's full deployment requires distributed infrastructure unsuited for the 4 GB librarian envelope. Workflow integration limited to schema studying.

[Source: Evaluating Urls System Integration.docx, URL 15]
