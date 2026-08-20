---
title: "CTIFoundry — agent-native CTI corpus scaffold (arXiv 2608.18613)"
type: source
tags: [arxiv, cti, cyber, k243]
keywords: [CTIFoundry, CVE, CWE, CAPEC, ATT&CK, CTIConnect]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/cemini-license-posture.md
  - entities/tools/ai-infra-guard.md
  - sources/eval-repository-revenue-2026-08-20.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — authorized-target CTI substrate; no PoC
- @concepts/cemini-license-posture.md — no CTIFoundry clone this batch
- @entities/tools/ai-infra-guard.md — same-day cyber REFERENCE
- @sources/eval-repository-revenue-2026-08-20.md — AI-Infra-Guard Extract

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.18613, "CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence" |
| Authors | Yutong Cheng, Changze Li, Qian Cui, Wei Ding, Lingzhi Wang, Yan Chen, Peng Gao (Virginia Tech / Amazon / Northwestern) |
| Retrieved | 2026-08-20 |
| File | `arxiv-2608.18613-ctifoundry-an-agent-native-corpus-scaffold-for-c.pdf` |
| sha256 | `5eb57b72669afd3cd3863fa34273e32d017eaa7a5344beee0541429b949ad1b4` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.18613-ctifoundry-an-agent-native-corpus-scaffold-for-c.pdf` |
| Dual-ID | **OSINT K243**. Cyber lab **authorized-target only**. No exploit PoC. |

## Narrative

CTIFoundry argues the bottleneck on agentic cyber-threat-intelligence investigation is the **corpus substrate**, not the harness. Threat reports are still packaged as opaque RAG chunks. The scaffold materializes typed structure at build time: a deterministic ontology over CVE / CWE / CAPEC / ATT&CK whose official cross-references become traversable edges; a span-grounded report layer with alias-resolved entities; hybrid dense+lexical retrieval. At query time that structure is seven typed tools plus three procedural skills (resolve before search; traverse official edges before text similarity; verify every candidate).

**Concrete claim `[TENTATIVE]`:** swapping only the action surface on mini-swe-agent lifts CTIConnect overall F1 from 0.610 to 0.829 (gpt-5.4) and 0.470 to 0.745 (claude-haiku-4-5). A small model on the scaffold beats a flagship on flat files, at roughly **half** the tool calls. Build-time validation claims zero fabricated identifiers. Cyber steal: typed ontology + span provenance for authorized lab investigations. Do not scrape criminal forums. Do not write exploit payloads.

## Snippets

> "a small model on CTIFoundry surpasses a flagship model on the flat substrate." [Source: arxiv-2608.18613 abstract]
