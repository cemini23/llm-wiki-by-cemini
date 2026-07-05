---
title: ICE facility jobs monitor cadence
type: concept
tags: [meta, ice, hiring, automation, cadence]
keywords: [ice-facility-jobs, corecivic, geo-group, hiring-monitor, anomaly-report]
related:
  - concepts/ice-turnkey-research-backlog-2026-06-30.md
  - concepts/geo-ice-turnkey-acquisition-thesis.md
  - concepts/cxw-california-city-ice-turnkey-research-2026-06-29.md
  - entities/companies/corecivic.md
  - entities/companies/geo-group.md
  - meta/ice-detention-stats-cadence.md
maturity: draft
created: 2026-07-04
updated: 2026-07-04
---

## Relations

- @concepts/ice-turnkey-research-backlog-2026-06-30.md — Tier 4 jobs/hiring anomaly lane
- @concepts/geo-ice-turnkey-acquisition-thesis.md — GEO facility-acquisition watchlist
- @concepts/cxw-california-city-ice-turnkey-research-2026-06-29.md — CoreCivic / California City context
- @entities/companies/corecivic.md — CXW operator
- @entities/companies/geo-group.md — GEO operator
- @meta/ice-detention-stats-cadence.md — paired ICE biweekly occupancy / publish-gap lane

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily while CXW/GEO turnkey thesis is active |
| **Last run** | 2026-07-04 |
| **Package** | `scripts/intel/monitors/` |
| **Thesis config** | `config/theses/ice-turnkey/` |
| **Script** | `bash scripts/run_ice_turnkey_monitors.sh` (detention stats + jobs) |
| **Due check** | `bash scripts/check_ice_facility_jobs_due.sh` |
| **Jobs config** | `config/theses/ice-turnkey/jobs.yaml` |
| **Report** | `.local/reports/ice-facility-jobs/YYYY-MM-DD-jobs-sweep.md` |
| **Snapshot** | `.local/ice-jobs-daily/YYYY-MM-DD/snapshot.json` |
| **Prod timer** | `cemini-ice-facility-jobs.timer` on `cemini-prod` (detention stats + jobs) |
| **Prod root** | `cemini-prod:/opt/cemini/intel/ice-facility-jobs/` |
| **Prod log** | `cemini-prod:/opt/cemini/logs/ice-facility-jobs.log` |

The monitor fetches live CoreCivic Phenom and GEO/Jibe job feeds, normalizes postings, archives the raw ATS payloads in the daily snapshot, assigns them to target facility clusters within a configurable radius, scores role families, compares cluster counts against same-operator non-target facility baselines, and diffs against the previous snapshot. The prod timer runs every four hours and also runs the paired **ICE detention stats** monitor (`@meta/ice-detention-stats-cadence.md`) so both lanes continue while the laptop is off.

Primary signal is **change over time**, not raw job count. High-signal roles include facility administration, security leadership, case processing, intake/admin/records/mailroom, transport/removal/aviation, food/commissary, and maintenance. Health roles are lower-weight individually but can matter when they repeat or line up with litigation / monitor / conditions pressure.

The monitor is an **early weak-signal instrument**, not a legal-confirmation feed. 8-Ks, deeds, and title/escrow awards remain the hard confirm/falsifier layer; the jobs lane is meant to catch pre-disclosure operating tells such as role churn, facility activation, transport buildout, federal-side staffing/vendor backfill, and changes in target-facility staffing cadence before the market has a clean filing.

Cluster scoring now distinguishes target-facility-name matches from radius-only context and excluded context. Corporate, BI/community-supervision, ISAP, reentry, and other non-detention roles remain visible in reports but do not drive anomaly rank or Discord alerts. Each cluster also carries a signal category (`activation`, `compliance`, `transfer_pool`, `operating_stack`, `transport`, or `watch_only`) and an acquisition-relevance tag so a hiring burst is not automatically interpreted as a sale signal.

The first run on 2026-07-04 fetched **1,102 active jobs** and stored a baseline. It ranked Leavenworth/MRRC, Florence/Pinal/Eloy, GEO Adelanto/Desert View, GEO Aurora, and GEO Conroe/Montgomery as the strongest live clusters, with California City downgraded to a medium compliance/stabilization signal rather than a clean acquisition signal.

## Snippets

> First run baseline stored; no new-job alerts emitted.
> — [Source: `.local/reports/ice-facility-jobs/2026-07-04-jobs-sweep.md`]
