---
title: "Inside the trap: a renewal law for prefix-cache collapse in LLM agent serving (arXiv 2611.08902)"
type: source
related:
  - concepts/prefix-cache-collapse-agent-serving.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving |
| Author | Akshat Valse; Ali Jannesari (Iowa State University) |
| Type | arXiv preprint (cs.DC) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf` |
| Retrieved | 2026-11-09 |
| File | `arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf` |
| Pages | 66 |
| Read status | read |

## Narrative

Prefix caching lets an LLM agent reuse the key–value (KV) state of the previous turn. A follow-up turn whose prefix is still cached prefills only its new tokens. In this workload a hit prefills 551 tokens and a miss prefills about 11,100. The gap is about a factor of 16 in prefill work per session.

The cached KV belongs to sessions that sit idle in tool calls. Admitting waiting work evicts it. A burst of new sessions can tip the engine into a state where **every turn misses**. Then the queue grows, the gap between a session's turns grows with it, and idle KV is evicted before its owner returns. The engine stays in this state even at a load it carried from empty.

### The registered stampede test

The test runs on SGLang 0.5.22 and vLLM 0.32.0, on one A100 or H200, serving Qwen2.5-7B-Instruct or Llama-3.1-8B-Instruct. Each arm runs on a fresh server. A 200-session burst arrives within 60 s at 1200 s into the run.

| Arm | Outcome |
|---|---|
| BURST | zero cache hits to the end of the run in all 30 runs, 7500 s after the burst |
| NOBURST | good for the full 8700 s in every matched run |
| CAPPED | client-side session cap prevented the trap in all 30 runs |

The five paired tests passed at nine of ten rates. A dose response exists: bursts of 25 and 40 sessions stayed good, bursts of 60 and 100 left the engine stuck.

### Why the intuition fails

A quasi-static model treats the trapped state as the falling branch of a throughput curve. On these engines that reading is wrong in two ways. Trapped turns all miss, so the engine prefills at the all-miss token rate. Yet sessions complete **faster** than the all-miss capacity, by up to 2.4 times in one run. The turns that get served are young and short.

The paper idealises the trapped engine as a fluid FIFO server on which every turn misses and every turn rejoins the tail of the queue. Along FIFO orbits the cycles obey a linear renewal recursion. Below the all-miss capacity the trap drains, as classical theory says. Above it, a Perron root fixes the dynamics: every trapped state converges to a self-similar regime where the gap between turns grows linearly.

The operational consequence is the important part. **The throughput measured inside a trap overstates the recovery threshold.** In the CUT-A test, arrivals were cut to below the trapped throughput of the same seeds' uncut runs, but above the all-miss capacity. All three runs stayed trapped.

### Two exits

**Refuse arrivals.** The SHED test stops arrivals for 600 s or 3600 s. The short stop left the engine stuck (2 of 2 runs). The long stop recovered it (2 of 2 runs, 355 to 378 sessions refused).

**Cap sessions.** A client-side FIFO session cap at about the peak of the closed-population throughput curve rescued 9 of 9 established traps at the same load. No session was shed, and the engine stayed good after release.

### Defensive reading

The paper describes an availability failure without naming an attacker, and the failure has a security shape. A **short burst of new sessions is a cheap input** that can collapse a shared agent-serving pool and keep it collapsed. The pool does not recover when the burst ends. The defensive control is admission control: a session cap sized to the throughput curve, plus a check for the all-miss state before any capacity decision.

The second defensive point is about metrics. A dashboard that watches sustained throughput will show a trapped engine as healthy. The signal to watch is the prefix-cache hit fraction and the backlog slope, not the completion rate.

### Limits

The authors state that they do not prove the engine converges to the model. The workload is synthetic, with exponential 5 s tool times and no shared prefixes. The models are dense and 7 to 8B in size. The paper is a performance study, not a security evaluation, and no adversarial actor is modelled.

## Snippets

> "A 200-session burst left the engine at zero hits to the end in all 30 runs, while every matched no-burst run stayed good and a session cap prevented the trap in all 30 capped runs." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]

> "A cut in arrivals to below the trapped throughput of the same seeds' uncut runs, but above the all-miss capacity, left all three CUT-A runs trapped." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.2]

> "A session cap restores reuse: in registered tests it rescued 9 of 9 established traps at the same load without shedding, and the engine stayed good after release." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]

> "In our workload a hit prefills 551 tokens and a miss about 11,100, and a session's prefill work with every turn missing is about 16 times that with every follow-up hitting." [Source: arxiv-2611.08902-inside-the-trap-a-renewal-law-for-prefix-cache-c.pdf p.1]
