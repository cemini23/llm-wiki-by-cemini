---
title: Multi-Wiki Repository Revenue Evaluation — 20 URLs (2026-11-04)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [repository revenue evaluation, runtime v10.11, phase-0, helix-foundry, worldmonitor, doop, soup]
related:
  - entities/tools/helix-foundry.md
  - entities/tools/worldmonitor.md
  - entities/tools/doop.md
  - entities/tools/soup.md
  - entities/tools/worktrunk.md
  - entities/tools/scenario-labs-skills.md
  - entities/tools/unslop.md
  - sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md
  - sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md
maturity: draft
created: 2026-11-04
updated: 2026-11-04
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10.11) |
| Type | Generated evaluation report, agent-authored and cited |
| Received | 2026-11-04 |
| Inbox | `research to be indexed/Multi-Wiki Repository Revenue Evaluation.docx` |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit. **#1 Atto + Collectibles + Game-Time (co-equal)**; #2 CeminiDFS + CeminiParlays; #3 GuruWatcher + Basgiath |

Despite the new "Repository" filename, the internal title still says **v10.11** — the same label as the 2026-11-03 batch. The version string is not tracking batches reliably.

## Narrative

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License (verified) |
|---|------|------|--------------|-------------|--------------------|
| 1 | max-sixty/worktrunk | **Extract** | CCC | game-time, atto | MIT OR Apache-2.0 *(repeat)* |
| 2 | floci-io/floci | Context | Cybersec | lab | MIT |
| 3 | JiaFeiMiao-K-Cat/DiscImageStudio | Pass | Image-gen | none | GPL-3.0+ |
| 4 | github/spec-kit | Context | CCC | atto, game-time | MIT |
| 5 | The-PR-Agent/pr-agent | Context | CCC | game-time | Apache-2.0 / MIT |
| 6 | MichaelCade/90DaysOfDevOps | Pass | CCC | none | not found |
| 7 | Thysrael/Horizon | Context | OSINT | guruwatcher, pm-canary | not found |
| 8 | scenario-labs/skills | **Extract** | Game-dev | game-time | MIT *(repeat — vendor cloud)* |
| 9 | justrach/nanolight | Pass | CCC | none | not found |
| 10 | MakazhanAlpamys/Soup | **Extract** | Cybersec | lab | **Apache-2.0** *(report: not found)* |
| 11 | kgoedecke/doop | **Extract** | CCC | game-time, atto | **AGPL-3.0** *(report: MIT)* |
| 12 | deepcoldy/botmux | Pass | CCC | none | not found *(repeat)* |
| 13 | koala73/worldmonitor | **Extract** | OSINT | guruwatcher, pm-canary | AGPL-3.0-only |
| 14 | doobidoo/mcp-memory-service | Context | CCC | none | not found |
| 15 | ccch1mneyyy/dsh-Go | Context | CCC | none | AGPL-3.0 / MIT parts |
| 16 | helixdb/helix-foundry | **Extract** | OSINT | atto, family-tree, collectibles | **Apache-2.0** |
| 17 | NVIDIA/auto-ontology | Watch | OSINT | atto | not found |
| 18 | sorrycc/Mayoi PR #102 | Pass | CCC | none | not found |
| 19 | DeepSeek-V4-Pro…heretic-i1-GGUF | Watch | Cybersec | lab | not found |
| 20 | heydamir/unslop | Context | CCC | none | **CC-BY-4.0** *(report: not found; repeat)* |

Tally: **0 Integrate**, 6 Extract, 2 Watch, 7 Context, 5 Pass, 0 unavailable.

### What kind of batch this is

**Zero Integrates, and the report says why:** "all high-value finds in this batch require targeted pattern, skill, or schema extraction into existing shipped project briefs rather than raw drop-in replacement."

That is an honest self-assessment and it is correct for most of the list. But the batch also has a **quality problem**: eight of twenty licences are recorded as "NOT FOUND", and roughly seven entries admit the repo contents were never retrieved — *botmux*, *unslop*, *Horizon*, *auto-ontology*, *Mayoi*, *nanolight*, and *90DaysOfDevOps* all carry phrasing like "None verifiable without hallucinating unindexed capabilities." To its credit the report says so rather than inventing; the cost is that those seven rows carry almost no information.

**Four URLs are repeats** from earlier batches: worktrunk, scenario-labs/skills, botmux, unslop. Each re-tiers differently from its first appearance, which is itself a signal about stability.

### Phase-0, 2026-11-04 — four material corrections

GitHub egress is denied in the sandbox; checks used repository pages via web fetch.

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| **kgoedecke/doop** | "MIT — complies with Game-Time's zero-copyleft rule" | **AGPL-3.0.** The README states GNU AGPL v3: self-hosting and modification are fine, but **offering a modified version as a service requires publishing the changes**. Name and logo are trademarks. **42** MCP tools (report said 40). | **The licence claim is wrong and it breaks the routing.** Doop cannot go into a zero-copyleft game-time build or a commercial Atto kit. It is also **not fully local**: the built-in agent needs a connected model account or an Anthropic/Azure key, and connecting Claude Code or ChatGPT means driving it "on your own subscription". |
| **koala73/worldmonitor** | "AGPL-3.0 for non-commercial use; commercial license from Elie Habib required for commercial SaaS or rebranding" | **AGPL-3.0-only.** The README says the opposite of the report: "Commercial use **is** permitted under the AGPL when you comply with its copyleft and source-availability terms." A separate commercial or trademark agreement applies to **private proprietary use or official branding**, not to commercial use as such. | The restriction is **narrower than reported** and the practical conclusion is unchanged: never bundle it into a zero-copyleft or commercial build. Consume it as an external feed only. |
| **worldmonitor** | Presented as a 100-tool MCP feed for GuruWatcher | `tools/list` is public, but **`tools/call` requires an `X-WorldMonitor-Key` header or OAuth**, with keys from `worldmonitor.app/pro`. Feature-specific data sources may need credentials too. | **Not a free feed.** Any GuruWatcher integration is gated on a paid key. That changes it from "wire this up" to "price this first". |
| **helixdb/helix-foundry** | Routed to `Desktop/family/research/` and Atto vault for a "complete local-first" ontology workflow | Apache-2.0 confirmed, 2.0k stars, 360 commits. Loopback-only binding confirmed. **But local does not mean offline:** "Foundry will use Claude or OpenAI if your shell has the corresponding API key. Otherwise it falls back to a local Ollama, LM Studio or any OpenAI-compatible server." The README warns: "Never expose it through a reverse proxy, tunnel or port forward." | **A direct collision with Atto's ban 4.** On a machine with `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` exported, family records would go to a cloud model by default. Usable only with those keys absent and a local endpoint pinned. See @entities/tools/helix-foundry.md. |
| **MakazhanAlpamys/Soup** | "NOT FOUND" licence; "8B LLM fine-tuning on 4 GB laptop GPU" | **Apache-2.0**, 10.1k stars, `soup-cli` on PyPI. But: "A CUDA GPU is recommended. **Apple Silicon (MPS) is supported**, and CPU is described as 'experimental — very slow.'" Layer streaming is an **opt-in beta**. | The licence clears. The hardware story does **not** match an Apple Silicon laptop: the 4 GB claim is a CUDA story, and MPS support says nothing about whether layer streaming works there. |
| **heydamir/unslop** | "NOT FOUND" | **CC-BY-4.0**, verified on 2026-11-02. Repeat URL. | Report error; the existing page is correct. |

### The two items actually worth pursuing

**helix-foundry** is the strongest find, and it comes with the sharpest warning. A local ontology drafter with a mandatory human promotion gate and row/quote provenance is close to what Atto needs for citation lineage. It is also, by default, a thing that will send your data to a frontier model if a key happens to be set.

**worldmonitor** is the second, and it is a feed rather than a tool: FRED, Finnhub, and chokepoint data behind an MCP server. Useful for GuruWatcher and pm-canary only after the key cost is known.

### Everything else

- **Context (7):** floci (local cloud emulator on :4566, MIT), github/spec-kit (constitution.md workflow, MIT), pr-agent (PR diff compression), Horizon (news-source platform; only the companion site repo was found), mcp-memory-service, dsh-Go (Android DeepSeek harness, AGPL), unslop (already catalogued).
- **Pass (5):** DiscImageStudio (optical disc art), 90DaysOfDevOps (study guide), nanolight (macOS launcher), botmux (repeat, contents never retrieved), Mayoi PR #102 (a pull request, not a project).
- **Watch (2):** NVIDIA/auto-ontology — only the eval repo's PR page was indexed. DeepSeek-V4-Pro heretic GGUF — no model card benchmarks, no tool-call stability data.

## Snippets

> "Integrate: 0 — none (all high-value finds in this batch require targeted pattern, skill, or schema extraction into existing shipped project briefs rather than raw drop-in replacement of shipped modules)" — report, aggregate

> "GNU AGPL v3. You can self-host and modify it, but offering a modified version as a service means you have to publish your changes." — Doop README [fetched 2026-11-04]

> "Commercial use is permitted under the AGPL when you comply with its copyleft and source-availability terms." — WorldMonitor README [fetched 2026-11-04]

> "Foundry will use Claude or OpenAI if your shell has the corresponding API key. Otherwise it falls back to a local Ollama, LM Studio or any OpenAI-compatible server you point it at." — helix-foundry README [fetched 2026-11-04]

> "A CUDA GPU is recommended. Apple Silicon (MPS) is supported, and CPU is described as 'experimental — very slow.'" — Soup README [fetched 2026-11-04]

## Dead Ends

- **Treating Doop as MIT.** It is AGPL-3.0; the report's licence line is wrong.
- **Treating "local-first" in helix-foundry as "nothing leaves the machine".** It uses a cloud model by default when a key is present.
- **Reading the Soup 4 GB claim as an Apple Silicon claim.** It is a CUDA story.
- **Assuming worldmonitor's MCP tools are callable without a key.** `tools/list` is public; `tools/call` is not.
