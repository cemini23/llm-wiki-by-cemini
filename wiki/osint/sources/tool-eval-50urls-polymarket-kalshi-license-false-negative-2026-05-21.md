---
title: "Tool Evaluation — 50 URLs (Polymarket / Kalshi arb cluster, recon tooling, v4 prompt) — 2026-05-21"
type: source
tags: [source, tool-evaluation, gemini-deep-research, license-false-negative, polymarket, kalshi, cross-venue-arbitrage, cybersec-recon, k55]
keywords: [50-url-eval, polymarket-kalshi-arbitrage-bot, kalshi-trading-bot, polymarket-near-resolution-bot, gamma-trade-lab, no-license-found, license-detection-false-negative, v4-prompt, cross-wiki-routing-matrix]
related:
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - sources/5-5-moarrr-tool-eval.md
  - sources/5-6-links-eval-batch.md
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/polymarket-near-resolution-bot.md
  - entities/tools/prediction-market-analysis.md
  - entities/tools/awesome-polymarket-tools-harish-garg.md
  - concepts/cemini-license-posture.md
  - concepts/polymarket-bot-architecture.md
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md
  - sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
maturity: validated
read_status: deep-read
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- @sources/links-3-5-4-tool-eval.md, @sources/polymarket-5-5-tool-eval.md, @sources/5-5-links-2-tool-eval.md, @sources/5-5-moarrr-tool-eval.md, @sources/5-6-links-eval-batch.md — prior K53/K54 tool-eval batches in the same Gemini-DR family
- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — v3 prompt iteration (this batch uses v4)
- @entities/tools/polymarket-near-resolution-bot.md — the single Adopt from this batch
- @entities/tools/prediction-market-analysis.md — URL 48 already covered in K52; license verified in-file (MIT) contra this eval's NO LICENSE FOUND Reject
- @entities/tools/awesome-polymarket-tools-harish-garg.md — URL 7 already covered in K53
- @concepts/cemini-license-posture.md — this batch is the largest single demonstration of the "NO LICENSE FOUND" false-negative pattern

## Raw Concept

- **Title**: "Cemini OSINT Workspace: Master Tool Evaluation & Architecture Integration Report"
- **Author**: Gemini Deep Research (v4 multi-wiki eval prompt, frozen at `@ccc-wiki prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md`)
- **Type**: docx — 50-URL evaluation with per-URL cross-wiki routing matrix (7 wikis × ✅/❌ per row)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/tool-evaluation-50urls-2026-05-21.docx`
- **Retrieved**: 2026-05-21
- **Length**: ~3 MB, 1048 lines, 110 hyperlinks, 50 URL entries + Aggregate Summary + License Pattern Summary + Cross-routing Batch + Post-run Spot-check
- **Read status**: deep-read

## Narrative

### Aggregate verdict

| Tier | Count | Repos |
|------|-------|-------|
| **Adopt** | **1** | `gamma-trade-lab/Polymarket-Near-Resolution-Bot` (MIT, URL 5) |
| Steal-from | 0 | — |
| Defer | 0 | — |
| Reference-only | 0 | — |
| Reject | **31** | All due to `NO LICENSE FOUND` (see false-negative analysis below) |
| Unavailable | **17** | URLs 1, 15-17, 19, 21-22, 25-26, 28, 30-31, 33, 40, 43, 45-46 — unreachable domains, GitHub topic pages, blog tutorials, non-repo URLs |
| None / N/A | 1 | URL 1 (domain unreachable) |

**Primary-fit distribution**: Cemini financial 19, Cybersec 5, OSINT 4, CCC 3, SEO 1, Image-gen 0, 3D-printing 0, None 17.

### Critical pattern: "NO LICENSE FOUND" false-negative at scale

This batch is the **largest single demonstration** of the K53/K54-documented license-detection failure pattern (see @concepts/cemini-license-posture.md). **31 of 50 URLs** were Rejected solely on the basis of `NO LICENSE FOUND`. Prior batches (K53 obs 2191, K54 obs 2194, 2202) established that this label is systematically unreliable — `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` spot-checks consistently flip Rejects to MIT/Apache/BSD.

**Concrete in-batch reproduction of the error**: URL 48 = `Jon-Becker/prediction-market-analysis` is labelled `NO LICENSE FOUND` in this eval. But Cemini already verified it as **MIT (in-file, not just API)** during K52 (`@entities/tools/prediction-market-analysis.md`). The eval re-makes the same error against a repo Cemini has already cleared.

The eval acknowledges the issue in its closing "Post-run Spot-check (Cursor on OSINT)" section, which prescribes exactly the `gh api` verification loop Cemini has been running for two months. The eval's own NEEDS VERIFICATION tags on most Rejects mark the same gap.

**Cemini posture**: Treat this batch's Reject decisions as **provisional, not terminal**. The 31 Rejects in aggregate are noted but **not promoted to per-tool entity stubs**. Any specific repo from the Reject list can be promoted to entity-page status if and when an independent license verification flips it clean.

### Polymarket / Kalshi arb cluster (URLs 6, 21-49)

~30 of the 50 URLs are Polymarket-Kalshi cross-venue arbitrage bots, weather-trading bots, or related variants — a near-saturation sweep of the public OSS landscape Cemini already mapped in K53/K54 (`@concepts/polymarket-market-making-architectures.md`, `@concepts/cross-venue-arbitrage-pattern.md`).

**Genuinely new entries** (not previously catalogued in osint-wiki):

- **URL 5 — `gamma-trade-lab/Polymarket-Near-Resolution-Bot`** [Adopt]: MIT, Python, 9★, last commit 2026-05-21, 0 issues. Scans Polymarket CLOB mid-prices for heavily-favored binary outcomes nearing expiration — a specific late-stage execution slice that does not duplicate any existing wiki entity. → new entity at @entities/tools/polymarket-near-resolution-bot.md.
- **URL 42 — `suislanchez/polymarket-kalshi-weather-bot`** [Reject]: 31-member GFS ensemble + BTC microstructure + Kelly sizing + React dashboard. Highest reported profits **$1.8K**. Adds an operator data-point to @concepts/polymarket-weather-trading-strategy.md but the public PnL is well below ColdMath's $124K. Notable for the GFS-ensemble approach (vs ColdMath's pilot-aviation feed).
- **URL 34 — `rodlaf/KalshiMarketMaker`** [Reject]: Referenced from HN id=43073378. Simple market-making strategies on Kalshi — extends @concepts/polymarket-market-making-architectures.md to Kalshi side, but no novel architecture vs the existing poly-market-maker cluster.

**Recurring duplicates**:

- "polymarket-kalshi-arbitrage-bot" appears as URLs **6, 36, 38, 39, 40** — 5 different forks/clones of the same canonical name across different owners (TopTrenDev, Composio-HQ, Longbridges, sanzoI-tech, +1 unavailable). This is the same fork-storm pattern noted in K53.
- "kalshi-trading-bot" appears as URLs **31, 32, 33** (Siva-Chidambaram12 et al.) and "kalshi-ai-trading-bot" as URLs **37, 41** (ryanfrigo, bestpracticaI).
- "polymarket-copytrade" appears as URLs **24, 29** (kyyook, mclaeo).

### Out-of-OSINT-scope fits (cross-wiki routing batch)

Per the v4 prompt, the eval proposes cross-wiki stubs for entries that have secondary relevance to other Cemini wikis. Following the K55 ingest decision (briefs only, no stubs in sibling wikis):

- **Cybersec-wiki**: URLs 2 Awesome-Hacking, 3 open-source-web-scanners, 4 CF-Hero, 9 jadx-ai-mcp, 12 LLM4Pentest, 14 reconftw, 10 OpenMonoAgent.ai → consolidated into `../projects/Cybersecurity wiki/briefs/2026-05-21_k55-cybersec-toolset-from-tool-eval.md` (cross-wiki brief).
- **CCC-wiki**: URLs 8 Vane, 13 wuphf, 18 vex-tui → CCC-relevance noted; no separate brief (would be redundant with Thariq's full HTML concept-page ingest).
- **Image-gen-wiki**: URL 20 dotlottie-react-native — UI animation, mentioned only.
- **SEO-wiki**: URL 20 dotlottie-react-native (same) — frontend animation; SEO relevance is marginal; not routed.

### Trust assessment

- **Methodology**: v4 prompt produces a richer per-URL breakdown than v3 (adds the 7-wiki routing matrix, Reasoning paragraph, NEEDS VERIFICATION tag). Improvement over v3.
- **License-detection unreliability** (NO LICENSE FOUND false-negative) is **architecturally inherited** from the underlying retrieval — not a v4 regression. It will persist until the prompt explicitly mandates `gh api` license lookup as a step rather than a post-run analyst task.
- **Cross-wiki routing matrix** is mostly accurate when the primary-fit is clear; suggestions like "Cybersec stub for awesome-openbb" are awkward but harmless.
- **The single Adopt is genuine** and verifiable: `gamma-trade-lab/Polymarket-Near-Resolution-Bot` does exist on GitHub at the cited URL, has MIT in-file, and the described capability (CLOB mid-price scan for near-resolution favorites) matches the README.

### Reject list (recorded for completeness, no per-tool entity pages)

URLs 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 20, 23, 24, 27, 29, 32, 34, 35, 36, 37, 38, 39, 41, 42, 44, 47, 48, 49.

Of these, **9 have potential interest for Cemini if license verifies clean** (manual flag, not auto-promotion):

- URL 8 `ItzCrazyKns/Vane` — AI answering engine, OpenWebUI-style; potential local Cemini research assistant
- URL 13 `nex-crm/wuphf` — Multi-agent collaborative office; Claude-Code-aware
- URL 18 `CodeOne45/vex-tui` — Terminal CSV/Excel viewer; useful for librarian raw-data inspection
- URL 32 `Siva-Chidambaram12/kalshi-trading-bot` — Multi-agent AI Kalshi bot
- URL 36 `Composio-HQ/polymarket-kalshi-arbitrage-bot` — Composio is a serious company; license-flip plausible
- URL 39 `sanzoI-tech/polymarket-kalshi-arbitrage-bot` — Active CI, releases
- URL 42 `suislanchez/polymarket-kalshi-weather-bot` — GFS ensemble + Kelly sizing
- URL 44 `OctagonAI/kalshi-trading-bot-cli` — Real CLI distribution
- URL 48 `Jon-Becker/prediction-market-analysis` — **Already verified MIT in K52** (eval error)

## Snippets

> "Adopt: 1 — gamma-trade-lab/Polymarket-Near-Resolution-Bot (URL 5)" [Source: tool-evaluation-50urls-2026-05-21.docx — Aggregate Summary]

> "NO LICENSE FOUND: 31. Poison-pill licenses caught: 0 (Specifically identified via explicit text; 31 assumed proprietary due to missing data). Clean MIT / Apache / BSD: 1 (Polymarket-Near-Resolution-Bot - MIT)." [Source: tool-evaluation-50urls-2026-05-21.docx — License pattern summary]

> "the extreme failure rate due to NO LICENSE FOUND underscores the necessity for the automated post-run sequence ... the analyst must execute the following terminal command via Cursor against all rejected entities to retrieve latent SPDX identifiers before final knowledge-base ingestion: `gh api repos/<owner>/<repo> --jq '.license.spdx_id'`" [Source: tool-evaluation-50urls-2026-05-21.docx — Post-run Spot-check]

> "This repository fulfills a critical algorithmic requirement for the Cemini financial suite, explicitly providing Python 9 logic to scan Central Limit Order Book (CLOB) mid-pricing for heavily favored binary outcomes nearing expiration on Polymarket." [Source: tool-evaluation-50urls-2026-05-21.docx — URL 5 reasoning, gamma-trade-lab/Polymarket-Near-Resolution-Bot]

## Dead Ends

- **31 Reject entries do not become entity stubs.** Prior batches (K53, K54) experimented with auto-creating reject-stubs and found they polluted the wiki with low-signal pages requiring constant pruning. K55 batch confirms the decision: aggregate the Rejects in this source page, document the false-negative pattern, do not create per-tool stubs. If a specific Reject ever earns an independent license verification, it can be promoted at that point.
- **No automatic re-verification loop wired.** The eval's closing prescription (`gh api` post-run on all 31 Rejects) is **deliberately not run** as part of this ingest. Doing so would amplify the v4 prompt's NO LICENSE FOUND failure mode by validating it as a workflow expectation. The correct fix is upstream: v5 prompt should perform license lookup inline, not delegate it to the analyst.
