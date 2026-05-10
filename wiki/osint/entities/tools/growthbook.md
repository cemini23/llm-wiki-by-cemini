---
title: "GrowthBook — Feature Flag MCP Methodology"
type: entity
tags: [tool, feature-flags, mcp, ab-testing, llm-orchestration, open-core]
keywords: [GrowthBook, feature flags, A/B testing, MCP server, Bayesian statistics, LLM orchestration, MIT open-core]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - entities/tools/flagsmith.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 9)
- `@entities/tools/flagsmith.md` — alternative feature flag platform (Defer tier, license gated)

## Raw Concept

GrowthBook is an open-core feature flagging and A/B testing platform with an MCP server for programmatic flag control. Warehouse-native architecture (connects to existing data warehouse, doesn't ingest events directly).

- **Repo**: `github.com/growthbook/growthbook`
- **License**: MIT (Open Core), with proprietary GrowthBook Enterprise License on specific directories
- **Stack**: TypeScript 96.1%, Node.js 20.x, MongoDB
- **Maturity**: 7.7k stars, v4.3.0 (Feb 2026)

## Narrative

GrowthBook exposes an MCP server for feature flag management, theoretically allowing LLM orchestrators to dynamically toggle trading subroutines based on market conditions. Its warehouse-native architecture (querying existing data rather than ingesting events) makes it lighter than PostHog-class analytics platforms.

### Integration vectors

- **Cemini prod (Steal-from)**: Study the MCP server's TypeScript implementation for exposing feature flag controls as callable tools. The methodology — integrating A/B testing boundaries into LLM orchestration — is valuable. But the core GrowthBook application and its MongoDB dependency must be rejected from deployment.
- **Workflow (Adopt)**: Claude Code studies the MCP server locally to abstract feature-flag JSON configurations into Python algorithms before pushing to production.

### Risks

- **Open-core licensing**: MIT core is safe, but enterprise directories contain proprietary code. Inadvertently committing or using code from restricted directories could introduce license claims.
- **MongoDB dependency**: Adds operational complexity vs PostgreSQL-native alternatives. Must determine if MCP server can function statelessly against a local JSON file, bypassing MongoDB entirely.

### Open questions

- Can the GrowthBook MCP server component be decoupled from the main application and run statelessly against a local JSON file, bypassing MongoDB? `[NEEDS VERIFICATION 2026-05-10]`

[Source: Project Link Evaluation Brief 5_10.docx, URL 9]
