---
title: "Hugging Face Model Evals.docx — 74 URL poker/MARL HF eval (2026-06-23)"
type: source
tags: [tool-evaluation, huggingface, poker, marl, license-compliance, k127]
keywords: [huggingface-model-evals, MARSHAL, Kuhn poker, Poker_LORA, balatro-poker-cards, MCP security]
related:
  - sources/eval-huggingface-models-k146-refresh-2026-07-05.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/cemini-tool-evaluation-plan-62url-2026-06-23.md
  - sources/links-6-22-tool-eval.md
  - concepts/active-project-research-routing.md
  - concepts/openclaw-security-taxonomy.md
maturity: draft
read_status: deep-read
created: 2026-06-23
updated: 2026-07-05
---

## Relations

- @concepts/kuhn-poker-sft-curriculum-reference.md — K126 Kuhn SFT cluster extended by MARSHAL reject row
- @sources/links-6-22-tool-eval.md — prior HF poker SFT eval lineage

## Raw Concept

- **Original title**: Algorithmic Wagering and Multi-Agent Reinforcement Learning Ecosystem Audit
- **Author**: Gemini Deep Research (74 Hugging Face URLs — poker/MARL/vision)
- **Type**: DOCX (`Hugging Face Model Evals .docx`)
- **Location**: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Hugging Face Model Evals .docx`
- **Retrieved**: 2026-06-23
- **sha256**: `ac7b9a9c029840813596a4277a2fa0bd90c3fc921651c8c6089fcb2a82589a9f`
- **Read status**: deep-read

## Narrative

HF ecosystem audit spanning **MARL poker SLMs**, legacy scraped corpora, and MCP security warnings. Highlights industry pivot from CFR solvers to **Qwen2/3 0.5B–4B self-play** models (MARSHAL framework) and documents **pickle-deserialization RCE** in malicious MCP adapters.

### Recommendation distribution

| Tier | Count | Notes |
|------|-------|-------|
| **UNAVAILABLE** | 52 | 404 / deleted HF repos — strict no-hallucination |
| **Reject** | 18 | NO LICENSE poker models, deprecated Keras2 card classifiers |
| **Defer** | 2 | UltraData-SFT-2605 (identity gate); yolo11_poker_hand_detection |
| **Adopt** | 1 | Wakkamaruh/balatro-poker-cards (Apache-2.0) — **image-gen domain**, not co-primary brief |
| **Steal-from** | 1 | SoelMgd/Poker_LORA (Apache-2.0) — LoRA fine-tune pattern for poker reasoning |

### Notable rows (no reject-stub farm)

| URL | Tier | License | Routing |
|-----|------|---------|---------|
| nics-efc/MARSHAL-Kuhn-Poker-Qwen3-4B | Reject | NO LICENSE | Gambling-wiki reference — complements K126 Kuhn SFT |
| SoelMgd/Poker_LORA | Steal-from | Apache-2.0 | Poker Arena — LoRA curriculum reference |
| Wakkamaruh/balatro-poker-cards | Adopt | Apache-2.0 | Image-gen wiki — FLUX LoRA asset |
| openbmb/UltraData-SFT-2605 | Defer | Apache-2.0 | CCC — Deep Thinking SFT pipeline (gated access) |

### Security note

Docx cites MCP pickle RCE exfiltration — reinforces `@concepts/openclaw-security-taxonomy.md` and `.cursor/rules/osint-mcp-defaults.mdc` hardened MCP posture. No new entity stub.

## Snippets

> "The proliferation of open-weight models tailored to game-theoretic environments indicates a structural transition from static CFR algorithms to dynamic MARL." [Source: Hugging Face Model Evals.docx §foundational (retrieved 2026-06-23)]

> "Malicious orchestrator components weaponized Python pickle deserialization to execute arbitrary shell commands." [Source: Hugging Face Model Evals.docx §MCP security (retrieved 2026-06-23)]

> "Tier: Reject — MARSHAL-Kuhn-Poker-Qwen3-4B — complete absence of a verifiable license string on an IP-sale surface." [Source: Hugging Face Model Evals.docx URL 2 (retrieved 2026-06-23)]
