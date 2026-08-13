---
title: ppt-master — AI-native PowerPoint generation engine
type: entity
tags: [entity, tool, pptx, atto, mit, k235, presentation]
keywords: [ppt-master, DrawingML, native-charts, Edge-TTS, narration, genealgy-decks]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Integrate (Atto)
- @concepts/cemini-license-posture.md — verified-MIT precedent vs docx claims

## Raw Concept

Repo `hugohe3/ppt-master` (~46.3k★). First surfaced in K235 20-URL eval as the Atto concierge-deck generator (natively editable .pptx with real DrawingML shapes, native charts, transitions, Edge TTS narration). Phase-0 this session: **MIT verified** via gh api + LICENSE file (docx claimed MIT — confirmed); but shallow clone = **1.3 GB** (examples/ 581M dominates).

## Narrative

**Verdict: CONDITIONAL-GO Integrate (Atto).** License clean; size fails the 500 MB `.local/adopts/` vendoring threshold — adopt via **sparse checkout of `skills/ppt-master/` + requirements.txt**, never a full clone. Value: removes the manual-design bottleneck in the ≥$2.5k concierge tier by generating editable decks from M1–M14 extraction outputs (family-tree JSON → client-ready presentation).

Constraints (policy-wired):
- **PII boundary**: narration/design via external AI APIs (Edge TTS cloud, LLM providers) requires prompt routing + data masking per Atto's share perimeter; no client PII to unvetted endpoints.
- **Fidelity unverified**: SVG→native mapping on macOS vs Windows needs a smoke test before any pipeline commit (docx NEEDS VERIFICATION carried forward).
- HITL before wiring into Atto pipeline — proposal via /phase1.

[Source: hugohe3/ppt-master (retrieved 2026-08-13); Deep Research URL Evaluation.docx]
