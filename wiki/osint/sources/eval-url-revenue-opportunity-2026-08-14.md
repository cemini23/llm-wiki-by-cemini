---

title: "Eval — Revenue Opportunity URL Evaluation 2026-08-14 (20-URL, K237)"
type: source
tags: [eval, phase-0, k237, atto, guruwatcher, ccc, cyber, seo]
keywords: [ente, cyberscraper-2077, rachoon, rustscan, deepseek-harness, whapa, hermes-bot-mode, siftly, voxcpm, ai-marketing-skills, webchat, jumpserver, comet, waku, spacesuit, edgevpn, best-windows-apps, withoneai-cli, macro, log-viewer, vero]
related:
  - entities/tools/ente.md
  - entities/tools/cyberscraper-2077.md
  - entities/tools/rachoon.md
  - entities/tools/rustscan.md
  - entities/tools/voxcpm.md
  - entities/tools/vero.md
  - concepts/e2ee-vault-share.md
  - concepts/dex-fee-implied-volatility.md
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - sources/eval-url-revenue-opportunity-2026-08-15.md
  - sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md
  - sources/arxiv-2608.12566-domus-2026-08-14.md
  - sources/arxiv-2608.13340-uniswap-fee-iv-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-15
read_status: read


---

## Relations

- @entities/tools/ente.md — Extract (Atto Access Share E2EE, AGPL-3.0, size-skip clone)
- @entities/tools/cyberscraper-2077.md — Integrate (cyber lab, MIT, cloned 0.4MB)
- @entities/tools/rachoon.md — Extract (Atto billing/PDF, AGPL-3.0, pattern-only)
- @entities/tools/rustscan.md — Extract (cyber recon, GPL-3.0 — docx claimed MIT, wrong)
- @entities/tools/voxcpm.md — Extract (Atto narrated histories, Apache-2.0)
- @entities/tools/vero.md — paper ref 2608.13522 (CCC verified-software, Apache-2.0)
- @concepts/e2ee-vault-share.md — ente → Atto Access Share zero-knowledge vault
- @concepts/dex-fee-implied-volatility.md — Uniswap 2608.13340 → pm/xsp signal
- @concepts/cemini-license-posture.md
- @concepts/active-project-research-routing.md
- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 prior batch
- @sources/eval-url-revenue-opportunity-2026-08-11.md — K231 prior batch
- @sources/eval-url-revenue-opportunity-2026-08-15.md — K239: rachoon/RustScan/WebChat reappear; do not re-tier

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Repository Revenue Opportunity Evaluation.docx` + `Repository Revenue Opportunity Evaluation (1).docx` |
| sha256 (both) | `07bf0537…ca051d8` / `2ef3cacb…39a127` |
| Duplicate status | **Near-duplicate** — full recursive `unzip` diff of both docx is empty; identical `word/document.xml`, same file set, only zip-level byte difference. **Folded into this one source page**; both archived to egress. |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` (both files) |
| retrieved | 2026-08-14 |
| URLs evaluated | 20 |
| Theme | Zero-knowledge archival storage, agent orchestration harnesses, high-speed OSINT/pentest scrapers, self-hosted billing engines |

## Narrative

20-URL revenue-opportunity evaluation with batch theme covering zero-knowledge archival storage, agent orchestration harnesses, high-speed OSINT/pentest scrapers, and self-hosted billing engines. Docx license claims were **never trusted** — every GO/Extract/Integrate verdict re-verified via `gh api repos/{owner}/{repo}` (SPDX + size). Full spot-check below.

### Verdict aggregate (with license re-verification)

| Tier | Count | URLs |
|------|-------|------|
| Integrate | 1 | **CyberScraper-2077** (MIT ✓, 0.4MB → cloned; routed to cyber lab, not GuruWatcher) |
| Extract | 6 | **ente** (AGPL-3.0 ✓, 704MB → size-skip clone), **rachoon** (AGPL-3.0 ✓, pattern-only), **RustScan** (GPL-3.0 — docx claimed MIT), **VoxCPM** (Apache-2.0 ✓), Hermes-Bot-Mode (MIT ✓), Siftly (MIT — docx said NOT FOUND) |
| Extract-hold | 2 | deepseek-harness (MIT ✓, **do-not-replace** — claude-ds keep-wrapper posture already set), whapa (license **null**, privacy-sensitive family data → pattern-awareness only, no clone) |
| Context | 5 | WebChat (MIT), jumpserver (GPL-3.0), waku.sh (MIT), spacesuit (null license), edgevpn (Apache-2.0) |
| Pass | 6 | log-viewer (MIT), comet (MIT), best-windows-apps (null), withoneai/cli (null), macro (AGPL-3.0, 1.69GB), ai-marketing-skills → moved to Extract (MIT) |

### License re-verification (gh api — docx claims were wrong on 7/20)

| Repo | Docx claim | gh api SPDX | Size |
|------|-----------|-------------|------|
| ente/ente | AGPL-3.0 | AGPL-3.0 ✓ | 721MB (size-skip) |
| itsOwen/CyberScraper-2077 | MIT | MIT ✓ | 0.4MB |
| ad-on-is/rachoon | AGPL-3.0 | AGPL-3.0 ✓ | 3.9MB |
| bee-san/RustScan | **MIT** | **GPL-3.0** | 14.5MB |
| deepseek-ai/deepseek-harness | MIT | MIT ✓ | 114MB |
| B16f00t/whapa | GPL-3.0 | **null** (no LICENSE file) | 31MB |
| NousResearch/Hermes-Bot-Mode | MIT | MIT ✓ | 8.7MB |
| viperrcrypto/Siftly | NOT FOUND | **MIT** | 0.3MB |
| OpenBMB/VoxCPM | Apache 2.0 | Apache-2.0 ✓ | 4.5MB |
| ericosiu/ai-marketing-skills | NOT FOUND | **MIT** | 0.7MB |
| molvqingtai/WebChat | MIT | MIT ✓ | 5.8MB |
| jumpserver/jumpserver | GPL-3.0 | GPL-3.0 ✓ | 138MB |
| zeronsh/comet | NOT FOUND | **MIT** | 33MB |
| mudler/edgevpn | NOT FOUND | **Apache-2.0** | 9.9MB |
| macro-inc/macro | NOT FOUND | **AGPL-3.0** | 1.69GB |
| sunblaze-ucb/vero | (paper ref) | Apache-2.0 ✓ | 1.9MB |

**Pattern:** docx license claims unreliable in both directions — false "MIT" (RustScan actually GPL-3.0) and false "NOT FOUND" (Siftly/comet/edgevpn/ai-marketing-skills/log-viewer all resolve). Reproduces the K53/K54 + K231 "never trust eval SPDX" lesson.

### Phase-0 clone log (`.local/adopts/`)

| Repo | Verdict | Clone? | Size |
|------|---------|--------|------|
| CyberScraper-2077 | Integrate GO (cyber lab) | ✓ cloned | 1MB |
| sunblaze-ucb/vero | paper ref 2608.13522 | ✓ cloned | 14MB |
| ad-on-is/rachoon | Extract reference (AGPL pattern) | ✓ cloned | 8MB |
| bee-san/RustScan | Extract reference (GPL pattern) | ✓ cloned | 7MB |
| ente/ente | Extract (AGPL) | **size-skip** 721MB — README/docs only | — |
| deepseek-harness | Extract, do-not-replace | skip (already evaluated) | — |
| macro-inc/macro | Pass | **size-skip** 1.69GB | — |
| whapa | Context (null license) | skip | — |

Total cloned this batch: **30MB** (within 500MB budget).

### Routing notes

- **Atto** (Priority #1): ente E2EE vault/share pattern (**required brief**), rachoon Gotenberg billing PDF (AGPL isolate), VoxCPM narrated histories (secondary), ai-marketing-skills Gumroad conversion copy (Extract, MIT — feeds SEO wiki).
- **GuruWatcher** (Priority #2): **no brief** — no price/level watch source in this batch (CyberScraper was docx-routed to GW paywall scraping but is a scraping tool, not a watch; Siftly/Hermes are orchestration patterns, not watches).
- **Cyber / local-abliterated lab**: CyberScraper-2077 (GO Integrate, MIT), RustScan (Extract, GPL-3.0), skill-misevolution + self-evolving-defense papers.
- **CCC /route**: AutoDesign meta-harness (2608.13560), Vero (2608.13522), skill misevolution (2608.12851), deepseek-harness do-not-replace, Gemini 3.7 Flash (Latent Space).
- **SEO**: SparkToro zero-click brief (not a stub).
- **xsp/pm**: Uniswap fee-IV (2608.13340) → concrete DEX-side volatility/flow signal → pm brief + scp; WuBlock weekly → wiki-only (venue/market context, no implementable flow signal).
- **Poker**: skip (no IIG hook).
