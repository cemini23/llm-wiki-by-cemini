---
title: "InscriptionOCR: dataset and method for understanding inscriptions (arXiv 2610.09439)"
type: source
tags: [source, k285, arxiv, ocr, historical-documents, nmt]
keywords: [inscriptionocr, brahmi, prakrit, ocr, transliteration, m2m-100, epigraphy, cc-by-nc]
related:
  - concepts/k285-arxiv-wave.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-arxiv-wave.md

## Raw Concept

| Title | InscriptionOCR: A Dataset and Method for Understanding Inscriptions |
| Authors | Jaidev Sanjay Khalane, Akbar Ali, V. N. Prabhakar, Shanmuganathan Raman (IIT Gandhinagar) |
| Type | arXiv preprint (cs.CV) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.09439-inscriptionocr-a-dataset-and-method-for-understa.pdf` |
| Retrieved | 2026-10-08 |
| arXiv | 2610.09439v1 |
| License | **CC BY-NC 4.0** |
| Code/Data | `github.com/JaidevSK/InscriptionOCR-Brahmi-Prakrit` · Kaggle dataset (~650 MB) |
| read-status | read |

## Narrative

An end-to-end pipeline for **Ashokan Brahmi stone inscriptions**: image enhancement → OCR → transliteration → machine translation. It releases the **largest public Brahmi OCR dataset** and a **Prakrit–English parallel corpus**.

### Pipeline

Grayscale → Gaussian denoise → histogram-adaptive threshold → morphological dilation/erosion → contour detection. OCR: CNN classifiers (LeNet-5, VGG-16, ResNet-50, EfficientNet) with a **564-class** output on 64×64 grayscale input. Transliteration: **Brahmi → Devanagari → ISO Roman**. Translation: fine-tune **M2M-100 (418M)**, T5-Base, or Helsinki Opus.

### Results

- OCR test accuracy: **ResNet-50 100.00%**, EfficientNet 99.96%, VGG-16 99.39%, LeNet-5 88.72%.
- NMT: **M2M-100 BLEU 56.367 / METEOR 0.772**; Opus BLEU 14.120; T5-Base 7.75.
- Data: **253,800 OCR images** (228,420 train / 25,380 test); 2,224 sentence pairs.

### Why it matters here

The **domain is epigraphy (Brahmi/Prakrit), not Italian genealogy** — so it is not directly an Atto tool. What transfers is the **pipeline shape**: a low-resource historical script handled with image restoration → OCR → transliteration → NMT. That is the same *shape* as the Atto historical-document problem, on a different script.

**Licence: CC BY-NC 4.0 — non-commercial.** Fine for research; check before any commercial use. **Transkribus remains the sole product HTR** for Atto. Route: CCC / family-history research awareness.

## Snippets

> "ResNet-50 test accuracy 100.00% … M2M-100 BLEU 56.367 / METEOR 0.772." [Source: arxiv-2610.09439-inscriptionocr-a-dataset-and-method-for-understa.pdf]

> "253,800 OCR images (228,420 train / 25,380 test); 2,224 sentence pairs." [Source: arxiv-2610.09439-inscriptionocr-a-dataset-and-method-for-understa.pdf]
