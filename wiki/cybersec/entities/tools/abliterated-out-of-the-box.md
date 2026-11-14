---
title: "AbliteratedOutTheBox — inference-time refusal removal for llama.cpp"
type: entity
related:
  - sources/newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/decoy-hardening-open-weight-abliteration.md
  - concepts/owned-target-whitehat-lab.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: tl;dr sec #354 listed the project in its quick links. This page records the method for the local whitehat lab. It does not endorse deployment outside an authorised lab.

## Narrative

AbliteratedOutTheBox is a fork of `llama.cpp`. It suppresses refusals at inference time without changing model weights and without retraining.

### Method as described

1. Force the model to produce both a compliant response and a refusal response for the same prompt.
2. Compute the activation difference between the two.
3. Use a look-ahead gate to detect a refusal forming during generation.
4. Project the activations away from the refusal direction as generation continues.

This is a runtime form of the abliteration technique, applied through the sampler rather than through weight editing.

### Why it fits the local lab

The local abliterated stack exists to run security tooling without provider filters. This approach adds one option with no separate checkpoint to manage. The trade-offs are the usual ones: unmeasured capability loss, no audit trail of the steering, and a fork that must track upstream `llama.cpp`.

### Measured caution

An independent comparison of an abliterated model against its base reported 26% fewer findings in source analysis, no gain in exploit development, and more autonomous post-exploitation behaviour. That result is for a weight-abliterated model, not for this fork. It supports one rule: measure before and after, and do not assume the base model's judgement survives.

### Status

`[OPEN QUESTION 2026-11-14]` Not tested in this workspace. Licence, upstream sync cadence, supported quantization formats and behaviour under long contexts are unverified.

### Related

See @concepts/local-abliterated-llm-pentest-stack.md for the surrounding stack decisions, and @concepts/owned-target-whitehat-lab.md for the authorisation boundary.
