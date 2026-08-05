# Plan — Cursor config P0/P1 cleanup (hard lane)

**WorkDir:** `/Users/claudiobarone/Projects/OSINT WORKSPACE`  
**Do not** put any API keys, tokens, or Bearer strings in files, commits, or chat.  
**Do not** run `gh auth token` and write the output into `mcp.json`.  
**Do not** commit `~/.cursor/mcp.json` or `~/.cemini/*`.

## Success criteria

1. No plaintext Brave key or GitHub Bearer in `~/.cursor/mcp.json` (env refs / wrapper only).
2. `tipdrop-route-outsource.mdc` deleted from both `~/.cursor/rules/` and project `.cursor/rules/`.
3. Project duplicate of `cemini-route-outsource.mdc` removed (keep **one** copy under `~/.cursor/rules/` only).
4. `.cursor/lazy-tool.yaml`: no `kb-server` / `cemini-librarian`; no `Desktop/OSINT` paths; conductor+exa point at Projects paths (or drop conductor if broken); keep `prod-mcp`; can keep fetch or drop (direct exa exists).
5. Cold MCP disabled (`"disabled": true`): global — playwright, brave-search (until env set), cloudflare×5, stash, stripe; project — obsidian-vault, mcp-legal-it, codebase-memory-mcp (dup), fetch optional; keep lazy-tool, exa, github (env-backed), discord-ops dry-run, chrome-devtools optional.
6. Demote `alwaysApply: false` on project: `osint-phase1-adopt-wires.mdc`, `osint-visual-deliverables.mdc`, `cemini-goal-skill.mdc`, `cemini-cursor-security-preflight.mdc`, `cemini-phase1-policy-wires.mdc` (federation copies stay global OR demote both — prefer global-only for federation rules, project-only for OSINT-specific).
7. Write operator doc `reports/audit/cursor-config-2026-08-01/OPERATOR_ENV_ROTATE.md` with paste-ready commands (no secret values).
8. Update `scripts/setup_cursor_github_mcp.sh` so it **never** embeds the token into mcp.json — use env placeholder + document `gh auth` / `export GITHUB_TOKEN=$(gh auth token)`.
9. Reindex lazy-tool if CLI available: `lazy-tool reindex --config ".cursor/lazy-tool.yaml"`.
10. Append one line to `wiki/log.md` under query/ops: config cleanup 2026-08-01 (no secrets).

## GitHub vs Brave (operator intent)

- **GitHub CLI:** already `gh auth` keyring — sufficient for `/route` shell `gh`. Prefer **not** requiring a new PAT rotate unless operator chooses refresh.
- **GitHub Cursor MCP:** remove embedded Bearer; use `"Authorization": "Bearer ${env:GITHUB_TOKEN}"` (or `GITHUB_PERSONAL_ACCESS_TOKEN`). Operator loads env from `gh auth token` (see OPERATOR doc). Optional: `gh auth refresh` if they want a new `gho_`.
- **Brave:** remove literal; `"BRAVE_API_KEY": "${env:BRAVE_API_KEY}"`; leave **disabled** until operator exports key. Document Brave dashboard rotate + export.

## Implement steps (executor)

### A. Rules (token waste)

- Delete:
  - `~/.cursor/rules/tipdrop-route-outsource.mdc`
  - `…/OSINT WORKSPACE/.cursor/rules/tipdrop-route-outsource.mdc`
  - `…/OSINT WORKSPACE/.cursor/rules/cemini-route-outsource.mdc` (keep global only)
- Demote AA false on project rules listed in success #6.
- Global: keep `cemini-route-outsource.mdc`, `cemini-projects.mdc`, demote or keep security/goal/phase1 once only under `~/.cursor/rules` (delete project duplicates of those three if identical).

### B. lazy-tool.yaml

- Remove entire `kb-server` source block.
- Change Desktop paths → `/Users/claudiobarone/Projects/OSINT WORKSPACE/...` for conductor and exa.
- Keep prod-mcp. Optionally remove fetch/exa from lazy-tool (direct exa MCP remains).

### C. Global mcp.json (redact secrets)

Edit `~/.cursor/mcp.json` carefully with python/json:

- `brave-search.env.BRAVE_API_KEY` → `"${env:BRAVE_API_KEY}"` and `"disabled": true`
- `github.headers.Authorization` → `"Bearer ${env:GITHUB_TOKEN}"` (keep url)
- Set `"disabled": true` on: playwright, cloudflare, cloudflare-docs, cloudflare-bindings, cloudflare-builds, cloudflare-observability, stash, stripe
- Keep atto enabled (no secrets in env beyond vault path)
- codebase-memory: `"disabled": true` globally OR leave one enabled — prefer disable both sides if cold

### D. Project mcp.json

- Remove `codebase-memory-mcp` entry entirely (global has it disabled).
- `"disabled": true` on: obsidian-vault, mcp-legal-it, fetch (optional), prod-mcp optional (lazy-tool covers it — disable direct prod-mcp to cut dup)
- Keep: lazy-tool, exa, discord-ops, chrome-devtools
- Fix obsidian path if left enabled: Projects not Desktop — but disabled is fine

### E. setup_cursor_github_mcp.sh

Rewrite to write env-ref config only; stop writing token into mcp.json; stop auto-writing PAT file unless `--write-pat-file`. Print instructions to export from `gh auth token`.

### F. OPERATOR_ENV_ROTATE.md

Must include paste-ready blocks:

```bash
# GitHub for Cursor MCP (uses existing gh auth — no new PAT required)
export GITHUB_TOKEN="$(gh auth token)"
# optional refresh if you want a new oauth token:
# gh auth refresh -h github.com -s gist,read:org,repo,workflow

# Persist for GUI apps (Cursor) — pick one:
# launchctl setenv GITHUB_TOKEN "$(gh auth token)"   # session; or use ~/.zshrc + restart Cursor from terminal
```

```bash
# Brave — after rotating key in Brave API dashboard
export BRAVE_API_KEY='paste-new-key-here'
# then enable brave-search in ~/.cursor/mcp.json (disabled: false)
```

Also: add to `~/.zshrc` the GITHUB_TOKEN export; restart Cursor from that shell OR use a LaunchAgent — document clearly.

### G. Out of scope this run

- Do NOT vacuum state.vscdb (operator closes Cursor first).
- Do NOT slim CLAUDE.md ritual (follow-up).
- Do NOT edit Claude Code global plugins/hooks (follow-up).
- Do NOT commit secrets. Prefer not committing mcp.json at all.

## Verify

```bash
# must print 0 credential literals (except ${env:…})
python3 -c "..."  # scanner: fail if gho_/ghp_/BSA literal in mcp.json
test ! -f ~/.cursor/rules/tipdrop-route-outsource.mdc
grep -n Desktop .cursor/lazy-tool.yaml && exit 1 || true
grep -n cemini-librarian .cursor/lazy-tool.yaml && exit 1 || true
```
