---
title: "MAEM — interpreting any residual-stream direction by scaling activation inversion (arXiv:2611.08465)"
type: source
tags: [source, arxiv, interpretability, activation-steering, lora, safety]
keywords: [MAEM, maximally activating example metamodel, activation inversion, residual stream, SAE features, steering vectors, LoRA backdoor, NLA, Qwen3.6-27B]
related:
  - concepts/activation-inversion-metamodels.md
  - concepts/activation-steering-video-generation.md
  - concepts/lora-weight-fingerprint-moderation.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Towards Interpreting Any Residual Stream Direction by Scaling Activation Inversion |
| Author | Celeste De Schamphelaere (MATS), Juan J. Vazquez, Ari Spiesberger, Tomáš Gavenčiak, Gavin Leech (Arb Research), Euan Ong, Jiahai Feng (Anthropic) |
| Type | arXiv:2611.08465 [cs.LG], 50 pages |
| Location | `research to be indexed/image-gen/arxiv-2611.08465-towards-interpreting-any-residual-stream-directi.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08465-towards-interpreting-any-residual-stream-directi.pdf` |
| Read status | read (abstract, method, results summary) |

## Narrative

An interpretability method with one clean and verifiable objective: given a direction in a model's residual stream, write text that strongly activates it.

**The method.** A MAEM is a fine-tune of a frozen language model. It takes a residual-stream direction as input and outputs text. The reward is the maximum cosine similarity between the input direction and the subject model's activations on the generated text. The loop is label-free, so a MAEM can train on any direction — natural activations, SAE features, steering vectors, or a weight-diff direction.

**Why the objective is better.** Most readers of an activation return a description. A description needs a human or model judge to check, and it can only carry concepts the reader has words for. A generated exemplar is checkable by one forward pass on the frozen subject model: either it fires the direction or it does not.

**Reported results.** A Qwen3.6-27B MAEM:

| Task | Result |
|---|---|
| Invert held-out activations | better than corpus search or an NLA |
| Beat corpus search at 10M tokens | majority of held-out languages and domains |
| Fire held-out SAE features (batch of eight) | 89% |
| Explain steering vectors | about as well as NLAs |
| Recover rank-1 LoRA backdoor payload | more often than corpus search |

The LoRA row is the most interesting for this wiki. A rank-1 backdoor that maps "hopeful" to a trigger phrase leaves a read direction and a write direction in the weights. The MAEM verbalises each, so the payload can be read without guessing.

**Stated limitations.** 6.5% of SAE features were never fired. Sample diversity is lower than corpus exemplars. An automated explainer using MAEM exemplars described features worse than one using corpus windows, and was on par with an NLA.

**Relevance to image generation.** Direct relation to diffusion work is indirect. The shared object is the LoRA adapter. Persona work trains many small LoRAs from users, marketplaces and third parties. A method that reads what a rank-1 adapter does, and states it in text, is a moderation primitive. It is also a way to read what an activation-steering direction in a text encoder does.

**Caveat.** Results are for language models. Nothing here was tested on a CLIP or T5 text encoder, or on a DiT. Transfer is plausible but untested [OPEN QUESTION 2026-11-10].

## Snippets

> "It also identifies concepts behind steering vectors about as well as NLAs, recovers the payloads of LoRA backdoors more often than corpus search, and can even verbalise some model workspace inner monologue." [Source: arxiv-2611.08465 p.1]

> "Unlike explanations produced by other metamodels (e.g. NLAs), MAEM exemplars can be verified with a forward pass on the subject model, making the MAEM objective a grounded alternative for scaling the training of metamodels." [Source: arxiv-2611.08465 p.1]

## Dead Ends

- **Assuming MAEM exemplars improve automatic explanation quality.** The paper reports the explainer was worse than one fed corpus windows, and level with an NLA.
