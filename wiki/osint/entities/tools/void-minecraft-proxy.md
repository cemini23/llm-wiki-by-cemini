---
title: "Void — Minecraft proxy for modded servers (caunt/Void)"
type: entity
tags: [tool, minecraft, proxy, java, basgiath, k283]
keywords: [void, caunt-void, minecraft-proxy, bungeecord, java-edition, bedrock, goal-match-stack-mismatch, k283]
related:
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - concepts/k283-eval-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-bedrock-ecosystem-2026-10-06.md — K283 eval (tier: Extract, but see note)
- @concepts/k283-eval-wave.md — K283 cluster hub

## Raw Concept

- **Repo (docx):** `github.com/void-community/Void` — **likely incorrect URL**
- **Repo (works-cited):** `github.com/caunt/Void` — "Minecraft Proxy for Modded Servers"
- **Tier (K283):** **Extract** (docx) — **re-classed Goal-match / Stack-mismatch**
- **License:** **MIT** (real repo)
- **Stack:** C# (.NET 10), Docker, Kubernetes

## Narrative

A modern, high-performance **proxy for modded Minecraft servers** — an alternative to the legacy BungeeCord proxy, with async packet routing and container deployment for multi-world scaling.

### The correction

The docx names `void-community/Void`, but its own works-cited resolves the real project to **`caunt/Void`**. Treat `void-community/Void` as a likely dead/incorrect URL.

More importantly: **Void proxies Java-Edition servers.** Basgiath is a **Bedrock** add-on, and Bedrock Dedicated Server has no BungeeCord-style proxy in this batch. So the row is a **goal match, stack mismatch** — the same pattern as K282's Java-Fabric `FabricModdingConventions`. The technique to watch is *how* a proxy shards worlds; the tool itself does not apply.

### Why it still earns a page

It is the clearest example of the recurring K281–K283 failure mode: a generated URL list that conflates Java and Bedrock tooling. Recording it stops the next ingest from re-scoring the same mistake.

## Snippets

> "Void — Minecraft Proxy for Modded Servers." [Source: eval-bedrock-ecosystem-2026-10-06.md, works cited]
