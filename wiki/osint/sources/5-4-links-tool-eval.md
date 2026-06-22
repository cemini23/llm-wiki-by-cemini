---
title: "5_4 links — System Architecture & Integration Feasibility Report (19 candidates)"
type: source
tags: [llm-agents, audit-security, dev-tooling, wiki-tooling, financial-research, license-compliance, cemini-internal]
keywords: [tool-evaluation, license-posture, karpathy-pattern, swarmvault, mitre-atlas, kelly-criterion, klaassen-magnus-elo, medskillaudit, adaptive-rag, IP-sale-readiness]
related:
  - sources/links-2-5-4-tool-eval.md
  - sources/gemini-sci-research-2602-03837.md
  - sources/more-links-5-2-arch-eval.md
  - sources/links-5-2-tool-eval.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/autoresearch-loop-pattern.md
  - entities/tools/swarmvault.md
  - entities/tools/mitre-atlas.md
  - entities/tools/probablyprofit.md
  - entities/tools/medskillaudit.md
  - entities/tools/klaassen-magnus-elo.md
  - concepts/mitre-atlas-taxonomy.md
  - sources/5-5-links-2-tool-eval.md
  - sources/5-5-links-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - sources/links-6-22-tool-eval.md
maturity: draft
read_status: deep-read
created: 2026-05-04
updated: 2026-05-11
---

## Relations

- @sources/links-2-5-4-tool-eval.md — companion 14-tool eval batch ingested same day; together they form a 33-tool sweep
- @sources/gemini-sci-research-2602-03837.md — co-ingested methodology paper that frames the autoresearch / agentic-tool-use patterns surfaced in this batch
- @sources/more-links-5-2-arch-eval.md — K27's 19-tool architecture eval; identical 8-section template; this batch extends the license-pattern catalog
- @sources/links-5-2-tool-eval.md — K27's companion 19-tool batch; same Gemini-DR rubric
- @concepts/cemini-license-posture.md — three license-pattern findings recurring (NO-LICENSE default-copyright, AGPL-as-poison, GPL-as-derivative-risk); this batch adds a fourth pattern: **CC-BY-NC-SA contamination via training data** (tennis_atp dataset → tennis_match_prediction code MIT but data-bound)
- @concepts/wiki-tooling-evaluation.md — surfaces SwarmVault as a serious candidate to address the llm-wiki-compiler bug (`CONCEPTS_DIR` hardcoded flat-layout assumption, deployment-blocked at v0.4.0)
- @concepts/autoresearch-loop-pattern.md — atlas-gic (this batch's URL 9 ref via links-2-5-4 pair) implements the Sharpe-as-loss-function variant; this batch's MITRE ATLAS provides the security-vocabulary scaffold
- @entities/tools/swarmvault.md — Adopt-tier; deep eval as wiki-compiler replacement candidate
- @entities/tools/mitre-atlas.md — Adopt-tier; security-taxonomy for wiki + LLM agent threat modeling
- @entities/tools/probablyprofit.md — Steal-from-tier; Kelly criterion + LLM ensemble consensus for prediction-market trading
- @entities/tools/medskillaudit.md — Steal-from-tier; veto-gate framework for LLM-agent skill validation
- @entities/tools/klaassen-magnus-elo.md — Steal-from-tier; tennis-prediction Elo variant (mathematical pattern, data-license blocker)

## Raw Concept

- Original title: "System Architecture and Integration Feasibility Report: Candidate Repositories and Products" (Gemini Deep Research output)
- Author: Gemini Deep Research (one-shot evaluation of 19 user-supplied URLs)
- Type: docx (Cemini-internal architecture evaluation)
- Location: cemini-librarian:/opt/cemini-bulk/research/5_4 links.docx
- Retrieved: 2026-05-04
- Length: ~3.0 MB, 19 candidates evaluated using identical 8-section template (Identity / What it is / Scoring / Per-category eval / Recommendation tier / Risks / Open questions / Sources)
- Read status: deep-read

## Narrative

Cemini-internal evaluation of 19 systems, repositories, and products against the same three-environment rubric used in K27's 38-tool batch (`@sources/more-links-5-2-arch-eval.md` + `@sources/links-5-2-tool-eval.md`). Heavily skewed toward financial-research tooling (3× tennis-data repos as quantitative-modeling reference), wiki-tooling alternatives (swarmvault as direct llm-wiki-compiler peer), and LLM-agent infrastructure (MITRE ATLAS taxonomy, claude-memory-compiler, medical-research-skills veto-gate framework).

**Prediction-market scope reframing** (added 2026-05-04 per user note): Cemini's prediction-market targets (Kalshi + Polymarket per existing roadmap) cover **sports, healthcare/biotech, politics, weather, economic indicators**. The Gemini DR eval treated tennis-prediction repos and medical-research-skills as out-of-domain ("orthogonal to financial research"), but Polymarket/Kalshi markets on tennis match outcomes and FDA approvals/biotech catalysts are *directly* in-scope. This reframes:

- `tennis_atp` (CC BY-NC-SA): still NC-blocks Cemini deployment, but the *modeling pattern* (historical match data → Elo ratings → win-probability prediction) is the canonical prediction-market sports template
- `tennis_match_prediction` (MIT code, NC-data-coupled): Klaassen-Magnus Elo is **directly applicable** to any prediction market on tennis matches — algorithm extracts cleanly, retrain on commercially-licensed data
- `aipoch/medical-research-skills` (MIT): the medical-research domain content is **directly applicable** to any biotech/pharma prediction market (FDA approval contracts on Polymarket/Kalshi, drug-trial outcomes, healthcare-company event-driven prediction). The MedSkillAudit veto-gate framework adapts to either financial-prompt validation OR direct in-domain medical-research validation.

The Gemini DR eval's three-environment rubric (Cemini production / wiki librarian / workflow) didn't include "prediction-market verticals" as an explicit fit category — future evals should add this dimension.

**Recommendation distribution:**

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 2 | atlas.mitre.org/ATLAS (CC BY 4.0 / MITRE ToU — security taxonomy → wiki ingest), swarmclawai/swarmvault (MIT — Karpathy LLM Wiki impl, 3-layer + tree-sitter + Ollama + MCP server) |
| **Steal-from** | 4 | jgollub1/tennis_match_prediction (MIT — Klaassen-Magnus Elo math, 69.7% accuracy beat Barnett-Clarke 64.6%), aipoch/medical-research-skills (MIT — MedSkillAudit veto-gate framework: 40% static + 60% dynamic + Veto Gates), randomness11/probablyprofit (MIT — Kelly + LLM ensemble consensus + multi-vector kill switch), athina-ai/rag-cookbooks (MIT — Adaptive/Corrective/Self RAG LangGraph patterns) |
| **Defer** | 3 | nautechsystems/nautilus_trader (LGPL-3.0 — institutional Rust+Python engine; PyO3 dynamic-linking blurs LGPL "derivative work" — needs legal sign-off), coleam00/claude-memory-compiler (NO LICENSE — Karpathy-pattern session-memory tool, perfect fit but unlicensed), LearningCircuit/local-deep-research (URL unavailable) |
| **Reference-only** | 2 | JeffSackmann/tennis_atp (CC BY-NC-SA 4.0 — historical match data, NC blocks Cemini), JeffSackmann/tennis_slam_pointbypoint (CC BY-NC-SA 4.0 — point-by-point Grand Slam data, NC blocks Cemini) |
| **Reject** | 5 | hip4.io (3rd-party GUI for HIP-4 — counterparty risk, inaccessible during eval), willchen96/mike (AGPL-3.0 + critical security flaws — RLS missing, hardcoded HMAC, plaintext LLM stream logging), Leantime/leantime (AGPL-3.0 + PHP/MySQL stack mismatch), frappe/erpnext (GPL-3.0 + MariaDB mandate violates Postgres constraint), 1weiho/open-slide (MIT but namespace-confusable with LGPL OpenSlide medical library), open-metadata/OpenMetadata (Apache-2.0 — JVM exceeds 7 GB RAM cap on EPYC host) |
| **Defer-Unavailable** | 3 | whyhow-ai/knowledge-graph-studio (URL unavailable), nrehiew.github.io/blog/minimal_editing (URL unavailable), LearningCircuit/local-deep-research (URL unavailable, contextual association with Alibaba DeepResearch family) |

**Critical findings:**

### 1. SwarmVault is the first concrete candidate to address the llm-wiki-compiler deployment block

Per `@concepts/wiki-tooling-evaluation.md` Phase 3 status: llm-wiki-compiler v0.4.0 is **deployment-blocked** by hardcoded `CONCEPTS_DIR = "wiki/concepts"` flat-layout assumption that breaks the nested `concepts/` + `entities/` + `sources/` wiki. kb-server was adopted as workaround.

SwarmVault claims to implement the **same Karpathy LLM Wiki three-layer architecture** (Raw / Wiki / Schema) with native Ollama (`nomic-embed-text`) + built-in MCP server + Obsidian export (`graph export --obsidian`) [Source: 5_4 links.docx URL 18; SwarmVault docs at https://www.swarmvault.ai/docs]. License is MIT (clean for IP-sale).

**Open question for follow-up evaluation**: does SwarmVault have the same flat-layout assumption? The eval mentions it "constructs a durable, persistent three-layer architecture" but doesn't explicitly confirm whether the wiki layer accepts nested directories. **Action item**: clone repo, inspect source for path-resolution logic before any deployment commitment. Recorded as @concepts/wiki-tooling-evaluation.md follow-up.

### 2. Tennis-data license trap (CC-BY-NC-SA contamination via training data)

A new license-pattern variant surfaces in this batch: `jgollub1/tennis_match_prediction` is MIT-licensed *code* but is data-coupled to Jeff Sackmann's tennis_atp dataset (CC BY-NC-SA 4.0). The Klaassen-Magnus Elo *algorithm* can be safely lifted (mathematical methods are not copyrightable), but any *trained model weights or feature pipelines* derived from the NC-licensed data inherit the NC restriction.

**Mitigation**: extract the algorithm only, retrain against commercially-licensed data feeds. Documented as caveat for any "MIT code + restrictive data" combinations in future evals. Update `@concepts/cemini-license-posture.md` with this fourth pattern.

### 3. Three-environment rubric remains stable but adds two new failure modes

K27 documented three license patterns (NO-LICENSE default-copyright, AGPL-as-poison, GPL-as-derivative-risk via LLM coding agents). This batch adds:

- **CC-BY-NC + ML-data contamination** (tennis_atp + tennis_match_prediction): MIT code can be poisoned by NC-licensed training data downstream
- **Namespace-confusion license risk** (1weiho/open-slide vs CMU openslide.org): unrelated repos sharing names triggers false-positive SCA scanner flags during M&A diligence

Both patterns now flagged as evaluation criteria for future batches.

### 4. MedSkillAudit veto-gate framework is directly transferable

aipoch/medical-research-skills bundles a static-and-dynamic LLM-skill audit framework: 40% static + 60% dynamic scoring, with explicit Veto Gates (Operational Stability, Scientific Integrity). The medical-domain content is irrelevant; the **audit harness is reusable**.

Direct application: refactor the harness to validate financial-reasoning prompts written for the DeepSeek API before staging them via `briefs/` → `/opt/cemini/briefs/`. Pairs with the wiki-lint workflow.

### 5. probablyprofit's safeguards are reusable; networking layer is not

Polymarket-targeted but engineered as a production trading framework — Kelly criterion sizing, automated drawdown protection, multi-vector emergency kill switch, LLM ensemble consensus mode (Claude + GPT-4 + Gemini vote on trades). MIT-licensed.

Cemini already targets Kalshi (not Polymarket), so the networking adapters require a full rewrite. Extractable: risk-management math, kill-switch implementation, LLM-voting consensus topology.

### 6. MITRE ATLAS taxonomy fits the wiki layer cleanly

CC BY 4.0 with explicit MITRE attribution requirement: 16 tactics × 170 techniques × 35 mitigations × 57 case studies. Convertible to interconnected markdown pages parseable by the librarian's MCP server. Provides standardized vocabulary for any future LLM-agent security audit work (input sanitization, prompt-injection resilience, RAG context injection — see Morris II Worm case study).

Attribution requirement: **"© 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation."** must appear on any wiki page derived from ATLAS material.

### Architectural patterns worth extracting

- **swarmvault three-layer + MCP-native architecture** → potential llm-wiki-compiler replacement
- **MedSkillAudit veto-gate harness** → financial-prompt validation pre-deployment
- **Klaassen-Magnus Elo + Efron-Morris estimators** → general-purpose Bayesian-weighted predictor pattern (sports → quant)
- **probablyprofit Kelly + ensemble consensus** → prediction-market scaling logic
- **rag-cookbooks Adaptive/Corrective RAG** → upgrade path for LangGraph 4-node StateGraph in Cemini orchestrator

## Snippets

- **SwarmVault three-layer architecture**: "constructs a durable, persistent three-layer architecture (Raw sources, compiled Wiki, programmatic Schema) utilizing raw Markdown files for long-term storage and SQLite for instantaneous hybrid search (combining full-text indexing with semantic embeddings). It natively parses over 30 programming languages via tree-sitter AST, integrates flawlessly with local LLMs such as Ollama, and exposes a built-in MCP server, allowing external agents like Claude Code to seamlessly query and traverse the compiled knowledge graph." [Source: 5_4 links.docx URL 18]

- **Klaassen-Magnus Elo predictive performance**: 2016 accuracy 69.7% / log loss 0.594, beating Barnett-Clarke (64.6% / 0.663) and Barnett-Clarke opponent-adjusted EM (67.6% / 0.632). [Source: 5_4 links.docx URL 3]

- **MedSkillAudit veto-gate composition**: "two-stage scoring system (40% Static, 60% Dynamic) and strict 'Veto Gates' (checking Operational Stability, Scientific Integrity)." [Source: 5_4 links.docx URL 9]

- **probablyprofit risk controls**: "Kelly criterion position sizing, automated maximum drawdown protection, and a multi-vector emergency kill switch... 'ensemble consensus mode,' which orchestrates multiple LLMs (Claude, GPT-4, Gemini) to vote dynamically on trade executions." [Source: 5_4 links.docx URL 12]

- **MITRE ATLAS scope**: 16 tactics × 170 techniques × 35 mitigations × 57 case studies, NIST SP-800-53 integration, used by 150+ organizations including federal agencies. [Source: 5_4 links.docx URL 8]

- **claude-memory-compiler positioning**: "directly adapted from Karpathy's LLM Knowledge Base pattern, it injects session hooks (.claude/settings.json) to automatically capture conversation transcripts. A background process (flush.py) then utilizes the Claude Agent SDK to extract critical decisions, patterns, and architectural context, appending this intelligence to a markdown-based index file, notably eliminating the need for a complex vector database." [Source: 5_4 links.docx URL 14] — Defer: NO LICENSE.

- **HIP-4 protocol throughput claim**: "~200,000 orders/sec (shared engine)" via underlying HyperCore engine, with unified Perps + Prediction margin (vs Polymarket's isolated 1× margin on Polygon). [Source: 5_4 links.docx URL 5; bitget.com/news/detail/12560605394797]

- **AGPL-3.0 + critical security flaws** (willchen96/mike): "issue #9 indicates that all LLM stream events, including highly sensitive document contents, are logged to disk in plaintext... missing RLS policies, hardcoded fallback HMAC tokens enabling unauthorized access, and severe authorization bypasses that permit cross-project chat injection." [Source: 5_4 links.docx URL 7] — Reject: AGPL alone would block; combined with security flaws is disqualifying.

## Dead Ends

*(none yet — first ingest of this source.)*
