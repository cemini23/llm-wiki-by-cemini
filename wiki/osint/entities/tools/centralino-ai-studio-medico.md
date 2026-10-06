---
title: "albeSavvy/centralino-ai-studio-medico — Italian telephony intent routing"
type: entity
tags: [tool, telephony, italian, intent-routing, atto, k283]
keywords: [centralino, telephony, italian, intent-classification, stato-civile, atto, comune, k283]
related:
  - sources/eval-bedrock-ecosystem-2026-10-06.md
  - concepts/k283-eval-wave.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-bedrock-ecosystem-2026-10-06.md — K283 eval (tier: Extract, route **Atto**)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @concepts/atto-genealogy-agent-kit.md — Atto agent kit

## Raw Concept

- **Repo:** `github.com/albeSavvy/centralino-ai-studio-medico`
- **Tier (K283):** **Extract** (route: Atto; `atto overlap 0.70`)
- **License:** NOT FOUND (docx)
- **Stack:** Python, FastAPI, telephony API (claimed)
- **Docx metadata:** NOT FOUND

## Narrative

An **Italian-language automated PBX switchboard** built for medical clinics. The domain is medical, but the core is a **voice + intent-routing pipeline in Italian**: linguistic parsing, intent classification, appointment/inquiry scheduling.

### Why it matters here

Atto Concierge cases (≥$2,500) involve **Italian municipal office follow-up** — *stato civile* / comune inquiries by phone. Italian intent classification and structured interaction logging could save 5–10 operator hours per case. Route: Atto brief.

### Boundary — privacy is the gate

**Client genealogical PII must never reach a third-party telephony model API without a human verification gate.** This is the highest-risk row in the K283 Bedrock batch because it touches live client contact. Extract the *intent-routing patterns*, not the telephony vendor integration.

## Snippets

> "Implements Italian linguistic parsing, intent classification, and appointment/inquiry scheduling patterns tailored for Italian administrative communication." [Source: eval-bedrock-ecosystem-2026-10-06.md]
