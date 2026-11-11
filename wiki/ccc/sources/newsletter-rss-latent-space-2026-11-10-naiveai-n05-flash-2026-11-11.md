---
title: "Naive-N0.5-Flash — 2,100 tokens/sec, and a model trained to do AI research"
type: source
tags: [source, newsletter, models, coding, open-weights, speed]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | NaiveAI promises 2,100 tokens per second — how well does it work? |
| Source | latent-space (new review series) |
| Published | 2026-11-10 |
| Read status | skimmed (opening) |

## Narrative

A new review series, and the first subject is chosen for a specific claim: **2,100 tokens per second**.

**Naive-N0.5-Flash** is an **open-weights** model built for AI coding tasks, tuned to generate as many tokens per second as possible, from a Chinese company called NaiveAI. It is an evolution of **Xiaomi's MiMo-V2.5** — a **310B-parameter sparse MoE with 15B active**, trained on 48T tokens, whose language backbone mixes sliding-window attention with global self-attention — trained further for long-context reasoning and paired with NaiveAI's own **NaiveRT** inference engine.

### The claim worth separating from the number

The pitch is not only speed: it is **"a model built largely by AI and trained to do AI research itself, with recursive self-improvement as the long-term goal."**

That is a different claim from tokens per second, and the two should not be read together as one result. A fast model that does research is two claims; either can hold without the other.

**Tokens per second is a throughput number, not a capability number.** For an agent doing long tool loops, throughput matters — it is time-to-completion. For a reviewer, what matters is whether the output is right.

### Why it is filed here

It is the first entry in a review series the newsletter frames as unbiased, and the model is open-weights — the class this workspace can actually run. Worth tracking for local coding-agent use.

**Caveat.** Opening section only. No benchmark from the review itself is captured here.

## Snippets

> "A model built largely by AI and trained to do AI research itself, with recursive self-improvement as the long-term goal." [retrieved 2026-11-11]

## Dead Ends

- **Reading 2,100 tokens/sec as a quality claim.** It is throughput.
