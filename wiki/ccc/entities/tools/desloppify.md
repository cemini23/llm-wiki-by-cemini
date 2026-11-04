---
title: "desloppify — code health harness (custom licence, NOT open source)"
type: entity
tags: [tool, code-health, agents, licence-restricted, cleanup]
keywords: [desloppify, code health, dead code, duplication, triage queue, blind scoring, licence]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 17, **Extract** tier. Routed to game-time, Atto, and Collectibles.

The question this page answers: **what does a code-health loop look like when it is a queue rather than a report?**

## Narrative

### What it does

"An agent harness to make your slop code well-engineered and beautiful." 4.0k stars, 919 commits, 29 languages.

It merges two kinds of check:

- **Mechanical** — dead code, duplication, complexity, test gaps.
- **LLM review** — naming, abstractions, module boundaries.

Then it maintains a **prioritised fix loop with persistent state in `.desloppify/`**, surviving across sessions. It can run as a full-codebase gate in CI.

### The pattern worth taking

Most code-quality tools produce a report. A report is read once and abandoned. This produces a **queue** that persists — which is the difference between a suggestion and work that actually gets done across many sessions.

The scoring split the report names, **25% mechanical and 75% blind LLM judgement**, is the other piece. "Blind" matters: the reviewer does not see which commit or author produced the code, so it scores the artefact rather than the story.

Both of those ideas transfer without the tool.

### Phase-0, 2026-11-03 — the licence is the finding

The report lists this as "Custom license (free for any individual developer working independently or at a company for their own work, an…" — truncated mid-sentence, and the truncation hides the constraint.

The repository page says:

- Free for **any individual**, whether independent or at a company, **for their own work**.
- Free for **open-source companies**, including commercial use.
- **For-profit, closed-source companies that want to commercialise it are directed to the LICENSE file for pricing.**

So it is **not an OSI licence** and it is **not simply free**. There is a commercial tier behind a custom agreement.

**What this decides:**

| Use | Position |
|-----|----------|
| Running it on the operator's own repos as an individual | Permitted |
| Extracting the scan → triage → queue pattern | Permitted — it is an idea |
| Shipping it, or running it, inside a **commercial closed-source product** | **A paid licensing question.** Do not assume. |

The report routes it to Atto and Collectibles, both of which have paid SKUs. That routing is fine for internal development hygiene and is **not** fine if the tool becomes part of what ships.

### Recommendation

Adopt the **pattern**. Before adopting the **tool** anywhere it might ship, read the LICENSE and decide whether the commercial tier applies.

### Status

Extract, **pattern only**, licence restricted.

## Snippets

> "Agent harness to make your slop code well-engineered and beautiful." — repository description [fetched 2026-11-03]

> It is free "for any individual — whether working independently or at a company — to use for their own work", and "for open source companies to use in any capacity, including commercial". For-profit, closed-source companies that want to commercialize it are pointed to the LICENSE file for pricing. [repository page, fetched 2026-11-03]

## Dead Ends

- **Reading the truncation as "just free".** The clause that follows is the one that costs money.
- **Bundling it into a commercial Atto or Collectibles build.** That is the case the custom licence prices.
