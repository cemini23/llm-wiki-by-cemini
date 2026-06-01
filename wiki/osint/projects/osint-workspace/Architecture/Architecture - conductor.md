---
title: Architecture — conductor module
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
project: "[[projects/osint-workspace/OSINT Workspace]]"
module: conductor
path: conductor/
scanned-commit: b960aae
tags: [architecture, conductor, mcp]
ai-first: true
related:
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/librarian-server-architecture.md
  - entities/tools/lazy-tool.md
maturity: validated
---

## Relations

- @projects/osint-workspace/Architecture/Architecture - Overview.md
- @concepts/librarian-server-architecture.md

## For future Claude

Documents the **`conductor/`** Python package in this repo: a **laptop MCP shim** and local orchestrator code that mirrors the Cemini Conductor taxonomy/cascade design. Production routing runs on `cemini-librarian` under `/opt/cemini`; `conductor/mcp_server.py` SSH-invokes that CLI. Scan: 26 Python files under `conductor/`, commit `b960aae`.

<!-- @generated:start -->

## Responsibility

Multi-model **query router** for analyst-style financial questions: classify taxonomy → select model pool → cascade → optional kb-server/stash tools → structured response. [Source: `conductor/orchestrator.py` module docstring, retrieved 2026-06-01]

## Key components (in-repo)

| File / area | Role |
| --- | --- |
| `orchestrator.py` | `Conductor` class — wires taxonomy, pool, cascade, tools |
| `taxonomy.py` | Query classification (ticker, macro, quant methods, etc.) |
| `cascade.py` | Model cascade routing |
| `pool.py` | Model pool selection |
| `mcp_client.py` | `KBServerClient`, `StashClient` |
| `mcp_server.py` | Stdio MCP exposing `conductor_query` |
| `api.py` | DeepSeek client |
| `config.yaml` | Runtime config |
| `cli.py` | CLI entry used over SSH on librarian |

## Runtime path (laptop MCP)

`conductor/mcp_server.py` runs locally in Cursor/Claude MCP config. On `conductor_query`, it **SSHs to `cemini-librarian`** and executes:

`cd /opt/cemini && PYTHONPATH=/opt/cemini .venv/bin/python -m conductor.cli ...`

[Source: `conductor/mcp_server.py` lines 42–56, retrieved 2026-06-01]

**Implication:** Laptop folder is source-of-truth for development; **live routing** depends on deployed `/opt/cemini` conductor on the librarian/prod federation.

## Dependencies

- Python stdlib + `yaml` in orchestrator; `requirements.txt` in `conductor/` for full install
- External: SSH to `cemini-librarian`, DeepSeek API (via deployed stack), kb-server, stash (when enabled in config)

## Role in the whole

Agents in **OSINT WORKSPACE** reach unified wiki + analyst synthesis via **lazy-tool** → `conductor_query` (preferred) or direct MCP when catalogued. This module does **not** execute trades or modify prod config.

<!-- @generated:end -->
