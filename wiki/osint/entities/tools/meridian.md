---
title: "Meridian — Claude Max Subscription Wrapper (NO-GO 2026-05-12: OAuth-grafting confirmed)"
type: entity
tags: [tool, claude-code-alternative, claude-max, k39, no-go, reject, family-c-tos-confirmed, no-license-file]
keywords: [meridian, claude max, oauth grafting, tos landmine, family-c, anthropic terms of service]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/9router.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: NO-GO 2026-05-12 — OAuth-grafting CONFIRMED via direct code audit + no-LICENSE-file
license_verified: NONE (badge claims MIT; LICENSE file absent; `gh api license.spdx_id` = null)
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

**NO-GO / REJECT 2026-05-12** — OAuth-grafting onto Claude Max credentials CONFIRMED via direct repo audit. K38 9router pattern repeat.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/rynfar/meridian` — 1,221★ / 145 forks / 26 open issues / last push 2026-05-11.

**License — RED**: `gh api repos/rynfar/meridian --jq '.license.spdx_id'` returns `null`. No LICENSE file in repo root despite README badge claiming MIT. **5th occurrence of no-LICENSE pattern** (after K36 finance-skills + K38 Readme.skill + K38 AI-Trader + K39 mac-code — see below).

**OAuth-grafting — CONFIRMED**:

1. `src/proxy/tokenRefresh.ts:30` reads `~/.claude/.credentials.json` directly (the file Claude Code's own auth subsystem writes after `claude login`). Also reads from macOS Keychain via `/usr/bin/security` with hardcoded service name `Claude Code-credentials` (line 29).
2. `src/proxy/tokenRefresh.ts:27` calls `https://platform.claude.com/v1/oauth/token` to perform the refresh **itself**, not via the SDK. `OAUTH_CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"` (line 28) is Claude Code's own OAuth client ID being reused. This is the textbook OAuth-grafting pattern.
3. `src/proxy/oauthUsage.ts:26-27` calls **private/undocumented** Anthropic endpoint `https://api.anthropic.com/api/oauth/usage` with `anthropic-beta: oauth-2025-04-20` header — exactly the kind of private endpoint that gets rate-limited or revoked when Anthropic notices third-party traffic.
4. README's load-bearing disclaimer ("No OAuth interception. No binary patches. No hacks. Just pure, documented SDK calls.") is **directly contradicted** by the code. SDK delegation is the marketing claim; OAuth credential reads + own refresh + private endpoint use is what ships.

**Family-C TOS landmine — CONFIRMED**. Mechanism is identical to K38 9router NO-GO pattern: third-party tool reuses Claude Max OAuth credentials from disk to drive non-Anthropic-blessed clients. Direct Anthropic ToS violation; Anthropic-credential revocation risk; IP-sale-readiness blocker.

**Cemini-coverage comparison**: Cemini already uses official Anthropic API + DeepSeek API via documented channels. Meridian provides nothing the existing stack lacks — only adds TOS risk + credential leak surface + npm-package single-dev (rynfar sole maintainer) supply-chain risk.

### Verdict

**NO-GO / REJECT — DEFER-INDEFINITELY**. Do not install. Activation trigger: only reconsider if (a) Anthropic publishes explicit endorsement of third-party OAuth-credential reuse (vanishingly unlikely; would moot the entire Max-subscription product), AND (b) repo adds clean LICENSE file. Both conditions must fire.

Adds to LESSONS.md mischaracterization catch-count as **7th catch** (after K28 SwarmVault + K30 PageIndex + K30 Claude-OSINT + K38 9router + K38 guild + K38 Readme.skill). Pattern: eval-brief frames OAuth-grafting as "Adopt — Workflow only" without auditing the actual auth flow.

[Source: Evaluating Project Links for Stacks.docx URL 11; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
