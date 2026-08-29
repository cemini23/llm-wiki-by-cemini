---
title: JIT-Agent — just-in-time harness intelligence model
type: entity
tags: [tool, harness, ccc, k250]
keywords: [JIT-Agent, HarnessFactory, Evo-GDPO, bingreeky]
related:
  - sources/arxiv-2608.25593-jit-agent-2026-08-29.md
  - concepts/k250-harness-intelligence-wave.md
  - entities/tools/starharness.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
wire_status: reference
wire_target: CCC
wire_note: REFERENCE clone only; trainer wont_wire; do not replace /route or Cursor harness
---

## Relations

- @sources/arxiv-2608.25593-jit-agent-2026-08-29.md — arXiv 2608.25593 paper
- @concepts/k250-harness-intelligence-wave.md — K250 harness cluster
- @entities/tools/starharness.md — stratified evolution sibling (K313)

## Raw Concept

Repo `bingreeky/JIT`. NOASSERTION license on gh API — verify LICENSE file before Integrate. ~124MB REFERENCE clone at `.local/adopts/JIT`. HarnessFactory unified scaffold codebase.

## Narrative

JIT-Agent is the first purpose-built model for **just-in-time harness generation** — synthesizing task-specific harness code for arbitrary agentic LLMs rather than relying on static Ahead-of-Time harnesses like Claude Code/OpenCode configs. Training: customize (task adaptivity) → repair (diagnostic recovery) → Evo-GDPO evolve (archive distillation).

**Verdict: GO REFERENCE (CCC).** Runtime **`wont_wire`** on prod Cursor/`/route`. Pairs K313 StarHarness (stratified search) and K281 AutoDesign (external eval contract). Do not treat JIT output as pass-criteria authority.
