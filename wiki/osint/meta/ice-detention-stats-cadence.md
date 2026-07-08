---
title: ICE detention stats monitor cadence
type: concept
tags: [meta, ice, detention, automation, cadence]
keywords: [ice-detention-stats, biweekly, occupancy, adp, guaranteed-minimum, staleness]
related:
  - meta/ice-facility-jobs-cadence.md
  - concepts/ice-turnkey-research-backlog-2026-06-30.md
  - concepts/geo-ice-turnkey-acquisition-thesis.md
  - entities/facilities/florence-az-detention-cluster.md
  - sources/ice-ja-26-0143-first-american-escrow-2026.md
  - sources/ca-doj-immigration-detention-2026-ab103.md
  - concepts/government-single-buyer-asset-rerating.md
maturity: draft
created: 2026-07-04
updated: 2026-07-07
---

## Relations

- @meta/ice-facility-jobs-cadence.md — paired CXW/GEO turnkey monitor lane (same prod timer)
- @concepts/ice-turnkey-research-backlog-2026-06-30.md — overcrowding / occupancy screen
- @concepts/geo-ice-turnkey-acquisition-thesis.md — facility watchlist
- @entities/facilities/florence-az-detention-cluster.md — escrow J&A Florence disambiguation
- @sources/ice-ja-26-0143-first-american-escrow-2026.md — First American title/escrow J&A primary source
- @sources/ca-doj-immigration-detention-2026-ab103.md — CA DOJ point-in-time counts vs ICE ADP/gtd min
- @concepts/government-single-buyer-asset-rerating.md — utilization = weeks–months signal lane in the cross-sector monitor map

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Every 4h on prod (bundled with jobs monitor); daily on laptop while thesis active |
| **Last run** | 2026-07-04 |
| **Last ICE publish** | 2026-04-09 (`FY26_detentionStats_04092026.xlsx`) |
| **Last IIDS pull (sheet)** | 2026-04-02 |
| **Staleness** | **86 days** — statutory biweekly cadence not resumed post-shutdown reopen |
| **Script** | `bash scripts/run_ice_detention_stats_monitor.sh` |
| **Due check** | `bash scripts/check_ice_detention_stats_due.sh` |
| **Config** | `config/theses/ice-turnkey/detention-stats.yaml` |
| **Cache sync** | `bash scripts/sync_ice_detention_cache_to_prod.sh` (ICE.gov blocks prod datacenter IP) |
| **Report** | `.local/reports/ice-detention-stats/YYYY-MM-DD-stats-sweep.md` |
| **Archive** | `.local/ice-detention-stats/{original-filename}.xlsx` |
| **Source page** | [ICE detention management](https://www.ice.gov/detain/detention-management) |
| **Prod timer** | `cemini-ice-facility-jobs.timer` (runs detention stats then jobs) |

Congress requires ICE to publish detention statistics **twice monthly** (H.R. 1158 / DHS Appropriations). The `Facilities FY26` sheet in each workbook lists facility-level **FY26 year-to-date average daily population (ADP)** by gender/criminality, plus **Guaranteed Minimum** where applicable. This is the canonical **public** occupancy lane — Vera (`vera-institute/ice-fytd-stats`) and Deportation Data Project mirror drops because ICE overwrites prior files.

**Method limits:** ADP is a fiscal YTD average, not a live headcount. `Guaranteed Minimum` is a contract floor, not rated capacity. TRAC's Jul 2025 overcapacity report used **FOIA** for point-in-time contractual capacity + census on 2025-04-13. **CA DOJ AB 103 (May 2026)** provides independent **2025 inspection-date headcounts** vs ICE contract bed caps — e.g. Otay **1,433** vs **1,142** (Oct 2025) vs ICE excel ~**1,380 ADP** vs **750** gtd min (Apr 2026 pull). Use this monitor for **screening and publish-gap detection**; cross-check DOJ/TRAC for point-in-time overcapacity.

On the last available file (pull 2026-04-02), escrow-cluster stress by ADP vs guaranteed min: **Krome** +410, **Otay Mesa** +630, **Batavia** +87; **Florence SPC** under min (−64). Monitor Discord-alerts on **new workbook publish** (`--notify`). **Prod:** ICE.gov returns Akamai 403 from Hetzner — sync laptop xlsx cache via `sync_ice_detention_cache_to_prod.sh`; prod re-parses cached workbook.

## Snippets

> Data Source: ICE Integrated Decision Support (IIDS), 04/02/2026
> — [Source: `FY26_detentionStats_04092026.xlsx` Facilities sheet (retrieved 2026-07-04)]

> Facilities sheet reports FY26 year-to-date average daily population (ADP), not a live headcount.
> — [Source: `.local/reports/ice-detention-stats/2026-07-04-stats-sweep.md`]
