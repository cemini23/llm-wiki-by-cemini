---
title: "Short-term barrier option price expansion (2610.00340)"
type: source
tags: [source, k278, quant, options, volatility]
keywords: [k278, barrier-option, rough-vol, expansion, FILE]
related:
  - concepts/k278-vol-quant-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-vol-quant-wave.md

## Raw Concept

| File | `arxiv-2610.00340-short-term-barrier-option-price-expansion.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.00340-short-term-barrier-option-price-expansion.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| Dual-ID | **OSINT K278** |
| sha256 | `89db5cf74991215efa472666cfedc3cd40a8234c11c8127da1912c5f5c40cb34` |
| arXiv | 2610.00340 |
| Author | Masaaki Fukasawa (The University of Osaka) |

## Narrative

An asymptotic expansion for a short-dated up-and-out put.

The leading term is the time-inhomogeneous Black-Scholes barrier price, fitted to the forward variance curve. The first model-dependent correction is of order theta to the power H plus one half, where H is the order of the relative volatility fluctuation. That single exponent covers both rough models, where H is below one half, and regular models, where H equals one half.

The method derives the expansion as maturity and the near-barrier strike and barrier scale shrink together, in a Bachelier limit. It assumes joint weak convergence of the normalized terminal return, the relative volatility fluctuation, and the running maximum, plus uniform integrability. It validates against Monte Carlo and a Crank-Nicolson CEV partial-differential-equation benchmark.

Results for the CEV case, with 21 strikes: mean absolute error falls from 0.09426 under Black-Scholes to 0.01248 with the difference correction. Against the PDE benchmark the correction gives a mean absolute error of 0.00429 and a maximum of 0.01445. For rough Bergomi at H equals 0.1, the mean absolute error falls to 0.10319 and the maximum from 0.52969 to 0.18689. The largest Monte Carlo standard error was 0.00649, over 200,000 paths and 25,000 time steps.

The author admits one gap. The bound used for one theorem is not directly available in the general rough case, so weak convergence plus uniform integrability alone do not justify the analogous limit. A residual discrepancy remains, combining approximation, sampling, and discretization error.

No code URL. No clone. This is a method note, not a signal. **No trade. No sizing change.**
