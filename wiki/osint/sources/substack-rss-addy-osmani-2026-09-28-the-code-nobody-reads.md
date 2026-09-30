---
title: "Addy Osmani — The Code Nobody Reads (2026-09-28)"
type: source
tags: [source, k276, newsletter, agents, code-review]
keywords: [k276, code-review, accountability, harness]
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

| File | `substack-rss-addy-osmani-2026-09-28-the-code-nobody-reads.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-addy-osmani-2026-09-28-the-code-nobody-reads.md` |
| Archive | egress-fi 2026-09-30 |
| URL | https://addyo.substack.com/p/the-code-nobody-reads |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `cc4076bb3cfe4361f2c9d792b5fbeae57fc16d678a26e0742726f558938d329d` |

## Narrative

The essay argues that line-by-line human review is ending for most code, but that review as accountability is not. Trust must come from the checks built around the model, because a non-deterministic model cannot be certified.

Two governing costs are named: checking unreviewed work, and undoing failures the checks miss.

Figures quoted: 570 review comments with only 14% about defects; under 1% of Claude findings marked incorrect; substantive-review pull requests rising from 16% to 54%; about 8 times more code merged per day. It cites SQLite at about 156,000 lines of C with a test corpus 590 times larger, and a reported 100,000-line compiler built with 16 agents for just under $20,000.

This matches the K275 commit-authority theme: the check, not the model, carries authority. FILE the pattern. Do not build a review harness from this essay alone.
