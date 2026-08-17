---
title: "Tripwire — training-free certified safety neurons (arXiv 2608.14392)"
type: source
tags: [arxiv, llm-safety, cyber, k240]
keywords: [tripwire, safety-neurons, ASR, bias-patch, abliterated]
related:
  - concepts/intent-not-form-refusal.md
  - sources/eval-url-revenue-opportunity-2026-08-17.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @concepts/intent-not-form-refusal.md — wrapper-invariant refusal sibling (K239 WIFA)
- @sources/eval-url-revenue-opportunity-2026-08-17.md — Qwen abliterated GGUF Watch; do not clamp without HITL

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.14392, "Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons" |
| Authors | Wei Zhao, Zhe Li, Peixin Zhang, Jun Sun (Singapore Management University) |
| Retrieved | 2026-08-17 |
| File | `arxiv-2608.14392-tripwire-triggering-aligned-refusal-via-statisti.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.14392-tripwire-triggering-aligned-refusal-via-statisti.pdf` |
| Type | cs.AI preprint, 9pp |
| Dual-ID | **OSINT K240**. **CCC K240** = robotics solver (old). Cyber lab awareness only. **No PoC.** |

## Narrative

Training-free defense: identify safety-specific neurons with per-neuron Welch t-tests under BH-FDR plus a utility-specificity filter, then **clamp** those neurons at their harmful-conditional mean so the model receives an internal "this input is harmful" signal and fires the refusal it already learned in alignment. Two equivalent deployments: detector-gated inference-time clamp, and an offline bias-patch weight edit.

Reported `[TENTATIVE]`: average ASR **≤2.0%** across Llama-2/3.1 and Qwen2.5 vs four jailbreaks (GCG, AmpleGCG, AutoDAN, Jailbreak-R1); utility drop **0.5%–5.3%** on MT-Bench — smallest among compared defenses.

### Steal / do-not

Cyber lab awareness. **Do not** neuron-clamp abliterated lab models without HITL. Do not put jailbreak / Tripwire PoC / HTB payloads in the wiki. Pairs Qwen 27B abliterated GGUF **Watch, no weight download**.

## Snippets

> "TripWire reduces the average attack success rate to at most 2.0% while incurring a utility drop of only 0.5% to 5.3% on MT-Bench." [Source: arxiv-2608.14392 abstract]
