---
title: "Hugging Face Model Evals.docx — 74 URL refresh (2026-07-05)"
type: source
tags: [tool-evaluation, huggingface, poker, marl, license-compliance, k146]
keywords: [huggingface-model-evals, MARSHAL, Poker_LORA, MCP pickle RCE, k127-refresh]
related:
  - sources/huggingface-model-evals-74url-2026-06-23.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/active-project-research-routing.md
  - entities/tools/hf-mcp-server.md
maturity: draft
read_status: skimmed
created: 2026-07-05
updated: 2026-10-25
clusters: [rl-marl, poker, wiki-tooling]
---

## Relations

- @sources/huggingface-model-evals-74url-2026-06-23.md — K127 prior ingest (same 74-URL audit; different file hash)
- @concepts/kuhn-poker-sft-curriculum-reference.md — MARSHAL Kuhn row
- @concepts/openclaw-security-taxonomy.md — MCP pickle RCE warning

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Algorithmic Wagering and Multi-Agent Reinforcement Learning Ecosystem Audit |
| **URLs** | 74 |
| **sha256** | `8a3ce23ccd8bbee661044687ff954debc1c004c535f1f2fa4a3aa20e43845e96` |
| **Prior sha256 (K127)** | `ac7b9a9c029840813596a4277a2fa0bd90c3fc921651c8c6089fcb2a82589a9f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Hugging Face Model Evals.docx` |
| **Retrieved** | 2026-07-05 |
| **Read status** | skimmed — tier distribution matches K127; no new Adopt entities |

## Narrative

K146 **refresh drop** of the same Gemini HF audit (74 URLs). `preingest_check` verdict NEW due to different sha256/filename; content distribution unchanged from `@sources/huggingface-model-evals-74url-2026-06-23.md`:

| Tier | ~Count | Action |
|------|--------|--------|
| UNAVAILABLE | 52 | No stubs |
| Reject | 18 | NO LICENSE / stale dumps |
| Defer | 2 | UltraData-SFT-2605 (gated) |
| Adopt | 1 | Wakkamaruh/balatro-poker-cards → image-gen (K127 filed) |
| Steal-from | 1 | SoelMgd/Poker_LORA → poker curriculum |

No new entity pages or David briefs — reinforces MCP pickle-deserialization RCE discipline and MARSHAL license reject. Archive supersedes local K127 docx only as cold-store pointer.

## Snippets

> "Malicious orchestrator components … weaponized Python pickle deserialization to execute arbitrary shell commands." [Source: Hugging Face Model Evals.docx §Foundational (retrieved 2026-07-05)]
