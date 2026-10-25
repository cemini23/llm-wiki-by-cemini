---
title: "awesome-ralph — curated Ralph autonomous-agent pattern resources (Steal-from)"
type: entity
tags: [tool, awesome-list, ralph-pattern, autonomous-agent, file-based-memory, gemini-eval-doc1]
keywords: [awesome-ralph, snwfdhmp, ralph wiggum, prd.json, progress.txt, fresh-context loops, autonomous agent pattern]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/ralph-autonomous-agent-pattern.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/smart-ralph.md
  - entities/tools/ralph-claude-code.md
maturity: draft
created: 2026-05-12
updated: 2026-10-25
gemini_eval_doc1_url: 1
phase_0_verdict: STEAL-FROM 2026-05-12 (extract Ralph methodology, no wholesale fork)
---

## Relations

- @entities/tools/smart-ralph.md
- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 1)
- `@concepts/ralph-autonomous-agent-pattern.md` — distilled Ralph methodology written from this entry

## Raw Concept

- **Repo**: `github.com/snwfdhmp/awesome-ralph`
- **License** [per Gemini eval]: MIT
- **Tier**: Steal-from
- **Primary fit**: Workflow (methodology extraction; the Ralph pattern itself, not the repo)

## Narrative

Curated awesome-list for the Ralph autonomous-agent pattern: file-based persistent memory (`prd.json` + `progress.txt`), fresh-context-per-iteration loops, separate `PROMPT_plan.md` / `PROMPT_build.md` skill files. Pattern is distilled into `@concepts/ralph-autonomous-agent-pattern.md` for reference; the repo itself is a directory pointer, not a tool to install.

### Integration vector

Read the awesome-list, extract specific implementation hints (e.g., progress.txt schema). Apply pattern in any laptop-side Claude Code skill needing long-running task continuity beyond a single context window. **Do not fork** — there's no codebase to fork; the value is methodological.
