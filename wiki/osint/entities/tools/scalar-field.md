---
title: "Scalar Field — YC Spring 2025 agentic trading desk (Reject, K55)"
type: entity
tags: [entity, tool, agentic-trading, yc-spring-2025, closed-source, commercial-saas, reject, competitive-intel, k55]
keywords: [scalar-field, scalarfield.io, yc-spring-2025, agentic-trading-desk, closed-source-saas, langgraph-incompatible, vendor-lock-in, competitive-intelligence]
related:
  - sources/multi-wiki-tool-eval-19url-2026-05-20.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-20
updated: 2026-05-20
---

## Relations

- @sources/multi-wiki-tool-eval-19url-2026-05-20.md — K55 tool eval URL 1, **Reject**
- @concepts/cemini-license-posture.md — closed-source SaaS exemplar

## Raw Concept

- **URL**: `https://scalarfield.io/`
- **License**: NO LICENSE FOUND (closed-source commercial)
- **Stack**: agentic terminal SaaS
- **Maturity**: Y Combinator Spring 2025 cohort; active commercial entity
- **K55 verdict**: **Reject** for all 7 surfaces.

## Narrative

YC Spring 2025 company building an "AI Agentic Trading Desk" — a closed-source competitor to what Cemini is itself building. Eval rejection is straightforward (no open-source license, no self-host path, proprietary endpoints). Recorded primarily as **competitive-intelligence** documentation.

### Per eval description

> "Scalar Field platform is designed as an agentic terminal capable of running compute-heavy backtests, parsing fundamental datasets, and chaining multi-hop workflows for autonomous execution across equities and prediction markets ... agent-driven execution models, wherein the terminal persists memory across sessions and autonomously reorganizes data based on new market signals."

### Why this matters as competitive intelligence

- Validates that the market is converging on the agentic-trading-desk pattern (memory persistence + multi-hop workflows + autonomous execution) — same direction Cemini is going.
- Validates the demand surface: equities + prediction markets, agent-driven, terminal-style UX. Cemini covers prediction markets explicitly; equities is a future expansion surface.
- YC backing implies real capital + GTM machinery; this is a real competitor for the same market thesis.

### Differentiation Cemini retains

- **Self-host**, no vendor lock-in
- **Open architecture** (wiki as long-term memory, conductor MCP)
- **Specific verticals** (Polymarket + weather + sports + LP-rewards farming + DEX perps) vs Scalar Field's broader "any market" framing

### K55 eval verdict (verbatim)

> "The complete absence of an open-source license or verifiable codebase mandates immediate rejection from the technological stack ... without the ability to self-host the prediction layer or manipulate the source code to interface with the local LangGraph and Redis Streams architecture, the tool introduces unacceptable vendor lock-in. Furthermore, deploying proprietary third-party solutions within the financial stack violates the foundational intellectual property sale-readiness protocols."

### Cemini fit

- **None as adoption target** — Reject.
- **Reference** as competitive-intel marker; monitor for product changes / pivots.

### NEEDS VERIFICATION

- Commercial terms of service and exact API rate limits, **only if** the architectural board ever authorized integration of external closed-source endpoints (currently a hard no per IP-sale policy).
