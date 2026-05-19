---
title: ArcticDB — server-less S3-backed time-series database (Man Group)
type: entity
tags: [entity, tool, time-series-database, tick-storage, market-data, bsl-license, k52, phase-0-pending]
keywords: [arcticdb, man-group, time-series-database, s3-backed, server-less, pandas, tick-storage, business-source-license, bsl, market-dataset]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/hedge-fund-open-source-tooling.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 1 (@zostaff) catalog entry that surfaced ArcticDB
- @concepts/hedge-fund-open-source-tooling.md — parent catalog; ArcticDB is the one Cemini-relevant adoption candidate broken out here
- @concepts/cemini-license-posture.md — ArcticDB's BSL license is the gating concern for adoption

## Raw Concept

What prompted this page: K52 ingest of @zostaff's hedge-fund OSS catalog. ArcticDB stood out as the single entry that maps onto a real Cemini need — the historical market-data layer (`cemini-librarian:/opt/cemini-bulk/market-dataset/`) — so it gets its own entity page with a Phase-0 framing rather than living only as a catalog row.

## Narrative

### What it is

ArcticDB (`man-group/ArcticDB`, ~2.3k★ as of May 2026) is a **server-less, S3-backed time-series database** built by Man Group / AHL. It stores billions of rows of time-series data directly in object storage with no database server process — the client library reads/writes Parquet-like segments to S3 (or compatible object stores). The interface is pandas-native: DataFrame in, DataFrame out. Per @zostaff's post, it is the database Bloomberg licensed from Man Group.

### Why it is a Cemini adoption candidate

Cemini's raw market-data canon currently lives as historical files under `/opt/cemini-bulk/market-dataset/`. ArcticDB would give that layer:
- versioned, queryable tick/bar storage with no server to operate;
- pandas-native access for the research/backtest path;
- object-storage backing that fits the Hetzner + snapshot model.

It is a plausible replacement for ad-hoc CSV/Parquet handling in the market-dataset layer.

### The license gate — `[NEEDS VERIFICATION 2026-05-18]`

ArcticDB is under the **Business Source License (BSL)**, *not* a standard OSI open-source license. BSL is free for non-production use and converts to an open license after a change date, but **commercial / production deployment requires a paid license** until then. Cemini's trading stack is a commercial production system — so adoption is **not free** the way an MIT tool would be.

Before any adoption:
1. Read ArcticDB's actual `LICENSE` file and BSL "Additional Use Grant" — BSL terms are per-project; the production-use carve-out and the change-date matter.
2. Confirm whether Cemini's intended use (internal research-stack storage vs. a customer-facing product) falls inside or outside the free Additional Use Grant.
3. If a paid license is required, price it against the alternative (stay on Parquet, or use a permissively licensed store).

This is exactly the license-posture discipline in @concepts/cemini-license-posture.md — a capable tool with a non-OSS license is a *conditional* candidate, not a free one.

### Verdict

**Phase-0 pending.** Capable and well-fit on the technical axis; gated entirely on the BSL terms. Run the standard Phase-0 audit (clone, read LICENSE, verify maturity signals, check the failure mode — here the failure mode is *license*, not architecture) before any GO/NO-GO.

## Snippets

> "Stores billions of rows of time-series data in S3 with no server. Pandas in, pandas out. ... License: BSL, free for non-commercial use." [Source: posts-2026-05-18.docx — Post 1, @zostaff]
