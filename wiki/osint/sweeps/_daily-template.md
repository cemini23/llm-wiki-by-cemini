# Daily Research Digest — YYYY-MM-DD

Discovery-only. Window: `YYYY-MM-DD` → `YYYY-MM-DD` (7 days). 5 Exa queries × up to 3 hits (deduped across queries).

Reference: `@scripts/daily_research_config.yaml`. **Does NOT ingest.**

---

## Active topics (sync from ROADMAP)

- _(edit `scripts/daily_research_config.yaml` when workstreams shift)_

---

## Inbox (`research to be indexed/`)

_Empty — no manual drops pending._

---

## Exa candidates

### Q1: prediction-markets (N hits)

Query: `...` · category: `news`

| Pick | Date | Title | Cluster | URL |
|------|------|-------|---------|-----|
| [ ] R1 | | [Title](https://…) | prediction-markets | |

---

## Wiki gap detect

OK — Nd since last run.

---

## Social pass (Cursor session — not automated)

- **twitter-reader**: Search fintwit for Polymarket, Kalshi, agent tooling from last 24h
- **opencli-reader**: HackerNews / arXiv frontpage for quant + agent harness
- **telegram-reader**: Financial Telegram channels — PM/crypto macro headlines

---

## Ingest session prompt (copy into Cursor)

```
Ingest selected rows from wiki/sweeps/YYYY-MM-DD-daily.md:
- Run preingest_check on any new URLs/files
- Deep-read approved candidates; discuss takeaways before writing
- Touch 3–15 wiki pages; lint; update ROADMAP + briefs if prod-touching
```

---

## Summary

| Metric | Count |
|--------|-------|
| Exa hits (deduped) | 0 |
| Inbox files | 0 |
| Gap detect due | no |

### Next steps

1. Check boxes on rows worth fetching (`R1`, `R2`, …).
2. Optional: run social pass tools above in the same session.
3. Drop PDFs/docx into inbox or fetch URLs via Exa MCP in Cursor.
4. Ingest approved items — do not auto-commit from this script.

### Discard

`rm wiki/sweeps/YYYY-MM-DD-daily.md` if nothing worth acting on.
