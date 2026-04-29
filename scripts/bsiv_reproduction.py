#!/usr/bin/env python3
"""
BSIV reproduction — Schadner (arXiv 2604.24480, 27 Apr 2026)

Reproduces the 328-test-case deterministic grid from §3 of the paper, comparing:
  - Schadner's explicit closed-form IV via inverse-Gaussian quantile
  - scipy.optimize.brentq iterative root search (canonical baseline)

Reports accuracy (max + mean absolute error vs ground-truth v) and speed
(microseconds per evaluation, replicated 5 runs of 1.64M evaluations each).
"""
import math
import time
import numpy as np
from scipy.stats import norm, invgauss
from scipy.optimize import brentq


# ---------------------------------------------------------------------------
# Forward Black-Scholes (normalized; F = forward, k = log(K/F), v = σ√T)
# Eq. (3) of the paper:
#   c_BS(k, v) = Φ(-k/v + v/2) - e^k · Φ(-k/v - v/2)
# ---------------------------------------------------------------------------
def bs_call_normalized(k: float, v: float) -> float:
    if v <= 0:
        return max(0.0, 1.0 - math.exp(k))
    d1 = -k / v + v / 2.0
    d2 = -k / v - v / 2.0
    return float(norm.cdf(d1) - math.exp(k) * norm.cdf(d2))


# ---------------------------------------------------------------------------
# Schadner explicit IV — Eq. (1) and Eq. (2)
# ---------------------------------------------------------------------------
def iv_schadner(c: float, k: float, T: float = 1.0) -> float:
    """
    Returns σ (annualized vol) given normalized call price c, log-moneyness k,
    and time-to-expiry T. Returns total vol v = σ√T internally and rescales.

    Eq. (1):
      σ = (2/√T) · [IG⁻¹((1-c)/m; 2/|k|, 1)]^(-1/2)
      where m = 1 if K>F (k>0), m = K/F = e^k if K<F (k<0)

    Eq. (2) ATM case (k=0):
      σ = (2/√T) · Φ⁻¹((c+1)/2)
    """
    # ATM closed form
    if abs(k) < 1e-15:
        v = 2.0 * norm.ppf((c + 1.0) / 2.0)
        return v / math.sqrt(T)

    # OTM (k > 0) or ITM (k < 0) via inverse Gaussian
    abs_k = abs(k)
    if k > 0:
        # OTM call — m = 1
        q = (1.0 - c) / 1.0
    else:
        # ITM call — m = K/F = e^k (k < 0 so 0 < e^k < 1)
        m = math.exp(k)
        q = (1.0 - c) / m

    # Inverse Gaussian quantile with mean μ = 2/|k|, shape λ = 1
    # scipy.stats.invgauss is parameterized as IG(mu) where mu IS the mean
    # parameter for the case λ=1; let's verify and pass mu = 2/|k|.
    mu_param = 2.0 / abs_k
    x = invgauss.ppf(q, mu_param)

    if x <= 0 or not math.isfinite(x):
        return float("nan")

    v = 2.0 / math.sqrt(x)
    return v / math.sqrt(T)


# ---------------------------------------------------------------------------
# Baseline — brentq root search on Eq. (3)
# ---------------------------------------------------------------------------
def iv_brentq(c: float, k: float, T: float = 1.0,
              v_lo: float = 1e-8, v_hi: float = 10.0,
              xtol: float = 1e-12) -> float:
    """Iterative root search via Brent's method. Canonical baseline."""
    def residual(v):
        return bs_call_normalized(k, v) - c
    try:
        v = brentq(residual, v_lo, v_hi, xtol=xtol, maxiter=100)
    except ValueError:
        return float("nan")
    return v / math.sqrt(T)


# ---------------------------------------------------------------------------
# Test grid — Eq. (13) of the paper
# ---------------------------------------------------------------------------
def build_grid():
    """Build the (v, Δ) → (k, c) test grid per §3 / Eq. (13)."""
    v_values = [0.01, 0.05] + list(np.arange(0.10, 2.05, 0.05))
    delta_values = [0.05, 0.20, 0.30, 0.45, 0.55, 0.70, 0.80, 0.95]
    cases = []
    for v in v_values:
        for delta in delta_values:
            # Eq. (13): k = v · (v/2 - Φ⁻¹(Δ))
            k = v * (v / 2.0 - norm.ppf(delta))
            c = bs_call_normalized(k, v)
            cases.append({"v_true": v, "delta": delta, "k": k, "c": c})
    return cases


# ---------------------------------------------------------------------------
# Accuracy comparison
# ---------------------------------------------------------------------------
def measure_accuracy(cases, T=1.0):
    schadner_errs = []
    brentq_errs = []
    for case in cases:
        v_true = case["v_true"]
        c = case["c"]
        k = case["k"]
        # iv_schadner returns σ; multiply by √T to get total vol v back
        v_sch = iv_schadner(c, k, T) * math.sqrt(T)
        v_bre = iv_brentq(c, k, T) * math.sqrt(T)
        schadner_errs.append(abs(v_sch - v_true))
        brentq_errs.append(abs(v_bre - v_true))
    schadner_errs = np.array(schadner_errs)
    brentq_errs = np.array(brentq_errs)
    return {
        "schadner_mean_err": float(np.nanmean(schadner_errs)),
        "schadner_max_err": float(np.nanmax(schadner_errs)),
        "brentq_mean_err": float(np.nanmean(brentq_errs)),
        "brentq_max_err": float(np.nanmax(brentq_errs)),
        "n_cases": len(cases),
        "n_schadner_nan": int(np.isnan(schadner_errs).sum()),
        "n_brentq_nan": int(np.isnan(brentq_errs).sum()),
    }


# ---------------------------------------------------------------------------
# Speed comparison — paper's protocol: 328 cases × 5000 reps × 5 runs
# ---------------------------------------------------------------------------
def measure_speed(cases, n_reps=5000, n_runs=5):
    """
    Per the paper: one timing run = 328 test cases × 5000 reps = 1.64M evals
    per method. Recorded over 5 runs.
    """
    schadner_runs = []
    brentq_runs = []
    for run in range(n_runs):
        # Schadner
        t0 = time.perf_counter()
        for _ in range(n_reps):
            for case in cases:
                _ = iv_schadner(case["c"], case["k"], 1.0)
        t1 = time.perf_counter()
        schadner_runs.append(t1 - t0)
        # brentq
        t0 = time.perf_counter()
        for _ in range(n_reps):
            for case in cases:
                _ = iv_brentq(case["c"], case["k"], 1.0)
        t1 = time.perf_counter()
        brentq_runs.append(t1 - t0)
    n_evals = len(cases) * n_reps
    return {
        "n_evals_per_run": n_evals,
        "n_runs": n_runs,
        "schadner_total_s": [round(t, 4) for t in schadner_runs],
        "brentq_total_s": [round(t, 4) for t in brentq_runs],
        "schadner_mean_us_per_eval": (sum(schadner_runs) / len(schadner_runs)) / n_evals * 1e6,
        "brentq_mean_us_per_eval": (sum(brentq_runs) / len(brentq_runs)) / n_evals * 1e6,
    }


def main():
    cases = build_grid()
    print(f"=== BSIV reproduction grid: {len(cases)} cases (paper says 328) ===\n")

    print("[1] Accuracy comparison")
    print("-" * 70)
    acc = measure_accuracy(cases)
    for k, v in acc.items():
        if isinstance(v, float):
            print(f"  {k:30s} {v:.3e}")
        else:
            print(f"  {k:30s} {v}")
    print()

    print("[2] Speed comparison (paper's protocol: 328 × 5000 × 5)")
    print("-" * 70)
    # Use a smaller n_reps for a first run (laptop will be slower than HP EliteBook
    # i5-1145G7; we don't need the exact 1.64M number, we need the ratio)
    spd = measure_speed(cases, n_reps=1000, n_runs=3)
    print(f"  n_evals_per_run        {spd['n_evals_per_run']}")
    print(f"  n_runs                 {spd['n_runs']}")
    print(f"  Schadner total (s)     {spd['schadner_total_s']}")
    print(f"  brentq total (s)       {spd['brentq_total_s']}")
    print(f"  Schadner us/eval       {spd['schadner_mean_us_per_eval']:.3f}")
    print(f"  brentq us/eval         {spd['brentq_mean_us_per_eval']:.3f}")
    speedup = spd['brentq_mean_us_per_eval'] / spd['schadner_mean_us_per_eval']
    print(f"  Speedup (brentq/Schadner) = {speedup:.2f}×")
    print(f"  Paper claim:           3.4× vs Jäckel 2024 (different baseline)")


if __name__ == "__main__":
    main()
