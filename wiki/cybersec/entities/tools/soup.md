---
title: "Soup — YAML fine-tuning with layer streaming (Apache-2.0; CUDA story, not Apple Silicon)"
type: entity
tags: [tool, fine-tuning, low-vram, layer-streaming, local-lab, apache-2.0]
keywords: [soup, soup-cli, layer streaming, qlora, lora, 4gb gpu, mps, apple silicon]
related:
  - "@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md"
maturity: draft
created: 2026-11-04
updated: 2026-11-04
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md, URL 10, **Extract** tier. Routed to the local-abliterated / operator lab.

The question this page answers: **can an 8B model be trained on hardware this estate actually has?**

## Narrative

### What it is

`MakazhanAlpamys/Soup`. A CLI for fine-tuning and post-training from a **single YAML config**, with no SSH or infrastructure setup.

Coverage is broad: SFT; preference methods DPO, GRPO, PPO, KTO, ORPO, SimPO, IPO, BCO; LoRA and QLoRA; quantisation; data tools; evaluation; serving; and export to GGUF, ONNX, and TensorRT.

The headline feature is **layer streaming** — load the frozen base model's layers from system RAM one at a time, so a model that does not fit in VRAM can still train. The claim is that output stays bit-identical to a normal run.

**10.1k stars**, 1.7k forks, `soup-cli` on PyPI, v0.77.1.

### Phase-0, 2026-11-04 — the licence clears, the hardware claim does not

**Licence: Apache-2.0.** The report recorded "NOT FOUND". Confirmed at the repository's licence section, with the standard Apache redistribution terms — keep `LICENSE` and `NOTICE`, mark changed files.

**Hardware, from the README:**

| Platform | Position |
|----------|----------|
| CUDA GPU | **"recommended"** — the headline path |
| **Apple Silicon (MPS)** | "supported" |
| CPU | "experimental — very slow" |

Standard QLoRA guidance given: about 7B at 8 GB VRAM, 14B at 16 GB, 34B at 24 GB, 70B at 48 GB.

**The mismatch.** The report frames this as "8B LLM fine-tuning on **4 GB laptop GPU**". Two things are true at once: layer streaming is an **opt-in beta**, and the 4 GB story is a **CUDA** story. Apple Silicon is "supported" — which says MPS runs, and says nothing about whether layer streaming works there or what it costs in speed.

The estate's laptop is Apple Silicon. So the claim that goes untested is the one that matters.

### The test that would settle it

Before any use: take one small model, run a short SFT run with layer streaming **on MPS**, and record tokens/second and peak memory against the same run without streaming. If streaming does not work on MPS, the tool is ordinary QLoRA and the 4 GB framing is irrelevant here.

The bit-identical claim is also worth checking — a streaming implementation that silently changes numerics would be a quiet corruption in a fine-tuned model.

### Fit

The **lab only** — local-abliterated, authorized whitehat scope. A YAML-driven post-training CLI is useful there precisely because it does not need infrastructure. It is not an Atto, Collectibles, or game-time tool.

### Status

Extract. Licence clears; the Apple Silicon question is open and should be measured before it is believed.

## Snippets

> "[Apache-2.0](LICENSE). Copyright 2026 Makazhan Alpamys and the Soup contributors." — README [fetched 2026-11-04]

> "A CUDA GPU is recommended. Apple Silicon (MPS) is supported, and CPU is described as 'experimental — very slow.'" — README [fetched 2026-11-04]

## Dead Ends

- **Reading the 4 GB headline as an Apple Silicon claim.** It is CUDA, and layer streaming is an opt-in beta.
- **Assuming "MPS supported" means the streaming path works on MPS.** Untested.
