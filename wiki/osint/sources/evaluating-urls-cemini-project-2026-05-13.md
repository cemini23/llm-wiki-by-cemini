---
title: "Gemini DR — Evaluating URLs for Cemini Project (v2, 33 URLs, 2026-05-13)"
type: source
tags: [source, gemini-deep-research, link-evaluation, tool-audit, multi-wiki, ip-sale-ready, cybersec-wiki, seo-wiki, workflow, license-quarantine]
keywords: [gemini deep research, multi-wiki eval, tool audit, link evaluation, whale, claude-obsidian, open-seo, IDAssist, FuzzyAI, pentest-ai-agents, cua, PageIndex, agent-skills, autoharness, cypht, awesome-codex-subagents, Dulus]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
  - entities/tools/pageindex.md
  - entities/tools/claude-mem.md
  - entities/tools/whale.md
  - entities/tools/claude-obsidian.md
  - entities/tools/open-seo.md
  - entities/tools/idassist.md
  - entities/tools/fuzzyai.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/cua.md
  - entities/tools/agent-skills.md
  - entities/tools/autoharness.md
  - entities/tools/cypht.md
  - entities/tools/awesome-codex-subagents.md
  - entities/tools/dulus.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — sibling K42 doc (37 URLs, different cohort, earlier-form prompt)
- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — sibling K42 doc (34 URLs, threat-intel SaaS cluster, v2 prompt)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — K40 prompt definition this batch uses
- `@concepts/tool-evaluation-framework.md` — methodology framework
- `@concepts/cemini-license-posture.md` — license-quarantine policy this eval enforces
- `@concepts/paradigm-vs-license-inverse-correlation.md` — emerging pattern: novel architectures cluster in poison-licensed repos
- `@entities/tools/pageindex.md` — eval lists Adopt (98.7% FinanceBench); cross-reference notes the existing 2026-05-05 NO-GO covers the wiki-layer use case, not the long-form-document use case the FinanceBench score refers to
- `@entities/tools/claude-mem.md` — eval lists claude-obsidian Adopt; potential parallel-impl with already-adopted claude-mem (v13.0.1)

## Raw Concept

- **Source**: `Evaluating URLs for Cemini Project.docx` (3.05 MB)
- **Author**: Gemini Deep Research (v2 multi-wiki prompt, executed 2026-05-13 08:06)
- **Type**: Multi-wiki link evaluation report
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/evaluating-urls-cemini-project-2026-05-13.docx` (post-scp)
- **Retrieved**: 2026-05-13
- **Pages**: 33 URL evaluations + executive synthesis + aggregate summary + cross-routing batch + license pattern summary
- **Read status**: deep-read

Doc 1 of the K42 link-eval triplet. Most architecturally significant of the three — covers laptop-side workflow + cybersec + SEO surfaces with several flagship Adopts (whale, claude-obsidian, FuzzyAI, cua, PageIndex contra-flag).

## Narrative

### Aggregate

| Tier | Count | Items |
|------|------:|-------|
| Adopt | 9 | whale, claude-obsidian, open-seo, IDAssist, FuzzyAI, pentest-ai-agents, cua, PageIndex, agent-skills (header text says 8 — minor count error in source) |
| Steal-from | 3 | autoharness, cypht, awesome-codex-subagents |
| Defer | 1 | Dulus |
| Reference-only | 3 | awesome-list, awesome-ai-agents-2026, ratctf |
| Reject | 4 | RedditVideoMakerBot (GPL-3.0), codegraph-rust (NO LICENSE), mangofetch (GPL-3.0), Awesome-LLMs-for-Vulnerability-Detection (NO LICENSE) |
| UNAVAILABLE | 9 | evanflow, cybersecurity-attacks-on-sim-cards, CTI-RAG, Personal_AI_Infrastructure, 10458e77, stemdeck, local-deep-research, docuseal, AiToEarn |

### Primary-fit distribution

- Cemini financial: 1
- OSINT wiki: 1
- Cybersec wiki: 5
- Image-gen wiki: 0
- SEO wiki: 2
- 3D-printing wiki: 0
- Workflow: 10
- None: 1

Heavy Workflow + Cybersec skew. Most Adopt-tier content routes laptop-side or to cybersec-wiki, not to OSINT or Cemini financial.

### Cross-routing batch (key items)

**OSINT-wiki**: whale (DeepSeek prefix-cache for terminal scraping), claude-obsidian (3-round autoresearch loop for librarian), FuzzyAI (PAIR/Crescendo prompt-injection patterns for adversarial financial-news detection), openhuman (TokenJuice HTML compression — Reject but value-extract), PageIndex (hierarchical tree for long-form quant filings).

**Cybersec-wiki**: autoharness (tau2_bench defensive eval), claude-obsidian (`[!contradiction]` syntax for pentest report cross-ref), cypht (SRI + header fingerprinting for legacy PHP), awesome-ai-agents-2026 (EU AI Act compliance timelines), awesome-codex-subagents (security-auditor + browser_debugger personas), cua (QEMU sandbox API for malware execution analysis), agent-skills (security-auditor checklist injection).

**SEO-wiki**: open-seo (Adopt, primary fit).

**Workflow**: 10 items including IDAssist (laptop-side identity ops), agent-skills (skill structural schema), pentest-ai-agents (red-team automation).

### License pattern

- **NO LICENSE FOUND**: codegraph-rust, Awesome-LLMs-for-Vulnerability-Detection
- **Poison-pill (GPL-3.0)**: RedditVideoMakerBot, mangofetch
- **Clean MIT/Apache/BSD**: majority of Adopt + Steal-from tier
- Aggregate matches K40+K41 pattern: novel architectures tend to be poison-licensed; clean-licensed tools are typically more conventional.

### Critical flags vs existing wiki

**Flag 1 — PageIndex Adopt with "98.7% FinanceBench accuracy"** vs existing `@entities/tools/pageindex.md` **NO-GO 2026-05-05**:

The existing NO-GO is for the wiki-retrieval layer (single-file API, agentic per-query cost, no cross-link/frontmatter parsing). The 98.7% FinanceBench score refers to VectifyAI's Mafin 2.5 *product*, not the OSS lib's wiki-fit. The Doc 1 eval re-evaluates the OSS lib for long-form quant filings (10-Ks, FinanceBench-style) — a use case where the existing NO-GO explicitly says PageIndex re-enters consideration. **No contradiction; the two evaluations target different use cases.** Update PageIndex page to cross-link this batch.

**Flag 2 — claude-obsidian Adopt** vs already-adopted `@entities/tools/claude-mem.md` (v13.0.1, Phase-2 PASS 2026-05-12):

Eval recommends claude-obsidian for "3-round autoresearch loop into librarian tools" + "`[!contradiction]` syntax for cross-referencing conflicting reports". Both functions partially overlap with claude-mem's session-state cache + observation indexing. **Decision needed**: swap claude-mem → claude-obsidian, run parallel (different scope: claude-mem = session memory, claude-obsidian = wiki-side reasoning over markdown), or Reference-only. Default to **parallel-run** pending Phase-0 audit on claude-obsidian (license verification, repo maturity, conflict with existing claude-mem hooks).

**Flag 3 — autohardness / cypht / awesome-codex-subagents** at Steal-from tier:

Steal-from = extract methodology, don't import codebase. Per Cybersec routing batch these feed defensive-ops literature. No conflict with existing wiki; primary contribution is to cybersec-wiki.

### Cemini integration vectors (highest priority)

1. **whale (DeepSeek prefix-cache routing)** → Cemini financial: terminal-based market scraping
2. **PraisonAI** (from Doc 3, sibling) + **mirage** (Doc 3) — orchestration + VFS
3. **agent-skills schema** — embed `.agents/skills/` structural pattern into Cemini's Workflow surface
4. **FuzzyAI** PAIR/Crescendo adversarial patterns — defensive layer for news-rewriter robustness (intersects with `@concepts/verbalized-sampling-llm-diversity.md` Vector 5)
5. **cua QEMU sandbox** — possible isolation primitive for autonomous Cemini agent execution (intersects with K41 Forrest Chang weather bot's safety needs)

### Cross-wiki routing scope (off-OSINT)

Per Doc 1 routing batch + primary-fit distribution, the following stub/brief actions land in non-OSINT wikis:

- **cybersec-wiki**: stubs for autoharness, cypht, cua, FuzzyAI, awesome-codex-subagents, pentest-ai-agents (6 items) — to be created via `scripts/cross_wiki_route.py`
- **seo-wiki**: stub for open-seo (1 item)
- **image-gen-wiki**: 0
- **3d-printing-wiki**: 0

## Snippets

- **"BSL and PolyForm shift"** — eval flags the systemic license-quarantine pattern: novel orchestration engines and knowledge-graph compilers using Business Source License 1.1 and PolyForm-Noncommercial-1.0.0 specifically to prevent commercial expropriation. Same pattern observed across all 3 K42 docs.
- **"Model Context Protocol (MCP) as standard transport layer"** — the v2 prompt frames the May 2026 paradigm shift as MCP-default for agentic tooling; aligns with `@concepts/mcp-tool-marketplace.md`.

## Dead Ends

*(none — first ingest of this doc.)*

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13); arXiv: N/A]
