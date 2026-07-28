---
title: "Self-Authored Verification Is Unreliable (arXiv 2607.24300)"
type: source
tags: [source, arxiv, harness, verification, k198, ccc]
keywords: [verifier-deployment gap, self-improving agents, heuristic rewrite]
related:
  - concepts/verifier-deployment-gap.md
  - concepts/skill-regression-tax.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/verifier-deployment-gap.md
- @concepts/skill-regression-tax.md
- @concepts/code-as-agent-harness.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.24300-self-authored-verification-is-unreliable-in-heur.pdf` |
| **sha256** | `0a1434ea1c9b533855c856bf49ff5271d1bcc70aa1cb3ac8f040250b5f46f372` |
| **arXiv** | [2607.24300](https://arxiv.org/abs/2607.24300) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.24300-self-authored-verification-is-unreliable-in-heur.pdf` |

## Narrative

Self-improving agents that rewrite heuristics **and** author their own accept tests show a **verifier–deployment gap**: self-scores stay near-perfect while real performance degrades. Same failure mode as skill regression tax / play-adequacy vs prediction-accuracy.

**Steal:** poker sandbox + CCC harness — never promote decide() / skill PRs on self-authored gates alone; keep external yardstick / regression matrices.

## Snippets

> "The agent controls both the optimized object and its verifier."
