---
title: "Depth-dependent safety geometry in vision-language models"
type: source
tags: [source, arxiv, safety-alignment, multimodal]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Depth-Dependent Safety Geometry in Vision-Language Models: Layer-Wise Localization and Bidirectional Refusal Control |
| Authors | Muhammad Zeeshan Karamat, Syed Talal Hassan, Christiana Chamon — Virginia Tech |
| arXiv | 2610.32182 |
| File | `arxiv-2610.32182-depth-dependent-safety-geometry-in-vision-langua.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32182 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper asks where a vision-language model keeps its safety behaviour, and whether that
location can be steered. The authors use no retraining and no parameter change. They only
read and push activations at inference time.

On Qwen3-VL-4B, an activation-divergence analysis shows the safety geometry is **not
uniform across depth**. Causal interventions then split the depth into two regimes:

- **Early vision layers** give strong bidirectional refusal control through directional
  steering. Unsafe rejection moves across a range of **6% to 96%**.
- **Later layers** respond more to activation-magnitude scaling. They also show a
  substantial safety–selectivity trade-off: a change that strengthens refusal also degrades
  useful behaviour.

The authors report qualitatively similar depth-dependent geometry on InternVL2.5-4B, though
the exact layer and the magnitude differ. From this they argue the pattern recurs across VLM
architectures.

Two claims matter for defenders. First, the paper separates *representational separability*
from *causal controllability*. A layer can encode the difference between safe and unsafe
without giving a clean handle to act on it. Second, the finding exposes a **white-box
representation-level attack surface**. An adversary with weight access can steer refusal
down. The authors use this to argue for inference-time stabilisation of safety-sensitive
representations. All figures are the authors' own; treat them as single-source.

## Snippets

> "Causal interventions show that early vision layers support strong bidirectional refusal control through directional steering, with unsafe rejection spanning 6%–96%." [Source: `arxiv-2610.32182-depth-dependent-safety-geometry-in-vision-langua.pdf` p.1 (arXiv 2610.32182), retrieved 2026-10-27]
