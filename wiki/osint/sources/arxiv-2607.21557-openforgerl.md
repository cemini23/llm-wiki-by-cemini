---
title: "OpenForgeRL (arXiv 2607.21557)"
type: source
tags: [source, arxiv, agent-rl, harness, k193, watch]
keywords: [OpenForgeRL, veRL, OpenClaw, Codex, OSWorld, harness-native RL]
related:
  - entities/tools/openforgerl.md
  - concepts/agentic-context-management.md
  - sources/arxiv-2607.21503-agentic-context-management.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-24
clusters: [k193-ingest]
---

## Relations

- @entities/tools/openforgerl.md
- @concepts/agentic-context-management.md
- @sources/arxiv-2607.21503-agentic-context-management.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.21557-openforgerl-train-harness-native-agents-in-any-e.pdf` |
| **sha256** | `2ab40353893eff95b84314067bf5cebcff34d915298c6f4f9aef9591b9b063fe` |
| **arXiv** | [2607.21557](https://arxiv.org/abs/2607.21557) |
| **Authors** | Xiao Yu et al. (Columbia / Dartmouth / Microsoft Research) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.21557-openforgerl-train-harness-native-agents-in-any-e.pdf` |

## Narrative

Open framework to **train harness-native agents** (Claude Code / Codex / OpenClaw-class) end-to-end: proxy records harness model calls for standard RL (veRL); K8s pods run rollouts remotely — train≠deploy mismatch closed. Reports strong GUI/claw numbers (e.g. OSWorld-Verified 37.7; WebVoyager 72.3). RL helps reliability (self-verify, tool coverage) but **error recovery stays weak**. Code/data/models “will release” — **Phase-0 = WATCH** until public repo + license.

**Steal (poker / CCC harness):** don’t reimplement a toy harness for training; prefer train-in-real-harness when code lands; expect harness choice to dominate learnability.
