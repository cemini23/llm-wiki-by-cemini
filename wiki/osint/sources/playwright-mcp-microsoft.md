---
title: microsoft/playwright-mcp — DOM Accessibility Tree MCP Server (TypeScript, Apache-2.0)
type: source
tags: [llm-tooling, mcp, browser-automation, playwright, dom-accessibility, chromium, firefox, webkit, workflow-adopt, cemini-defer, ip-sale-clean]
keywords: [playwright-mcp, accessibility-tree, dom-snapshot, structured-snapshot, headless-chromium, headless-firefox, mcp-server, javascript-heavy-pages, sec-edgar-parsing, bot-detection-bypass, kalshi-scraping]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - concepts/ip-sale-readiness.md
  - entities/frameworks/fastmcp.md
  - sources/agent-browser-vercel-labs.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, ingest-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; classified Defer-Cemini / Adopt-Workflow
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent
- @concepts/librarian-server-architecture.md — relevant: deploying playwright-mcp on the CPX21 librarian server is rejected (~2.6 GB RAM headroom is insufficient for headless Chromium alongside Ollama and llm-wiki-compiler). Strict server-class separation required
- @concepts/ip-sale-readiness.md — Apache-2.0 clears IP-sale checks (Exa-verified 2026-04-28: 31638 ★)
- @entities/frameworks/fastmcp.md — Cemini's MCP layer; if playwright-mcp ever moves from Workflow-only to production, it would attach to the existing FastMCP via a separate Docker container

## Raw Concept

- **URL**: https://github.com/microsoft/playwright-mcp
- **Type**: Open-source repository / MCP server
- **License**: Apache-2.0 (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 31638 ★ / 2583 forks / 26 open issues
- **Stack**: TypeScript 62.3%, JavaScript 31.8%, Dockerfile 5.9%
- **Org**: microsoft (Microsoft official Playwright team — high authoritative signal)
- **Created**: 2025-03-21; **Last push**: 2026-04-27; **Latest release**: v0.0.71 (2026-04-27)
- **Releases**: 61 published
- **Homepage**: https://www.npmjs.com/package/@playwright/mcp
- **Topics**: mcp, playwright

## Narrative

### What it does
The Playwright MCP server bridges LLMs with the Playwright browser-automation engine. Diverging from fragile pixel-screenshot-based approaches that rely on multimodal vision models, this server computes and exposes the DOM's **structured accessibility tree** directly to the LLM. Translates highly dynamic, JavaScript-heavy web interfaces into deterministic, structured data formats — empowering vision-less models to execute UI interactions, parse embedded HTML tables, and traverse complex visual layouts with absolute predictability.

### Why Adopt-for-Workflow / Defer-for-Cemini

Two-tier recommendation reflecting the dual hardware envelope:

**Adopt-for-Workflow (laptop)**: 
- Microsoft official, Apache-2.0, 31k stars, active maintenance.
- Local laptop has ample resources to run headless Chromium + Playwright alongside Claude Code.
- Phenomenal accelerator for laptop-side scraper development on JavaScript-heavy financial sites (Kalshi, SEC EDGAR's React-based search interface, broker-journal extraction).
- Replaces brittle Selenium scripts and screen-scraping with deterministic accessibility-tree parsing.

**Defer-for-Cemini (Hetzner production)**:
- Headless Chromium alone consumes 300 MB – 1.5 GB resident per active tab.
- Cemini's 7 GB envelope is already contested by Postgres + Polars + Redis + Python.
- Production deploy requires draconian Docker memory caps + sustained stress-tests proving no OOM-kill under load.
- **Pre-promotion gates**:
  1. Soak-test in a separate Docker container with `deploy.resources.limits.memory: 1.5g` cap for 14 consecutive days.
  2. Verify aggressive restart policies (e.g., `restart: unless-stopped` + healthcheck) reset the process if it leaks beyond cap.
  3. Programmatic tab-killing logic — no long-lived tabs.
  4. Monitor PostgreSQL latency during tab spawn — ensure no IO contention on Hetzner SSD.
  5. Confirm production stability before promoting from "isolated container" to "production critical path."

### Where it falls short

1. **Wiki / librarian server fit: ❌** — booting Chromium alongside Ollama and Node.js on the 4 GB CPX21 server will predictably OOM-kill the llm-wiki-compiler daemon. Don't deploy on the librarian.
2. **Long-running memory leaks** — Playwright automation scripts are notorious for memory leaks during prolonged 24/7 background execution. If integrated into the production ingest layer, the dedicated Docker container needs aggressive restart policies, explicit connection timeouts, and programmatic tab-killing logic.

### Integration vector

**Laptop (immediate adopt):**
```
1. npm install -g @playwright/mcp  (or use npx)
2. Configure Claude Code to bind to the MCP server endpoint
3. Use for:
   - Kalshi market scrapes
   - SEC EDGAR React-search-page parsing
   - Broker journal extraction (PDF-via-print + DOM scrape)
   - Academic paper PDFs trapped behind aggressive JS rendering
   - Any JS-heavy site where requests + BeautifulSoup gives 0 useful output
```

**Cemini production (deferred):**
```
1. Deploy as separate Docker container in the 40-container swarm
2. Strict memory cap in docker-compose.yml: limits.memory: 1.5g
3. Healthcheck + restart: unless-stopped
4. Communicate with Cemini's FastMCP orchestrator over MCP protocol (no HTTP coupling)
5. Replace the requests + BeautifulSoup calls in ingest layer for JS-obfuscated financial feeds
```

### Risks & open questions

1. **Accessibility-tree truncation on long pages** [NEEDS VERIFICATION] — Gemini flagged: "Rigorous verification is required to determine if the structured accessibility snapshot algorithm dynamically truncates elements when parsing extremely long web pages (such as monolithic SEC 10-K filings), which would result in critical context loss for the LLM." Test against a known SEC 10-K before promoting from Workflow Adopt to Cemini Adopt.
2. **Memory leak resistance under 14-day soak** [NEEDS VERIFICATION] — gating verification for production promotion.
3. **No SBOM for transitive dependencies** — Apache-2.0 at top level verified; transitive npm dependencies must be `npm audit` + `license-checker`'d before production.

## Snippets

> "Playwright MCP server" [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]

> "Defer (for Cemini) / Adopt (for Workflow). Adopt the software immediately within the local development environment to vastly accelerate the prototyping of research scrapers. Defer production integration until the container undergoes rigorous, sustained Docker memory-capping stress tests to guarantee the Chromium instance will not trigger OOM kills on the Hetzner hardware." [Source: Gemini DR report, URL 13]

> "Standard Playwright instances routinely consume between 300 MB and 1.5 GB of RAM per active tab. Given Cemini's strict ~7 GB envelope (which is already fiercely contested by Postgres, Polars, Redis, and Python), integrating this server demands draconian memory limits (deploy.resources.limits.memory) hardcoded into the docker-compose.yml." [Source: Gemini DR report, URL 13 — Cemini integration vector]
