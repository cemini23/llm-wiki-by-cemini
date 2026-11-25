---
title: "Refusal Register is Causally Steerable — category-aligned components in Gemma-2-9B-IT (2611.20405)"
type: source
maturity: draft
related:
  - concepts/refusal-and-abstention-direction-geometry.md
  - concepts/local-abliterated-llm-pentest-stack.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** Refusal Register is Causally Steerable: Decomposing the Refusal Direction into Category-Aligned Components in Gemma-2-9B-IT
- **Authors:** Janhavi Khindkar, Nataliia Povarova (independent researchers)
- **Type:** arXiv preprint (cs.CL)
- **Location:** `research to be indexed/cybersec/arxiv-2611.20405-refusal-register-is-causally-steerable-decomposi.pdf`
- **Retrieved:** 2026-11-17
- **arXiv:** 2611.20405v1, 16 November 2026
- **Code:** https://github.com/Jank14/valueshift-icml-2026
- **Read status:** read — 8 pages extracted 2026-11-22

## Narrative

The refusal direction literature asked one question: does a single residual-stream direction control refusal. This paper asks a second question. Does a refusal-related direction also carry information about the register of the refusal, meaning how the model refuses.

The authors test Gemma-2-9B-IT at layer 20. They derive two SVM linear directions, B1 for harmful content against neutral, and B2 for self-reference against neutral. The cosine between them is 0.252, about 75 degrees, so they are not parallel. B1 aligns with the Arditi-style difference-of-means direction at cosine 0.68. B2 aligns at 0.24.

The headline result is a dose-response test. The authors add the harmful-against-neutral direction to self-reference prompts that already refuse. At alpha 2.0, content-safety vocabulary rises from 2.55 to 10.37 hits per 100 tokens. A magnitude-matched random direction gives 1.13 to 2.16. The model still refuses, but it switches from meta-style wording ("as a language model") to content-style wording ("this would be harmful").

The effect reproduces in Gemma-2-2B-IT at layer 12. Content vocabulary rises from 1.72 to 6.37 at alpha 1.0, against a random control of 1.35. The injection window is narrower in the smaller model.

The two directions are not symmetric. Ablating top-K SAE features aligned with B1 selectively reduces refusal in its own category. B2 has a smaller effect in every test: ablation, sufficiency, and injection. The authors read B1 as encoding both category detection and refusal vocabulary. They read B2 as encoding mostly category detection.

Ablation, sufficiency, and injection all agree, and random controls stay clean: 0 of 150 in steering sufficiency, 0.22 off-target in injection at alpha 2.0.

[Source: arxiv-2611.20405-refusal-register-is-causally-steerable-decomposi.pdf]

## Snippets

> "The model continues to refuse but switches register from meta-style ('as a language model. . . ') to content-style ('this would be harmful')."
[Source: arXiv:2611.20405v1 abstract]

> "B1 appears to encode both category detection and refusal-vocabulary information, while B2 encodes primarily category detection."
[Source: arXiv:2611.20405v1 abstract]
