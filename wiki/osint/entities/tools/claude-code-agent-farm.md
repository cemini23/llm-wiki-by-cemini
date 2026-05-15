---
title: "claude_code_agent_farm — Parallel Claude Code Orchestration via tmux"
type: entity
tags: [dev-tooling, claude-code, multi-agent, tmux, orchestration, python, mit, steal-from-tier, laptop-only]
keywords: [agent-farm, parallel-agents, tmux-orchestration, lock-based-concurrency, heartbeat-monitoring, multi-agent-coordination]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Steal-from tier, CCC wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed, 821 stars, Python 3.13+ with uv. Orchestrates up to 50 simultaneous Claude Code agents across tmux panes with lock-based file-write conflict prevention.

## Narrative

Agent Farm demonstrates production-grade parallel Claude Code orchestration patterns: smart monitoring dashboard with heartbeat tracking and HTML run reports, automatic size-based settings backup/restore loops, and pre-flight system verification via a doctor command. The lock-based concurrency system preventing agent file-write conflicts across 20+ tmux panes is the key architectural extraction.

**Tier: Steal-from** — extract heartbeat tracking, HTML report generation, and backup/restore loop logic for the conductor/librarian architecture. Do NOT adopt the core orchestrator — /opt/cemini uses LangGraph for DAG-based agent routing, not terminal multiplexing. MIT license safe for extraction. Cross-wiki routing: document parallel tmux orchestration patterns for large-scale network enumeration in Cybersec wiki.
