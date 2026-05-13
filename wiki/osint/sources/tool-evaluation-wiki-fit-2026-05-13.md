---
title: "Gemini DR — Tool Evaluation and Wiki Fit (v2, 34 URLs, 2026-05-13)"
type: source
tags: [source, gemini-deep-research, link-evaluation, tool-audit, multi-wiki, ip-sale-ready, cemini-financial, cybersec-wiki, license-quarantine, threat-intel-saas]
keywords: [gemini deep research, multi-wiki eval, PYDNS-Scanner, claude-code-telegram, GitNexus, markra, PraisonAI, mirage, openhuman, frona, shodan, hunter, fullhunt, onyphe, socradar, intelx, pulsedive, ivre, mcp, vfs, virtual-filesystem]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
  - concepts/threat-intel-saas-cluster.md
  - entities/tools/pydns-scanner.md
  - entities/tools/claude-code-telegram.md
  - entities/tools/gitnexus.md
  - entities/tools/markra.md
  - entities/tools/praisonai.md
  - entities/tools/mirage.md
  - entities/tools/openhuman.md
  - entities/tools/frona.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- Cross-wiki routing brief: `@cybersecurity-wiki/briefs/2026-05-13_k42-cybersec-routing.md` (sibling of wiki/, not lint-tracked)
- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — sibling K42 doc
- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — sibling K42 doc
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — K40 prompt definition
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/cemini-license-posture.md` — license posture
- `@concepts/paradigm-vs-license-inverse-correlation.md` — emerging pattern (strongest evidence in this doc)
- `@concepts/threat-intel-saas-cluster.md` — new concept page documenting the rejected SaaS family (Shodan/FullHunt/ONYPHE/SOCRadar/Pulsedive/IntelX/Hunter/PublicWWW)

## Raw Concept

- **Source**: `Tool Evaluation and Wiki Fit.docx` (3.08 MB)
- **Author**: Gemini Deep Research (v2 multi-wiki prompt, executed 2026-05-13 08:04)
- **Type**: Multi-wiki link evaluation report (v2 May 2026 cohort with executive architectural synthesis)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/tool-evaluation-wiki-fit-2026-05-13.docx` (post-scp)
- **Retrieved**: 2026-05-13
- **Pages**: 34 URL evaluations + executive synthesis + aggregate + cross-routing + license summary + works-cited
- **Read status**: deep-read

Doc 3 of the K42 link-eval triplet. **Strongest of the three for architectural intelligence** — the executive synthesis explicitly identifies the MCP-as-standard-transport + VFS-mount + deterministic-graph-RAG paradigm shift; surfaces the threat-intel SaaS cluster (8 commercial Rejects); and captures the license-quarantine pattern explicitly via BSL 1.1 (Frona) + PolyForm-Noncommercial (GitNexus) + AGPL-3.0 (Markra) + GPL-3.0 (OpenHuman, IVRE).

## Narrative

### Executive synthesis (paraphrased)

> May 2026 paradigm: MCP as standard transport. Unified Virtual File Systems (Mirage) replace bespoke SDKs by mounting MongoDB/Redis/S3/GDrive as POSIX directory trees so LLMs use `grep`/`jq`/`cat` natively. Deterministic graph-backed memory (GitNexus → LadybugDB; Frona → SurrealDB; OpenHuman → SQLite/Obsidian) supersedes raw embedding-similarity. Sandboxed execution (Frona rootless OCI, PraisonAI Shadow Git Checkpoints) becomes paramount as agents transition from drafting code to executing it.

This is the most useful single passage across all 3 K42 docs — captures the architectural moment the eval is pricing.

### Aggregate

| Tier | Count | Items |
|------|------:|-------|
| Adopt | 3 | PYDNS-Scanner (Cybersec), PraisonAI (Cemini financial), markra (Workflow, AGPL-3.0 quarantine) |
| Steal-from | 4 | claude-code-telegram, mirage, openhuman, GitNexus |
| Defer | 0 | — |
| Reference-only | 1 | awesome-ai-agents-2026 |
| Reject | 12 | shodan.io, hunter.io, fullhunt.io, onyphe.io, socradar.io, Coalitioninc, ivre.rocks (GPL-3.0), publicwww.com, pulsedive.com, intelx.io, frona (BSL 1.1), shadcnstudio |
| UNAVAILABLE | 14 | trustclaw, tinyfish-cookbook/tinyskill, telltru.com, search.censys.io, vulners.com, wigle.net, agentmemory, draftside, runrate, tablericons, rapidform, euroscanner, peekaboo, tinylab |

### Primary-fit distribution

- Cemini financial: 2 (PraisonAI, mirage)
- OSINT wiki: 2
- Cybersec wiki: 10 ← **heaviest of all 3 docs**
- Image-gen wiki: 0
- SEO wiki: 1 (shadcnstudio)
- 3D-printing wiki: 0
- Workflow: 5
- None: 14

**The most cybersec-heavy of the 3 K42 docs.** The threat-intel SaaS cluster (Shodan/FullHunt/ONYPHE/SOCRadar/Pulsedive/IntelX/Hunter/PublicWWW/Coalitioninc-BinaryEdge) accounts for 9 of the 10 Cybersec primary-fits, all Reject for lack of OSS license.

### Specific Adopt details

**PraisonAI** (7.5k stars, MIT, Python+TS+Rust, multi-DB): The most credible Cemini-financial Adopt candidate of all 3 K42 docs. Native **Doom Loop Detection** (auto-recover from recursive logic traps — direct utility against the autonomous-trading buy/sell loop risk) + **Shadow Git Checkpoints** (filesystem rollback on execution failures — direct utility for sandboxed Polymarket/Kalshi adapter execution). Competing orchestration framework to current LangGraph in Conductor stack. **Phase-0 audit warranted before Adopt commitment.**

**mirage** (2.1k stars, Apache-2.0, TS+Python+Redis, Strukto AI): Unified Virtual File System mounting MongoDB/Redis/S3/GDrive as POSIX paths so LLMs use stdlib Bash tools. Cemini direct utility: mount Redis Streams + Postgres backtesting tables under `/opt/cemini/vfs/` so agents `grep` market data without bespoke SDK code. Steal-from tier (extract two-layer cache architecture: Index cache + File cache) rather than full Adopt — too much scope for current Conductor needs.

**PYDNS-Scanner** (330 stars, MIT, Python 3.11+ async): Cybersec-primary. SlipNet mode for DNSTT and NoiseDNS tunnel verification (red-team reconnaissance). Cross-route brief to OSINT-wiki for ISP/AS-number detection heuristics. Workflow Catalog the Textual TUI as standard for laptop-side diagnostic tools.

**markra** (103 stars, AGPL-3.0, Tauri+Rust): Local-first WYSIWYG Markdown editor with native Ollama integration. AGPL-3.0 confines to non-shipped Workflow only — never near `/opt/cemini` artifacts. Use-case: laptop-side wiki editor that doesn't ping cloud telemetry. Lower priority than syncthing for laptop ops.

### Steal-from details

**GitNexus** (38.1k stars, **PolyForm-Noncommercial-1.0.0**): 12-phase DAG ingestion pipeline parses Tree-sitter ASTs into LadybugDB semantic graph entirely in-browser via WASM. The 6-stage call-resolution pipeline (extract-call → emit-edge) is bleeding-edge for static code analysis. Existing `@entities/tools/gitnexus.md` page should be updated to cross-reference this v2 eval and note the PolyForm license confirms our existing classification.

**openhuman** (3.6k stars, GPL-3.0): TokenJuice HTML→Markdown compression layer claiming ~80% token cost reduction; SQLite memory tree syncs with Obsidian markdown vault. GPL-3.0 forbids `/opt/cemini` integration; methodology extraction only — adopt the **compression heuristics**, not the codebase.

**claude-code-telegram** (2.6k stars, MIT, FastAPI+SQLite+Whisper STT): CLAUDE_ALLOWED_TOOLS env array + APPROVED_DIRECTORY sandboxing — architectural blueprint for hardening local MCP servers against path-traversal. >85% pytest coverage, strict mypy. Steal: webhook event-driven components for isolated laptop-side task schedulers.

### Threat-intel SaaS cluster (Reject, but value-extractable methodology)

| Tool | Capability | Why Reject |
|------|-----------|------------|
| Shodan | Internet Intelligence; exposed ports, TLS certs, global IP enrichment | NO LICENSE FOUND; closed SaaS |
| FullHunt | EASM with native MCP server, CVE-to-attack-surface mapping | NO LICENSE FOUND |
| ONYPHE | 20B banners + 5B DNS records monthly; 48mo passive DNS history | NO LICENSE FOUND |
| SOCRadar | Agentic Threat Intelligence (ATI) via conversational MCP | NO LICENSE FOUND |
| Pulsedive | MITRE ATT&CK enrichment; STIX/TAXII 2.1 → SIEM | NO LICENSE FOUND |
| IntelX | Darknet buckets (Stealer Logs, COMB); Simhash similarity | NO LICENSE FOUND |
| Hunter | Email/domain mapping for corporate entity profiling | NO LICENSE FOUND |
| PublicWWW | Source-code signature search across 516M pages | NO LICENSE FOUND |
| Coalitioninc | BinaryEdge transition (deprecated standalone) | Proprietary acquisition |

All 9 documented for OSINT-wiki methodology reference (their CTI workflows are real and battle-tested) but **zero codebase integration** allowed by IP-sale posture. → captured in new `@concepts/threat-intel-saas-cluster.md`.

### License pattern (strongest evidence across the 3 docs)

- **NO LICENSE FOUND**: 10 (the SaaS cluster + shadcnstudio)
- **Poison-pill licenses**: 5 (GitNexus PolyForm-Noncommercial; Markra AGPL-3.0; OpenHuman GPL-3.0; IVRE GPL-3.0; Frona BSL 1.1)
- **Clean MIT/Apache/BSD**: 4 (PYDNS-Scanner, claude-code-telegram, PraisonAI, mirage)

**Confirming the inverse-correlation hypothesis**: the most technically sophisticated tools (GitNexus 12-phase DAG, Frona rootless OCI, OpenHuman TokenJuice 80% compression, Markra Tauri local-first) all carry license restrictions deliberately preventing commercial expropriation. Clean-licensed tools tend to be conventional in scope.

### Critical flags

**Flag 1 — PraisonAI Adopt** for Cemini financial primary fit:

Implies replacing or supplementing LangGraph in Conductor stack. Doom Loop Detection + Shadow Git Checkpoints are real safety primitives. But adoption decision requires:
- Phase-0 audit on Conductor compatibility (LangGraph already wires Conductor's 4-stage pipeline)
- License confirmation (MIT eval claim → verify LICENSE file)
- Performance latency vs Polymarket/Kalshi adapter SLAs
- Migration cost from current LangGraph adapters

→ ROADMAP item: **PraisonAI Phase-0 audit**, K42 follow-up.

**Flag 2 — mirage VFS pattern** as Cemini-financial Steal-from:

VFS mount for Redis Streams + Postgres backtesting is architecturally compelling. But Cemini's Phase-0 audit pattern requires verifying production-readiness (2.1k stars is moderate; 13 open issues; recent May 2026 commit). → ROADMAP item: **mirage VFS evaluation — viability of VFS-mount /opt/cemini data layer**.

**Flag 3 — GitNexus existing entity page update**:

Existing `@entities/tools/gitnexus.md` records prior assessment. Doc 3 confirms PolyForm-Noncommercial-1.0.0 — must cross-link. The 12-phase DAG architecture is referenced for Workflow-side stub creation only.

### Cross-wiki routing scope (off-OSINT)

- **cybersec-wiki**: 8 stubs for threat-intel SaaS cluster (Shodan, FullHunt, ONYPHE, SOCRadar, Pulsedive, IntelX, Hunter, PublicWWW) — methodology documentation, not codebase. **Compress into one cluster brief** rather than 8 individual stubs.
- **cybersec-wiki**: stub for PYDNS-Scanner (DNS recon)
- **cybersec-wiki**: stub for IVRE (GPL-3.0 quarantine, methodology only)
- **cybersec-wiki**: stub for frona (BSL 1.1 quarantine, OCI sandbox methodology)
- **seo-wiki**: stub for shadcnstudio (Reject for license, but design-template methodology valuable for DESIGN.md templates)
- **image-gen-wiki**: 0
- **3d-printing-wiki**: 0

## Snippets

- **VFS paradigm**: "Mirage…mounts disparate backend services (e.g., MongoDB, Redis, Amazon S3, Google Drive) under a single, unified directory tree, [allowing] language models to utilize the POSIX-compliant vocabulary they were trained on (e.g., grep, jq, cat) without requiring custom software development kits." [Source: Tool Evaluation and Wiki Fit.docx p.6/§Macro-Architectural]
- **PraisonAI safety primitives**: "native Doom Loop Detection to automatically recover from recursive logic traps, alongside Shadow Git Checkpoints that roll back the filesystem upon execution failures." [Source: ibid., §URL 9]
- **License-as-paradigm-tax**: "BSL and PolyForm Shift: Frona utilizes the Business Source License (BSL) 1.1, explicitly preventing third-party platform-as-a-service distribution until its scheduled conversion to Apache 2.0 in 2029. GitNexus utilizes PolyForm-Noncommercial-1.0.0, establishing a hard blockade on corporate utilization." [Source: ibid., §IP-Sale Readiness]

## Dead Ends

*(none — first ingest.)*

[Source: Tool Evaluation and Wiki Fit.docx (retrieved 2026-05-13)]
