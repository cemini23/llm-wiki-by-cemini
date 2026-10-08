---
title: "EmbodiedRSI: active continual robot learning via hypothesis-guided co-evolution (arXiv 2610.10498)"
type: source
tags: [source, k285, arxiv, robotics, rl, harness, self-improvement]
keywords: [embodiedrsi, hypothesis-graph, value-of-information, code-skill-co-evolution, robocasa365, libero-pro, sim-to-real]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/agent-harness-verification-bottleneck.md

## Raw Concept

| Title | EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution |
| Authors | Python Song, Zhixuan Liang, Kelsey Fu, Mengdi Wang, Junfeng Yang, Shilong Liu (Columbia Univ.; Princeton Univ.) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10498-embodiedrsi-active-continual-robot-learning-thro.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10498v1 |
| Site | `geeksongs.github.io/agentic_robotics/` |
| read-status | read |

## Narrative

A self-evolving **robotics** harness that decides **which physical experiment to run next** and turns the interaction into improved code and skills, with the **robot foundation model frozen**.

### Method — Fast-Slow dual system

**Fast System:**
- **Hypothesis Graph** with Beta(α, β) confidence `c_i = (n_sup + α)/(n_sup + n_ref + α + β)`.
- **Value-of-Information experiment selection**: `G_k(t) = H_exp(D_k) − E_e[H_exp(D_k ∪ {e})]`, scored `VOI_k(t) = G_k(t)/C(t)`.
- **Code–Skill co-evolution**: joint gain `w_ij = R(C_i, S_j) − max{R(C_i), R(S_j)}`.

**Slow System:** hierarchical memory (M1→M2→M3) with **reward-grounded memory learning**, PPO reward `r_mem = λ₁(R_{t+1}−R_t) + λ₂(H_t−H_{t+1}) − λ₃C_{t+1}`.

### Results

- **RoboCasa365: 77.0% overall, 71.3% Composite-Unseen** vs 40.1% best baseline.
- LIBERO-Pro: 86.8% vs 72.1%.
- **Zero-shot sim-to-real** on an SO-101 arm (SmolVLA): **46.0% → 71.3%**; poker-chip task **10.0% → 90.0%**.

### Why it matters here

The **Value-of-Information experiment selection** is the transferable idea: spend the next experiment where it most reduces uncertainty about the hypothesis set. That is a general **active-learning** principle, not just robotics. The **frozen foundation model + learned harness/code/skills** shape mirrors the wiki's harness thread. **No licence stated.** Route: CCC / Game-dev (sim) awareness.

## Snippets

> "Value-of-Information Experiment Selection G_k(t) = H_exp(D_k) − E_e[H_exp(D_k∪{e})]." [Source: arxiv-2610.10498-embodiedrsi-active-continual-robot-learning-thro.pdf]

> "Zero-shot sim-to-real on SO-101 arm … 46.0% → 71.3%; poker-chip task 10.0% → 90.0%." [Source: arxiv-2610.10498-embodiedrsi-active-continual-robot-learning-thro.pdf]
