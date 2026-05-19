---
title: cemini-poly-proxy — German order-routing relay (Hetzner Falkenstein)
type: entity
tags: [infrastructure, hetzner, polymarket, hyperliquid, order-routing, proxy, cemini-deployment]
keywords: [cemini-poly-proxy, falkenstein, fsn1, ssh-tunnel, order-egress, geo-routing, germany, third-server]
related:
  - concepts/cemini-ai-assistant.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
maturity: draft
created: 2026-05-19
updated: 2026-05-19
# Live-probed 2026-05-19 (read-only SSH via cemini-prod jump host). Refresh on spec/role change.
---

## Relations

- @concepts/cemini-ai-assistant.md — candidate host for the Cemini AI assistant gateway during its internal-only phase (this box has the headroom)
- @entities/infrastructure/cemini-stack.md — the umbrella production topology; this is the previously-undocumented third server
- @concepts/librarian-server-architecture.md — the librarian (kb-server + stash) this box would query if it hosts Cemini AI; both are Hetzner, different DCs (Falkenstein vs Ashburn)

## Raw Concept

The third Hetzner server in the Cemini fleet — surfaced 2026-05-19 when the user named it as the egress relay through which Polymarket and Hyperliquid orders route. It postdates every prior infrastructure record: `hot.md`, `.local/server.md`, @entities/infrastructure/cemini-stack.md and @concepts/librarian-server-architecture.md all describe a *two*-server topology, and `hot.md` still documents Polymarket order routing as a laptop-side forward-tunnel test harness. This page closes that documentation gap.

Probed read-only 2026-05-19 — SSH via `cemini-prod` as jump host (the box's port 22 is firewalled to the Hetzner fleet, not the open internet).

## Narrative

### What it is

| Field | Value |
|---|---|
| Hostname | `cemini-poly-proxy` |
| Provider / location | Hetzner Cloud, **Falkenstein (FSN1), Germany** |
| Public IP / SSH access | see `.local/server.md` (jump host required) |
| Spec | 2 vCPU · 4 GB RAM (3.7 GiB measured) · 75 GB disk · Ubuntu 24.04.4 LTS |
| Utilisation (2026-05-19) | 432 MB RAM used · 1.5 GB disk used · load average 0.00 |
| Headroom | ~3.3 GB RAM free · ~71 GB disk free |
| Running | `sshd` only — no Docker, no WireGuard, no proxy daemon |

### Role — order-egress relay

`cemini-poly-proxy` exists so that Polymarket and Hyperliquid order traffic egresses from a **German IP** rather than the Ashburn production IP. Polymarket enforces geo-blocking on order submission (`POST /order` returns HTTP 403 from US IPs; market-data reads are unrestricted — profiled 2026-05-18, recorded in `hot.md`).

The routing mechanism is lightweight: there is **no WireGuard and no proxy process listening**. The relay is almost certainly plain **SSH tunnelling** — `cemini-prod` opens an `ssh -D`/`-L` tunnel *through* this box so order calls exit with the German IP. `sshd` on `:22` is the entire serving surface, which is why the box sits at load 0.00. `[TENTATIVE 2026-05-19 — mechanism inferred from the probe; not yet confirmed against cemini-prod config]`

This supersedes the abandoned approaches recorded in `hot.md`: server-side WireGuard on `cemini-prod` (dropped as fragile) and the laptop-side `polymarket_proxy.py` forward-tunnel (a validation harness that violated the deployment boundary). The German relay is the production answer — egress is server-side and the laptop is out of the path.

### Relationship to the rest of the fleet

It is the **third** Hetzner server, joining `cemini-prod` (Ashburn, trading stack) and `cemini-librarian` (Ashburn, knowledge serving). Unlike those two it is in a different datacentre — Falkenstein, not Ashburn — a deliberate consequence of needing a non-US egress IP. Falkenstein-to-Ashburn is a transatlantic hop (~90-100 ms server-to-server; laptop-to-Falkenstein measured 153 ms RTT 2026-05-19).

### Spare capacity — candidate Cemini AI host

The box is near-idle: one near-zero-cost job (SSH tunnelling) on librarian-class hardware. With ~3.3 GB RAM and ~71 GB disk free it can comfortably host the **Cemini AI assistant** gateway (see @concepts/cemini-ai-assistant.md) during that project's internal-only phase. Caveats are recorded on that page — chiefly (a) the transatlantic hop to the Ashburn kb-server on every retrieval, and (b) the security argument against co-locating an eventually-public chatbot on a box that sits in the live order-execution path. Both are deferred, not dismissed, while the assistant has no external users.

## Snippets

### Read-only probe — 2026-05-19 (via `ssh -J cemini-prod`)

```
=HOST=   cemini-poly-proxy
=OS=     Ubuntu 24.04.4 LTS
=CPU=    2
=MEM=    total 3.7Gi / used 432Mi / free 2.9Gi / available 3.3Gi  (swap 0B)
=DISK=   /dev/sda1  75G  1.5G used  71G avail  3%
=UPTIME= up 1 day 5:56, load average 0.00 0.00 0.00
=DOCKER= no docker
=LISTEN= sshd :22 (v4+v6); systemd-resolved :53 (localhost only)
=WG=     no wireguard
```

whois on the public IP → `netname: CLOUD-FSN1 · country: DE · descr: HETZNER-DC` — confirms Hetzner Falkenstein.

## Dead Ends

- **Direct SSH from the laptop** — `cemini-poly-proxy:22` is firewalled; the connection times out from the laptop's residential IP. Reachable only via `ssh -J cemini-prod` (jump host). Recorded in `.local/server.md`.
