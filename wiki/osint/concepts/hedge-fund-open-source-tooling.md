---
title: Hedge-Fund & Quant-Firm Open-Source Tooling
type: concept
tags: [concept, quant-finance, open-source, hedge-funds, tooling, infrastructure, k52]
keywords: [hedge-fund-oss, two-sigma, man-group, jane-street, de-shaw, hudson-river-trading, optiver, worldquant, arcticdb, flint, alpha101, open-source-recruiting-brand]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - entities/tools/arcticdb.md
  - concepts/quant-finance.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 1 (@zostaff), the source catalog this page synthesizes
- @entities/tools/arcticdb.md — the one Cemini-relevant adoption candidate from the list, broken out to its own entity page
- @concepts/quant-finance.md — corpus-index home for quant tooling
- @concepts/cemini-license-posture.md — the open/closed split and ArcticDB's BSL exception are license-posture data points

## Raw Concept

What prompted this page: K52 ingest of @zostaff's X post cataloging 22 public GitHub repos from hedge funds and quant firms. The post is a curated inventory; this page preserves the inventory in a queryable table and records the open-vs-closed thesis, so a future "is there an OSS tool for X from a real quant shop" query has a home.

## Narrative

### The catalog — 7 firms that publish, by AUM

| Firm | Manages | Repos in the post |
|---|---|---|
| Two Sigma | \$70B AUM | 4 |
| Man Group / AHL | \$228.7B AUM | 4 |
| Jane Street | \$39.6B trading revenue (2025) | 4 |
| D.E. Shaw | \$90B AUM | 4 |
| Hudson River Trading | \$20B trading capital | 3 |
| Optiver | global options market maker | 2 |
| WorldQuant | \$9B AUM | 1 (community impl) |

Almost all repos are **MIT / Apache-2.0 / BSD**. The single exception is **ArcticDB** (Man Group) under the **Business Source License 1.1 (BSL)**. The post frames BSL as "paid license required for commercial deployment" — but that is an oversimplification. Verified 2026-05-18: ArcticDB's BSL **Additional Use Grant** forbids only re-offering ArcticDB *as a multi-tenant hosted database service*; all other use, including commercial internal use, is free, and each version converts to Apache-2.0 two years after release. See @entities/tools/arcticdb.md.

### The 22 repos

**Two Sigma (\$70B AUM)** — engineering-tooling oriented:
- `twosigma/flint` (~1k★) — time-series joins on Apache Spark with temporal tolerance; "find the nearest quote for every trade" at billions-of-ticks scale.
- `twosigma/beakerx` (~2.8k★) — polyglot Jupyter (Python/Scala/Groovy/Kotlin/Clojure/Java in one notebook).
- `twosigma/marbles` (~116★) — unit tests that explain failures in plain English.
- `twosigma/cook` (~338★) — batch job scheduler on Mesos/Kubernetes.

**Man Group / AHL (\$228.7B AUM)** — data + reporting:
- `man-group/ArcticDB` (~2.3k★) — server-less S3-backed time-series database; pandas in, pandas out. **BSL license.** Bloomberg licensed this database. → @entities/tools/arcticdb.md.
- `man-group/dtale` (~5.1k★) — browser GUI over pandas DataFrames (filters, correlations, charts); most-starred Man Group repo.
- `man-group/notebooker` (~900★) — turns Jupyter into a scheduled reporting engine.
- `man-group/PyBloqs` (~183★) — HTML reports from Python, no frontend.

**Jane Street (\$39.6B trading revenue 2025)** — largest commercial OCaml user:
- `janestreet/core` (~1.2k★) — alternative OCaml standard library.
- `janestreet/magic-trace` (~5.3k★) — high-resolution process tracer on Intel Processor Trace; most-starred Jane Street repo.
- `janestreet/async` (~233★) — cooperative concurrency in OCaml.
- `janestreet/hardcaml` (~1k★) — OCaml library for hardware (FPGA/ASIC) design.

**D.E. Shaw (\$90B AUM)** — Python research ergonomics:
- `deshaw/pyflyby` (~409★) — auto-import for IPython/Jupyter.
- `deshaw/pjrmi` (~47★) — Python↔Java RPC with no glue code.
- `deshaw/versioned-hdf5` (~89★) — version control for HDF5 files (built with Quansight Labs).
- `deshaw/nbstripout-fast` (~29★) — strips Jupyter outputs before git commit; Rust rewrite of nbstripout.

**Hudson River Trading (\$20B trading capital)** — C++ / FPGA latency tooling:
- `hudson-trading/corral` (~175★) — structured concurrency for C++20.
- `hudson-trading/slang-server` (~224★) — SystemVerilog language server.
- `hudson-trading/heracles-ql` (~27★) — Python DSL for alerts on latency-sensitive services.

**Optiver (global options market maker)** — nanosecond tooling:
- `optiver/timestamp9` (~65★) — nanosecond timestamps for Python.
- `optiver/optiver-asyncpg` — production fork of asyncpg (fast async PostgreSQL).

**WorldQuant (\$9B AUM)** — official GitHub is near-empty; the community filled the gap:
- `yli188/WorldQuant_alpha101_code` (~748★) — community implementation of all 101 formulaic alphas from WorldQuant's "101 Formulaic Alphas" paper.

### The open-vs-closed thesis

Firms that publish **nothing**: Renaissance Technologies (~\$130B AUM, ~66% annual returns three decades running), Citadel / Citadel Securities (~\$65B), Bridgewater (~\$100B), Millennium (~\$70B), Point72 / Cubist (~\$35B), AQR (~\$99B — account exists but holds only a pandas fork).

The split is not random — it maps onto each firm's competitive moat:

- **Edge = the people you hire** → open-source as a recruiting brand. Two Sigma, D.E. Shaw, Jane Street, HRT publish so interesting engineers find them. Jane Street's ~30M LOC, ~1M public, is described as "a recruiting strategy."
- **Edge = the alpha you discover** → close everything; any public code is a hint to competitors. Renaissance forbids even detailed résumés.

Man Group is a partial third case: it open-sources because its core IP (ArcticDB) was already licensed to Bloomberg, and as a publicly listed firm visible OSS is institutional marketing.

### Cemini posture

- **ArcticDB is an adopt-eligible candidate** — server-less S3-backed tick storage maps directly onto the `cemini-librarian:/opt/cemini-bulk/market-dataset/` layer. License verified 2026-05-18: the BSL Additional Use Grant **permits Cemini's intended internal use for free** (Cemini is not running a hosted Database Service). Remaining gate is purely technical (benchmark vs current Parquet handling) — see @entities/tools/arcticdb.md.
- **flint / alpha101** are reference material, not adoptions: flint is Spark-coupled (Cemini is not a Spark shop); alpha101 is a feature-engineering reference for the signal layer.
- The rest (beakerx, dtale, magic-trace, pyflyby, …) are general dev ergonomics — note their existence, do not Phase-0 them unless a concrete need surfaces.
- This post is a **directory**, not an evaluation. Treat star counts as point-in-time (post date ~May 2026); any actual adoption runs the standard Phase-0 audit.

## Snippets

> "Almost everything below is under MIT, Apache 2.0, or BSD. The single exception: ArcticDB from Man Group uses the Business Source License (BSL), free for non-production use, paid license required for commercial deployment." [Source: posts-2026-05-18.docx — Post 1, @zostaff]

> "When Jane Street published magic-trace and got 5,300 stars, every infrastructure engineer who used it now knows where to send a CV." [Source: posts-2026-05-18.docx — Post 1, @zostaff]

## Dead Ends

*(none yet — first synthesis.)*
