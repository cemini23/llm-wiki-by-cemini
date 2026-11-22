---
title: "Generalization of text-line segmentation for historical-document HTR"
type: source
maturity: draft
related:
  - concepts/htr-segmentation-generalization.md
  - concepts/gpuology-genealogy-agent-kit.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Generalization of Text Line Segmentation for HTR in Historical Documents |
| Author | Gayan H. Pathirage, Stephan M. Unter, Simon Corbillé, Elisa H. Barney Smith |
| Type | arXiv preprint, computer vision |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.24726-generalization-of-text-line-segmentation-for-htr.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.24726v1, 18 Nov 2026 |
| Pages | 12 |
| Read status | read |

## Narrative

Text-line segmentation is the step before recognition in most HTR pipelines: find the lines on a page, then transcribe each line. Museums and archives cannot label large samples for every new collection, so the question is how well detector models transfer.

The authors test three object detectors, Hi-SAM, YOLO and RT-DETR, on nine datasets that differ in layout and language. They also test few-shot fine-tuning with a small number of labelled lines per target dataset. [Source: arxiv-2611.24726-generalization-of-text-line-segmentation-for-htr.pdf p.1]

The downstream measure is character error rate of a CRNN recogniser on the segmented lines. Depending on the dataset, CER ranges from 2.48% to 7.07% per page. The authors argue this is enough for reading comprehension and simple text search.

Two points are useful beyond the benchmark. First, mean average precision (mAP) is an insufficient metric for line segmentation; it does not track recognition quality. Second, the paper reports training and inference resources for each setting, so a reader can pick a model against real hardware.

For the genealogy pipeline, this is directly relevant. Segmentation quality caps transcription quality on noisy civil and parish records. The practical recipe: use a detector that transfers, fine-tune with a few labelled lines per archive, and judge the result with CER, not mAP.

## Snippets

> "Depending on the dataset, our CRNN models achieve character error rates (CER) ranging from 2.48% to 7.07% per page for the segmented text lines." [Source: arxiv-2611.24726-generalization-of-text-line-segmentation-for-htr.pdf p.1]
