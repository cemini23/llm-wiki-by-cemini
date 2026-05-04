---
title: MITRE ATLAS — Adversarial Threat Landscape for AI Systems
type: entity
tags: [security, taxonomy, mitre, ai-threats, llm-security, adopted-tier, cc-by-4-0]
keywords: [atlas, mitre, ai-security, prompt-injection, rag-security, threat-model, adversarial-ml, morris-ii-worm]
related:
  - sources/5-4-links-tool-eval.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/mitre-atlas-taxonomy.md
maturity: validated
created: 2026-05-04
updated: 2026-05-04
---

## Adoption status — concept page shipped 2026-05-04

`wiki/concepts/mitre-atlas-taxonomy.md` is the canonical Cemini-side synthesis of ATLAS v5.6.0. Per the K28 plan's Option C: single concept page + reference URLs (NOT a full mirror of all 200+ ATLAS objects, since atlas.mitre.org is the canonical live source).

The synthesis page covers:
- 16 tactics enumerated (1-line summaries each)
- 20 LLM/agent-relevant techniques (Cemini's primary threat surface)
- 11 LLM-relevant mitigations mapped to Cemini implementation loci
- 10 high-impact case studies (Morris II Worm, Bing Chat Data Pirate, Slack AI exfil, OpenClaw cases CS0048-CS0051, etc.)
- Implementation cross-walk: ATLAS techniques → Cemini codepaths
- Open follow-ups (technique classes lacking mapped defenses)

## License correction (vs K28 ingest)

K28 evaluator recorded ATLAS as "CC BY 4.0 + custom MITRE Terms of Use". Verified 2026-05-04:

- **atlas-data GitHub repo** (canonical data source): **Apache-2.0** (per `mitre-atlas/atlas-data/LICENSE`). Permissive — preserve copyright notice, state changes, attribute origin.
- **atlas.mitre.org website**: separate MITRE Terms of Use; the eval's CC BY 4.0 + verbatim attribution boilerplate applies when reproducing **website-presented** rendered content (case-study HTML, matrix views), NOT raw data feed.

License-posture concept page (`@concepts/cemini-license-posture.md`) updated to reflect this distinction. Refresh cadence and re-fetch instructions documented in the synthesis page's "Updating this page" footer.

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 8, **Adopt** tier verdict
- @concepts/wiki-tooling-evaluation.md — ATLAS taxonomy is canonical reference material to ingest into the wiki layer
- @concepts/cemini-license-posture.md — license: CC BY 4.0 + custom MITRE Terms of Use; safe for IP-sale with explicit attribution

## Raw Concept

MITRE's adversarial-threat-landscape framework specifically for AI-enabled systems. Modeled directly after MITRE ATT&CK; maps adversary tactics, techniques, and case studies against AI lifecycle stages (reconnaissance → data poisoning → model evasion → exfiltration). Identified as **Adopt-tier** in the 2026-05-04 Gemini DR eval — wiki-layer ingest as canonical security reference material.

## Narrative

- **URL**: https://atlas.mitre.org/
- **License**: CC BY 4.0 + custom MITRE Terms of Use
- **Scope**: 16 tactics × 170 techniques × 35 mitigations × 57 case studies (per Gemini DR)
- **Integration with NIST**: deeply integrated with NIST SP-800-53 security standards
- **Adoption signal**: actively used by 150+ organizations including federal agencies

### Why Adopt for the wiki layer

The taxonomy is high-density structured content that converts cleanly to interconnected markdown pages parseable by the librarian's MCP server. Provides:

1. **Standardized vocabulary** for any future LLM-agent security audit work in Cemini (input sanitization, prompt-injection resilience, RAG context injection)
2. **Concrete case studies** — including the Morris II Worm — that inform implementation of pre-call hooks in `services/llm_analyst/deepseek_client.py`
3. **No deployable code** to integrate; pure documentation, so no software-license complications

### Attribution requirement

Per MITRE Terms of Use, any wiki page derived from ATLAS material must include verbatim:

> "© 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation."

This is a hard requirement, not best-effort. Failure to attribute breaches the license.

### Practical use cases for Cemini

- **DeepSeek API pre-call hooks**: Morris II Worm case study illustrates RAG context-injection vectors → input sanitization at the Polars-pipeline → LLM boundary
- **MCP server hardening**: ATLAS techniques on "LLM Prompt Crafting" + "Gather RAG-Indexed Targets" inform the librarian server's MCP query surface design
- **Audit posture for IP-sale**: the K-series eval record + an ATLAS-grounded threat model = cleaner due-diligence story for an institutional acquirer

## Snippets

- **ATLAS scope** (Gemini DR eval): "16 tactics, 170 techniques, 35 mitigations, and 57 case studies, can be systematically parsed and synced into the Karpathy LLM Wiki pattern as a series of interconnected Markdown pages." [Source: 5_4 links.docx URL 8]

- **Morris II Worm relevance**: case studies "outlining the 'Morris II Worm' highlight the necessity of input sanitization to prevent RAG context injection, directly influencing how Polars pipelines feed data to the DeepSeek API." [Source: 5_4 links.docx URL 8]

- **Recommendation tier**: "Adopt (for the Wiki/Librarian server). Systematically ingest the ATLAS taxonomy into the markdown repository. The framework directly informs the strict security posture required for the production trading stack's LLM components and provides a standardized vocabulary for auditing AI vulnerabilities." [Source: 5_4 links.docx URL 8]
