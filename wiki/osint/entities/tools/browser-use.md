---
title: "browser-use — local Chromium automation with a local model (MIT)"
type: entity
tags: [tool, browser, automation, collectibles, local, mit]
keywords: [browser-use, chromium, cdp, ollama, checkpoint, sold comps, pop reports]
related:
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-evaluation-2026-11-10.md, URL 6, **Extract** tier. Routed to Collectibles and Atto.

The question this page answers: **can browser automation run without a metered cloud?**

## Narrative

### Phase-0, 2026-11-10 — the licence clears and the local path exists

The report records the licence as **"NOT FOUND"**. It is **MIT**, stated in the README and the repository metadata.

More useful, because the report framed this as a cloud product:

| Path | How | Key |
|------|-----|-----|
| **Local** | `Browser('chromium')` with a model — the README shows "a local model, e.g. **Ollama** through `ChatOpenAI(...)`" | **none** |
| Cloud (default) | `Browser()` is "a Browser Use Cloud browser (default)" | `BROWSER_USE_API_KEY`, one key pays for model and browser |

**The free local path exists; the documented quickstart steers you to the metered one.** That is a documentation default, not a capability limit — and it is the same pattern as the previous batch's `scenario-labs/skills`, where the licence was fine and the vendor was the real constraint.

### What v1.0.0 adds

- A **persistent Python/CDP REPL** — write a script against a live page and run it repeatedly, instead of re-driving the browser from zero each time.
- **`checkpoint(..., partial=True)`** — save progress mid-flow, so a crawl that dies at page 40 resumes rather than restarting.

For comp and population-report harvesting those are the two things that matter. The failure mode of a multi-page scrape is losing the batch when one page hangs; partial checkpoints fix exactly that.

### The boundary

Collectibles' rule is that card images are the product. browser-use drives a **local Chromium** against **public listing pages** — that is ordinary reading, and it is the same category as the plain fetchers already accepted.

It does **not** solve the evasion question. If a target puts an access control in the way, browser automation hits it the same as any other client, and the per-site decision from Scrapling and botasaurus applies unchanged.

### Status

Extract, **local Chromium only**. Never the cloud default.

## Snippets

> The README shows `Browser('chromium')` paired with an LLM such as `ChatOpenAI`, and mentions using "a local model, e.g. Ollama through `ChatOpenAI(...)`." No API key is required. [fetched 2026-11-10]

> The README says the library is "MIT licensed". [fetched 2026-11-10]

## Dead Ends

- **Running the cloud default.** It meters both model and browser.
- **Expecting this to bypass a bot check.** It is a browser, not an evasion layer.
