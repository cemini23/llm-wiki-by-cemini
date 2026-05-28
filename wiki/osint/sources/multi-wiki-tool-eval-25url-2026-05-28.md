---
title: "Multi-Wiki Tool Evaluation — 25-URL Audit (May 2026, K73)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, k73]
keywords: [tool-eval, 25-url, no-license-found, bsl-misread, mcp-patterns, ccc-routing]
related:
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-tool-eval-27url-2026-05-27.md
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
maturity: validated
read_status: deep-read
created: 2026-05-28
updated: 2026-05-28
clusters: [cemini-internal, tool-evaluation]
---

## Relations
- @ccc-wiki/briefs/2026-05-28_k73-ccc-tool-eval-license-skepticism.md  (cross-wiki brief)

- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — another doc-level eval confirming the two-gate necessity
- @concepts/cemini-license-posture.md — repeats known false-negative patterns ("NO LICENSE FOUND", blanket BSL reject language)
- @sources/multi-wiki-tool-eval-27url-2026-05-27.md — immediate predecessor batch (same genre)
- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — predecessor with similar overturn patterns

## Raw Concept

| Field | Value |
|-------|-------|
| Title | `Cemini Multi-Wiki Link Evaluation Report (May 2026 Batch)` |
| File | `Tool Evaluation for Cemini Wiki.docx` |
| sha256 | `c8b606bebaad2529b896be095a7fc0f849e86cde9849843f9fa66b3642f75ad7` |
| URL labels | 25 (`URL 1` ... `URL 25`) |
| URLs extracted | 92 |
| Location | `research to be indexed/Tool Evaluation for Cemini Wiki.docx` |

## Narrative

The document is a broad LLM-style architecture/eval narrative across Cemini + sibling wiki surfaces. It is useful for **candidate discovery**, but not for direct adoption decisions without Phase-0 checks.

Recurring risk patterns in this batch match prior K68–K72 tool-eval ingests:

1. **"NO LICENSE FOUND" false negatives** are present again.
2. **BSL language is over-broad** (treated as blanket poison-pill rather than Additional Use Grant analysis).
3. Strongly opinionated reject language appears without reproducible verification blocks.

Actionable posture remains unchanged:

- use this as a **routing + triage source**;
- run `gh api` + LICENSE-file verification for every Adopt/Steal-from candidate;
- never promote doc-level verdicts straight into prod-facing adoption.



### K73 Phase-0 audits completed (2026-05-28)

| Repo | Verified license | Maturity snapshot | Phase-0 verdict | Why |
|------|------------------|-------------------|-----------------|-----|
| `WH-2099/mermaid-skill` | MIT | 79★, updated 2026-05-28 | **CONDITIONAL-GO (CCC/local)** | Good skill pattern for diagram workflows; not a cemini-prod runtime dependency. |
| `mukul975/cve-mcp-server` | Apache-2.0 | 726★, active | **CONDITIONAL-GO (cybersec wiki / workstation)** | Strong vuln-intel utility; out-of-scope for trading runtime, route to cybersec/CCC docs. |
| `ariadng/metatrader-mcp-server` | MIT | 391★, active | **NO-GO for current prod** | MT4/MT5-centric forex bridge; domain mismatch with PM/Kalshi/HL stack. |
| `mhallsmoore/qsforex` | **No LICENSE file** | 849★, legacy repo | **NO-GO** | License unknown + alpha-state forex engine + dated architecture. |
| `blacklanternsecurity/bbot` | AGPL-3.0 | 9.7k★, active | **REJECT for prod** | Network copyleft poison-pill for IP-sale-bound core stack. |
| `NoFxAiOS/nofx` | AGPL-3.0 | 12.4k★, active | **REJECT for prod** | AGPL-3.0 + heavy forex scope mismatch. |
| `deepentropy/tvscreener` | Apache-2.0 | 1.0k★, active | **Reference-only / CONDITIONAL-GO local** | Useful data-fetch helper; vendor ToS + source reliability checks required before any server use. |
| `EA31337/EA31337` | GPL-3.0 | 1.1k★, active | **REJECT for prod** | GPL-3.0 copyleft conflicts with IP-sale posture. |

## Snippets

> "Licenses categorized as poison pills ... AGPL-3.0 ... BSL ... immediate rejection" [Source: Tool Evaluation for Cemini Wiki.docx K73]

> "The following analysis ... parses twenty-five specific external targets" [Source: same]

## Dead Ends

- License-gating prose is directionally useful but technically over-general; must not be copied into adoption verdicts without source-level checks.
