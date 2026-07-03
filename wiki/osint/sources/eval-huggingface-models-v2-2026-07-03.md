---
title: "Hugging Face Model Evaluation 2.docx — agentic HF batch (2026-07-03)"
type: source
tags: [tool-evaluation, huggingface, k141, docx]
keywords: [Unlimited-OCR, rampart, Agents-A1, Qwen-AgentWorld, Ornith, DeepSeek-V4, DavidAU]
related:
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/unlimited-ocr.md
  - entities/tools/rampart.md
  - entities/tools/agents-a1.md
  - sources/huggingface-model-evals-74url-2026-06-23.md
maturity: draft
read_status: read
created: 2026-07-03
updated: 2026-07-03
clusters: [wiki-tooling, tipdrop]
---

## Relations

- @entities/tools/unlimited-ocr.md — K141 Adopt MIT → TipDrop M4 ingest
- @entities/tools/rampart.md — K141 Adopt CC-BY (docx) → TipDrop M2 PII
- @entities/tools/agents-a1.md — K141 Adopt Apache-2.0 → OSINT long-horizon research

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hugging Face Model Evaluation 2 (Gemini Deep Research RUNTIME v9) |
| **Type** | DOCX |
| **sha256** | `d97a2ab50bb654f790e051bcf7ae663c004b4fb3ca440b4eb7faacc57168905f` |
| **URLs** | 20 HF models |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Hugging Face Model Evaluation 2.docx` |
| **Retrieved** | 2026-07-03 |
| **Read status** | read (`gh api` on GitHub-linked rows) |

## Narrative

K141 HF batch — **20 models** (agentic SLMs, OCR, compliance, image-gen).

### Tier distribution (docx + gh spot-check 2026-07-03)

| Tier | Count | Notable |
|------|-------|---------|
| **Adopt** | 11 | Unlimited-OCR (MIT), rampart (CC-BY docx), Agents-A1, Ornith-35B, gemma agentic fable5, Qwen-AgentWorld, BFS face-swap, Qwen-Image-Edit, multi-angle LoRA, DavidAU Qwen3.5 |
| **Reference-only** | 3 | DeepSeek-V4-Pro-DSpark, Ornith-9B-GGUF, gemma-3-1b-it |
| **Defer** | 1 | nvidia/Qwen3.6-27B-NVFP4 → xsp-killer |
| **Reject** | 5 | ideogram NC, openai/gpt-oss-120b, Llama 3.1 license, Ornith-9B dup, Krea custom license |

### gh corrections vs docx

| Asset | Docx license | Verified 2026-07-03 |
|-------|--------------|---------------------|
| nationaldesignstudio/rampart | CC-BY-4.0 | **NOASSERTION** on gh — CONDITIONAL-GO; verify HF card |
| TencentCloud/CubeSandbox | Apache-2.0 | **NOASSERTION** on gh — see multi-wiki eval entity |
| Qwen/Qwen-AgentWorld-35B-A3B | Apache-2.0 | HF-only — no `gh api` repo |

### David / TipDrop routing

| Row | Brief home |
|-----|------------|
| baidu/Unlimited-OCR | `tipdrop-workspace-kit/briefs/` — M4 long PDF ingest |
| nationaldesignstudio/rampart | `tipdrop-workspace-kit/briefs/` — M2 client-side PII scrub |

**DavidAU/** HF model = cybersec uncensored reasoning — **not** operator David; wiki-only.

## Snippets

> "Unlimited-OCR … Reference Sliding Window Attention (R-SWA) … 50-plus-page regulatory compliance PDFs in a single forward pass." [Source: Hugging Face Model Evaluation 2.docx URL 2 (retrieved 2026-07-03)]
