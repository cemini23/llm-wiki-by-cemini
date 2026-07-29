---
title: GitHub Repo Revenue Evaluation — OpenWork Extract + BR civic APIs Pass (2026-07-29)
type: source
tags: [source, tool-evaluation, revenue, atto, k204, docx, mcp]
keywords: [different-ai/openwork, brasil.io, querido-diario, quorum-api, pix-api, PayloadsAllTheThings, MediaCrawler]
related:
  - entities/tools/different-ai-openwork.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/italian-citizenship-latam-audience-systems.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: deep-read
---

## Relations

- @entities/tools/different-ai-openwork.md — sole **Extract** (Atto MCP desktop UI)
- @concepts/wiki-tooling-evaluation.md — eval ritual
- @concepts/gpuology-genealogy-agent-kit.md — Priority #1 product
- @concepts/italian-citizenship-latam-audience-systems.md — BR audience ≠ BR civic APIs
- @concepts/cemini-license-posture.md — MIT vs FSL / AGPL isolation

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GitHub Repository Revenue Evaluation (security / OSINT / MCP desktop batch) |
| URLs | 20 |
| Filename (inbox) | `GitHub Repository Revenue Evaluation.docx` |
| Filename (egress) | `GitHub Repository Revenue Evaluation-2026-07-29-security-mcp.docx` |
| sha256 | `3b855bc1694b7c0505e37a5da4ac3b051bb62813ca865e30a5c8a775414fd51e` |
| Distinct from | K168 (`ac781556…`), K163, history Analysis docx — **different URL batch** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Revenue Evaluation-2026-07-29-security-mcp.docx` |
| Laptop extract | `.local/research/atto-latam-audience-systems/GITHUB-EVAL-2026-07-29.md` |

**Never trust eval license claims** — verify via `gh api` before Phase-0.

## Narrative

Batch theme (evaluator): security auditing, OSINT platforms, localized MCP desktop agents. Priority lens: Atto #1 · GuruWatcher #2.

### Aggregate tiers

| Tier | Count | Repos |
|------|-------|-------|
| **Integrate** | 0 | — |
| **Extract** | 1 | [different-ai/openwork](https://github.com/different-ai/openwork) — Atto MCP desktop UI / skill router |
| **Watch** | 0 | — |
| **Context** | 16 | snipe-it, faceswap, MediaCrawler, ANE, quorum-api, brasil.io, PayloadsAllTheThings, bettercap, ctf-tools, 0l4bs, ATSCAN, Ciphey, juice-shop, pwndbg, theHarvester, SUDO_KILLER |
| **Pass** | 1+ | open-erp (also listed Pass); snipe-it Pass for Atto ops |
| **UNAVAILABLE** | 2 | okfn-brasil/querido-diario, bacen/pix-api |

### Brazilian / LatAm civic APIs — do they help Atto?

**Verdict: no productizable citizenship/registry path.** Operator suspicion that “Brazilian APIs” would feed civil-record / JS tooling is **not** supported by this batch:

| Repo | What it is | Atto citizenship fit |
|------|------------|----------------------|
| `thiagobarbosa/quorum-api` | São Paulo City Council public-spending API | **None** — civic finance, not cartório / CRC |
| `okfn-brasil/querido-diario` | Official gazette scrape (metadata UNAVAILABLE in eval) | **None** for Italian JS packs |
| `turicas/brasil.io` | Aggregated BR public datasets | **Context only** — no Italian archival / certidão issuance |
| `bacen/pix-api` | Pix payment specs (UNAVAILABLE in eval) | Payments later — **not** registry; UNAVAILABLE this run |
| `Purple-Stock/open-erp` | BR retail ERP | **Pass** — inventory ERP ≠ genealogy |

Atto Brazil locale still needs **cartório / CNJ apostille / certidão** paths from K203 country briefs — not these GitHub civic stacks.

### OpenWork (only Extract)

MIT core outside `/ee`; enterprise under **FSL-1.1-MIT**. Phase-0 (2026-07-29): **CONDITIONAL-GO Extract** — clone `.local/adopts/openwork`; patterns only; **no** Atto Electron vendor / no `ee/` dependency. See `@entities/tools/different-ai-openwork.md` + `scripts/adopt_k204_phase0.sh`.

### License friction (wiki-only Context)

AGPL/GPL (snipe-it, bettercap, theHarvester) isolate; MediaCrawler commercial-use disclaimer; ANE private Apple APIs — never ship in kit.

## Snippets

> Extract: 1 — [https://github.com/different-ai/openwork + P&L boost for Atto via a robust MCP desktop agent UI…]

> Reasoning: While theoretically useful for South American data journalism, the complete lack of Western financial or Italian archival overlap nullifies any viable P&L trajectory. [brasil.io]

[Source: GitHub Repository Revenue Evaluation-2026-07-29-security-mcp.docx]
