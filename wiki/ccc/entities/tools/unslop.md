---
title: "unslop — Claude Code skill that audits and removes generic AI UI (CC-BY-4.0)"
type: entity
tags: [tool, claude-code, skill, frontend, design, atto]
keywords: [unslop, ai slop, purple gradient, design audit, claude skill, cc-by-4.0]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
  - entities/tools/boardui.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 18, **Integrate** tier. Routed to Atto portals and the Access-share screens.

The question this page answers: **how do you stop an agent from producing the same generic interface every time?**

## Narrative

### What it is

A Claude Code skill that audits a screen for a specific, nameable set of visual clichés and then rewrites it.

The tells it names: purple gradients, glowing blobs, emoji labels, uneven spacing.

### How it runs

1. **Audit** — list the visual problems with their location.
2. **Direction** — propose a design concept and **ask before changing anything**.
3. **Passes** — rework one dimension at a time: spacing, colour, icons, copy, type, layout, details, visuals, motion.

It edits the real source — Next.js, React, Vue, Svelte, Tailwind, or plain HTML/CSS. Optional Playwright plus Chromium to snapshot live sites or render a short story video; ffmpeg on `PATH` for the video.

Install: copy `skills/unslop` into `~/.claude/skills/`, or into a project's `.claude/skills/`.

### The gate that makes it usable

Step 2 stops and asks. That is the difference between a design tool and an agent that repaints a production page with no review. Keep it.

### Licence — Phase-0, 2026-11-02

**CC-BY-4.0**, confirmed. The attribution obligation is specific: redistributing the **skill files themselves** requires crediting Damir Sokolovsky (@heydamir) with a link back to the repository. CSS and React changes made to your own application are not affected.

For local use in `~/.claude/skills/`, nothing needs to be published. The obligation appears only if the skill is redistributed — for example inside an Atto kit.

### Why it fits Atto

The report ties this to conversion on the $499–$899 kits, the ≥$2,500 concierge, and the $8–20/month Access share. Those are pages a buyer looks at before paying.

The honest scope: this improves how a page reads, not whether the product is correct. It removes a class of visual default that signals "generated", which is a trust signal on a page whose whole claim is archival rigour.

### Caveats

- It **may offer to connect an image-generation service** for hero visuals. It asks first. On Atto, decline — the design language should not depend on a generative service that can produce invented imagery on an archival product.
- It edits real production files. Run it on a branch and read the diff.

### Status

Integrate. Local use, no attribution owed. Review the diff.

## Second sighting — 2026-11-04: the report contradicts a verified fact

`@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md` URL 20 re-surfaces this tool and records its licence as **"NOT FOUND"**, with the improvement line "None verified in crawl" — meaning the report did not retrieve the repository.

**The licence was verified on 2026-11-02: CC-BY-4.0**, with the attribution obligation applying only to redistribution of the skill files. This page is correct and the report is not.

The tool has now appeared in **two** batches and been downgraded to "unindexed" in the second. That is a retrieval failure on the eval side, not a change in the world — and it is the clearest illustration in this batch of why every licence line needs a Phase-0 pass rather than a citation.

## Snippets

> "It also edits real source code and may offer to connect an image-generation service — it asks first." [README, fetched 2026-11-02]

> "The credit must name Damir Sokolovsky (@heydamir) and link back to the repository." — CC-BY-4.0 terms as stated in the README [fetched 2026-11-02]

## Dead Ends

- **Letting it wire an image generator into an archival product.** Generated hero imagery on a page about record authenticity is the wrong signal.
- **Redistributing the skill files without attribution.** CC-BY-4.0 requires it.
