---
title: "tl;dr sec #342 — Figma agentic detection, Uber ADR, 1Password SPIFFE, Cloudflare AAM"
type: source
tags: [cyber, soc, agent-identity, detection, blue-team]
keywords: [Figma, Panther, Uber-ADR, SPIFFE, JWT-SVID, Cloudflare-AAM, CosmosEscape, Brockman]
related:
  - concepts/agent-runtime-identity-adr.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/inadvertent-context-leakage.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/agent-runtime-identity-adr.md
- @concepts/agent-safety-executable-evaluation.md
- @concepts/inadvertent-context-leakage.md

## Raw Concept
- **title:** [tl;dr sec] #342 - Figma's Agentic Detection, Agent Identity, Uber's Agent-(E)DR
- **author:** tl;dr sec (issue roundup; primary writeups Figma / Uber / 1Password / Cloudflare / Wiz / Brockman)
- **type:** newsletter
- **location:** research to be indexed/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342---figmas-agentic-detection-agent-id.md
- **retrieved:** 2026-08-20
- **pages:** full issue (AppSec, Cloud, Blue Team, AI+Security)
- **read-status:** skimmed

## Narrative
Issue to page for cyber wiki: agent identity + agent-(E)DR + tool-layer safety. Skip ads, DEF CON filler, QM/autoharness (point those at CCC, do not duplicate a harness page here).

**Figma / Panther.** Agentic detection investigates alerts across AWS/Okta/GitHub/GCP/osquery, opens draft PRs. ~70% faster TTR on complex alerts; ~20% fewer pages via severity downgrade. Three memories: case RAG, steering markdown, procedural schema. **Safety at the tool layer, not the prompt**; PRs default draft; channel-aware prompts so public Slack does not get secrets.

**Uber ADR.** Agent telemetry sensor (prompts, MCP, traces, tools, execution context) + two-tier detector (creds, injection, exfil, policy-violating tools). ADR-Bench: 300+ tasks, 17 techniques, 133 MCP servers. Code + paper out. This is the agent-(E)DR pattern.

**1Password local-agent identity.** OS code-sign → SPIFFE JWT-SVIDs from Secure Enclave/TPM; OAuth token exchange with `sub=human` / `act=agent`; transaction tokens vs prompt injection; no standing secrets on disk.

**Cloudflare Agent Access Model.** Identity broker, task-scoped access, mediation layer, irreversible Trust Ratchet, activity log, grant review. Multiplayer (one agent, many principals) still unsolved.

**Wiz CosmosEscape.** Gremlin sandbox bypass via .NET reflection on Cosmos DB Gateway → platform-wide Cosmos Master Key → any tenant primary key + Config Store enum. Microsoft hotfixed in 48h and removed the master key. Awareness, not a clone.

**Brockman Defender’s Window.** Codex security plugin, alert triage, attack-path enumeration, 10-step defender playbook; urgency before open-weight peers. Policy posture, not a procedure dump.

Pairs with SecPro #248 (foundations) and Fairoze leakage (outputs as channels).

## Snippets
> Three memory layers (case memory as the RAG corpus of historical alerts, steering memory as behavioral guidance in markdown, procedural memory as self-learned database schemas) … safety controls sit at the tool layer rather than in prompt instructions, with agent-authored PRs defaulting to draft. [Source: https://tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-20)]

> Uber ADR … pairs an observability sensor that captures agent telemetry (prompts, MCP activity, reasoning traces, tool calls, execution context) with a two-tier detector … ADR-Bench across 300+ tasks covering 17 agent attack techniques and 133 MCP servers. [Source: https://tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-20)]

> A trusted local app … minting short-lived SPIFFE JWT-SVIDs … OAuth 2.0 Token Exchange for delegated tokens carrying sub (human) and act (agent) claims. [Source: https://tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-20)]
