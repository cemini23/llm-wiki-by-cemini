# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (2026-05-15 ~11:15am EDT — K46 shipped + 6 adoptions + server aligned)

### K46 — COMPLETE
- Committed (2522830) & pushed to main
- 4 source pages + 5 tool entities + 1 upgrade + 2 cross-wiki routes + 9 bidirectional fixes
- Lint: 0 K46-introduced gaps, 10 pre-existing bidirectional, 4 orphans, 34 cross-wiki dangling

### Adoptions — COMPLETE
- **turbovec** — core lib + Python bindings both build & pip-installed. Fix: `-undefined dynamic_lookup` in build.rs (standard macOS extension pattern) instead of linking Python3.framework. Install date: 2026-05-15
- **octocode-mcp** — installed globally (npm), MCP server verified running. Install date: 2026-05-15
- **claude-red** — 58 SKILL.md files installed to ~/.claude/skills/claude-red/. Install date: 2026-05-15
- 6 briefs written → server (/opt/cemini/briefs/): turbovec, octocode-mcp, claude-red, a-stock-data, synth-subnet, beever-atlas

### Server context-saving alignment — COMPLETE
- claude-mem@thedotmack plugin enabled in /root/.claude/settings.json
- CLAUDE_CODE_DISABLE_AUTO_MEMORY="1" set
- /opt/cemini/CLAUDE.md: Session-start ritual + hot.md pattern prepended (250→278 lines)
- /opt/cemini/hot.md created (Step 141/143 state, stack health, pending briefs)
- /opt/cemini/.gitignore: hot.md added

### Workspace state
- Inbox: CLEAN
- Git (OSINT): clean (all committed + pushed)
- Git (CCC): clean
- Git (Cybersec): has Claude-Red page
- Tools installed: ~/tools/turbovec, ~/tools/claude-red, octocode-mcp (global)

### What is NOT done
- Outlier Weekly Issue 2 full refresh: operator market decision + full numerical refresh pending Day 12 (~May 24-25)
- Server brief review: a-stock-data, synth-subnet, beever-atlas staged for server-Claude review

### Next session — resume options
1. Outlier Weekly Issue 2 operator market decision + Day-10 prep
2. Server-side brief review (a-stock-data pipeline, synth-subnet CRPS, beever-atlas patterns)
3. New direction from user
