---
title: "K291 — cybersecurity wave (2026-10-14)"
type: concept
tags: [wave, k291, ingest, hub, red-team, llm-security]
keywords: [K291, jailbreak evaluation, harmful code generation, cybersecurity transformer, speculative decoding]
related:
  - sources/arxiv-ct0-cybersecurity-transformer-2610.16550-2026-10-14.md
  - sources/arxiv-speccloak-harmful-code-specifications-2610.17907-2026-10-14.md
  - sources/arxiv-attck-r-long-horizon-jailbreaking-2610.16305-2026-10-14.md
  - sources/arxiv-sp2ec-self-speculative-decoding-vlm-2610.18735-2026-10-14.md
maturity: draft
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/arxiv-ct0-cybersecurity-transformer-2610.16550-2026-10-14.md — 4B specialist; 80 files/sec IoC screening
- @sources/arxiv-speccloak-harmful-code-specifications-2610.17907-2026-10-14.md — specification framing lowers refusal; 28.91% verified ASR
- @sources/arxiv-attck-r-long-horizon-jailbreaking-2610.16305-2026-10-14.md — protected evaluations; ASR 0.896 → 0.608
- @sources/arxiv-sp2ec-self-speculative-decoding-vlm-2610.18735-2026-10-14.md — inference speed for VLMs (lowest relevance)

## Raw Concept

The question this page answers: **what did the K291 cybersec inbox contain, and which findings change how this workspace evaluates its own agents?**

## Narrative

**Two of the four papers carry a finding. One is a tooling paper. One is barely cybersecurity.**

### ATTCK-R — unprotected evaluations overstate vulnerability

The most transferable result. Introducing **a single prompt-based safety protection** reduces the average attack success rate of a strong multi-turn baseline from **0.896 to 0.608** — a **32.1% relative drop**.

> "Unprotected evaluations substantially overestimate real-world vulnerabilities."

ATTCK-R itself is a planning-driven multi-turn red-team framework for **protected black-box** systems: a structured belief state over a long-horizon trajectory, **optimization-based tactic curation** that abstracts reusable strategies from past successes and failures, and **informed traceback** that resumes attacks from strategically meaningful states instead of restarting. Evaluated across **9 LLMs** behind a prompt-based protection layer.

**The lesson for this workspace: any red-team ASR measured without the deployment's protection layer is not a deployment number.** This is the same class of error as an eval that scores what a system withholds.

### CT0 — small and specialised beats large and general, for one job

A **~4B** cybersecurity transformer on an open Qwen3.5-4B base, specialised by two-phase on-policy distillation. One set of weights serves two modes: **System 1** returns typed security decisions in a single forward pass without generating a token; **System 2** is the usual tool-using agent; a **confidence gate** spends generation only where the fast path is unsure.

| Measure | Value |
|---|---|
| cybench-subtask (agentic) | **21.1%** vs 7.6% base |
| IoC screening | **80 files/sec** |
| Own-refusal detection | **96.5%** at 47 ms (self-judging model: 76.5% at 254 ms) |
| Jailbreak flagging | **AUROC 0.966** at 8 ms |
| Build cost | ~314 RTX PRO 6000 GPU-hours, one workstation GPU |

**The pattern is the confidence gate**: generate only for the facts the fast path is unsure about.

### SpecCloak — specification framing lowers refusal

Across five open-weight models, **removing explicit risk keywords only partially reduces refusal**, but **stating requirements as an engineering specification lowers it substantially — even with the keywords retained**. SpecCloak combines the template with discriminator-guided optimisation for **28.91% execution-verified ASR** across eight models on RedCode-Gen. The defence prototype, **SpecReveal**, reaches **96.88%** attack detection without target-model fine-tuning.

**Contribution to the wiki's existing framing:** refusal is not a property of the request's keywords. It moves with the *form* the request takes.

### SP2EC — lowest relevance

Training-free adaptive self-speculative decoding for VLMs; a bandit algorithm that adapts the draft configuration during generation, up to **11%** faster than prior self-speculative methods. Filed for completeness; no security content.

### Boundary

No install, no PoC, no live Discord, no MCP wire, no `/route` swap.

## Snippets

> "we show that the introduction of a prompt-based safety protection reduces the average attack success rate of a strong multi-turn baseline from 0.896 to 0.608 (32.1% relative), demonstrating that unprotected evaluations substantially overestimate real-world vulnerabilities." [Source: arxiv-2610.16305 p.1]

> "removing explicit risk keywords only partially reduces refusal, whereas specification prompting substantially lowers refusal even when these keywords are retained." [Source: arxiv-2610.17907 p.1]

> "alias3-micro screens eighty files per second for indicators of compromise, catches its own refusals at 96.5% accuracy in 47 ms where the model judging itself reaches 76.5% in 254 ms." [Source: arxiv-2610.16550 p.1]

## Dead Ends

- **Reporting an ASR without stating the protection layer.** ATTCK-R shows the gap between protected and unprotected evaluation is 32% relative on the same baseline.
- **Treating keyword filtering as a refusal boundary.** SpecCloak restates the same request as a specification and refusal falls while the keywords are still present.
