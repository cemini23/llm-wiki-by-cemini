---
title: Architecture — ui module
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
project: "[[projects/osint-workspace/OSINT Workspace]]"
module: ui
path: ui/
scanned-commit: b960aae
tags: [architecture, ui, dev-tooling]
ai-first: true
related:
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - entities/infrastructure/cemini-stack.md
maturity: draft
---

## Relations

- @projects/osint-workspace/Architecture/Architecture - Overview.md

## For future Claude

**`ui/`** is a **minimal local dev front-end** (3 files): static `index.html` + stdlib `serve.py` proxy so the browser can call the Cemini AI gateway on `cemini-egress-fi` without CORS changes. Not part of prod Compose; optional operator tooling.

<!-- @generated:start -->

## Responsibility

Local **chat UI** for the FastAPI gateway on `cemini-egress-fi:8088`.

## Components

| File | Role |
| --- | --- |
| `index.html` | Browser chat client |
| `serve.py` | HTTP server on `127.0.0.1:9000` (default); proxies `/chat`, `/health` to tunneled gateway |
| `README.md` | Runbook: SSH tunnel `8288→8088`, env `CEMINI_AI_GATEWAY_PORT`, `CEMINI_AI_UI_PORT` |

## Data flow

```
browser :9000  →  ui/serve.py  →  localhost:8288 (SSH -L)  →  cemini-egress-fi:8088
```

[Source: `ui/README.md`, retrieved 2026-06-01]

## Dependencies

- Python 3.11+ stdlib only (no npm build in `ui/`)
- Requires active SSH tunnel to egress host

## Role in the whole

**Developer convenience** alongside wiki/conductor workstreams — does not participate in ingest, sync, or trading execution.

<!-- @generated:end -->
