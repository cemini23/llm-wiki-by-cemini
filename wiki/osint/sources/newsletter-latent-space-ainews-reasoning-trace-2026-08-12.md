---
title: "AINews — How to Steal a Reasoning Trace (CoT Exfiltration)"
type: source
tags: [newsletter, k233, cyber, ccc, cot, security]
keywords: [ainews, reasoning-trace, cot-extraction, encrypted-thinking, claude, gpt, gemini, coT-privacy]
related:
  - concepts/reasoning-trace-exfiltration.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/agent-skill-rl-extraction.md
  - concepts/ai-industry-trends-2026.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: read
---

## Relations

- @concepts/reasoning-trace-exfiltration.md — security/privacy surface
- @concepts/llm-routing-deepseek-openrouter-failover.md — provider-proxy relevance
- @concepts/agent-skill-rl-extraction.md — skill-compilation paragraph connects to SKILLER/K233
- @concepts/ai-industry-trends-2026.md
- @cybersecurity-wiki/briefs/2026-08-12_k233-reasoning-trace-exfil.md (cross-wiki brief)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | "[AINews] How to steal a Reasoning Trace" |
| URL | https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace |
| sha256 | `d5e35741581619b4eaa01359a16df0f5772c26b52101235860c535010aab52f1` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-12-ainews-how-to-steal-a-reasoning-trace.md` |
| retrieved | 2026-08-12 |

## Narrative

AINews daily digest for 2026-08-10/11. Headline story: a responsibly-disclosed attack (first compromise noted by Matthew Green in May) demonstrating it is possible to **decode and port encrypted/signed reasoning blocks** from frontier APIs to different models/sessions/users — and use them to improve open models.

Technique (per paper templates, some variants fixed already):
1. Obtain a legitimate encrypted/signed reasoning block from an API response.
2. Replay it into a different request (possibly another account/session) to a weaker model from the same provider.
3. Place it in an assistant/model turn and prompt/prefill the weaker model to transcribe the attached reasoning.
4. Sample repeatedly, discard refusals, optionally reconcile multiple noisy transcriptions.

Per-model details: **Claude** — replay signed thinking block to Haiku 4.5 with an assistant prefill such as `<thinking-copy>`; **GPT** — inject the `encrypted_content` reasoning item multiple times into a fabricated conversation, sample up to 50 outputs, bypassing an apparent ~50-token verbatim-output threshold via chunked continuations; **Gemini** — attach `thought_signature` to a model turn with a `<thought>` prefill, repeated sampling + reconciliation.

**Alarm note quoted from the disclosure:** a scan of ~7,000 public traces found 62 unique API keys, 33 email addresses, 33 passwords, and other sensitive data (64 appeared *exclusively* inside reasoning blocks, nowhere visible). If you ever shared a Claude Code/Codex session with encrypted reasoning blobs, they can be decoded and leak personal data.

Also relevant (same digest):
- **Skill compilation**: compact natural-language skills distilled from prior trajectories recover **55% to >100%** of the gap between non-reasoning and reasoning modes on multi-step agentic tasks, with **2.7–6× fewer output tokens** — directly reinforces the SKILLER skill-extraction thesis (K233).
- **Nemotron 3.5 Lightning** (NVIDIA "local agent workforce", Harvey: Legal Agent Bench 0%→8.3%, output 90k→37k tokens).
- **Unsloth Desktop** (open-source local train/run desktop app, MLX/GGUF/diffusion, sandboxed code exec, MCP, 2× faster training 70% less VRAM).
- **Meta Muse Glimmer 30B** (Apache-2.0 dense multimodal, always-on local agent workflows, ~4-bit <20GB, DFlash drafter).
- **Grok Bot** (xAI persistent logged-in agent teammates), **ChatGPT desktop for Linux** + agent-workflow import/sync.
- **ExtractBench** (LlamaIndex: commercial VLMs keep precision high but recall collapses <35% on docs >50 pages via silent truncation), **AA-AnalystAgent** (Claude Opus 5 leads 54%).
- **Attestable** ($20M seed; ZK proofs for AI integrity), **deterministic integer-only inference** across A100/H100/M5/EPYC/Xeon (Qwen3-0.6B identical hashed logits, 106 tok/s CUDA-graph A100).

Route: **cyber brief** (CoT exfiltration + public-trace hygiene) + **CCC** (skill compilation, local models) + wiki concepts.

[Source: Latent Space AINews 2026-08-12 (retrieved 2026-08-12)]
