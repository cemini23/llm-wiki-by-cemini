---
title: "ARIS — Auto-Research-In-Sleep"
type: entity
tags: [tool, research-automation, claude-code, skill, workflow, deferred]
keywords: [ARIS, auto-research, ML research, skill framework, markdown-driven, MIT license]
related:
  - sources/project-link-evaluation-brief.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
phase_0_reaudit: 2026-05-10 — 78 skills found (paper-write/proof-checker/specification-writing/research-wiki/idea-creator/experiment-plan); broader scope than initial brief assumed; selective adoption recommended over wholesale install
---

## Relations
- `@sources/project-link-evaluation-brief.md` — source evaluation brief
- `@concepts/tool-evaluation-framework.md` — evaluation methodology

## Raw Concept

ARIS (Auto-Research-In-Sleep) is a Markdown-based orchestration framework for automating ML research lifecycles via Claude Code. Evaluated in the Project Link Evaluation Brief (URL 12) and recommended for **Adopt**.

- **Repo**: `github.com/wanshuiyin/Auto-claude-code-research-in-sleep`
- **License**: MIT
- **Stack**: Pure Markdown + text instruction files
- **Footprint**: Kilobytes of disk, zero runtime overhead (runs inside Claude Code process)

## Narrative

ARIS provides a structured research automation pipeline via plain-text SKILL.md definitions. It defines an `/idea` → `/experiment` → `/paper` workflow that Claude Code executes, with built-in cross-model review loops.

### Integration vectors

- **Workflow (Adopt)**: Install via `git clone` into Claude Code context directory. Invoke during manual research/curation phase to automate structured exploration of complex financial mechanisms.
- **Cemini prod (No)**: Autonomous multi-hour LLM research loops on the trading server would consume API tokens and CPU during active trading hours.
- **Wiki server (No)**: Text-compilation server doesn't execute research workflows.

### Risks

- **Prompt drift**: LLMs tend to ignore Markdown instructions over long conversations; requires human supervision
- **API cost exhaustion**: Autonomous cross-model review loops can silently burn API tokens if the agent gets trapped in adversarial review cycles

### Cemini significance

Provides a structured, repeatable research methodology at zero framework cost. The Markdown-driven architecture aligns with the existing wiki workflow — research skill definitions can themselves be versioned as wiki pages.

[Source: Project Link Evaluation Brief.docx, URL 12]
