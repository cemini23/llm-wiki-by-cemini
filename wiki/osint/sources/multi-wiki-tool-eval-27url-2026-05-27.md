---
title: "Multi-Wiki Tool Evaluation — 27-URL Audit (May 2026, K71)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, k71]
keywords: [tool-evaluation, camofox, polyweather, metatrader-mcp, automaton, karpathy-skills, stock-screener]
related:
  - entities/tools/camofox-browser.md
  - entities/tools/xang1234-stock-screener.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/tools/polyweather.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
  - sources/arxiv-epicure-food-embeddings-2605.22391.md
maturity: validated
read_status: deep-read
created: 2026-05-27
updated: 2026-05-27
clusters: [cemini-internal]
---

## Relations

- @entities/tools/camofox-browser.md — K71 OSINT Adopt (MIT; npm server)
- @entities/tools/xang1234-stock-screener.md — K71 Steal-from (Apache-2.0)
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — URL 2 reconfirm no LICENSE
- @entities/tools/polyweather.md — URL 3 AGPL hard reject
- @concepts/cemini-license-posture.md
- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — prior batch (22 URL)
- @sources/arxiv-epicure-food-embeddings-2605.22391.md — K71 co-ingest (Epicure arXiv)

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation (27 URLs) — *Tool Evaluation Prompt Analysis* (new sha256 vs K68)
- **Retrieved**: 2026-05-27
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation Prompt Analysis.docx`
- **Read status**: deep-read

## Narrative

Twenty-seven URLs. **GitHub API spot-check** on all Adopt/Steal-from rows (2026-05-27). Key corrections:

| Repo | Eval | Verified |
|------|------|----------|
| multica-ai/andrej-karpathy-skills | Adopt MIT | **No LICENSE** → Reference-only (CCC brief, not install) |
| suislanchez/polymarket-kalshi-weather-bot | Steal MIT | **No LICENSE file** — unchanged from K60 |
| PolyWeather | Reject AGPL | **AGPL-3.0 confirmed** |
| automaton | Reject (malware) | MIT license but **Reject on security** (wallet drain #245) |
| camofox-browser | Adopt | **MIT** — laptop `npm install -g camofox-browser` |

### Tier counts (post-verify)

| Tier | Count |
|------|------:|
| Adopt | 7 (was 8; karpathy-skills demoted) |
| Steal-from | 4 |
| Reference-only | 3 |
| Defer | 2 |
| Reject | 11 |

### OSINT pages from this batch

- **New:** @entities/tools/camofox-browser.md, @entities/tools/xang1234-stock-screener.md
- **Updated:** @entities/tools/polyweather.md (K71 AGPL note)

Cross-wiki briefs staged: **ccc-wiki**, **seo-wiki**, **cybersecurity-wiki** (see `briefs/2026-05-27_k71-*-from-osint.md`).

CCC pages: `@ccc-wiki/entities/tools/metatrader-mcp-server.md`, `three-man-team`, `claude-subconscious`, `council-of-high-intelligence`, `open-claude-code`, `mercury-agent-skills`, `solo-founder-superpowers`, `build-your-own-openclaw`, `ai-infra-engineer-learning`, `andrej-karpathy-skills-multica`, `bmad-creative-intelligence-suite`.

## URL ledger (eval + verify)

| # | Item | Tier | Primary | Verified license | Notes |
|---|------|------|---------|----------------|-------|
| 1 | [Hacking Artificial Intelligence – E](https://hackers-arise.com/hacking-artificial-intelligence-ai-enumerating-ai-systems/) | Reference-only | Cybersec | — |  |
| 2 | [polymarket-kalshi-weather-bot](https://github.com/suislanchez/polymarket-kalshi-weather-bot) | Steal-from | Cemini financial | NO LICENSE | Steal-from unchanged — K60 |
| 3 | [PolyWeather](https://github.com/yangyuan-zhen/PolyWeather) | Reject | — | AGPL-3.0 | Reject confirmed |
| 4 | [polymarket-weather-bot](https://github.com/AadiXD200/polymarket-weather-bot) | Reject | — | — |  |
| 5 | [kalshi-polymarket-trader](https://github.com/erickdronski/kalshi-polymarket-trader) | Reject | — | — |  |
| 6 | [metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) | Adopt | CCC | MIT | Adopt stands |
| 7 | [bbot](https://github.com/blacklanternsecurity/bbot) | Reject | — | AGPL-3.0 | Reject confirmed |
| 8 | [automaton](https://github.com/Conway-Research/automaton) | Reject | — | MIT | Reject security — key exfil #245 |
| 9 | [machine-learning-refined](https://github.com/neonwatty/machine-learning-refined) | Reject | — | — |  |
| 10 | [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Adopt | CCC | NO LICENSE | Adopt → Reference-only; gh license null |
| 11 | [most-capable-agent-system-prompt](https://github.com/fainir/most-capable-agent-system-prompt) | Reject | — | — |  |
| 12 | [three-man-team](https://github.com/russelleNVy/three-man-team) | Adopt | CCC | MIT | Adopt stands |
| 13 | [claude-ads](https://github.com/AgriciDaniel/claude-ads) | Defer | SEO | — |  |
| 14 | [NotFair (toprank)](https://github.com/nowork-studio/NotFair) | Adopt | SEO | MIT | Adopt stands |
| 15 | [context-mode](https://github.com/mksglu/context-mode) | Reject | — | — |  |
| 16 | [autoskills](https://github.com/midudev/autoskills) | Reject | — | — |  |
| 17 | [claude-subconscious](https://github.com/letta-ai/claude-subconscious) | Adopt | CCC | MIT | Adopt stands |
| 18 | [camofox-browser](https://github.com/jo-inc/camofox-browser) | Adopt | OSINT | MIT | Adopt stands |
| 19 | [build-your-own-openclaw](https://github.com/czl9707/build-your-own-openclaw) | Reference-only | CCC | — |  |
| 20 | [mercury-agent-skills](https://github.com/cosmicstack-labs/mercury-agent-skills) | Steal-from | CCC | — |  |
| 21 | [ai-infra-engineer-learning](https://github.com/ai-infra-curriculum/ai-infra-engineer-learning) | Reference-only | Cemini financial | — |  |
| 22 | [bmad-module-creative-intelligence-s](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite) | Defer | CCC | — |  |
| 23 | [stock-screener](https://github.com/xang1234/stock-screener) | Steal-from | Cemini financial | Apache-2.0 | Steal-from stands |
| 24 | [regime_model](https://github.com/QuhiQuhihi/regime_model) | Reject | — | — |  |
| 25 | [council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | Adopt | CCC | MIT | Adopt stands |
| 26 | [open-claude-code](https://github.com/ruvnet/open-claude-code) | Adopt | CCC | MIT | Adopt stands |
| 27 | [solo-founder-superpowers](https://github.com/whawkinsiv/solo-founder-superpowers) | Steal-from | CCC | MIT | Steal-from stands |

## Snippets

> "Camofox provides a highly optimized drop-in Playwright replacement that natively evades these blocks." [Source: Tool Evaluation Prompt Analysis.docx URL 18 — actual deploy is npm REST server, 2026-05-27]

> "AGPL-3.0 … would legally force the open-sourcing of the proprietary Cemini algorithmic trading stack." [Source: Tool Evaluation Prompt Analysis.docx URL 3 PolyWeather]
