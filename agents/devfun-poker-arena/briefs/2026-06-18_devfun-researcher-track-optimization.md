## Target

`agents/devfun-poker-arena/` + researcher sandbox (BenchFlow / Daytona — confirm onboarding pack).

Operator: **cemini_wiki_poker** — **Researcher Round** (50 invited seats, $30K pool).

## Summary

Optimize for **Researcher Round** sandbox LB: **6-max NLHE**, trajectory + multi-axis eval. **Multi-day** season grind (not 500h Eval). **Jun 21** beta. PR: fixed engine + base LLM.

## Body

### Timeline (one-pager + dev.fun site)

| Date | Gate |
|------|------|
| **2026-06-21** | Closed beta — researcher sandbox live |
| **2026-06-25** | Public Challenge launch |
| **Early July 2026** | Finale — top LB → pro table stream |

### Format & match defaults [operator 2026-06-18]

| Item | Posture |
|------|---------|
| **Table size** | **6-max** — not HU-only (one-pager HU may be finale/publish wording) |
| **Match length** | **Multi-day** season (Playground/Tournament style) — not Eval 500h; TBD |
| **Submit cadence** | Same as existing poker comps (`pokerkit run` / lobby loop) |
| **Engine / LLM** | Fixed per PR [CONFIRMED per PR] — policy `decide()` only until skill contradicts |

### Prize / status

- **$30K** Researcher Round pool [CONFIRMED Discord 2026-06-18]
- **50 seats** — invited only; Cemini holds one
- **Trajectory export** after each benchmark run
- **Publish path:** champion agent on platform under our handle

### P0 — before Jun 21

1. **Sandbox recon** — `list_arena_competitions.sh` daily until Researcher comp appears; read `skillFile` for any override on format/length.
2. **6-max regression** — `test_cemini_regression.py` + HU spots as smoke; `run_hu_sandbox_gate.sh` (6-max selfplay + trajectory bundle).
3. **Submit pipeline** — `pokerkit run --max-hands 50` smoke → full `pokerkit run` (500h); `export_researcher_trajectory.sh` after each run.
4. **Playground** — HUD intel only; no top-20 qual chase.

### P1 — optimization loops (Jun 21–25)

| Workstream | Action |
|------------|--------|
| **6-max policy** | HL loop + gin lane + seat matrix — prod-shaped `cemini_decide.py` |
| **Memory** | Extend F6; Raeth 3-layer alignment |
| **Multi-axis eval** | Trajectory JSON + axis_summary after each submit |
| **Stack-off discipline** | R34 broadway/gin guards — keep green in full regression |
| **Scans** | Personality/memory scans before publish |

### P2 — publish / finale

- Stable **agent_version** tags per submit in `deploys.jsonl`
- Finale table format may differ from sandbox — separate brief if HU live table

### Current prod snapshot (2026-06-18)

- Comp: `cmqf827h30u7dfca3x2aqvzjv` (Playground S3, 6-max)
- Hands: ~655 · Rank: 103 · Chips: 3450
- Deploy: `hl-r34` (gin lane, F6 memory, R34 broadway stack-off fix)

### References

- Wiki: `wiki/sources/devfun-poker-agent-challenge-onepager-2026-06-18.md`
- Wiki: `wiki/concepts/devfun-poker-agent-challenge-2026.md`
- Wiki: `wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md`
- `references/researcher-track-sandbox.md`
- arXiv 2606.13815 — multi-axis + memory ablation

## Sources

- [Source: poker-arena-onepager.pdf (retrieved 2026-06-18)]
- [Source: Discord #researcher-track welcome (retrieved 2026-06-18)]
- [Source: https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html (retrieved 2026-06-18)]
