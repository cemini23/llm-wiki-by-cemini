---
title: "Inkling 2 Mini — local multimodal VLM at ~20 GB (Apache-2.0)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@cybersecurity-wiki/concepts/open-weight-abliterated-models-2026-11.md"
  - concepts/local-inference-runtimes.md
updated: 2026-11-22
maturity: draft
---
## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md, URL 13,
**Integrate** tier. Routed to Collectibles and Atto.

The question this page answers: **can a laptop replace a rented GPU for image reading?**

## Narrative

### What it is

An open-weight, natively multimodal model from Thinking Machines Lab, released
2026-11-20.

- **Architecture** — 24-layer looped MoE; the middle 12 layers run three passes, for 48
  layer applications.
- **Parameters** — 26.4B total, 3.4B active, 5.4B effective active.
- **Context** — 1M tokens.
- **Images** — 40 px to 4096 px, native.
- **Footprint** — ~20 GB checkpoint at native NVFP4/MXFP8; smallest GGUF ~17.5 GB.
- **Runs on** — 32 GB+ Apple Silicon (Ollama, MLX, llama.cpp) or 32 GB+ VRAM (vLLM,
  SGLang).

**Apache-2.0**, with a separate Acceptable Use Policy.

### Published numbers

Thinking Machines reports under-100B open-weight best scores: DeepSWE v1.1 48.2%,
SWE-bench Verified 79.2%. Independent Artificial Analysis testing reports 20 on the
Intelligence Index at $0.59 per task against Qwen3.8-27B's $3.53, and 9.0 minutes
against 38.2.

[CONFIRMED — vendor and independent figures reported; not re-measured here]

The cost and latency figures are the interesting ones. They imply the looped-MoE
structure buys throughput at a given quality, not just quality.

### Why it matters for Collectibles

Collectibles currently reads card images through a **RunPod cloud worker**
(`runpod/runpod_worker.py`). [CONFIRMED — local repository check 2026-11-22]

That is a per-image cost and an off-box transfer of collector images. A 4096 px-capable
local VLM at ~20 GB removes both, and satisfies the existing "card images stay local"
rule by construction rather than by policy.

Bulk 2027 NJ collection cataloguing is exactly the workload where a per-image cloud
charge compounds.

### Why it matters for Atto

Atto has no local multimodal model. An offline mode backed by this model gives a
privacy-first option for genealogy customers on 32 GB machines — no image egress, no
API key, no per-page charge.

That is a product differentiator, not just a cost saving: "your documents never leave
the machine" is a claim the paid tiers can carry.

### The caution

A 20 GB model on a 32 GB machine leaves 12 GB for everything else. It runs, but not
alongside a second large model or a heavy browser session. Benchmark on the target
machine before promising the workflow.

### Status

Integrate. Queued for Collectibles and Atto.

## Snippets

> Open-weights natively multimodal (text + images 40px–4096px) 24-layer looped MoE
> transformer (26.4B total, 3.4B active, 5.4B effective active; 1M token context).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 13]

## Dead Ends

- **Assuming 32 GB is comfortable.** A 20 GB model leaves 12 GB for the OS and the app.
- **Promising offline mode without measuring tokens per second on the target Mac.**
