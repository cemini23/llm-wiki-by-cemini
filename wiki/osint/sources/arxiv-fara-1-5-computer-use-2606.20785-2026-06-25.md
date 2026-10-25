---
title: "Fara-1.5 — scalable learning environments for computer use agents (arXiv 2606.20785)"
type: source
tags: [source, arxiv, computer-use, browser-agent, microsoft, k129]
keywords: [2606.20785, FaraGen1.5, CUA, browser-use, Online-Mind2Web, WebVoyager, verifier]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - sources/playwright-mcp-microsoft.md
  - concepts/fara-computer-use-agent-training.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-10-25
clusters: [llm-agents]
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md — verifier / computer-use steal for poker harness
- @sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md — parallel agent-harness cluster (K128)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Fara-1.5: Scalable Learning Environments for Computer Use Agents |
| **Authors** | Aravind Rajeswaran et al. (Microsoft) |
| **arXiv** | 2606.20785v1 (Jun 2026) |
| **sha256** | `616d97136eefbff49495efa000733a226812f1ee50e3eeeaf2019f3f02d05d31` |
| **Repo** | https://github.com/microsoft/fara [TENTATIVE] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.20785-2606-20785v1-fara-1-5-scalable-learning-environm.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + pipeline architecture) |

## Narrative

**FaraGen1.5** pipeline: modular **environments** (live sites + synthetic auth-gated sims), **solvers** (frontier models e.g. GPT-5.4 + user simulator for multi-turn), and **verifiers** (task correctness, efficiency, critical-point adherence). Addresses expensive human CUA demos.

**Fara1.5 models:** Qwen3.5-native CUAs at 4B / 9B / 27B; iterative SFT balancing FaraGen coverage, high-value tasks, and deficiency targeting.

**Benchmarks:** Fara1.5-9B → 63.4% Online-Mind2Web, 86.6% WebVoyager; Fara1.5-27B → 72.3% Online-Mind2Web — SOTA per size class [TENTATIVE — paper table].

**Cemini steal:** **Verifier triad** (correctness + efficiency + critical-point) maps to poker-arena / game-dev playtest harness — not prod browser automation without license + infra review.

## Snippets

> "FaraGen1.5 uses both live websites and synthetic environments that faithfully simulate domains gated by authentication or that require irreversible actions." [Source: arXiv:2606.20785 abstract (retrieved 2026-06-25)]

> "FaraGen1.5 scores the resulting trajectories with three complementary verifiers covering task correctness, efficiency, and critical-point adherence." [Source: arXiv:2606.20785 abstract (retrieved 2026-06-25)]

> "Fara1.5-27B achieves 72.3% on Online-Mind2Web, which is competitive with much larger proprietary systems." [Source: arXiv:2606.20785 abstract (retrieved 2026-06-25)]

## Dead Ends

- Microsoft CUA stack ≠ Cursor built-in browser default — see `@sources/playwright-mcp-microsoft.md` RAM envelope on CPX21.
