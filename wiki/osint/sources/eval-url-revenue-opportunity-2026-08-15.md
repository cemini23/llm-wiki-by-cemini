---
title: "Eval — Multi-Wiki URL Revenue Evaluation 2026-08-15 (18-URL, K239)"
type: source
tags: [eval, phase-0, k239, atto, guruwatcher, ccc, cyber]
keywords: [lfm-encoder, fclones, openai-privacy-filter, timesfm, rachoon, rustscan, ai-data-extraction, webchat, 0day-rubbish, leaksforums]
related:
  - entities/tools/fclones.md
  - entities/tools/openai-privacy-filter.md
  - entities/tools/rachoon.md
  - entities/tools/rustscan.md
  - entities/models/timesfm.md
  - entities/tools/privacy-filter.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/active-project-research-routing.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @entities/tools/fclones.md — GO Extract (MIT, cloned 1MB) Atto vault APFS CoW dedupe
- @entities/tools/openai-privacy-filter.md — GO Extract (Apache-2.0, cloned 1MB); ≠ packyme/privacy-filter
- @entities/tools/rachoon.md — docx Integrate **overridden** → AGPL Extract-only (K237)
- @entities/tools/rustscan.md — docx Integrate + MIT **overridden** → GPL-3.0 Extract-only (K237)
- @entities/models/timesfm.md — Apache-2.0 code clone 7MB; HF checkpoints skipped
- @entities/tools/privacy-filter.md — name collision: K215 packyme MIT vs this batch openai Apache-2.0
- @concepts/atto-genealogy-agent-kit.md — fclones + PII filter feed Atto vault
- @concepts/active-project-research-routing.md
- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 prior batch (rachoon/RustScan/WebChat)

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Multi-Wiki URL Revenue Evaluation.docx` |
| sha256 | `081aafedfabc939c2ea9bf5737fccc8ae344b740b9d063d8618d0d3fc499e8fc` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki URL Revenue Evaluation.docx` |
| retrieved | 2026-08-15 |
| URLs evaluated | 18 |
| Theme | Local CPU neural encoders, archive dedupe, PII filters, forecast models, financial/security tooling |
| License report | `.local/reports/license-k239-2026-08-15.md` |

## Narrative

18-URL revenue-opportunity evaluation. **Docx license claims were never trusted.** Every Extract/Integrate verdict re-verified via `gh api repos/{owner}/{repo}` (SPDX + size). K237 already established rachoon = AGPL Extract-only and RustScan = GPL-3.0 Extract-only — this batch's docx re-tiered both to Integrate (and re-claimed RustScan MIT). Those overrides stand.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | Docx listed 4; all overridden or size/license-gated |
| Extract | 2 | **fclones** (MIT ✓), **openai/privacy-filter** (Apache-2.0 ✓) |
| Extract-hold | 3 | LFM 350M + LFM 230M (`license=other`, no weights); timesfm **code** cloned, **checkpoints skipped** |
| Extract-blocked | 2 | 0xSero/ai-data-extraction (**null SPDX**); cordiverse/paper (**null SPDX**) |
| Extract-reaffirm | 2 | rachoon AGPL; RustScan GPL-3.0 — **do not re-tier to Integrate** |
| Context | 5 | 0day-Rubbish (MIT, no exploit clone), LEAKSFORUMS (null), electerm (MIT), aiwg (MIT), WebChat (MIT — **keep K237 Context**) |
| Pass | 4 | MagicMirror (MIT), luna (null), log-viewer (MIT), usefastlane.ai (SaaS) |

### License re-verification (gh api)

| Repo | Docx claim | gh api SPDX | Size | Action |
|------|-----------|-------------|------|--------|
| pkolaczk/fclones | MIT / Extract | MIT | 0.9MB | cloned `.local/adopts/fclones` 1MB |
| openai/privacy-filter | Apache/MIT / Extract | Apache-2.0 | 0.1MB | cloned `.local/adopts/openai-privacy-filter` 1MB |
| google-research/timesfm | Apache-2.0 / Integrate | Apache-2.0 | 4.3MB repo | cloned code 7MB; **no HF checkpoints** |
| LiquidAI/LFM2.5-Encoder-350M | LFM Open v1.0 / Extract | **other** | HF weights | **skip** |
| LiquidAI/LFM2.5-Encoder-230M | LFM Open v1.0 / Integrate | **other** | HF weights | **skip** |
| ad-on-is/rachoon | NOT FOUND / **Integrate** | **AGPL-3.0** | 3.9MB | already cloned REFERENCE; Extract-only |
| bee-san/RustScan | **MIT** / **Integrate** | **GPL-3.0** | 14.5MB | already cloned REFERENCE; Extract-only |
| 0xSero/ai-data-extraction | NOT FOUND / Extract | **null** | 62KB | no clone |
| cordiverse/paper | MIT / Extract | **null** | 0.9MB | no clone |
| molvqingtai/WebChat | MIT / Extract | MIT | 6.1MB | Context (K237) |
| Exploit-Garbage/0day-Rubbish | NOT FOUND / Context | MIT | 1.2MB | Context; **no exploit payloads in wiki** |
| FSECDEV/LEAKSFORUMS | NOT FOUND / Context | **null** | 12KB | Context |
| electerm/electerm | MIT / Context | MIT | 35MB | Context |
| jmagly/aiwg | NOT FOUND / Context | MIT | 82MB | Context |
| MagicMirrorOrg/MagicMirror | MIT / Pass | MIT | 27MB | Pass |
| Opisek/luna | NOT FOUND / Pass | **null** | 2.3MB | Pass |
| opcodesio/log-viewer | MIT / Pass | MIT | 4.9MB | Pass |
| usefastlane.ai | Commercial / Pass | n/a | n/a | Pass |

**Pattern:** docx still invents Integrate tiers on copyleft (rachoon/RustScan) and SPDX on LFM/null-license Extract rows. Reproduces K53/K54/K231/K237 "never trust eval SPDX."

### Phase-0 clone log

| Repo | Verdict | Clone? | Size |
|------|---------|--------|------|
| fclones | GO Extract | ✓ NEW | 1MB |
| openai-privacy-filter | GO Extract | ✓ NEW | 1MB |
| timesfm | Extract / code-only | ✓ NEW (no LFS) | 7MB |
| rachoon | Extract AGPL | already present | 8MB |
| RustScan | Extract GPL | already present | 7MB |
| LFM 350M/230M | Extract-hold | **skip weights** | — |
| ai-data-extraction / cordiverse/paper | null SPDX | skip | — |
| 0day-Rubbish | Context | skip (authorized-lab intel only) | — |

This-batch new clones: **9MB** (≪ 500MB).

### Pass / Context aggregate (no reject-stub farm)

- **Pass:** MagicMirror (smart-mirror kiosk; no P&L/ops hook), luna (self-hosted calendar), log-viewer (Laravel/PHP — stack miss), usefastlane.ai (closed SaaS agent builder).
- **Context:** 0day-Rubbish (automated 0-day recon writeup — **authorized scope only; no PoC in wiki**), LEAKSFORUMS (static breach-forum index; do not interact), electerm (Electron SSH/MCP GUI; CVE-2026-41501 awareness), aiwg (WireGuard mesh; existing tunnels suffice), WebChat (K237 Context — P2P URL-bound chat; not re-Extracted).
- **Null-SPDX Extract blocked:** ai-data-extraction (Cursor/Codex/Claude session scrapers — PII/secret leak risk even if cloned later), cordiverse/paper (Cordis/DeepSeek-harness undo/hot-plug writeup; K237 already **do-not-replace** deepseek-harness).

### Routing notes

- **Atto (#1):** fclones + openai/privacy-filter are the real post-license steal (vault dedupe + PII strip). LFM encoder is a CPU PII/class *story* only until SPDX-clear weights exist. rachoon stays AGPL isolate. **Never** Barone/living-person vitals in git or Atto fixtures.
- **GuruWatcher (#2):** timesfm code is already an Adopt entity; this batch does **not** wire inference into prod watches. Bond-crash watches come from the Capital Flows source, not this eval.
- **Cyber:** RustScan Extract-only; 0day-Rubbish Context-only; no crimeware clone.
- **CCC:** cordiverse/paper + ai-data-extraction stay unwired (null SPDX).
- **xsp/pm:** none from this eval.

## Snippets

> Batch theme: Local CPU-optimized neural models, agent harness fault-tolerance, archive deduplication, and financial/security tooling. [Source: Multi-Wiki URL Revenue Evaluation.docx]

> Docx Integrate list: rachoon, RustScan, timesfm, LFM 230M — license+size overrides leave **zero** new Integrate GO. [Source: `.local/reports/license-k239-2026-08-15.md`]
