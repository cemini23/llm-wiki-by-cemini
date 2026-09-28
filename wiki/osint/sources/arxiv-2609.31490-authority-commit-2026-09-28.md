---
title: "Authority at commit time (2609.31490)"
type: source
tags: [source, k275, agents, governance]
keywords: [k275, reject-and-rerun, commit-authority, FILE]
related:
  - concepts/k275-harness-evolution-wave.md
maturity: draft
created: 2026-09-28
updated: 2026-09-28
read_status: skimmed
---

## Relations

- @concepts/k275-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.31490-authority-at-commit-time-reject-and-rerun-semant.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.31490-authority-at-commit-time-reject-and-rerun-semant.pdf` |
| Archive | egress-fi 2026-09-28 |
| Retrieved | 2026-09-28 |
| Dual-ID | **OSINT K275** |
| sha256 | `1bf395f32f29034de3565a47067666863ab0a237cc8e5313393256c2ef99f0e6` |
| arXiv | 2609.31490 |
| Author | Jesus Salas |

## Narrative

An agent can finish work against a snapshot that is already stale. The paper treats the agent as a proposal writer. A separate service is the only authority that may commit an effect. At admission it checks the proposal's dependencies against current state, then accepts the effect or sends stale work back to run again. Unaffected work can continue.

The pattern matches an external check before a side effect. It does not replace `/route`. Do not rewrite the verify contract mid-run.
