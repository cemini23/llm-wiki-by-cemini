#!/usr/bin/env python3
"""
BSIV vectorized benchmark — the Cemini-relevant test.

Cemini's production hot path runs IV inversion across batches of options
(Polygon options chains, Kalshi event-market binary contracts). The relevant
question is NOT scalar-call speed but **vectorized array speed**.

This benchmark builds an N=10000 array of (k, c) pairs spanning realistic
moneyness/IV ranges and times:
  (a) Schadner formula vectorized via numpy + scipy.stats.invgauss.ppf array call
  (b) scipy.optimize.brentq looped (no vectorized brentq exists)
"""
import math
import time
import numpy as np
from scipy.stats import norm, invgauss
from scipy.optimize import brentq


def bs_call_normalized_array(k: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Vectorized normalized Black-Scholes call."""
    d1 = -k / v + v / 2.0
    d2 = -k / v - v / 2.0
    return norm.cdf(d1) - np.exp(k) * norm.cdf(d2)


def iv_schadner_vectorized(c: np.ndarray, k: np.ndarray, T: float = 1.0) -> np.ndarray:
    """
    Vectorized Schadner IV. Handles three cases element-wise:
      - ATM (k=0): closed form via Φ⁻¹
      - OTM (k>0): m=1, q=(1-c)
      - ITM (k<0): m=e^k, q=(1-c)/m

    Returns σ array.
    """
    out = np.empty_like(c, dtype=np.float64)

    # Mask: ATM (k≈0)
    atm = np.abs(k) < 1e-15
    out[atm] = 2.0 * norm.ppf((c[atm] + 1.0) / 2.0)

    # OTM (k > 0)
    otm = k > 1e-15
    if otm.any():
        abs_k_otm = np.abs(k[otm])
        q_otm = 1.0 - c[otm]  # m = 1
        mu_param_otm = 2.0 / abs_k_otm
        # scipy.stats.invgauss.ppf accepts arrays for both q and mu
        x_otm = invgauss.ppf(q_otm, mu_param_otm)
        out[otm] = 2.0 / np.sqrt(x_otm)

    # ITM (k < 0)
    itm = k < -1e-15
    if itm.any():
        abs_k_itm = np.abs(k[itm])
        m_itm = np.exp(k[itm])  # m = K/F = e^k (k<0)
        q_itm = (1.0 - c[itm]) / m_itm
        mu_param_itm = 2.0 / abs_k_itm
        x_itm = invgauss.ppf(q_itm, mu_param_itm)
        out[itm] = 2.0 / np.sqrt(x_itm)

    # Total vol → σ
    return out / math.sqrt(T)


def iv_brentq_loop(c: np.ndarray, k: np.ndarray, T: float = 1.0) -> np.ndarray:
    """Loop scipy.optimize.brentq over the array — there is no vectorized brentq."""
    out = np.empty_like(c, dtype=np.float64)
    for i in range(len(c)):
        try:
            v = brentq(lambda v: bs_call_normalized_array(np.array([k[i]]), np.array([v]))[0] - c[i],
                       1e-8, 10.0, xtol=1e-12)
            out[i] = v / math.sqrt(T)
        except ValueError:
            out[i] = float("nan")
    return out


def build_realistic_grid(n: int = 10000, seed: int = 42):
    """
    Build N (k, c) pairs spanning realistic moneyness/IV ranges:
      - log-moneyness k ~ Uniform(-0.5, 0.5)  (covers deep ITM to deep OTM)
      - true σ ~ Uniform(0.05, 1.0)            (5% to 100% annualized vol)
      - T = 1 year throughout
    Returns (k, c, v_true) arrays where c is the normalized call price implied
    by (k, σ, T).
    """
    rng = np.random.default_rng(seed)
    k = rng.uniform(-0.5, 0.5, size=n)
    sigma = rng.uniform(0.05, 1.0, size=n)
    T = 1.0
    v_true = sigma * math.sqrt(T)
    # Avoid k=0 exactly (would trip ATM mask boundary)
    k = np.where(np.abs(k) < 1e-10, 1e-9, k)
    c = bs_call_normalized_array(k, v_true)
    return k, c, sigma, v_true


def run_benchmark(n: int = 10000, n_runs: int = 5):
    print(f"=== Vectorized BSIV benchmark — N={n} options × {n_runs} runs ===\n")

    k, c, sigma_true, v_true = build_realistic_grid(n=n)

    # Pre-warm: scipy compiles internal kernels on first invgauss call
    _ = iv_schadner_vectorized(c[:10], k[:10])
    _ = iv_brentq_loop(c[:10], k[:10])

    # Schadner vectorized
    sch_times = []
    for _ in range(n_runs):
        t0 = time.perf_counter()
        sigma_sch = iv_schadner_vectorized(c, k)
        t1 = time.perf_counter()
        sch_times.append(t1 - t0)
    print(f"  Schadner vectorized:  mean {np.mean(sch_times) * 1000:.2f} ms / "
          f"{np.mean(sch_times) / n * 1e6:.3f} us per option")

    # brentq loop
    bre_times = []
    for _ in range(n_runs):
        t0 = time.perf_counter()
        sigma_bre = iv_brentq_loop(c, k)
        t1 = time.perf_counter()
        bre_times.append(t1 - t0)
    print(f"  brentq looped:        mean {np.mean(bre_times) * 1000:.2f} ms / "
          f"{np.mean(bre_times) / n * 1e6:.3f} us per option")

    speedup = np.mean(bre_times) / np.mean(sch_times)
    print(f"\n  ** Speedup (brentq / Schadner) = {speedup:.1f}× **")

    # Accuracy verification across the array
    err_sch = np.abs(sigma_sch - sigma_true)
    err_bre = np.abs(sigma_bre - sigma_true)
    print(f"\n  Schadner: mean abs err {err_sch.mean():.3e}, max {err_sch.max():.3e}, "
          f"NaNs {np.isnan(sigma_sch).sum()}")
    print(f"  brentq:   mean abs err {err_bre.mean():.3e}, max {err_bre.max():.3e}, "
          f"NaNs {np.isnan(sigma_bre).sum()}")

    # Cemini-relevant interpretation
    print(f"\n=== Cemini interpretation ===")
    print(f"  At {n} options/batch (sample Polygon equity options chain):")
    print(f"    Schadner: {np.mean(sch_times) * 1000:.1f} ms per IV inversion of full chain")
    print(f"    brentq:   {np.mean(bre_times) * 1000:.1f} ms per IV inversion of full chain")
    print(f"  CPU savings on the IV hot path: {speedup:.1f}× → "
          f"{(np.mean(bre_times) - np.mean(sch_times)) * 1000:.1f} ms freed per chain pass")


if __name__ == "__main__":
    # Run on sizes representative of Cemini production load
    run_benchmark(n=1000, n_runs=5)
    print()
    run_benchmark(n=10000, n_runs=3)
