---
title: "Fusion — Multi-Node Agent Orchestrator (Runfusion)"
type: entity
tags: [dev-tooling, multi-agent, worktree-isolation, nodejs, electron, sqlite, mit, steal-from-tier]
keywords: [fusion, agent-orchestrator, worktree-isolation, plan-review-execute, git-worktree, multi-agent-concurrency]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @ccc-wiki/entities/fusion.md  (cross-wiki stub)

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Steal-from tier, CCC wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed, 520 stars. Node.js/Electron agent orchestrator managing 440+ agents across 16 hierarchical companies with Worktree Isolation pattern.

## Narrative

Fusion's key architectural contribution is the Worktree Isolation pattern: each task operates in an isolated git worktree (`fusion/{task-id}`), preventing file collisions across parallel agent executions. The enforced "Plan → Review → Execute → Review" workflow gates are directly applicable to CCC wiki subagent orchestration patterns.

**Tier: Steal-from** — extract the Worktree Isolation pattern, workflow gate design, and Smart Merge conflict resolution logic. Do NOT adopt the full stack — Node.js/Electron/Capacitor introduces frontend architectural bloat incompatible with Cemini's terminal-native, Python-driven environment. MIT license safe for conceptual extraction.

**NEEDS VERIFICATION:** How the SQLite state store handles complex merge conflicts during automated Smart Merge sequences.
