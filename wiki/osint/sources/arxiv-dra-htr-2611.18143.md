---
title: "DRA-HTR: Disentangling Representation and Adaptation for Handwritten Text Recognition (2611.18143)"
type: source
maturity: draft
related:
  - concepts/htr-domain-adaptation.md
  - sources/arxiv-domain-adaptation-htr-2611.17952.md
updated: 2026-11-16
read_status: read
---

## Raw Concept

- **Title:** DRA-HTR: Disentangling Representation and Adaptation for Handwritten Text Recognition
- **Authors:** Gayan H. Pathirage, Florent Imbert, Denis Coquenet, Elisa H. Barney Smith
- **Type:** arXiv preprint
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.18143-dra-htr-disentangling-representation-and-adaptat.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18143
- **Read status:** full — 20 pages extracted 2026-11-16

## Narrative

Extends the DRANet line to handwriting. Source-domain pretraining, unsupervised adaptation to the target's visual style by generating target-style source samples, then task-specific training on those samples.

The paper adds a second layer, DRAL-HTR: post-OCR correction with a large language model, treating language adaptation as complementary to visual adaptation.

Reported across seven HTR datasets in four languages with one hyperparameter set: state of the art on four datasets and competitive on three. Against the original DRANet it reports an average Character Error Rate reduction of 13.52 percentage points, and average standard deviation across runs falling from 7.23 to 1.11 points. Post-OCR correction takes a further 2.16 points.

The stability number is the interesting one. A method that works on four of seven datasets with one configuration, and whose run-to-run spread collapses by 6 points, is easier to operationalise than a higher peak score.

[Source: arxiv-2611.18143-dra-htr-disentangling-representation-and-adaptat.pdf]

## Snippets

> "it reduces the Character Error Rate (CER) in average by 13.52 percentage points, and the average standard deviation decreases from 7.23 to 1.11 percentage points."

## Dead Ends

- **Full-read note (2026-11-16):** The limitation that motivates the method: labelled historical data is scarce, so adaptation must exploit unlabelled target data. [Source: arxiv-dra-htr-2611.18143.md full text, 20pp]
