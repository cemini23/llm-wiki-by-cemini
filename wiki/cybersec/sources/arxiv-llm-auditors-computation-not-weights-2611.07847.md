---
title: "Computation, not weight access: LLMs as auditors of clinical prediction networks (arXiv 2611.07847)"
type: source
related:
  - concepts/llm-audit-computation-not-weight-access.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Computation, not weight access: large language models as auditors of clinical prediction networks |
| Author | Zhiyu Liu (Tianjin Medical University); Xinyu Yang (Tianjin Medical University General Hospital) |
| Type | arXiv preprint (cs.LG) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf` |
| Retrieved | 2026-11-06 |
| File | `arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf` |
| Pages | 13 |
| Read status | read |

## Narrative

The paper separates two claims that earlier work mixed. The first claim is that a large language model (LLM) can read the **raw weights** of a small neural network and say what the network was trained to do. The second claim is that an LLM can **compute with** the network by writing and running code. The authors hold the network fixed and vary the access mode. They find that computation and task elicitation carry the result, and that weight access does not.

### Design

The authors train tanh multilayer perceptrons on simulated cohorts of 20,000 adults with aneurysmal subarachnoid haemorrhage. Network sizes run from 105 to 38,401 weights. Each network carries a planted relationship (a threshold, an interaction, a half-strength version of either) or no relationship. One 209-weight network is trained on labels that under-record deaths among women farmers over 65.

Five GPT models take part. GPT-6 Astra is the main model; gpt-6.1-sol, gpt-6-sol, gpt-6-luna and gpt-5.6-sol are comparators. Each run is one prompt and one reply. A script scores every reply against the known ground truth with rules written before the runs. The plan and scoring code were committed to a repository before the first run.

Three access modes are compared. In the first mode the weights sit in the prompt and every tool is disabled. In the second mode a calculation-only tool holds the weights (white box). In the third mode the same tool exposes only the network's predictions (black box).

### Results

**No tool.** Astra recovered the planted relationship in all six runs on 353-weight networks. At 3,457 weights the result became unstable and repeats differed widely. The failing replies explained themselves: the model could not run the numerical sweep it planned, so it linearised the network around a midpoint.

**Default instruction produced refusals.** Under the one-sentence default instruction, 11 of 12 audit and repair runs declined the task. Astra argued that a distortion is not identifiable without a reference. The argument is correct mathematics but answers a different question. One paragraph of explicit instruction removed 11 of 12 refusals, and raised no false alarm in the controls.

**With the calculator.** Astra recovered the planted relationship in all 29 runs that had one, on networks from 353 to 38,401 weights. It raised no false alarm in 15 runs on null networks. It found the biased subgroup in 6 of 6 runs. Median run time was 12 minutes with 7 to 14 tool calls.

**Access made no difference.** In 18 black-box runs, strength ratios and R² matched the white-box runs cell by cell.

**A script matched the comparators.** An exhaustive search with prediction access found the subgroup in under a second. The authors designed the search space with knowledge of the answer, so the script is not a fair general baseline. Still, the LLM's added value sits in designing and running the audit, not in a capability beyond a well-specified script.

### Defensive reading

The result is a measurement finding for model auditing. White-box weight access is not required to audit what a small network computes, once the auditor can run code against it. An auditor that must be given raw weights is a weaker requirement than it appears, and a claim of "native weight reading" is not supported at scale.

The second finding is about elicitation. A default system instruction produced refusals framed as non-identifiability. The refusals were technically defensible and operationally useless. Security tooling that depends on a model choosing an unstated option needs an explicit instruction to choose.

## Snippets

> "With the tool, it recovered the planted relationship in all 29 runs on networks of up to 38,401 weights, raised no false alarm in 15 runs on null networks, and found the biased subgroup in 6 of 6 runs. Black-box access performed as well as white-box access." [Source: arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf p.1]

> "Under the default instruction, 11 of 12 audit and repair runs declined (95% interval 0.65–0.99)." [Source: arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf p.6]

> "For auditing these networks, what mattered was computation and elicitation, not access to the weights." [Source: arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf p.1]
