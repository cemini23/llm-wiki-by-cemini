---
title: "Code w/ Claude 2026 — Ivan Nardini live-builds a GCP feedback app (X clip via @clayul)"
type: source
tags: [source, x-video, claude-code, google-cloud, k238]
keywords: [Ivan Nardini, Code with Claude, Cloud Run, Firestore, Vertex, plan mode, MCP, skills, subagents]
related:
  - concepts/persona-hat-claude-code-sdlc.md
  - concepts/claude-code-skills-md-workflow.md
  - concepts/code-as-agent-harness.md
  - concepts/role-specialization-model-rsm.md
  - entities/tools/google-skills.md
  - entities/people/ivan-nardini.md
maturity: draft
read_status: read
created: 2026-08-15
updated: 2026-08-15
clusters: [k238-ingest]
---

## Relations

- @concepts/persona-hat-claude-code-sdlc.md — five-hat SDLC steal (PM → UX → SWE → security → data)
- @concepts/claude-code-skills-md-workflow.md — skills as implementation blocks vs MCP as architecture
- @concepts/code-as-agent-harness.md — live instance of skills + MCP + subagents as harness
- @concepts/role-specialization-model-rsm.md — demo hats vs paper RSM (overlap / no scope lock)
- @entities/tools/google-skills.md — **not** github.com/google/skills packing; Cloud Run/Firestore Claude Code skills
- @entities/people/ivan-nardini.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Tweet** | https://x.com/clayul/status/2087915800933933510 |
| **Poster** | @clayul (clip), 2026-08-13 14:54 UTC; ~6.7M views at retrieve |
| **Canonical talk** | Code w/ Claude 2026 SF, 2026-05-06 16:05–16:35 — Ivan Nardini (Google Cloud DevRel / AI/ML) |
| **Session page** | https://claude.com/code-with-claude/session/sf-building-with-claude-on-google-cloud |
| **YouTube** | https://www.youtube.com/watch?v=SqHsS737CeA (official Claude channel; 1589s; uploaded 2026-05-08) |
| **Duration** | X amplify ~1568s; YouTube 1589s |
| **Filename** | `x-clayul-ivan-nardini-claude-gcp-2026-08-13.mp4` |
| **sha256 (mp4)** | `b6b07acaa217557a4d9a1746fc829d2cb1798be93f98ef2f839621931839e5a1` (564,254,096 bytes) |
| **sha256 (en.txt)** | `8dc51b3abb2f78e0d24ca643b441e500e3607d0257d183042380bbba156b96c0` |
| **Transcript** | YouTube auto-captions `en.vtt` → `x-clayul-ivan-nardini-claude-gcp-2026-08-13.en.txt` (yt-dlp; no Whisper — ffmpeg missing locally) |
| **Retrieved** | 2026-08-15 via opencli `twitter thread` + yt-dlp (X mp4 + YT subs) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-clayul-ivan-nardini-claude-gcp-2026-08-13.mp4` |

## Narrative

@clayul's Spanish clip-post frames a Google Cloud engineer building a complete app with Claude from scratch in ~26 minutes on stage — "worth more than any $500 vibe-coding course." The clip is the **Code w/ Claude 2026** session *Building with Claude on Google Cloud*: Nardini wears **five hats** (PM, UI/UX, software engineer, security engineer, growth/data) to ship a live **session-feedback app** on GCP.

**Harness stack shown:** Claude Code on **Vertex / Google Cloud models** via **Application Default Credentials** (no API-key rotate; data stays in-project; pay-per-token + provisioned throughput vs message-cap). **Plan mode** for UX (think-then-propose; optional Figma MCP). SWE hat: **Developer Knowledge API MCP** (fresh GCP docs → architecture) paired with **Google Cloud Skills** (Cloud Run deploy, Cloud Run↔Firestore wiring — implementation blocks, not the picture). **Three parallel subagents** (API, ingestion pipeline, dashboard). Pre-built **security review** (OWASP + service-account least privilege); Nardini admits the security engineer both *approves and deploys* — demo simplification. Live Cloud Run endpoint; BigQuery + Looker / BigQuery MCP for the data hat.

**Cemini steal (CCC-primary):** split MCP (architecture/docs) from skills (one block); fan-out subagents by component; plan mode before UX code; security review as a required check, not a vibe. **Do not** treat 26 minutes as a production SDLC — replies correctly flag testing, CI/CD, monitoring, maintenance. **Do not** conflate this talk's "Google Cloud Skills" with `@entities/tools/google-skills.md` (github.com/google/skills packing repo).

**Routing:** CCC brief. No Atto/GuruWatcher/poker/xsp-pm scp.

## Snippets

> "Un ingeniero de Google Cloud acaba de mostrar cómo construir una aplicación completa con Claude desde cero. … Vale más que cualquier curso de codificación por vibras de $500, sin equipo, sin configuración, solo Claude y un objetivo." [Source: https://x.com/clayul/status/2087915800933933510 (retrieved 2026-08-15)]

> "with the MCP server you will be able to design the architecture, with the skills you will be able to cover the single blocks of this architecture." [Source: YouTube auto-captions SqHsS737CeA]

> "we are going to spin up three different sub agents, one for the API, one for the ingestion pipeline, and the other one for the dashboard." [Source: YouTube auto-captions SqHsS737CeA]

> "we are letting the security engineer not only to approve if the app is secure enough to be deployed, but it will also deploy the app in this case. But again, this is just a demo" [Source: YouTube auto-captions SqHsS737CeA]
