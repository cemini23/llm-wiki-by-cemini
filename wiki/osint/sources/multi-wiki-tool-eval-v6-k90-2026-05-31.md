---
title: "Multi-Wiki Tool Evaluation (v6 prompt, K90 batch — 41 URLs)"
type: source
tags: [source, gemini-deep-research, tool-eval, v6-prompt, license-corrections, k90, gambling-wiki]
keywords: [autohedge, harrier, polymarket-skills, polybot, finrl, sports-betting, fredbet, hyperframes, hermes-desktop]
related:
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/cemini-license-posture.md
  - concepts/tool-evaluation-framework.md
  - concepts/polymarket-bot-architecture.md
  - concepts/gambling-wiki-federation.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/tools/polybot.md
  - entities/tools/harrier-pm-toolkits.md
  - entities/tools/polymarket-skills-mjunaidca.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - "@gambling-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md"
  - "@ccc-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md"
  - "@ccc-wiki/entities/tools/npxskillui.md"
  - "@ccc-wiki/entities/tools/hermes-desktop.md"
  - "@ccc-wiki/entities/tools/everything-claude-code.md"
  - "@ccc-wiki/entities/tools/librechat.md"
  - "@ccc-wiki/entities/tools/skyhook-radar.md"
  - "@ccc-wiki/sources/trading-posts-compilation-16-2026-05-31.md"
  - "@ccc-wiki/concepts/agent-personality-file-hermes-openclaw.md"
  - "@ccc-wiki/concepts/nine-stage-agent-team-production.md"
  - "@ccc-wiki/concepts/remote-hermes-access-pattern.md"
  - "@ccc-wiki/concepts/ai-agents-learning-roadmap-reference.md"
  - "@ccc-wiki/concepts/claude-artifacts-app-building.md"
  - entities/tools/goaccess.md
maturity: draft
read_status: deep-read
created: 2026-05-31
updated: 2026-06-01
---

## Relations
- @gambling-wiki/briefs/2026-05-31_k90-gambling-tool-eval-from-osint.md  (cross-wiki brief)

- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — prior v5 batch; v6 adds **gambling-wiki** as 8th surface
- @concepts/gambling-wiki-federation.md — first v6 batch with gambling-primary routing
- @concepts/cemini-license-posture.md — NO LICENSE false-negative pattern continues on gambling weather bots

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report (Batch v6, May 2026) |
| **Author** | Gemini Deep Research (v6 multi-wiki eval prompt) |
| **Type** | docx |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-tool-eval-v6-k90-2026-05-31.docx` |
| **Retrieved** | 2026-05-31 |
| **URLs** | 41 evaluated |
| **Read status** | deep-read + `gh api` license spot-check (`.local/reports/license-spot-check-2026-05-31-1923.txt`) |

## Narrative

K90 v6 batch: first eval run with **gambling-wiki** surface. PM bot/tool cluster re-evaluated under world-cup-bot gap-fill rule. **Weather-bot URL graveyard:** 5 UNAVAILABLE + 4 Reject — do not re-evaluate dead GitHub paths.

### Gemini aggregate (as reported)

| Tier | Count | Headlines |
|------|-------|-----------|
| Adopt | 10 | AutoHedge, claude-ads, hyperframes, npxskillui, Harrier PM toolkits, hermes-desktop, ECC, goaccess, polymarket-skills, polymarket-mcp-server |
| Steal-from | 5 | polybot, FinRL, AlphaPy, georgedouzas/sports-betting, fredbet |
| Defer | 2 | Open-Generative-AI, skyhook-io/radar |
| Reference-only | 4 | LibreChat, Awesome-Vision-World-Model, deepresearch, ATPBetting |
| Reject | 13 | VTuber stack, roboto_origin (GPL), CloddsBot, PolyWeather (AGPL), offensive-claude, ai-security-arsenal, EpicStaff, BeatTheBookie (GPL), weather bots, pretrehr duplicate, ChatGPT sports bot |
| UNAVAILABLE | 7 | polymarket_lp_tool, hydra-node weather, GastonDeMichele, GuillermoEguilaz, jd5688, risedownlabs, srlesrle |

### License corrections after `gh api` [CONFIRMED 2026-05-31]

| URL | Gemini | Verified | Action |
|-----|--------|----------|--------|
| hypnguyen1209/offensive-claude | Reject (cyber) | **MIT** | Reject upheld — wrong domain / prompt-injection toy, not offensive tradecraft adopt |
| alsk1992/CloddsBot | Reject | **MIT** | Reject upheld — overlaps world-cup-bot; no gap-fill |
| yangyuan-zhen/PolyWeather | Reject | **AGPL-3.0** | Reject upheld — copyleft + weather-bot graveyard |
| Lisandro79/BeatTheBookie | Reject | **GPL-3.0** | Reject upheld — GPL poison pill |
| edouardthom/ATPBetting | Reference | **null** | Reference-only; R tennis models, not prod adopt |
| pretrehr/Sports-betting | Reject | **MIT** | Reject upheld — duplicate of georgedouzas/sports-betting (steal-from) |
| mjunaidca/polymarket-skills | Adopt | **null** | Adopt → Phase-0 pending; verify LICENSE file before install |
| Roboparty/roboto_origin | Reject | **GPL-3.0** | Reject upheld |
| heygen-com/hyperframes | Adopt | **Apache-2.0** | Image-gen primary |
| fred4jupiter/fredbet | Steal-from | **MIT** | Gambling-wiki steal-from (social betting app patterns) |

### OSINT-priority outcomes

1. **HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits (Adopt → Phase-0 pending)** — MIT; toolkit inventory for PM bot modules; see `@entities/tools/harrier-pm-toolkits.md`.
2. **mjunaidca/polymarket-skills (Adopt → Phase-0 pending)** — Claude Skills for PM; null LICENSE on API — verify before install; see `@entities/tools/polymarket-skills-mjunaidca.md`.
3. **caiovicentino/polymarket-mcp-server (Adopt reaffirmed)** — already Wave 5B validated; K90 confirms gap-fill still valid vs world-cup-bot.
4. **ent0n29/polybot (Steal-from reaffirmed)** — MIT; Python strip-mine only; see `@entities/tools/polybot.md`.
5. **FinRL / AlphaPy (Steal-from → Cemini financial)** — prod brief only; not OSINT entity bodies.

### Gambling-wiki routing (8 primary-fit URLs)

| Tier | Repo | Notes |
|------|------|-------|
| Reference-only | edouardthom/ATPBetting | Tennis ML; no LICENSE file |
| Steal-from | georgedouzas/sports-betting | MIT; dataloader / backtest patterns |
| Steal-from | fred4jupiter/fredbet | MIT; social betting UX |
| Reject | MoonsatProtocol/Polymarket-Weather-Bot | null license; weather-bot graveyard |
| Reject | Lisandro79/BeatTheBookie | GPL-3.0 |
| Reject | ryankrumenacker/sports-betting-arbitrage-project | null |
| Reject | pretrehr/Sports-betting | duplicate |
| Reject | llSourcell/ChatGPT_Sports_Betting_Bot | null; tutorial quality |

**Brief:** `Gambling wiki/briefs/2026-05-31_k90-gambling-tool-eval-from-osint.md`

### Cross-wiki routing (other surfaces)

| Target | Items | Brief |
|--------|-------|-------|
| **ccc-wiki** | npxskillui, hermes-desktop, affaan-m/ECC, LibreChat ref, radar Defer | `Cemini claude code CCC/briefs/2026-05-31_k90-ccc-tool-eval-from-osint.md` |
| **seo-wiki** | claude-ads, goaccess | `SEO:GEO B&M Business/briefs/2026-05-31_k90-seo-tools-from-osint.md` |
| **image-gen-wiki** | hyperframes Adopt, Open-Generative-AI Defer, VTuber Reject | tangential — no brief unless operator requests |
| **Cemini financial** | AutoHedge Adopt, FinRL/AlphaPy steal-from | `briefs/2026-05-31_k90-cemini-financial-tool-eval.md` |

## Snippets

> "v6 protocol adds Gambling wiki as surface 3 — retail wagering and sports-betting OSS only; OSINT retains PM bots and CeminiSuite integration." [Source: multi-wiki-tool-eval-v6-k90-2026-05-31.docx]

> "Weather-bot GitHub URLs remain a high-noise cluster: seven UNAVAILABLE rows in a single batch." [Source: multi-wiki-tool-eval-v6-k90-2026-05-31.docx]
