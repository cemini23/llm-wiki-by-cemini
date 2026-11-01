---
title: "Elorian Glimpse and the DecoyCount visual-reasoning benchmark"
type: source
tags: [source, newsletter, visual-reasoning, benchmarks, agents]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Can Frontier Models See Past a Decoy? Elorian Tests Visual Reasoning |
| Source | Latent Space |
| File | `newsletter-rss-latent-space-2026-10-29-can-frontier-models-see-past-a-decoy-elorian-tes.md` |
| Retrieved | 2026-11-01 |
| URL | https://latent.space/p/elorian/ |
| Read status | read |

## Narrative

Latent Space reports that Elorian launched its first visual reasoning model, Glimpse. The company promotes Glimpse as a visual thinking model that reasons about the physical world from what it sees. The newsletter says Elorian emerged from stealth in April with $55 million in seed funding, co-led by Striker Venture Partners, Menlo Ventures, and Altimeter Capital. That funding figure is a single-source claim. CEO Andrew Dai co-authored the 2015 paper "Semi-supervised sequence learning" with Quoc Le. He then worked at Google DeepMind on GLaM MoE, PaLM 2, and Gemini, and left Google this year to co-found Elorian.

With the AI data company Mercor, Elorian announced the DecoyCount benchmark. The benchmark tests whether language models count objects, or rely on visual shortcuts and substitution heuristics. The source says DecoyCount exposes interpretable counting failures across seven mechanisms. Dai uses a mirror example. A person sees one apple and its reflection. A model can miss the apple, which is a vision failure, or count the apple and the reflection as two, which is a reasoning failure. Most benchmarks check only the final number, so both failures look the same.

The paper that accompanies the release, as quoted here, says frontier models scored below 50% accuracy on DecoyCount. The highest score in that paper was GPT-6 Astra at 43.17%. The paper concludes that stronger general reasoning does not by itself generalize to aligned visual reasoning. These paper figures are single-source claims in this newsletter. The paper omits Glimpse.

Dai told Latent Space that an internal test scored Glimpse at 50.48% on the 1,660 DecoyCount items. He said the evaluation images and text were withheld from training, and a contamination check found no overlap in the training data checked. He named Gemini-3.8-flash at 32.71%, Qwen3.8-max at 28.31%, and Claude-Fable-5.1 at 25.22%. He said Glimpse was the only model in the comparison to clear 50%, and that GPT-6 Astra at 43.17% was about 7 points behind. These scores come from one email in this newsletter. Dai said the Glimpse result is a single run of the model on its own, without an agent or tool harness. The six models in the paper were each averaged across three runs under their reported settings.

Dai describes visual thinking as generating images and editing images inside the reasoning trace, along with language. The generated or edited image is part of the chain of reasoning. He places this next to world models such as World Labs Atlas, announced in September and subsequently acquired by AMD, and Google Genie 4. He says world models enable direct action on a world. Glimpse targets indirect action: visual reasoning that informs a decision or a workflow, such as a policy check on a user-contributed video.

The newsletter names robotics, engineering, defense, and building-code checks as uses. On the robotics benchmarks WGO Bench and ERQA, Elorian claims a rating equal or higher than frontier models, at a much cheaper price. The newsletter prints no scores for those two benchmarks. A warehouse example says a familiar 12-slot tray might hold only 10 parts, and a 24-pack label does not mean 24 items remain in the box. Glimpse is designed to ground the count in visible evidence. The Glimpse launch post says a full stack built for multimodal intelligence can unlock AGI in the physical world. Dai says a large gap remains between humans and machines, and he treats visual reasoning as a required step toward AGI. For an agent-harness reader, the run protocol is the operational point in this source. Glimpse used one run, with no agent or tool harness. The six paper models each used a three-run average under their reported settings. The source also says a final count hides whether a failure is vision or judgement, while Glimpse puts image generation and image editing inside the reasoning trace. Every number above comes from this one newsletter.

## Snippets

> "Without any cues, Glimpse scored 50.48% on the 1,660 DecoyCount items, making it the only model in the comparison to clear 50%. The closest was GPT-6 Astra at 43.17%, about 7 points behind, and Gemini-3.8-flash scored 32.71% while Qwen3.8-max scored 28.31%, and Claude-Fable-5.1 came in at 25.22%." [Source: https://latent.space/p/elorian/ (retrieved 2026-11-01)]
