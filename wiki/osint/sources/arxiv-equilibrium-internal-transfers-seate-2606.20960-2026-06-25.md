---
title: "Equilibrium with Internal Transfers — SETE / M-SETE (arXiv 2606.20960)"
type: source
tags: [source, arxiv, game-theory, equilibrium, marl, k129]
keywords: [2606.20960, SETE, M-SETE, internal transfers, Nash equilibrium, social welfare, MIT]
related:
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/garip-running-average-self-play.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - sources/arxiv-equilibrium-efgsas-2606.13093-2026-06-18.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [rl-marl, llm-agents]
---

## Relations

- @concepts/multi-agent-fictitious-play-llm.md — complementary equilibrium-learning cluster (K124 MAFP)
- @sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md — prior fictitious-play ingest

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Equilibrium with Internal Transfers |
| **Authors** | Mingyang Liu, Gabriele Farina, Asuman Ozdaglar (MIT) |
| **arXiv** | 2606.20960v1 (Jun 2026) |
| **sha256** | `726b7ccc0d23e359c824045e8e11450b03e6ebf921905af814ec46696d20b3f8` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.20960-2606.20960v1-equilibrium-with-internal-transfers.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + equilibrium definitions) |

## Narrative

Classical **NE** can have arbitrarily bad social welfare and is hard to compute. Authors augment games with **budget-balanced internal transfers** paid only if recipients do not deviate.

| Concept | Mechanism | Guarantee |
|---------|-----------|-----------|
| **SETE** | Self-Enforcing Transfer Equilibrium — peer transfers + prescribed strategies | Polymatrix: any social-welfare stationary point → SETE; poly-time algorithm + decentralized learning |
| **M-SETE** | Mediated SETE — mediator binds payment schedule + strategies | Any finite game: socially optimal profile as M-SETE; NE of augmented game (not just agent normal form) |

**Cemini posture:** **REFERENCE / steal-from** — transfer-augmented incentive design for multi-agent poker / MAFP research briefs; no direct prod install. Complements K127 GARIP reference-update schedule and K124 MAFP.

## Snippets

> "We study augmented game models in which players use budget-balanced internal transfers to improve incentives before play." [Source: arXiv:2606.20960 abstract (retrieved 2026-06-25)]

> "For polymatrix games, we show that every stationary point of the social welfare function … can be sustained as a SETE." [Source: arXiv:2606.20960 abstract (retrieved 2026-06-25)]

> "An M-SETE is a Nash equilibrium of the augmented game itself, not merely of its agent normal form." [Source: arXiv:2606.20960 abstract (retrieved 2026-06-25)]

## Dead Ends

- Polymatrix ≠ NLHE — steal is **incentive mechanism**, not literal transfer table for dev.fun submission.
