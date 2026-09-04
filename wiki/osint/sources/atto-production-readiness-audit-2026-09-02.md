---
title: Atto production-readiness audit (2026-09-02)
type: source
tags: [source, audit, atto, genealogy, production-readiness]
keywords: [Atto, ATTO-001, sidecar, Puppeteer, W14, sdist, PII]
related:
  - concepts/atto-local-first-threat-model.md
maturity: draft
created: 2026-09-04
updated: 2026-09-04
read_status: read
---

## Relations

- @concepts/atto-local-first-threat-model.md — local-assist / vault / PII
- Brief home: `../atto/briefs/2026-09-04_atto-prod-audit.md`

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Atto Production Readiness Audit |
| Type | independent repository test report |
| Snapshot | `c8a9ac2c6a56` on `testbranch` |
| Date | 2026-09-02 |
| Host | Windows NT 10.0.26200; Python 3.12.11; Node 22.20.0; Rust 1.98.0 |
| Filename | `ATTO-Audit.pdf` |
| sha256 | `4cf31df03afdd891…` |
| Verdict | **NOT READY** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` (post-archive) |

## Narrative

Windows snapshot audit. Core Python engine and web UI are broadly healthy. Release is blocked.

938 automated tests/smokes passed. 1 deterministic test failure. 16 triaged findings (0 Critical, 2 High, 7 Medium, 7 Low). Production Python branch coverage 74%.

**P0 before next Windows kit:** ATTO-001 sidecar invokes bare `python` after installing PyInstaller into `.venv`. ATTO-002 isolated browser tool ships six high npm advisories (Puppeteer 24.43.1). ATTO-003 W14 Rust golden path fails because empty `truth.ged` blocks Rossi fixture seed. ATTO-004 required CI is Python-only. ATTO-005 sdist absorbs untracked workspace (audit tree 146 MB).

**P1 for this wiki:** ATTO-007 "local" LLM assist accepts `--base` / `ATTO_OMLX_BASE` and sends raw `--file` without the strip-safe pack. That is a PII routing hole against the local-first threat model.

No live FamilySearch, Antenati, Cloudflare, or real vault data were used. Synthetic fixtures only. NSIS/WebView2 installer timed out — environmental, not counted in the 16.

## Snippets

> Release verdict: NOT READY

> Do not publish the next Windows kit until ATTO-001, ATTO-002, ATTO-003, and ATTO-004 are closed and re-run in CI.

[Source: ATTO-Audit.pdf]
