---
title: "Large deviations for integrated exponentials of Gaussian Volterra processes — variance options"
type: source
related:
  - concepts/variance-option-short-maturity-asymptotics.md
  - concepts/rough-log-normal-volatility.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Large deviations for integrated exponentials of Gaussian Volterra processes — application to variance options |
| Author | Antoine Jacquier, Mugad Oumgari, Dan Pirjol, Lingjiong Zhu |
| Type | arXiv preprint, math.PR, arXiv:2611.34567v1 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.34567-large-deviations-for-integrated-exponentials-of.pdf` |
| Retrieved | 2026-11-26 |
| Pages | 1–44 plus appendices, submitted 25 November 2026 |
| Read status | read (abstract, introduction, main results, numerical section) |

## Narrative

### The problem

A variance option pays on realised variance. Under a rough volatility model the realised variance is the time integral of an exponential of a fractional Brownian motion. The short-maturity price of that option needs the small-time tail of that integral. This paper proves the tail law and turns it into prices. [Source: arxiv-2611.34567 p.1]

### The object

The paper works with `Z_T = ∫₀ᵀ exp(ν X_t + φ(t)) dt`, where `X_t = ∫₀ᵗ K(t−u) dW_u` is a Gaussian Volterra process. The kernel is `K(t) = t^(H−1/2) ℓ(t)` with `H` in `(0, 1/2]` and `ℓ` slowly varying at zero and non-increasing near zero. That covers fractional Brownian motion and both common rough-volatility kernels. The realised variance is `Z_T / T`.

### Results

Three limit laws for `Z_T / T` as `T` goes to zero:

- **Large deviations.** Theorem 2.5 gives a large deviation principle with an explicit rate function. The rate function is fully explicit at `H = 1/2`.
- **Central limit theorem.** Theorem 2.14.
- **Moderate deviations.** Theorem 2.15, the near-the-middle regime that bridges the CLT and the large deviations.

The kernel generality is the main technical step. Earlier results of this type, including those of Lacombe, Muguruza and Stone for rough Bergomi, use the Riemann-Liouville kernel. This paper allows any regularly varying kernel that satisfies the assumption, and adds the `φ` term and a negative-moment statement.

### Application to variance options

Section 3 transfers the limit laws to option prices:

- out-of-the-money variance calls and puts at short maturity (Theorem 3.3),
- at-the-money asymptotics (Theorem 3.13),
- an expansion of the rate function in log-moneyness around the at-the-money strike (Section 3.5).

The headline, stated as a contrast in Remark 3.16: **at-the-money variance options vanish at rate `T^H`**, against the `√T` decay of at-the-money European options on the asset itself. Because `H` is near 0.1 in equity index data, the two decay at very different speeds. The `H = 1/2` case is consistent with the classical Asian-option results.

Section 4 gives explicit level and slope of the short-maturity implied volatility of variance options (Proposition 4.1) and compares them with Alòs, García-Lorite and Muguruza. The validation is numerical, in the rough Bergomi model.

### Honest limits

The results are asymptotic as `T` goes to zero. They are not a pricing formula for any finite maturity. The constants depend on the kernel, and the paper shows the two standard kernels give constants that differ by a factor of `√(8H)/(2H+1)`, which equals one only at `H = 1/2`. A reader who mixes kernels will get the wrong constant. The numerical work is in one model, not a market calibration.

### Read

For this workspace the value is the tail law for a time-integrated exponential, and the clean statement that variance-option decay scales with `H`. It is a reference paper, not a signal. No trading lane depends on it.
