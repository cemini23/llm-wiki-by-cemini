---
title: "Schadner — An Explicit Solution to Black-Scholes Implied Volatility (arXiv 2604.24480, U. Liechtenstein, 2026)"
type: source
tags: [paper, options-pricing, black-scholes, implied-volatility, quantitative-finance, closed-form-solution, cemini-adopt-candidate, ip-sale-clean, schadner]
keywords: [implied-volatility, black-scholes, closed-form, explicit-formula, inverse-gaussian, quantile-function, schadner, options-pricing, scipy-optimize-brentq, newton-raphson-replacement, polars-vectorization, kalshi-options, polygon-options]
related:
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - concepts/options-derivatives.md
  - concepts/ip-sale-readiness.md
  - concepts/wiki-tooling-evaluation.md
  - entities/infrastructure/polars.md
maturity: validated
created: 2026-04-29
updated: 2026-04-29
clusters: [quant-finance, options-pricing]
---

## Relations

- @sources/gemini-dr-wave3-link-eval-2026-04-28.md — parent canonical Wave 3 ingest source where this paper was surfaced as the wave's headline Adopt-Cemini-Wiki-Workflow finding
- @concepts/options-derivatives.md — direct concept-level home: this is a foundational compute-cycle accelerator for any options-pricing pipeline using Black-Scholes
- @concepts/ip-sale-readiness.md — CC BY 4.0 license cleared (paper-level); standard arxiv academic license, attributable
- @entities/infrastructure/polars.md — implementation surface: the explicit formula maps cleanly onto vectorized Polars LazyFrames over options chains
- @concepts/wiki-tooling-evaluation.md — WTE Wave 3 register lists this paper as the wave's headline Adopt-Cemini-Wiki-Workflow finding

## Raw Concept

- **Original title**: "An Explicit Solution to Black–Scholes Implied Volatility"
- **Author**: Wolfgang Schadner (University of Liechtenstein)
- **Type**: arXiv preprint (q-fin)
- **arXiv ID**: 2604.24480 (v1)
- **Submitted**: 27 April 2026
- **License**: CC BY 4.0 (standard arXiv attribution-only license; commercial-use permissive)
- **PDF URL**: https://arxiv.org/pdf/2604.24480
- **HTML mirror**: https://arxiv.org/html/2604.24480v1
- **Discovered via**: Gemini DR Wave 3 evaluation 2026-04-28 (`@sources/gemini-dr-wave3-link-eval-2026-04-28.md` URL 12)
- **Read status**: read — abstract + Gemini synthesis ingested 2026-04-29; full-paper deep-read pending pre-deployment empirical verification
- **PDF on librarian**: not yet downloaded; available via arxiv URL on demand. If/when downloaded for a deep-read, scp to `cemini-librarian:/opt/cemini-bulk/research/schadner-2604.24480-bs-iv-explicit.pdf`

## Narrative

### What it claims

The paper presents what its abstract calls **"the first explicit formula for Black-Scholes implied volatility,"** resolving a 50-year-old computational problem in options pricing. The standard Black-Scholes call price function `C(σ; S, K, r, T)` is non-invertible analytically with respect to `σ` — extracting implied volatility from observed market prices has historically required iterative numerical methods:

- **Newton-Raphson** (fast convergence near root, fragile near boundaries)
- **Brent's method** (`scipy.optimize.brentq` — robust but iterative, multiple function evaluations per IV solve)
- **Bisection** (slow but reliable)
- **Infinite-series approximations** (e.g., Pólya-style approximations — fast but accuracy-bounded)

Schadner's key observation: the Black-Scholes call price can be **reframed conceptually as the survival probability of an inverse Gaussian distribution**. Inverting that identity yields IV via a single quantile-function evaluation — no iteration required.

**Numerical claims** (per the paper's testing):
- ~**3.4× faster** than current state-of-the-art numerical approximations
- **Machine-precision accuracy maintained** (i.e., not a precision-trade-off; this is a clean speedup)

### Why this matters for Cemini

Cemini's options-pricing pipeline (across Kalshi prediction markets and Polygon options chains) hits IV computation at high frequency:

- Kalshi event markets where the binary contract price implies a probability that maps to IV equivalents
- Polygon options chains across watchlist tickers, recomputed across the surface
- Greeks calculations downstream of IV (delta, vega, gamma)

A 3.4× compute-cycle reduction on this hot path frees CPU for downstream analytics on the same single-VPS budget. CPU-bound work on the Hetzner host (CPU-only, 7 GB RAM ceiling, GIL-bound Python) is the limiting reagent for ingest throughput.

### Implementation plan (target for Cemini deployment)

**Phase 1 — laptop deep-read + transcription**:
1. Fetch the paper PDF locally (`curl https://arxiv.org/pdf/2604.24480 -o /tmp/schadner.pdf`).
2. Read the full derivation. Verify the inverse-Gaussian reframing is mathematically sound (the Gemini synthesis is the abstract's claim, not validated by us).
3. Transcribe the explicit formula into a working Python prototype. Validate against `scipy.optimize.brentq` outputs across:
   - Standard moneyness range (S/K ∈ [0.7, 1.3])
   - Boundary conditions (deep ITM and deep OTM, near-expiry)
   - Multiple expiries (1d, 1w, 1m, 1y)
4. Profile: confirm 3.4× speedup or document the actual speedup achieved on Cemini's data shapes.

**Phase 2 — Cemini production swap**:
1. New file: `services/quant/iv_explicit.py` with the Schadner formula (Polars-vectorized over options chains).
2. Comprehensive unit test suite covering boundary edge-cases (where inverse Gaussian quantile functions can hit floating-point underflow).
3. Behind a feature flag during initial rollout — A/B against existing `scipy.optimize.brentq` path, monitor numerical drift.
4. Once flag is verified clean across 1+ week of production data, retire the old path.

### Risks (from Gemini's evaluation + my reading)

1. **Implementation Error Risk** (Gemini's framing): mathematical transcription from theoretical LaTeX to executable Python must be exact. Inverse Gaussian quantile distributions are sensitive to floating-point precision at extreme inputs. Testing must cover deep-OTM near-expiry options where standard FP arithmetic underflows.

2. **Empirical reproduction gap** (my framing): the paper claims 3.4× speedup but does so against unspecified hardware and data shapes. Cemini's specific Polars + Polygon-options configuration may yield different numbers. **Block production deployment until reproduction**.

3. **Mathematical novelty gap**: 50 years of options-pricing literature exists. Schadner's claim of "first explicit formula" must be validated against prior work before declaring it a true breakthrough. Reasonable hypothesis: the formula is correct but may be a known result rederived, in which case other implementations may exist. Worth a literature search before committing to maintain a from-scratch implementation.

4. **Single-author + recent paper** (2026-04-27 submission): not yet peer-reviewed. arxiv preprints can be wrong; commit to deploying only after Cemini's own reproduction validates correctness.

### Open questions

- **[NEEDS VERIFICATION 2026-04-29]**: Does the explicit formula match `scipy.optimize.brentq` to machine precision across Cemini's actual options-data range (Polygon equities + Kalshi binaries)?
- **[NEEDS VERIFICATION 2026-04-29]**: Does the 3.4× speedup hold on CPU-only Hetzner hardware against Cemini's Polars-vectorized data shapes?
- **[NEEDS VERIFICATION 2026-04-29]**: What's the failure mode at boundaries (deep OTM, near-expiry, extreme skew)? Where does the explicit formula degrade vs the iterative methods it replaces?
- **[NEEDS VERIFICATION 2026-04-29]**: Does the paper cite prior closed-form attempts? If yes, those should be evaluated — there may be older proven implementations preferable to a fresh transcription.

### Citation

> Schadner, W. (2026). *An Explicit Solution to Black-Scholes Implied Volatility*. arXiv:2604.24480 [q-fin]. https://arxiv.org/abs/2604.24480

## Snippets

> "This paper identifies what appears to be the first explicit formula for Black–Scholes implied volatility, resolving a 50-year-old problem in option pricing. The key observation is that the call price [...] can be reframed as the survival probability of an inverse Gaussian distribution." [Source: arxiv 2604.24480 abstract excerpt, retrieved via Exa crawling_exa 2026-04-29]

> "The research demonstrates that the standard call option price can be reframed conceptually as the survival probability of an inverse Gaussian distribution. By inverting this exact identity, the formula allows IV to be calculated directly through a single execution of a quantile function, completely bypassing iterative inversion algorithms. Extensive numerical testing within the paper proves that the explicit formula operates approximately 3.4 times faster than current state-of-the-art numerical approximations while impeccably maintaining machine precision accuracy." [Source: Gemini DR Wave 3 synthesis, URL 12, 2026-04-28]

> "It will permanently replace existing, computationally heavy numerical approximation functions (such as `scipy.optimize.brentq`) currently applied iteratively across massive Polars DataFrames during the real-time ingest of Kalshi prediction markets or Polygon options chains." [Source: Gemini DR Wave 3 — concrete integration vector for Cemini production stack]

> "It is critical to build comprehensive unit tests ensuring the formula remains robust at extreme boundaries (for instance, when evaluating deeply out-of-the-money options nearing their expiration dates), where inverse Gaussian distributions might encounter dangerous floating-point underflow limitations in standard Python libraries." [Source: Gemini DR Wave 3 — implementation risk]
