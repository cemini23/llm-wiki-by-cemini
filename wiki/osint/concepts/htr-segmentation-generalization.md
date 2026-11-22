---
title: HTR for historical records — segmentation transfer and dataset-distillation limits
type: concept
maturity: draft
related:
  - sources/arxiv-text-line-segmentation-generalization-2611.24726.md
  - sources/arxiv-dataset-distillation-htr-2611.21054.md
  - concepts/gpuology-genealogy-agent-kit.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: what do two 2026 HTR papers say about building a low-cost transcription pipeline for civil and parish records?

Built from arXiv 2611.24726 (text-line segmentation, 2026-11-18) and arXiv 2611.21054 (dataset distillation for HTR, 2026-11-18).

## Narrative

**The pipeline.** Historical-document HTR is usually two steps: segment the page into text lines, then transcribe each line with a recogniser. Archives cannot label a large sample for every new collection, so both steps must transfer.

**Segmentation transfers, from a few labels.** Three object detectors (Hi-SAM, YOLO, RT-DETR) were tested on nine datasets with different layouts and languages, and with few-shot fine-tuning. Downstream character error rate on the segmented lines ranges from 2.48% to 7.07% per page. Two practical rules come out of it:

- Do not judge a segmenter by mean average precision. It does not track recognition quality. Use CER on the downstream recogniser.
- Report training and inference resources, then choose the model against the hardware you actually have.

**Dataset distillation does not transfer, yet.** Classification-era distillation (gradient matching, distribution matching, trajectory matching) was adapted to a CRNN/CTC recogniser by grouping transcriptions into "text pseudo-classes" and optimising only the pixels of real starting lines. Across four datasets and budgets of 1% to 10%, no distilled set beat its real starting lines. Random lines beat medoid lines, and further optimisation degraded recognition.

**The practical recipe.** Keep a small curated set of real labelled lines per collection. Fine-tune the segmenter and recogniser on it. Measure with CER. Do not spend effort synthesising a distilled training set for HTR.

**Caveat.** Both results are from 2026 preprints. The CER ranges are the authors' own benchmarks, not an independent comparison. Tag performance claims `[TENTATIVE]` until a second source confirms them.
