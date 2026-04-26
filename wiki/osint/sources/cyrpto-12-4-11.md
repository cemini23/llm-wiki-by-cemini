---
title: "Crypto-Agility Inventories via Collaborative LLMs (PQC readiness)"
type: source
tags: [pdf, llm-agents, portfolio-strategy, audit-security]
clusters: [llm-agents, portfolio-strategy, audit-security]
related:
  - concepts/llm-agent-systems.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- Original title: Building Crypto-Agility Inventories with Collaborative LLMs (inferred from extract)
- Authors: Hirsch et al.
- Affiliation: OTH (Ostbayerische Technische Hochschule) + Fraunhofer AISEC
- Type: PDF, research paper
- Location: research for cemini/cyrpto 12 4:11.pdf
- Length: ~20 pages
- Retrieved: 2026-04-23
- Publication date: 2025
- Read status: deep-read
- Primary cluster: audit-security
- All clusters: llm-agents, portfolio-strategy, audit-security
- Flag: *"portfolio-strategy" in cluster list is a misnomer — this is software/crypto portfolio inventory, not financial portfolio strategy.*

## Narrative

Hirsch et al. use a collaborative-LLM pipeline to generate crypto-agility inventories for large software estates. The goal is preparing organizations for post-quantum cryptography (PQC) migration by first cataloguing every cryptographic primitive in use (RSA, ECDSA, AES-GCM, etc.) across their codebase. A multi-LLM agent system reads source code, config files, and binary strings, cross-checks findings across LLMs for agreement, and produces a per-package crypto inventory with confidence scores. Evaluated on **65,000 Fedora packages**; the pipeline is shown to be materially more thorough than static regex-based crypto detectors and captures primitives hidden in configs or wrapper libraries.

The empirical scale is the main contribution — 65K packages is large enough to test the pipeline's precision/recall on a realistic distribution, and the authors report the collaborative step (cross-LLM agreement) as the key driver of precision. Fraunhofer AISEC affiliation gives strong security-research credibility.

For Cemini: directly relevant if PQC readiness becomes an IP-sale due-diligence item. The pipeline pattern (collaborative LLM agents for codebase inventory + confidence scoring) is reusable for any codebase audit task — crypto inventory, dependency inventory, secret inventory. The specific PQC focus is narrow, but the architectural pattern generalizes.

## Key findings

- Collaborative multi-LLM pipeline for crypto-agility inventory across software estates.
- Evaluated on **65,000 Fedora packages**; outperforms regex-based detectors.
- Cross-LLM agreement step is the key precision driver.
- Fraunhofer AISEC affiliation; solid security-research provenance.
- Architectural pattern (collaborative LLMs + confidence scoring) generalizes beyond crypto to any codebase audit.

## Snippets

- **abstract** — "We use collaborative LLMs to generate crypto-agility inventories at scale" — the contribution.
- **empirical** — "Evaluated on 65,000 Fedora packages" — scale figure.
- **method** — Cross-LLM agreement gates the final inventory, boosting precision over single-LLM baselines.
