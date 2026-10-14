---
title: Claude Code — Command & Conquer iOS native port case study — 2026-07-07
type: source
tags: [source, claude-code, agent, legacy-port, digest]
keywords: [claude-code, command-conquer, ios, legacy, fable]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/agent-harness-castle-project.md
  - sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md
  - sources/chierhu-ai-coding-tools-game-dev-2026-06-21.md
  - sources/inbox-arxiv-reject-batch-2026-07-10.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: news-digest
source_url: https://theplanettools.ai/blog/command-conquer-native-ios-port-claude-code-fable-5-2026
maturity: validated
created: 2026-07-10
updated: 2026-07-10
---

## Raw Concept

Digest pick (2026-07-07): Google exec reportedly used **Claude Code** (Fable 5) to port **2003 Command & Conquer** to native iOS — legacy C/C++ codebase, not greenfield Godot.

## Narrative

### Pattern [TENTATIVE — press summary]

| Layer | Notes |
|-------|-------|
| Task class | **Legacy port** / platform migration vs greenfield slice |
| Stack | Original C&C → iOS native (not Godot) |
| Agent | Claude Code + Fable-tier model |
| Contrast | castle-sim = Godot 4 + markdown stories + Stagehand smoke |

### castle-sim relevance

| Extract | Skip |
|---------|------|
| Proof that agents handle **large legacy codebases** under operator supervision | Expecting C&C port workflow for greenfield Godot |
| Reinforces verify gates for non-trivial refactors (@concepts/agent-harness-castle-project.md) | iOS/C++ toolchain adoption |

**Verdict:** **WATCH (case study)** — @concepts/ai-assisted-game-dev-workflows.md; **no Phase-0, no brief** (wrong stack; castle-sim is greenfield Godot). Complements @sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md (greenfield) with legacy-port contrast.

## Dead Ends

- Using C&C iOS port press as castle-sim implementation template
