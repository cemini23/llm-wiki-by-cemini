---
title: "Google Code Wiki — Hosted AI-Generated Repository Documentation"
type: entity
tags: [tool, documentation, google, code-visualization, deferred, saas]
keywords: [Google Code Wiki, code documentation, Gemini, SaaS, code visualization, IP security]
related:
  - sources/project-link-evaluation-brief.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief.md` — source evaluation brief (URL 11)

## Raw Concept

Google's hosted SaaS platform that dynamically generates, organizes, and hosts structured documentation for software repositories by ingesting a GitHub URL and parsing the entire codebase.

- **Site**: `codewiki.google/`
- **License**: Proprietary (closed Google service)
- **Stack**: Hosted SaaS; future local Gemini CLI announced but not released

## Narrative

**Verdict: Defer** — gated on release of local Gemini CLI.

The hosted version requires pointing at a public repository, which would expose Cemini's private IP. The promised local Gemini CLI would enable offline documentation generation without data egress. Until released and verified for data isolation, this remains deferred.

[Source: Project Link Evaluation Brief.docx, URL 11]
