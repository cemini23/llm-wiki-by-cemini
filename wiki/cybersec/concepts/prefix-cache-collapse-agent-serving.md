---
title: "Prefix-cache collapse: a burst can trap an agent-serving pool"
type: concept
related:
  - sources/arxiv-prefix-cache-collapse-renewal-law-2611.08902.md
updated: 2026-11-10
---

## Raw Concept

Question: **can a short burst of sessions permanently degrade a shared LLM agent-serving pool?** From arXiv 2611.08902, a registered measurement study with a renewal-law model of the trapped state.

## Narrative

LLM agents make many turns per session. Each turn sends the previous context plus new tool output. Prefix caching reuses the key–value state of the previous turn, so a follow-up turn prefills only its new tokens. In the measured workload a cache hit prefills 551 tokens and a miss prefills about 11,100 — a factor of about 16 in prefill work per session.

The cached state belongs to sessions that are idle inside a tool call. Admitting new work evicts it. That creates a positive feedback loop.

1. A burst of new sessions arrives.
2. Admission pressure evicts idle-prefix KV.
3. Returning sessions miss and prefill at the full length.
4. The queue grows, so the gap between a session's turns grows.
5. The longer gap evicts more KV, so more turns miss.

The engine settles into an **all-miss steady state** and does not leave it when the burst ends.

### Measured behaviour

A 200-session burst within 60 s left the engine at zero cache hits to the end of the run in all 30 runs, 7500 s after the burst. Matched no-burst runs stayed healthy for the full 8700 s. A client-side session cap prevented the trap in all 30 capped runs. There is a dose response: bursts of 25 and 40 sessions were absorbed, bursts of 60 and 100 were not.

### The counterintuitive part

Classical queueing says the trapped state is the falling branch of the throughput curve. On these engines it is not. Trapped sessions complete **faster** than the all-miss capacity, because the turns that get served are young and short. So the throughput read inside a trap is higher than the throughput a recovering system can sustain.

The operational trap follows. Cutting arrivals to below the trapped throughput but above the all-miss capacity leaves the engine stuck. Measured trap throughput overstates the recovery threshold.

### Controls

Two exits work, and they differ in cost.

| Exit | Mechanism | Measured result |
|---|---|---|
| Refuse arrivals (shed) | stop admitting sessions long enough to drain | 600 s stop failed (2/2 stuck); 3600 s stop recovered (2/2) |
| Cap sessions | client-side FIFO cap near the throughput-curve peak | rescued 9/9 established traps, no session shed, stayed good after release |

The session cap is the cheaper control. It restores reuse by keeping the admitted population inside the region where prefixes survive.

### Security reading

This is an availability failure with a cheap attacker input. No credential and no exploit are needed. A short burst of new sessions against a shared agent pool can collapse it and keep it collapsed. The victims are the sessions already in flight.

For a defensive team, three consequences.

- **Treat admission control as a security control.** A per-client session cap belongs in the threat model, not only in the capacity plan.
- **Watch the right metric.** Sustained throughput shows a trapped engine as healthy. Watch the prefix-cache hit fraction and the backlog slope.
- **Do not size recovery to the observed throughput.** Use the all-miss capacity measured with caching disabled as the reference rate.

### Limits

The authors state they do not prove the engine converges to their model. The workload is synthetic: exponential 5 s tool times, no shared prefixes, dense 7 to 8B models, one A100 or H200. The paper is a performance study and models no adversary. The link from a burst to an attack is an inference, not a tested claim in the paper.

Confidence: the burst-to-trap result is `[TENTATIVE]` — one lab, two engines, one workload shape. The attacker framing is `[OPEN QUESTION 2026-11-10]`: no one has measured a deliberate burst as an attack in production.

## Snippets

> "The cached KV belongs to sessions that sit idle in tool calls, and admitting waiting work evicts it. A burst of new sessions can therefore tip the engine into a state in which every turn misses, the queue grows, the gap between a session's turns grows with it, and idle KV is evicted before its owner returns." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]

> "A session cap restores reuse: in registered tests it rescued 9 of 9 established traps at the same load without shedding, and the engine stayed good after release." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]

> "In model F below, for our workload, a cut to just below the throughput measured in an all-miss trap does not clear it." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]
