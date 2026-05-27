---
title: cemini-egress-fi — Finnish order-routing relay (Hetzner Helsinki)
type: entity
tags: [infrastructure, hetzner, polymarket, hyperliquid, order-routing, proxy, cemini-deployment]
keywords: [cemini-egress-fi, helsinki, hel1, finland, ssh-tunnel, order-egress, geo-routing, non-us-egress, third-server]
related:
  - concepts/cemini-ai-assistant.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
  - sources/arxiv-inference-scaling-llms-2605.19775.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - concepts/laptop-prod-research-split.md
  - entities/tools/camofox-browser.md
  - entities/tools/hl-funding-sniper.md
maturity: draft
created: 2026-05-19
updated: 2026-05-27
# Live-probed 2026-05-20 (read-only SSH via cemini-prod jump host). Refresh on spec/role change.
---

## Relations

- @concepts/cemini-ai-assistant.md — candidate host for the Cemini AI assistant gateway during its internal-only phase (this box has the headroom)
- @entities/infrastructure/cemini-stack.md — the umbrella production topology; this is the third Hetzner server (added 2026-05-19, swapped DC 2026-05-20)
- @concepts/librarian-server-architecture.md — the librarian (kb-server + stash) this box would query if it hosts Cemini AI; both are Hetzner, different DCs (Helsinki vs Ashburn)
- @sources/arxiv-inference-scaling-llms-2605.19775.md — K48: long chain-of-thought reasoning is KV **capacity-bound**; this host (4 GB, no GPU) is **API-gateway-only** for frontier reasoning — do not install local CoT weights here
- @concepts/polymarket-copy-trading-strategy.md — K57: hybrid Polymarket CLOB copy latency; gateway must not promise sub-block parity
- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — @spottr_trade Post 7 (0-block vs detection)
- @entities/tools/camofox-browser.md — K71: camofox is laptop-only; not deployed on egress-fi
- @entities/tools/hl-funding-sniper.md — K72: **no** funding bot on egress; HL orders stay prod EMS + `HYPERLIQUID_PROXY`

## Raw Concept

The third Hetzner server in the Cemini fleet — the egress relay through which Polymarket and Hyperliquid orders route. Originally provisioned at Hetzner Falkenstein (Germany, hostname `cemini-poly-proxy`) and surfaced 2026-05-19; **rebuilt at Hetzner Helsinki (Finland, hostname `cemini-egress-fi`) on 2026-05-20** after the user verified both venues accept egress from Finland. The role and operational pattern carry over unchanged; only the datacentre and hostname differ.

Probed read-only 2026-05-20 — SSH via `cemini-prod` as jump host (the box's port 22 is firewalled to the Hetzner fleet, not the open internet).

## Narrative

### What it is

| Field | Value |
|---|---|
| Hostname | `cemini-egress-fi` |
| Provider / location | Hetzner Cloud, **Helsinki (HEL1), Finland** |
| Public IP / SSH access | see `.local/server.md` (jump host required; `cemini-egress-fi` SSH alias) |
| Spec | 2 vCPU · 4 GB RAM (3.7 GiB measured) · 75 GB disk · Ubuntu (kernel 6.8.0-117) |
| Utilisation (2026-05-20) | 428 MB RAM used · 1.5 GB disk used · load average 0.00 |
| Headroom | ~3.3 GB RAM free · ~71 GB disk free |
| Running (2026-05-22) | `sshd` + **Cemini AI** gateway under `/opt/cemini-ai/` — no Docker, no WireGuard, no separate proxy daemon |
| AS / rDNS | AS24940 Hetzner Online GmbH · `static.190.139.168.204.clients.your-server.de` |

### Role — order-egress relay

`cemini-egress-fi` exists so that Polymarket and Hyperliquid order traffic egresses from a **Finnish IP** rather than the Ashburn production IP. Polymarket enforces geo-blocking on order submission (`POST /order` returns HTTP 403 from US IPs; market-data reads are unrestricted — profiled 2026-05-18). Finland was chosen over the previous Germany location after the user confirmed **both venues accept Helsinki egress** (PM **and** HL); the Falkenstein box only had to cover PM, so picking a country that clears both consolidates two routing paths onto one relay.

The routing mechanism is lightweight: there is **no WireGuard and no proxy process listening**. The relay is plain **SSH tunnelling** — `cemini-prod` opens an `ssh -D`/`-L` tunnel *through* this box so order calls exit with the Finnish IP. `sshd` on `:22` is the entire serving surface, which is why the box sits at load 0.00.

This supersedes (a) the abandoned server-side WireGuard on `cemini-prod` (dropped as fragile, see `hot.md`), (b) the laptop-side `polymarket_proxy.py` forward-tunnel (a validation harness that violated the deployment boundary), and (c) the now-decommissioned Falkenstein predecessor (`cemini-poly-proxy`; see Dead Ends).

### Relationship to the rest of the fleet

It is the **third** Hetzner server, joining `cemini-prod` (Ashburn, trading stack) and `cemini-librarian` (Ashburn, knowledge serving). Unlike those two it is in a different datacentre — Helsinki, not Ashburn — a deliberate consequence of needing a non-US egress IP. Helsinki-to-Ashburn is a transatlantic hop of **~118–120 ms RTT** server-to-server `[CONFIRMED 2026-05-22 — ping from cemini-egress-fi to cemini-librarian 5.161.179.207, 3 samples avg 119 ms]`, slightly longer than the previous Falkenstein-to-Ashburn (~90-100 ms) but inside the same order of magnitude; the choice was venue-coverage-driven, not latency-driven.

### Spare capacity — candidate Cemini AI host

The box is near-idle: one near-zero-cost job (SSH tunnelling) on librarian-class hardware. With ~3.3 GB RAM and ~71 GB disk free it can comfortably host the **Cemini AI assistant** gateway (see @concepts/cemini-ai-assistant.md) during that project's internal-only phase. Caveats recorded on that page — chiefly (a) the transatlantic hop to the Ashburn kb-server on every retrieval, and (b) the security argument against co-locating an eventually-public chatbot on a box that sits in the live order-execution path. Both are deferred, not dismissed, while the assistant has no external users.

**K48 inference-scaling posture [CONFIRMED 2026-05-21]:** arXiv:2605.19775 shows long chain-of-thought reasoning is **KV capacity-bound**, not compute-bound. This host has **no GPU** and only 4 GB RAM — it must remain an **API-routing gateway** (DeepSeek / OpenRouter) for reasoning models, not a local weight host. Lazy-tool on the laptop reduces MCP schema bloat but does not solve the KV wall.

**K57 Polymarket copy-trading latency posture [CONFIRMED 2026-05-22]** — adoption on egress-fi is **documentation only** (no new binaries from K57; flox / near-resolution-bot stay off this box). From @spottr_trade: leader fills on Polymarket's **hybrid CLOB** (off-chain match, on-chain settlement). Followers observe via mempool/settlement — **not** at match time. Marketing **"0-block execution"** means the follower lands in the **same Polygon settlement block** as the leader, not zero detection lag. Any Cemini AI or propose-action flow hosted here must **not** claim sub-block copy parity or HFT-grade mirror latency without measured end-to-end ms on real fills. Prod operator detail: brief `2026-05-22_k57-polymarket-operator-refinements-cemini.md` on `cemini-prod` (read-only from this workspace).

### GDPR / EU-residency posture

Helsinki is an EU member state — the same EU-data-residency story applies as it did for Falkenstein. Customer-side sessions and stash memory landing on this box stay inside the EU; DeepSeek inference still leaves the EU and would need an EU-hostable synthesis model if a hard EU-residency requirement on *inference* surfaces.

## Snippets

### Read-only probe — 2026-05-20 (via `ssh -J cemini-prod`)

```
=HOST=    cemini-egress-fi
=OS=      Linux 6.8.0-117-generic (Ubuntu)
=CPU=     2
=MEM=     total 3.7Gi / used 428Mi / free 2.9Gi / available 3.3Gi
=DISK=    /dev/sda1  75G  1.5G used  71G avail  3%
=UPTIME=  16 min, load average 0.00 0.00 0.00
=DOCKER=  no docker
=LISTEN=  sshd :22 (v4+v6); systemd-resolved :53 (localhost only)
=WG=      no wireguard
=EGRESS=  204.168.139.190 (IPv4) / 2a01:4f9:c010:da39::1 (IPv6)
```

### Read-only probe — 2026-05-22 (via `ssh -J cemini-prod`)

```
=HOST=    cemini-egress-fi
=UPTIME=  up 2 days, 45 minutes
=MEM=     458Mi / 3.7Gi used
=DOCKER=  none
=LISTEN=  sshd :22 only (public)
=/opt=    cemini-ai/ (gateway tree; K57 adds no new packages here)
```

ipinfo.io on the public IP → `city: Helsinki · region: Uusimaa · country: FI · org: AS24940 Hetzner Online GmbH · timezone: Europe/Helsinki`. rDNS `static.190.139.168.204.clients.your-server.de` confirms Hetzner.

## Dead Ends

- **Direct SSH from the laptop** — `cemini-egress-fi:22` is firewalled at the Hetzner edge; the connection times out from the laptop's residential IP. Reachable only via `ssh -J cemini-prod` (jump host). The SSH alias `cemini-egress-fi` in `~/.ssh/config` bakes in `ProxyJump cemini-prod` so the indirection is transparent.

- **Predecessor — `cemini-poly-proxy` (Falkenstein, Germany)** — retired 2026-05-20. The Falkenstein box played the same role (egress relay) with the same spec class (2 vCPU / 4 GB / 75 GB, sshd-only) at IP `178.105.151.69`. It was swapped out for the Helsinki box because Polymarket *and* Hyperliquid both accept Finnish egress, whereas Falkenstein had been provisioned with only Polymarket in mind. The architecture is unchanged; only the country and hostname are.
