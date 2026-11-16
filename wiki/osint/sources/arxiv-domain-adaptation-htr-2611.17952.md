---
title: "Domain Adaptation Based Pipeline for Character Classification and Handwritten Text Recognition (2611.17952)"
type: source
maturity: draft
related:
  - concepts/htr-domain-adaptation.md
  - sources/arxiv-dra-htr-2611.18143.md
updated: 2026-11-16
---
## Raw Concept

- **Title:** Domain Adaptation Based Pipeline for Character Classification and Handwritten Text Recognition
- **Authors:** Florent Imbert, Simon Corbillé, Hui Han, Elisa H. Barney Smith (Luleå University of Technology)
- **Type:** arXiv preprint, cs.CV
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.17952-domain-adaptation-based-pipeline-for-character-c.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.17952
- **Read status:** full — 20 pages extracted 2026-11-16

## Narrative

Historical handwriting work suffers from scarce labels and abundant unlabelled data. The paper proposes a three-step unsupervised domain-adaptation pipeline: pretrain an expert model on source data, adapt it to unlabelled target data to close the distribution gap, then train the expert on source data rendered in target style.

The claim that matters for cost planning: the extra adaptation compute is spent during training only, not at inference.

Results reported: state of the art on Safran-MNIST-DLS (Track 2 of DAGECC) at 76.17% macro F1, and competitive results on each READ 2018 dataset without using target labels.

Directly relevant to any OCR or archive-digitisation lane, including historical registry work. The pipeline is a general recipe: align feature distributions, then retrain on style-transferred source data.

[Source: arxiv-2611.17952-domain-adaptation-based-pipeline-for-character-c.pdf]

## Snippets

> "The unsupervised training increases the computation time only during training not in inference."

> "We establish a new state-of-the-art on the Safran-MNIST-DLS dataset … with 76.17% Macro F1-score."

## Dead Ends

- **Full-read note (2026-11-16):** The motivating limitation is that supervised models generalise poorly to unseen distributions; the pipeline closes that gap, it does not remove it. [Source: arxiv-domain-adaptation-htr-2611.17952.md full text, 20pp]
