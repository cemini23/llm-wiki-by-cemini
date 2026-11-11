---
title: Multi-Wiki Repository Revenue Evaluation — 20 URLs (2026-11-11)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [runtime v10.11, phase-0, shadcn improve, autoharness, claude-video, neo4jev]
related:
  - "@ccc-wiki/entities/tools/shadcn-improve.md"
  - "@ccc-wiki/entities/tools/autoharness.md"
  - "@image-gen-wiki/entities/tools/claude-video.md"
  - entities/tools/neo4jev.md
  - entities/tools/jevals.md
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
  - sources/arxiv-v10-11-late-skip-no-lane-2026-11-11.md
maturity: draft
created: 2026-11-11
updated: 2026-11-11
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research Runtime (v10.11) |
| Received | 2026-11-11 |
| Inbox | `research to be indexed/Multi-Wiki Repository Revenue Evaluation.docx` |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit |

**Sixth batch labelled v10.11.** The theme is explicit: "Agent Skills and Self-Learning Harnesses, Agent-Ready Web Design Systems, Multimodal Video and 3D Code Synthesis, Bounded Graph Decision Models (Jev), and Whitehat Lab Infrastructure."

## Narrative

### Tier table

| # | Tool | Tier | Project fit | License (verified) |
|---|------|------|-------------|--------------------|
| 1 | meta/astryx | Watch | CCC | MIT |
| 2 | GoogleChrome/modern-web-guidance-src | **Extract** | game-time, atto | Apache-2.0 |
| 3 | **shadcn/improve** | **Integrate** | atto, collectibles, game-time | **MIT** |
| 4 | we-promise/sure | Pass | none | AGPL-3.0-only |
| 5 | homeassistant-ai/ha-mcp | Context | CCC | MIT |
| 6 | andyhuo520/vibe-knowledge | **Extract** | atto, game-time, basgiath | not found |
| 7 | Pluviobyte/saas-growth-agents | Context | SEO | not found |
| 8 | dabingfy-dot/solo-to-team-skills | **Extract** | atto, collectibles, guruwatcher | not found |
| 9 | Nyxera0x/cutaway | **Extract** | game-time, basgiath | MIT |
| 10 | jazzenchen/agent-hud-open | Context | CCC | Apache-2.0 |
| 11 | phuryn/product-engineering | Context | CCC | MIT |
| 12 | tobi/wrapvm | Watch | cybersec | not found |
| 13 | jexp/neo4jev | **Extract** | atto, family-tree, parlays | **MIT** |
| 14 | janestreet/agent_skills | **Extract** | atto | MIT |
| 15 | ryzqi/learn-agent | Context | CCC | not found |
| 16 | **bradautomates/claude-video** | **Integrate** | collectibles, game-time | **MIT** |
| 17 | **tigerless-labs/autoharness** | **Integrate** | atto, collectibles, game-time | **MIT** |
| 18 | boogalooSec/EquationGroup | Pass | cybersec | not found |
| 19 | rapid7/metasploit-framework | Context | cybersec | BSD-style |
| 20 | karpathy/nn-zero-to-hero | Pass | none | not found |

Tally: **3 Integrate**, 6 Extract, 2 Watch, 6 Context, 3 Pass.

**Three Integrates is the most any batch has produced**, and all three are agent-harness tooling rather than project dependencies.

### Phase-0, 2026-11-11

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| **shadcn/improve** | Integrate; "six phases" | **MIT.** The README enumerates **five**: Recon → parallel 9-category Audit → Vet → Prioritize → Plan. Execute exists as a separate feature, not a sixth phase. **The safety property is the finding:** "Executors edit only in disposable worktrees, and **merging is always yours**." The skill itself writes only to `plans/`. | Integrate holds and is stronger than reported. A read-only advisor with a human merge gate is the shape this workspace already prefers. |
| **autoharness** | Integrate; distils skills into `.claude/autoharness/` | **MIT.** Python 3.11+, no third-party dependencies. **Where it writes is different from the report:** learned skills go to **`.claude/skills/`** (project) or **`~/.claude/skills/`** (global); archived skills to `.claude/skills/.archive/<name>/`; **state** lives in `.claude/autoharness/`. **It only manages skills it created**, and leaves hand-written skills alone. | Integrate holds. The "never touches your skills" property is what makes it safe to run here — this workspace has hand-written skills. |
| **claude-video** | Integrate for video ingest | **MIT.** **The data path depends entirely on which engine runs:** the **Gemini engine is the default when a key is present** — YouTube links go straight to Google, and other URLs and local files are uploaded to Google's Files API. **The local engine runs when no key is set**, using ffmpeg/yt-dlp on the machine. WhisperX is key-free and local. | **A ban-4 hazard the report did not mention.** On a machine with a Gemini key exported, video leaves the machine by default. Use the local engine, and prove it with the same no-network assertion as jevals. |
| **neo4jev** | Extract; bounded Jev decisions over graph hops | **MIT.** **Requires a remote TypeSafe `system_one` service and `TYPESAFE_API_KEY`** — without the key every call fails and the notebooks fall back to "explicitly labelled stand-in answers". Also **requires Neo4j** (defaults to the public Companies demo graph). | **The opposite of `jevals` on locality.** Same Jev family, but this one is hosted-only. Relevant to Atto only as a design reference, not as anything runnable under ban 4. |
| **meta/astryx** | Watch: React 19 Beta, canary chart packages, Next 15 + Tailwind traps | Eight-year internal Meta design system, 13,000+ apps, MIT. | Watch is right, for the stated reasons. |

### The three Atto-relevant extracts form another chain

Read together they are a **teaching and verification stack**, not a retrieval one:

- **`janestreet/agent_skills`** — a Socratic tutor: diagnostic, a 0–5 mastery map, **one question per turn**, spaced review, and a mastery assessment. The report routes this to an Italian paleography tutor inside the Atto playbook subscription.
- **`dabingfy-dot/solo-to-team-skills`** — four Markdown skills enforcing a 5-state task register ("pending → accepted → checkpoint → delivered") plus `evidence-before-done`. That is the same contract as provenance-as-lookup, expressed as a workflow.
- **`neo4jev`** — bounded decision over graph edges, as a design reference.

The first two are safe and cheap. The third is hosted-only.

### The pattern continues

Fifth batch running where the eval's confidence about **what a tool does when it runs** is lower than its confidence about **what the tool is for**. The three Integrates were all correctly identified as valuable and all three had a material detail wrong or missing — a phase count, a write location, and a data path.

That is not a reason to stop using the pipeline. It is the reason Phase-0 exists, and it now has a consistent shape: **the licence is usually right, the mechanism is usually approximate.**

## Snippets

> "Executors edit only in disposable worktrees, and merging is always yours." — shadcn/improve README [fetched 2026-11-11]

> Learned skills go into `.claude/skills/` in the project, or `~/.claude/skills/` for global lessons. Archived skills move to `.claude/skills/.archive/<name>/`. [autoharness, fetched 2026-11-11]

> **Gemini engine (default when a key is present):** YouTube links are sent straight to Google. Other URLs and local files are uploaded to Google's Files API. [claude-video, fetched 2026-11-11]

> Without a `TYPESAFE_API_KEY`, each call is attempted and fails, and the app continues on "explicitly labelled stand-in answers". [neo4jev, fetched 2026-11-11]

## Dead Ends

- **Running claude-video with a Gemini key exported.** The default engine is a cloud upload.
- **Treating neo4jev as a local Jev option.** It is hosted-only; `jevals` via Laya is the local path.
- **Expecting autoharness to write where the report says.** Skills go to `.claude/skills/`; `.claude/autoharness/` holds state.
