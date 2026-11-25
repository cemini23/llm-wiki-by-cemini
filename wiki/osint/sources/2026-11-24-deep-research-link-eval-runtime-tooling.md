---
title: "Deep Research link evaluation — AI SRE and security agents, local inference, video repurposing (2026-11-24)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - sources/2026-11-22-deep-research-link-eval-abliterated-harness.md
  - "@game-dev-wiki/entities/tools/autoclip.md"
  - "@ccc-wiki/concepts/agent-runtime-tooling-2026-11.md"
  - "@image-gen-wiki/concepts/local-inference-runtimes.md"
  - "@ccc-wiki/entities/whatsflare.md"
  - "@cybersecurity-wiki/concepts/secret-masking-regression-tests.md"
  - "@cybersecurity-wiki/entities/tools/claude-bughunter.md"
updated: 2026-11-24
read_status: read
maturity: draft
---
## Raw Concept

- **Title:** Multi-Wiki Link Revenue Evaluation (batch E)
- **Author:** Deep Research evaluation run, v10.13 anti-bloat and consolidation gates
- **Type:** vendor-link evaluation report (DOCX)
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Link Revenue Evaluation.docx`
- **Retrieved:** 2026-11-24
- **Pages:** 20 URL records
- **Read status:** read

Batch theme: AI coding, SRE, and security agents, local inference and UI frameworks,
video repurposing, and new model releases as of 2026-11-24.

## Narrative

One URL earned Extract, none earned Integrate. Seven Pass, nine Context, two Watch,
and one UNAVAILABLE.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Extract | 1 | `autoclip` |
| Context | 9 | `Claude-BugHunter`, `openvino`, `opensre`, `CoreCoder`, `nakama`, `gemini-api-cli`, `book-to-skill`, `watch-mcp`, `safe-anything` |
| Watch | 2 | `nanoui`, GLM-5.4 |
| Pass | 7 | `minimind`, `app-store-compliance`, `AFFiNE`, `Ghost-Downloader-3`, `sub2api`, `vibestack`, `Deep-Live-Cam` |
| UNAVAILABLE | 1 | `whatsflare` |

### The UNAVAILABLE verdict is wrong, again

The report grades `dannybyarun/whatsflare` UNAVAILABLE with the note "This website is
inaccessible", and skips analysis.

Direct checks on 2026-11-24 return **HTTP 200**. The GitHub API reports a live
repository — MIT, 5 stars, pushed 2026-11-21, description "WhatsFlare — WhatsApp
gateway for Cloudflare Workers: baileys in a Durable Object, a REST + WebSocket API".
[CONFIRMED]

This is the **second consecutive batch** where a live URL was graded UNAVAILABLE and
skipped. The 2026-11-17 batch had four such cases. That makes it a pattern in the
evaluation pipeline, not an accident, and it is the reason Gate 0 exists in
@concepts/agent-link-evaluation-gates-v1013.md: check the report's own verdict before
applying any gate.

### Recorded but blocked

- **GLM-5.4** — a 750B-scale loop transformer with 1M context, multimodal, and
  128K output. It is **proprietary and subscription-only** as of 2026-11-23; open
  weights and a public API are planned with no date. Watch only — there is nothing to
  invoke programmatically.
- **`nanoui`** — a Zig native UI shell (~0.7 MB reported) over system webviews, as an
  alternative to Electron for game-time's future Steam build. v0.14.8, no Steamworks
  bindings, no API stability. Watch only.

### Licence position

`CoreCoder`, `nakama`, `gemini-api-cli`, `book-to-skill`, and `watch-mcp` are graded
Context with **no licence found**. Under Gate 1 that is all rights reserved, so nothing
may be copied from them. The report treats a missing licence as a note rather than a
block; it does not matter here because none earned a tier, but the same omission graded
`wrapvm` as "friction only" in an earlier batch.

Permissive: `autoclip` MIT, `openvino` Apache-2.0, `opensre` Apache-2.0,
`Claude-BugHunter` MIT plus CC-BY-4.0 prose, `safe-anything` MIT.

## Snippets

> Governed by mandatory v10.13 Anti-Bloat & Consolidation Gates (uncapped true-merit
> discovery overriding the legacy v10.12 Max 2 cap).
> [Source: Multi-Wiki Link Revenue Evaluation.docx, research plan]

> Direct navigation to https://github.com/dannybyarun/whatsflare returned an explicit
> inaccessible response. Per evaluation protocol, deep analysis is skipped and the URL
> is graded UNAVAILABLE.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 19]

## Dead Ends

- **Accepting an UNAVAILABLE verdict.** Two batches in a row produced false ones.
- **Treating a missing licence as a footnote.** Five items here have none.
