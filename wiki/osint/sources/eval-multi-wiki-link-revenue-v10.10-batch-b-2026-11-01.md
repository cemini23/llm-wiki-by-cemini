---
title: Multi-Wiki Link Revenue Evaluation v10.10 — batch B, 20 URLs (2026-11-01)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [multi-wiki link evaluation, runtime v10.10, system-one model, MCP ATO, pageindex, ontology, design log]
related:
  - entities/tools/liquidai-d1-2b.md
  - entities/tools/jeveryword.md
  - entities/tools/agentdiscoverability-track.md
  - entities/tools/design-log-methodology.md
  - entities/tools/open-ontologies.md
  - entities/tools/pageindex.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research Runtime (v10.10) |
| Type | Generated evaluation report, agent-authored and cited |
| Author | Cemini eval pipeline |
| Received | 2026-11-01 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki URL Revenue Evaluation.docx` |
| Sibling | `Multi-Wiki Link Revenue Evaluation.docx` — same runtime version, different batch |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit. Priority #1 Atto and Collectibles (co-equal), #2 GuruWatcher and Basgiath, #3 CeminiDFS, #4 CeminiParlays |

Batch theme: System-One decision models, verifiable ontology and tree-search retrieval, MCP agent discoverability, Claude Code and Cursor harness methodology, ComfyUI video character swap, and local abliterated security tooling.

## Narrative

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License |
|---|------|------|--------------|-------------|---------|
| 1 | stevecad/steve-blender-connector | Context | 3D-printing | none | MIT |
| 2 | deepseek-ai/dsh-superagent-prototype | Context | CCC | none | MIT |
| 3 | brenoepics/video-to-skill | Context | CCC | atto, collectibles (partial) | MIT |
| 4 | jkrup/jeveryword | **Extract** | CCC, OSINT | atto, collectibles, guruwatcher | MIT |
| 5 | OBLITERATUS/DeepSeek-V4.1-Flash-1017-obliterated | Watch | Cybersec | local-abliterated-lab | MIT |
| 6 | LiquidAI/d1-2B | **Integrate** | Image-gen, OSINT | collectibles, atto, ceminiparlays | LFM Open License v1.0 |
| 7 | EpicGames/unreal-engine-skills | Context | Game-dev | none | MIT |
| 8 | agentdiscoverability.com/track | **Extract** | SEO, CCC | atto / atto-mcp | proprietary SaaS |
| 9 | aitmpl.com brainstorming skill | Context | CCC | none | not stated |
| 10 | dollarsforless.com | Pass | OSINT | none | n/a |
| 11 | YGMontop/AutoGameSkill | UNAVAILABLE | Game-dev | none | not found |
| 12 | Hack-with-Github/Awesome-Hacking | Context | Cybersec | none | CC0-1.0 |
| 13 | VectifyAI/PageIndex | **Extract** | OSINT, CCC | atto, family-tree, guruwatcher, collectibles | MIT SDK / proprietary API |
| 14 | nullclaw/nullclaw | Watch | CCC | none | not found |
| 15 | google/elephant-goldfish-model | Watch | CCC | none | not found |
| 16 | yoavaa/design-log-methodology | **Extract** | CCC, OSINT | ceminidfs, atto, collectibles | MIT |
| 17 | lawyered.lawyer/lawyeredos | Pass | OSINT | none | proprietary |
| 18 | fabio-rovai/open-ontologies | **Extract** | CCC, OSINT | atto, family-tree | MIT (verified Phase-0) |
| 19 | D3voz/openjutsu | Watch | Image-gen, Game-dev | basgiath (TikTok clips) | MIT |
| 20 | togg53192-cmd/jailbreaks | Context | Cybersec | local-abliterated-lab | not found |

Tally: 1 Integrate, 5 Extract, 4 Watch, 7 Context, 2 Pass, 1 unavailable.

### The one integrate

**URL 6, LiquidAI/d1-2B → Collectibles, Atto, CeminiParlays.** A 1.92B-parameter decision model built on LFM3-VL-2B. It answers in a single forward pass instead of generating tokens. Question types: `noul`, `choice`, `score` across 2–10 ordered levels, text/number/date span extraction, and `box`/`boxes` visual localisation. It is explicitly **not** a chat model. The report routes it to:

- **Collectibles** — pre-grade condition scoring, corner and centering box localisation, sold-comp title parsing.
- **Atto** — local record triage.
- **CeminiParlays** — a zero-cost local "jev-gate" for slip screening.

Phase-0 confirmed the licensing position (see below). This is the first batch since v10.9 to return an Integrate.

### The five extracts

**URL 4, jeveryword → Atto, Collectibles, GuruWatcher.** The report converts span extraction and word-level PII detection into numbered-token multiple-choice. The invariant is `text.slice(start, end) === value` for every returned field, with a probability attached. It routes to GuruWatcher to stop generative quote drift on newsletter claims.

**URL 8, agentdiscoverability.com/track → atto-mcp.** The report introduces an Agent Tool Optimization framework — Found → Picked → Positioned — measured over trailing 30-day intent runs, plus MCP schema rules (tool-name alignment, long-description matching customer queries, structured outputs). It applies this to Atto's Claude Connector and ChatGPT Plugin listings.

**URL 13, VectifyAI/PageIndex → Atto, family-tree, GuruWatcher, Collectibles.** A layout-derived hierarchical tree index with multi-hop traversal that follows cross-references. The report applies it to multi-hundred-page Italian civil registers. **This re-opens a prior NO-GO** — see below.

**URL 16, design-log-methodology → CeminiDFS, Atto, Collectibles, repo-wide.** A frozen-design-log workflow. Design is written and approved first, then frozen. An immutable "Implementation Results" section records deviations. A "Minimize new surface (null hypothesis first)" gate must be justified before any new code.

**URL 18, open-ontologies → Atto, family-tree.** A Rust binary that reports the blast radius of a planned ontology change, and emits a certificate a separate Lean checker can verify.

### The four watch items

| Tool | Blocker |
|------|---------|
| OBLITERATUS/DeepSeek-V4.1-Flash | 755B parameters, 1.5 TB BF16. Needs multi-node GPU or future quantization. |
| nullclaw | No verified stars, commit, or license. No RAM bottleneck justifies a Zig rewrite of working daemons. |
| elephant-goldfish-model | Sparse public documentation on `egm.dev`. Needs manual source inspection. |
| openjutsu | Needs 16–24 GB CUDA VRAM and about 35 GB checkpoints. Routed only to Basgiath TikTok clips. |

### Phase-0 corrections

Phase-0 ran on 2026-11-01. GitHub egress is denied in the session sandbox. Checks used source files fetched from the raw content hosts and the Hugging Face model card. This confirms license text and README claims. It does not confirm commit depth, issue counts, or full tree structure.

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| LiquidAI/d1-2B | "LFM Open License v1.0 — verify redistribution terms for packaged Atto kits versus internal Collectibles use" | The licence grants commercial use below a **$10 000 000** annual-revenue threshold. Above it, use "is not licensed". Redistribution requires passing on the licence, marking modified files, and including NOTICE attributions. | **Cleared for Atto kits today.** Below the threshold, bundling in a paid product is permitted. Add the NOTICE file and the licence copy to the kit. |
| LiquidAI/d1-2B | "prefer Transformers FP16 or d1-2B-MLX-8bit over GGUF when bounding boxes or span extractions are required" | The model card documents **only** Transformers `trust_remote_code=True` inference. Benchmarks: H100 5.7 ms, MI325X 3.8 ms, **Apple M5 Pro via `mps` 18.6 ms**. The card does not document MLX or GGUF. | Run **Transformers on `mps`** on the laptop. Treat the MLX/GGUF paths as community builds that need their own verification. `boxes` returns fractional coordinates, up to 16 instances. |
| fabio-rovai/open-ontologies | "License: NOT FOUND in public snippets (verify Cargo.toml and LICENSE)" | README states **MIT**. Rust binary. Reasoning via OWL/RDFS, SHACL, SWRL/RIF. MCP server with 39 tools. | License doubt cleared. Certificate verification needs only the two TSV files and a Lean build — no network, no LLM. |
| yoavaa/design-log-methodology | "MIT" | The README does not state a licence. The Claude Code instructions say to copy the rule file into `claude.md`. | Use the **methodology**, which is portable text. Confirm the licence in the repository before copying files. |
| jkrup/jeveryword | "must be run strictly on local model paths … rather than external cloud endpoints" | MIT, zero package dependencies, Node 20+. **But it requires a model.** The bundled `createJevClient` needs `TYPESAFE_API_KEY`. The hosted endpoint uses USDC payments with 25 free calls per day per IP. No local model path is documented. | **Blocks Atto vault use.** The invariant `text.slice(start, end) === value` is safe regardless of who runs the model, but the *text* leaves the machine. Use it only on non-PII text until a local Jev-equivalent exists. |
| jkrup/jeveryword | Treated as a live candidate | **4 stars.** The report itself logged "listed as 0–1 in earlier snapshots". | Very low maturity. Extract the numbered-token pattern. Do not depend on the package. |
| VectifyAI/PageIndex | Extract, routed to multi-hundred-page civil registers | The prior Phase-0 NO-GO (`entities/tools/pageindex.md`, 2026-05-05) rejected PageIndex **for the wiki layer** and named the exact condition that would revive it: *"PageIndex becomes a candidate ONLY IF Cemini begins indexing long-form professional documents … as a separate retrieval tier alongside the wiki."* Multi-hundred-page Italian civil registers are that corpus. | **Not a contradiction — the documented re-entry trigger fired.** Scope any new Phase-0 to long-form archival PDFs. The wiki-layer NO-GO stands. |
| open-ontologies | "certificate … bound to a SHA-256 digest" | The digest binds to the **input bytes**, not to the state of the world. In the default in-memory storage mode, `load` followed by `reason` certifies nothing and prints only a warning. Persistent mode is required for reuse across time. | Set persistent mode in any Atto proof pipeline. Record the mode in the certificate header. |

### Everything else

Seven Context and two Pass rows carry no action:

- **steve-blender-connector** — a useful reference for signed local MCP bridge actions with SHA-256 input hashes and duplicate-run prevention. 3D-printing only.
- **dsh-superagent-prototype** — a formal Source → Trigger → Thread → Eval → Ticket domain separation, where a resumed Ticket must revalidate its Mandate. CCC reference.
- **video-to-skill** — extracts UI steps from screen frames, not audio, and emits `SKILL.md`.
- **EpicGames/unreal-engine-skills** — official vendor skill decomposition for Claude Code.
- **aitmpl brainstorming skill** — catalog component scanned by NVIDIA SkillSpector.
- **Awesome-Hacking** — CC0 meta-index, 118.0k stars.
- **jailbreaks** — 31 adversarial prompt templates for defensive guardrail testing.
- **Pass:** dollarsforless.com (no content found), lawyered.lawyer (marketing site).

## Snippets

> "URL 6 (LiquidAI/d1-2B: immediate local millisecond visual pre-grade scoring, corner and centering box localization, and sold-comp confidence gating for /Users/claudiobarone/Projects/collectibles/briefs/ … plus local record triage for /Users/claudiobarone/Projects/atto and zero-cost local jev-gate execution for /Users/claudiobarone/Projects/CeminiParlays)" — report, aggregate summary

> "LiquidAI/d1-2B uses LFM Open License v1.0 (verify redistribution terms for packaged Atto kits versus internal Collectibles use, and prefer Transformers FP16 or d1-2B-MLX-8bit over GGUF when bounding boxes or span extractions are required)" — report, implementation friction

Phase-0 fetch of the d1-2B LICENSE, 2026-11-01:

> "Any Commercial Use of the Work or a Derivative Work by a Legal Entity that exceeds the Threshold is not licensed." Threshold defined as "$10,000,000 or more" in annual revenue.

Phase-0 fetch of the jeveryword README, 2026-11-01:

> "export TYPESAFE_API_KEY=…" — required for the bundled `createJevClient`. "On Vercel no key is needed, because AI Gateway accepts the project's own identity token."

## Dead Ends

- **Running jeveryword against Atto vault records or `Desktop/family/`.** The library is local, the model is not. Text leaves the machine unless a local Jev-equivalent model exists.
- **Treating the d1-2B MLX and GGUF builds as documented.** The model card documents Transformers only. The MLX and GGUF download counts are real, but their behaviour is unverified here.
- **Reading the PageIndex Extract as a reversal of the 2026-05-05 NO-GO.** It is not. The NO-GO was for the wiki layer. This batch targets archival PDFs, which is the stated re-entry condition.
