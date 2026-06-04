---
title: Sandboxed Coding Agents are Competitive Omni-modal Task Solvers (arXiv:2606.00579)
type: source
tags: [source, arxiv, agent-harness, sandbox, omni-modal, k96]
keywords: [2606.00579, omni-coding, code-x, terminal-bench-o, sandboxed-agents]
related:
  - concepts/cli-anything-agent-native-computer-use.md
  - sources/cemini-external-code-audit-errors-2026-06-03.md
  - concepts/nemo-execution-aware-optimization-modeling.md
  - sources/arxiv-nemo-execution-aware-optimization-2601-21372-2026-06-04.md
read_status: skimmed
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- @concepts/cli-anything-agent-native-computer-use.md — complementary CLI surface pattern
- @ccc-wiki/concepts/agent-vm-sandboxing.md — sandbox posture for agent tool use

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sandboxed Coding Agents are Competitive Omni-modal Task Solvers |
| Authors | Dongping Chen et al. (UMD + MBZUAI) |
| arXiv | 2606.00579 |
| Retrieved | 2026-06-03 |
| Location | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.00579-sandboxed-coding-agents-are-competitive-omni-mod.pdf` |
| read_status | skimmed |

Daily digest fetch 2026-06-03. Repo: https://github.com/Dongping-Chen/OmniCoding

## Narrative

Text+image coding agents with **sandboxed terminal tool-use** match or beat native omnimodal models on video/audio benchmarks by converting tasks to **retrieval + code orchestration** (ffmpeg, whisper, OCR) rather than ingesting full media streams. Introduces **Code-X** training recipe and **TerminalBench-O** process-level benchmark.

**Cemini relevance:** REFERENCE for librarian/conductor multimodal ingest (video briefs, NotebookLM) — aligns with `@concepts/cli-anything-agent-native-computer-use.md` steal-from, not a prod install.

## Snippets

> coding agents with only text+image access and a sandboxed tool-use interface can match, and in several settings outperform, SOTA native omnimodal models

[Source: arxiv-2606.00579-sandboxed-coding-agents-are-competitive-omni-mod.pdf p.1, retrieved 2026-06-03]
