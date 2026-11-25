---
title: "A joint framework for SPX, VIX and VXX"
type: source
maturity: draft
related:
  - concepts/vix-first-joint-spx-vix-calibration.md
  - concepts/vix-term-structure-fractional-memory.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | A joint framework for SPX, VIX and VXX |
| Author | Martino Grasselli, Andrea Stanghellini, Sara Svaluto-Ferro |
| Type | arXiv preprint, q-fin.MF |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.25047-a-joint-framework-for-spx-vix-and-vxx.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.25047v1, 18 Nov 2026 |
| Pages | 38 |
| Read status | read |

## Narrative

Options on SPX, VIX and VXX price different parts of the same volatility risk. VIX links equity options to expected future variance. VXX turns exposure to the VIX futures curve into a traded product. A joint model must satisfy all three at once.

The construction places the tractable specification at the VIX level. The index is a linear functional of the truncated signature of a time-extended polynomial diffusion. Instantaneous SPX variance is then recovered from the requirement that its risk-neutral conditional expected 30-day average equals the squared VIX. With truncated signatures, that recovery reduces to finite-dimensional linear algebra, which also gives explicit access to the futures that underlie VXX. [Source: arxiv-2611.25047-a-joint-framework-for-spx-vix-and-vxx.pdf p.1]

Why VXX matters: the roll. VXX tracks a strategy in the first two VIX futures, with weights adjusted to keep short-term exposure. Its value depends on the level and shape of the curve and on the joint dynamics of both contracts. Lu (2023) documents that VXX option information is not fully spanned by VIX options, so the extra market carries extra constraints. [Source: arxiv-2611.25047-a-joint-framework-for-spx-vix-and-vxx.pdf p.2]

The authors develop a regularised model that keeps variance non-negative, and they quantify the pricing error of the tractable VIX and VXX proxies. Applications to short-dated smiles show joint calibration across the three markets, with Monte Carlo proxy-error bounds well below quoted bid-ask spreads.

The honest read: this is a modelling paper, not a trading system. It extends the wiki's VIX-first joint-calibration concept to a third market. The proxy-error-below-spread result is the part a practitioner can use as a sanity check.

## Snippets

> "Applications to short-dated option smiles illustrate joint calibration across the three markets, with Monte Carlo estimates of the proxy error bounds well below quoted bid–ask spreads." [Source: arxiv-2611.25047-a-joint-framework-for-spx-vix-and-vxx.pdf p.1]
