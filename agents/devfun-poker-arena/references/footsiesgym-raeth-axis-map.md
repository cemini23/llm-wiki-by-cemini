# FootsiesGym → Raeth M₁–M₉ → Cemini proxies (K151)

Steal map from arXiv **2607.06514** (FootsiesGym) + **2607.06854** (lightweight game agents).
**Do not** install FootsiesGym / Unity / PettingZoo. **Do not** replace pokerkit.

## FootsiesGym API (eval literacy only)

| Primitive | FootsiesGym | Poker analog |
|-----------|-------------|--------------|
| Action space | \|A\|=6 default (none/back/forward/attack/±attack); optional \|A\|=9 charge toggles | Discrete legal actions via `allowedActions` |
| Observation | 85-d (88 w/ charge): common distance + shared×2 (self/opp) + **privileged self** (dash, charge timer, prev action) | Hole cards + stack/bet public; villain hole **hidden** |
| Rewards | Zero-sum; ±w terminal; timeout 0 | Chip delta / bb/100 |
| Action delay | Frames between select → execute; delay 0 → pure react; higher → prediction/commitment | SPR / timing commitment; cannot “react” to unobserved intent |
| Exploitability | Approximate best-response (PPO vs frozen checkpoint) | Selfplay vs toughest yardstick villain (TEN, maniac_shark) |
| Curriculum | PFSP / population of past checkpoints | Nemesis ladder: rock → lag → TEN → maniac_shark_lite_2 |

Code: https://github.com/como-research/FootsiesGym (reference only).

## Axis map

| FootsiesGym dimension | Raeth axis | Cemini proxy (`researcher_trajectory_summary.py`) |
|-----------------------|------------|---------------------------------------------------|
| Bet/spacing timing under delay | M₁ Bet sizing | `M1_bet_size_histogram` (street bet-ratio buckets) |
| Charge/special commitment vs react | M₂ Bluffing / deception | Timing + SPR commitment literacy (refs only; no LLM judge) |
| Privileged self vs shared opp block | M₃ Opponent reading | HUD archetype + nemesis seed; never invent villain hole |
| Reactive collapse vs stationary opp | M₄ Composure | `M4_vpip_delta_post_bad_beat` |
| PFSP / rising opponent pool | M₅ Adaptability | Nemesis curriculum in HU gate advisory lanes |
| Special-move discovery rarity | M₆ Prediction accuracy | Reasoning YAML equity/hand claims (regex) |
| Mixed strategy over cyclic RPS | M₇ Strategic mixing | `M7_mean_action_entropy` by (street, position) |
| No privileged leak in traces | M₈ Factual accuracy | `M8_hallucination_rate`, `M8_hole_leak_rate` (**P0 gate**) |
| Role asymmetry (self vs opp features) | M₉ Positional awareness | `M9_vpip_by_position`, `M9_positional_vpip_gap` (**P0 gate**) |

**Key FootsiesGym finding:** H2H skill ≠ exploitability. EMAgnet beat PPO variants head-to-head yet was **most exploited** by approximate BR. Cemini mirrors this with `exploitability_advisory` in `axis_summary.json` (advisory only — not a submit fail).

## Lightweight-agent recipe (2607.06854)

Graded against a **fixed expert outside the train loop** (never train on the yardstick).

| Helps | Fails / skip |
|-------|----------------|
| Trust-region / disciplined updates | Dense short-term reward shaping |
| Rising opponent curriculum | Live LLM as train opponent (too slow) |
| Warm-start + **keep best checkpoint** | Capacity chase (wider/deeper nets) |
| Well-aimed sparse reward | Imitation / DAgger (causal confusion) |

**Ceiling is information-bound, not capacity-bound.** Fair ISMCTS (hidden cards re-dealt) stayed weak; oracle search with true hidden cards jumped. For Cemini: prefer tougher villains + best-checkpoint discipline over raising MC sample counts or model size.

## Cemini do / do-not

**Do**

1. Export trajectory + `axis_summary.json` every Researcher / HU gate run.
2. Grade against fixed local yardsticks (rock, lag, TEN, maniac_shark) — not live ladder TrueSkill as a train target.
3. Flag skill-vs-yardstick disconnect via `exploitability_advisory`.
4. Keep M₈/M₉ submit gates; treat exploitability as advisory.

**Do not**

1. Replace pokerkit with FootsiesGym or any fighting-game env.
2. Train / tune decide() against the live ladder TrueSkill yardstick.
3. Assume bigger MC / bigger nets break the information ceiling.
4. Claim villain private state in reasoning (privileged-feature leak).

## Related

- `@wiki/concepts/poker-arena-multi-axis-cognitive-profile.md`
- `@wiki/sources/arxiv-footsiesgym-2607.06514-2026-07-09.md`
- `@wiki/sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md`
- `briefs/2026-07-09_k151-footsiesgym-benchmark-steal.md`
- `briefs/2026-07-11_k152-expert-yardstick-forgetting-regret-steal.md`
- `references/expert-yardstick-pool.md` (K152 frozen pool + forgetting regret)
- `examples/researcher_trajectory_summary.py`
