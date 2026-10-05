---
title: QUEEN — a chess model that plays grandmaster-level and explains its moves (2026-10-05)
type: source
tags: [source, arxiv, game-ai, llm, model-architecture, reference]
keywords: [queen, chess, expert-encoder, cross-attention, bellman-distillation, explainable-agent]
related:
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/rts-siege-ai-reference.md
  - concepts/agent-harness-castle-project.md
  - sources/inbox-arxiv-reject-batch-2026-10-05.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.03695
maturity: validated
created: 2026-10-05
updated: 2026-10-05
---

## Raw Concept

**arXiv:2610.03695** — **QUEEN** is a 4B-parameter chess-language model from Princeton Language and Intelligence. The problem it addresses: chess engines play superhumanly but explain nothing, while language models explain plausibly but play weakly. QUEEN plays at the level of a typical Grandmaster AND explains its moves. Authors: Adithya Bhaskar, Jeffrey Cheng, Danqi Chen.

## Narrative

### Architecture [CONFIRMED]

An encoder-decoder design. The **encoder is a silent chess expert** — Leela, a 240M-parameter encoder-only model (BT5, 15 layers). The **decoder is an instruction-tuned LM** — SmolLM3-3B. **Gated cross-attention** layers (inspired by Flamingo) connect them. 16 cross-attention blocks pair the i-th encoder hidden state with the 2i-th decoder hidden state, placed before every other decoder layer, so multi-scale board features accumulate into the residual stream. They tested 3 bridge architectures and 3 decoder families (SmolLM3, Qwen, Gemma at similar scale) and chose SmolLM3-3B.

### Training [CONFIRMED]

A **domain-adaptation curriculum** teaches the decoder to extract chess concepts from the encoder's latent representations. A question-answering curriculum asks progressively harder questions (position, future position after 1-8 moves). The encoder and decoder start frozen; only the cross-attention bridge trains in that stage, with LoRA needed on the decoder to get meaningful results. Then **iterative distillation**: a natural-language analog of the **Bellman update**. The model analyzes the positions after its top candidate moves and consolidates them into an explanation of the current position, which is distilled back into the model. Over **seven iterations** the model gains **over 900 Elo (1782 → 2697)**.

### Results [CONFIRMED]

It substantially surpasses all frontier models on both playing strength and puzzle accuracy, with **three orders of magnitude fewer parameters**. LM-based evaluations show its explanations are fluent and approach GPT-5.6-Sol (high) in coherence. Training data includes the Lichess database (https://database.lichess.org/).

### castle-sim / game-AI relevance [CONFIRMED]

Map to @concepts/game-ai-rl-augmentation-shelf.md and @concepts/stronghold-2-ai-lords.md. Two transferable ideas. First, the **silent-expert-plus-explainer** split: a fast hand-coded policy can stay authoritative (like a JSON-weighted lord director) while a smaller language model is trained only to interpret its state and produce an explanation. That gives an AI lord that plays by readable rules AND can explain why, without making the LLM the decision-maker. Second, the **domain-specific small model beats frontier models at the domain** — relevant to any local NPC model plan. Note the caveat that this is chess, a perfect-information game with a strong expert encoder available.

### Caveat [TENTATIVE]

The recipe needs a strong expert encoder to exist for the domain, and chess has one. Castle-sim's lord director is not at that level, so the "silent expert" half of the recipe is the missing piece. The paper itself notes the approach generalises to "games, robotics, and computer use" where expert encoders exist — a claim, not a demonstrated result for RTS.

### Phase-0 [CONFIRMED]

The paper shows Code and Website links as icons; no repository URL resolves in the text. No artifact to clone-audit. **STEAL-FROM (pattern only).**

## Dead Ends

- Replacing the hand-coded lord director with a language model.
- Expecting the distillation recipe to work without an expert encoder.
