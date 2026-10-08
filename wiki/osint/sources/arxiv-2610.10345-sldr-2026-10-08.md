---
title: "SLDR: defending against malicious fine-tuning (arXiv 2610.10345)"
type: source
tags: [source, k285, arxiv, security, fine-tuning, lora, refusal]
keywords: [sldr, malicious-fine-tuning, lora-poison, layer-sensitivity, dynamic-routing, refusal-restoration, harmful-score]
related:
  - concepts/k285-arxiv-wave.md
  - concepts/skill-misevolution.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md
- @concepts/skill-misevolution.md

## Raw Concept

| Title | SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing |
| Authors | Hui Zhang, Yachao Yuan, Jiayun Wang, Yuanzhuo Li, Hongtao Wang, Yali Yuan (NCEPU; Southeast Univ.; Soochow Univ.) |
| Type | arXiv preprint (cs.CR) — NeurIPS 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.10345-sldr-defending-against-malicious-fine-tuning-via.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.10345v1 |
| Code | `github.com/Stardust457/SLDR` (to be open-sourced on acceptance) |
| read-status | read |

## Narrative

**Malicious fine-tuning** poisons a model (often via a rented LoRA) to strip refusal behaviour. SLDR defends **after** the poison, cheaply.

### The finding

Layer safety sensitivity is **signed**: scaling a layer can *strengthen or weaken* refusal. So do not repair the whole model — repair only the **two extreme-sensitivity layers**.

### Method

1. **Signed layer-sensitivity probe** → pick `l_min = argmin κ_l` and `l_max = argmax κ_l`.
2. Train a **LoRA recovery adapter on those two layers only.**
3. At inference, compute a malicious score
   `S_malicious(x) = (1/N) Σᵢ [cos(r(x), r(xᵢ^harmful)) − cos(r(x), r(xᵢ^benign))]`
   and route through the adapter **iff S > τ** (τ = 0). Benign queries take the untouched path.

### Results

- Average **Harmful Score 11.54 → 0.08** on Llama-3.1/SST2, with **finetune accuracy 92.39 → 92.32 (near-lossless)**.
- HS ≤ 0.40 at poison ratios up to **ρ = 1.0**.
- Beats BDS (1.68), Panacea (5.20), Lisa, Antidote, STAR-DSS, One-shot FT.
- Works across Llama-3.1 / Llama-3 / Qwen-2.5 / Mistral-v0.2.

### Why it matters here

A **cheap, targeted repair** for the fine-tuning-as-a-service attack — repair two layers, route only malicious queries. Relevant to the local abliterated lab (where fine-tunes are the whole point) and to the `skill-misevolution` thread. **Safety research; no PoC.**

## Snippets

> "Layer safety sensitivity is signed: scaling a layer can strengthen or weaken refusal." [Source: arxiv-2610.10345-sldr-defending-against-malicious-fine-tuning-via.pdf]

> "Average Harmful Score 11.54 → 0.08 … Finetune Accuracy 92.39 → 92.32 (near-lossless)." [Source: arxiv-2610.10345-sldr-defending-against-malicious-fine-tuning-via.pdf]
