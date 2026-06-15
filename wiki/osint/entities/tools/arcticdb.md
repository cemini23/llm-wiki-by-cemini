---
title: ArcticDB — server-less S3-backed time-series database (Man Group)
type: entity
tags: [entity, tool, time-series-database, tick-storage, market-data, bsl-license, k52, adopt-eligible]
keywords: [arcticdb, man-group, time-series-database, s3-backed, server-less, pandas, tick-storage, business-source-license, bsl, market-dataset]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
  - concepts/hedge-fund-open-source-tooling.md
  - concepts/cemini-license-posture.md
  - concepts/laptop-prod-research-split.md
  - sources/cemini-laptop-prod-research-handoff-2026-05-23.md
  - entities/tools/dataset-viewer.md
  - concepts/cemini-backtest-report-kit.md
  - meta/librarian-decommission-2026-06-14.md
  - meta/equity-signal-backtest-cadence.md
maturity: draft
created: 2026-05-18
updated: 2026-06-14
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 1 (@zostaff) catalog entry that surfaced ArcticDB
- @sources/multi-wiki-link-eval-41url-2026-05-18.md — K53 eval URL 16; independently Rejected ArcticDB as a "BSL poison-pill" — the same license misread this page corrects
- @concepts/hedge-fund-open-source-tooling.md — parent catalog; ArcticDB is the one Cemini-relevant adoption candidate broken out here
- @concepts/cemini-license-posture.md — ArcticDB's BSL license is the gating concern for adoption
- @concepts/cemini-backtest-report-kit.md — Phase 2 equity momentum backtest reads `equity_bars` via SSH
- @meta/equity-signal-backtest-cadence.md — quarterly sweep ritual

- @meta/librarian-decommission-2026-06-14.md — librarian LMDB deleted; laptop `.local/arctic-market-dataset/`

## Raw Concept

`[POST-DECOMMISSION 2026-06-14]` Server LMDB on deleted `cemini-librarian` is gone unless restored from snapshot. Equity backtest: `scripts/refresh_arctic_equity_bars.py` → laptop `.local/arctic-market-dataset/`.

What prompted this page: K52 ingest of @zostaff's hedge-fund OSS catalog.

## Narrative

### What it is

ArcticDB (`man-group/ArcticDB`, ~2.3k★ as of May 2026) is a **server-less, S3-backed time-series database** built by Man Group / AHL. It stores billions of rows of time-series data directly in object storage with no database server process — the client library reads/writes Parquet-like segments to S3 (or compatible object stores). The interface is pandas-native: DataFrame in, DataFrame out. Per @zostaff's post, it is the database Bloomberg licensed from Man Group.

### Why it is a Cemini adoption candidate

Cemini's raw market-data canon currently lives as historical files under `/opt/cemini-bulk/market-dataset/`. ArcticDB would give that layer:
- versioned, queryable tick/bar storage with no server to operate;
- pandas-native access for the research/backtest path;
- object-storage backing that fits the Hetzner + snapshot model.

It is a plausible replacement for ad-hoc CSV/Parquet handling in the market-dataset layer.

### The license gate — verified `[CONFIRMED 2026-05-18]`

ArcticDB is under the **Business Source License 1.1** (Licensor: Man Group Operations Limited) — *not* a standard OSI license, which is why GitHub's detector reports it as `NOASSERTION` / "Other". But the BSL's force depends entirely on its **Additional Use Grant**, and ArcticDB's is narrow. Verbatim from the repo `LICENSE.txt` (read 2026-05-18):

> *Additional Use Grant: You may make use of the Licensed Work under the terms of this License, **provided that you may not use the Licensed Work for a Database Service.** A "Database Service" is a commercial offering that allows third parties (other than your employees and contractors) to access the functionality of the Licensed Work by creating tables whose schemas are controlled by such third parties.*
>
> *Change Date: ... two years as of the release date of [each] version. Change License: Apache License, version 2.0.*

**What this means for Cemini.** The only thing the BSL forbids is **re-offering ArcticDB itself as a multi-tenant hosted database service**. Cemini's intended use — storing its *own* market data for its *own* trading stack, schemas controlled by Cemini — is **not a "Database Service"** and is fully permitted, with no paid license. Each version also converts to plain Apache-2.0 two years after its release.

So the @zostaff post's framing ("paid license required for commercial deployment") is an **oversimplification** — BSL ≠ "commercial = paid". The restriction is specifically the SaaS-rehosting carve-out, which Cemini does not trip. The license-posture lesson: read the *Additional Use Grant*, not just the license name (recorded in @concepts/cemini-license-posture.md).

A second source made the same mistake: the K53 multi-wiki tool-eval (@sources/multi-wiki-link-eval-41url-2026-05-18.md, URL 16) independently Rejected ArcticDB, calling BSL 1.1 a "severe poison-pill license [that] strictly prohibits any commercial application without direct, paid licensure." That is the identical misread — it treats the license *name* as the verdict and never reads the Additional Use Grant. Both that eval's reject and the @zostaff framing are **superseded by this page's verification.**

### Verdict

**Adopt-eligible — license-clear for Cemini's intended use.** Technically well-fit (server-less S3-backed tick storage maps directly onto the market-dataset layer) and the BSL Additional Use Grant permits it for free.

### Adoption status — installed on cemini-librarian (2026-05-18)

ArcticDB **6.17.0** is installed and verified on `cemini-librarian`, the host of the market-dataset canon (`/opt/cemini-bulk/`):

- Installed into a dedicated venv at `cemini-librarian:/opt/cemini-bulk/.venv` (`pip install arcticdb`), isolated from the kb-server / Ollama serving path.
- **Smoke test passed**: created an LMDB-backed Arctic store, wrote a time-indexed DataFrame, read it back — values and DatetimeIndex timestamps roundtrip correctly. (ArcticDB does not persist the index `.freq` attribute — expected and harmless; the timestamps themselves are exact.)

This completes the Phase-0 "does the wheel install and run on the actual Hetzner host" check.

### Step 189 — live benchmark (2026-05-23)

On librarian against `s&p500 data kaggle/all_stocks_5yr.csv` (200k rows): pandas read 0.112s / tail-1000 **0.109s** vs ArcticDB read-all 0.014s / tail-1000 **0.011s**; write 0.153s. Artifact: `briefs/step189_arcticdb_benchmark_live.json` (prod + handoff bundle). **Verdict:** strong case for Arctic on repeated tail/range queries; full `market-dataset/` migration still operator-gated. See @concepts/laptop-prod-research-split.md.

### Market-dataset migration (2026-05-23) `[CONFIRMED]`

**Done on cemini-librarian:**

| Item | Value |
|------|-------|
| URI | `lmdb:///opt/cemini-bulk/arctic-market-dataset` |
| Library | `equity_bars` |
| Symbols | **8,507** unique tickers |
| Rows | **~17.45M** |
| On-disk store | **~536 MB** (raw tree ~1.6 GB retained as fallback) |
| Script | `scripts/migrate_market_dataset_to_arcticdb.py` |

~51 empty `.us.txt` stubs skipped; duplicate paths deduped by symbol. **Prod stack not rewired** — cemini-prod still uses prior paths until server-Claude brief.

**What remains**: wire backtest/research consumers on prod to Arctic URI; optional S3-backed store for multi-host access. Staged prod brief: `briefs/2026-05-23_arcticdb-prod-backtest-wiring.md` (rsync read replica + `ArcticDBManager` + QuantOS backtester).

## Snippets

> "Stores billions of rows of time-series data in S3 with no server. Pandas in, pandas out. ... License: BSL, free for non-commercial use." [Source: posts-2026-05-18.docx — Post 1, @zostaff]
