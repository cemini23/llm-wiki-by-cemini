---
title: "Wu Blockchain — Binance co-CEOs address the $6.34B hack"
type: source
related:
  - concepts/crypto-custody-single-point-of-failure.md
  - entities/data-sources/binance.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Binance Co-CEOs Address $6.34B Hack: Fake Job Interviews, Wallet Exploit, and Recovery Efforts |
| Author | Wu Blockchain (transcript of a public Binance Space) |
| Type | newsletter, RSS, interview transcript |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-11-25-binance-co-ceos-address-634b-hack-fake-job-inter.md` |
| Retrieved | 2026-11-25 |
| Published | 2026-11-25 |
| Read status | read |

## Narrative

### The incident

On 30 October, attackers compromised an internal wallet-signing service and bypassed normal withdrawal procedures to take about **$6.34 billion** in crypto assets. About **$2.85 billion** was frozen or intercepted by the time of the discussion. Binance says it will cover all losses and has replenished about 98 percent of affected token balances. [Source: substack-rss-wublock-2026-11-25-binance-co-ceos-address-634b-hack-fake-job-inter.md]

Every figure, attribution and recovery claim in this source comes from Binance executives. The newsletter says so: these are public statements, not independently verified findings.

### How the breach happened

A software engineer was contacted on a legitimate recruitment platform by someone posing as a project lead. Two interviews followed, the second impersonating a fictitious company's chief executive. Near the end the engineer was asked to download a coding assignment onto a work laptop. The repository contained malware that executed during installation, replaced legitimate development-tool components, and called attacker-controlled servers. Binance believes the malware was previously unknown and evaded third-party endpoint security.

Binance says its security team blocked 57 suspected North Korean cyberattacks in 2026.

### The transferable lesson

Suspending withdrawals stopped new requests but did not revoke on-chain permissions the attackers had already established. Revoking them required separate on-chain transactions. Because the hot wallets used multiparty computation, no single complete key existed to sign the revocations, so engineers had to build a revocation process under time pressure. Containment took hours.

That is the lesson Binance says it wants other platforms to hear: an on-chain authorisation survives an off-chain withdrawal freeze, and an MPC wallet has no single key for an emergency revoke.

### Remediation and strategy

Immediate steps by 3 November: rebuilt wallet systems in new environments, replaced compromised employee devices, revoked credentials, tightened access control. Longer term: stronger isolation between systems and employee devices, independent security reviews, more AI-based threat detection. Yi He says the industry should shift from speculation toward tokenised real-world assets and equity perpetuals.

### Read

Adds concrete detail to `concepts/crypto-custody-single-point-of-failure.md`: the recruitment-lure entry vector, the MPC revocation gap, and the on-chain-permission persistence. Treat all dollar figures as unverified statements.
