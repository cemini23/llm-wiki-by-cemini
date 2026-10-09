---
title: K283 — Basgiath Bedrock add-on extracts (routed brief, landed 2026-10-06)
type: source
tags: [source, triage, briefs, minecraft, bedrock, cross-wiki]
keywords: [simple-money, bedrock-ui-animations, books-addon, mc-mod-migrator, just-clock, roleplay-currency]
related:
  - concepts/minecraft-bedrock-addons-scripting.md
  - concepts/minecraft-modding-ecosystem.md
  - entities/tools/blockbench.md
  - sources/cross-wiki-routed-briefs-2026-10-05.md
  - meta/cross-wiki-routing.md
  - sources/k284-k285-basgiath-clip-tooling-2026-10-08.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-06
updated: 2026-10-07
---

## Raw Concept

Cross-wiki brief from OSINT batch K283, landed here 2026-10-06. A 20-row GitHub eval routed **13 rows to Basgiath** (the Bedrock fan map). Five clean **Extract** techniques were identified. The brief's own boundary is explicit and this page preserves it: **free, non-monetised fan project; in-game roleplay tokens only; no Marketplace; no official novel text.**

## Narrative

### The five extracts

| # | Repo | What it gives | Overlap |
|---|------|---------------|---------|
| 1 | [`Flower7C3/simple-money`](https://github.com/Flower7C3/simple-money) | Turnkey currency framework: multiple coin tiers, paper bills, crafting conversion recipes, an ATM block, packaged as `.mcaddon`. MIT (stated). Enables a cadet trading loop — dorm supplies, flight gear, a trading post | 0.80 |
| 2 | [`tfgh6/bedrock-ui-animations`](https://github.com/tfgh6/bedrock-ui-animations) | JSON UI easing curves, smooth progress-bar interpolation, transition keyframes. Best value-per-line in the batch | 0.85 |
| 3 | [`Flower7C3/books-minecraft-bedrock-addon`](https://github.com/Flower7C3/books-minecraft-bedrock-addon) | Custom readable items and paginated content beyond the vanilla book limit. Academy archives, dragon codices, flight manuals | 0.75 |
| 4 | [`kongbai9288/mc-mod-migrator`](https://github.com/kongbai9288/mc-mod-migrator) | Automated refactor of deprecated entity components and JSON UI tags across Mojang updates | 0.70 |
| 5 | [`Flower7C3/just-clock`](https://github.com/Flower7C3/just-clock) | On-screen clock via mcfunction hooks, no experimental flags. Timed obstacle courses, curfew challenges | 0.60 |

The docx lists `bedrock-ui-animations` twice (rows 13 and 20). It is **one repo**.

### Where each applies

- **UI easing** is the largest visual-quality gain for the least code — it targets the dragon-flight speedometer, altitude display, and stamina bar. Smoothing those is what makes HUD readouts look authored rather than debug.
- **The HUD timer** pairs with the Gauntlet's existing timing work, and needs no experimental flags, so it is safe on the stable `@minecraft/server` line.
- **Readable lore items** extend the vanilla book limit, which matters for an archive-heavy academy map.

### Gates that must hold

1. **Currency stays 100% in-game roleplay tokens.** No real-money transactions, no paid server perks, no Marketplace. This constraint is what makes the currency framework safe to use, and it is non-negotiable — the project is non-monetised.
2. **All lore text is original fan-written.** No official novel excerpts, no copyrighted passages. Label everything fan-made.
3. **Schema check on `mc-mod-migrator`.** The row's stack claims Java, and the sibling K282 batch already produced a Java tool that does not transfer to Bedrock. Verify the migrator targets **Bedrock** schema before relying on it. The reusable part is the migration *pipeline*, not necessarily the tool.

### Rejected in this batch

- **`void-community/Void`** — a modern .NET-10 proxy for **Java-Edition** modded servers (real repo `caunt/Void`, MIT). Bedrock has no equivalent proxy. **Goal match, stack mismatch** — the same failure mode as K282's `FabricModdingConventions`. Do not wire.
- **Texture packs, launchers, backup scripts, CS16MC** — Context only.
- **`roma234567/AUTOCLICKER`** — Pass. Unattended click automation violates the manual-operator gate.

### Relevance to this wiki beyond Basgiath

The batch is a worked example of the Bedrock add-on surface described in @concepts/minecraft-bedrock-addons-scripting.md: small MIT add-ons that ship a behaviour pack, a resource pack, and JSON UI, with no code beyond the Script API. The currency, book, and clock repos are each a self-contained demonstration of one pattern. The `.mcaddon` packaging convention appears in all of them.

## Dead Ends

- Monetising any of this. The boundary is explicit and the project is free.
- Taking `void-community/Void` as a Bedrock tool. It is a Java proxy.
- Trusting `mc-mod-migrator`'s Bedrock support without checking the schema it targets.
