---
title: K293 ccc wave — skills, evidence, and coordination (Oct 2026)
type: concept
related:
  - sources/arxiv-2610-23599-cdse-skill-differentiation.md
  - sources/arxiv-2610-26836-evidence-substitution.md
  - sources/arxiv-2610-23804-jarvis-coordination.md
  - sources/arxiv-2610-22292-catch-honesty.md
  - sources/arxiv-2610-26211-legal-overrefusal-small-llms.md
  - sources/arxiv-2610-23791-drugharness.md
  - sources/arxiv-2610-23839-discoveryrsi.md
  - concepts/evidence-substitution-retrieved-tool-output.md
maturity: draft
updated: 2026-10-20
---

## Raw Concept

CCC K293, 2026-10-20. Seven harness papers routed out of the osint, seo, and game-dev inboxes. No install. No clone. No `/route` swap.

## Narrative

Three harness facts are worth keeping.

1. **Name the file that is allowed to answer.** When a long tool report stays out of context, GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 points because they answer from a different file. Claude shows no detectable cost. @concepts/evidence-substitution-retrieved-tool-output.md
2. **Split a skill by job, then update each part.** CDSE (Meta, Experience, Tool, Script) wins all 36 settings, +7.6 points over the base agent. @sources/arxiv-2610-23599-cdse-skill-differentiation.md
3. **Give coordination its own model.** Jarvis, with the front model and the back end held fixed, raises a voice-task success count from 29 to 192 of 278. @sources/arxiv-2610-23804-jarvis-coordination.md

The other four are method notes. CATCH trains honesty on a few hundred self-report targets and keeps utility better than activation steering. @sources/arxiv-2610-22292-catch-honesty.md Small on-prem models refuse benign legal prompts 2–20× more often after an "I am a lawyer" prefix. @sources/arxiv-2610-26211-legal-overrefusal-small-llms.md DrugHarness and DiscoveryRSI are skill-evolution loops. This wiki records the loop and does not record the chemistry or the assays. @sources/arxiv-2610-23791-drugharness.md @sources/arxiv-2610-23839-discoveryrsi.md
