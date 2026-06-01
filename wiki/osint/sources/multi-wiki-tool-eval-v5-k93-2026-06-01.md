---
title: Multi-Wiki Tool Evaluation Report v5 (34 URLs) — K93 ingest
type: source
tags: [source, tool-evaluation, multi-wiki-routing, license-audit, k93]
keywords: [tool-eval-v5, revfactory-harness, netviz, deptry, goaccess, omniVoice-reject, ogi-agpl]
related:
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - entities/tools/revfactory-harness.md
  - entities/tools/shadowarcanist-netviz.md
  - entities/tools/agents-best-practices.md
  - entities/tools/goaccess.md
  - entities/tools/deptry.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
clusters: [tool-evaluation]
---

## Relations

- @concepts/cemini-license-posture.md — never trust docx license claims
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md
- @entities/tools/revfactory-harness.md — Adopt (Apache-2.0 verified)
- @entities/tools/shadowarcanist-netviz.md — Adopt (MIT verified)
- @entities/tools/agents-best-practices.md — promoted Defer → Adopt (MIT verified)
- @entities/tools/goaccess.md — Adopt (MIT verified)
- @entities/tools/deptry.md — Adopt (MIT verified)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation Report (v5) |
| URLs | 34 |
| Location | `research to be indexed/Tool Evaluation and Wiki Fit.docx` |
| sha256 | `c6eec4cb060d75f7…` (3,024,438 bytes) |
| License spot-check | `.local/reports/license-spot-check-2026-06-01-1738.txt` |
| Read | 2026-06-01 deep-read (tiers + gh api overrides) |

## Narrative

### Aggregate tiers (per-URL lines authoritative)

| Tier | Count | Notes |
|------|-------|-------|
| Adopt | 5 | harness, netviz, agents-best-practices, goaccess, deptry |
| Steal-from | 1 | claude-code-ultimate-guide (CC-BY-SA-4.0 — reference only) |
| Reference-only | 9 | Anthropic/LangChain docs |
| Defer | 7 | OpenDataLoader PDF, Typst, reverse-skill, library-skills, deep-eye, memory-os, ai-sales-team |
| Reject | 9 | OmniVoice commercial poison, crocoddyl domain mismatch, MNN, OGI **AGPL-3.0**, cyber-llm-agents, etc. |
| UNAVAILABLE | 3 | brain-in-a-box, multiagent-coaching, threadron |

### License overrides (gh api)

| Repo | Eval claim | Verified |
|------|------------|----------|
| debpalash/OmniVoice-Studio | NO LICENSE | **NOASSERTION** custom commercial — **Reject** |
| khashashin/ogi | — | **AGPL-3.0** — hard reject |
| revfactory/harness | Apache-2.0 | **Apache-2.0** ✅ |
| ShadowArcanist/netviz | — | **MIT** ✅ (prior batch: Steal-from → Adopt for cybersec viz) |
| DenisSergeevitch/agents-best-practices | — | **MIT** ✅ |
| allinurl/goaccess | — | **MIT** ✅ |
| osprey-oss/deptry | — | **MIT** ✅ |
| FlorianBruniaux/claude-code-ultimate-guide | — | **CC-BY-SA-4.0** — reference, not prod link |

### Cross-wiki routing

- **CCC:** harness Adopt, agents-best-practices, Anthropic doc references
- **Cybersec:** netviz Adopt (network graph viz)
- **SEO:** goaccess (log analytics for marketing sites)
- **OSINT:** deptry (Python dep hygiene in ingest scripts)

No world-cup-bot overlap on Adopt rows.

## Snippets

> "AGPL-3.0… automatically triggers a hard rejection for any IP-sale-bearing surface." [Source: Tool Evaluation and Wiki Fit.docx v5 — aligns with @concepts/cemini-license-posture.md]
