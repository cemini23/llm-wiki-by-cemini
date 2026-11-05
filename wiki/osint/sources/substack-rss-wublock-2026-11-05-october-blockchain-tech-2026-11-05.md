---
title: "Wu Blockchain — October blockchain tech: Bitcoin Core v32.1 and the post-quantum question"
type: source
tags: [source, newsletter, bitcoin, ethereum, protocol, security]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | October Blockchain Technology Update |
| Source | wublock |
| Author | GaryMa, Wu Blockchain |
| Published | 2026-11-05 |
| Read status | skimmed (Bitcoin section) |

## Narrative

### Bitcoin Core v32.1

**v32.0 was tagged but never fully released** after last-minute issues. v32.1 is the release that actually shipped.

Content:

- Parallellised block validation, and mempool-based fee estimation.
- **Fixes a potential IP-address leak** affecting transactions broadcast through `sendrawtransaction` under `-privatebroadcast=1`.
- Transaction relay rate limiting was **redesigned around a global backlog**, to reduce CPU and memory pressure during volume bursts.

**The IP-leak fix is the one to keep.** It means that until v32.1, a node using private broadcast could leak the originating IP of a transaction it relayed. That is a deanonymisation path in a feature whose whole purpose is privacy.

### The disclosure policy change

Bitcoin Core updated its security disclosure policy: **vulnerabilities that are easy to rediscover — including with LLM-based tooling — will now be backported across maintained releases and disclosed more quickly**, rather than waiting for the traditional long embargo.

That is a direct response to LLMs making vulnerability rediscovery cheap. An embargo that assumes rediscovery is expensive stops working when it is not, and the policy moved accordingly.

**This is the most transferable finding in the piece.** Any disclosure policy with a fixed embargo window now rests on an assumption that model-assisted analysis has already broken.

### Coinbase's post-quantum proposal

An **institutional technical recommendation, not a consensus decision**, arguing that a Bitcoin post-quantum migration could take years and should be prepared well in advance.

It suggests:

- Exploring extensible signing paths — **BIP-360 (P2MR)** and **P2TRv2**.
- A **staged transition** where conventional and post-quantum signatures coexist.
- Evaluating impact on block space, verification performance, and institutional MPC custody.
- A **separate policy discussion** for coins that cannot migrate in time — lost keys, long-dormant holdings.

That last bullet is the hard one and the proposal names it rather than deferring: a post-quantum migration is also, unavoidably, a decision about who owns abandoned coins.

**Caveat.** Bitcoin section only; the Ethereum section and remainder were not read.

## Snippets

> "v32.1 fixes a potential IP-address leak affecting transactions broadcast through sendrawtransaction under -privatebroadcast=1." [retrieved 2026-11-05]

> Vulnerabilities "easy to rediscover, including with LLM-based tooling, will now be backported across maintained releases and disclosed more quickly". [retrieved 2026-11-05]

## Dead Ends

- **Treating the Coinbase proposal as a network decision.** It is an institutional recommendation.
