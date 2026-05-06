---
title: loki-mode — Multi-Agent SDLC Framework (BUSL-1.1, License Drift Exemplar)
type: entity
tags: [tool, multi-agent-sdlc, busl-license, license-drift, reject-tier, ip-poison-pill, autonomous-coding]
keywords: [loki-mode, asklokesh, busl-1.1, business-source-license, license-drift, license-transition, sdlc-orchestrator, 41-agent-framework]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - concepts/ip-sale-readiness.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 14, **REJECT** tier — license is the kill, not the architecture
- @concepts/cemini-license-posture.md — **License Drift exemplar** for new mode #10 in license-pattern catalog (added K32, 2026-05-06)
- @concepts/ip-sale-readiness.md — BUSL-1.1 transition is poison pill for IP sale; even softened-monetization frame doesn't override (because aggregator-staleness is itself a maintainer-trust signal)

## Raw Concept

asklokesh/loki-mode is a multi-agent autonomous SDLC framework. Self-described: "Spec to deployed app. PRD, GitHub issue, OpenAPI/JSON/YAML, or one-line brief. 5 AI providers, 11 quality gates."

K32 DR verdict: **REJECT**. The license posture is the kill — the project transitioned from MIT to BUSL-1.1 (Business Source License) at a specific commit, but third-party aggregators (libraries.io, SourceForge mirror) still falsely report MIT. This pattern is what we call **License Drift**.

Documented here primarily as the catalog exemplar for mode #10 (License Drift), not for adoption analysis.

## Narrative

- **URL**: `https://github.com/asklokesh/loki-mode` ✓ DR-cited
- **License (current)**: BUSL-1.1 (Business Source License) per repository commits — verified by DR
- **License (aggregators report)**: MIT — false metadata, several months stale
- **Stack**: TypeScript/Bun runtime (per recent migration); legacy Python backend
- **Architecture**: 41 agent types across 8 swarms; 11 automated quality gates; 3-reviewer agent code review per task; ChromaDB-backed codebase search MCP server with 15 tools

### License Drift in detail (the catalog-exemplar value)

The drift went undetected by multiple third-party aggregators:

| Source | Claim | Status |
|--------|-------|--------|
| Repository `LICENSE` file (canonical) | BUSL-1.1 | Current, accurate |
| Repository commits (canonical) | Show MIT → BUSL-1.1 transition | Current, accurate |
| `LICENSE-CHANGE-NOTICE.md` (canonical) | Documents the change | Current, accurate |
| `https://sourceforge.net/projects/loki-mode.mirror/` | MIT | **STALE / WRONG** |
| `libraries.io/cargo/loki-mode` (or similar aggregator) | MIT (per DR analysis) | **STALE / WRONG** |
| Older online documentation / community summaries | MIT | **STALE / WRONG** |

**Operational lesson**: in any IP-due-diligence pass, license metadata MUST be sourced from the canonical repository's current `LICENSE` file + recent commit log + any `LICENSE-CHANGE-NOTICE.md`. **Aggregators are unreliable for time-shifted-license-changes** — they sync metadata at a point in time and may not reflect upstream license transitions for weeks or months.

This is the failure mode that catches engineers who run `pip-licenses` or `npm-license-checker` on a transitive dependency, get a "MIT" report, and proceed without checking the canonical repo.

### Why BUSL-1.1 is poison pill for IP sale

Business Source License v1.1 is **source-available with use restriction + future open-source conversion**. Key clauses:

- Source code is publicly visible and modifiable
- Use is restricted (typically: "non-production" or "non-competing-with-licensor")
- After a "Change Date" (commonly 4 years), the license auto-converts to a permissive license (commonly Apache-2.0 or MIT)

For Cemini's IP-sale frame, BUSL-1.1 is **not OSI-approved open source**. An institutional acquirer's diligence would flag any BUSL dependency in the production stack as a commercial-use risk. Even reading BUSL code with the intent to mirror algorithms in clean-room style is risky if the LLM-coding-agent path absorbs implementation patterns subconsciously (per K27 GPL-LLM-agent derivative-work risk).

### Even with monetization-priority softening, this is still REJECT

Per `monetization_priority_2026.md` memory, license-only auto-rejects soften when revenue is the bottleneck. But in this case the rejection isn't license-only — it's compounded:

1. **License Drift is a maintainer-trust red flag**: a project that transitions licenses without making the change widely visible (and lets aggregators stay stale) signals lower transparency. Future drift could happen again.
2. **41-agent / 8-swarm architecture cannot run on Cemini's 7GB Hetzner ceiling** — hardware mismatch alone is REJECT for production.
3. **TypeScript/Bun migration** vs Cemini's Python-first stack adds runtime complexity for marginal benefit.
4. **API token cost**: orchestrating 41 sub-agents per task drives DeepSeek API costs up exponentially with no proven marginal value over a well-crafted single-LangGraph implementation.

### Open questions (low priority — REJECT stands)

- ⚠ Exact "Change Date" in the BUSL transition (when does it become Apache/MIT)?
- ⚠ Are there licensed customers using loki-mode currently, or is this a side project that licensed itself to keep options open?

### Adoption status — REJECT (license + architecture)

Not adopted. Not under evaluation. Documented as License Drift catalog exemplar.

## Snippets

### License Drift — DR direct framing

> "While earlier versions or community summaries erroneously claim the project operates under MIT, repository commits explicitly demonstrate that the license was changed to BUSL-1.1 (Business Source License). The system context unequivocally states that 'BSL with restrictive terms' resides firmly on the poison-pill reject list. ... The foremost risk is License Drift. The project transitioned from the permissive MIT license to the restrictive BUSL-1.1 recently. However, online aggregators and older documentation still falsely report it as MIT. **Trusting third-party aggregators over the actual repository's commit history in an M&A context leads to catastrophic due-diligence failure.**" [Source: 5_6 links.docx URL 14]

### Operational scope (DR-cited)

> "asklokesh/loki-mode: Multi-agent autonomous SDLC framework. Spec to deployed app. PRD, GitHub issue, OpenAPI/JSON/YAML, or one-line brief. 5 AI providers, 11 quality gates." [Source: https://github.com/asklokesh/loki-mode (retrieved 2026-05-06)]
