---
title: "Deep Research URL Evaluation 2026-08-13 (20-URL batch)"
type: source
tags: [eval, phase-0, k235, atto, guruwatcher, ccc, cyber]
keywords: [ppt-master, claude-task-viewer, quotio, fastdup, benchflow, valuecell, apkleaks, watermarks-remover, smolvm, vibeindex, GHunt, sentrux, firecracker, rapidscan, macro-inc, agentic-data-scientist, legal-skills, macos-iso-builder, theholyword, CLIProxyAPI]
related:
  - entities/tools/ppt-master.md
  - entities/tools/claude-task-viewer.md
  - entities/tools/quotio.md
  - entities/tools/benchflow-artifacts.md
  - entities/tools/valuecell.md
  - entities/tools/apkleaks.md
  - entities/tools/smolvm.md
  - entities/tools/ghunt.md
  - entities/tools/sentrux.md
  - concepts/cemini-license-posture.md
  - sources/eval-url-revenue-opportunity-2026-08-12.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: read
---

## Relations

- @entities/tools/ppt-master.md — Integrate (Atto concierge decks, MIT verified, sparse-adopt)
- @entities/tools/claude-task-viewer.md — Integrate (CCC harness observability, MIT verified)
- @entities/tools/quotio.md — Integrate (CCC quota failover; was Extract in K233)
- @entities/tools/benchflow-artifacts.md — Extract (cyber PR audit, AGPL-3.0 → isolate)
- @entities/tools/valuecell.md — Extract (GuruWatcher news agents only, no execution modules)
- @entities/tools/apkleaks.md — Extract (cyber APK secret scan)
- @entities/tools/smolvm.md — Integrate-conditional (cyber microVM, license unverified)
- @entities/tools/ghunt.md — Context (Google accounts OSINT methodology)
- @entities/tools/sentrux.md — Watch (immature; K233 Extract downgraded)
- @concepts/cemini-license-posture.md — license verification overrides docx claims
- @sources/eval-url-revenue-opportunity-2026-08-12.md — prior 20-URL eval batch (different URL set)

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Deep Research URL Evaluation.docx` |
| sha256 | `8d50bcbc6eb01799e3605dd8603674a19d8395ae4f60d97eefe2d5d35e9dd9d5` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Deep Research URL Evaluation.docx` |
| retrieved | 2026-08-13 |
| URLs evaluated | 20 |
| Batch theme | Agentic frameworks, microVM sandboxes, OSINT tools, API orchestration, presentation generation |
| Priority lens | revenue + project fit; Atto #1 · GuruWatcher #2 |

## Narrative

20-URL deep-research batch. Docx tier calls are **claims, not verdicts** — license claims verified independently this session (gh api + LICENSE files) before any Integrate/Extract adoption. Summary of independent verification:

**Integrate (docx): 4**
- `hugohe3/ppt-master` (Atto) — **MIT verified** (gh api + LICENSE file). Shallow clone = 1.3 GB (examples 581M, skills 115M) → over `.local/adopts/` 500 MB threshold. **CONDITIONAL-GO**: sparse-adopt `skills/ppt-master/` + requirements.txt, never full clone. PII → external TTS/AI APIs must stay masked.
- `L1AD/claude-task-viewer` (CCC) — **MIT verified**; cloned `.local/adopts/claude-task-viewer` (3.2M). Read-only local Kanban over `~/.claude/tasks/`; zero agent interference.
- `nguyenphutrong/quotio` (CCC) — **MIT verified**; cloned `.local/adopts/quotio` (165M). Upgraded Extract→Integrate vs K233; quota failover proxy.
- `visual-layer/fastdup` (Atto image dedup) — **REJECT for Atto**: LICENSE file = **CC BY-NC-ND 4.0** (non-commercial, no-derivatives). gh api NOASSERTION had masked this. Docx's Atto Integrate call is invalid for a commercial product. Non-commercial personal use only → WATCH.

**Extract (docx): 5**
- `benchflow-ai/artifacts` (local-lab) — **AGPL-3.0 verified** (gh api). repo-report/repo-verify/repo-scrub local-only validation. Extract pattern + run as isolated binary/microVM; **no proprietary merge**.
- `ValueCell-ai/valuecell` (GuruWatcher) — Apache-2.0 per docx (unverified this session; Extract = news-agent patterns only). Hard ban: never pull execution/order modules.
- `dwisiswant0/apkleaks` (cyber) — Apache-2.0 per docx (unverified). JADX + regex JSON secret scan; CVE-2021-21386 history noted; isolate APK decompilation.
- `guillaumemeyer/watermarks-remover` (Atto) — license **NOT FOUND**. Ethical gray (strips C2PA/SynthID/Unicode marks) → restricted to Atto document formatting only, never deception, never on wiki/brief provenance.
- `vibeindex.dev` (CCC) — 90k+ skill/MCP index with claimed Cisco Skill Scanner. Security flags unverified; treat as discovery directory, not trust signal.

**Watch (docx): 3** — K-Dense-AI/agentic-data-scientist (xsp, API-cost risk); sentrux (CCC, license NOT FOUND, immaturity — downgrade from K233 Extract); firecracker (cyber, Apache-2.0, prefer smolvm abstraction).

**Context (docx): 5** — GHunt (AGPL per docx but **no LICENSE file in repo** — unverifiable; wiki methodology only); gfodor/legal-skills (license NOT FOUND); LongQT-sea/macos-iso-builder (license NOT FOUND; Apple EULA limits virtualization to Apple hardware); theholyword.net (family-tree archival texture); Zhihu CLIProxyAPI domestic-model routing (CCC API-routing notes).

**Pass (docx): 2** — skavngr/rapidscan (GPL-2.0, Py2.7, last commit 2023); macro-inc/macro (monolithic SaaS, no modular value).

Revenue by project: atto=4, guruwatcher=1, local-abliterated-lab=3, family-tree=1. No poker-arena hooks in this batch.

## Snippets

> "Never trust docx license claims" — operating rule this batch: 2 of 5 docx license claims (fastdup NOASSERTION→CC BY-NC-ND; GHunt AGPL→no LICENSE file) failed independent verification.

> Combo (valid): benchflow repo-scrub + smolvm microVM → sanitize untrusted repo payloads before Claude/Cursor ingest in the local lab. [Source: Deep Research URL Evaluation.docx]

## Dead Ends

- Full clone of ppt-master for Phase-0 audit: 1.3 GB even at `--depth 1` (examples/ assets dominate) → sparse-adopt path instead of vendoring.
- GHunt license verification: no LICENSE file on `main` or `master` → docx AGPL claim unverifiable; Context tier anyway (no clone).
