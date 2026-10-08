---
title: "PatchBench: measuring collateral damage in activation patching (arXiv 2610.10276)"
type: source
tags: [source, k285, arxiv, safety, interpretability, evals, jailbreak]
keywords: [patchbench, activation-patching, jailbreak-repair, hncs, bnps, mmlu-blind, collateral-damage]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/agent-safety-executable-evaluation.md

## Raw Concept

| Title | PatchBench: Measuring Collateral Damage in Activation Patching |
| Authors | Alexi Canesse et al. (LIX École Polytechnique / IP Paris; AMIAD) |
| Type | arXiv preprint (cs.LG) — NeurIPS 2026 Evaluations & Datasets |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10276-patchbench-measuring-collateral-damage-in-activa.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10276v1 |
| Code | `github.com/orailix/PatchBench-Local` (MIT) · data non-commercial |
| read-status | read |

## Narrative

**Activation patching** "repairs" a model's refusal on a jailbreak by steering activations. This paper asks whether that is a **selective repair** or **broad local suppression** — and shows aggregate metrics miss the difference.

### Method

From 27,870 jailbreak prompts → manual filter (15,314) → query 8 open-source LLMs → WildGuard filtering + pairwise Elo ranking → **50 failures per model**. **PatchBench-Local** generates **29 neighbours per source**: 19 harmful variants (paraphrase, translation, punctuation, case-inversion, spelling), 5 structural-benign, 5 lexical-benign (harmful word, benign intent). Two metrics:

- **HNCS** — Harmful Neighbour Correction (did the fix generalise?)
- **BNPS** — Benign Neighbour Preservation (did it break benign neighbours?)

### The finding

**Aggregate safety metrics hide collateral damage.** AST-style patching gains HNCS but loses large BNPS: **Qwen-3B +3.1 HNCS over AlphaSteer yet −27.4 BNPS**; Gemma-4B **58.3 lower BNPS**. And crucially: **MMLU can be flat while local regression is severe** — CAST on Llama-8B shows MMLU **−0.07** points but BNPS **−26.3** points.

### Why it matters here

A **general measurement lesson**: a global benchmark can be blind to a large local regression. That is the same shape as the wiki's "audit the change set, not the metric" doctrine, and it matters for any safety tuning on the local abliterated lab. Route: cyber / local lab. **No PoC.**

## Snippets

> "MMLU can be flat while local regression is severe (CAST on Llama 8B: MMLU −0.07 pts, BNPS −26.3 pts)." [Source: arxiv-2610.10276-patchbench-measuring-collateral-damage-in-activa.pdf]

> "AST gains HNCS but loses big BNPS — Qwen 3B: +3.1 HNCS over AlphaSteer yet −27.4 BNPS." [Source: arxiv-2610.10276-patchbench-measuring-collateral-damage-in-activa.pdf]
