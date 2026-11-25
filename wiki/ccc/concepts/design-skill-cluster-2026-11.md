---
title: "Design and motion skill cluster — what six 2026-11 agent skills actually encode"
type: concept
related:
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/context-engineering.md
updated: 2026-11-17
maturity: draft
---

## Raw Concept

Six URLs from the 2026-11-17 batch grade Context under the Workstation Harness Freeze.
All six are agent skills for interface design. The question this page answers: **when
six skills claim to make an agent's UI work better, which rules are load-bearing?**

Source: @osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md.

## Narrative

### The six

| Repo | Stars | Licence | What it encodes |
|------|-------|---------|-----------------|
| `nextlevelbuilder/ui-ux-pro-max-skill` | 151k | MIT | A BM25 corpus: 80 visual styles, 34 landing-page blueprints, 192 product types, 1,934 font pairings, responsive checklists |
| `emilkowalski/skills` | 58k | MIT | Vercel/Linear craft: component stress testing, mobile touch fixes, animation-latency removal |
| `Nutlope/hallmark` | 57k | MIT | Three quality gates and `sloplint.mjs`, a DOM/CSS linter run at 8 viewport widths |
| `jakubkrehel/make-interfaces-feel-better` | 4.1k | MIT | Optical alignment, concentric radius math, hit-target padding |
| `benjitaylor/skills` | 3.5k | **none** | React/CSS product-demo and bento-grid composition rules |
| `brijr/gui` | 191 | Apache-2.0 | Point-and-click: a visual selection maps to file path, line, and computed CSS |

### The useful distinction

These split into two kinds, and only one kind survives without installation.

**Encoded knowledge** — `ui-ux-pro-max`, `hallmark`, `make-interfaces-feel-better`.
Their value is a table: which radii nest correctly, which contrast ratio is the floor,
which font pairs work. A table can be copied into a checklist and used without the
skill existing. That is why they are worth reading during a freeze.

**Behavioural tooling** — `brijr/gui`, `make-interfaces-feel-better`'s lint pass,
`hallmark`'s `sloplint.mjs`. These need to run. They are frozen, and unreadable as
prose — the rules live in code.

### Three rules worth keeping

From the cluster, three rules are mechanical enough to apply by hand:

1. **Concentric radius** — an inner radius equals the outer radius minus the padding.
   A card with 12 px radius and 8 px padding takes a 4 px child radius. Getting this
   wrong is the most common "why does this look off" in a card list.
2. **Hit targets** — a 44 px minimum touch area regardless of visual size. The visual
   box may be 24 px; the interactive box may not.
3. **Optical, not geometric, centring** — a glyph or icon is centred on its ink, not on
   its bounding box. Text with a descender sits one pixel high if centred by box.

Each rule is one line. None needs a package.

### The anti-slop gate

`hallmark` frames the real problem: generated interfaces converge on the same look.
Its answer is a lint pass with concrete heuristics — too many gradients, uniform
spacing that ignores hierarchy, decorative borders on everything.

For our stack the applicable part is the **8-width check**. A layout verified at 375,
768, and 1440 px is verified at three widths; the failures cluster at 320, 414, 834,
1024, and ultrawide. Resize before calling a UI done.

### Why none of this is queued

Gate 3 freezes installation. `benjitaylor/skills` fails Gate 1 as well — no licence
means no copying, so even its prose cannot be lifted.

The rules above are restatements in our own words of general design practice. They are
not copied text.

## Snippets

> An agent skill that helps make your interface feel better.
> [`jakubkrehel/make-interfaces-feel-better`, repository description, 2026-11-17]

## Dead Ends

- **Installing a design skill during the harness freeze.** Six skills, six blocks.
- **Copying from `benjitaylor/skills`.** No SPDX licence, so all rights reserved.
