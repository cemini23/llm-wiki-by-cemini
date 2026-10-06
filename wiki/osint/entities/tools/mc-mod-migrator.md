---
title: "kongbai9288/mc-mod-migrator — automated Bedrock schema migration"
type: entity
tags: [tool, minecraft, bedrock, basgiath, migration, k283]
keywords: [mc-mod-migrator, bedrock, schema-migration, json, basgiath, mojang, k283]
related:
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - concepts/k283-eval-wave.md
  - concepts/k282-level-editors-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-bedrock-ecosystem-2026-10-06.md — K283 eval (tier: Extract, Basgiath 0.70)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @concepts/k282-level-editors-wave.md — Bedrock packaging wave (K282)

## Raw Concept

- **Repo:** `github.com/kongbai9288/mc-mod-migrator`
- **Tier (K283):** **Extract** (Basgiath overlap 0.70)
- **License:** NOT FOUND (docx)
- **Stack:** Python / Java (claimed)
- **Docx metadata:** NOT FOUND

## Narrative

Automated **add-on component migration** and schema conversion across breaking Minecraft engine updates — refactor deprecated JSON components and JSON UI tags so an add-on keeps loading after a Mojang update.

### Why it matters here

Complex Bedrock add-ons break when Mojang deprecates entity components. Basgiath's pack will face the same monthly churn. **The useful idea is the migration pipeline, not the code.** Companion to the K282 packaging standard (`.mcaddon`, matched UUID pairs).

### Boundary

**Automated schema transforms must be regression-tested** — a silent entity-behaviour corruption is worse than a load failure. Also verify the row actually targets **Bedrock** schema; the stack says Java, and in K282 a Java-Fabric tool was a goal-match / stack-mismatch Pass. Same check applies here.

## Snippets

> "Rapid version updates from Mojang frequently deprecate entity components and JSON UI tags, creating ongoing maintenance overhead for complex add-ons." [Source: eval-bedrock-ecosystem-2026-10-06.md]
