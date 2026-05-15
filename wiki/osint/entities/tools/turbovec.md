---
title: "Turbovec — SIMD-Accelerated Quantized Vector Index"
type: entity
tags: [tool, vector-search, simd, quantization, rust, memory-efficiency, nearest-neighbor]
keywords: [turbovec, ryancodrai, simd, neon, lloyd-max-quantization, vector-index, memory-compression, rust, mit-license, adopt]
related:
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - entities/infrastructure/conductor-librarian-architecture.md
  - entities/tools/leann.md
  - concepts/kb-server-retrieval-scaling.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @sources/multi-wiki-link-eval-v4-2026-05-15.md — evaluated in v4 link-eval (Adopt tier)
- @entities/infrastructure/conductor-librarian-architecture.md — vector compression directly applicable to kb-server's embedding store
- @entities/tools/leann.md — competing compact local vector index (graph selective-recomputation vs. SIMD quantization); benchmarked head-to-head 2026-05-15
- @concepts/kb-server-retrieval-scaling.md — the K47 benchmark + NO-GO decision: turbovec not wired into kb-server (corpus too small)

## Raw Concept

Promoted from the v4 multi-wiki link evaluation (2026-05-15). Tier: **Adopt**. Primary fit: OSINT-wiki.

URL: https://github.com/RyanCodrai/turbovec
License: MIT
Stars: 652 | Last commit: NOT FOUND | Open issues: 0
Stack: Rust / Python / SIMD (NEON)

## Narrative

A high-performance vector index achieving 16x memory compression via advanced Lloyd-Max scalar quantization with random orthogonal rotations. Key metrics:

- **31 GB float32 corpus → 4 GB RAM** — enables air-gapped operation on M-series Mac hardware
- **12-24x faster search** vs uncompressed indexes via hand-written NEON SIMD kernels
- **Zero open issues** — production-stable implementation

The compression ratio is designed for *large* corpora (the project's headline is 31 GB → 4 GB). On the actual kb-server corpus it is not useful — see `## Librarian deployment` below and `@concepts/kb-server-retrieval-scaling.md`: at 943 vectors there is nothing to compress.

Technical note: the IdMapIndex uint64 stability during concurrent O(1) removals requires isolated benchmarking to verify index integrity under write-heavy workloads.

## Librarian deployment (2026-05-15)

Installed on `cemini-librarian` (the 24/7 kb-server host) per the deployment-boundary rule — any wiki-serving component lives on the librarian, not the laptop.

- Rust toolchain installed via rustup; `cargo build --release` clean after `apt install libssl-dev pkg-config` (an `openssl-sys` transitive dep).
- Python bindings via `maturin develop --release` into `/opt/turbovec-venv`. Linux-specific fix: the `_turbovec.abi3.so` linked `cblas_sgemm` undefined — resolved by `apt install libopenblas-dev` + `patchelf --add-needed libopenblas.so` on the extension module.
- Smoke test passed: `TurboQuantIndex(dim, bit_width)`, batch `add`, `search`.

**Benchmark vs kb-server's brute-force search** (943-vector live corpus):

| bit_width | search | recall@10 | index file |
|-----------|--------|-----------|------------|
| 4 | 16 µs/q | 0.922 | 180 KB |
| 3 | 19 µs/q | 0.876 | 136 KB |
| 2 | 25 µs/q | 0.814 | 92 KB |

kb-server brute-force baseline: 23 µs/q, recall 1.000. **Verdict: NOT wired into kb-server** — turbovec trades exact recall for quantized recall to save microseconds on a 1.4 MB corpus. Staged on the librarian for the day the corpus is genuinely large. Full reasoning: `@concepts/kb-server-retrieval-scaling.md`.

## Local adoption (2026-05-15)

- Core Rust library (`~/tools/turbovec/turbovec`) builds cleanly with `cargo build --release`
- Python bindings (`~/tools/turbovec/turbovec-python`) required build.rs fix:
  - **Problem**: pyo3 0.27 cdylib needs Python C API symbols at link time; Xcode CLT Python 3.9 only provides Python3.framework (not standalone `libpython3.9.dylib`). Framework-based linking (`-F<path> -framework Python3`) creates `@rpath/Python3.framework/...` references that maturin's wheel repair can't resolve.
  - **Fix**: `-undefined dynamic_lookup` in build.rs — the standard macOS Python extension pattern. Python C API symbols resolve from the interpreter process at dlopen time. Accelerate framework still linked explicitly for BLAS.
  - Installed via `pip install -e .` (maturin build backend)
- Functional smoke test passed: TurboQuantIndex (add, search, swap_remove, prepare, write/load) + IdMapIndex

## Cross-wiki routing

- **@ccc-wiki** — brief detailing integration of the turbovec Rust crate into Python-based backtesting pipeline for accelerated similarity searches on historical market regimes.
