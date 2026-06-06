---
title: "Multi-Wiki Tool Evaluation — 22-URL Audit (May 2026)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, k68]
keywords: [tool-evaluation, openkb, iron-proxy, reclip, taste-skill, claudish, omniparse, nango, license-verification]
related:
  - entities/tools/vectify-openkb.md
  - entities/tools/reclip.md
  - entities/tools/iron-proxy.md
  - entities/tools/cryptex-oss.md
  - entities/tools/claudish.md
  - entities/tools/aruneshdev-kalshi-weather-xgboost.md
  - sources/multi-wiki-tool-eval-27url-2026-05-27.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - sources/multi-wiki-tool-eval-25url-2026-05-28.md
maturity: validated
read_status: deep-read
created: 2026-05-26
updated: 2026-06-06
clusters: [cemini-internal]
---

## Relations

- @entities/tools/vectify-openkb.md — Adopt (OSINT) — CONDITIONAL-GO vs kb-server
- @entities/tools/reclip.md — Adopt (OSINT)
- @entities/tools/iron-proxy.md — Adopt (cybersec) — egress-control patterns
- @entities/tools/cryptex-oss.md — Adopt (cybersec)
- @entities/tools/claudish.md — eval Adopt overturned (no LICENSE on GitHub)
- @entities/tools/aruneshdev-kalshi-weather-xgboost.md — URL 22 duplicate; Reject upheld
- @ccc-wiki/entities/tools/google-eng-practices.md — CCC reference (eng-practices)
- @ccc-wiki/entities/tools/ml-intern.md — CCC reference
- @ccc-wiki/entities/tools/rowboat.md — CCC steal-from
- @ccc-wiki/entities/tools/centaur.md — CCC architecture-only steal-from
- @ccc-wiki/entities/tools/purple-cli.md — CCC CONDITIONAL-GO
- @ccc-wiki/concepts/tools-we-dont-use.md — claudish overturn register
- @sources/multi-wiki-tool-eval-27url-2026-05-27.md — K71 successor batch (27 URL)
- @sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md — K102 successor (50 URL, same filename new sha256)

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation Report (May 2026) — *Tool Evaluation Prompt Analysis*
- **Type**: Internal evaluation document (.docx)
- **Retrieved**: 2026-05-26
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation Prompt Analysis.docx`
- **URLs**: 22
- **Read status**: deep-read

## Narrative

Twenty-two repositories and platforms evaluated against Cemini deployment surfaces (`/opt/cemini`, OSINT wiki, sibling wikis, `.cursor/mcp.json`). **GitHub API license spot-check (2026-05-26)** applied to every Adopt row — one overturn (claudish) and one duplicate (URL 22 = existing AruneshDev weather repo).

### Tier distribution (eval vs verified)

| Tier | Eval count | Post-verify notes |
|------|------------|-------------------|
| Adopt | 9 | **8** stand; **claudish** → no LICENSE → Reject for adoption |
| Steal-from | 5 | centaur LICENSE = Other/NOASSERTION — steal patterns only after reading LICENSE |
| Reference-only | 3 | Pyth Terminal blog, eng-practices, cp-algorithms |
| Defer | 2 | Vane, MoneyPrinterTurbo |
| Reject | 3 | omniparse GPL-3.0, nango ELv2, pentest GPL-3.0 |

### OSINT-primary Adopt (verified SPDX)

| URL | Repo | License | Fit |
|-----|------|---------|-----|
| 1 | VectifyAI/OpenKB | Apache-2.0 | Local-first markdown wiki + PageIndex retrieval — **CONDITIONAL-GO** vs existing kb-server (do not replace serving path) |
| 12 | averygan/reclip | MIT | Natural-language video moment search — ingest / OSINT media workflows |
| 14 | ItzCrazyKns/Vane | MIT | Defer — Perplexity-class research UI; overlap with conductor + Exa |

### Cemini-financial / prod-adjacent

| URL | Repo | Verdict |
|-----|------|---------|
| 3 | Pyth Terminal (blog) | Reference-only — no code |
| 17 | NangoHQ/nango | **Reject** — Elastic License 2.0 |
| 22 | AruneshDev/Automated-Trading-System-Kalshi-Weather-Model | **Reject** — no LICENSE (already @entities/tools/aruneshdev-kalshi-weather-xgboost.md CONDITIONAL-GO steal-from) |

### Cybersec-primary (cross-wiki brief)

| URL | Repo | License | Tier |
|-----|------|---------|------|
| 2 | facex-engine/facex | Apache-2.0 | Steal-from |
| 7 | ironsh/iron-proxy | Apache-2.0 | Adopt |
| 8 | paradigmxyz/centaur | Other | Steal-from |
| 9 | m4xx101/cryptex-oss | MIT | Adopt |
| 21 | ZishanAdThandar/pentest | GPL-3.0 | Reject |

### CCC / SEO (cross-wiki briefs only — no OSINT entity farm)

- **CCC Adopt (eval):** Understand-Anything, claudish (overturned), purple, ml-intern (steal), rowboat (steal), eng-practices (reference)
- **SEO Adopt:** taste-skill, social-media-skills; Defer: MoneyPrinterTurbo

### License corrections vs eval text

| Repo | Eval claim | Verified |
|------|------------|----------|
| MadAppGang/claudish | MIT | **No LICENSE** (GitHub API `license: null`) |
| AruneshDev/…Weather-Model | NO LICENSE | Confirmed — duplicate of K66 entity |
| VectifyAI/OpenKB | Apache-2.0 | Confirmed |
| ironsh/iron-proxy | Apache-2.0 | Confirmed |

### Reject discipline

GPL-3.0 (**omniparse**, **pentest**) and **ELv2 (nango)** are poison pills for `/opt/cemini` IP-sale surfaces per @concepts/cemini-license-posture.md. No per-reject stub pages — reasoning consolidated here.

## Snippets

> "OpenKB … utilizes PageIndex retrieval, effectively sidestepping the overhead of traditional vector embeddings while maintaining deep cross-referencing capabilities." [Source: Tool Evaluation Prompt Analysis.docx — URL 1]

> "iron-proxy … OAuth JWT grants, GCP synthetic tokens, and robust query string scanning for granular egress control." [Source: Tool Evaluation Prompt Analysis.docx — URL 7]

> "omniparse … GPL-3.0 … server-deployed parsing tool acts as a severe poison pill." [Source: Tool Evaluation Prompt Analysis.docx — URL 4]
