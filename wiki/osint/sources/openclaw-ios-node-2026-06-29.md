---
title: "OpenClaw official iOS node app (2026-06-29)"
type: source
tags: [source, openclaw, ios, mobile, agent-harness, k135]
keywords: [openclaw-ios, mobile-node, gateway-pairing, app-attest, push-relay, app-store]
related:
  - entities/tools/openclaw.md
  - concepts/openclaw-security-taxonomy.md
  - sources/eval-github-batch-unusualwhales-2026-06-28.md
  - entities/tools/hermes-agent.md
  - concepts/llm-agent-systems.md
  - concepts/reasoning-safety-monitor.md
  - concepts/sae-execution-contract.md
  - entities/tools/clawdbot.md
  - sources/3-17-agent-research.md
  - sources/4-3-link-re-2.md
  - sources/crypto-7-4-11.md
  - sources/ai-2-4-3.md
maturity: draft
read_status: read
created: 2026-06-29
updated: 2026-06-29
clusters: [agent-harness, mobile, security]
---

## Relations

- @entities/tools/openclaw.md — entity synthesis + Cemini posture
- @concepts/openclaw-security-taxonomy.md — gateway threat model; iOS node mitigations
- @sources/eval-github-batch-unusualwhales-2026-06-28.md — K133 DM pairing steal

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | OpenClaw official iOS / Android companion apps |
| **Author** | OpenClaw Foundation (Peter Steinberger origin; foundation governance post-Feb 2026) |
| **Type** | First-party App Store / Google Play release + monorepo `apps/ios` |
| **Retrieved** | 2026-06-29 |
| **Read status** | read (official docs + press + GitHub license spot-check) |
| **Primary URLs** | [docs.openclaw.ai/platforms/ios](https://docs.openclaw.ai/platforms/ios) · [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |

## Narrative

**2026-06-29:** OpenClaw shipped **first-party mobile companion apps** (iOS App Store + Android Google Play). The phone app is a **node**, not a hosted assistant — it pairs to a **self-hosted Gateway** on Mac/Linux/Windows (WSL2) over WebSocket (LAN Bonjour, Tailscale DNS-SD, or manual host:port default **18789**).

### Architecture (node vs gateway)

| Role | Runs where | Powers |
|------|------------|--------|
| **Gateway** | User's Mac/PC/VPS | LLM routing, channels (Telegram/WhatsApp/etc.), tools, exec policy |
| **iOS node** | iPhone/iPad | Chat UI, **action approvals**, Talk/voice, opt-in camera/location/photos/canvas |

Agents invoke phone capabilities via `node.invoke` (`canvas.*`, `camera.*`, `screen.*`, `location.*`, `talk.*`) — subject to iOS foreground limits. **Not** Codex Computer Use / desktop MCP control.

### Security improvements vs early-2026 OpenClaw panic

Official docs and release engineering add **mobile-specific controls** that partially address K20 structural conditions:

1. **Manual device pairing by default** — `openclaw devices approve <requestId>` on gateway; auto-approve only via explicit CIDR opt-in.
2. **Relay-backed push (official builds)** — App Attest + StoreKit transaction JWS; hosted relay at `ios-push-relay.openclaw.ai`; **raw APNs token not stored on gateway**; relay registration **delegated to paired gateway identity** (cross-gateway push blocked).
3. **Per-capability opt-in** on device (camera, location, contacts, etc.).
4. **Reduced blast radius** — compromised node ≠ full gateway RCE; gateway still holds exec/tool surface (K20 layers 4–7 remain relevant on host).
5. **Apple distribution proof** — hosted relay rejects unsigned/local Xcode builds; limits drive-by relay abuse.

**Residual risks [CONFIRMED from prior corpus + press]:** prompt injection on gateway, malicious skills marketplace, broad host permissions if gateway runs on primary machine. MacRumors/9to5Mac repeat injection + permission warnings. **Third-party** "OpenClaw" store clones exist — use **first-party** build only [TENTATIVE].

### Cemini posture shift (2026-06-29)

| Surface | Prior (K14/K17) | Updated |
|---------|-----------------|---------|
| **cemini-prod / Lane A executor** | NO-GO | **NO-GO** — unchanged |
| **IP-sale trading gateway** | NO-GO | **NO-GO** — proprietary data + plugin supply chain |
| **Laptop operator: personal gateway + iOS approvals** | Rejected wholesale | **CONDITIONAL-GO** — pairing gates, no prod secrets on gateway, steal DM/pairing patterns |
| **Threat-model reference (K20)** | Core taxonomy | **Still core** — applies to gateway; iOS node adds inter-layer controls |

License: **MIT** (LICENSE file on `openclaw/openclaw`; GitHub API metadata shows NOASSERTION — verify file, not API).

## Snippets

> "The iOS app is a mobile node surface, not a Codex Computer Use backend." [Source: https://docs.openclaw.ai/platforms/ios (retrieved 2026-06-29)]

> "Only genuine OpenClaw iOS builds distributed through Apple can use the hosted relay. A gateway can send relay-backed pushes only for iOS devices that paired with that specific gateway." [Source: https://docs.openclaw.ai/platforms/ios — Authentication and trust flow (retrieved 2026-06-29)]

> "OpenClaw for iOS can be used alongside an existing gateway as a secure node for chat, voice approvals, sharing, and device-aware automation." [Source: MacRumors 2026-06-29 — https://www.macrumors.com/2026/06/29/openclaw-ios-app/]

## Dead Ends

- Treating iOS node as **standalone** assistant without gateway — wrong product shape; not Cemini-relevant.
- Replacing **Hermes** or **Conductor** with OpenClaw on prod — still out of scope; Hermes comparison remains valid (@entities/tools/hermes-agent.md).
