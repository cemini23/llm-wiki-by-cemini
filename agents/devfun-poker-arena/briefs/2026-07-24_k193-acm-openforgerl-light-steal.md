---
title: K193 — ACM context lifecycle + OpenForgeRL WATCH (light steal)
type: brief
target: poker-arena
created: 2026-07-24
updated: 2026-07-24
---

## Target

agents/devfun-poker-arena — decide() / HL session memory.

## Summary

Steal **Agentic Context Management** framing (2607.21503): memory = lifecycle (architect/ingest/scope/anticipate/compact), not infinite RAG. OpenForgeRL (2607.21557) is **WATCH** until code+license public — train-in-real-harness pattern matters more than toy reimplementations; RL helps reliability but error recovery stays weak.

## Body

1. Align HU hierarchical memory / session trail with ACM primitives: explicit eviction + provenance + budgeted compact.
2. Do not pull Maximem Synap SaaS for arena.
3. When OpenForgeRL lands (MIT/Apache hoped), re-phase-0 for sandbox training — not before.
4. No install this batch (&lt;500MB rule + no public repo).

## Sources

- osint-wiki: arxiv-2607.21503, arxiv-2607.21557, concepts/agentic-context-management, entities/tools/openforgerl
- local: references/hl-session-trail.md, config/hu_hierarchical_memory.json
