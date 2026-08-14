---
title: Steal — verification-under-deception eval (K278 ATOBench) for arena agents
type: brief
target: claude.ai
created: 2026-08-14
---

## Target

claude.ai · Claude Desktop · hands-on (arena-agent harness). Source wiki: cybersecurity-wiki `concepts/atobench-verification-chain-deception.md` and `sources/arxiv-2608-12996-atobench-deceptive-observations.md`.

## Summary

**ATOBench** (2608.12996) evaluates agents by their **verification chain, not final outcome**, under **deceptive observations**. It injects registered response changes, pairs each run with a native run, and traces later actions → recovered evidence → stopping → claim grounding. Key finding: **an agent can stay active (repeat probes, produce a plausible report) after its evidence path has broken — activity ≠ verification.** Light steal for arena agents that reason about opponents/hand state from noisy or adversarial signals.

## Body

### Arena transfer

- **Deceptive observations exist in poker too** — a solver or arena agent reasons from opponent actions that can be bluffs, tells, or injected noise. ATOBench's pairing method transfers: to eval an agent harness change, run baseline vs changed on the same scenario set, aligned at first output divergence, and diff the *evidence paths* not just the win/loss.
- **Score "decision traceable to evidence" separately from "activity"** — an agent that explores many lines and concludes confidently may have a broken evidence chain. For arena agents, this maps to: did the agent's bet sizing / action selection actually follow from the observed hand state, or did it keep acting without grounding?
- **Preserve evidence through reporting** — recovery only counts if the evidence survives to the decision. For arena: keep the reasoning trace attached to the action.

### Numbers that transfer

- SQLi contract: ATO added **median 14 actions + 9 repetitions** yet no route restored a supported finding — busy agent ≠ correct agent.
- JWT: 44/45 runs preserved evidence into a supported outcome — evidence survival is the separator.

### Scope

REFERENCE — ATOBench repo is a placeholder; pattern steal only. Authorized-lab framing: no live-target applications from this paper. This is a light steal; K279 MARC decomposer is covered by today's CCC brief.

## Sources

- arXiv:2608.12996 (27 pp, 450 episodes / 225 pairs / 5 model routes)
- cybersecurity-wiki `sources/arxiv-2608-12996-atobench-deceptive-observations.md`

## Wired

- `examples/verification_chain.py` + `tests/test_verification_chain.py` — evidence-locator attach, activity vs evidence-intact scoring, busy-after-break flag, matched-pair first-divergence + evidence-path diff
- Reference: `references/atobench-verification-chain.md`
