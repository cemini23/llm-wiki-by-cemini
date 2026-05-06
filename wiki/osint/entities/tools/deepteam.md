---
title: deepteam — LLM Red-Teaming Framework (Apache-2.0, Vendor-Pull SaaS)
type: entity
tags: [tool, llm-redteam, security-eval, apache-2-license, defer-tier, owasp-llm-top-10, confident-ai-saas-vendor-pull]
keywords: [deepteam, confident-ai, llm-jailbreaking, prompt-injection, owasp-top-10-llms-2025, mitre-atlas, nist-ai-rmf, deepseek-redteam, real-time-guardrails]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - concepts/mitre-atlas-taxonomy.md
  - entities/infrastructure/deepseek-api.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 7, **DEFER** tier (laptop-side workflow OK; Cemini-prod blocked on RAM profiling)
- @concepts/cemini-license-posture.md — Apache-2.0 (clean); axis is operational (RAM) + commercial pull-up (Confident AI SaaS), not license
- @concepts/mitre-atlas-taxonomy.md — deepteam directly references MITRE ATLAS as one of its compliance frameworks
- @entities/infrastructure/deepseek-api.md — primary candidate target for red-team scans (Cemini's LLM brain endpoint)

## Raw Concept

confident-ai/deepteam is a comprehensive open-source Large Language Model red-teaming and continuous evaluation framework. Equips developers with 50+ vulnerabilities and 20+ research-backed adversarial attack methods (jailbreaking, prompt injection, single-turn + multi-turn). Tests against OWASP Top 10 for LLMs 2025, NIST AI RMF, MITRE ATLAS. Provides 7 production-ready guardrails for real-time LLM I/O classification.

K32 DR verdict: **DEFER**. License is clean. RAM footprint of real-time guardrails is undocumented and risks OOM on Cemini's 7GB Hetzner ceiling. SaaS vendor-pull-up via Confident AI platform is a cost/lock-in axis to monitor.

## Narrative

- **URL**: `https://github.com/confident-ai/deepteam` ✓ DR-cited
- **License**: Apache-2.0 — clean, IP-sale safe
- **Stack**: Python (CLI + library); integrates with arbitrary LLM endpoints
- **Maturity**: not extracted from DR; need follow-up

### Two integration vectors with different risk profiles

**Vector 1 — Workflow (laptop-side red-team testing)**

Install via `pip install -U deepteam` on the developer laptop. Before shipping a brief or modifying the LangGraph state machine, run `deepteam` adversarial scans against the proposed logic. The local execution doesn't touch production RAM constraints; vulnerability reports are static markdown.

**Recommendation**: clean adopt path on the laptop. Apache-2.0, no resource concerns.

**Vector 2 — Production guardrails (real-time inline)**

deepteam ships 7 guardrail classifiers designed for **real-time binary classification of LLM inputs and outputs**. These could pre-filter:

- Untrusted GDELT news ingest (jailbreak-injection risk in news content)
- Open-web scraping outputs (prompt-injection in scraped pages)
- User-supplied trader queries (in any future user-facing interface)

But the classifier models themselves consume RAM. With Cemini's 7GB ceiling already accommodating PostgreSQL + pgvector + Redis + Polars + LangGraph + DeepSeek-API client, adding 7 classifier models (resident memory undocumented) risks OOM.

**Recommendation**: **DEFER** until RAM profile is measured locally. Could be 50MB total or 500MB total — undocumented.

### Confident AI vendor pull-up (cost/lock-in axis)

The deepteam project actively integrates with the Confident AI commercial SaaS platform for managing risk assessments and dashboarding advanced vulnerability monitoring. The OSS framework is functional standalone, but the upgrade path to "advanced" tier funnels through the SaaS.

This is a soft license-compliance pattern (not in catalog yet — possibly mode #11 candidate, "Apache + commercial vendor pull-up"). Operational implication: if Cemini adopts deepteam workflow-side and finds it valuable, the natural growth path leads to a Confident AI SaaS subscription. Budget that vector before adoption.

### Why DEFER not REJECT not ADOPT

DEFER tier captures three states:

1. License is fine (Apache-2.0)
2. The capability is genuinely useful (LLM red-teaming for production-grade Cemini-prod safety)
3. Two undocumented operational concerns (RAM footprint + token cost) prevent immediate adoption decision

Path forward when monetization-priority creates real urgency:

1. Profile deepteam classifiers' RAM footprint locally (laptop measurement)
2. Estimate deepseek-api token cost for a representative red-team sweep (multi-turn attacks consume budget)
3. If RAM < 300MB total and per-sweep cost < $5, ADOPT for laptop-side; production decision separately

### Open questions

- ⚠ Resident RAM footprint of all 7 production guardrails running concurrently in a FastAPI dependency injection chain
- ⚠ Latency overhead per LLM call when guardrails are inline
- ⚠ DeepSeek API token cost for a full red-team sweep (50+ vulns × 20+ attack methods × multi-turn)
- ⚠ Which OWASP LLM Top 10 vulns are most relevant to Cemini's actual production attack surface (financial-data-driven LLM with open-web ingest)?

### Adoption status — DEFERRED

Not adopted. Workflow-side adoption is unblocked but deferred until concrete need (e.g., adversarial testing required by an acquirer or partner).

## Snippets

### deepteam scope (DR direct quote)

> "Deepteam is a comprehensive, open-source Large Language Model (LLM) red-teaming and continuous evaluation framework. It equips developers with over 50 ready-to-use vulnerabilities and more than 20 research-backed adversarial attack methods—encompassing both single-turn and multi-turn vectors like jailbreaking and prompt injection. It is explicitly designed to pressure-test LLM applications against established safety frameworks, including the OWASP Top 10 for LLMs 2025, NIST AI RMF, and MITRE ATLAS." [Source: 5_6 links.docx URL 7]

### Confident AI vendor pull-up framing

> "The project exhibits a clear platform upsell strategy; it heavily integrates with the 'Confident AI' commercial platform for managing risk assessments, indicating a potential vendor lock-in vector for advanced vulnerability monitoring and dashboarding. Operationally, executing multi-turn adversarial attacks automatically against the DeepSeek API during testing phases will incur substantial, recurring token costs that must be budgeted." [Source: 5_6 links.docx URL 7]
