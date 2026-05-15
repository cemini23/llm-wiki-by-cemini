---
title: "Cemini Multi-Wiki Link Evaluation Report v3 (May 2026)"
type: source
tags: [tool-evaluation, phase-0-audit, multi-wiki, license-audit, adopt-stealfrom-reject, 2026]
keywords: [multi-wiki-tool-eval, 26-tool-batch, license-poison-pill, cross-wiki-routing, ip-sale-perimeter, adopt-6, steal-from-7, reject-6, unavailable-4]
related:
  - entities/tools/codegraph.md
  - entities/tools/visual-explainer.md
  - entities/tools/deepeval.md
  - entities/tools/voicebox.md
  - entities/tools/openusage.md
  - entities/tools/apktool-mcp-server.md
  - entities/tools/omnivoice.md
  - entities/tools/tpotce.md
  - entities/tools/myip.md
  - entities/tools/claude-code-agent-farm.md
  - entities/tools/decepticon.md
  - entities/tools/fusion.md
  - entities/tools/open-generative-ai.md
  - entities/tools/tracer.md
maturity: draft
read_status: deep-read
created: 2026-05-14
updated: 2026-05-14
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/codegraph.md — already cataloged; this eval confirms Adopt tier, CCC wiki primary fit
- @entities/tools/visual-explainer.md — Adopt, CCC wiki, MIT
- @entities/tools/deepeval.md — Adopt, OSINT wiki, Apache-2.0
- @entities/tools/voicebox.md — Adopt, Image-gen wiki, MIT
- @entities/tools/openusage.md — Adopt, CCC wiki, MIT
- @entities/tools/apktool-mcp-server.md — Adopt, Cybersec wiki, Apache-2.0
- @entities/tools/omnivoice.md — Adopt, Image-gen wiki, Apache-2.0
- @entities/tools/tpotce.md — Steal-from (GPL-3.0 poison pill), Cybersec wiki
- @entities/tools/myip.md — Steal-from, OSINT wiki, MIT
- @entities/tools/claude-code-agent-farm.md — Steal-from, CCC wiki, MIT
- @entities/tools/decepticon.md — Steal-from, Cybersec wiki, Apache-2.0
- @entities/tools/fusion.md — Steal-from, CCC wiki, MIT
- @entities/tools/open-generative-ai.md — Steal-from, Image-gen wiki, MIT
- @entities/tools/tracer.md — Steal-from, Cemini financial, MIT (highest-ROI extraction)

## Raw Concept

- **Title:** Cemini Multi-Wiki Link Evaluation Report (v3, May 2026)
- **Type:** Internal evaluation document (.docx)
- **Location:** `cemini-librarian:/opt/cemini-bulk/research/Multi-Wiki Tool Evaluation.docx`
- **Retrieved:** 2026-05-14
- **Scope:** 26 tools/repos evaluated across all 6 Cemini wikis + /opt/cemini financial stack

## Narrative

Batch architectural evaluation of 26 software repositories against Cemini operational perimeters: algorithmic trading stack compatibility, wiki fit, license posture relative to IP asset sale, and anti-hallucination protocols. Each tool receives a tier classification and cross-wiki routing directives.

### Tier summary

| Tier | Count | Tools |
|------|-------|-------|
| **Adopt** | 6 | visual-explainer, codegraph, deepeval, voicebox, openusage, apktool-mcp-server, OmniVoice |
| **Steal-from** | 7 | tpotce, MyIP, claude_code_agent_farm, Decepticon, Fusion, Open-Generative-AI, tracer |
| **Reference-only** | 3 | Stable-Diffusion (FurkanGozukara), Surge, red-run |
| **Reject** | 6 | minimalfirewall, Web-Fuzzing-Box, iii, ScottPlot, nowledge-mem, context-mode (unavailable subset) |
| **UNAVAILABLE** | 4 | geodro/lerd, outlierweekly.substack.com, mksglu/context-mode, hermes-agent PR#16219 |

### License risk pattern

- **Poison-pill licenses caught (5):** tpotce (GPL-3.0), minimalfirewall (AGPL-3.0), Stable-Diffusion (GPL-3.0), red-run (GPL-3.0), iii (Elastic License 2.0)
- **NO LICENSE FOUND (2):** Web-Fuzzing-Box, nowledge-mem — mandatory TENTATIVE Reject
- **Clean MIT/Apache/BSD (12):** all Adopt and Steal-from tools

### Primary-fit distribution

CCC wiki: 6 | Cybersec wiki: 4 | Image-gen wiki: 3 | OSINT wiki: 2 | Cemini financial: 1 | None: 6

### Cross-wiki routing directives

The report contains 17 cross-wiki routing directives — stubs and briefs to be created in secondary wikis where architectural concepts have applicability beyond the primary-fit wiki. See full text in `## Snippets` of the raw source for the complete routing table.

## Snippets

See full extracted text at `cemini-librarian:/opt/cemini-bulk/research/Multi-Wiki Tool Evaluation.docx`. Key routing directives reproduced in individual tool entity pages created from this source.
