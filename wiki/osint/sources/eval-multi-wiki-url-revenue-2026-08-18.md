---
title: "Eval — Multi-Wiki URL Revenue 2026-08-18 (20-URL, K241)"
type: source
tags: [eval, phase-0, k241, osint, alpr, cyber]
keywords: [CyberChef, sherlock, mitaka, IntelTechniques, redditsfinder, OSINT4ALL]
related:
  - entities/tools/cyberchef.md
  - entities/tools/sherlock.md
  - entities/tools/mitaka.md
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - concepts/cemini-license-posture.md
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - sources/osint4all-startme-2026-08-18.md
  - sources/eval-url-revenue-opportunity-2026-08-08.md
  - entities/catalogs/osint4all-search-domain.md
  - entities/catalogs/osint4all-productivity.md
  - sources/eval-multi-wiki-url-revenue-2026-09-02.md
  - sources/eval-multi-wiki-url-revenue-copy-2026-09-02.md
  - sources/eval-repository-revenue-analysis-2026-09-02.md
  - concepts/k254-eval-github-wave.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @entities/tools/cyberchef.md — K149 Context; URL eval tried **Integrate** — **do not re-tier**
- @entities/tools/sherlock.md — MIT Extract (already K227); re-clone K241
- @entities/tools/mitaka.md — MIT browser OSINT Extract
- @entities/tools/osint4all.md — nested SOCMINT/GEOINT hubs
- @concepts/osint4all-catalog.md — KEEP/DEAD/CONTEXT filing
- @concepts/cemini-license-posture.md
- @sources/eval-multi-wiki-revenue-plan-2026-08-18.md — same-day K241 GitHub eval
- @sources/osint4all-startme-2026-08-18.md — start.me L1rEYQ + nested boards
- @sources/eval-url-revenue-opportunity-2026-08-08.md — prior sherlock/OSINT URL eval
- @entities/catalogs/osint4all-search-domain.md — search/dork locators
- @entities/catalogs/osint4all-productivity.md — CyberChef KEEP row

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Multi-Wiki URL Revenue Evaluation.docx` |
| sha256 | `92ef1e2658d77c2257b63f6fdbfdb4fef5ed679fb841b915019aa6f192a82f8c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki URL Revenue Evaluation.docx` |
| retrieved | 2026-08-18 |
| URLs evaluated | 20 |
| Theme | OSINT locators, ALPR, username/email, IntelTechniques, CyberChef |
| License report | `.local/reports/license-k241-2026-08-18.md` |
| Dual-ID | **OSINT K241** = this inbox. Resolve by file+wiki, not bare K#. |

## Narrative

20-URL OSINT/ALPR evaluation. **Docx license claims were never trusted.** **0 new runtime Integrate GO.** The only Integrate attempt was **gchq/CyberChef** — already filed as `@entities/tools/cyberchef.md` K149 **Context**. Manual analyst bookmark; not a production library; do not re-tier.

Preingest flagged LIKELY because this docx cites OSINT4ALL nested hubs already on `@sources/osint4all-startme-2026-08-18.md`. Proceed as a **new eval source**; do not fold the eval into the catalog hub.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | CyberChef Integrate overridden (keep Context) |
| Extract clone | 2 | **sherlock** MIT (re-clone); **mitaka** MIT |
| Extract pattern-only (no clone) | 1 | redditsfinder MIT stale 2022 (Pushshift likely dead; 65MB skip) |
| Context-Extract wiki (no scrape) | 1 | IntelTechniques workbook / tools / Twitter / Telephone — proprietary JS; paid workbook not scraped |
| Context locators | 8 | odfinder; dorksearch; osint.sh; MarineTraffic; voter CSE; LastPass username; IDCrawl; SOCMINT/GEOINT nested hubs |
| Watch commercial | 2 | facecheck.id; Plate Recognizer |
| Pass | 3 | discordbotlist; DoNotPay; (plus Bot Sentinel Watch) |
| Watch | 1 | Bot Sentinel |

### License / action table

| Repo / URL | Docx claim | gh SPDX / note | Action |
|------------|-----------|----------------|--------|
| gchq/CyberChef | Apache / **Integrate** | Apache-2.0 (known) | **Already Context K149 — ignore Integrate** |
| sherlock-project/sherlock | n/a (catalog) | **MIT** | **CLONE Extract** (~2.5MB) |
| ninoseki/mitaka | n/a (catalog) | **MIT** | **CLONE Extract** (2.1MB) |
| Fitzy1293/redditsfinder | MIT / Extract | MIT stale 2022 | pattern only; **no clone** |
| IntelTechniques workbook/tools | proprietary | n/a | Context-Extract wiki; **no paid scrape** |
| discordbotlist.com | SaaS / Pass | n/a | Pass |
| odfinder / dorksearch / osint.sh | locators / Context | n/a | Context |
| MarineTraffic | commercial / Context | n/a | Context |
| voter CSE | public CSE / Context | n/a | Context (authorized-target only) |
| Plate Recognizer | commercial ALPR | n/a | Context commercial |
| SOCMINT / GEOINT start.me | nested hubs | n/a | Context → catalog |
| facecheck.id | commercial face search | n/a | Watch commercial |
| LastPass username | locator / Context | n/a | Context |
| DoNotPay | SaaS / Pass | n/a | Pass |
| IDCrawl | locator / Context | n/a | Context |
| Bot Sentinel | Watch | n/a | Watch |

### Pass / Context / Rejects (folded here — no reject-stub farm)

- **Pass:** discordbotlist (directory, not a bot to vendor); DoNotPay (consumer legal SaaS miss).
- **Context:** OSINT locators (odfinder, dorksearch, osint.sh, MarineTraffic, voter CSE, LastPass username, IDCrawl) + nested SOCMINT/GEOINT boards. Bookmark locators; **authorized-target scraping only**.
- **Watch commercial:** facecheck.id; Plate Recognizer (ALPR SaaS — ToS + paid API; not a silent Atto dependency).
- **Do not scrape** IntelTechniques paid workbook JS.
- **Do not visit** leak-dump / darknet / insecam rows if they appear on nested OSINT4ALL boards — those stay CONTEXT/CAUTION on the catalog.

### Routing notes

- **Atto FIND:** sherlock + mitaka = username / browser-OSINT Extract. Human-gated; platform ToS; no Barone PII fixtures.
- **Cyber:** CyberChef stays Context bookmark. No bot embedding.
- **SEO / gambling / xsp / pm:** none from this eval.

## Snippets

> CyberChef: claimed Integrate → **already K149 Context**. Do not re-tier. [Source: `.local/reports/license-k241-2026-08-18.md`]

> redditsfinder: MIT Extract → **pattern only**, stale 2022, no 65MB clone. [Source: `.local/reports/license-k241-2026-08-18.md`]
