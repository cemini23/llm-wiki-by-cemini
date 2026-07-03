---
title: Godot Foundation — AI contribution policy update — 2026-07-01
type: source
tags: [source, godot, policy, ai, harness, news]
keywords: [godot-foundation, ai-contributions, vibe-coding, upstream]
related:
  - entities/engines/godot-4.md
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md
  - sources/inbox-arxiv-reject-batch-2026-07-03.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: news-article
source_url: https://www.gamedeveloper.com/business/godot-to-ban-almost-all-ai-coding-contributions
maturity: validated
created: 2026-07-03
updated: 2026-07-03
---

## Raw Concept

Godot Foundation (Jul 2026) announces **upcoming contribution policy** banning most **genAI code in upstream engine PRs** — autonomous agents, vibe-coded substantial blocks, AI-authored maintainer communication. Exceptions: completion, regex, find-replace; disclose any AI use in PR discussion.

## Narrative

### Policy summary [CONFIRMED — Godot Foundation blog via GameDeveloper.com]

| Banned (upstream `godotengine/godot`) | Allowed |
|---------------------------------------|---------|
| Autonomous AI agent PRs | Code completion, regex, find-replace |
| AI-generated substantial code blocks | Human-authored code with disclosure if AI-assisted |
| AI text in human↔maintainer comms | Machine translation of human-written text |

**Rationale:** maintainers cannot hold AI responsible for fixes; demoralizing review load from "AI slop" PRs (Rémi Verschelde Feb 2026 precedent).

### castle-sim / harness relevance

| Extract | Skip |
|---------|------|
| **Private game repo** AI harness (Cursor, Codex, MCP) **unchanged** — policy is engine upstream only | Panic-disabling agents on castle-sim |
| Reinforces **comprehension debt** thesis [@sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md] | Contributing AI patches to Godot core without human ownership |
| If operator ever upstreams Godot patches: human-authored + disclose | Banning hi-godot/hera on **game project** |

**Verdict:** **STEAL-FROM (policy fence)** — gitignored `briefs/research/godot-upstream-pr-ai-policy-fence.md`.

Cross-ref: @concepts/agent-harness-castle-project.md; @entities/engines/godot-4.md.

## Dead Ends

- Interpreting policy as ban on AI-assisted **game development** — scope is foundation/engine contributions only
