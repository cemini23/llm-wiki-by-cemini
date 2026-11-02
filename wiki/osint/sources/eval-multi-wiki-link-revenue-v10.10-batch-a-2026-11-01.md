---
title: Multi-Wiki Link Revenue Evaluation v10.10 — batch A, 20 URLs (2026-11-01)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [multi-wiki link evaluation, runtime v10.10, phase-0, tool triage, karpathy, quants.md, global-law]
related:
  - entities/tools/lexifina-global-law.md
  - entities/tools/karpathy-autoresearch.md
  - entities/tools/quants-md.md
  - entities/tools/zero-breach-toolkit.md
  - entities/tools/parallel-ai.md
  - concepts/autoresearch-loop-pattern.md
  - concepts/historical-jurisdiction-atlas.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
  - concepts/regime-threshold-parameters.md
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
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Link Revenue Evaluation.docx` |
| Sibling | `Multi-Wiki URL Revenue Evaluation.docx` — same runtime version, different batch |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit. Priority #1 Atto and Collectibles (co-equal), #2 GuruWatcher and Basgiath, #3 CeminiDFS, #4 CeminiParlays |

The two `.docx` files share the internal title "v10.10". They are two different batches. This page covers the batch whose inbox filename says **Link**. See @sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md for the other.

Batch theme: Karpathy pretraining and tokenization, open trading-strategy libraries, agentic web extraction, git-versioned statutory corpora, offline spyware forensics, and 2D/3D rendering toolchains.

## Narrative

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License |
|---|------|------|--------------|-------------|---------|
| 1 | karpathy/minbpe | Context | CCC | none | MIT |
| 2 | karpathy/nanoGPT | Pass | CCC | none | none found |
| 3 | karpathy/llm.c | Context | CCC, Cybersec | none | none found |
| 4 | karpathy/nanochat | Context | CCC | none | none found |
| 5 | karpathy/autoresearch | **Extract** | CCC, Gambling, OSINT | ceminidfs, collectibles, xsp-killer | MIT (verified) |
| 6 | quants.md | **Extract** | OSINT | xsp-killer, guruwatcher | none stated |
| 7 | debuffjp/spryte | Context | Game-dev | none | none found |
| 8 | zeux/meshoptimizer | Context | Game-dev, 3D-printing | basgiath (minor) | MIT |
| 9 | Auburn/FastNoise2 | Context | Game-dev, Image-gen | none | MIT |
| 10 | platform.parallel.ai | **Watch** | OSINT, CCC | collectibles, atto, guruwatcher | proprietary SaaS |
| 11 | NSFW-API/NSFW_Wan_1.3b | Pass | Image-gen | none | CreativeML OpenRAIL-M |
| 12 | interplains/Zero-Breach-Toolkit | **Extract** | Cybersec | local-abliterated-lab | Apache-2.0 |
| 13 | heyclicky.com | Pass | CCC | none | proprietary |
| 14 | TokisanGames/Terrain3D | Context | Game-dev | none | MIT |
| 15 | RodZill4/material-maker | Context | Game-dev, Image-gen | basgiath | MIT |
| 16 | effekseer/Effekseer | Context | Game-dev | none | MIT |
| 17 | Zylann/godot_voxel | Context | Game-dev | none | MIT |
| 18 | lexifina/global-law | **Extract** | OSINT, CCC | atto, family-tree | CC0-1.0 |
| 19 | karpathy/micrograd | Pass | CCC | none | MIT |
| 20 | karpathy/nn-zero-to-hero | Pass | CCC | none | MIT |

Tally: 0 Integrate, 4 Extract, 1 Watch, 10 Context, 5 Pass, 0 unavailable.

### The four extracts

**URL 18, lexifina/global-law → Atto.** The report claims a local, zero-network Python stdio MCP server with 18 read-only tools, and a git-commit-per-event provenance model. It routes this to `atto-mcp` and `~/AttoVault/` to ground citizenship proofs in the law in force on an ancestor's vital-event date. Phase-0 corrected the coverage claim — see below.

**URL 5, karpathy/autoresearch → CeminiDFS, Collectibles, xsp-killer.** The report extracts an autonomous hill-climbing loop. An agent proposes a mutation, runs a bounded evaluation, and keeps only the change that beats the incumbent. It pairs this with URL 6 to prevent in-sample overfitting. Phase-0 found a hardware gate — see below.

**URL 6, quants.md → xsp-killer, GuruWatcher.** The report extracts walk-forward validation harnesses, explicit order templates (bracket, stop-limit, trailing stop-limit), and risk sizing (monthly circuit breaker, risk-parity capped). The report itself warns that many catalog strategies post sub-0.5 Sharpe.

**URL 12, interplains/Zero-Breach-Toolkit → local-abliterated-lab.** The report extracts an offline, read-only, zero-dependency spyware IOC scanner. Its useful part is the three-part output contract: what was found, an evidentiary strength grade, and an explicit list of surfaces that could not be checked.

### Watch, and why

**platform.parallel.ai.** The report routes it to Collectibles and Atto for structured dataset discovery and change monitoring. It holds it in Watch on measured latency: about 13.6 s per Search Pro request against 669 ms for Brave and 1 335 ms for Firecrawl. Five sequential agent calls compound to about 68 s. Live JavaScript extraction takes 60–90 s. Pricing is fragmented across six APIs and nine task tiers, from $0.12 to $2.40 per request. The report requires a head-to-head latency and accuracy bake-off against Firecrawl before any paid commitment.

### Phase-0 corrections

Phase-0 ran on 2026-11-01. GitHub egress is denied in the session sandbox, so repository clones were not available. Checks used source files fetched directly from the raw content hosts. This level confirms license text, README claims, and manifest data. It does not confirm commit depth, issue counts, or full tree structure.

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| lexifina/global-law | "Audit the Italian submodule (italy-law) for historical 1865, 1912, and 1948 statutory coverage" | Italy **is** present at `italy/national/acts`, covering the Constitution, every legge costituzionale, and L. 300/1970. **Coverage begins 1947-02-22.** No 1865 or 1912 corpus. The manifest flags "corpus.json lacks language" and "corpus.json has no citation rule". | The extract covers **1948 onward only**. The two eras that matter most for jure sanguinis — the 1865 Civil Code and Law 555/1912 — are absent. Downgrade to partial fit. |
| karpathy/autoresearch | Routed to CeminiDFS, Collectibles, and xsp-killer with no hardware note | Exists, 99.0k stars, **MIT**. The loop requires **one NVIDIA GPU** (tested on H100), Python 3.10+, and `uv`. Three files matter: `prepare.py` fixed, `train.py` agent-edited, `program.md` human-edited. Five-minute wall-clock budget per run, metric `val_bpb`. | The **pattern** transfers. The **code** does not run on the Apple Silicon laptop. Extract the loop contract, not the harness. |
| karpathy/autoresearch | "NOT FOUND" for stars, commit, and license | Resolved: 99.0k stars, MIT, active | Clears the report's license doubt. |

### Everything else

The ten Context rows and five Pass rows carry no action. They are catalogued so a later sweep does not re-evaluate them. Notable Pass reasons:

- **nanoGPT** — deprecated upstream in November 2025 in favour of nanochat.
- **NSFW_Wan_1.3b** — adult text-to-video weights with no project overlap.
- **heyclicky.com** — a screen-watching desktop agent. It conflicts with the Atto PII vault boundary and the CeminiParlays no-automated-slip rule.
- **micrograd**, **nn-zero-to-hero** — teaching material.

The Game-dev block (spryte, meshoptimizer, FastNoise2, Terrain3D, material-maker, Effekseer, godot_voxel) is uniformly Context. Basgiath ships on Minecraft Bedrock through MCPEDL and CurseForge. Re-platforming to Godot would remove that distribution surface. Only **material-maker** earns a routing line: it can author copyright-clean fan textures under the Basgiath ban on official art.

## Snippets

> "URL 18 (lexifina/global-law) → Projects/atto (atto-mcp, ~/AttoVault/, Priority #1) + Desktop/family/research/: extract the local, zero-network Python stdio MCP server (tools/mcp_server.py with 18 read-only tools for dated YYYY-MM-DD statutory lookups, diffs, and word-level attribution) and the git-commit-per-event temporal provenance schema." — report, aggregate summary

> "Audit the Italian submodule (italy-law) for historical 1865, 1912, and 1948 statutory coverage before citing in concierge packets." — report, URL 18 business risk

> "License: CC0-1.0 for repository structure and tooling (NOASSERTION on GitHub API; underlying statutory text in each country submodule remains governed by that jurisdiction's repository terms)." — report, URL 18

Phase-0 fetch of `manifest.json`, 2026-11-01:

> "Italian law: the Constitution, every legge costituzionale, L. 300/1970…" — coverage begins `1947-02-22`, latest record `2026-06-23`, tool `tools/vigente.py`.

> "corpus.json lacks language (defaults are used)"; "corpus.json has no citation rule"

## Dead Ends

- **Running autoresearch's harness on the laptop.** It needs an NVIDIA GPU. The laptop is Apple Silicon. Only `program.md` and the keep-or-revert contract transfer.
- **Citing global-law for pre-1948 Italian citizenship law.** The corpus starts at 1947-02-22. The 1865 Civil Code and Law 555/1912 are outside it. Atto still needs a separate pre-1948 source.
