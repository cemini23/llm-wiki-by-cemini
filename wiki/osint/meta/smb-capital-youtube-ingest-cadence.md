---
title: SMB Capital YouTube ingest cadence
type: concept
tags: [meta, youtube, smb-capital, ingest, cadence, k79]
keywords: [smbcapital, youtube-ingest, channel-backfill, yt-dlp]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-05-22.md
  - sources/smb-capital-youtube-week-2026-05-05.md
  - sources/smb-capital-youtube-week-2026-04-14.md
  - sources/smb-capital-youtube-week-2026-04-01.md
  - sources/smb-capital-youtube-week-2026-03-22.md
  - sources/smb-capital-youtube-week-2026-03-14.md
maturity: core
created: 2026-05-29
updated: 2026-05-29
- @sources/smb-capital-youtube-week-2026-05-22.md — batch 1
- @sources/smb-capital-youtube-week-2026-05-05.md — batch 2
- @sources/smb-capital-youtube-week-2026-04-14.md — batch 3
- @sources/smb-capital-youtube-week-2026-04-01.md — batch 4
- @sources/smb-capital-youtube-week-2026-03-22.md — batch 5
- @sources/smb-capital-youtube-week-2026-03-14.md — batch 6

## Narrative

| Field | Value |
|-------|-------|
| **Channel** | [SMB Capital (@smbcapital)](https://www.youtube.com/@smbcapital) |
| **Direction** | Newest-first; work **backward** |
| **Tooling** | `yt-dlp` auto-captions → `.local/` → librarian transcript `.md` |
| **Last batch** | 2026-03-14 → 2026-03-19 (3 videos) |
| **Next batch** | playlist #19–21 (see resume pointer) |
| **Total ingested** | **18 videos** |

### Batch 1 — 2026-05-19 → 2026-05-23 ✓

`AZy-LET8THE`, `34TnfjFWbj8`, `FDGN3sMF8AY`

### Batch 2 — 2026-05-05 → 2026-05-12 ✓

`YqNXTEEn1HQ`, `R04-2QQXkYc`

### Batch 3 — 2026-04-14 → 2026-04-25 ✓

`45eaVU5NVi8`, `mssPkDuQnmY`, `sh5h0GJzjNk`

### Batch 4 — 2026-03-31 → 2026-04-08 ✓

| Date | ID | Title |
|------|-----|-------|
| 2026-04-08 | `K2e1Sdpfv7s` | Dr. Steenbarger — Positive Trading Psychology |
| 2026-04-04 | `JddKb9XyOqk` | 5 Signs You're About to Become a Profitable Trader |
| 2026-04-01 | `afDpTJ6I3gA` | Best Earnings Trading Strategy |
| 2026-03-31 | `Rqmdw4xyIMM` | How to use Claude To Gain a Huge Day Trading Edge |

### Batch 5 — 2026-03-22 → 2026-03-28 ✓

| Date | ID | Title |
|------|-----|-------|
| 2026-03-22 | `qqGXLNwcUk0` | The 7 Trading Signals You Can't Trade Without |
| 2026-03-25 | `Jniwt90PUS4` | The $100 New Options Strategy |
| 2026-03-28 | `rFBSm3OwH-4` | The "8-Figure Table" |

### Batch 6 — 2026-03-14 → 2026-03-19 ✓

| Date | ID | Title |
|------|-----|-------|
| 2026-03-19 | `vthfx0ZFQ6A` | The Keys to Trading Success (From Real Prop Traders) |
| 2026-03-17 | `TpAPTwLMb44` | How to Maximize Options Profits |
| 2026-03-14 | `V-ASQFpDL0g` | The Missing Piece That Made Trading 5× Easier |

### Resume pointer

Next session (playlist order): **`QHvp6sja4S4`** (7 red flags, 2026-03-12), **`MlcwkmSpQaY`** (5 Levels of Competence, 2026-03-05), **`K6YVPHULzPA`** (Wheel Options, 2026-02-28).

User-gated — agent does not auto-run channel backfill.

### Distribution workflow (mandatory — do not lose desk knowledge)

After **each batch** (or when operator says "ship SMB brief"):

| Step | Action |
|------|--------|
| 1 | Wiki source + concepts + bidirectional links |
| 2 | Combined transcript → `scp` → `cemini-librarian:/opt/cemini-bulk/research/smb-capital-youtube-week-YYYY-MM-DD-transcripts.md` |
| 3 | **Update rolling prod brief** — `briefs/2026-05-29_k79-smb-capital-youtube-synthesis-cemini.md` (append batch summary + wiki routes) |
| 4 | `python3 scripts/skill_audit.py briefs/2026-05-29_k79-smb-capital-youtube-synthesis-cemini.md` |
| 5 | `bash scripts/smb_youtube_ship.sh` — SCP brief → `cemini-prod:/opt/cemini/briefs/` + `sync_wiki_to_librarian.sh` |
| 6 | `git commit` wiki + script + ROADMAP/log; `git push`; verify prod brief path |

**Rationale:** Official [@smbcapital](https://www.youtube.com/@smbcapital) channel = desk-validated strategies. Wiki is canonical detail; **prod brief is the anti-loss index** for server-Claude. Options automation still requires backtest; process/execution adoption can proceed from brief P0/P1.

**Prod brief (current):** `cemini-prod:/opt/cemini/briefs/2026-05-29_k79-smb-capital-youtube-synthesis-cemini.md`
