---
title: Crypto custody — the single point of failure and the threshold fix
type: concept
related:
  - entities/companies/circle.md
  - sources/substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md
  - sources/substack-rss-wublock-2026-11-06-wublockchain-weekly-democratic-win-triggers-mark.md
  - sources/substack-rss-wublock-2026-11-07-weekly-project-updates-aave-rolls-out-fixed-rate.md
  - sources/substack-rss-wublock-2026-11-08-asias-weekly-top10-crypto-news-pboc-to-probe-sol.md
updated: 2026-11-10
---

## Raw Concept

Where crypto assets are lost, and what a threshold-key design changes. Prompted by the Gate essay and the Binance incident report in the same wave.

## Narrative

### Where the losses are

The 2026 loss split is the load-bearing number.

| Cause | Share of first-half 2026 losses |
|---|---|
| Private-key compromise and phishing | over 60% |
| Code vulnerabilities | a little over 10% |

Scale: more than **600 incidents** in 2026, above **$8bn** of losses. September was **$768m**, the worst month until October, which passed **$6bn** before month end. [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

The implication is direct. A defence budget weighted toward contract audits addresses about one tenth of the loss pool.

### Two single points

Every custody model has one of two single points:

- **The platform.** Exchange assets are pooled, so the exchange is the highest-value target.
- **The individual.** One lost seed phrase, one phishing signature, one compromised device has no undo.

The Binance incident shows a third path that ends in the same place. The attack started with a fake job interview and a malicious project, moved through internal AI tools to reach other engineers, then used stolen credentials to deploy containers against wallet signing services. It ended with an **EIP-7702 delegation** that let attacker contracts move funds.

Two transferable lessons:

1. **A withdrawal halt is not containment.** The on-chain authorisation stays live. Binance needed a separate revocation procedure. [Source: substack-rss-wublock-2026-11-06-wublockchain-weekly-democratic-win-triggers-mark.md]
2. **Internal AI tooling is a lateral-movement path.** The tools were not the infection vector, but they were the pivot.

### The threshold design

Gate proposes a three-shard MPC vault:

| Property | Stated design |
|---|---|
| Key form | 3 MPC shards: device, Gate, recovery partner |
| Complete key exists | never |
| Platform compromise | attacker holds one shard |
| User loss | recovery requires Gate plus partner plus user identity check |
| Withdrawal delay | 48 hours, freezable by the user |
| Platform failure | user reconstructs with device and partner shards, open-source tools |

[Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

### What the design does and does not fix

It fixes **one-sided movement**. It does not remove counterparty risk, because the recovery partner is a second counterparty. It also adds a recovery procedure with its own attack surface.

Three claims are testable and none is tested in the post:

- `[NEEDS VERIFICATION 2026-11-10]` — is the third-party shard holder a legally independent entity?
- `[NEEDS VERIFICATION 2026-11-10]` — do the open-source recovery tools exist and run offline?
- `[OPEN QUESTION 2026-11-10]` — is the 48-hour delay enforced server-side or only in the client?

### The operational conflict

Safety rules and liquidity rules pull against each other. Korea is considering a **99% cold-wallet ratio**, up from 80%. With a higher cold ratio, hot-wallet balances shrink, and withdrawals slow. Bithumb already had a 13-hour delay in August. [Source: substack-rss-wublock-2026-11-08-asias-weekly-top10-crypto-news-pboc-to-probe-sol.md]

A custody design that promises instant exit and a 99% cold ratio cannot both be true.

### Applying it to a trading bot

The same threshold logic applies to key handling:

- never hold a single key that can move the whole balance;
- separate the signing key from the execution host;
- set a withdrawal path that needs two independent approvals;
- log every authorisation change, including token approvals.

## Snippets

> "Over 60% of losses in the first half of the year came from private key compromises and phishing, where code vulnerabilities only account for a little over 10%." [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

> "Binance stated that suspending withdrawals could not immediately stop the established on-chain malicious authorizations." [Source: substack-rss-wublock-2026-11-06-wublockchain-weekly-democratic-win-triggers-mark.md]

> "No single party should be able to move your funds alone." [Source: substack-rss-wublock-2026-11-10-gate-founder-shares-his-approach-to-security-no.md]

## Dead Ends

- **Treating MPC as risk removal.** It converts one single point into three, plus a recovery counterparty.
- **Listing "halt withdrawals" as full containment.** On-chain delegations survive the halt.
