---
title: claude-task-viewer — web Kanban for Claude Code tasks
type: entity
tags: [entity, tool, observability, kanban, mit, ccc, k235]
keywords: [claude-task-viewer, SSE, task-dashboard, blockedBy, gantt, agent-observability]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Integrate (CCC)
- @concepts/agent-toolkit-routing-research-backlog.md — CCC harness observability lane

## Raw Concept

Repo `L1AD/claude-task-viewer` (710★, last push 2026-02-14). Node/SSE web Kanban reading `~/.claude/tasks/` directly; live blockedBy relationships, gantt-style timelines, desktop notifications; read-only by design (zero interference with agent autonomy).

## Narrative

**Verdict: GO Integrate (CCC harness observability).** **MIT verified** via gh api (docx said "implied by medium article" — now confirmed); cloned `.local/adopts/claude-task-viewer` (3.2M). Replaces terminal-tail ops for Atto M1–M14 / GuruWatcher multi-agent runs.

Caveats: concurrency with many agents mutating tasks JSON simultaneously is unverified (docx NEEDS VERIFICATION carried forward); local-only data hygiene is inherent (reads local file state). Combo from docx: quotio (quota board) + task viewer = unified orchestration dashboard — track as optional, not a dependency.

[Source: L1AD/claude-task-viewer (retrieved 2026-08-13)]
