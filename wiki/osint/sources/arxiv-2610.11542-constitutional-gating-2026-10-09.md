---
title: "Constitutional gating and deterministic recovery (arXiv 2610.11542)"
type: source
tags: [source, k287, arxiv, agents, gates]
keywords: [constitutional-gating, cognitive-annealing, deadlock, k287]
related:
  - concepts/k287-arxiv-wave.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
read_status: read
---

## Relations

- @concepts/k287-arxiv-wave.md

## Raw Concept

| Title | Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation |
| Authors | Masaaki Nakatsu, Reno Wang |
| Type | arXiv preprint |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.11542-constitutional-gating-and-deterministic-recovery.pdf` |
| Retrieved | 2026-10-09 |
| arXiv | 2610.11542v1 |
| Licence | arXiv non-exclusive distribution 1.0 |
| read-status | read |

## Narrative

The paper tests a constitution, a four-tier swarm, and a deterministic recovery step against a gatekeeper with fixed acceptance rules. Five runs per arm.

The constitution makes an acceptable framing possible and not reliable (0 of 5 baseline unlocks, 1 of 5 and 2 of 5 with the constitution). Under a compliance deadlock, LLM-only steering escapes 0 of 5 times. Atomic purge plus a canonical recovery message escapes 5 of 5 times, at the same call budget.

This matches the desk rule that a hard gate beats another prompt. The paper does not change that rule. No agent-wiki brief.

## Snippets

> "LLM-only steering escapes 0 of 5 times while atomic purge plus a canonical strike escapes 5 of 5 (Fisher p = 0.008)." [Source: arxiv-2610.11542 PDF, abstract]
