---
title: "JEV TIP 001 — skill classify before prompt inject (@parcadei)"
type: source
tags: [source, k266, ccc, jev, skills]
keywords: [k266, Jev, skill routing, prompt injection, route-task, TIP format]
related:
  - concepts/k266-ccc-jev-x-wave.md
  - sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
  - entities/tools/jev-mcp.md
  - sources/x-article-0xmovez-jev-engineering-2026-09-19.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
read_status: read
---

## Relations

- @sources/x-article-0xmovez-jev-engineering-2026-09-19.md
- @concepts/k266-ccc-jev-x-wave.md
- @sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
- @entities/tools/jev-mcp.md

## Raw Concept

| File | `x-post-parcadei-jev-tip-001-skill-classify-2026-09-19.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-post-parcadei-jev-tip-001-skill-classify-2026-09-19.md` |
| Retrieved | 2026-09-19 |
| Dual-ID | **OSINT K266** |
| Author | @parcadei — post id `2101132368949993830` |
| Kind | Short post — JEV TIP 001 |
| Metrics | 421 likes · 416 bookmarks · 32,472 impressions (X MCP 2026-09-19) |
| sha256 | `0a054dcc17ea792267d3644a9b3917d405f2f548cbf5a880fb41d1724180a72f` |

## Narrative

Shortest and highest like-to-impression entry in the wave: **421 likes on 32,472 impressions**. One tip, one job.

**The tip.** Stop spending main-model tokens on deciding which skill to load. Use Jev to **classify the task against skill names plus short descriptions**, then inject the selected skill directly into the prompt before the prompt reaches the main model.

This is a skill-router pattern: a cheap classification call replaces a full model pass spent on the same decision. It sits next to the LangChain model-routing and Auto Mode patterns from @sydneyrunkle — same underlying move, applied at the skill boundary rather than the model or tool boundary.

**CCC reading.** FILE. The workspace already has `route-task` / `/route` and a Cursor skill catalog. A skill-name classifier **could** be a HITL experiment: build the candidate list from skill names plus one-line descriptions, let the classifier pick, and log the choice for review. **Do not replace `route-task` or `/route`.** Do not auto-load skills from a classifier score. **0 product Integrate GO.**

**Cemini23 voice note.** The **`TIP 00N`** format is the transferable artifact — a numbered one-tip post with a single instruction and no funnel. See `@briefs/2026-09-19_k266-seo-voice.md`.

## Snippets

> "JEV TIP 001: Stop wasting your main model's tokens figuring out which skill to load. Use JEV to classify the task against skill names + short descriptions, then inject the selected skill directly into the prompt before it reaches the model" [Source: x-post-parcadei-jev-tip-001-skill-classify-2026-09-19.md]
