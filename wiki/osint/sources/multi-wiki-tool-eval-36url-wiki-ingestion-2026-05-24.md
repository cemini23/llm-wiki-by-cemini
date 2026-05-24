---
title: "Multi-Wiki Link Evaluation — 36-URL batch (v4, Wiki Ingestion, May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki-routing, license-audit, k63]
keywords: [36-url, openevolve, dataset-viewer, awesome-cursorrules, nidhogg, tradingagents-cn, graphcast, weather-bot, cursor-ecosystem, license-corrections]
related:
  - concepts/cemini-license-posture.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/tools/openevolve.md
  - entities/tools/dataset-viewer.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/claude-code-game-studios.md
  - entities/tools/nidhogg.md
  - entities/tools/tradingagents-cn.md
  - entities/tools/graphcast.md
  - entities/tools/superalgos.md
  - entities/tools/openpatchlab-polymarket-weather-trading-bot.md
  - entities/tools/katbrink-polymarket-weather-trading-bot.md
  - entities/tools/tsukamg-polymarket-weather-trading-engine.md
  - entities/tools/agents-best-practices.md
  - entities/tools/freqtrade.md
  - concepts/multi-agent-trading.md
  - sources/tradingagents.md
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - sources/multi-wiki-tool-eval-26url-2026-05-19.md
  - sources/multi-wiki-tool-eval-19url-2026-05-20.md
maturity: validated
read_status: deep-read
created: 2026-05-24
updated: 2026-05-24
clusters: [tool-evaluation]
---

## Relations

- @concepts/cemini-license-posture.md — sixth multi-wiki eval reinforcing license-layer unreliability
- @concepts/polymarket-weather-trading-strategy.md — URLs 19–20, 23 + Tsukamg weather corrections
- @entities/tools/freqtrade.md — URL 30 GPL reaffirm
- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — prior v4 20-URL batch (K60)
- @ccc-wiki/briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md
- @cybersecurity-wiki/briefs/2026-05-24_k63-cybersec-nidhogg-from-osint.md
- @seo-wiki/briefs/2026-05-24_k63-weather-icons-ui-from-osint.md

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation Report (v4) — Tool Evaluation for Wiki Ingestion
- **Type**: LLM multi-wiki tool-eval (36 GitHub URLs)
- **Location**: `research to be indexed/Tool Evaluation for Wiki Ingestion.docx` → `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation for Wiki Ingestion.docx`
- **Retrieved**: 2026-05-24
- **Read status**: deep-read + `gh api` license spot-check on all 36 repos

## Narrative

### Tier rollup (eval vs API-corrected 2026-05-24)

| Tier | Eval | After verification | Notes |
|------|------|-------------------|--------|
| Adopt | 5 | **2** | openevolve, awesome-cursorrules — **3 downgraded** (dataset-viewer, community-plugins, TradingAgents-CN — license/metadata gaps) |
| Steal-from | 3 | **4** | + Tsukamg weather (eval Reject → MIT); Nidhogg, Claude-Code-Game-Studios, weather-icons |
| Defer | 4 | **6** | agents-best-practices, ECC, graphcast, Superalgos + OpenPatchLab + Katbrink (ex-UNAVAILABLE) |
| Reference-only | 5 | **7** | paper list, cursor, avante.nvim, wego, earth, genuinetools/weather |
| Reject | 14 | **15** | + piracy/cursor-abuse cluster; freqtrade/backtrader GPL reaffirmed |
| UNAVAILABLE | 4 | **0** | All four resolved via `gh api` — two MIT weather bots promoted; three PM bots lack LICENSE file |

### Per-URL table (corrected posture)

| # | Repo | Eval | License (API) | Corrected | Primary |
|---|------|------|---------------|-----------|---------|
| 1 | [Nidhogg](https://github.com/Idov31/Nidhogg) | Steal-from | GPL-3.0 | Steal-from (cybersec) | Cybersec |
| 2 | [openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | Adopt | Apache-2.0 | **Adopt** (CCC) | CCC |
| 3 | [vbsec](https://github.com/tanviet12/vbsec) | Reject | **MIT** | Reject (eval wrong on license; 193★ but shell-scan skill — out of scope) | — |
| 4 | [bb-huge](https://github.com/ShulkwiSEC/bb-huge) | Reject | NONE | Reject | — |
| 5 | [dataset-viewer](https://github.com/stardustai/dataset-viewer) | Adopt | **NONE** | **CONDITIONAL-GO** — README MIT badge, no LICENSE file | OSINT |
| 6 | [agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) | Defer | MIT | Defer (CCC) | CCC |
| 7 | [Awesome-LLM-Quantitative-Trading-Papers](https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers) | Reference | NONE | Reference-only (reading list) | OSINT |
| 8 | [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Steal-from | MIT | Steal-from (CCC harness) | CCC |
| 9 | [cursor](https://github.com/cursor/cursor) | Reference | NONE | Reference-only (issues tracker) | CCC |
| 10 | [cursor-auto-free](https://github.com/chengazhen/cursor-auto-free) | Reject | NONE | Reject (NC license / abuse) | — |
| 11 | [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | Adopt | CC0-1.0 | **Adopt** (CCC rules catalog) | CCC |
| 12 | [go-cursor-help](https://github.com/yuaotian/go-cursor-help) | Reject | MIT | Reject (ToS circumvention) | — |
| 13 | [Captura](https://github.com/MathewSachin/Captura) | Reject | MIT | Reject (screen capture — domain) | — |
| 14 | [cursor-vip](https://github.com/kingparks/cursor-vip) | Reject | MIT | Reject (piracy) | — |
| 15 | [community-plugins](https://github.com/cursor/community-plugins) | Adopt | **NONE** | **CONDITIONAL-GO** — no LICENSE file | CCC |
| 16 | [ECC](https://github.com/affaan-m/ECC) | Defer | MIT | Defer (~190k★ — Phase-0 before any extract) | CCC |
| 17 | [avante.nvim](https://github.com/yetone/avante.nvim) | Reference | Apache-2.0 | Reference-only (Neovim agent UI) | CCC |
| 18 | [cursor2api](https://github.com/7836246/cursor2api) | Reject | MIT | Reject (proxy abuse; eval NO LICENSE wrong) | — |
| 19 | [OpenPatchLab/polymarket-weather-trading-bot](https://github.com/OpenPatchLab/polymarket-weather-trading-bot) | UNAVAILABLE | MIT | **Defer** — 147★; Phase-0 vs K60 cluster | Cemini |
| 20 | [Tsukamg/polymarket-weather-trading-engine](https://github.com/Tsukamg/polymarket-weather-trading-engine) | Reject | **MIT** | **CONDITIONAL-GO** — eval false NO LICENSE | Cemini |
| 21 | [graphcast](https://github.com/google-deepmind/graphcast) | Defer | Apache-2.0 | Defer (DeepMind weather ML) | OSINT |
| 22 | [SwiftLanguageWeather](https://github.com/JakeLin/SwiftLanguageWeather) | Reject | MIT | Reject (iOS sample app) | — |
| 23 | [Katbrink/polymarket-weather-trading-bot](https://github.com/Katbrink/polymarket-weather-trading-bot) | UNAVAILABLE | MIT | **Defer** — 136★ | Cemini |
| 24 | [bkhezry/weather](https://github.com/bkhezry/weather) | Reject | Apache-2.0 | Reject (Android weather app) | — |
| 25 | [genuinetools/weather](https://github.com/genuinetools/weather) | Reject | MIT | Reference-only (CLI weather) | OSINT |
| 26 | [wego](https://github.com/schachmat/wego) | Reference | ISC | Reference-only (terminal weather) | OSINT |
| 27 | [weather-icons](https://github.com/erikflowers/weather-icons) | Steal-from | NONE | Steal-from UI patterns (SEO); no LICENSE file | SEO |
| 28 | [earth](https://github.com/cambecc/earth) | Reference | MIT | Reference-only (wind viz) | OSINT |
| 29 | [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | Adopt | **NOASSERTION** | **CONDITIONAL-GO** — verify license file before import | Cemini |
| 30 | [freqtrade](https://github.com/freqtrade/freqtrade) | Reject | GPL-3.0 | Reject (existing @entities/tools/freqtrade.md) | — |
| 31 | [Superalgos](https://github.com/Superalgos/Superalgos) | Defer | Apache-2.0 | Defer (visual bot builder; heavy) | Cemini |
| 32–34 | mila89 / heyFive-dev / ShinyaTomitsuka PM bots | UNAVAILABLE | NONE | Reject — no LICENSE file (~262–267★) | — |
| 35 | [polymarket-copy-trading-bot](https://github.com/Parallax-Trading/polymarket-copy-trading-bot) | Reject | NONE | Reject | — |
| 36 | [backtrader](https://github.com/mementum/backtrader) | Reject | GPL-3.0 | Reject (GPL; legacy) | — |

### Cemini-relevant headlines

1. **openevolve** (Apache-2.0, ~6.4k★) — evolutionary coding agent (AlphaEvolve-class); CCC Adopt for harness token/routing optimization.
2. **awesome-cursorrules** (CC0-1.0, ~40k★) — rules catalog for `.cursor/rules`; CCC Adopt as pattern library (not blind copy).
3. **TradingAgents-CN** (~27k★) — Chinese fork of multi-agent trading framework; overlaps @sources/tradingagents.md (Tauric paper) but separate codebase — CONDITIONAL-GO pending license clarity.
4. **Weather bot UNAVAILABLE fixes** — OpenPatchLab + Katbrink are MIT with ~140★ each; Tsukamg engine MIT — add to weather Phase-0 queue alongside K60 suislanchez.
5. **Cursor abuse cluster** — reject cursor-vip, go-cursor-help, cursor-auto-free, cursor2api regardless of MIT (operational / legal risk).

### Cross-wiki routing

- **CCC-wiki brief** — openevolve, awesome-cursorrules, Claude-Code-Game-Studios, agents-best-practices, ECC, community-plugins
- **Cybersec-wiki brief** — Nidhogg (GPL steal-from patterns only)
- **SEO-wiki brief** — weather-icons CSS patterns

### Reject discipline

Fourteen eval Rejects + five license-downgraded Adopts aggregated here. **No per-repo reject-stub farm** for 1★ HTML hubs or cursor piracy tools.

## Snippets

> "Strict adherence to intellectual property hygiene… GPL-3.0 or lacking explicit license metadata is systematically categorized." [Source: Tool Evaluation for Wiki Ingestion.docx, 2026-05-24]

> "openevolve… open-source implementation of AlphaEvolve… optimizing token budgets." [Source: same, URL 2]
