---
title: "WuBlockchain — Gate founder on custody: no single party can move funds alone"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/crypto-custody-single-point-of-failure.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Gate Founder Shares His Approach to Security: No Single Party Can Move Funds Alone |
| Author | Dr. Han (Gate founder and CEO), compiled by Wu Blockchain |
| Type | newsletter, RSS, sponsored-adjacent company essay |
| Location | `research to be indexed/substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md` |
| Retrieved | 2026-11-10 |
| File | substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md |
| Read status | read |

## Narrative

This is a first-person essay by the Gate founder, published through WuBlockchain. Treat the architecture description as a vendor claim. The loss statistics are the part worth checking.

### The loss statistics

- More than **600 security incidents** in 2026 so far, with losses above **$8bn**.
- **September** was the worst month at **$768m**, until October.
- October had passed **$6bn** before the month ended.
- More than **60% of first-half losses** came from **private-key compromise and phishing**. Code vulnerabilities account for a little over **10%**.

[Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

The split is the important number. Defence money that goes only to contract audits addresses about one tenth of the loss pool.

The essay also reports a supply-chain attack on hardware-wallet distribution channels in October that cost users nearly **$100m**.

### The proposed architecture

Gate proposes a **Vault** product with one rule: no single party can move funds alone.

- The private key is split into **three MPC shards**: user device, Gate, and a recovery partner. The complete key never exists.
- If Gate is compromised, the attacker gets one shard.
- If the user loses the device, Gate and the partner can help recover only after the user passes identity verification.
- Vault withdrawals have a **48-hour delay**, and the user can freeze during that window.
- If Gate disappears, the user can reconstruct with the device shard and the third-party shard using open-source tools.

[Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

### What is a claim and what is a test

`[TENTATIVE]` for every architecture statement. The post gives no audit, no independent review, and no test of the emergency-recovery path.

The claims that **can** be tested:

- Does the third-party shard holder actually exist as an independent entity?
- Do the open-source recovery tools exist and run offline?
- Is the 48-hour delay enforced server-side or client-side?

The first two are checkable today. The third needs a demonstration.

### Why it matters here

The essay names the failure mode that the Binance breach also showed: **a single point at the platform or a single point at the individual**. The proposed fix is a threshold, which is a general pattern. The same pattern applies to any custody design, including the key handling for a trading bot.

## Snippets

> "Over 60% of losses in the first half of the year came from private key compromises and phishing, where code vulnerabilities only account for a little over 10%." [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

> "No single party should be able to move your funds alone." [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

> "Both failing simultaneously is the only scenario that creates risk." [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

## Dead Ends

- **Reading this as an independent security analysis.** It is a company essay.
- **Assuming MPC removes counterparty risk.** The recovery partner is a second counterparty, not an absence of one.
