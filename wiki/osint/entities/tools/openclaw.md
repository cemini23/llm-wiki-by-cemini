---
title: OpenClaw — personal AI gateway + mobile nodes
type: entity
tags: [entity, tool, agent-runtime, open-source, mobile, k135]
keywords: [openclaw, clawdbot, moltbot, gateway, ios-node, mit, foundation]
related:
  - sources/openclaw-ios-node-2026-06-29.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/hermes-agent.md
  - entities/tools/clawdbot.md
  - sources/3-17-agent-research.md
  - sources/4-3-link-re-2.md
  - sources/ai-2-4-3.md
  - sources/eval-github-batch-unusualwhales-2026-06-28.md
  - entities/tools/claw-swe-bench.md
  - concepts/llm-agent-systems.md
  - concepts/sae-execution-contract.md
  - concepts/reasoning-safety-monitor.md
  - sources/crypto-7-4-11.md
maturity: draft
created: 2026-06-29
updated: 2026-06-29
---

## Relations

- @sources/openclaw-ios-node-2026-06-29.md — K135 iOS/Android first-party apps (2026-06-29)
- @concepts/openclaw-security-taxonomy.md — K20 threat model (gateway-focused)
- @entities/tools/hermes-agent.md — positioned successor; OpenClaw still wider channel coverage
- @entities/tools/clawdbot.md — K55 name-collision stub (ColdMath "Clawdbot" may = this project)
- @sources/3-17-agent-research.md — Tier C prod rejection (K16); K135 Tier A carve-out
- @sources/ai-2-4-3.md — 190-advisory taxonomy source

## Raw Concept

What prompted this page: **2026-06-29** first-party **OpenClaw iOS/Android** companion apps + operator request to **re-open** evaluation — open-source (MIT), materially safer mobile pairing/push design, but gateway risks from K14/K20 remain on the host.

## Narrative

**Repository:** [openclaw/openclaw](https://github.com/openclaw/openclaw) — self-hosted personal AI assistant (Gateway control plane + channel integrations). Origin: Clawdbot → Moltbot → OpenClaw; creator Peter Steinberger joined OpenAI **2026-02-14**; project transferred to **OpenClaw Foundation** (community maintainers). ~381k★ (2026-06-29).

**License (Phase-0):** **MIT** — LICENSE file on main; `gh api` returns NOASSERTION (ignore API; read file).

### Product shape

```
[iPhone iOS node] <--WS pairing--> [Gateway on Mac/PC] <--tools/channels--> [LLM APIs + messaging apps]
```

- **Gateway** — exec policy, plugins/skills, WebSocket API (port 18789 default), channel bridges.
- **Mobile node** — chat, push approvals, Talk mode, opt-in device sensors; `openclaw nodes invoke` from gateway CLI.

Android + iOS first-party store apps announced **2026-06-29**; iOS docs: App Attest relay, manual pairing, Bonjour/Tailscale discovery.

### Cemini posture (2026-06-29 revision)

| Tier | Verdict | Scope |
|------|---------|-------|
| **A — Mobile node + personal laptop gateway** | **CONDITIONAL-GO** | Operator-only: approvals on phone, no cemini-prod secrets, gateway on isolated user account; steal pairing/relay patterns |
| **B — Research reference** | **REFERENCE** | K20 taxonomy + Claw-SWE-Bench harness eval (@entities/tools/claw-swe-bench.md) |
| **C — Prod trading / IP-sale stack** | **NO-GO** | K17: plugin supply chain + prompt injection + host exec — disqualifier unchanged |

**CONDITIONAL-GO gates (Tier A):**

1. Gateway **not** on cemini-prod or machine with trading keys / wiki prod tunnels.
2. **Manual** `openclaw devices approve` — no auto-approve CIDR unless lab-only.
3. **First-party** App Store / Play build only (avoid clone apps).
4. Skills/plugins: curated allowlist; no marketplace drag-and-drop on gateway handling sensitive repos.
5. Steal **DM/pairing allowlist** pattern for TipDrop/webhook bridges (@sources/eval-github-batch-unusualwhales-2026-06-28.md K133).

**Not a Hermes replacement** for Cemini — Hermes ships self-improving skills + bounded memory without full OpenClaw host surface (@entities/tools/hermes-agent.md).

### vs prior rejection (K14/K17)

Early corpus rejected OpenClaw for **IP-sale trading integration** (malicious plugins, centralized trust broker). That rejection stands for **Tier C**. Tier A acknowledges **architectural separation**: iOS node hardening (relay attestation, pairing approval, capability opt-in) reduces mobile-specific risk without clearing gateway-layer K20 advisories.

## Snippets

> "Integrating OpenClaw into an algorithmic trading suite handling proprietary financial data is an immediate disqualifier for an IP sale." [Source: sources/3-17-agent-research.md — retained for Tier C]

> "Pair with your private OpenClaw Gateway by QR code or setup code … Review Gateway action approvals from your iPhone." [Source: App Store description via MacRumors 2026-06-29]

## Dead Ends

- **Full gateway on Hetzner prod** — still NO-GO; use prod MCP + Conductor patterns instead.
- **OpenClaw as cemini_decide / poker sandbox runtime** — wrong fit; use Arena starter kit + verifier harness.
