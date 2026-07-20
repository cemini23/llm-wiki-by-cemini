---
title: Inbox arXiv reject batch — 2026-07-20 (3 lockstep-query false positives)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, lockstep, mis-route, uas, quantum, covariance]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-19.md
  - concepts/rts-networking-deferred.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-20
updated: 2026-07-20
---

## Raw Concept

Three PDFs from `2026-07-20-daily.md` (arxiv-only paper lane; news disabled). **All reject** — `lockstep-deterministic` cluster arXiv-API fallback matched bare `deterministic` / `simulation` tokens outside game networking. Preingest: 3× NEW.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.15583 | Distributed continuous aerial surveillance by UAS swarms (LTL specs) | **Reject** | Multi-UAS formal methods / eess.SY — not RTS lockstep; no castle-sim adopt |
| 2607.15597 | Deterministic atom-shuttle interconnects (atom–ion CZ gate) | **Reject** | Quantum hardware (quant-ph) — title “deterministic” ≠ game lockstep |
| 2607.15945 | Testing the rank of the spot covariance matrix (Itô semi-martingale) | **Reject (route @osint-wiki)** | High-frequency stats / math.ST — CeminiSuite quant shelf only if operator pulls; **no prod brief** |

**Phase-0:** none. **Local adopt:** none.

**Briefs:** none — no poker / David / xsp / pm / castle-sim / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 3 PDFs to egress; clear inbox. Tighten `lockstep-deterministic` `arxiv_query` to drop bare `deterministic`/`simulation` (require lockstep / rollback netcode + game/RTS/multiplayer/networking).

## Snippets

```
python3 scripts/preingest_check.py → 3 NEW, 0 LIKELY, 0 DUPLICATES
Digest cluster: lockstep-deterministic (arXiv API)
```

## Dead Ends

- Treating title-token “deterministic” as networked-game lockstep research
- Auto-scp’ing spot-covariance / quant-stats papers to cemini-prod
