---
title: "How Much Due Diligence Before You Bid? — arXiv 2606.29457"
type: source
tags: [arxiv, game-theory, auctions, poker, imperfect-information, k138, pdf]
keywords: [takeover auction, due diligence, PPO, PPG, CFR, OpenSpiel, exploitability, deal games, Sparq]
related:
  - concepts/takeover-auction-diligence-solvers.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/multi-agent-fictitious-play-llm.md
  - sources/arxiv-nash-solver-selection-2606.28308-2026-06-30.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
maturity: draft
read_status: read
created: 2026-07-01
updated: 2026-07-01
clusters: [game-theory, poker, rl-marl]
---

## Relations

- @concepts/takeover-auction-diligence-solvers.md — synthesized concept
- @concepts/nash-equilibrium-solver-selection.md — K136 solver-family literacy cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | How Much Due Diligence Before You Bid? Learning in Intractable Takeover Auctions |
| **Author** | Zain Naboulsi (Sparq) |
| **arXiv** | 2606.29457v1 |
| **Type** | PDF |
| **sha256** | `34e66fcdabfc15c9dda1d1396e81af1bbdea48863cae3be6a89922617eeed96f` |
| **Repo** | https://github.com/zainnab-sparq/imperfect-information-deal-games |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.29457-1-introduction.pdf` |
| **Retrieved** | 2026-07-01 |
| **Read status** | read (abstract + intro + solver benchmark sections) |

## Narrative

Models M&A takeover contests as **two-player zero-sum auction games** (common-value w/ winner's curse, toehold, IP variants) on a reusable **DealGame** abstraction over **OpenSpiel**. Benchmarks **nine solvers** (CFR, MMD, PSRO, REINFORCE, PPO, PPG, deep PG, Deep CFR, NFSP).

### Key findings

1. **Economic:** optimal due-diligence signal count is **finite** and **decreases** with per-signal cost; symmetric acquisition equilibrium is more conservative than one-sided calc.
2. **Computational:** on enumerable games, **exact solvers (CFR, MMD, PSRO) beat PPO/PPG** in exploitability and wall-clock; PPO/PPG dominate among **learning** solvers at equal episode budget.
3. **Scaling:** PPO flat per-target wall-clock vs CFR steep growth — advantage only **beyond enumeration**; on largest tabular game PPO fails to hit exploitability target.
4. **Intractable regime:** multi-signal auction too large to enumerate — PPO/PPG drive calibrated LBR exploitability estimate below naive unshaded bidder (**lower bound**, not Nash cert).

**Cemini relevance:** poker-arena literacy — when to trust PPO self-play vs exact CFR on toy games; diligence↔signal-count link mirrors private-info action-space blowup in imperfect-info poker. **Not NLHE prod.**

## Snippets

> "Wherever the game is small enough to tabulate, the exact solvers (CFR, MMD, PSRO) are both lower in exploitability and faster." [Source: arxiv-2606.29457-1-introduction.pdf abstract (retrieved 2026-07-01)]

> "PPO and PPG are by far the strongest learning solvers, but only within that family." [Source: arxiv-2606.29457-1-introduction.pdf abstract (retrieved 2026-07-01)]
