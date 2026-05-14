---
title: "Nested Learning — Behrouz et al, Google Research (NeurIPS 2025)"
type: source
tags: [source, ml-research, neurips-2025, nested-learning, hope-architecture, titans, continuum-memory, google-research, ccc-wiki-primary]
keywords: [nested-learning, behrouz, razaviyayn, zhong, mirrokni, google-research, neurips-2025, hope-architecture, titans, continuum-memory-system, m3-optimizer, delta-gradient-descent, nsam, ruler-niah, babilong-10m]
related:
  - concepts/nested-learning.md
  - "@ccc-wiki/concepts/nested-learning.md"
maturity: validated
read_status: deep-read
created: 2026-05-13
updated: 2026-05-13
clusters: [ml-research, agent-memory-architecture]
---

## Relations

- @concepts/nested-learning.md — OSINT-side stub; the load-bearing concept page lives in ccc-wiki
- `@ccc-wiki/concepts/nested-learning.md` — primary concept page (ccc-wiki is the meta-wiki on agent architecture / memory / orchestration)

## Raw Concept

- **Title**: Nested Learning (NL)
- **Authors**: Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni (Google Research)
- **Venue**: NeurIPS 2025
- **Format**: PDF, 52 pages
- **Drop location**: `research to be indexed/NL.pdf` → librarian
- **sha256**: `a0d8e2638994ee92...`
- **Size**: 6,126,809 bytes
- **Preingest verdict**: NEW

**What prompted this page**: Boundary-case ingest — the paper is fundamentally about ML architecture (multi-timescale associative memory + self-modifying optimizer + chained MLPs), which fits ccc-wiki (the meta-wiki for agent / workflow / memory design) better than osint-wiki. OSINT keeps a stub for cross-reference; the substantive concept page lives in ccc-wiki.

## Narrative

### Core thesis

ML models are best understood as **nested associative memory systems** with per-level optimization at multi-timescale frequencies. Each level updates at a different "Update Frequency" (the paper's load-bearing primitive in Definition 2).

### Key definitions (paper §2-3)

- **Definition 2 — Update Frequency**: the rate at which a memory level's parameters change. Lower-level memory (e.g., attention weights) updates at every forward pass; higher-level memory (e.g., model weights) updates at every gradient step.
- **Definitions 3-7 — Nested System / NSAM (Neural System with Associative Memory) / Generalized NSAM variants**: formalize the multi-level associative-memory framing. Each level has its own optimizer, frequency, and addressing scheme.

### Hope architecture

The paper's primary architectural contribution. Hope combines:

1. **Self-modifying Titans** — Titans variant where the model generates its own values and keys via Delta Gradient Descent (DGD) with weight decay. The model's parameters update on its own internal signal, not just the external gradient.
2. **Continuum Memory System (CMS)** — a chain of MLPs at progressively longer chunk sizes / lower update frequencies. Short-chunk MLP captures local context; long-chunk MLP captures session-scale context; longest captures world-scale.
3. **M3 optimizer** — the paper's proposed optimizer combining Adam + Muon + CMS. Different parameter classes get different optimizers, gated by the CMS chunk size.

### Empirical results

The paper claims wins across multiple benchmarks:

| Benchmark | Hope result | Comparison baseline |
|-----------|-------------|---------------------|
| RULER NIAH (S-NIAH-1, 16K context) | 100% accuracy | Transformer 79.8% |
| BABILong (10M context retention) | passes | Transformer fails |
| Language modeling (1.3B params) | 58.04 avg | Transformer++ 53.38 |
| Continual translation | passes (Manchu + Kalamang) | Transformer degrades |
| MAD synthetic benchmark | passes | Transformer fails |
| Formal language recognition | parity, aⁿbⁿ | Transformer fails parity |

### Cemini relevance

- **Direct architectural relevance**: Cemini's Conductor + librarian + memory-graph architecture has multi-timescale memory (chroma vectors at one freq, observation graph at another, kb-server at another). The Hope/CMS frame may be the cleanest existing-literature anchor for the "chain of memories at different update frequencies" pattern Cemini already implements ad-hoc.
- **M3 optimizer is not directly relevant** to Cemini (Cemini doesn't train models). The interesting transfer is the **Update-Frequency-as-design-primitive** idea — naming the cadence at which each layer of Cemini's memory ought to refresh.
- **Self-modifying Titans / DGD** is the speculative-but-interesting bit — could agents that modify their own kb-server / observation-graph contents at a higher update frequency than the human operator be a Cemini design direction? Open question.
- **RULER NIAH @ 100% / 16K** and **BABILong @ 10M context** are impressive enough to flag as a watch-this-architecture signal, even if Cemini never implements Hope itself.

This source is filed primarily under ccc-wiki because the meta-architecture lens (workflow / subagent / conductor design) is where the value lands. OSINT keeps a stub for cross-reference when prediction-market / RL-for-trading work touches multi-timescale memory.

## Snippets

> "ML models are nested associative memory systems with per-level optimization at multi-timescale frequencies." [Source: NL.pdf §1 — paraphrased]

> "Hope architecture: self-modifying Titans (DGD with weight decay, generates own values/keys) + Continuum Memory System (chain of MLPs at chunk sizes/frequencies)." [Source: NL.pdf §4 — paraphrased]

> "RULER NIAH S-NIAH-1: Hope 100% at 16K vs Transformer 79.8%. BABILong: Hope retains 10M context. Language modeling: 1.3B params, 58.04 avg vs Transformer++ 53.38." [Source: NL.pdf §6 — paraphrased empirical table]

## Dead Ends

- **Treating NL as a trading-strategy paper** — it isn't. The empirical wins are on language / synthetic / formal-language benchmarks. The relevance to Cemini is architectural (memory + update-frequency design), not strategy.
- **Trying to implement Hope locally** — the M3 optimizer and DGD-with-weight-decay require model-training infrastructure Cemini doesn't have and isn't proposing to acquire. The takeaway is conceptual.
- **Routing this paper to osint-wiki primary** — initial instinct was financial-research-adjacent (because NeurIPS papers sometimes seed RL-for-trading work), but the paper itself is fundamentally about associative-memory architecture. ccc-wiki is the correct primary home.
