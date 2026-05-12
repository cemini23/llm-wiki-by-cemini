---
title: "Meridian — Claude Max Subscription Wrapper (RED-FLAG: Family-C TOS suspect)"
type: entity
tags: [tool, claude-code-alternative, claude-max, k39, adopt-tier-flagged, phase-0-pending, family-c-tos-suspect]
keywords: [meridian, claude max, oauth grafting, tos landmine, family-c, anthropic terms of service]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/9router.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: PENDING — high-suspicion Family-C TOS landmine pattern (cf. 9router NO-GO 2026-05-11)
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 11)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/mcp-tool-marketplace.md` — Family-C TOS-risk rubric applied
- `@entities/tools/9router.md` — K38 precedent NO-GO on same TOS landmine pattern (OAuth-grafting onto vendor credentials)

## Raw Concept

- **Repo / URL** (per source brief): `github.com/rynfar/meridian`
- **Tier (per source brief)**: **Adopt — Workflow only** (eval brief recommendation)
- **Tier downgrade pending**: **NEEDS Phase-0** before any laptop install
- **License** (per source brief): MIT
- **Stack**: Tool to "Use your Claude Max subscription with [coding agents]" — per eval brief description

## Narrative — RED FLAG

The eval-brief description "Use your Claude Max subscription with [another coding agent]" has the **exact signature** of the Family-C TOS landmine pattern that K38's 9router demonstrated (NO-GO 2026-05-11):

> 9router's "free unlimited" providers operate by OAuth-grafting onto third-party developer-tier auth — direct conflict with IP-sale-readiness license posture.

Meridian's mechanism is **likely** one of:
1. **OAuth-grafting** onto a Claude.ai web-tier or Claude Max subscription to drive third-party clients → direct Anthropic ToS violation, Anthropic-credential revocation risk
2. **Proxying** Claude Max API access for use outside the Claude Code / Anthropic-blessed clients
3. **Legitimate Anthropic-supported access pattern** (low-probability — Anthropic's official posture is that Claude Max is for personal use on official clients)

### Integration vector

**Adopt → HOLD pending Phase-0**. Do not install on laptop until Phase-0 confirms:
1. Auth mechanism (legitimate API key vs. session-token grafting vs. OAuth credential leak)
2. Anthropic ToS posture (Anthropic-endorsed vs. tolerated vs. ToS-violating)
3. License file presence
4. Single-dev bus-factor (rynfar is sole maintainer per eval brief)

If grafting is confirmed, **DOWNGRADE to NO-GO** and add to LESSONS.md mischaracterization catch-count (currently 6 catches across K28+K30+K36+K38).

### NEEDS VERIFICATION

- Authentication mechanism (API key, OAuth, session token)
- Anthropic ToS alignment
- LICENSE file presence in repo
- Star count, contributor count, recency

### Phase-0 audit status

**PENDING — HIGH PRIORITY**. This is the most TOS-suspicious tool in K39; verify before any other Phase-0 in this batch.

[Source: Evaluating Project Links for Stacks.docx URL 11; retrieved 2026-05-11]
