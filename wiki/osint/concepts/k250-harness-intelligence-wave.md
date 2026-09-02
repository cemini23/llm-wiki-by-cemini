---
title: K250 harness intelligence wave (Aug 2026)
type: concept
tags: [agents, harness, k250, ccc]
keywords: [JIT-Agent, ReasoningBank, harness-intelligence, just-in-time]
related:
  - sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md
  - sources/arxiv-2608.25593-jit-agent-2026-08-29.md
  - sources/source-grok-loop-engineering-note-2026-08-29.md
  - sources/source-harness-final-anonymous-2026-08-29.md
  - entities/tools/jit-agent.md
  - entities/tools/reasoning-bank.md
  - concepts/k250-skill-evolution-wave.md
  - sources/eval-github-revenue-evaluation-k250-2026-08-29.md
  - sources/eval-links-empty-stub-k250-2026-08-29.md
  - concepts/k252-harness-evolution-wave.md
maturity: draft
created: 2026-08-29
updated: 2026-08-31
wire_status: policy_wired
wire_target: ccc-k246-k253-phase1-wires.mdc
---

## Relations

- @sources/eval-links-empty-stub-k250-2026-08-29.md — empty eval stub

- @sources/eval-github-revenue-evaluation-k250-2026-08-29.md — GitHub revenue eval

- @sources/arxiv-2509.25140-reasoning-bank-2026-08-29.md — reasoning-memory bank + MaTTS
- @sources/arxiv-2608.25593-jit-agent-2026-08-29.md — JIT harness synthesis model
- @sources/source-grok-loop-engineering-note-2026-08-29.md — operator Grok loop engineering PDF
- @sources/source-harness-final-anonymous-2026-08-29.md — anonymous harness design note
- @entities/tools/jit-agent.md — bingreeky/JIT REFERENCE clone
- @entities/tools/reasoning-bank.md — google-research/reasoning-bank REFERENCE
- @concepts/k250-skill-evolution-wave.md — WikiSkill sibling cluster

## Raw Concept

K250 harness-intelligence cluster — ReasoningBank (reasoning strategies in memory) + JIT-Agent (trainable just-in-time harness generator) + operator harness/Grok loop notes.

## Narrative

Three papers/notes converge on **harness intelligence** as a trainable axis orthogonal to model scaling. ReasoningBank distills success/failure trajectories into a reusable reasoning-memory bank with memory-aware test-time scaling (MaTTS). JIT-Agent trains a meta-model to synthesize task-adaptive four-module harnesses (memory, planning, action, capability orchestration) for off-the-shelf LLMs, with customize → repair → evolve stages; reported competitive with OpenCode and Claude Code runtimes on DeepSearchQA/OdysseyBench.

Operator PDFs (`grok_loop_engineering_note_HQ.pdf`, `harness_final.pdf`) are CCC-context loop/harness design notes — REFERENCE only, no runtime wire. **Phase-1:** pairs K313 stratified harness evolution, K281 AutoDesign (external eval contract), K292 HCL. **0 Integrate GO** — `.local/adopts/` REFERENCE clones only; never auto-evolve `.cursor/skills`.
