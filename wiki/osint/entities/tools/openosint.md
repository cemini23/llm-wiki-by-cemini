---
title: "OpenOSINT — AI OSINT agent (REPL / MCP / CLI)"
type: entity
tags: [tool, reference-only, osint, mcp, cybersec, k88, phase-0-complete, eval-mismatch]
keywords: [openosint, mcp, repl, shodan, virustotal, holehe, sherlock, anthropic, recon]
related:
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/librarian-server-architecture.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
phase_0_verdict: NO-GO 2026-05-31 — product misidentified in K88 eval (no WebGL/geospatial dashboard); duplicates Exa/brave + discrete API recon tools; laptop-only optional recon bundle via cybersec-wiki if operator wants bundled MCP
adoption_status: PHASE-0-COMPLETE 2026-05-31
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 Adopt **overturned** after Phase-0 (eval description wrong)
- @concepts/librarian-server-architecture.md — not a kb-server/conductor substitute
- @concepts/tool-evaluation-framework.md — eval-mismatch flag for future v5 batches

## Raw Concept

- **Repo**: `github.com/OpenOSINT/OpenOSINT`
- **License**: MIT `[CONFIRMED 2026-05-31]` — root `LICENSE`; optional paid **Commercial License** for closed-source SaaS without attribution (core MIT unchanged)
- **PyPI**: **openosint 2.18.0** — `pip install openosint` works; Python ≥3.10
- **Prompted by**: K88 eval claimed "Palantir-style 60fps WebGL map" with GDELT/aircraft/satellite — **Phase-0 found this description does not match the repo**

## Narrative

OpenOSINT is an **Anthropic-tool-use OSINT agent** with four surfaces: interactive REPL, direct CLI subcommands, MCP server (`openosint-mcp`), and a FastAPI **Web UI** (v2.12+) for chat-style investigations. The model chains **16 modular recon tools** (email/username/breach/WHOIS/IP/DNS/dorks/paste/phone/Shodan/VirusTotal/Censys/IP2Location/AbuseIPDB/GitHub). It is **not** a geospatial dashboard product.

### Phase-0 audit (2026-05-31)

Repo cloned to `/tmp/ph0-openosint/`; maturity via `gh api`.

#### License — claim vs actual

| Claim | Actual |
|-------|--------|
| MIT Adopt | **MIT CONFIRMED** — standard LICENSE file. `COMMERCIAL-LICENSE.md` adds paid tier for closed-source commercial use without attribution; **does not affect** MIT open-source / academic / personal use |

No copyleft; IP-sale-safe for reference patterns. Commercial upsell is a process note, not a license blocker for internal laptop eval.

#### Maturity — observed

| Metric | Observed | Note |
|--------|----------|------|
| Stars | **292** | High for ~3-week-old project |
| Forks | 60 | Active community |
| Open issues | 2 | Low |
| Created | **2026-05-06** | Very young (~25 d at audit) |
| Last push | **2026-05-30** | Daily cadence |
| Version | **2.18.0** (PyPI + repo) | Classifier: **Production/Stable** (author claim) |
| Python modules | 30 under `openosint/` | Substantive agent + MCP, not a landing page |

Fast iteration velocity; treat "Production/Stable" as author marketing until longer track record.

#### Failure-mode probe — OSINT dashboard / librarian class

**1. Product identity mismatch (load-bearing).** K88 eval and initial OSINT stub described WebGL map + GDELT/aircraft/satellite feeds. **Repo grep: zero matches** for `webgl`, `gdelt`, `mapbox`, `leaflet`, `aircraft`, `satellite`. Actual product = AI agent orchestrating classic recon APIs + external CLI binaries. **The v5 eval Adopt rationale was based on a hallucinated or conflated product.**

**2. Librarian / conductor overlap.** kb-server serves wiki RAG; conductor routes cross-wiki queries; Exa + fetch + brave-search cover external URL research for this workspace. OpenOSINT does **not** index local wiki corpora and is **not** a drop-in librarian component.

**3. Operational dependencies.** Full function requires:
- **External binaries** (optional per tool): `holehe`, `sherlock`, `sublist3r`, `phoneinfoga`
- **API keys** for premium tools: `ANTHROPIC_API_KEY` (agent), `HIBP_API_KEY`, `SHODAN_API_KEY`, `VIRUSTOTAL_API_KEY`, `CENSYS_API_ID/SECRET`, `IP2LOCATION_API_KEY`, `ABUSEIPDB_API_KEY`
- **Ollama** path for offline model (degraded vs Claude tool-use quality)

Missing keys return descriptive errors — graceful, but **high setup tax** vs using Exa/brave directly in Cursor.

**4. MCP surface vs lazy-tool pattern.** Ships standalone MCP (`openosint-mcp`) with 16 tools. Adding it globally duplicates recon tooling already available piecemeal (Shodan MCP elsewhere, playwright browser, finance social readers). **lazy-tool catalog** prefers proxying known capabilities — another full agent MCP increases attack surface and key-management burden.

**5. Scope / boundary.** README + `DISCLAIMER.md`: **authorized security research only**. Fits cybersec-wiki engagement tradecraft, **not** CeminiSuite prod trading path or 24/7 librarian serving.

**6. Web UI optional extra.** `[web]` extra pulls FastAPI + uvicorn + **playwright** — overlaps Cursor built-in browser rule; do not install `[web]` or `[all]` on OSINT laptop by default.

#### Comparison vs existing Cemini coverage

| Need | Existing path | OpenOSINT adds? |
|------|---------------|-----------------|
| Wiki / brief research | kb-server, conductor, grep | No |
| External URL facts | Exa, fetch, brave-search | Partial overlap |
| Financial social | finance-skills readers | No |
| Browser verify | Cursor built-in browser | Web UI redundant |
| Pentest recon bundle | Discrete tools + cybersec skills | **Maybe** — bundled MCP convenience only |

### Decision — NO-GO (OSINT wiki Adopt overturned)

**Do not adopt** on librarian, prod, or egress. **Do not** position as geospatial entity tracker — that capability is not in this repo.

**Optional escape hatch (cybersec-wiki only):** if operator runs authorized recon engagements and wants a **laptop-only bundled MCP**, `pip install openosint` + configure keys/binaries is acceptable as **Reference / optional MCP** — track on `@cybersecurity-wiki` if pursued, not OSINT prod stack.

**Eval hygiene:** flag K88 OpenOSINT row in `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` as **Adopt overturned → NO-GO (product mismatch)** for future v5 prompt tuning.

## Snippets

> "OpenOSINT is an AI agent for Open Source Intelligence with three interfaces: an interactive terminal REPL, a direct CLI, and an MCP server … plus a browser-based Web UI." [Source: OpenOSINT/OpenOSINT README.md, cloned 2026-05-31]

> "Personal, academic, and open source use is already covered by the MIT License — no purchase needed." [Source: OpenOSINT COMMERCIAL-LICENSE.md]

## Dead Ends

- **K88 "Palantir-style dashboard" adopt path** — repo contains no geospatial/WebGL/GDELT stack; librarian deployment plan abandoned after clone audit 2026-05-31.
