---
title: "Eval — Multi-Wiki Revenue Opportunity Evaluation (K260)"
type: source
tags: [source, k260, eval]
keywords: [k260, SPDX, DeskcommCRM, pentagi, OpenResearch]
related:
  - concepts/k260-eval-github-wave.md
  - concepts/k260-atto-wave.md
  - concepts/k260-cybersec-wave.md
  - entities/tools/colibri.md
  - entities/tools/claude-red-offensive-skills.md
  - entities/tools/pentagi.md
  - entities/tools/deskcommcrm.md
  - entities/tools/aimap.md
  - entities/tools/openresearch.md
maturity: draft
created: 2026-09-13
updated: 2026-09-13
read_status: read
---

## Relations

- @concepts/k260-eval-github-wave.md
- @concepts/k260-atto-wave.md
- @concepts/k260-cybersec-wave.md
- @entities/tools/colibri.md
- @entities/tools/claude-red-offensive-skills.md
- @entities/tools/pentagi.md
- @entities/tools/deskcommcrm.md
- @entities/tools/aimap.md
- @entities/tools/openresearch.md

## Raw Concept

| File | `Multi-Wiki Revenue Opportunity Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Revenue Opportunity Evaluation.docx` |
| Retrieved | 2026-09-13 |
| Dual-ID | **OSINT K260** |
| sha256 | `32131426afefa40d5122c8c8c2301c59f20777e80510b4229eb518f7cacc5b30` |

## Narrative

Never trust docx SPDX. gh api 2026-09-13 overrides the eval:

| Repo | SPDX | ★ | size_kb | Verdict |
|------|------|---|---------|---------|
| JustVugg/colibri | Apache-2.0 | 28951 | 14989 | **Watch** — already `entities/tools/colibri.md`. No new clone. ~0.05–1.06 tok/s. **wont_wire.** |
| ever-co/ever-gauzy | AGPL-3.0 | 4577 | 259836 | Pass + AGPL SIZE-SKIP. No clone. |
| melgarafael/DeskcommCRM | **MIT** (docx said NOT FOUND) | 2011 | 125929 | **GO REFERENCE** ~126MB. Atto EXTRACT. PII vault. |
| vxcontrol/pentagi | MIT | 23692 | 57851 | **GO REFERENCE** ~58MB. Cyber lab EXTRACT. |
| alphaXiv/OpenResearch | MIT | 1787 | 73492 | **GO REFERENCE** ~73MB. CeminiDFS FILE. |
| SnailSploit/Claude-Red | MIT | 3865 | 2332 | Already `entities/tools/claude-red-offensive-skills.md`. FILE. **No new clone. No PoC in wiki.** |
| jihe520/MathModelAgent | — | — | — | Pass (docx). Skip clone. |
| tonhowtf/omniget | GPL-3.0 | 11137 | 54687 | EXTRACT-ONLY. No vendor. |
| sparkyniner/Netryx-Astra-V2-Geolocation-Tool | **null** | 919 | 52661 | **NO-GO clone.** FILE mention on this page only. |
| BishopFox/aimap | MIT | 378 | 1376 | **GO REFERENCE** ~1.4MB. Cyber EXTRACT. |
| KatrielMoses/voidaccess | — | — | — | Pass. Skip. |
| soxoj/telegram-bot-dumper | **MIT** (docx claimed GPL — wrong) | 368 | 817 | EXTRACT awareness. No clone. Do not dump Telegram. |

Web services (tinywow, cobalt, cleanup.pictures, 10minutemail, openlibrary, alternativeto, downsub, ninite): aggregate Pass/Context/Extract on this page. openlibrary = Atto EXTRACT mention only. cobalt AGPL Context. **No reject stubs.** **0 Integrate GO.**

## Snippets

> Never trust docx SPDX. DeskcommCRM MIT (docx NOT FOUND). telegram-bot-dumper MIT (docx claimed GPL). Netryx SPDX null NO-GO clone. [Source: Multi-Wiki Revenue Opportunity Evaluation.docx; gh api 2026-09-13]
