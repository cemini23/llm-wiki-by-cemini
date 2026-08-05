# Operator — env + rotate (Cursor MCP P0)

**Date:** 2026-08-01  
**No secrets in this file.** Do not paste API keys into chat, git, or `mcp.json`.

Agent sandbox **cannot write** `~/.cursor/*` (macOS TCC). Run global steps in **Terminal.app**.

---

## 0. One-shot global cleanup (required)

**Why:** Cursor agent / Grok cannot write `~/.cursor/*` (macOS TCC). Project-tree fixes are already applied; only this step needs **Terminal.app**.

From the OSINT workspace:

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
bash scripts/apply_cursor_global_p0_cleanup.sh
```

What it does (no tokens printed):

- Deletes `~/.cursor/rules/tipdrop-route-outsource.mdc` (keep only `cemini-route-outsource.mdc`)
- Rewrites `~/.cursor/mcp.json`:
  - Brave → `"BRAVE_API_KEY": "${env:BRAVE_API_KEY}"` + `disabled: true`
  - GitHub → `"Authorization": "Bearer ${env:GITHUB_TOKEN}"` (no embedded Bearer)
  - `disabled: true` on playwright, cloudflare×5, stash, stripe, codebase-memory-mcp, brave-search

Dry-run:

```bash
bash scripts/apply_cursor_global_p0_cleanup.sh --dry-run
```

Optional GitHub MCP re-wire (env-ref only; never embeds token):

```bash
bash scripts/setup_cursor_github_mcp.sh
# only if you want a file backup of the gh oauth token (not required for MCP):
# bash scripts/setup_cursor_github_mcp.sh --write-pat-file
```

---

## 1. GitHub for Cursor MCP (existing `gh auth` — no new PAT required)

```bash
# GitHub for Cursor MCP (uses existing gh auth — no new PAT required)
export GITHUB_TOKEN="$(gh auth token)"
# optional refresh if you want a new oauth token:
# gh auth refresh -h github.com -s gist,read:org,repo,workflow

# Persist for GUI apps (Cursor) — pick one:
# launchctl setenv GITHUB_TOKEN "$(gh auth token)"   # session; or use ~/.zshrc + restart Cursor from terminal
```

### Persist across restarts (recommended)

Add to `~/.zshrc` (token not stored; re-read from keychain on each shell):

```bash
# Cursor GitHub MCP — load from gh keychain (never commit this token)
if command -v gh >/dev/null 2>&1; then
  export GITHUB_TOKEN="$(gh auth token 2>/dev/null || true)"
fi
```

Then **launch Cursor from that shell** so GUI inherits the env:

```bash
export GITHUB_TOKEN="$(gh auth token)"
open -a Cursor
# or: open -a "Cursor" "/Users/claudiobarone/Projects/OSINT WORKSPACE"
```

Session-only for apps already running:

```bash
launchctl setenv GITHUB_TOKEN "$(gh auth token)"
# then fully quit + reopen Cursor
```

`/route` shell `gh` already uses keychain — no change needed for CLI.

---

## 2. Brave Search MCP (rotate + export; leave disabled until ready)

1. Open Brave Search API dashboard → **rotate / revoke** the old key that was embedded in `mcp.json`.
2. Create a new key if you still want Brave as fallback (day-to-day prefer **Exa**).
3. Export (do not write into mcp.json):

```bash
# Brave — after rotating key in Brave API dashboard
export BRAVE_API_KEY='paste-new-key-here'
# then enable brave-search in ~/.cursor/mcp.json (disabled: false)
```

4. Persist same way as GitHub (`~/.zshrc` + launch Cursor from shell, or `launchctl setenv`).
5. Edit `~/.cursor/mcp.json` → `brave-search.disabled: false` only after env is set.
6. Reload Cursor MCP panel.

Until then keep **brave-search disabled** (script sets this).

---

## 3. Verify (safe — no secret dump)

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"

# Credential literals must be 0 (env refs OK)
python3 << 'PY'
import json, re
from pathlib import Path

def scan(path: Path):
    t = path.read_text()
    hits = []
    for pat, label in (
        (r"\bgho_[A-Za-z0-9_]+", "gho_"),
        (r"\bghp_[A-Za-z0-9_]+", "ghp_"),
        (r"\bgithub_pat_[A-Za-z0-9_]+", "github_pat_"),
        (r"\bBSA[A-Za-z0-9_-]{10,}", "BSA"),
    ):
        if re.search(pat, t):
            hits.append(label)
    # env refs are fine
    print(f"{path}: literals={hits or 'NONE'}")
    if hits:
        raise SystemExit(1)

scan(Path.home() / ".cursor" / "mcp.json")
print("tipdrop exists:", (Path.home()/".cursor"/"rules"/"tipdrop-route-outsource.mdc").exists())
PY

test ! -f ~/.cursor/rules/tipdrop-route-outsource.mdc
grep -n Desktop .cursor/lazy-tool.yaml && exit 1 || echo "lazy-tool: no Desktop paths"
grep -n cemini-librarian .cursor/lazy-tool.yaml && exit 1 || echo "lazy-tool: no librarian"
```

---

## 4. Already done by agent (project tree)

| Item | Status |
|------|--------|
| Project `tipdrop-route-outsource.mdc` | deleted |
| Project `cemini-route-outsource.mdc` | deleted (global only) |
| Project identical dups `cemini-goal-skill` + `cemini-cursor-security-preflight` | deleted |
| Demote AA false: `osint-phase1-adopt-wires`, `osint-visual-deliverables`, `cemini-phase1-policy-wires` | done |
| `.cursor/lazy-tool.yaml` kb-server removed; Desktop→Projects | done |
| Project `mcp.json` cold disable + drop codebase-memory | done |
| `scripts/setup_cursor_github_mcp.sh` env-ref only | done |

## 5. Out of scope (follow-up)

- Vacuum `state.vscdb` (close Cursor first)
- Slim CLAUDE.md ritual
- Claude Code global plugins/hooks

---

## 6. After global script

1. Reload Cursor window  
2. MCP panel: github green when `GITHUB_TOKEN` is set; brave disabled until export  
3. Confirm only **one** route rule injects (`cemini-route-outsource`)
