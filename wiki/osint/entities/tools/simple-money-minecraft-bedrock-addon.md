---
title: "Flower7C3/simple-money — in-game currency addon for Bedrock"
type: entity
tags: [tool, minecraft, bedrock, economy, basgiath, k283]
keywords: [simple-money, bedrock, in-game-currency, atm-block, mcaddon, basgiath, k283]
related:
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - concepts/k283-eval-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-bedrock-ecosystem-2026-10-06.md — K283 eval (tier: Extract, Basgiath 0.80)
- @concepts/k283-eval-wave.md — K283 cluster hub

## Raw Concept

- **Repo:** `github.com/Flower7C3/simple-money-minecraft-bedrock-addon`
- **Tier (K283):** **Extract** (Basgiath overlap 0.80)
- **License:** **MIT** (stated)
- **Stack:** Python 93.2%, Shell 6.5%, mcfunction 0.3%, Bedrock JSON
- **Docx metadata:** 1★ / last commit 6 months ago

## Narrative

A turnkey **in-game currency framework**: multiple coin tiers, paper bills, crafting conversion recipes, and an **ATM block**, packaged as `.mcaddon`.

### Why it matters here

Basgiath's academy world wants a cadet trading loop — dorm supplies, dragon-flight gear, a trading post. This provides the primitives. **Critically, it is 100% in-game roleplay currency**, which satisfies the Basgiath non-monetization rule.

### Boundary

**Currency must stay in-game roleplay tokens.** No real-money transactions, no paid server perks, no Minecraft Marketplace monetization. Verify behaviour-pack interactions when combined with custom entity packs. Companion to the K282 packaging standard.

## Snippets

> "Purely virtual in-game currencies satisfy all Basgiath non-monetization constraints while significantly enriching roleplay depth." [Source: eval-bedrock-ecosystem-2026-10-06.md]
