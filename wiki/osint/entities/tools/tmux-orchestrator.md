---
title: "Tmux-Orchestrator — Persistent Multi-Agent Tmux Framework"
type: entity
tags: [tool, steal-from, tmux, claude-code, workflow-laptop, auto-checkpoint, mit-license]
keywords: [Tmux-Orchestrator, tmux, persistent session, schedule_with_note, auto-commit, 30-minute checkpoint, multi-agent, hierarchical agents]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/context-compression-resume-pattern.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 9)
- `@concepts/context-compression-resume-pattern.md` — schedule-and-resume pattern relevant here

## Raw Concept

Script-driven framework using tmux to facilitate 24/7 autonomous AI agent execution in persistent background sessions. Three-tier hierarchy: Orchestrator → Project Managers → Engineers. Self-scheduling check-ins + automated 30-minute Git commits.

- **Repo**: `github.com/Jedward23/Tmux-Orchestrator`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Bash scripts + Python utility (`tmux_utils.py`)
- **Maturity**: ~10 commits, no formal release — proof-of-concept
- **Bus factor**: 1

## Narrative

**Recommendation: Steal-from specific scripts, do not adopt full hierarchy.** The 3-tier multi-agent design is overengineered for solo-developer workflow. But the schedule-and-checkpoint mechanics are valuable.

### Patterns worth stealing

1. **`schedule_with_note.sh`** — agent self-scheduling check-ins. Adapt as Zsh alias or `wiki_lint.py` hook for long-running research sessions (e.g., 50-paper synthesis tasks the developer wants to leave running while laptop is closed).
2. **30-minute auto-commit script** — automated Git checkpointing. Survives terminal crash / network drop / lid close. Wire into local Zsh + wiki working directory.

### Why not adopt the full framework

- Production stack requires deterministic state machines (LangGraph + PostgreSQL) — Bash tmux scripts can't deliver observability/rollback metrics
- Script-based terminal scraping (`tmux send-keys` + raw stdout parsing) is notoriously brittle, race-prone, breaks on ANSI pollution
- Low maturity: 10 commits, no releases → proof-of-concept, not stable software
- Knowledge layer pipeline is already simpler via Node.js file watchers in `llm-wiki-compiler`

### Risks (if extracting scripts)

- **ANSI escape sequence pollution [OPEN QUESTION 2026-05-10]**: `tmux_utils.py` must handle unescaped chars without corrupting shell injections
- **License verification**: confirm MIT before extracting
- **Low maturity**: upstream may go stale — fork and own the extracted scripts

[Source: Evaluating Code for Trading Stacks.docx, URL 9]
