---
title: "Thinking before thinking: agentic inference through meta-reasoning (2609.38147)"
type: source
tags: [source, k276, agents, inference, harness]
keywords: [k276, meta-reasoning, controller, artifact-graph, FILE]
related:
  - concepts/k276-harness-evolution-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.38147-thinking-before-thinking-scaling-agentic-inferen.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.38147-thinking-before-thinking-scaling-agentic-inferen.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `2a67b8ef69c5db6c05ecbc776868a16f934f597eaaae6c1ca9cc561f2562b166` |
| arXiv | 2609.38147 |
| Authors | Paras Dahal, Anton Bakhtin, Taco Cohen, Zhengxing Chen, Carole-Jean Wu, Rob Fergus, Scott Yih, Gabriel Synnaeve, Ruslan Salakhutdinov, Sanjeev Arora, Jason Weston, Anirudh Goyal (Meta Superintelligence Labs) |

## Narrative

The paper separates two roles in a long agent run. Workers do the task-level computation. A controller decides what to do next: which partial work to build on, whether to start fresh, and when to stop. Between decisions the controller holds only a compact account of the run, not the full history.

The claim is that control becomes its own task as runs get longer. The authors call this agentic meta-reasoning.

Results: on ProgramBench, which tests long-horizon program reconstruction, the method reaches 71.5% with GPT-5.5 against 58.0% for Codex, and 67.2% with Opus 4.8 against 65.5% for Claude Code. On other benchmarks it gains 3.6 to 4.2 points over direct control, averaged across three frontier models. It keeps improving across budget ranges where direct control plateaus.

The authors admit the overhead can hurt at small budgets.

Two transferable design notes: keep the controller context bounded, and compose work as an artifact graph rather than replaying history. Date is 30 September 2026.

No code URL found. No clone. FILE only.
