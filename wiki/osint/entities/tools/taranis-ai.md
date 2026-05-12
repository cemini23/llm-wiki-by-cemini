---
title: "taranis-ai — OSINT Threat Intelligence (EUPL-1.2 REJECT)"
type: entity
tags: [tool, osint, threat-intelligence, eupl-1.2, license-reject, k39, reject-tier]
keywords: [taranis-ai, threat intelligence, EUPL-1.2, copyleft, ip-sale-poison-pill, hardware-overcap]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 5)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — **EUPL-1.2 added to license blocker catalog this batch**

## Raw Concept

- **Repo / URL** (per source brief): `github.com/taranis-ai/taranis-ai`
- **Tier (per source brief)**: **Reject** — comprehensive license + hardware veto
- **License** (per source brief): **EUPL-1.2 (European Union Public Licence)**

## Narrative

OSINT-focused threat-intelligence platform. Eval brief rejects on two compounding grounds:

### Why reject — license

EUPL-1.2 is a **strong copyleft** with explicit network-distribution / SaaS clauses (Article 14.3 + the EUPL's treatment of "linking and embedding"). For Cemini's IP-sale-readiness posture, EUPL-1.2 is functionally equivalent to AGPL-3.0: any remote-network access to a derivative work triggers source-disclosure obligations on the entire combined work. **Poison pill** for institutional acquisition.

### Why reject — hardware

Eval brief documents 16 GB minimum hardware envelope. Hetzner CPX21 (4 GB) and CPX31 (7 GB) both fall short by a factor of 2-4×. Even if license were clean, deployment is hardware-impossible.

### Integration vector

**Reject** — no Adopt / Steal-from / Reference-only carve-out. Architecture is too tightly coupled to PostgreSQL-on-large-host + Celery + Bootstrap admin UI; not a useful reference pattern for Cemini's quant-trading-specific OSINT needs.

### License catalog impact

**Catalog entry to add to `@concepts/cemini-license-posture.md`**: EUPL-1.2 — hard reject. Reasoning: network-distribution / SaaS clause triggers source-disclosure on remote access; equivalent to AGPL-3.0 for our purposes.

[Source: Evaluating Project Links for Stacks.docx URL 5; retrieved 2026-05-11]
