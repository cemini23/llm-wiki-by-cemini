---
title: "Cemini Multi-Wiki Link Evaluation Report — 44-Tool Audit (May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki, license-audit, ip-sale, adopt-tier, steal-from, ccc-wiki]
keywords: [tool evaluation, license audit, IP sale readiness, AGPL poison pill, cross-wiki routing, qstrader, garden-skills, octotools, gbrain, agent-skills, everything-claude-code, claude-code-karma, hetty, scientific-agent-skills]
related:
  - concepts/tool-evaluation-framework.md
  - concepts/ip-sale-readiness.md
  - entities/tools/qstrader.md
  - entities/tools/garden-skills.md
  - entities/tools/claude-code-karma.md
  - entities/tools/octotools.md
  - entities/tools/gbrain.md
  - entities/tools/agent-skills-addyosmani.md
  - entities/tools/everything-claude-code.md
  - entities/tools/hetty.md
  - entities/tools/scientific-agent-skills.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations
- @seo-wiki/briefs/2026-05-16_osint-audit-garden-skills-may-2026.md  (cross-wiki brief)
- @image-gen-wiki/briefs/2026-05-16_osint-audit-garden-skills-may-2026.md  (cross-wiki brief)
- @cybersecurity-wiki/briefs/2026-05-16_osint-audit-cross-routes-may-2026.md  (cross-wiki brief)
- @ccc-wiki/briefs/2026-05-16_osint-audit-cross-routes-may-2026.md  (cross-wiki brief)

- `@concepts/tool-evaluation-framework.md` — methodology this audit applies
- `@concepts/ip-sale-readiness.md` — IP-sale boundary enforced by the license checks
- `@entities/tools/qstrader.md` — Adopt: backtesting framework
- `@entities/tools/garden-skills.md` — Adopt: Claude Code skill collection
- `@entities/tools/claude-code-karma.md` — Adopt: session monitoring dashboard
- `@entities/tools/octotools.md` — Adopt: agentic reasoning framework
- `@entities/tools/gbrain.md` — Adopt: agent memory router
- `@entities/tools/agent-skills-addyosmani.md` — Adopt: engineering skills
- `@entities/tools/everything-claude-code.md` — Adopt: master agent harness
- `@entities/tools/hetty.md` — Steal-from: HTTP security toolkit
- `@entities/tools/scientific-agent-skills.md` — Steal-from: scientific agent skills

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation Report
- **Author**: Cemini internal (AI-generated under anti-hallucination protocol)
- **Type**: Internal tool evaluation document (.docx)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit.docx`
- **Retrieved**: 2026-05-16
- **Pages**: ~25 (evaluates 44 URLs)
- **Read status**: read

## Narrative

Systematic evaluation of 44 software repositories, threat intelligence reports, and developer resources against 7 Cemini wiki surfaces (Cemini financial, OSINT, Cybersecurity, Image-gen, SEO, 3D-printing, CCC). Each asset scored on license compliance, maturity signals, wiki fit, and cross-wiki routing potential. Operates under a strict anti-hallucination protocol: unavailable URLs are classified as such rather than synthesized.

### Tier distribution

| Tier | Count | Criteria |
|------|-------|----------|
| Adopt | 7 | MIT/Apache-2.0 license + strong wiki fit + mature |
| Steal-from | 2 | MIT license + extractable patterns without full integration |
| Reference-only | 4 | Informational value only; no code ingestion |
| Reject | 27 | No license (25), AGPL poison pill (2), NC clause (1), dead URL (3), or insufficient data |
| Unavailable | 4 | URL unreachable; no synthesis attempted |

### Adopt-tier (7 tools)

| Tool | License | Stars | Primary Wiki | Cross-route |
|------|---------|-------|-------------|-------------|
| mhallsmoore/qstrader | MIT | — | Cemini financial | OSINT |
| ConardLi/garden-skills | MIT | 4,900 | CCC | Image-gen, SEO |
| JayantDevkar/claude-code-karma | Apache-2.0 | 204 | CCC | OSINT |
| octotools/octotools | MIT | 1,400 | CCC | Cemini financial |
| garrytan/gbrain | MIT | 12,200 | CCC | OSINT |
| addyosmani/agent-skills | MIT | 41,300 | CCC | Cemini financial |
| affaan-m/everything-claude-code | MIT | 182,600 | CCC | Cemini financial, Cybersec |

### Steal-from-tier (2 tools)

| Tool | License | Stars | Primary Wiki |
|------|---------|-------|-------------|
| dstotijn/hetty | MIT | — | Cybersec |
| K-Dense-AI/scientific-agent-skills | MIT | 19,818 | CCC (OSINT cross-route) |

### License pattern summary

- **25 of 44** (57%) lack any detectable license — the dominant failure mode
- **3 poison-pill licenses** caught: boostsecurityio/smokedmeat (AGPL-3.0), c0m4r/kula (AGPL-3.0), datawhalechina/hello-agents (CC-BY-NC-SA-4.0)
- **10 clean MIT/Apache/BSD** licenses
- AGPL-3.0 is treated as a hard reject: network-accessible AGPL code triggers copyleft disclosure obligations incompatible with IP-sale readiness

### Primary-fit distribution

Cemini financial: 2 | OSINT: 6 | Cybersec: 15 | Image-gen: 0 | SEO: 1 | 3D-printing: 0 | CCC: 16 | None: 4

### Cross-wiki routing batch

The report mandates documentation stubs in secondary wikis:
- **Cemini financial**: octotools, addyosmani/agent-skills, everything-claude-code
- **OSINT**: Windows DNS CVE blog, qstrader, claude-code-karma, gbrain, scientific-agent-skills
- **Cybersec**: globalthreatmap, Master-OSINT-Toolkit, trickest/inventory, everything-claude-code
- **Image-gen**: garden-skills
- **SEO**: garden-skills
- **CCC**: trafexia, jadx-mcp-server, cronalytics
