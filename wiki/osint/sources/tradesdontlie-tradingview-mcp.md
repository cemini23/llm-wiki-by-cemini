---
title: "tradesdontlie/tradingview-mcp — TradingView Desktop MCP Bridge (JavaScript, MIT-file/NOASSERTION-aggregator, 2.4k★) ⚠️ Family C TOS-conflict"
type: source
tags: [github, mcp-server, tradingview, chrome-devtools-protocol, pine-script, license-disputed, family-c-tos-conflict, ip-sale-flag, gemini-dr-wave4, defer-or-steal-from]
keywords: [tradingview-mcp, tradesdontlie, chrome-devtools-protocol, cdp, electron-app-bridge, pine-script-v6-prototyping, license-disputed-mit-vs-noassertion, family-c-tos-conflict-pattern, automated-trading-tos-violation-warning, mit-trademark-disclaimers-tradingview-anthropic, account-termination-risk, ui-automation-brittleness]
clusters: [llm-agents, dev-tooling, market-data]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/wiki-tooling-evaluation.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A URL 20 — **Gemini DR brief recommended Adopt; anti-hallucination spot-check 2026-04-29 reclassified to Defer (TOS legal review) or Steal-from (CDP pattern only)**. This dedicated source page formalizes the reclassification.
- @concepts/ip-sale-readiness.md — **Worked example of Family C TOS-conflict-via-clean-license-code pattern** (added to ip-sale-readiness 2026-04-29 as a direct response to this finding). The LICENSE file is MIT, the GitHub aggregator shows NOASSERTION because of the trademark disclaimers, AND the README explicitly warns about TradingView TOS conflicts for automated-trading use.
- @concepts/high-signal-paper-patterns.md — rubric: license-dispute (file MIT vs aggregator NOASSERTION) + TOS-conflict warnings = automatic Family-C flag per the rubric's negative-signals section

## Raw Concept

- **URL**: https://github.com/tradesdontlie/tradingview-mcp
- **Type**: Open-source MCP server / JavaScript bridge to TradingView Desktop
- **License**: **DISPUTED**: LICENSE file is MIT (Copyright 2026 tradesdontlie); GitHub repo aggregator shows License: **"Other (NOASSERTION)"** (because of additional trademark notices below the MIT text). The README also includes substantial TRADEMARK NOTICE + DISCLAIMER sections about TradingView Inc. and Anthropic PBC.
- **Stars / Forks (Exa-verified 2026-04-29)**: 2,362 ★ / 1,230 forks (note: high fork:star ratio of ~52% — unusual; possibly forked-as-template by many users)
- **Stack**: JavaScript 98.1% / Shell 1.2% / Batchfile 0.5% / VBScript
- **Org**: tradesdontlie (1 contributor)
- **Created**: 2026-03-29; **Last push**: 2026-04-04 (active 6 days; then quiet)
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 20); reclassified during anti-hallucination spot-check; promoted with downgrade 2026-04-30
- **Read status**: read-skim (Exa-fetched LICENSE + README + Gemini brief evaluation)

## Narrative

### What it is — and what it claims to be

An MCP server that uses **Chrome DevTools Protocol (CDP)** to bridge an AI agent (Claude Code etc.) to a **locally running instance of the TradingView Desktop application**. The Electron-based TradingView Desktop must be launched with `--remote-debugging-port=9222`, after which the LLM gets "eyes and hands" on the TradingView UI: write/inject/compile Pine Script v6 code, navigate charts, read indicator values (RSI, MACD), draw trend lines, monitor price ticks.

**The author's own framing**: the tool processes data purely locally and "functions as a research assistant, not an automated trading bot."

### The license dispute (Family C TOS-conflict pattern)

Per `@concepts/ip-sale-readiness.md` Family C — the **first worked example** of the new TOS-conflict pattern:

1. **The code license is MIT** — Copyright 2026 tradesdontlie; standard MIT text; clean for redistribution.
2. **GitHub's aggregator parser flags NOASSERTION** because the LICENSE file appends substantial non-license text:
   > "ADDITIONAL NOTICE: This software is not affiliated with, endorsed by, or associated with TradingView Inc. … This license applies to the source code of this project only and does not grant any rights to TradingView's software, data, or intellectual property."
   > "TRADEMARK NOTICE: The MIT license above applies to the source code in this repository only. It does not grant any rights to the trademarks, logos, or intellectual property of TradingView Inc. or Anthropic, PBC."
3. **The README itself warns**:
   > "Performing automated trading or algorithmic decision-making using extracted data" may conflict with TradingView's Terms of Use. **For Cemini's algorithmic-trading use case, this is a direct conflict.**

The architectural problem: even though the code is MIT, **TradingView's TOS — to which Cemini has no direct license relationship — applies to the use of TradingView's data**. Running Cemini against extracted-via-CDP TradingView data is the use case the README explicitly warns against.

### Cemini-side reclassification

**Original Gemini DR verdict**: Adopt (Workflow).
**Wave 4A canonical brief reclassification (2026-04-29)**: Defer (TOS legal review) OR Steal-from (CDP pattern only).
**This page formalizes**: Steal-from for the **Chrome DevTools Protocol bridge pattern**; Defer for direct deployment.

The valuable extraction:
- **CDP-against-Electron-apps pattern** is genuinely interesting and reusable. Useful for any Electron-based vendor app Cemini wants to programmatically inspect (e.g., a hypothetical Bloomberg Terminal Desktop or similar).
- **Pine Script v6 compilation feedback loop** (push code, execute, read errors) is a useful workflow pattern, separate from TradingView specifically.

The do-not-deploy parts:
- **The TradingView data binding itself** — Cemini's algorithmic-trading deployment must use a TOS-cleared data source (Polygon, Coinbase, Alpaca already pass this).

### Risks & open questions

1. **TradingView account-termination risk** — the brief notes: "Deploying this tool risks immediate account bans; it should only be operated using a secondary, non-mission-critical account." Even Workflow use against the user's primary TradingView account carries termination risk.
2. **CDP brittleness** — UI automation against an Electron app's DOM is fragile. "Any minor update pushed to TradingView's Electron DOM structure will instantly break the 78 specialized MCP tools, requiring constant maintenance."
3. **License clarity** [NEEDS VERIFICATION 2026-04-30] — re-check the LICENSE file periodically. If the trademark/disclaimer text is removed in a future commit, the GitHub aggregator may revert to "MIT", but the underlying TOS-conflict still applies.
4. **Headless deployment impossibility** — TradingView Desktop is a graphical Electron app requiring display servers (X11/Wayland or macOS WindowServer). Cannot be deployed on cemini-prod (headless Hetzner host). **Confirms Workflow scope only**, even before TOS analysis.
5. **Active period was brief** — 6 days of pushes (2026-03-29 to 2026-04-04). Project may have stabilized OR may have been abandoned. Pre-Workflow-adoption check: verify the latest commit still works against current TradingView Desktop.

### Cemini-side adoption assessment

**Decision: Steal-from + Defer**. Do not deploy this project. Extract the CDP-against-Electron-apps pattern to a Cemini-internal note for future reference.

Concrete next-steps:
1. **Skip direct adoption**. Flag in `concepts/ip-sale-readiness.md` Family C as the worked example (already done 2026-04-29).
2. **If Pine Script prototyping is needed**: use TradingView's official Pine Editor in the browser (manual; doesn't trigger TOS concerns) rather than this CDP bridge.
3. **If CDP-against-Electron pattern is wanted later**: clone the repo, study the architecture, write Cemini-specific implementation against a TOS-cleared target. Don't reuse the TradingView-specific data binding.
4. **Pre-emptive legal note**: if Cemini ever does wire a TradingView data source, route via Polygon's TradingView-data-license-resold path (if available), not via this CDP bridge.

### Citation

> tradesdontlie. (2026). *TradingView MCP Bridge*. https://github.com/tradesdontlie/tradingview-mcp (LICENSE file: MIT 2026 tradesdontlie; GitHub aggregator: NOASSERTION; README warns automated-trading use may violate TradingView TOS; 2,362 stars / 1,230 forks; 6-day active period 2026-03-29 to 2026-04-04)

## Snippets

> **The TOS-conflict warning (the load-bearing finding)**:
>
> "This tool uses Chrome DevTools Protocol to programmatically interact with the TradingView Desktop app, which may conflict with those terms. … Performing automated trading or algorithmic decision-making using extracted data … Connecting to TradingView's servers or infrastructure (all access is via the locally running Desktop app) … Market data accessed through this tool remains subject to exchange and data provider licensing terms. **Do not redistribute, store, or commercially exploit any data obtained through this tool.**" [Source: https://github.com/tradesdontlie/tradingview-mcp README, retrieved 2026-04-29 via Exa]

> **The trademark/disclaimer text (cause of NOASSERTION on GitHub aggregator)**:
>
> "ADDITIONAL NOTICE: This software is not affiliated with, endorsed by, or associated with TradingView Inc. Users are solely responsible for ensuring their use complies with TradingView's Terms of Use and all applicable laws. This license applies to the source code of this project only and does not grant any rights to TradingView's software, data, or intellectual property. TRADEMARK NOTICE: The MIT license above applies to the source code in this repository only. It does not grant any rights to the trademarks, logos, or intellectual property of TradingView Inc. or Anthropic, PBC." [Source: https://github.com/tradesdontlie/tradingview-mcp/blob/main/LICENSE, retrieved 2026-04-29 via Exa]
