---
title: "HTML-Effectiveness Pattern — LLM-Generated Interactive HTML Artifacts"
type: entity
tags: [tool, design-pattern, html, claude-code, deliverables, visualization]
keywords: [HTML artifacts, Claude Code, Thariq, interactive deliverables, design pattern, XSS]
related:
  - sources/project-link-evaluation-brief.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief.md` — source evaluation brief (URL 3)

## Raw Concept

A design paradigm advanced by Anthropic's Thariq: AI agents should generate self-contained, interactive HTML files (with collapsible sections, embedded SVG diagrams, sortable tables) rather than monolithic walls of static Markdown when producing complex deliverables.

- **Site**: `thariqs.github.io/html-effectiveness/`
- **Related repo**: `github.com/dogum/html-artifacts` (Apache-2.0)
- **License**: Pattern concept is free; specific CSS/HTML on demo site has ambiguous licensing

## Narrative

The HTML-effectiveness pattern proposes that for complex quantitative mechanism explanations, system outage incident reports, or interactive data exploration, LLMs should output self-contained HTML artifacts instead of Markdown. HTML enables collapsible sections, sortable tables, inline SVG, and interactive filtering that static Markdown cannot express.

### Integration vectors

- **Workflow (Steal-from)**: Adopt the design pattern via a Claude Code SKILL.md with PreToolUse/PostToolUse hooks. When the agent produces complex deliverables, it defaults to interactive HTML instead of Markdown.
- **Wiki server (Steal-from)**: Embed interactive HTML templates into the Markdown rendering pipeline managed by `llm-wiki-compiler`. Complex quantitative mechanism explanations or system outage incident timelines become interactive.
- **Cemini prod (No)**: Trading execution doesn't consume HTML artifacts.

### Risks

- **XSS vector**: LLM-generated HTML rendered locally or served via librarian dashboard introduces Cross-Site Scripting risk. If an agent hallucinates or is prompted to inject malicious `<script>` tags, the artifact becomes an attack vector. Mitigation: CSP headers + sandboxed iframe rendering.
- **License ambiguity**: The HTML/CSS on the demo site lacks an explicit open-source license. The instructional companion repo is Apache-2.0, but the visual templates require license verification before embedding.

### Open questions

- Explicit open-source license governing the HTML, CSS, and inline SVG template structures on the portfolio site `[NEEDS VERIFICATION 2026-05-10]`

[Source: Project Link Evaluation Brief.docx, URL 3]
