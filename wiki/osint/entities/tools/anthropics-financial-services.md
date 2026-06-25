---
title: "Anthropic Financial Services — Enterprise MCP Blueprint for Finance"
type: entity
tags: [tool, financial-services, mcp, anthropic, prompt-engineering, reference-architecture]
keywords: [Anthropic, financial services, MCP connectors, prompt schemas, FactSet, S&P Global, LSEG, Apache-2.0]
related:
  - sources/project-link-evaluation-brief.md
  - sources/eval-url-cemini-research-2026-06-25.md
  - concepts/tool-evaluation-framework.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-05-10
updated: 2026-06-25
---

## Relations
- `@sources/project-link-evaluation-brief.md` — source evaluation brief (URL 4)
- `@sources/eval-url-cemini-research-2026-06-25.md` — K129 Adopt reconfirm (Apache-2.0)

## Raw Concept

Anthropic's enterprise-grade reference architecture for financial services: reference agents, system prompts, and MCP data connectors tailored for banks, asset managers, and quantitative research teams.

- **Repo**: `github.com/anthropics/financial-services`
- **License**: Apache-2.0
- **Stack**: Python scripts, YAML schemas, JSON configurations
- **Footprint**: <100 MB disk, ~50-100 MB runtime RAM per MCP tool

## Narrative

This repository provides production-grade blueprints for financial reasoning agents, including MCP connectors for FactSet, S&P Global, LSEG, and other institutional data providers. It includes structured system prompts for financial data normalization, compliance auditing, and earnings report parsing.

### Integration vectors

- **Cemini prod (Steal-from)**: Extract financial reasoning schemas and API connector patterns into the ~130 `@mcp.tool` decorators on the Cemini server. The programmatic logic for parsing complex earnings reports, normalizing financial data across providers, and enforcing compliance audit trails is directly portable.
- **Workflow (Steal-from)**: Save the sophisticated analytical prompt structures as persistent system instructions within the Obsidian vault to guide Claude Code in extracting superior insights from quantitative financial research papers.

### Risks

- **Vendor lock-in**: Documentation is heavily biased toward Anthropic ecosystem (Claude Cowork, Claude Code, Claude Managed Agents). Adapting templates for DeepSeek chat-completions requires prompt translation work.
- **Credential security**: MCP connectors for FactSet, S&P Global, LSEG require secure handling and rotation of sensitive vendor API credentials.

### Open questions

- Explicit dependency list in `requirements.txt` to confirm absence of transitive AGPL/SSPL libraries `[NEEDS VERIFICATION 2026-06-25]`

[Source: Project Link Evaluation Brief.docx, URL 4]
