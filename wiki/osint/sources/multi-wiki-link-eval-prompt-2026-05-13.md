---
title: "Gemini DR — Multi-Wiki Link Evaluation Prompt (37 URLs, 2026-05-13)"
type: source
tags: [source, gemini-deep-research, link-evaluation, tool-audit, multi-wiki, ip-sale-ready, cybersec-wiki, workflow, license-quarantine]
keywords: [gemini deep research, multi-wiki eval, marketingskills, n8n-workflows, tabularis, OpenSpec, syncthing, agent-lightning, YellowKey, GreenPlasma, witr, awesome-deep-research, 4gaBoards, home-assistant, Aegis, joplin, OsmAnd, immich, mealie]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
  - entities/tools/marketingskills.md
  - entities/tools/n8n-workflows.md
  - entities/tools/tabularis.md
  - entities/tools/openspec.md
  - entities/tools/syncthing.md
  - entities/tools/agent-lightning.md
  - entities/tools/yellowkey.md
  - entities/tools/greenplasma.md
  - entities/tools/witr.md
  - entities/tools/awesome-deep-research.md
  - entities/tools/home-assistant-core.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- Cross-wiki routing brief: `@seo-wiki/briefs/2026-05-13_k42-seo-routing.md` (sibling of wiki/, not lint-tracked)
- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — sibling K42 doc (33 URLs, Workflow-heavy)
- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — sibling K42 doc (34 URLs, threat-intel SaaS cluster)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — K40 prompt definition this batch uses
- `@concepts/tool-evaluation-framework.md` — methodology framework
- `@concepts/cemini-license-posture.md` — license-quarantine policy
- `@concepts/paradigm-vs-license-inverse-correlation.md` — emerging pattern

## Raw Concept

- **Source**: `Multi-Wiki Link Evaluation Prompt.docx` (71 KB)
- **Author**: Gemini Deep Research (multi-wiki prompt, executed 2026-05-13 08:19)
- **Type**: Multi-wiki link evaluation report
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-link-eval-prompt-2026-05-13.docx` (post-scp)
- **Retrieved**: 2026-05-13
- **Pages**: 37 URL evaluations + aggregate + cross-routing + works-cited
- **Read status**: deep-read

Doc 2 of the K42 link-eval triplet. Distinct cohort from Docs 1/3 — covers Workflow tooling (n8n, OpenSpec, syncthing), offensive cybersec payloads (YellowKey Bitlocker bypass, GreenPlasma privesc), and architectural references (home-assistant/core async Python).

## Narrative

### Aggregate

| Tier | Count | Items |
|------|------:|-------|
| Adopt | 5 | marketingskills, n8n-workflows (docs site + main repo), tabularis, OpenSpec, syncthing |
| Steal-from | 4 | agent-lightning, YellowKey, GreenPlasma, witr |
| Defer | 0 | — |
| Reference-only | 3 | Awesome-Deep-Research, 4gaBoards, home-assistant/core |
| Reject | 8 | deprecated-generative-ai-python (archived), Aegis (GPL-3.0), joplin (no license), OsmAnd (unverified), agent-brains.com (SaaS), Awesome-LLMs-for-Vulnerability-Detection (no license), immich (AGPL-3.0), mealie (AGPL-3.0) |
| UNAVAILABLE | 14 | InsForge, AdStrike, cc-statusline (×2 dupe), Sulphur-2-base, evals, text-based-osint-methods, person-of-interest-2026, kitchenowl, nextcloud/server, hantanet, Contexly, manuskript, agent-skills (Doc 2's instance unreachable), 4gaBoards (dupe) |

### Primary-fit distribution

- Cemini financial: 1
- OSINT wiki: 2
- Cybersec wiki: 4
- Image-gen wiki: 0
- SEO wiki: 1
- 3D-printing wiki: 0
- Workflow: 11
- None: 2

Workflow dominates (11/37 primary-fit) — laptop-side developer tooling is the dominant signal in this cohort.

### Cross-routing highlights

- **Cemini financial**: tabularis (MCP-native Postgres client → /opt/cemini DB integration); OpenSpec (Spec-Driven Development to enforce deterministic Python module generation); witr (process-ancestry telemetry for Redis Streams hygiene).
- **Cybersec-wiki**: Awesome-Deep-Research (multi-agent vuln-discovery blueprints); n8n-workflows (AI-BOM scanner heuristics for LangGraph mesh auditing — RCE detection, unauthenticated MCP, hardcoded API keys); YellowKey (Bitlocker bypass exploit methodology, MIT-licensed, Win 11/Server 2025); GreenPlasma (CTFMON privesc PoC, C++, May 2026).
- **OSINT-wiki**: n8n-workflows (LinkedIn 66-node scraping pipeline); syncthing (decentralized threat-intel dataset replication).
- **SEO-wiki**: marketingskills (.agents/skills/ structural schema for content automation).
- **Workflow**: marketingskills + agent-lightning (Microsoft RL agent tracing).

### License pattern

- **NO LICENSE FOUND**: 4 (joplin, agent-brains.com, Awesome-LLMs-for-Vulnerability-Detection, OsmAnd unverified)
- **Poison-pill (GPL/AGPL)**: 3 (Aegis GPL-3.0, immich AGPL-3.0, mealie AGPL-3.0)
- **Clean MIT/Apache/BSD/MPL**: 13 (most Adopts + Steal-from)

Confirms the established pattern: novel architectures with sophisticated capabilities tend to carry restrictive licenses; permissive licenses correlate with mature, mainstream tooling.

### Specific Adopt details

**n8n-workflows** (54k stars effective at 4,343 production-ready scripts): MIT-licensed, includes Trusera AI-BOM scanner for hardcoded API key + MCP client exposure detection + RCE risk identification via Code Execution + HTTP Request node chaining. Aggressive Adopt candidate.

**OpenSpec** (47.6k stars, MIT, tuned for Opus 4.5/GPT 5.2): Spec-Driven Development (SDD) imposing deterministic constraints on AI-generated code via `proposal.md`/`specs/`/`design.md` artifacts. Direct utility for `/opt/cemini` Python module generation.

**syncthing** (84k stars, MPL-2.0, v2.1.0 May 2026): Decentralized cryptographic file sync. Direct utility for replicating laptop-side Claude Code state + MCP server artifacts across multiple analyst machines.

**tabularis** (1.6k stars, Apache-2.0, Rust/Tauri v2, MCP-native): Direct integration of MCP server into PostgreSQL/SQLite clients for AI-assisted SQL generation. Direct utility for /opt/cemini PG instances.

**marketingskills** (Adopt for SEO/Workflow): `.agents/skills/` schema for Claude Code plugin integration on marketing content workflows.

### Cross-wiki routing scope (off-OSINT)

- **cybersec-wiki**: stubs for YellowKey, GreenPlasma, witr (3 items) + brief on n8n AI-BOM scanner methodology
- **seo-wiki**: stub for marketingskills (1 item)
- **3d-printing-wiki**: 0
- **image-gen-wiki**: 0

## Snippets

- **"4,343 production-ready automation scripts"** (n8n-workflows) — explicit count establishing this is not a curated demo set but a massive automation library. [Source: Multi-Wiki Link Evaluation Prompt.docx URL 8]
- **"viral copyleft contamination"** language repeatedly used for AGPL-3.0/GPL-3.0 rejections — terminology aligning with Cemini's documented poison-pill governance posture. [Source: ibid., multiple URLs]

## Dead Ends

*(none — first ingest.)*

[Source: Multi-Wiki Link Evaluation Prompt.docx (retrieved 2026-05-13)]
