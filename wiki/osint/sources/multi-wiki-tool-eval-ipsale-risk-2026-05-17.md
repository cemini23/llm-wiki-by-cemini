---
title: "Cemini Multi-Wiki Ecosystem — Automated Tool Evaluation & IP-Sale Risk Assessment (56-repo batch, May 2026)"
type: source
tags: [source, tool-evaluation, phase-0-audit, multi-wiki-routing, license-audit, ip-sale, adopt-stealfrom-reject, k50]
keywords: [multi-wiki-tool-eval, 56-repo-batch, ip-sale-risk, no-license-epidemic, copyleft-poison-pill, cross-wiki-routing, chandra, recon-tooling, claude-code-tooling, llm-generated-eval]
related:
  - entities/tools/chandra.md
  - concepts/cemini-license-posture.md
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
maturity: validated
read_status: deep-read
created: 2026-05-17
updated: 2026-05-18
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/chandra.md — the single OSINT-primary Adopt (vision-language document-parsing model)
- @concepts/cemini-license-posture.md — the IP-sale copyleft / no-license posture this eval enforces
- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — prior multi-wiki tool-eval batch (K49 v3 iteration); this is the successor batch
- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — next multi-wiki tool-eval batch (K51, 36 repos); successor to this one
- @cybersecurity-wiki/entities/tools/gau.md — Adopt-tier, cybersec primary fit (cross-routed)
- @cybersecurity-wiki/entities/tools/katana.md — Adopt-tier, cybersec primary fit (cross-routed)
- @cybersecurity-wiki/entities/tools/gopacket.md — Steal-from tier, cybersec primary fit (cross-routed)
- @cybersecurity-wiki/entities/tools/openvpn-install.md — Steal-from tier, cybersec primary fit (cross-routed)
- @seo-wiki/entities/tools/html-anything.md — Adopt-tier, SEO primary fit (cross-routed)
- @seo-wiki/entities/tools/itshover.md — Adopt-tier, SEO primary fit (cross-routed)
- @seo-wiki/entities/tools/oransim.md — Adopt-tier, SEO primary fit (cross-routed)
- @ccc-wiki/entities/tools/ai-token-monitor.md — Adopt-tier, CCC primary fit (cross-routed)
- @ccc-wiki/entities/tools/codexbar.md — Adopt-tier, CCC primary fit (cross-routed)
- @ccc-wiki/entities/tools/superclaude-framework.md — Adopt-tier, CCC primary fit (cross-routed)
- @ccc-wiki/entities/tools/roo-code.md — Adopt-tier, CCC primary fit (cross-routed)

## Raw Concept

- **Title**: Cemini Multi-Wiki Ecosystem: Automated Tool Evaluation and IP-Sale Risk Assessment Report
- **Type**: LLM-generated multi-wiki tool-evaluation report (Gemini Deep Research style)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Multi-Wiki Tool Evaluation.docx`
- **Retrieved**: 2026-05-17 (dropped into `research to be indexed/`)
- **Scope**: 56 candidate repositories evaluated across 7 surfaces (Cemini-financial / OSINT / Cybersec / Image-gen / SEO / 3D-printing / CCC) against operational utility + IP-sale licensing compliance.
- **Verdict basis**: license verification (SPDX), maturity signals (stars / last commit / open issues), stack fit, cross-wiki routing, copyleft / no-license IP-contamination risk.

Doc-level evaluation — verdicts derive from the report's research, not from a Cemini Phase-0 source audit. Phase-0 clone audits remain owed before any Adopt-tier code lands on a production surface. Successor to the K49 "Tool Evaluation and Wiki Fit v3 Iteration" eval (`@sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`).

## Narrative

### Headline — the no-license epidemic

The dominant finding is a **licensing-hygiene crisis**: of 56 repos, **40 are Reject** — and the bulk of those reject on **NO LICENSE FOUND**. Repos labelled "open source" in their README but shipping no `LICENSE` file default, under copyright law, to **all-rights-reserved** — illegal to use in an IP-sale-bound proprietary stack. The eval treats any unlicensed repo as a structural reject. AGPL-3.0 / SSPL-1.0 / EUPL-1.2 / CC-BY-NC / BSL remain catastrophic copyleft poison pills for every surface bearing proprietary code.

### Verdict ledger (56 repos)

| Tier | Count |
|------|-------|
| Reject | 40 (mostly NO-LICENSE; some GPL/AGPL/non-commercial) |
| Reference-only | 3 |
| Defer | 1 |
| **Adopt** | **10** |
| **Steal-from** | **2** |

### Actionable verdicts (12) — license + primary fit + routing

| Tool | Tier | License | Primary fit | Routed |
|------|------|---------|-------------|--------|
| **chandra** | Adopt | Apache-2.0 (code) / OpenRAIL-M (weights) | OSINT | `entities/tools/chandra.md` (this wiki) |
| **gau** | Adopt | MIT | Cybersec | → cybersecurity-wiki |
| **katana** | Adopt | MIT | Cybersec | → cybersecurity-wiki |
| **gopacket** | Steal-from | Apache-2.0 | Cybersec | → cybersecurity-wiki |
| **openvpn-install** | Steal-from | Unlicense | Cybersec | → cybersecurity-wiki |
| **html-anything** | Adopt | Apache-2.0 | SEO | → seo-wiki |
| **itshover** | Adopt | MIT | SEO | → seo-wiki |
| **oransim** | Adopt | Apache-2.0 | SEO | → seo-wiki |
| **ai-token-monitor** | Adopt | MIT | CCC | → ccc-wiki |
| **CodexBar** | Adopt | MIT | CCC | → ccc-wiki |
| **SuperClaude_Framework** | Adopt | MIT | CCC | → ccc-wiki |
| **Roo-Code** | Adopt | Apache-2.0 | CCC | → ccc-wiki |

**OSINT relevance is thin this batch** — only **chandra** is OSINT-primary (a document-parsing vision-language model for the ingest pipeline). The 11 other actionable tools are recon/security (cybersec), web-design (SEO), or Claude-Code tooling (CCC) — cross-routed to sibling wikis. All 12 actionable tools are permissively licensed (MIT / Apache-2.0 / Unlicense) — clean for the IP sale; the licensing crisis is entirely on the Reject pile.

### Caveats

- **Doc-level only** — stars/commit counts and capability claims come from the report's research, not independent verification. Phase-0 audits owed before adoption.
- **40 Rejects not page-ified** — the no-license / copyleft rejects are recorded here in aggregate, not given entity pages (per the corpus-overflow / don't-force-route discipline). Notable reject classes: unlicensed exploit/recon code (ParamSpider, NGINX-RIFT-SCAN, MiniPlasma), unlicensed awesome-lists, GPL/AGPL production tools.
- **Roo-Code** is Apache-2.0 but **archived by its owner** — adoptable only as a fork-and-maintain blueprint, not a live dependency.
- **chandra weights** are OpenRAIL-M (use-restricted) — compliant for self-hosting under the revenue threshold; flagged on the entity page.

## Snippets

> "This report systematically categorizes [fifty-six] candidate repositories across seven distinct evaluation surfaces, applying strict anti-hallucination disciplines to verify capabilities, community maturity, and licensing posture based exclusively on verifiable repository metadata." [Source: Multi-Wiki Tool Evaluation.docx — intro]

> "Under international copyright law, the absence of an explicit license defaults to exclusive copyright retention by the author, rendering the software illegal to duplicate, modify, or deploy in a commercial, IP-bearing context." [Source: Multi-Wiki Tool Evaluation.docx — Licensing Taxonomy]
