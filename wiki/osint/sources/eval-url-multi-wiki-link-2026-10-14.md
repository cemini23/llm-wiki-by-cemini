---
title: "Tool eval — Multi-Wiki Link Evaluation (20 URLs, 2026-10-14)"
type: source
tags: [eval, tool-evaluation, licence-verification, phase-0, k291]
keywords: [tool eval, licence drift, gh api, SPDX, tier, club-3090, star counts]
related:
  - concepts/k291-osint-wave.md
  - concepts/tool-evaluation-framework.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-15
---

## Relations

- @concepts/k291-osint-wave.md — K291 osint wave hub
- @concepts/tool-evaluation-framework.md — the tiering frame this eval applies

## Raw Concept

Title: Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10.9)
Type: Tool evaluation docx, 20 URLs
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Link Revenue Evaluation.docx`
Retrieved: 2026-10-14
Read status: read

## Narrative

An eval docx arrived in the K291 osint inbox and was **archived without review** during the first pass of the wave. It was recovered and the Phase-0 licence pass run on 2026-10-15.

**Batch theme:** agentic operational auditing, consumer-GPU LLM fine-tuning and multi-engine serving, differential binary decompilation, equity factor drawdown analytics, developer harness tooling.

### The docx's tiers

| Tier | Count | Items |
|---|---|---|
| Extract | 3 | iFixAi, Soup, Liquiqation Nation |
| Context | 7 | scientific-agent-skills, tiny11builder, dx-ball, ai-memory, stylebot, watchdog, dotfiles |
| Pass | 7 | nvm, Tov, omacharts, duckdb-object-storage, layer5, meshery, crop-map |
| UNAVAILABLE | 1 | cambrianmanagement.ai |

**0 Integrate GO.**

### Phase-0 result: the docx licence claims are wrong or incomplete on 5 of 17 GitHub repos

Verified with `gh api repos/<owner>/<name>` on 2026-10-15.

| # | Repo | Docx claim | `gh api` says | Verdict |
|---|---|---|---|---|
| 1 | nvm-sh/nvm | MIT | MIT | ✓ |
| 2 | K-Dense-AI/scientific-agent-skills | MIT | MIT | ✓ |
| 3 | ifixai-ai/iFixAi | Apache-2.0 | Apache-2.0 | ✓ |
| 4 | ntdevlabs/tiny11builder | NOT FOUND | NOASSERTION | ≈ both unresolved |
| 5 | richiemcilroy/Tov | NOT FOUND | **MIT** | ✗ missed |
| 6 | N0zoM1z0/dx-ball | MIT | MIT | ✓ |
| 7 | MakazhanAlpamys/Soup | NOT FOUND | **Apache-2.0** | ✗ missed |
| 8 | **noonghunna/club-3090** | **AGPL-3.0** | **Apache-2.0** | ✗ **wrong, and it drove the tier** |
| 9 | jorgemanrubia/omacharts | NOT FOUND | **MIT** | ✗ missed |
| 10 | akitaonrails/ai-memory | MIT | MIT | ✓ |
| 11 | dentiny/duckdb-object-storage | MIT | MIT | ✓ |
| 12 | ankit/stylebot | MIT | MIT | ✓ |
| 13 | layer5io/layer5 | Apache-2.0 | Apache-2.0 | ✓ |
| 14 | meshery/meshery | Apache-2.0 | Apache-2.0 | ✓ |
| 15 | kzndotsh/watchdog | NOT FOUND | NOASSERTION | ≈ both unresolved |
| 18 | SabhyaC26/crop-map | NOT FOUND | **MIT** | ✗ missed |
| 20 | kzndotsh/dotfiles | NOT FOUND | NOASSERTION | ≈ both unresolved |

**5 of 17 disagree.** Three were websites (16, 17, 19) with no repository to check.

**The club-3090 row is the fourth consecutive wave carrying it.** K290's docx said AGPL-3.0 and tiered it Extract on copyleft grounds; K290's Phase-0 found Apache-2.0 and said so. This docx repeats the AGPL claim. The repo is Apache-2.0 — confirmed again. **A copyleft caution has now been raised against a permissive repository in two successive waves.**

### Star counts remain unreliable

| Repo | Docx | Actual | Delta |
|---|---|---|---|
| K-Dense-AI/scientific-agent-skills | 32,991 | **49,979** | +51% |
| nvm-sh/nvm | NOT FOUND | **95,540** | — |

Consistent with the standing finding: **docx star counts are ~2× off and frequently absent.** Treat them as unusable.

### What this changes

Nothing in the tiering here is an Integrate decision, so no product action follows. The finding is about the **eval pipeline**: for the fourth wave running, its licence column cannot be trusted without an independent check.

## Snippets

> "URLs received: 20 · URLs to evaluate this run: 20 (max 20)" [Source: Multi-Wiki Link Revenue Evaluation.docx p.1]

> "License: AGPL-3.0 — friction only" — on `noonghunna/club-3090`, which `gh api` reports as **Apache-2.0** [Source: Multi-Wiki Link Revenue Evaluation.docx]

## Dead Ends

- **Trusting the docx licence column.** Wrong or incomplete on 5 of 17 in this wave, and 5 of 20 in K290. Run `gh api` before any tier decision that rests on a licence.
- **Reading the tier table as a decision.** Every row here is Pass, Context, Extract or UNAVAILABLE. **0 Integrate GO.**
