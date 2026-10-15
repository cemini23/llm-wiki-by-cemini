---
title: "CT0 — Cybersecurity Transformer"
type: source
tags: [arxiv, specialist-model, on-policy-distillation, detection, agent]
keywords: [cybersecurity transformer, alias3-micro, confidence gate, IoC screening, cybench, tiny model]
related:
  - concepts/k291-cybersec-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-cybersec-wave.md — K291 cybersecurity wave hub

## Raw Concept

Title: CT0 — Cybersecurity Transformer
Author: Víctor Mayoral-Vilches (Alias Robotics)
Type: arXiv preprint (2610.16550)
Location: `research to be indexed/cybersec/arxiv-2610.16550-ct0-cybersecurity-transformer.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The question inverted:** not how large a model can be, but **how small a cybersecurity-specialist transformer can be while staying useful to a practitioner**. Answer: **~4B parameters** (`alias3-micro`), on an open Qwen3.5-4B base, specialised by two-phase on-policy distillation on the author's Cybersecurity AI dataset.

**One set of weights, two modes:**
- **System 1** — typed security decisions (is this file suspicious, is this request an attack, did the model just refuse) in a **single forward pass, generating no token**.
- **System 2** — the usual tool-using agent.
- A **confidence gate** spends generation only where the fast path is unsure.

| Measure | Value |
|---|---|
| cybench-subtask (agentic) | **21.1%** vs 7.6% base |
| IoC screening | **80 files/sec** |
| Own-refusal detection | **96.5%** at 47 ms (self-judging: 76.5% at 254 ms, missing half) |
| Jailbreak flagging | **AUROC 0.966** at 8 ms |
| Build cost | ~**314 RTX PRO 6000 GPU-hours**; served from one workstation GPU |

Extracts vulnerability facts more accurately than either mode alone **at a fifth of the generative cost**. Reported across eighteen benchmarks and use cases, with explicit notes on where the design does **not** help.

**Why it is filed here:** the **confidence gate** — generate only for what the fast path is unsure about — is the reusable architecture. Also notable: **the model catches its own refusals far better than a model judging itself**, at a sixth of the latency.

## Snippets

> "how small can a cybersecurity-specialist transformer be while remaining genuinely useful to a security practitioner?" [Source: arxiv-2610.16550 p.1]

> "catches its own refusals at 96.5% accuracy in 47 ms where the model judging itself reaches 76.5% in 254 ms and misses half of them." [Source: arxiv-2610.16550 p.1]

> "All of it is built in about 314 RTX PRO 6000 GPU-hours and served from one workstation GPU." [Source: arxiv-2610.16550 p.1]

## Dead Ends

- Assuming 4B is the ceiling for the architecture. The paper asks how small a *specialist* can be, not how small a cybersecurity model can be in principle.
