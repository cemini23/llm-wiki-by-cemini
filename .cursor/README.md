# Cursor MCP — OSINT workspace

## Home vs this folder (why colors differ)

| Where you are | lazy-tool | stash | prod-mcp / exa / fetch |
|---------------|-----------|-------|-------------------------|
| **Cursor Home** (no folder) | Off / not listed | Global only — red if tunnel down | Not loaded |
| **OSINT WORKSPACE** open | Project — should be green | Global — green if tunnel up | Project servers |

**lazy-tool off at Home is correct.** Open **File → Open Folder → OSINT WORKSPACE** for wiki / conductor / kb / prod proxy tools.

**stash red at Home, green in OSINT:** usually the same global server — Home may have connected before the SSH tunnel finished. Fix:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8088/sse   # expect 200
launchctl kickstart -k "gui/$(id -u)/com.cemini.stash-tunnel"
```

Then **Cursor Settings → MCP → stash → Retry** (or restart Cursor — see below).

---

## Reload Cursor after MCP changes

There is no separate “Developer: Reload” menu item in all builds. Use any of:

1. **Command Palette** (`Cmd+Shift+P`) → type **`Reload Window`** → run **Developer: Reload Window** (if shown) or **Reload Window**
2. **Cursor Settings → MCP** → **Retry** on each red server
3. **Quit Cursor completely** (`Cmd+Q`) and reopen — works every time; use this if MCP stays stale

---

## Project MCP (this folder)

**Turn lazy-tool ON:** `Cmd+Shift+J` → **Tools & MCP** → **lazy-tool** toggle → **On** (green).  
Cursor remembers this per machine. If it says **Off**, agents cannot reach kb-server / conductor — only prod/exa/fetch direct tools work.

| Server | Role |
|--------|------|
| **lazy-tool** | **Required — keep enabled** — conductor, kb-server, prod-mcp, fetch, exa (see `.cursor/rules/osint-mcp-defaults.mdc`) |
| **prod-mcp** | CeminiSuite prod (`:18002` tunnel) |
| **exa** | `scripts/mcp_exa.sh` → `~/.cemini/exa-api-key` |
| **fetch** | `mcp-fetch-server` |

## Global MCP (`~/.cursor/mcp.json`)

| Server | Role |
|--------|------|
| **stash** | Episodic memory `localhost:8088` |
| **brave-search** | Web search (API key in that file only) |
| **playwright** | Browser automation |

No `librarian-stash` in this project (duplicate removed).

---

## Maintenance

```bash
curl -s -o /dev/null -w 'stash:%{http_code}\n' http://127.0.0.1:8088/sse
curl -s -o /dev/null -w 'prod:%{http_code}\n' http://127.0.0.1:18002/mcp

cd "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
lazy-tool reindex --config ".cursor/lazy-tool.yaml"
```

LaunchAgents: `com.cemini.stash-tunnel`, `com.cemini.prod-mcp-tunnel` in `~/Library/LaunchAgents/`.

## Agent rules

- **OSINT folder:** `.cursor/rules/osint-mcp-defaults.mdc` (`alwaysApply: true`) — lazy-tool workflow
- **All folders:** `~/.cursor/rules/cemini-projects.mdc` — which repo to open for which work

No extra rules in Cursor Settings UI are required if those `.mdc` files are present.

## Subagents

You do **not** need custom subagents per wiki. Use:

- **This agent** + lazy-tool + wiki for ingest/query/lint
- Cursor **Task** / explore subagent only for large codebase audits (optional)
- **Separate Open Folder** per repo (CeminiSuite vs OSINT vs sibling wikis) for the right `.cursor/mcp.json`

Sibling wikis (image-gen, seo, cybersec, ccc) live under `Desktop/projects/…` — open that wiki’s parent project if you need project-specific MCP there.

## Secrets

- **Exa:** `~/.cemini/exa-api-key` or `EXA_API_KEY`
- **Brave:** `~/.cursor/mcp.json` only — never commit keys
