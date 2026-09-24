---
title: "Surface-Driven Stochastic Volatility for Commodity Options"
type: source
tags: [arxiv, source, k271, vol, options]
keywords: [k271, soybean, CVOL, stochastic-volatility, smile]
related:
  - concepts/k271-vol-quant-wave.md
maturity: draft
created: 2026-09-24
updated: 2026-09-24
read_status: skimmed
---

## Relations

- @concepts/k271-vol-quant-wave.md

## Raw Concept

| Paper | arXiv:2609.27138 |
| File | `arxiv-2609.27138-surface-driven-stochastic-volatility-for-commodi.pdf` |
| Location | `research to be indexed/arxiv-2609.27138-surface-driven-stochastic-volatility-for-commodi.pdf` |
| Archive | pending |
| Authors | Arthur Steve Tchoneteck, Tingjia Zhang, Frederi Viens (Rice University; ENSTA Paris) |
| Retrieved | 2026-09-24 |
| Pages | 43 |
| Dual-ID | **OSINT K271** |
| sha256 | `6ab1f30ec7b76f93b454e7d663d572b1b0c4fc4d56b2eee4a37c6b1285e7e0a7` |
| Code | No GitHub repo in the PDF |

## Narrative

The paper studies soybean futures options with daily CME CVOL indicators from October 2013 to August 2025. It reports that the at-the-money level and the convexity are positive, right-skewed, and fit by log-Ornstein–Uhlenbeck dynamics. The additive skew changes sign, so the paper puts that factor on an Ornstein–Uhlenbeck process on the real line.

Under a log-OU futures-volatility model, the paper maps three surface facts to three latent states. The at-the-money level maps to the volatility state. Convexity maps to a surface-implied vol-of-vol state. Skew maps to a leverage state. The paper then writes a risk-neutral pricing equation, checks prices with Monte Carlo and finite differences, and trains a neural-network surrogate.

**Cemini posture:** research surface only. **FILE. No live orders. No sizing change. 0 product Integrate GO.**
