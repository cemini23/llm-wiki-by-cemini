# Anytime-valid agent eval stopping (K226/K257)

Stop HU/sandbox agent comparisons when an anytime-valid confidence
sequence + variance-reduced payoffs certify the gap — not at a fixed
hand budget. AIVAT-style value baselines cut payoff variance; that is
what buys the shorter eval, not a looser significance bar.

## Steal

1. Prefer variance-reduced payoffs + anytime-valid confidence sequences
   over fixed hand budgets.
2. Record stop metadata + paired logs so a third party can recheck the
   stopping decision (estimator, bound halfwidth, n_hands, reason).
3. Guard the online value model so it never peeks at the current hand
   being evaluated.
4. Keep the TrueSkill / nine-axis framing; AV stopping only decides
   *when* to stop comparing, not the ranking method.

## Do not

- Stop early with an ordinary confidence interval — it invalidates
  coverage (deciding to stop from running outcomes is an
  optional-stopping violation).
- Quote the ~74x HUNL hand savings (AsympCS, arXiv 2608.06362) as Arena
  EV — it is the paper's claim for their games, not this Arena's.
- Install any TrajDebug / AV-AIVAT / PTC runtime (no usable public
  poker code in this batch).

## Sources

- arXiv 2608.06362 (AV-AIVAT / anytime-valid stopping)
- `briefs/2026-08-07_k226-av-aivat.md`
- `briefs/2026-08-07_k257-av-aivat-anytime-valid-stopping.md`
- `examples/eval_stop_metadata.py`
