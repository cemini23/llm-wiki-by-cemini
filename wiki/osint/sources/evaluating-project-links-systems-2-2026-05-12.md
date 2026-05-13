---
title: Gemini Deep Research — Evaluating Project Links for Systems 2 (2026-05-12, 26 URLs)
type: source
tags: [source, gemini-deep-research, link-evaluation, tool-audit, cybersec-cross-route, langgraph, agent-frameworks, ip-sale-ready, cemini-stack, librarian-stack, workflow]
keywords: [gemini deep research, AIRecon, IDAssist, OpenAnt, AiSOC, Taranis AI, RedactDesk, Bug-Bounty-Agents, Sim, Accomplish, hermes-war-room, openalternative, awesome-design-md, multi-model-redteam, anthropic harness, firecracker, mac-code]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — Doc 1 (sibling Gemini eval, 23 URLs)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — refined multi-wiki prompt drafted from these two evaluations
- `@concepts/tool-evaluation-framework.md` — three-surface methodology
- `@concepts/cemini-license-posture.md` — license reject-list referenced throughout

## Raw Concept

- **Title**: Technology Evaluation and Architectural Integration Report
- **Authoring tool**: Gemini Deep Research (Google)
- **Source filename**: `Evaluating Project Links for Systems 2.docx`
- **Sha256**: `f3d56c2b848a3477...`
- **Size**: 3,087,044 bytes
- **Retrieved**: 2026-05-12
- **Read status**: deep-read (all 26 URLs extracted into structured inventory; entity stubs created)
- **Location** (canonical): `cemini-librarian:/opt/cemini-bulk/research/Evaluating Project Links for Systems 2.docx`

## Narrative

26-URL deep-research evaluation. 6 URLs UNAVAILABLE (openui, opensourceprojects.dev ×2, openfang, ai-engineering-hub/finetune-studio-mcp-app, dashy). 20 evaluable URLs. **Sibling to Doc 1; significantly more cybersec-leaning content** — drove much of the discovery for the cybersec-wiki cross-route batch.

Recommendation distribution:

- **Adopt: 3** (multi-model-redteam, awesome-design-md; cross-prompt: AutoTS extends from Doc 1)
- **Steal-from: 8** (Sim pgvector schema, Accomplish IPC patterns, hermes-war-room SSE/Kanban, OpenAnt vuln-discovery two-stage, Anthropic harness blog Planner/Generator/Evaluator, RedactDesk PDF content-stream mutation, Bug-Bounty-Agents persona patterns, CodeNomad CLI-proxy monorepo, AiSOC LangGraph Investigation Ledger)
- **Reference-only: 4** (OpenAlternative directory, AIRecon pentest-state pattern, Firecracker microVM blog, mac-code F_NOCACHE study, Virtual Memory blog)
- **Reject: 5** (Ducky GUI port-scanner, IDAssist IDA-Pro plugin, Taranis AI EUPL/16GB, Karma no-LICENSE, multi-model-redteam unlicensed)

### Headline calls

**Critical Steal-from** (highest leverage for Cemini):

- **Anthropic harness-design blog** ([URL 11](https://www.anthropic.com/engineering/harness-design-long-running-apps)) — Planner/Generator/Evaluator trinity + Sprint Contract mechanism + structured handoff artifacts. Direct LangGraph adaptation candidate at `agents/orchestrator.py`. Steal-from-tier; first ✅ in Cemini column across both docs.

- **AiSOC** ([URL 26](https://github.com/beenuar/AiSOC)) — MIT. ~600-line LangGraph Investigation Ledger pattern, 14 log sources, Neo4j ledger replaceable with Cemini's existing PostgreSQL. Steal-from for trade auditability (IP-sale-ready audit-log requirements).

- **OpenAnt** ([URL 10](https://github.com/knostic/OpenAnt)) — Apache-2.0. Detect→Attack two-stage LLM vulnerability discovery pipeline. Cross-routed primary to `@cybersecurity-wiki/`; Steal-from-tier for vuln-discovery methodology.

- **Sim** ([URL 4](https://github.com/simstudioai/sim)) — Apache-2.0. pgvector + agent-state DB schemas reusable for Cemini LangGraph extension. Full Next.js + Bun stack rejected on RAM budget.

**Critical Adopts**:

- **awesome-design-md** ([URL 25](https://github.com/VoltAgent/awesome-design-md)) — MIT. Curated DESIGN.md files for LLM-consumed UI styling. Adopt for wiki + cross-route to SEO + image-gen wikis.

- **multi-model-redteam** ([URL 14](https://github.com/permoon/multi-model-redteam)) — NOT FOUND license (gemini eval flagged this as "Adopt despite no LICENSE" — re-graded **CONDITIONAL-ADOPT** below per Cemini license posture).

**Critical Rejects (poison-pill licenses / no-LICENSE pattern)**:

- **Taranis AI** ([URL 16](https://github.com/taranis-ai/taranis-ai)) — EUPL-1.2 copyleft + 16GB RAM minimum. Reject for IP-sale; cross-route to cybersec-wiki for OSINT-threat-intel methodology.
- **Karma** ([URL 17](https://github.com/gh0stkey/Karma)) — no LICENSE file + "HACK THE WORLD" persona branding. 9th catalog mode #1 occurrence. Reject; RedactDesk supersedes for the same use case.
- **multi-model-redteam** (re-graded): No LICENSE file → workspace-laptop adoption fine (it's a 30-line prompt, not a code library, and the prompt content itself is in the public README — no IP risk for laptop-side use). **But cannot ship to Cemini prod or librarian server** until LICENSE clarified.

### Aggregate patterns

- **No-LICENSE catalog mode #1 occurrence**: 2 new findings (Karma URL 17, multi-model-redteam URL 14). Running total post-this-doc: 10+.
- **Cybersec false-NO-GO**: 11 cybersec-relevant tools in this doc got Reject or Reference-only on Cemini/wiki/workflow grounds — most of those have legitimate cybersec-wiki value. Cross-routed batch documented in `@cybersecurity-wiki/`.
- **EUPL surfaced as a new poison-pill family**: Taranis AI is the first EUPL-1.2 catch. EUPL is EU-friendly copyleft; same legal effect as AGPL for derivative-work obligations on hosted services. Added to license-posture catalog.

### Full per-URL inventory (26 URLs)

| # | Title | License | Tier | Cemini / Wiki / Workflow | Cross-wiki |
|---|---|---|---|---|---|
| 1 | openui | UNAVAILABLE | — | — | — |
| 2 | OpenAlternative | CC0-1.0 | Reference-only | ❌ / ❌ / ✅ | seo, image-gen, cybersec, 3d-printing |
| 3 | Ducky | MIT | Reject | ❌ / ❌ / ❌ | cybersec |
| 4 | Sim | Apache-2.0 | Steal-from | ⚠️ / ❌ / ❌ | — |
| 5 | opensourceprojects.dev/1969 | UNAVAILABLE | — | — | — |
| 6 | AIRecon | MIT | Reference-only | ❌ / ❌ / ⚠️ | cybersec |
| 7 | Accomplish | MIT | Steal-from | ❌ / ❌ / ✅ | — |
| 8 | Firecracker (blog) | proprietary (blog) | Reference-only | ❌ / ❌ / ✅ | cybersec |
| 9 | hermes-war-room | MIT | Steal-from | ⚠️ / ❌ / ✅ | — |
| 10 | **OpenAnt** | **Apache-2.0** | **Steal-from** | ❌ / ❌ / ✅ | **cybersec** (primary) |
| 11 | **Anthropic harness blog** | proprietary (blog) | **Steal-from** | **✅ / ❌ / ✅** | — |
| 12 | IDAssist | MIT | Reject (Cemini-fit) | ❌ / ❌ / ❌ | **cybersec** |
| 13 | openfang | UNAVAILABLE | — | — | — |
| 14 | multi-model-redteam | **NOT FOUND** | Conditional-Adopt (laptop only) | ❌ / ❌ / ✅ | cybersec |
| 15 | mac-code | MIT (per badge — UNVERIFIED) | Reference-only | ❌ / ❌ / ✅ | image-gen |
| 16 | Taranis AI | EUPL-1.2 | Reject | ❌ / ❌ / ❌ | cybersec |
| 17 | Karma | **NOT FOUND** | Reject | ❌ / ❌ / ❌ | cybersec |
| 18 | RedactDesk | MIT | Steal-from | ❌ / ❌ / ✅ | cybersec |
| 19 | Virtual Memory (blog) | proprietary (blog) | Reference-only | ⚠️ / ⚠️ / ✅ | — |
| 20 | finetune-studio-mcp-app | UNAVAILABLE | — | — | — |
| 21 | opensourceprojects.dev/95a66df5 | UNAVAILABLE | — | — | — |
| 22 | Bug-Bounty-Agents | MIT | Steal-from | ❌ / ❌ / ✅ | **cybersec** (primary) |
| 23 | dashy | UNAVAILABLE | — | — | — |
| 24 | CodeNomad | MIT | Steal-from | ❌ / ❌ / ✅ | — |
| 25 | **awesome-design-md** | **MIT** | **Adopt** | ❌ / ✅ / ✅ | seo, image-gen |
| 26 | **AiSOC** | **MIT** | **Steal-from** | **⚠️ / ❌ / ❌** | cybersec |

### Cross-wiki batch

12 stubs created in `@cybersecurity-wiki/entities/tools/`:
- IDAssist (IDA Pro plugin, LLM-driven binary RE)
- AIRecon (autonomous pentest agent)
- OpenAnt (LLM vulnerability discovery)
- Bug-Bounty-Agents (43 offensive personas)
- AiSOC (LangGraph SOC orchestrator)
- Taranis-AI (OSINT threat-intel platform)
- Karma (PII redaction, no-license)
- RedactDesk (PDF content-stream mutation)
- Awesome_GPT_Super_Prompting (jailbreak corpus)
- Ducky (network scanner GUI)
- TaskExplorer (Windows kernel introspection)
- multi-model-redteam (parallel red-team prompt)

Plus 1 concept stub in `@cybersecurity-wiki/concepts/`:
- llm-vulnerability-discovery (OpenAnt + IDAssist methodology synthesis)

2 stubs in `@image-gen-wiki/`:
- supertonic (TTS — financial speech specialization, but cross-relevant for persona-voice ops)
- mac-code (M-series flash-paging, cross-relevant for local image-gen inference on M-series)

3 stubs in `@seo-wiki/`:
- ai-marketing-skills (extends marketingskills.md)
- awesome-design-md (DESIGN.md design-system reference)
- openalternative (general OSS directory reference)

## Snippets

### URL 11 (Anthropic harness blog, only ✅ on Cemini in this doc)

> March 24, 2026, Anthropic core engineering. Adopt the Planner/Generator/Evaluator trinity, Sprint Contract mechanism, and structured handoff artifacts for LangGraph adaptation. Specific integration vector: extend `agents/orchestrator.py` with the GAN-style adversarial Evaluator node that gates state transitions on MCP-driven verification calls.

### URL 26 (AiSOC, IP-sale-ready trade auditability angle)

> Self-hosted AI Security Operations Center with ~600-line LangGraph orchestrator, Investigation Ledger in Neo4j, 14 log sources, public CI-gated eval harness with OpenAPI specs and Terraform/Helm packaging. Steal-from to port the LangGraph Investigation Ledger logic into Cemini agents/orchestrator.py (using existing PostgreSQL instead of Neo4j) for IP-sale-ready trade auditability.

### URL 16 (Taranis AI, EUPL-1.2 first catch)

> EUPL-1.2 copyleft + 16GB RAM/4-core NLP pipeline; massive resource + IP poison-pill problems. Cross-routed to cybersec-wiki where the OSINT methodology + MISP integration patterns are legitimately interesting independent of deployment.

## Dead Ends

- 6 UNAVAILABLE URLs (Gemini retrieval failures). Re-attempt with direct GitHub clone if any become priority.
- mac-code "MIT badge" — K39 audit (2026-05-12 earlier today) confirmed `gh api license.spdx_id` = null for this repo. Gemini eval missed the no-LICENSE flag. Catalog mode #1 occurrence already counted in K39 batch.

## NEEDS VERIFICATION

- `[NEEDS VERIFICATION 2026-05-12]` AiSOC actual line count (~600 quoted; verify against repo)
- `[NEEDS VERIFICATION 2026-05-12]` OpenAnt "verified vulnerability discovery" claim — Apache-2.0 confirmed via Gemini eval but vuln-discovery-tool claims need independent reproduction before any adoption commit.
- `[NEEDS VERIFICATION 2026-05-12]` Sim "exceeds 2-3GB RAM" — Gemini flagged this as estimate, not measurement. Verify before any Cemini-prod-stack consideration.
- `[NEEDS VERIFICATION 2026-05-12]` JetBrains Air pricing tier — proprietary preview state, BYOK; pricing tiers and ACP protocol stability change frequently in preview.
