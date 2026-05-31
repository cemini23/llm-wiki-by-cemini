---
name: cemini-wiki-ingest
description: >-
  OSINT wiki ingest ritual — daily sweep triage, Posts.docx batches, tool-eval
  docx, K-batch standard flow, preingest, lint, librarian move, ROADMAP/briefs.
  Use when ingesting sources, running a K-batch, processing wiki/sweeps/*-daily.md,
  tool evaluation drops, or Posts.docx from research to be indexed/.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---

# Cemini wiki ingest (Phase 3)

Read `@.cursor/rules/osint-ingest-gates.mdc` first — human gates are non-negotiable.

## Entry points

| Trigger | Start here |
|---------|------------|
| Morning digest | `wiki/sweeps/YYYY-MM-DD-daily.md` — user picks `R1`, `R2`, … |
| Inbox drop | `research to be indexed/` — preingest already ran via WatchPaths |
| Posts.docx | Filename `Posts.docx` — always hash-discipline (K## in source slug) |
| Tool eval docx | Filename matches `tool.?eval|evaluation|wiki.?fit` |
| PDF / arXiv | Standard source page flow |

## Universal ritual (CLAUDE.md steps 0–11)

1. **`python3 scripts/preingest_check.py`** — stop on DUPLICATE unless supersede decided
2. **Discuss key takeaways with user before writing** — mandatory human gate
3. **Cross-wiki routing** — `python3 scripts/cross_wiki_route.py` when off-topic; prefer brief over stub
4. Write `wiki/sources/<slug>.md` + entity/concept stubs or updates (3–15 pages per ingest)
5. **`wiki/index.md`** + **`wiki/log.md`** append
6. **`python3 scripts/wiki_lint.py`** — fix orphans, bidirectional gaps, dangling links
7. **`python3 scripts/ingest_session_gate.py`** — mechanical pre-commit check
8. **`python3 scripts/sync_wiki_to_librarian.sh`** after commit (or post-commit hook)
9. **`scp` raw to librarian** + rm laptop copy
10. **ROADMAP.md** + stage **`briefs/`** if prod-touching
11. **`python3 scripts/skill_audit.py briefs/<file>.md`** before any prod scp

## A — Daily sweep ingest

When user says "ingest R2, R5 from today's digest":

1. Read `wiki/sweeps/YYYY-MM-DD-daily.md`
2. Fetch each URL via lazy-tool → fetch or Exa `crawling_exa`
3. Run preingest on any downloaded files
4. Follow universal ritual — one K-batch per session unless user splits

Copy-paste opener (also in digest file):

```
Ingest selected rows from wiki/sweeps/YYYY-MM-DD-daily.md:
- Run preingest_check on any new URLs/files
- Deep-read approved candidates; discuss takeaways before writing
- Touch 3–15 wiki pages; lint; ingest_session_gate; update ROADMAP + briefs if prod-touching
```

## B — Posts.docx batch

1. **`python3 scripts/extract_docx.py`** or read docx in session; count posts (`Next Post:` split)
2. Source slug: `trading-posts-compilation-N-YYYY-MM-DD.md` — **never reuse slug across hashes**
3. Record sha256 + post count in `## Raw Concept`
4. After OSINT source page exists — **seo-wiki style pass** (CLAUDE.md step 4c):
   - Read `@seo-wiki/prompts/posts-docx-style-pass.md`
   - Update `@seo-wiki/concepts/x-account-voice-and-format.md`
   - Append Article beats or create `x-article-N-notes.md`
   - One line in `@seo-wiki/wiki/log.md`
5. Route CCC/cybersec/image-gen content via `cross_wiki_route.py` (brief preferred)

## C — Tool eval docx (v5)

1. Inbox drop auto-runs **`bash scripts/post_tool_eval_license.sh`** — re-read `.local/reports/license-*`
2. **Never transcribe eval license claims** — verify via `gh api` per `@concepts/cemini-license-posture.md`
3. Source page: aggregate Rejects on source page; **no reject-stub farm**
4. Adopt-tier only → Phase-0 audit per `CLAUDE.md` before any install
5. v5 eval prompt lives in CCC wiki — use for new drops

## D — K-batch checklist

- [ ] preingest_check all inbox files
- [ ] User approved takeaways (human gate)
- [ ] 3–15 wiki pages touched
- [ ] Bidirectional `related:` on every new edge
- [ ] index.md + log.md updated
- [ ] wiki_lint clean
- [ ] ingest_session_gate.py
- [ ] librarian scp + laptop rm
- [ ] ROADMAP + briefs staged
- [ ] skill_audit on prod briefs

## Social pass (same session, not cron)

After digest triage, optional reads per `daily_research_config.yaml`:

- **twitter-reader** — fintwit PM/Kalshi/agent last 24h
- **opencli-reader** — HN / arXiv frontpage
- **telegram-reader** — macro/crypto channels

Drop saved threads into inbox or ingest inline as source stubs.

## Do NOT automate (Phase 4)

See `@.cursor/rules/osint-ingest-gates.mdc` — license claims, cross-wiki judgment, prod GO, contradiction resolution, and Tier 3 outbound ingest stay user-gated.
