---
title: "Security of deep research agents — attack surface and agenda seeding"
type: source
related:
  - concepts/generative-engine-optimization.md
  - concepts/geo-paid-placement-networks.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/ai-citation-sourcing-geo.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning |
| Authors | Yang Luo, Guangpu Chen, Yichen Liu, Zhaoyu Chen, Yifeng Gao, Zhiyang Ding, Qingni Shen, Zhonghai Wu (Peking University) |
| arXiv | 2611.20045 |
| Pages | 31 |
| File | `arxiv-2611.20045-security-of-deep-research-agents-attack-surface.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.20045-security-of-deep-research-agents-attack-surface.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

This paper surveys security for deep research agents. These agents read many web pages and write reports with citations, and users often treat the report as a research conclusion. Anyone who places content into the agent's retrieval results can change that conclusion.

The authors organize the field in four stages: retrieval, planning, evidence integration, and report generation. They align the area with retrieval-augmented generation (RAG) poisoning, prompt injection, and generative engine optimization (GEO). Of 34 primary studies, only 26.5% address the planning stage, and none tests end-to-end poisoning on commercial products.

**Agenda seeding.** The authors propose a new attack. The attacker writes no instructions and only introduces a fictitious evaluation metric into the web. Across 3,520 sandboxed research runs, GEO and prompt injection are nearly ineffective. Agenda seeding makes the attacker's target the top pick in 16% to 28% of reports. Injection detection, query anchoring, and verification prompting do not stop it, and verification prompting hurts utility.

**Prior poisoning evidence.** The paper cites WARP, which rewrites about 13 words on one frequently retrieved UGC page. That page is then retrieved in 57% to 76% of research runs and cited in 38% to 51% of reports.

**SEO relevance.** This is partial and indirect. The paper names GEO as a related threat and shows that content placement changes what agents report. It also shows that plain GEO is weak against a planning-stage attack, which suggests that defensive work must cover the whole agent pipeline, not only the retrieved text. The page links to the GEO concepts that this evidence touches. The percentages are single-source claims from this paper.

## Snippets

> "GEO and prompt injection are nearly ineffective, whereas agenda seeding makes the attacker's target the top pick in 16% to 28% of reports." [Source: `arxiv-2611.20045-security-of-deep-research-agents-attack-surface.pdf` p.1 (arXiv 2611.20045), retrieved 2026-11-22]

> "Only 26.5% of them involve the planning stage, and none performs an end-to-end poisoning evaluation on commercial products." [Source: same file, p.1]
