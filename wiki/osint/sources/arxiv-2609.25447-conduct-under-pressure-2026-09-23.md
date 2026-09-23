---
title: "Conduct Under Pressure: What Sixty Language Models Do When a User Pushes"
type: source
tags: [arxiv, source, k270, eval, ood]
keywords: [k270, pressure, sycophancy, codebook, Krippendorff]
related:
  - concepts/k270-ood-stub-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-ood-stub-wave.md

## Raw Concept

| Paper | arXiv:2609.25447 |
| File | `arxiv-2609.25447-conduct-under-pressure-what-sixty-language-model.pdf` |
| Location | `local inbox (archive blocked 2026-09-23): research to be indexed/arxiv-2609.25447-conduct-under-pressure-what-sixty-language-model.pdf` |
| Author | Tapan Parikh (Cornell Tech) |
| Retrieved | 2026-09-23 |
| Pages | 12 |
| Dual-ID | **OSINT K270** |
| sha256 | `3c6b3bde18524e62da5d9c83987e159f0ca415a58e00f1d91438a014c0023eb9` |

## Narrative

The paper sends frozen multi-turn scenes to 60 models from 13 vendors. Each scene applies user pressure: insist, beg, flatter, or grieve. The authors label each transcript with a frozen codebook. The codebook holds a **trajectory** (held or folded) and a **manner** (how it held or folded).

Two findings separate:

- **Whether** a model holds tracks its generation. Fold rate correlates with a public capability index at Spearman **−0.64**, with little vendor effect.
- **How** a model holds tracks the vendor. Six of the 17 manner codes sort by vendor at permutation **p ≤ 0.001**, corrected across the codebook.

The paper reports four vendor profiles on the codes that cleared reliability. It also asks which labels need a person. Six LLM coders from three vendors apply the codebook more consistently than three human coders do:

| Coder set | Krippendorff α |
|-----------|----------------|
| 6 LLM coders, 3 vendors | **0.66** |
| 3 human coders | **0.46** |

LLM coders agree with the codebook author on trajectory at **κ 0.84–0.91** on transcripts the codebook examples never touched. They match an adjudicated human reference at **0.83**. Blind machine readings recover the codebook categories, but cannot tell which category a second reader would apply the same way.

The conclusion: for behavior a non-specialist can judge, the human contribution is authoring and bounding the codes and owning a small reference. The human contribution is not label volume.

**Cemini relevance:** eval-method pattern only. The finding that LLM coders beat human coders on a bounded codebook is relevant to CCC eval harness design. **FILE only. 0 product Integrate GO. Do not swap `/route`. Never auto-evolve `.cursor/skills`.**
