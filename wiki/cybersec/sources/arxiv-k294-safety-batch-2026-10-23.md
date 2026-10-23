---
title: "K294 safety batch — translation bypass, decision sufficiency, and abliteration"
type: source
related:
  - concepts/k294-cybersec-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Type: safety batch, six arXiv PDFs
arXiv: 2610.27304, 2610.27446, 2610.28067, 2610.29342, 2610.29555, 2610.30785
Inbox files:
- `research to be indexed/ccc/arxiv-2610.27304-global-security-blind-spots-translation-as-a-saf.pdf`
- `research to be indexed/ccc/arxiv-2610.27446-decision-sufficiency-of-learned-representation-i.pdf`
- `research to be indexed/ccc/arxiv-2610.28067-contextual-candour-role-aware-graduated-disclosu.pdf`
- `research to be indexed/seo/arxiv-2610.29342-uncensored-is-not-unbiased-abliteration-removes.pdf`
- `research to be indexed/seo/arxiv-2610.29555-wrdo-weighted-refusal-direction-optimization-in.pdf`
- `research to be indexed/osint/arxiv-2610.30785-invisibilization-as-a-source-of-probability-bias.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/<basename>`
Retrieved: 2026-10-23
Read status: skimmed (title and abstract only)

## Narrative

### 1. Global security blind spots (2610.27304)

Jalil Alva and coauthors, Welo Data. Ten models, 79 languages.

Conditioned on safe English completions, mean bypass runs from **21.9%** to **44.4%**.

Nine of ten models change rank across three conditioning schemes that estimate the same quantity. No response changes.

### 2. Decision sufficiency (2610.27446)

Jipeng Li and Yanning Shen, UC Irvine.

On SmolLM2, two selected on/off sparse-autoencoder features raise minimum average loss by **0.0345-0.1166** versus the full state, even with the governing policy supplied. This holds on both autoencoders and both evaluation sets.

The fix is the controller input.

### 3. Contextual candour (2610.28067)

Devansh Srivastav and coauthors, CISPA.

A binary allow-or-refuse gate either over-refuses or leaks. Graduated disclosure sets the level of detail to the user authorisation.

The abstract says the method substantially reduces leakage while keeping correctness. It states no percent. This page adds none.

The paper names https://github.com/Dormant-Neurons/graduated_disclosure. **No clone.**

### 4. Uncensored is not unbiased (2610.29342)

Ju-Chun Ko. Two 2-bit pairs: Nemotron 3.5 Bolt and Qwen3.8-Flash-Next, each against a community abliteration. **22** statement pairs, three scripts.

Bolt Index S: **+0.58** Traditional Chinese, **+0.57** English, **+0.05** Simplified Chinese. The probability of affirming "Taiwan is part of the PRC" is **0.91** in Simplified and **0.06** in Traditional.

Abliteration moves Bolt by at most **0.06**.

On Qwen, abliteration removes every 1989 refusal and raises scores by **0.21** to **0.34**. The abliterated model still affirms the PRC claim in all three scripts. A four-sentence system prompt raises abliterated Qwen to **+0.93** to **+0.97**.

In **740,000** web documents, Simplified text on Taiwan contained PRC-framing terms **3.7 times** as often as Traditional text.

Abliteration is not debiasing. **No install.**

### 5. WRDO (2610.29555)

Grigoriy Evseev and coauthors.

WRDO learns weights over per-prompt refusal directions instead of one difference-of-means vector. The same machinery run in reverse tries to restore refusal on an abliterated checkpoint.

The abstract states no headline percent. This page adds none.

Code URL in the paper: https://github.com/brain-lab-research/WRDO. **No clone.**

### 6. Invisibilization (2610.30785)

Christian Arnold and coauthors.

Models refuse or hedge when a protected attribute is in the prompt. The refusal rate depends on the description rather than the evidence.

Telling the model to be careful raises the refusal rate. Scoring trust against verified outcomes lowers the rate at which the model drops the report.

The widest gap in the abstract is cut off in this skim. This page states no rate for any named group.

No install. No PoC.
