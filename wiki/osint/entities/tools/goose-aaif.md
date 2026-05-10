---
title: "Goose — AAIF General-Purpose AI Agent Framework"
type: entity
tags: [tool, ai-agent, mcp, acp, rust, typescript, reference-only]
keywords: [Goose, AAIF, agent framework, MCP, ACP, Rust, TypeScript, autonomous agent]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 5)

## Raw Concept

Goose is the Agentic AI Foundation's general-purpose native AI agent framework. 44.9k stars, Apache-2.0, v1.33.1 (April 2026). Rust + TypeScript, ships as desktop app and CLI.

- **Repo**: `github.com/aaif-goose/goose`
- **License**: Apache-2.0
- **Maturity**: 44.9k stars, 4,399 commits, v1.33.1

## Narrative

**Verdict: Reference-only.** Goose's MCP and ACP (Agentic Connectivity Protocol) implementations are worth studying as reference architectures for how industry-standard agents connect to complex tools. However, deploying a secondary autonomous agent alongside Claude Code on the macOS workflow would fragment workspace history. On Cemini prod, granting an autonomous Rust/TypeScript agent shell access to the trading server is architecturally incompatible with the deterministic LangGraph orchestrator.

Notable: 44.9k stars and Apache-2.0 make this one of the most mature open-source agent frameworks. The MCP implementation patterns specifically are worth deep study.

[Source: Project Link Evaluation Brief 5_10.docx, URL 5]
