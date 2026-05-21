---
title: "NOFX (NoFxAiOS/nofx) — agentic multi-market trading OS + Hackgate cautionary tale"
type: entity
tags: [entity, tool, agentic-trading, multi-market, polymarket, hyperliquid, agpl-3, cautionary, security-incident, slowmist, k56]
keywords: [nofxaios-nofx, agentic-trading-os, hackgate, slowmist-threat-intel-2025-11-17, zero-authentication, default-admin-mode, hardcoded-jwt-secrets, commit-517d0c-2025-10-31, ssrf-protection, usdc-pay-per-request, agpl-3-license]
related:
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - concepts/polymarket-bot-architecture.md
  - concepts/cemini-license-posture.md
  - concepts/cemini-deployment.md
  - concepts/cemini-ai-assistant.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
phase_0_verdict: REJECT — AGPL-3 (incompatible with Cemini IP-sale perimeter) + documented critical security incident (Hackgate, SlowMist 2025-11-17) demonstrating the failure mode that any AI-accelerated trading-stack development is at risk of
---

## Relations

- @sources/analyzing-github-projects-agentic-infra-2026-05-21.md — primary source (section "The Danger of Speed: Agentic Trading and the 'Hackgate' Incident")
- @concepts/polymarket-bot-architecture.md — NOFX is the cautionary case for any agent-driven Polymarket bot architecture
- @concepts/cemini-license-posture.md — AGPL-3 is incompatible with Cemini IP-sale; this entity reinforces the rejection criteria
- @concepts/cemini-deployment.md — operational counter-example for "what not to do" in production deployment
- @concepts/cemini-ai-assistant.md — Cemini AI assistant deliberately does NOT have unmediated trade execution; NOFX shows why

## Raw Concept

What prompted this page: K56 Analyzing GitHub Projects report — the "Hackgate" section. NOFX is positioned in the report as the theoretical zenith of AI integration in DeFi (agentic trading OS with AI Debate Arena consensus + autonomous execution); the SlowMist threat-intel disclosure of 2025-11-17 made it the textbook cautionary case.

- URL: `https://github.com/NoFxAiOS/nofx`
- License: **AGPL-3.0** (primarily)
- Stars / growth: ~9.2k in two months during late 2025 (viral dual-hype of AI + crypto)

## Narrative

**NOFX** (`NoFxAiOS/nofx`) is a self-hosted, multi-market agentic trading terminal. The architectural pitch: live market data → AI models (DeepSeek / GPT-4 / Qwen) → "AI Debate Arena" → consensus trade execution. Users fund a USDC wallet and pay per request, sidestepping API-subscription complexity.

NOFX's positioning sits at the intersection of Cemini's three current workstreams: (1) Polymarket execution (cemini-egress-fi relay), (2) Cemini AI assistant (cemini-egress-fi gateway), (3) directional / LP strategy code on cemini-prod. It is **what Cemini deliberately is not building** — a single binary that combines agent reasoning, model orchestration, and live trade execution behind a public-facing interface.

### Hackgate — the 2025-11-17 SlowMist disclosure

Timeline per the source report:

1. **2025-10-31** — Commit `517d0c` introduces "zero authentication" / "default admin mode" into core routing logic.
2. Operators deploy NOFX with default configs exposed to the public internet (the AGPL-3 + free distribution + viral growth combination made default-deployment the dominant operational pattern).
3. **2025-11-17** — SlowMist publishes a threat-intel report documenting that unauthenticated remote attackers can bypass all protected API routes.
4. The vulnerability is critical because NOFX interfaces directly with:
   - **Centralized Exchanges (CEX)** via highly privileged API keys
   - **Perpetual Decentralized Exchanges (Perp-DEX, e.g., Hyperliquid)** via **raw private wallets**
5. NOFX maintainers attempt to patch by introducing Authorization headers.
6. SlowMist identifies that **hardcoded JWT secrets remain embedded in the codebase** — attackers forge valid administrative tokens and bypass the patch.
7. Recent commits add SSRF (Server-Side Request Forgery) protection for user-controlled URLs and remove deprecated payment providers (continued security-debt remediation).

The financial-exposure consequence: attackers gained unauthenticated access to operator API keys and private wallets, with no way to invalidate the JWT secret without a full codebase + key rotation.

### Why this matters for Cemini

The Hackgate failure mode is **exactly what an AI coding agent would emit by default** if not explicitly instructed otherwise:

- "Zero auth in dev, add auth later" → forgotten and shipped (typical sprint pressure)
- Hardcoded JWT secret in the codebase → AI agents routinely emit example secrets unless explicitly required to use env vars / KMS
- AGPL-3 distribution + viral growth → operators inherit the default config without security review

Cemini's three architectural decisions directly counter this:

1. **cemini-egress-fi gateway is NOT publicly exposed** — bound to `127.0.0.1:8088`, accessed only via SSH tunnel from cemini-prod or laptop. The Cemini AI Phase-3 prod-UI brief (`briefs/2026-05-20_cemini-ai-prod-ui-integration.md`) has a **Step-0 HARD GATE**: server-Claude must verify the Streamlit UI sits behind Cloudflare Access before any wiring code is touched. If the UI is open-public, HALT.
2. **No hardcoded secrets in any Cemini service** — all keys via `.env` files or environment variables, never committed.
3. **Cemini AI assistant does NOT execute trades unmediated** — it can emit `proposed_action` payloads (confirm-card pattern, Phase-3 not yet live), but humans are in the loop. NOFX's "AI Debate Arena → autonomous execution" is the architecture Cemini specifically rejected.

### License posture

AGPL-3.0 is **incompatible with the Cemini IP-sale perimeter** (per @concepts/cemini-license-posture.md). NOFX cannot be vendored or forked into Cemini even if the security issues were resolved. This is independent of the Hackgate verdict — NOFX would be a NO-GO on license alone.

### Phase-0 verdict

**REJECT.** Two independent disqualifying factors:
1. License (AGPL-3.0 vs IP-sale perimeter)
2. Documented critical security incident (Hackgate, SlowMist 2025-11-17), patch-failure (hardcoded JWT secrets), and ongoing security-debt remediation

The entity is retained for **cautionary value only** — the failure mode is instructive.

## Dead Ends

- The SlowMist threat-intel post on Medium is cited but not pulled into our wiki. Recommended follow-up: `mcp__exa__crawling_exa` against `https://slowmist.medium.com/threat-intelligence-analysis-of-the-nofx-ai-automated-trading-vulnerability-e4f4664ad1e6` to extract the full technical writeup into `## Snippets`. The OneKey ecosystem article (`https://onekey.so/blog/...`) provides additional ecosystem-impact framing.

## Snippets

> "By deploying the software with default configurations exposed to the public internet, operators unknowingly allowed unauthenticated remote attackers to bypass protected API routes entirely."
> [Source: Analyzing GitHub Projects report, Hackgate section — citing SlowMist 2025-11-17]

> "Even after initial, frantic attempts by the NOFX maintainers to patch the software by introducing Authorization headers, the SlowMist team identified that hard-coded JSON Web Token (JWT) secrets remained embedded in the codebase. This rendered the authentication fix completely useless, as attackers could simply forge valid administrative tokens."
> [Source: Analyzing GitHub Projects report, Hackgate section]

> "When the speed of AI-assisted development outpaces fundamental security governance, the resulting financial exposure is immediate, severe, and highly public."
> [Source: Analyzing GitHub Projects report, Hackgate conclusion]
