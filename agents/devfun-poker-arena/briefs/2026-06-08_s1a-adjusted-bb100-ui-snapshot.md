---
title: S1a adjusted BB/100 UI snapshot (ephemeral test column)
type: brief
tags: [brief, poker, devfun, s1a, v2, de-luck, bb100]
created: 2026-06-08
target: gap audit + S1b scoring prep
competition_id: cmpy2qy65002ud9ej6b7jjq0l
---

## Target

CeminiSuite / gap premium audit — de-luck evidence when API did not expose `adjustedBbPer100`.

## Summary

Dev.fun **briefly showed** an **Adjusted BB/100** column on the S1 LIVE leaderboard (~2,362 hero hands, **290 ranked**). Column was **not sortable**; site **removed it again same morning (2026-06-08 ~7:24 AM)**. **No API field** on `/texas/benchmark/status` or leaderboard export at capture time. This brief + `tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json` are the **canonical log** (updated from 4 screenshots in `research to be indexed/bb snapshot/`).

**Poker Eval S1 (overnight prod run):** 500/500 complete — **adjusted bb/100 −17.45** (raw −37.8). Below L1 baseline (−15 to −5 vs reference panel). Not in eval top-50; separate from Playground chip rank.

## Body

### Capture metadata

| Field | Value |
|-------|--------|
| When | 2026-06-08 ~7:24 AM local (hero ~2,362 hands; field 290 ranked) |
| Source | Operator UI screenshots (4 panels, ranks 1–44 partial) |
| UI label | Adjusted BB/100 (green +values) |
| Sort | **Chips only** — bb/100 sort not available |
| Field size | 290 ranked (UI subtitle) |
| API | `detect_scoring_mode` → chip_accumulation; leaderboard `data: []` from export key |

### Hero vs field (logged rows)

| Metric | Cemini Wiki Poker | Notes |
|--------|-------------------|--------|
| Chip rank | **#1** | 139,946 chips |
| Hands | 2,362 | |
| Adjusted BB/100 | **+2,820.1** | UI value (2026-06-08 AM capture) |
| EV rank (≥400 hands logged) | **#3** | Behind 0xJeff_ai (+3,670.3), Jagoan Neon (+2,827.7) |

**De-luck conclusion [CONFIRMED for this snapshot]:** Chip #1 ≠ EV #1 among high-volume rivals. Do **not** widen nit posturing to chase leaderboard EV; use gap audit for structural fixes only.

### Top 27 by chip rank (full row from screenshots)

| # | Agent | Chips | Hands | Adj BB/100 |
|---|-------|------:|------:|-----------:|
| 1 | Cemini Wiki Poker | 139,927 | 2,283 | +2,917.2 |
| 2 | 0xJeff_ai | 122,121 | 1,366 | +4,068.2 |
| 3 | Jagoan Neon | 112,462 | 1,265 | +3,894.7 |
| 4 | Float Engine | 74,677 | 411 | +8,229.5 |
| 5 | Uday | 59,142 | 1,052 | +2,818.6 |
| 6 | PapiPrajogo | 44,953 | 1,066 | +1,974.2 |
| 7 | MonaSex Killer | 44,951 | 427 | +4,934.4 |
| 8 | Wild_Thistle_5 | 44,443 | 1,955 | +1,018.5 |
| 9 | Claude Sonnet | 41,319 | 1,718 | +1,293.7 |
| 10 | Adah Rain | 35,324 | 1,199 | +1,354.1 |
| 11 | IceMind | 31,204 | 1,263 | +1,100.5 |
| 12 | Wemby Guy | 28,772 | 893 | +1,576.9 |
| 13 | CryptoBro Poker Agent | 28,530 | 1,223 | +1,224.4 |
| 14 | zephyr | 27,061 | 360 | +3,636.0 |
| 15 | PokerKit Starter | 26,602 | 1,195 | +997.0 |
| 16 | Stariy physe | 24,165 | 1,208 | +866.9 |
| 17 | MaxCaution | 24,148 | 667 | +1,454.9 |
| 18 | Long Tú | 21,316 | 870 | +1,056.6 |
| 19 | PokerKit Nuts | 21,314 | 550 | +1,579.7 |
| 20 | Clawdi Riverguard | 20,977 | 781 | +2,157.9 |
| 21 | Alnitak | 20,334 | 1,603 | +570.3 |
| 22 | AlfieKnight | 19,506 | 465 | +1,912.7 |
| 23 | imsayurnara | 18,375 | 1,246 | +626.1 |
| 24 | kasper | 17,806 | 1,844 | +341.8 |
| 25 | Plutus | 16,550 | 280 | +2,474.8 |
| 26 | Anh Tình | 16,346 | 870 | +806.3 |
| 27 | TAG Forge | 15,802 | 1,018 | +738.2 |

### Partial rows (bb/100 only or incomplete)

| # | Agent | Adj BB/100 | Note |
|---|-------|----------:|------|
| 29 | uwu idk how to play poker | +7,942.9 | high variance |
| 32 | Bingo Finder Keystone C74A | +5,318.1 | |
| 39 | EquityBot v7 | +784.9 | V3-style bio visible |
| 40 | ED-209 Charlie | +4,328.7 | |
| 42 | HYDRA_SHARK | +182.7 | |
| 44 | Mas Buahlil Guanteng | +564.5 | |

### Audit implications

1. **Gap premium audit** — cite this snapshot for “chip #1 vs EV rank” (not chip-proxy math).
2. **Jeff / Neon** — remain nemesis-style EV references; do not mimic LAG width.
3. **Float / zephyr** — flag as small-sample EV outliers in audit prompts.
4. **S1b** — on day 1 run `detect_scoring_mode.py`; if column returns, export + screen record; merge via `import_bb100_snapshot.py`.
5. **Qualification** — still assume **chip top-20** until Discord confirms otherwise.

### Machine-readable

- JSON: `tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json`
- Import: `uv run python examples/import_bb100_snapshot.py --snapshot tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json --export-dir reports/exports/playground-s1-live-archive/`

## Sources

- Operator UI screenshots 2026-06-08 (4 images, S1 LIVE leaderboard)
- Prod `detect_scoring_mode.py` run 2026-06-08 — no API bb/100
- Qualification posture: chip top-20 (playground KO, no rebuy)
