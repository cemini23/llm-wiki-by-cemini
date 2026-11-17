---
title: "Agent presentation generation — native PPTX versus single-file HTML"
type: concept
related:
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-17
---

## Raw Concept

Two of the largest repositories in the 2026-11-17 batch make slide decks from a
document. The question this page answers: **when an agent builds a deck, should the
output be a real `.pptx` file or a single HTML page?**

Source: @osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md.

## Narrative

### Two answers, both MIT

**`hugohe3/ppt-master`** — 78k stars, Python, a `.claude-plugin`. Emits **native
PowerPoint**: DrawingML shapes, `p:sldMaster`/`p:sldLayout` templates, editable charts
and tables, OMML math, image queries against Wikimedia and Openverse with attribution.

**`zarazhangrui/frontend-slides`** — 33k stars. Emits a **single self-contained HTML
file**: inline CSS and JS, zero runtime dependencies, 34 template packs. Also reads an
existing `.pptx` via `python-pptx` to extract text, images, and speaker notes.

### The trade is ownership

A native `.pptx` is **editable by the recipient**. That is the whole point. A client
who receives a deck opens it in PowerPoint and changes a slide without asking. DrawingML
shapes stay shapes; charts stay charts with a data sheet behind them. The cost is that
the generator must model PowerPoint's object structure, which is why a real implementation
is large.

A single HTML file is **rendered by the recipient**, and looks exactly as built. It
cannot be edited in PowerPoint. It survives email and file shares because it has no
dependencies. The cost is that it is a picture of a deck, not a deck.

For anything that leaves the building and may be revised by someone else, native wins.
For anything that must look identical everywhere and will not be edited, HTML wins.

### Where this lands in our stack

No active project ships a PowerPoint SKU. Atto delivers research dossiers, Collectibles
delivers grading manifests, CeminiDFS delivers calibration reports. None is a deck.

So both are Context, and the report is right to refuse them. The extract, if a deck
need appears, is the **template structure** — `sldMaster` and `sldLayout` mapping in the
native case, the 34-pack organisation in the HTML case — not the generator.

### The one transferable detail

`ppt-master` attaches a **licence attribution to each Wikimedia/Openverse image query**.
Generated decks are the common place where an agent pulls an image and loses its
provenance. Recording the licence at fetch time, in the slide's own metadata, is a small
detail that prevents an unpleasant discovery later.

## Snippets

> AI turns documents or topics into real, native PowerPoint.
> [`hugohe3/ppt-master`, repository description, 2026-11-17]

> Creates beautiful slides on the web using a coding agent.
> [`zarazhangrui/frontend-slides`, repository description, 2026-11-17]

## Dead Ends

- **Generating HTML when the recipient will edit.** The deck is not editable and the
  recipient will ask for the source.
- **Letting the agent fetch images without recording the licence.** Provenance is lost
  by the time anyone asks.
