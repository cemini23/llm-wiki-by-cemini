---
title: Hetzner
type: entity
tags: [infrastructure, vps, hosting, cemini-deployment]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-17-git-research-pt2.md
  - sources/3-9-pm-research.md
  - sources/forex-research-3-18.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/deepseek-api.md
  - sources/crypto-3-4-11.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-17-git-research-pt2.md
- @sources/3-9-pm-research.md
- @sources/forex-research-3-18.md
- @concepts/ip-sale-readiness.md
- @entities/infrastructure/deepseek-api.md — host that holds the API client + key

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

Hetzner is a German VPS provider hosting the Cemini production stack.
The current deployment is a single CPU-only dedicated server: AMD EPYC,
128GB RAM, 18–26 Docker containers via docker-compose (not Kubernetes —
deliberately), targeting cost efficiency over horizontal scale.

Documented architectural facts across the corpus:
- **CPU-only constraint** — quant strategies rely on Polars/NumPy/CPU-native ML, not GPU acceleration. `[RETRACTED 2026-04-24]` Earlier phrasing here implied a local LLM (DeepSeek-R1-14B on Ollama) runs on the host; that is not deployed. See @entities/infrastructure/deepseek-r1-14b.md and @entities/infrastructure/ollama.md for the retraction notes.
- Server reference: `root@<see .local/server.md>`, path `/opt/cemini`.
- TimescaleDB + PostgreSQL + Redis + the LangGraph orchestrator +
  Prometheus/Loki/Grafana/Tempo stack + FastAPI app containers all co-
  tenant on the same host.
- IP-sale story: the whole stack reproduces from one docker-compose up
  on commodity CPU hardware — no vendor lock-in, no hyperscaler SLAs,
  no GPU-hour bills to untangle for the acquirer.

## Snippets

*(populate as source stubs are deep-read.)*
