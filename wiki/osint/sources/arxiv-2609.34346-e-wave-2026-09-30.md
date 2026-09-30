---
title: "E-WAVE: event-based continuous optical flow (2609.34346)"
type: source
tags: [source, k276, ood, vision, event-camera]
keywords: [k276, optical-flow, event-camera, name-only, FILE]
related:
  - concepts/k276-ood-stub-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-ood-stub-wave.md

## Raw Concept

| File | `arxiv-2609.34346-e-wave-event-based-continuous-optical-flow-via-w.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.34346-e-wave-event-based-continuous-optical-flow-via-w.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `35274731bb9d86d2c5286a28b9274147dd10413d2c7676e67482807910750e7e` |
| arXiv | 2609.34346 |
| Authors | Jiale Wu, Xiaoyang Bai, Haoming Yu, Yiwei Chen, Yifan Peng, Weiwei Xu |

## Narrative

E-WAVE estimates high-temporal-resolution optical flow from event-camera streams. It drops all-pairs correlation volumes. It uses global attention plus a Bezier displacement field, so memory and compute are not quadratic.

On MultiFlow the paper reports TEPE 1.81 and TAE 3.89. The best baseline is 2.28 and 5.32. On DSEC-Flow the result is comparable to state of the art.

The authors admit DSEC-Flow has no high-rate ground truth, so only low-rate evaluation is possible. Training used one-fifth of the MultiFlow set.

This is a computer-vision paper. It does not touch trading, agents, or genealogy. The name only is recorded. No code URL found. No clone.
