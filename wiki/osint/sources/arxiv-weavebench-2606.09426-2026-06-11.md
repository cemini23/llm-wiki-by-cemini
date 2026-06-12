---
title: WeaveBench — hybrid-interface computer-use agent benchmark (arXiv 2606.09426)
type: source
tags: [source, arxiv, computer-use-agents, benchmark, gui-cli, agent-harness]
keywords: [2606.09426, WeaveBench, CUA, trajectory-judge, hybrid-interface, OpenClaw]
related:
  - concepts/llm-agent-systems.md
  - concepts/code-as-agent-harness.md
maturity: validated
read_status: skimmed
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/llm-agent-systems.md — benchmark cluster
- @concepts/code-as-agent-harness.md — deployed-runtime evaluation gap

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces |
| **arXiv** | 2606.09426 |
| **sha256** | `1a5f233435576800433aa945eec9c54ae6412baed5779865c82f3feeea78f1c9` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.09426-introduction.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | skimmed — abstract, Table 1 positioning, headline PassRate |

## Narrative

**114 tasks** across 8 real-world domains on Ubuntu desktop; each requires **interleaved GUI + CLI/code** in one trajectory. Companion **trajectory-aware judge** audits deliverables, logs, screenshots, and shortcut behaviors (fabricated evidence, hard-coded metrics).

Best PassRate **41.2%** (Claude Opus 4.7 + Claude Code) vs >78% on OSWorld-Verified — outcome-only grading overestimates (GPT-5.5: 53.5% → 33.3% audited). GUI-only and CLI-only ablations ≤3.5%.

**Cemini mapping:** REFERENCE for **conductor/laptop harness** eval — Cemini workflows routinely mix browser, terminal, MCP, and file edits. Steal: trajectory judge + shortcut detection before trusting "task complete" on multi-hop wiki ingest or prod brief execution. No install — benchmark harness is external.

## Snippets

> "Outcome-only grading substantially overestimates agent performance."

> — [Source: arxiv-2606.09426-introduction.pdf Abstract, retrieved 2026-06-11]

> "Best model–runtime pairing reaches 41.2% PassRate … GUI-only and CLI-only settings stay at or below 3.5%."

> — [Source: arxiv-2606.09426-introduction.pdf §1, retrieved 2026-06-11]
