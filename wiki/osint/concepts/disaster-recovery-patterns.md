---
title: Disaster recovery patterns — RPO/RTO and the four failover shapes
type: concept
tags: [engineering, reliability, disaster-recovery, infrastructure]
keywords: [rpo, rto, backup-restore, pilot-light, warm-failover, active-active, capacity-reservation, slo]
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
  - concepts/ai-vendor-multimodel-resilience.md
  - entities/infrastructure/cemini-stack.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
- @concepts/ai-vendor-multimodel-resilience.md
- @entities/infrastructure/cemini-stack.md

## Raw Concept

**The question this page answers:** what are the standard disaster-recovery shapes, and which one fits a given service?

Source: Sam Newman, *Building Resilient Distributed Systems*, Chapter 10, via The Pragmatic Engineer, 2026-10-13.

## Narrative

### The two targets

- **RPO (recovery point objective)** — the **maximum tolerable data loss**, i.e. how far back the last usable backup or sync is.
- **RTO (recovery time objective)** — the **maximum tolerable unavailability**, including time to restore data, provision compute, and re-route traffic.

**You cannot have RPO 0 and RTO 0.** Cost and complexity rise steeply as either shrinks, and a literal zero is not achievable. **Different services need different targets** — a bank's payments path versus its sign-up flow.

**RPO/RTO are poor SLOs.** Disasters are too rare to accumulate useful SLIs. You can only measure *proxies* (for example, replication speed), which are tangential to the actual objective. Targets should also **exceed anything in your SLAs**.

### The four patterns

| Pattern | Data | Infrastructure | RPO / RTO |
|---------|------|----------------|-----------|
| **Backup and restore** | periodic backup to a second site | provisioned on demand | longest RTO (minutes → weeks if hardware must be bought); RPO = backup interval |
| **Pilot light** | continuous replication | provisioned after failover | much shorter RPO; RTO saves the restore step |
| **Warm failover** | continuous replication | partially provisioned, reserved for critical services | lower RTO for top-priority functions only |
| **Multisite active-active** | replication between 2+ sites, writes to any | always on | best RPO/RTO; highest cost and complexity |

They **compose** — a system can start at backup-and-restore and add replication and warm capacity over time. All require **traffic re-routing**; most require **cross-site replication**. Keep the **failover stack identical to the primary** so the same automation (Terraform, etc.) works on both.

### Capacity is now a first-class DR constraint

**GPU and memory costs spiked in 2025–2026**, and organisations report **failing to secure capacity for ordinary, non-AI workloads**. A DR plan that assumes **dynamic provisioning at failover time** may not get the capacity. Three options:

1. **Reserve capacity** — AWS EC2 reservations exist (paid whether used or not); **not possible for services like Lambda**.
2. **Prioritise critical services** — requires per-service RPO/RTO.
3. **Run fully redundant infrastructure** — costly, but **offset by reusing idle DR capacity** (for example as a load-test pool that is aborted when DR is needed).

### Why it matters here
Directly relevant to the **`cemini-*` hosts** (`@entities/infrastructure/cemini-stack.md`), whose posture is already "laptop canonical, egress cold store." The actionable question this frame raises: **what are the RPO/RTO for the wiki repo, the egress cold store, and GuruWatcher** — and is capacity reservation needed for anything that must survive a region failure? Also note the pairing with `@concepts/ai-vendor-multimodel-resilience.md`: a model provider is a **third-party dependency in the critical path**, and the same failover vocabulary applies.

## Snippets

> If asked what RPO and RTO you'd want in a vacuum, you'd probably give a very simple answer: you'd want an RPO of zero … and an RTO of zero too. … it's not possible to guarantee a zero RPO or RTO in any case. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> If your chosen approach assumes you can dynamically provision infrastructure when a failure occurs, you will have to look at what guarantees you have around the capacity you want. In a scenario where a major cloud vendor's region has failed, you may find yourself fighting over scraps with everyone else. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]
