---
title: Cemini Repository Topology — Monorepo vs Multi-Repo Decision Framework
type: concept
tags: [concept, infrastructure, cemini-internal, git, github, monorepo, workspace-ops]
keywords: [monorepo, multi-repo, Cemini-Financial-Suite, llm-wiki-by-cemini, deploy repo, research wiki, integration contracts, Cursor workspace]
related:
  - concepts/laptop-prod-research-split.md
  - concepts/librarian-server-architecture.md
  - concepts/cemini-deployment.md
  - entities/infrastructure/cemini-stack.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/laptop-prod-research-split.md — which **machine** runs which research step (orthogonal to git layout)
- @concepts/librarian-server-architecture.md — three-server runtime topology (prod / librarian / laptop editor)
- @concepts/cemini-deployment.md — how the deploy monorepo lands on Hetzner
- @entities/infrastructure/cemini-stack.md — 41-container production stack the deploy repo builds
- @concepts/cemini-license-posture.md — license boundaries when splitting or federating repos

## Raw Concept

User question (2026-05-28): Is one GitHub repo still fine for the whole Cemini project, or should it be split into parts? Tension: modular internals vs confusion when everything lives together; desire for seamless integration; uncertainty whether separate repos change runtime behavior.

This page records the **decision framework** — not a migration plan. Synthesized from the current federation map (`Cemini-Financial-Suite` README wiki table, `@concepts/laptop-prod-research-split.md`, prod stack audit K75).

## Narrative

### Current federation (already multi-repo)

Cemini is **not** a single-repo project today. Repositories are split by **role**, not by accident:

| Layer | GitHub / local path | Purpose | Visibility |
| --- | --- | --- | --- |
| **Deploy monorepo** | `cemini23/Cemini-Financial-Suite` → `/opt/cemini` on prod | Runnable trading stack: Docker Compose, brain, EMS, ingest, MCP, UI | Private (IP-sensitive) |
| **Financial research wiki** | `llm-wiki-by-cemini` — laptop `OSINT WORKSPACE/wiki/` | Ingest, curate, briefs → `/opt/cemini/briefs/` | Private |
| **Domain wikis** | ccc, cybersec, image-gen, seo, 3d-printing | Cross-domain knowledge; federated via `@wiki-alias/` | Public (except osint) |
| **Runtime** | `cemini-prod`, `cemini-librarian`, `cemini-egress-fi` | Integration at deploy time — Redis, Postgres, HTTP, private net | N/A (servers) |

The deploy monorepo **internally** contains multiple products in one tree: `QuantOS/`, `Kalshi by Cemini/`, `core/`, `agents/`, `cemini_mcp/`, etc. That internal layout is a **monorepo**; the outer project is a **federation**.

### Decision (2026-05-28): keep deploy monorepo; do not split trading code into separate GitHub repos

**Recommendation:** Keep **one deploy monorepo** for prod code. Keep **research wikis separate** (already correct). Do **not** split QuantOS / Kalshi / brain into independent GitHub repos unless release-cadence or team-ownership gates below are met.

**Rationale:**

1. **Integration is runtime-bound, not git-bound.** Prod integrates via shared Postgres/TimescaleDB, Redis pub/sub, HTTP bridges (e.g. QuantOS ↔ Kalshi), `docker-compose.yml`, and shared contract modules (`cemini_contracts/`, e.g. `strategy_logic_versions.py`). Separate repos would still need the same contracts — with added version-pinning and cross-repo PR overhead.

2. **Splitting repos does not reduce agent/human confusion by itself.** Confusion observed in practice comes from **which Cursor folder is open** (OSINT vs CeminiSuite vs prod SSH session), **subsystem naming** (three products in one directory), and **laptop tree vs `/opt/cemini` drift** — not from monorepo vs polyrepo at the GitHub level.

3. **Small-team cost.** Multi-repo without independent release trains adds submodule/tag choreography, duplicated CI, and atomic-change friction (one logical feature touching brain + Kalshi becomes two PRs + compatibility matrix).

4. **Precedent in workspace doctrine.** `@concepts/laptop-prod-research-split.md` already defines the meaningful boundary: laptop wiki curates → briefs stage → prod executes. That split is **deployment + IP**, not "split Kalshi into its own repo."

### When separate repos *would* make sense (future gates)

Split a subsystem into its own GitHub repo only when **all** of the following are true:

| Gate | Example trigger |
| --- | --- |
| **Independent release cadence** | Kalshi ships weekly; brain ships monthly; compose pins image tags explicitly |
| **Separate ownership** | Different maintainers; no routine cross-cutting changes |
| **Published SDK / external consumers** | e.g. `cemini-kalshi-client` on PyPI for third parties |
| **Hard contract surface** | Shared schemas in a pinned package (`cemini_contracts` semver); integration tests across repos |

Until then, splitting creates ops cost without integration benefit.

### Industry patterns (mapped to Cemini)

| Pattern | When it works | Cemini fit |
| --- | --- | --- |
| Monorepo (one deploy tree) | Shared contracts, atomic changes, one Compose stack, small team | **Current prod — keep** |
| Monorepo + internal packages | Same repo; clear `services/` or `packages/contracts` boundaries | **Best low-cost improvement** |
| Multi-repo + runtime compose | Independent teams/releases; published SDKs | Overkill today |
| Research repo ≠ code repo | IP, cadence, who edits what | **Already correct** (OSINT wiki ≠ CeminiSuite) |

Large org monorepos (Google, Meta) enforce boundaries via **folder ownership + build graph**, not by multiplying repos. Cemini's analog: subsystem docs + contract module + workspace discipline.

### What actually causes "everything feels together" confusion

| Source | Fix (repo split?) |
| --- | --- |
| Three products in one folder (`QuantOS/`, `Kalshi by Cemini/`, `core/`) | **No** — use subsystem `CLAUDE.md`, ownership map, contract imports |
| Three Cursor worlds (OSINT / CeminiSuite / prod SSH) | **No** — document "open this folder when…" in each repo README |
| Laptop git ≠ prod tree 1:1 | **No** — record deploy SHA on prod; briefs as handoff |
| Six federated wikis + cross-links | **No** — already correct for IP/visibility; use `@wiki-alias/` consistently |

### Low-cost clarity improvements (no migration)

1. **Subsystem boundary docs** — `QuantOS/CLAUDE.md`, `Kalshi by Cemini/CLAUDE.md`, `core/CLAUDE.md`: scope, integration points, do-not-touch lists.

2. **`cemini_contracts/` as integration surface** — cross-cutting IDs, event schemas, API DTOs, version registries live here; subsystems import, do not duplicate.

3. **Cursor folder discipline**

   | Open folder | When |
   | --- | --- |
   | `OSINT WORKSPACE` | Wiki ingest, briefs, research, kb-server queries via lazy-tool |
   | `CeminiSuite` | Prod code edits, Docker, local stack dev |
   | Prod SSH (server-Claude) | Read-only verify + execute briefs under `/opt/cemini/briefs/` only |

4. **Deploy manifest as source of truth** — tag or record git SHA deployed to `/opt/cemini` so laptop and prod are not ambiguous.

5. **Optional internal layout refactor** — e.g. `services/quantos`, `services/kalshi`, `packages/contracts` within the same repo — improves navigation without multi-repo overhead.

### Does multi-repo break seamless integration?

**No** — if integration is defined at runtime (Compose, Redis, DB, HTTP, shared contracts).

**Yes** — if repos split **without** hard contracts and deploy pinning; then Kalshi and brain drift independently.

Brief pipeline (`wiki/briefs/` → `scp` → `/opt/cemini/briefs/` → server-Claude) is the **intentional cross-repo integration path** for research → prod. It works regardless of whether QuantOS and Kalshi share one git repo.

### One-line decision

**One deploy monorepo + separate research wikis is the correct shape for Cemini today.** Reduce confusion via folder ownership, contracts, and workspace choice — not additional GitHub repos.

## Snippets

> "This trading stack is **private** (IP-sensitive). It is not a wiki; research canon lives in sibling wikis." [Source: Cemini-Financial-Suite README — Related Cemini knowledge wikis table]

> "You do not need to switch Cursor workspace for Kronos A/B if prod agent can reach Postgres — it is running on prod now." [Source: @concepts/laptop-prod-research-split.md]
