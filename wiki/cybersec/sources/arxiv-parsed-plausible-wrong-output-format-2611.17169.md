---
title: "Parsed, Plausible, Wrong: output format controls silent errors in small-model parsing (arXiv 2611.17169)"
type: source
related:
  - concepts/silent-error-rate-structured-output.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - sources/arxiv-nfr-to-hyperparameter-quantum-2611.16902.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing |
| Author | Umar Ahmed; Maxim Dunaev; Mohammad Nour Al Awad; Sergey Ivanov; Ivan Khodnenko (ITMO University) |
| Type | arXiv preprint (cs.CL), 2611.17169v1 |
| Location | `research to be indexed/cybersec/arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf` |
| URL | https://arxiv.org/abs/2611.17169 |
| Retrieved | 2026-11-13 |
| Pages | 10 |
| Read status | read |
| Code | https://github.com/UmarGit/coffee-llm |

## Narrative

A small parser that emits a well-formed but wrong tree fails silently. Nothing downstream can tell. The paper asks whether the **output format**, a free design choice, controls how often this happens.

### The four-way outcome split

Every test order ends in exactly one of four states:

| Symbol | Outcome | Visible to the caller |
|---|---|---|
| A | Correct (exact match) | yes |
| S | **Silent** — parses, does not match | **no** |
| D_parse | Does not parse | yes |
| D_refuse | Refuses a real order | yes |

The paper treats **S as the deployment objective**. A retry loop absorbs `D_parse`. A human fallback absorbs both parse and refuse. Nothing absorbs S, because the caller cannot see it.

### Design

Six lossless encodings of the same target tree, on the PIZZA ordering benchmark. The ladder runs from 44.3 tokens (s-expression) down to 10.9 tokens (plain words). Two matched-length pairs separate length from surface form. Models are Qwen3.5-0.8B and LFM2.5-350M with LoRA. The grid is 300 runs: 6 formats, 5 pool sizes, 5 seeds, 2 models. Statistics were fixed before the results were read.

### Results

Shortening alone never helps. Renaming constructors to single letters (EXR-SHORT) costs **10.6 points** on Qwen at every pool size. The plain-words encoding (WORDS) is the most accurate and the least silent:

| Metric | EXR (native) | WORDS |
|---|---|---|
| Exact match, Qwen | 85.8% | **87.5%** |
| Silent rate, Qwen | 10.3% | **4.5%** |
| Silent rate, LFM2 | 17.9% | **10.0%** |
| Output tokens, Qwen | 44.3 | 10.9 |
| Median latency, Qwen | 1,171 ms | 317 ms |

The silent-rate reduction is 2.3× on Qwen and 1.8× on LFM2, and it separates at every pool size. WORDS also invents 5.5× fewer entities than EXR on Qwen.

### Where the gain comes from

Negation is the largest error class that WORDS removes. A silent negation error happens on 2.0% of orders with EXR and 0.2% with WORDS on Qwen. The symbolic formats write "no onions" as a NOT construct or a sigil. WORDS writes it the way a customer says it.

WORDS still fails on line count: 36% of its remaining silent errors on Qwen.

### The guardrail has a price

Every run trains a refusal guardrail and a self-correction behaviour. Held-out negatives are refused 95.9–99.0% of the time. The price is real: **2.1–10.1% of genuine orders are refused**. The refused orders are mostly polite human phrasing that the training grammar never produces. An order that contains "please" or "thanks" is refused more often.

### Defensive reading

If a machine acts on parsed output without review, the silent error rate is the number to minimise. Exact match is the wrong ranking when it ignores S. Report all four outcomes, because the trade between them is the design decision.

Two format rules transfer. First, keep the target vocabulary natural and compress the structure. Second, do not assume that fewer tokens means fewer errors. Constrained decoding removes `D_parse` and cannot touch S.

This is a general control-design rule for agent tool calls. A tool argument that parses but carries the wrong value is the dangerous case. Validate the value against the request, not only the schema.

### Limits

One task, one benchmark, two sub-billion models. The authors state that persistence at larger models and other tasks is open. The four-way split is reusable; the size of the format effect is not yet established elsewhere.

## Snippets

> "A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.1]

> "Shortening alone never helps, but writing the target in ordinary words does." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.1]

> "Constrained decoding makes invalid output impossible … it cannot make a well-formed tree correct, so the silent rate is the part of the problem it does not reach." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.2]

> "A format with higher A but higher S ships more wrong orders." [Source: arxiv-2611.17169-parsed-plausible-wrong-output-format-controls-si.pdf p.6]
