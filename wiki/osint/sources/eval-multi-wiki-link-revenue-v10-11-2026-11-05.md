---
title: Multi-Wiki Link Evaluation — 20 URLs (2026-11-05)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [runtime v10.11, phase-0, deja-vu, ontographia, pagesift, helix-foundry]
related:
  - entities/tools/deja-vu.md
  - entities/tools/ontographia.md
  - entities/tools/pagesift.md
  - entities/tools/helix-foundry.md
  - sources/eval-multi-wiki-repository-revenue-2026-11-04.md
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
  - sources/arxiv-v10-11-late-skip-no-lane-2026-11-05.md
maturity: draft
created: 2026-11-05
updated: 2026-11-05
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Runtime Report (v10.11) |
| Received | 2026-11-05 |
| Inbox | `research to be indexed/Multi-Wiki Link Revenue Evaluation.docx` |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit, same stack |

**Fourth batch in a row labelled v10.11.** The version string has not moved since 2026-11-03.

## Narrative

### Tier table

| # | Tool | Tier | Project fit | License (verified) |
|---|------|------|-------------|--------------------|
| 1 | Usagi-org/ai-goofish-monitor | Extract | collectibles | MIT |
| 2 | lz4/lz4 | Context | game-time | BSD-2 (lib) / GPL-2.0+ (CLI) |
| 3 | ConardLi/garden-skills | Extract | game-time, atto | MIT |
| 4 | cagnulein/qdomyos-zwift | Pass | none | GPL-3.0 |
| 5 | kunchenguid/firstmate | Extract | CCC, game-time | MIT |
| 6 | three-gpu-pathtracer | Context | game-time | MIT |
| 7 | **vshulcz/deja-vu** | **Integrate** | all Priority #1 | **MIT** |
| 8 | wj-sidiss/otopilot | Context | game-time | MIT |
| 9 | storytold/craft-anything | Context | CCC | not found |
| 10 | edgesentry/ontographia | Extract | atto, family-tree | **Apache-2.0** |
| 11 | SwotAtmk/infinite-creation | Extract | game-time | not found |
| 12 | KKKKhazix/agent-autoloop | Watch | CCC | MIT |
| 13 | OpenSelena/omniget | Pass | none | GPL-3.0 |
| 14 | moonshotai/Kimi-K3.1-Pro | Extract | collectibles, game-time, guruwatcher | custom / NVIDIA OMA |
| 15 | JuneYaooo/rea-video | Extract | game-time, basgiath | Apache-2.0 |
| 16 | helixdb/helix-foundry | Watch | atto | Apache-2.0 |
| 17 | YOLOW92/pagesift | Extract | collectibles, atto | **AGPL-3.0** *(report: not found)* |
| 18 | apify/crawlee | Extract | collectibles | **Apache-2.0** *(report: not found)* |
| 19 | omkarcloud/botasaurus | Context | OSINT | MIT / Apache-2.0 |
| 20 | spider-rs/spider | Extract | collectibles, DFS | MIT |

Tally: 1 Integrate, 10 Extract, 2 Watch, 5 Context, 2 Pass.

### Phase-0, 2026-11-05

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| **pagesift** | "NOT FOUND — verify license in repository root" | **AGPL-3.0**, with a commercial licence available for proprietary use. 229 stars, 614 commits. | **Cannot enter a commercial Atto or Collectibles build.** The report routed it to both. Extract the idea — local Rust PDF/Office-to-Markdown — not the binary. |
| **crawlee** | "NOT FOUND in collected material (verify Apache-2.0)" | **Apache-2.0**, stated on the project page. | Clears. |
| **deja-vu** | Integrate; "99.8% of commands and 23% of decisions lost during context compaction" | **MIT confirmed**, ~1.4k stars. **43 harnesses**, not 44. Local index in `~/.cache/deja`, **zero LLM calls by default**. **But: "Credentials are redacted at index time, but the original transcripts keep them."** `deja secrets` lists affected sessions; `--scrub` rewrites with a backup. | The Integrate holds. The credential caveat did not make the report and it matters: **redaction is at the index, not the source.** |
| **ontographia** | Extract for Atto; two-stage query compilation | **Apache-2.0 confirmed — but 15 stars, 0 forks, 105 commits.** Deterministic Rust core: `Ontology → COM → validate(Intent) → AST → Cypher`. LLM is optional (`ontographia[llm]`, labelled experimental). **The README does not state whether the LLM layer works with a local model.** | The architecture is exactly right for Atto — the model never writes Cypher. The maturity is very low, and the one question that decides Atto usability is unanswered. |
| **helix-foundry** | Watch this time: "no 0.1.0 release tag, ontology-agent Docker image not published" | Evaluated 2026-11-04: Apache-2.0, 2.0k stars, 360 commits, runs. **It re-tiered Extract → Watch in one day on a packaging detail.** | The blocker is real but narrow. The substantive finding from yesterday stands unchanged and is the one that matters: **it calls Claude or OpenAI by default when a key is exported.** |

### The batch in one paragraph

One Integrate that holds — **deja-vu**, and its appeal is obvious in a workspace where memory capture has just failed: it indexes what the agents already wrote to disk, locally, with no model in the loop. One Atto-shaped idea that is architecturally correct and immaturity-blocked — **ontographia**. And a collecting-heavy tail of scrapers where the licences are the whole story: **pagesift is AGPL, not "not found"**, and the rest of the scraping stack (crawlee, spider, botasaurus, ai-goofish-monitor) is permissive but runs straight into the same detection-evasion question that Scrapling raised on 2026-11-02.

## Snippets

> "MIT © Vladislav Shulcz" — deja-vu [fetched 2026-11-05]

> "Credentials are redacted at index time, but the original transcripts keep them." — deja-vu README [fetched 2026-11-05]

> "`~/.config/deja/exclude` skips a project per line, or a whole store with `harness:opencode`" — deja-vu README [fetched 2026-11-05]

> "schema-constrained Intent, never raw Cypher" — ontographia [fetched 2026-11-05]

> pagesift is **AGPL-3.0**, "with an option to buy a commercial licence for proprietary use". [fetched 2026-11-05]

## Dead Ends

- **Treating pagesift's licence as unverified.** It is AGPL-3.0, and that disqualifies it from commercial builds.
- **Assuming deja-vu's credential redaction protects the source files.** It does not.
- **Reading ontographia's maturity as adequate because the architecture is right.** 15 stars and 105 commits.
