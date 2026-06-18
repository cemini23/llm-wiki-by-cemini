## Target

`agents/devfun-poker-arena/` + researcher sandbox (BenchFlow / Daytona — confirm onboarding pack).

Operator: **cemini_wiki_poker** — **Researcher Round** (50 invited seats, $30K pool).

## Summary

Pivot optimization from **6-max Playground qual** (rank ~103) to **Researcher Round** sandbox: eval focuses on **how** agents play (trajectory + multi-axis), not only bb/100. **Jun 21** closed beta · **Jun 25** public · **Early July** finale vs Tom Dwan / Jungleman. Export full trajectories after each run; contribute axis metrics narrative in Discord.

## Body

### Timeline (one-pager + dev.fun site)

| Date | Gate |
|------|------|
| **2026-06-21** | Closed beta — researcher sandbox live |
| **2026-06-25** | Public Challenge launch |
| **Early July 2026** | Finale — top LB → pro table stream |

### Prize / status

- **$30K** Researcher Round pool [CONFIRMED Discord 2026-06-18]; site cites **$50K** total arena pool across tracks.
- **50 seats** — invited only; Cemini holds one.
- **Trajectory export** — pull full run data after sandbox matches; align with multi-axis eval story.
- **Publish path:** champion agent on platform under our handle.

### P0 — before Jun 21 (3 days)

1. **Sandbox recon** — `./scripts/list_arena_competitions.sh` daily + Discord researcher channel + BenchFlow pack: competition ID, match length (500h?), allowed code surface, whether **base LLM is fixed** [NEEDS VERIFICATION per PR]. See `references/researcher-track-sandbox.md`.
2. **HU regression matrix** — extend `tests/test_cemini_regression.py` with HU table fixtures; run `pokerkit selfplay` HU 500h vs tight-passive baseline.
3. **Submit pipeline** — document exact command from starter kit / `arena.md` skill; dry-run sandbox submit from laptop (not prod rsync until confirmed).
4. **Deprioritize dual lobby** — main playground for HUD field intel only; no top-20 qual chase burn.

### P1 — optimization loops (Jun 21–25)

| Workstream | Action |
|------------|--------|
| **HU preflop** | Branch or config `CEMINI_TABLE_MAX=2`: gin thresholds already IP/OOP; verify open-raise sizing vs BenchFlow engine |
| **Memory** | Extend `session_memory.py`: within-hand villain line + cross-session JSON on librarian/prod reports; map to Raeth 3-layer model |
| **Multi-axis eval** | Log bet-size buckets + positional fold rate per session; **export trajectory JSON** after sandbox runs (`export_competition_hands.py` / replay) for researcher contribution |
| **Stack-off discipline** | Keep R34 gin/broadway guards — HU shove spots more frequent |
| **Scans** | Re-run dev.fun personality/memory scans before publish; target memory score ≥80 |

### P2 — publish / finale

- Stable **agent_version** tags per sandbox submit in `deploys.jsonl`.
- Narrative: structured skills + regression gates (not raw LLM at runtime).
- If finalist: separate **HU** tuning brief — no 6-max HL patches on finale day.

### Current prod snapshot (2026-06-18)

- Comp: `cmqf827h30u7dfca3x2aqvzjv` (Playground S3, **6-max**)
- Hands: ~655 · Rank: 103 · Chips: 3450
- Deploy: `s2p.977b981.hl-r34` (gin lane, F6 memory, R34 broadway stack-off fix)

### References

- Wiki: `wiki/sources/devfun-poker-agent-challenge-onepager-2026-06-18.md`
- Wiki: `wiki/concepts/devfun-poker-agent-challenge-2026.md`
- arXiv 2606.13815 — multi-axis + memory ablation
- Onboarding: `read https://arena.dev.fun/skills/arena.md`
- Docs: https://docs.dev.fun/

## Sources

- [Source: poker-arena-onepager.pdf (retrieved 2026-06-18)]
- [Source: Discord #researcher-track welcome (retrieved 2026-06-18)]
- [Source: https://dev.fun/ (retrieved 2026-06-18)]
- [Source: https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html (retrieved 2026-06-18)]
- [Source: arxiv-2606.13815-poker-arena-multi-axis-profiling-of-strategic-re.pdf p.1]
