---
title: "Cemini Multi-Wiki Link Evaluation Report — 26-URL batch (v3, May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki-routing, license-audit, k54]
keywords: [multi-wiki-tool-eval, 26-url-batch, quantdinger, nexttrade, yt-dlp, notebooklm-py, windows-use, delive, everos, moneyprinter, trufflehog, poly-arbitrage-bot, no-license-epidemic, license-finding-unreliability]
related:
  - entities/tools/quantdinger.md
  - entities/tools/nexttrade.md
  - entities/tools/yt-dlp.md
  - entities/tools/poly-arbitrage-bot.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
maturity: validated
read_status: deep-read
created: 2026-05-19
updated: 2026-05-19
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/quantdinger.md — URL 1, Adopt (verified Apache-2.0, 5,898★); self-hosted AI quant trading platform
- @entities/tools/nexttrade.md — URL 21, Adopt with caveats (verified MIT, but TypeScript not Python and ~1yr stale)
- @entities/tools/yt-dlp.md — URL 19, Adopt (Unlicense source); OSINT audio-visual intelligence gathering
- @entities/tools/poly-arbitrage-bot.md — URL 23, eval Reject **corrected** (verified MIT — already K53-verified); Polymarket↔Kalshi arb bot
- @concepts/cemini-license-posture.md — this eval is the K54 case: 9 of 26 license findings were wrong
- @ccc-wiki/briefs/2026-05-19_k54-tool-eval-ccc-items.md — cross-routed CCC items
- @cybersecurity-wiki/briefs/2026-05-19_k54-tool-eval-cybersec-items.md — cross-routed Cybersec items
- @image-gen-wiki/briefs/2026-05-19_k54-tool-eval-imagegen-items.md — cross-routed Image-gen items
- @seo-wiki/briefs/2026-05-19_k54-tool-eval-seo-items.md — cross-routed SEO item

## Raw Concept

- **Title**: "Cemini Multi-Wiki Link Evaluation Report: v3 Architecture Verification and Strategic IP Analysis" — `Tool Evaluation and Wiki Fit.docx`
- **Type**: LLM-generated tool-evaluation report (Gemini DR-style), 26 URLs across 7 wiki surfaces
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit.docx`
- **Retrieved**: 2026-05-19 (dropped into `research to be indexed/`)
- **Structure**: per-URL — URL / license / stars-commits-issues / stack / maturity / tier / primary-fit / 7-wiki routing matrix / cross-wiki routing / reasoning / license risk / NEEDS VERIFICATION. Plus aggregate summary, primary-fit distribution, cross-routing batch, license-pattern summary, and 45 cited works.

This is K54 — the fifth+ multi-wiki tool-eval batch in a month (K49 46-repo, K50 56-repo, K51 36-repo, K53 41-URL, K54 26-URL). Ingested **with verification corrections**: the eval's license layer was spot-checked against the GitHub API and found unreliable in *both* directions — see Narrative.

## Narrative

### Tier rollup (eval's own verdicts)

| Tier | Count | Items |
|---|---|---|
| Adopt | 6 | QuantDinger, notebooklm-py, Windows-Use, yt-dlp, NextTrade, DeLive |
| Steal-from | 1 | Reactive-Resume |
| Defer | 0 | — |
| Reference-only | 5 | VulnWeb, Hackers-Arise, free-programming-books, practice-c-programming-projects, PHPMailer |
| Reject | 11 | freellmapi, TruffleHog, MoneyPrinter, gitGraber, LLMFeeder, CVE-2026-3629, EverOS, GitDorker, H4X-Tools, poly-arbitrage-bot, pro-workflow |
| UNAVAILABLE | 3 | Vanilla_CLI, opensourceprojects.dev post, Comview |

Primary-fit: Cybersec 6, CCC 5, None 6, Cemini-financial 3, OSINT 1, Image-gen 1, SEO 1, 3D-printing 0. ~85% non-OSINT — heavy cross-routing batch.

### Verification corrections — the eval's license layer failed both ways

A GitHub-API check of all 23 retrievable repos (2026-05-19) found the eval **wrong on 9 of 26 items** — worse than the K53 batch. The eval failed in *two* directions: (a) it reported real LICENSE files as "NO LICENSE FOUND" (8 false negatives), and (b) it *invented* a license that does not exist (MoneyPrinter, claimed AGPL-3.0, is actually MIT).

| Repo | Eval verdict | GitHub API (verified 2026-05-19) | Corrected effect |
|---|---|---|---|
| `FujiwaraChoki/MoneyPrinter` (URL 10) | Reject — "AGPL-3.0 fatal poison pill" | **MIT**, 13,259★ | Eval *fabricated* the AGPL. License-clean; Image-gen-routed |
| `EverMind-AI/EverOS` (URL 17) | Reject — "NO LICENSE FOUND" | **Apache-2.0**, 4,968★ | Reject **overturned** — license-clean |
| `jatinkrmalik/LLMFeeder` (URL 13) | Reject — "NO LICENSE FOUND" | **MIT**, 411★ | Reject **overturned** — license-clean |
| `zostaff/poly-arbitrage-bot` (URL 23) | Reject — "NO LICENSE FOUND" | **MIT**, 20★ | Reject **overturned** (already K53-verified MIT) |
| `tashfeenahmed/freellmapi` (URL 4) | Reject — "NO LICENSE FOUND" | **MIT**, 1,335★, TypeScript | License-clean; Reject stands on the TS/Node stack mismatch |
| `PySecTools/CVE-2026-3629` (URL 15) | Reject — "NO LICENSE FOUND" | **MIT**, 1★ | License-clean; stays Reference-only (1★ PoC) |
| `trufflesecurity/trufflehog` (URL 5) | Reject — "NO LICENSE FOUND" | **AGPL-3.0**, 26,385★ | Reject **confirmed** — but for the *real* reason (copyleft) |
| `hisxo/gitGraber` (URL 11) | Reject — "NO LICENSE FOUND" | **GPL-3.0**, 2,277★ | Reject **confirmed** — copyleft poison pill |
| `vil/H4X-Tools` (URL 20) | Reject — "NO LICENSE FOUND" | **GPL-3.0**, 709★ | Reject **confirmed** — copyleft poison pill |
| `obheda12/GitDorker` (URL 18) | Reject — "NO LICENSE FOUND" | **NONE** (genuine), 2,525★, last push **2024-08** | Reject **confirmed** — genuinely unlicensed *and* stale |
| `rohitg00/pro-workflow` (URL 26) | Reject — "NO LICENSE FOUND" | **NONE** (genuine), 2,162★ | Reject **confirmed** — genuinely unlicensed |
| `Fapputa/Vanilla_CLI` (URL 3) | UNAVAILABLE — "NOT FOUND" | **exists**, NONE, 6★, C | Repo exists; trivial / unlicensed |
| `rockorager/comview` (URL 8) | UNAVAILABLE — "NOT FOUND" | **exists**, MIT, 117★, Go | Repo exists, license-clean |
| `austin-starks/NextTrade` (URL 21) | Adopt — "Python, NumPy/Pandas" | MIT, 1,741★, **TypeScript**, last push 2025-05-15 | Stack misidentified (TS, not Python); ~1yr stale |
| `EbookFoundation/free-programming-books` (URL 14) | Reference — license "NOT FOUND" | **CC-BY-4.0**, 388,551★ | License resolved |

Of the 10 repos the eval marked "NO LICENSE FOUND," **only 2 are genuinely unlicensed** (GitDorker, pro-workflow). The other 8 have real LICENSE files. The eval's clean-license claims mostly held (QuantDinger Apache-2.0, notebooklm-py MIT, Windows-Use MIT, yt-dlp Unlicense, DeLive Apache-2.0, Reactive-Resume MIT, PHPMailer LGPL-2.1 all confirmed) — **except MoneyPrinter, where the eval invented an AGPL license outright**. Net rule, restated from K53: treat every eval license finding — *positive or negative* — as unverified until checked against `gh api repos/<owner>/<repo>`.

### OSINT / Cemini-financial items (4)

- **URL 1 `brokermr810/QuantDinger`** — Adopt. Self-hosted AI quantitative trading platform (Python / Docker / Vue.js, multi-agent). Five-layer engine: indicators → signals → strategy → backtest → execution adapters; ships `.cursor/skills/quantdinger-agent-workflow`. Apache-2.0, 5,898★ (verified). Cemini-financial primary. → @entities/tools/quantdinger.md.
- **URL 21 `austin-starks/NextTrade`** — Adopt **with caveats**. UI-driven algorithmic-trading + backtesting framework. MIT, 1,741★ (verified) — but the eval misidentified the stack as Python; it is **TypeScript**, and the last push was **2025-05-15** (~1 year stale). Cemini-financial primary; reference-grade, not a live dependency. → @entities/tools/nexttrade.md.
- **URL 19 `yt-dlp/yt-dlp`** — Adopt. De-facto-standard media extractor (Python, 163k★, Unlicense source). OSINT-primary: raw audio-visual intelligence gathering; compile from the Unlicense source tarball, never the GPLv3+-encumbered pre-built binaries. → @entities/tools/yt-dlp.md.
- **URL 23 `zostaff/poly-arbitrage-bot`** — eval Reject (no-license) **corrected to MIT**. Polymarket↔Kalshi cross-exchange arbitrage bot; already cataloged from K53. K54 is an independent re-confirmation that the eval repeats the same false-negative. → @entities/tools/poly-arbitrage-bot.md.

### Cross-routed items (non-OSINT)

Routed to sibling wikis as destination briefs (`scripts/cross_wiki_route.py`):

- **CCC-wiki** — notebooklm-py (Adopt; reverse-engineered NotebookLM Python SDK + Claude Code skill, MIT 13.7k★), Windows-Use (Adopt; GUI-level Windows agent, MIT), DeLive (Adopt; system-audio capture + 12-backend ASR + MCP server, Apache-2.0), EverOS (eval Reject **corrected** → Apache-2.0; long-term-memory OS for agents — re-evaluate for token-economics research), LLMFeeder (eval Reject **corrected** → MIT; web-to-Markdown browser extension), pro-workflow (Reject — genuinely no-license confirmed; self-correcting SQLite-FTS5 memory, 37 hooks / 34 skills — monitor for a license), TruffleHog / Hackers-Arise / free-programming-books (Reference stubs).
- **Cybersec-wiki** — TruffleHog (AGPL-3.0 verified — production-Reject, but a credential-scanning Reference for the Cybersec wiki), VulnWeb (Reference; OWASP directory), Hackers-Arise (Reference; MCP-for-log-analysis tutorial), CVE-2026-3629 (MIT-verified PoC; WordPress priv-esc, manual analysis only), gitGraber (GPL-3.0 verified — Reject), GitDorker (no-license + stale — Reject), H4X-Tools (GPL-3.0 verified — Reject), Windows-Use (cross-route; GUI-agent lateral-movement stub).
- **Image-gen-wiki** — MoneyPrinter (license **corrected** AGPL→MIT; YouTube-Shorts/TikTok automation via MoviePy — now license-clean for persona-ops), yt-dlp (audio-extraction stub), DeLive (multi-provider ASR stub).
- **SEO-wiki** — Reactive-Resume (Steal-from; MIT 37k★, JSON→PDF/DOCX rendering pipeline + CSS template architecture).

### Caveats

- LLM-generated eval (Gemini DR-style); reasoning is verbose and over-emphatic ("catastrophic," "non-negotiable," "absolute"). Treat tiers as a shortlist, not a verdict.
- License layer verified unreliable in both directions (above). Any destination-wiki curator accepting a cross-routed item must re-verify its license via `gh api` first.
- Star/commit/issue metadata is mostly "NOT FOUND" in the eval — filled in here from the GitHub API.
- Stack fields are not reliable either — NextTrade was misidentified as Python (it is TypeScript).

## Snippets

> "Adopt: 6 ... Steal-from: 1 ... Defer: 0 ... Reference-only: 5 ... Reject: 11 ... UNAVAILABLE: 3." [Source: Tool Evaluation and Wiki Fit.docx — Aggregate summary]

> "NO LICENSE FOUND: 10 (freellmapi, TruffleHog, gitGraber, LLMFeeder, CVE-2026-3629, EverOS, GitDorker, H4X-Tools, poly-arbitrage-bot, pro-workflow) ... Poison-pill licenses caught: 1 (MoneyPrinter: AGPL-3.0)." [Source: Tool Evaluation and Wiki Fit.docx — License pattern summary] — note: 8 of the 10 "NO LICENSE" findings are wrong, and the MoneyPrinter AGPL claim is fabricated (verified MIT).

> "URL 10: MoneyPrinter ... License: AGPL-3.0 ... the IP analysis reveals a catastrophic liability ... requires an absolute organizational quarantine." [Source: Tool Evaluation and Wiki Fit.docx — URL 10] — `[RETRACTED]` — `gh api repos/FujiwaraChoki/MoneyPrinter` returns `spdx_id = MIT`.

## Dead Ends

- **Do not transcribe this eval's license findings — in either direction.** Verified 2026-05-19 that the eval reports retrieval gaps as "NO LICENSE FOUND" (8 false negatives of 10) *and* fabricated an AGPL-3.0 license for MoneyPrinter that does not exist (repo is MIT). This is a worse failure rate than the K53 batch. Same root cause as the K51 `fd` data artifact. Always re-check `gh api repos/<owner>/<repo>` before accepting *any* license claim.
