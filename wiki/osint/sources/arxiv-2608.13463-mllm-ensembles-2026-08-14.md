---
title: "MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification (arXiv 2608.13463)"
type: source
tags: [arxiv, mllm, vision, ocr, routing, atto, watch, k237]
keywords: [ARMDIL, MLLM router, heterogeneous ensembles, image classification, DINOv2, CLIP, image-quality, document routing]
related:
  - concepts/atto-genealogy-agent-kit.md
  - concepts/document-processing-pipeline-scale-patterns.md
  - entities/tools/voxcpm.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/atto-genealogy-agent-kit.md — OCR/document routing pattern for Atto
- @concepts/document-processing-pipeline-scale-patterns.md — pipeline-scale routing
- @entities/tools/voxcpm.md — voice-clone sibling Extract in same batch

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13463, "MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification" |
| Authors | Perkins, Squires, Milligan, Raskoti, Ungerboeck (U. Tennessee Knoxville) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.13463-mllm-routed-heterogeneous-ensembles-for-robust-c.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.CV preprint, 14pp |

## Narrative

**ARMDIL** (Adaptive Router for Multi-Domain Image classification with LLMs): a small MLLM (Gemma-4-12B, local 16GB VRAM) routes each input image to the best vision backbone (ResNet-50, DINOv2/V3, OpenCLIP) across four disjoint visual domains (CIFAR10/FER2013/EuroSAT/O-MNIST) over a unified 38-class label space. Router prompt = domain definitions + image-quality stats + chain-of-thought + "output ONLY the domain name", with an **UNSURE escape hatch → best-general fallback**.

### Key results

- ARMDIL 90.78% acc / 90.71 macro F1, beats best single backbone by 1.17%, majority-vote by 0.31% acc / 1.28% F1, trails near-optimal trained NN-Router by only 0.40%.
- **Router confusion**: FER2013 TPR 99.82%, O-MNIST 95.21%, CIFAR10 97.80%, but EuroSAT only 78.20% with 12.72% → UNSURE (low-contrast, edge-poor aerial images misclassified as blurry by IQ metrics).
- Self-consistency (4 samples, no CoT) improves routing accuracy but slightly degrades downstream classification (UNSURE fallback already covers the hard domain).

### Steal-for-Atto (WATCH, not integrate)

- **MLLM domain router over a heterogeneous OCR pipeline**: classify each input into document category (civil-record vs invoice vs archival-photo vs form) → dispatch to specialized OCR/vision backend. Zero router training; adding a domain = appending a prompt definition.
- **Image-quality statistics as routing signals**: blur/brightness/contrast/noise computed cheaply, fed alongside the image to route degraded archival scans to a more robust path. Caveat: IQ metrics mischaracterize uniform/low-edge imagery (plain documents) as blurry.
- **UNSURE fallback + unified label space** gives fault tolerance even on misroute.

**Brief:** wiki-only (Atto vision/OCR watch). Tier: `[TENTATIVE]` — toy-scale datasets, no peer review.
