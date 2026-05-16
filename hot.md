# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Architecture — what runs where (deployment boundary)

Three machines, split by function. Anything needing 24/7 uptime → Hetzner servers, never the laptop.
- **Laptop** (this workspace) — wiki authoring/curation; canonical git source. Can be powered off any time; only curation pauses, nothing serving breaks.
- **cemini-librarian** — 24/7 knowledge serving: kb-server (wiki RAG/MCP), Ollama (embeddings), stash. Synced wiki copy + raw-source canon (`/opt/cemini-bulk`) live here.
- **cemini-prod** (`/opt/cemini`) — 24/7 CeminiSuite trading stack (the brain consuming the library).
Rule: any wiki-serving component belongs on cemini-librarian. Laptop installs = benchmark/workflow only. Codified in CLAUDE.md "Deployment boundary" section.

## Position (2026-05-15 evening — K47 + K48 shipped)

### K47 — COMPLETE (commits f92ee8c, 48281f5, 4194d08, ea4ef42)
- 52-URL "Tool Evaluation and Wiki Fit" ingest; fingerprint-suite + LEANN local adoptions.
- Librarian deploy + benchmark: turbovec + LEANN installed on cemini-librarian; benchmarked vs kb-server brute-force (943-vector corpus). DECISION: NO-GO on wiring either into kb-server — concept page `kb-server-retrieval-scaling.md`. Trigger to revisit: >2000 chunks → sqlite-vss first. kb-server healthy, untouched.

### K48 — 13F ingest COMPLETE (commit 9455c13)
- 11 pages: source + 9 fund entity pages + smart-money concept. Inbox leftovers (by design): `klarman holdings.jpeg` (cropped Baupost dup), `tepper 2.jpeg` (unidentified — skip). No Third Point data supplied.

### K48 — weekly article searches COMPLETE (4 streams; commits 6192266, 6cc8fdd)
- Tier-2 arXiv sweep → `wiki/sweeps/2026-05-15.md` (5 clusters, 19 candidates).
- Ingested 7 source pages + 2 entity stubs: 4 arXiv (grep-harness, FPILOT RL-trading, coordination-layer, Polymarket fill-side) + 3 news clusters (critical-minerals/Pentagon, Polymarket insider-trading, crypto illicit-finance tracing) + T3 FCU + Arkham stubs.
- grep-vs-vector paper (arXiv:2605.15184) independently corroborates the K47 kb-server NO-GO.
- Newsletter research: Polymarket rare-event candidates surfaced (top pick "Iran war-powers resolution by May 31", 11%) — handed to Outlier Weekly track, not ingested.
- Note: subagents hit a usage limit mid-task (reset 7:30pm EDT); searches done in main thread.

### Workspace state
- Git (OSINT): clean, pushed (6cc8fdd). Lint: 0 bidirectional gaps across K47+K48.
- Tools: ~/tools/{turbovec,claude-red,fingerprint-suite}, octocode-mcp (global), leann (pip). Librarian: /opt/turbovec, /opt/leann-venv (staged, not wired).

### What is NOT done / pending
- Server-side Phase-0 review of awesome-finance-skills + pm-claude-skills briefs (server-Claude).
- `tepper 2.jpeg` unidentified fund — needs user ID to ingest.
- Outlier Weekly Issue 2 full refresh pending Day 12 (~May 24-25).
- arXiv sweep's other 15 candidates + market-news SKIM items — descriptive only, not ingested.

### Next session — resume options
1. Outlier Weekly next issue (Iran war-powers candidate)
2. Server-side brief review
3. New direction from user
