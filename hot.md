# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (2026-05-14 morning — K44 ingest CLOSED, largest cross-wiki routing event so far)

### Session summary

Full CLAUDE.md ingest pipeline (12 steps) executed on the single new inbox file: **"Tool Evaluation for Cemini Wiki Integration.docx"** (Gemini Deep Research v3, 28 URLs). Verdict rollup: **7 Adopt + 7 Steal-from + 1 Defer + 3 Reference + 3 Reject + 7 UNAVAILABLE**. All 6 sibling wikis touched (osint primary + ccc / cybersec / image-gen / seo / 3d-printing) — new largest cross-wiki routing event, superseding K43.

### What was created (committed across 5 git repos)

**OSINT-wiki** (1 source + 1 concept + 7 entity pages):
- Source: `eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md`
- Concept: `multi-wiki-eval-doc-level-vs-phase-0.md` — formalizes K43 two-gate lesson; documents LLM-eval skepticism flags (self-claimed anti-hallucination, footnote-without-bibliography)
- Deep entity: `aulekator-polymarket-btc-bot.md` (NautilusTrader 15-min BTC, direct K43 Polymarket-integration follow-up, 7 Phase-0 gates)
- Stubs: supavec / lap-platform / awesome-polymarket-tools-harish-garg (CC0 supersedes the rejected unlicensed alternative) / citriniresearch-2028-gic / 2 reject stubs (awesome-osint-arsenal, awesome-prediction-market-tools-aarora4)

**ccc-wiki** (9 stubs): alumnium + optillm + adamsreview (K37 convergence) + thuki + jcode (solo 6.1k★ inflation flag) + red-run (GPL patterns only) + lap-platform + gtm-agents + gym-anything (Defer)

**cybersecurity-wiki** (1 deep + 5 stubs): **betterleaks** (highest-priority Adopt — pre-IP-sale codebase audit critical; CEL filter + BPE tokenization; 6 Phase-0 gates + 3-phase adoption plan) + ai-infra-guard + cariddi + czkawka (dual-license isolation) + supavec + red-run

**image-gen-wiki** (2 stubs): training-tools/czkawka (LoRA dedup via czkawka_core MIT crate) + custom-nodes/ai-infra-guard (ComfyUI vuln signatures)

**seo-wiki** (1 update + 1 stub):
- **`geo-seo-claude.md` UPDATED** — pre-existing 2026-05-07 Phase-0 GO retained as authoritative; K44 cross-wiki convergence section appended (two independent evals converged on same GO → elevates signal quality, not duplicate work)
- gtm-agents stub

### Key K44 architectural findings

1. **Cross-wiki convergence pattern formalized**: geo-seo-claude pre-existed at validated; K44 independent reconfirmation is high-signal (not "over-claimed finding" — actual cross-wiki convergence).
2. **Star-inflation skepticism**: jcode 6.1k★ + geo-seo-claude 7.2k★ both solo maintainers — Phase-0 G1 (`gh api` star/fork ratio verification) is mandatory before adoption.
3. **License posture clarifications**:
   - czkawka **dual-license isolation** — extract czkawka_core (MIT) only; Krokiet/Cedinia GUI is GPL-3.0; verify via `cargo tree`.
   - red-run + cariddi **GPL-3.0** — architectural patterns extractable, no library embedding.
   - ai-infra-guard Apache-2.0 with **restrictive attribution clauses** — license deep-read required at Phase-0.

### K43 lesson reinforced (now formalized as concept page)

K43 doc-level ADOPTs failed Phase-0 2-for-2: bukosabino/ta (parallel-implementation conflict with pandas-ta-classic) + tradingview-mcp (TOS-on-redistribution gate). K44 treats **all Adopt/Steal-from verdicts as `doc-level-pending-phase-0`** until Phase-0 source audit clears them. The concept page `multi-wiki-eval-doc-level-vs-phase-0.md` is now the canonical reference.

### Wiki health

- wiki_lint K44-specific bidirectional gaps: **0** (5 patched at K44 close: polymarket-clob-api, polymarket-gamma-api, three-formula-system, bukosabino-ta, tradingview-mcp-atilaahmettaner, eval-github-repos-2026-05-13, awesome-polymarket-tools)
- Pre-existing dangling cross-wiki links from earlier K-series remain (tracked under K42/K43 cosmetic cleanup follow-ups in ROADMAP)
- All 5 wiki repos have local commits; **not pushed** (no explicit user request to push)

### Workspace state

- **Inbox** `research to be indexed/`: CLEAN
- **Librarian**: `Tool Evaluation for Cemini Wiki Integration.docx` confirmed at `/opt/cemini-bulk/research/` (3 MB, 13:06 server time)
- **Git** (5 wikis):
  - OSINT: HEAD `f977a29` "K44 ingest — 28-URL multi-wiki eval doc v3"
  - CCC: 9 K44 cross-route stubs committed (HEAD on K44 commit)
  - Cybersec: 6 K44 entries (incl. betterleaks deep) committed
  - Image-gen: 2 K44 stubs committed
  - SEO: 1 stub + 1 update committed
- **Briefs on cemini-prod**: unchanged from K43 close (no K44 briefs staged — K44 outputs are entity pages + Phase-0 audit queue, not deliverable briefs)

### K44 follow-ups summary (full table in ROADMAP.md)

**Phase-0 audit queue (14 items, ~7-14h estimated)**. Sequencing:
1. **betterleaks** (pre-IP-sale critical, top priority)
2. **aulekator-polymarket-btc-bot** (K43 follow-up)
3. **CCC Adopt trio**: alumnium + optillm + adamsreview (K37 cross-reference)
4. **gtm-agents** (SEO cross-route)
5. **Steal-from kb-server pipeline**: supavec + LAP
6. **CCC Steal-from**: thuki + jcode (solo-maintainer flag)
7. **Cybersec Steal-from**: ai-infra-guard + cariddi + czkawka
8. **GPL-patterns only**: red-run

### Next session — resume options

1. **Phase-0 audit: betterleaks** — top of K44 queue, pre-IP-sale-critical scope. Explore subagent ~30min.
2. **Phase-0 audit: aulekator-polymarket-btc-bot** — K43 Polymarket follow-up; G3 must resolve whether bot uses Gamma+CLOB or scraping or vendor SDK.
3. **Adams-review vs K37 reviewer-agent v2 convergence audit** — if mature, may obsolete K37 Sprint 5 deferral.
4. **K43 Polymarket integration follow-up** — monitor server-Claude execution of `2026-05-13_polymarket-gamma-clob-integration.md`.
5. **WW #178 third-source verification** — outstanding Exa-search candidate (Donny↔WW same-source dependency).
6. **K42/K43 cosmetic lint cleanup** — pre-existing dangling cross-wiki links surfaced by wiki_lint.
