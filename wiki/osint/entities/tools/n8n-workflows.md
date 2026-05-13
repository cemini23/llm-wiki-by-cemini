---
title: n8n-workflows — 4,343 automation scripts + AI-BOM scanner (Adopt-tier)
type: entity
tags: [tool, automation, n8n, workflow, ai-bom-scanner, trusera, adopt-tier, cybersec-cross-route, osint-cross-route, seo-cross-route, mit]
keywords: [n8n-workflows, n8n, workflow automation, AI-BOM, MCP detection, hardcoded keys, LinkedIn scraping, FastAPI, SQLite FTS5]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/mcp-tool-marketplace.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — origin source (Doc 2, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/mcp-tool-marketplace.md` — AI-BOM scanner detects MCP client exposure

## Raw Concept

- **URL**: `https://github.com/Zie619/n8n-workflows` + docs site `https://zie619.github.io/n8n-workflows/`
- **License**: MIT
- **Stars**: 4,343 workflows / star metrics in eval
- **Tier**: Adopt
- **Primary fit**: Workflow

## Narrative

Massive automation library. Notable for inclusion of Trusera's **AI-BOM scanner** detecting:
- Hardcoded API keys in JSON payloads
- MCP client exposure
- Unauthenticated webhooks
- RCE risk via Code Execution + HTTP Request node chaining

### Cross-routing

- **Cybersec-wiki**: AI-BOM scanner methodology for LangGraph mesh auditing
- **OSINT-wiki**: 66-node LinkedIn scraping + threat-actor profiling workflow
- **SEO-wiki**: CRM + marketing automation nodes
- **Workflow**: FastAPI backend + SQLite FTS5 search infrastructure

### Phase-0 audit (PENDING)

Verify AI-BOM heuristic accuracy against Cemini's custom MCP clients (LangGraph instances).

[NEEDS VERIFICATION 2026-05-13]

[Source: Multi-Wiki Link Evaluation Prompt.docx URLs 7-8 (retrieved 2026-05-13)]
