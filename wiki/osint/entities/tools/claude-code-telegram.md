---
title: claude-code-telegram — Telegram bot with sandbox hardening (Steal-from)
type: entity
tags: [tool, claude-code, telegram, sandbox, path-traversal-defense, mit, steal-from, workflow, cybersec-cross-route]
keywords: [claude-code-telegram, telegram bot, CLAUDE_ALLOWED_TOOLS, APPROVED_DIRECTORY, sandbox, whisper stt, fastapi]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Steal-from
- `@concepts/tool-evaluation-framework.md` — methodology

## Raw Concept

- **URL**: `https://github.com/RichardAtCT/claude-code-telegram`
- **License**: MIT
- **Stars**: 2.6k / 14 open issues
- **Stack**: Python 3.11+, Poetry, SQLite, FastAPI, Whisper (STT)
- **Tier**: Steal-from
- **Primary fit**: Workflow

## Narrative

Telegram bot for Claude Code with sandboxing hardening. Key extractable patterns:
- `CLAUDE_ALLOWED_TOOLS` env array (tool whitelist)
- `APPROVED_DIRECTORY` bounding box (path-traversal defense)
- FastAPI webhook event-driven components for laptop-side task schedulers
- Task (🧠) sub-agent orchestration path

>85% pytest coverage, strict mypy.

[Source: Tool Evaluation and Wiki Fit.docx URL 3 (retrieved 2026-05-13)]
