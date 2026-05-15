---
title: "Turbovec — SIMD-Accelerated Quantized Vector Index"
type: entity
tags: [tool, vector-search, simd, quantization, rust, memory-efficiency, nearest-neighbor]
keywords: [turbovec, ryancodrai, simd, neon, lloyd-max-quantization, vector-index, memory-compression, rust, mit-license, adopt]
related:
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - entities/infrastructure/conductor-librarian-architecture.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15T11:45
---

## Relations

- @sources/multi-wiki-link-eval-v4-2026-05-15.md — evaluated in v4 link-eval (Adopt tier)
- @entities/infrastructure/conductor-librarian-architecture.md — vector compression directly applicable to kb-server's embedding store

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

The compression ratio is directly applicable to the OSINT wiki's kb-server: the current embedding store for 867 wiki pages could be compressed to a fraction of its current memory footprint, enabling fully local, air-gapped semantic search without cloud dependence.

Technical note: the IdMapIndex uint64 stability during concurrent O(1) removals requires isolated benchmarking to verify index integrity under write-heavy workloads.

## Local adoption (2026-05-15)

- Core Rust library (`~/tools/turbovec/turbovec`) builds cleanly with `cargo build --release`
- Python bindings (`~/tools/turbovec/turbovec-python`) required build.rs fix:
  - **Problem**: pyo3 0.27 cdylib needs Python C API symbols at link time; Xcode CLT Python 3.9 only provides Python3.framework (not standalone `libpython3.9.dylib`). Framework-based linking (`-F<path> -framework Python3`) creates `@rpath/Python3.framework/...` references that maturin's wheel repair can't resolve.
  - **Fix**: `-undefined dynamic_lookup` in build.rs — the standard macOS Python extension pattern. Python C API symbols resolve from the interpreter process at dlopen time. Accelerate framework still linked explicitly for BLAS.
  - Installed via `pip install -e .` (maturin build backend)
- Functional smoke test passed: TurboQuantIndex (add, search, swap_remove, prepare, write/load) + IdMapIndex

## Cross-wiki routing

- **@ccc-wiki** — brief detailing integration of the turbovec Rust crate into Python-based backtesting pipeline for accelerated similarity searches on historical market regimes.
