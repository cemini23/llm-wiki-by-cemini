# Cemini OSINT Research Workspace

A local knowledge hub for OSINT and financial research — an LLM-curated, human-read wiki with helper scripts. This repo holds the **schema, the wiki, and the tooling**. Raw sources live in cold storage after ingest; there is **no 24/7 librarian server** (decommissioned 2026-06-14).

Welcome. If you are opening this tree for the first time, start with `CLAUDE.md`, then skim `wiki/index.md` and `ROADMAP.md`.

## What's tracked

| Path | Role |
|------|------|
| `CLAUDE.md` | Schema — how agents and humans operate this workspace |
| `ROADMAP.md` | Active workstreams, decisions, and open questions |
| `LESSONS.md` | Meta-lessons about *how we work* (distinct from `wiki/log.md`) |
| `wiki/` | The library: `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`, `meta/`, `sweeps/` |
| `scripts/` | Lint, ingest gates, digests, Phase-0 adopts, archive-to-egress helpers |
| `agents/` | Agent harnesses (e.g. `devfun-poker-arena/` — tracked briefs + examples) |
| `.cursor/` | Cursor rules + federation skills (`/goal`, `/route`, `to-issues`, `grill-with-docs`, …) |

## What's not tracked (and why)

- **`research to be indexed/`** — transient drop zone for new sources (gitignored)
- **`briefs/`** — deliverables staged for claude.ai or CeminiSuite (gitignored)
- **`hot.md`** — session-state cache across compaction (gitignored)
- **`.local/`** — SSH targets, local reports, optional datasets (gitignored)
- **`.claude/settings.local.json`**, **`.DS_Store`**, **`__pycache__/`** — local tooling cruft

## Architecture

1. **Raw sources** — immutable. Drop into `research to be indexed/` → ingest → archive with `scripts/archive_raw_to_egress.sh` to **`cemini-egress-fi:/opt/cemini-bulk/research/osint/`**. Older pages may still cite deleted `cemini-librarian:` paths as historical provenance only.

2. **The wiki** (`wiki/`, tracked) — LLM-written, human-read, cross-linked markdown. **Canonical on laptop git.** Sibling federation wikis live under `~/Projects/`.

3. **The schema** (`CLAUDE.md`) — how the LLM runs the wiki.

4. **Trading fleet (not this repo's write surface)**
   - **`cemini-prod`** — CeminiSuite (`/opt/cemini`)
   - **`cemini-egress-fi`** — Helsinki order egress (HL + PM) + federation raw-source cold store
   - **`cemini-librarian`** — **deleted** — see `wiki/meta/librarian-decommission-2026-06-14.md`

kb-server / stash / lazy-tool `kb_search` stay offline until librarian is restored. Query the wiki with Read/grep locally; use Exa for external gaps.

## Quick start

```bash
# Wiki health
python3 scripts/wiki_lint.py

# Gap detection (Tier 1)
python3 scripts/wiki_gap_detect.py

# Pre-distribution brief check
python3 scripts/skill_audit.py briefs/<file>.md

# Ingest session gate (before commit)
python3 scripts/ingest_session_gate.py
```

**Task routing (`/route`):** scripts live in private [`agent-toolkit`](https://github.com/cemini23/agent-toolkit) (`~/Projects/agent-toolkit`, `ROUTE_KIT`). TipDrop workspace-kit is redirect-only for route.

## Related repos

| Project | Path (laptop) |
|---------|----------------|
| **CeminiSuite** | `~/Projects/CeminiSuite` |
| **CCC (Cursor / Claude Code meta-wiki)** | `~/Projects/Cemini claude code CCC` |
| **Federation hub** | `~/Projects/cemini-federation-hub` |
| **agent-toolkit** (`/route` host) | `~/Projects/agent-toolkit` |
| **Atto** | `~/Projects/atto` · [youratto.com](https://youratto.com) |
| **GuruWatcher** | `~/Projects/GuruWatcher` · [guruwatcher.com](https://guruwatcher.com) |

Public domain wikis and the full alias table live in `CLAUDE.md` → Related Wikis.

## Collaborators

**New here?** Read in order:

1. **`CLAUDE.md`** — ingest, query, lint, distribution
2. **`wiki/index.md`** + **`wiki/log.md`** — catalog and recent ops
3. **`.cursor/README.md`** — MCP setup (turn **lazy-tool On** when this folder is open)

**Keep private (gitignored):** `briefs/`, `.local/`, `research to be indexed/`. Never commit secrets or SSH targets.

**Lab / cyber briefs:** stage under `Cybersecurity wiki/briefs/` (local abliterated lab). TipDrop/David kit is retired as a brief destination (2026-08-05).

**Before pushing:**

```bash
python3 scripts/wiki_lint.py
python3 scripts/ingest_session_gate.py
```

## Support

Thank you for your interest — and for any support, large or small. Tips and kind words both help keep Cemini research and tooling moving.

Voluntary tips fund open research and public tooling. **Donation-only addresses** — not trading or production wallets. Canonical copy: [CCC SUPPORT.md](https://github.com/cemini23/cemini-claude-code-CCC/blob/main/SUPPORT.md).

| Chain family | Address |
|--------------|---------|
| **X Money** (fiat, US) | Request [@Cemini23](https://x.com/Cemini23) in the X app — scan the Request QR |
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |
| **Hyperliquid** (referral) | [app.hyperliquid.xyz/join/CEMINI23](https://app.hyperliquid.xyz/join/CEMINI23) |

If you’d rather follow along or try something we ship:

- Newsletter — [Outlier Weekly](https://outlierweekly.substack.com) (Substack)
- Genealogy kit — [youratto.com](https://youratto.com)
- Newsletter parameter alerts — [guruwatcher.com](https://guruwatcher.com)
- X: [@Cemini23](https://x.com/Cemini23)
- Public agent meta-wiki — [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)

We’re grateful you’re here. Thank you for your support.
