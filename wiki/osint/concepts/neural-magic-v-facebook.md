---
title: Neural Magic, Inc. v. Meta Platforms, Inc. (formerly v. Facebook, Inc.)
type: concept
tags: [concept, legal, case-law, trade-secret, dtsa, mutsa]
keywords: [neural magic, meta, facebook, zlateski, dtsa, mutsa, trade secret, sparse neural network, cpu inference, casper, d mass, 20-cv-10444, 659 f supp 3d 138, ai trade secret, economic value from secrecy]
related:
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/defend-trade-secrets-act.md
  - concepts/ip-sale-readiness.md
  - concepts/ip-sale-corporate-structure.md
  - entities/platforms/mercury.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/fintech-startup-legal-ip-roadmap.md — K7 para 25 cites this case as evidence of the **economic-value-from-secrecy burden** that DTSA plaintiffs carry, and as precedent that DTSA enforcement against well-resourced AI defendants is procedurally tractable
- @concepts/defend-trade-secrets-act.md — parent statutory framework; this case is the AI/ML-context precedent that animates the K7 trade-secret-over-patent strategic positioning
- @concepts/ip-sale-readiness.md — case-precedent backdrop for the IP-sale-prep window's trade-secret-defense posture
- @concepts/ip-sale-corporate-structure.md — the *Neural Magic* fact pattern (employee-departure trade-secret-leakage) is precisely the threat model that the dual-entity HoldCo / OpCo segregation + Intercompany IP License Agreement address structurally
- @entities/platforms/mercury.md — co-promoted K7-tail concept-promotion 2026-04-27 sibling page (rejected-banking-alternative for the dual-entity stack); kinship marker only — no direct case-precedent semantic relationship

## Raw Concept

Case-docket framing: **Neural Magic, Inc. v. Meta Platforms, Inc.** (originally captioned v. Facebook, Inc.; renamed when Meta rebranded), No. **1:20-cv-10444-DJC**, **U.S. District Court for the District of Massachusetts**, before **Judge Denise J. Casper**. Reported summary-judgment ruling at **659 F. Supp. 3d 138 (D. Mass. 2023)**.

K7 (@sources/fintech-startup-legal-ip-roadmap.md para 25) cites this case as the single AI/ML-context precedent in the Cemini corpus for two propositions: (a) DTSA enforcement against a major-tech defendant is procedurally viable for an AI startup; (b) the plaintiff's burden to prove the trade secret derives **actual economic value from its secrecy** requires meticulous documentation. Detailed case facts below verified externally via Exa search 2026-04-27 against Reuters reporting + casemine + vLex docket records.

## Narrative

**[CONFIRMED — 2026-04-27 K7 deep-read + Exa primary-source verification] case-law precedent.** Procedural posture: settled with prejudice on confidential terms August 9, 2023, after summary judgment was denied March 6, 2023.

### Parties and counsel

- **Plaintiff**: Neural Magic, Inc. ("NMI") — Somerville, Massachusetts AI startup founded by former MIT researchers Nir Shavit and Alex Matveev. Investors included Andreessen Horowitz, VMware, Comcast, Verizon. NMI's core technology was algorithmic optimizations enabling **sparse neural networks to run inference efficiently on commodity CPUs** (no GPU required), reportedly delivering 3–7x speedups over competing frameworks.
- **Defendants**:
    - **Meta Platforms, Inc.** (formerly Facebook, Inc.) — alleged downstream user of misappropriated trade secrets
    - **Dr. Aleksandar Zlateski** — former NMI employee + computer scientist; MIT Ph.D. (Shavit served on his thesis committee); allegedly disclosed NMI trade secrets to Meta after leaving
- **Judge**: Hon. Denise J. Casper, U.S. District Judge

### Procedural timeline

| Date | Event |
|---|---|
| 2020 | Neural Magic files complaint against Facebook, Inc. + Zlateski in D. Mass. |
| (post-2021) | Case caption updated to v. Meta Platforms, Inc. following Facebook → Meta rebrand |
| March 6, 2023 | Judge Casper **denies** Meta's motion for summary judgment on Counts I (MUTSA) and II (DTSA) for **40 of 41 alleged trade secrets**; allows expert testimony quantifying damages at up to **$766 million in royalties**; grants summary judgment to defendants on the non-compete + Ch. 93A unfair-business-practices counts. Reported at **659 F. Supp. 3d 138**. |
| August 9, 2023 | Parties file joint dismissal with prejudice; **case settled on confidential terms** (jury trial had been set for September 2023) |

### Counts pleaded

NMI's operative complaint (D. 109) alleged five counts:

1. **Count I**: Misappropriation of trade secrets in violation of the **Massachusetts Uniform Trade Secrets Act (MUTSA)**, Mass. Gen. L. c. 93, § 42
2. **Count II**: Misappropriation of trade secrets in violation of the **Defend Trade Secrets Act (DTSA)**, 18 U.S.C. § 1836 et seq.
3. **Count III**: Unfair and deceptive business practices in violation of **Mass. Gen. L. c. 93A, § 11**
4. **Count IV** (Zlateski only): Breach of the non-disclosure and non-competition provisions of his NMI employment contract
5. **Count V** (Meta only): Tortious interference with NMI's advantageous contractual relations with Zlateski

Counts I + II + IV survived summary judgment and proceeded toward trial. Counts III + the non-competition portion of Count IV were dismissed at summary judgment.

### Factual background

NMI's allegations (as the case ultimately framed them at summary judgment):

- Zlateski conducted research on speeding up neural networks on CPUs at MIT before joining NMI; this research was part of NMI's pre-founding intellectual landscape
- After joining NMI, Zlateski was exposed to and contributed to NMI's proprietary sparse-neural-network CPU-inference algorithms
- Zlateski signed standard NMI NDA and non-compete agreements
- Zlateski left NMI and joined Meta (then Facebook)
- At Meta, Zlateski allegedly used and disclosed NMI's trade secrets in Meta's internal AI work
- Meta allegedly **published portions of the algorithms on the open-source GitHub platform**, publicly thanking Zlateski for solving "a key problem" for Meta's AI advancement

The 41 alleged trade secrets covered specific algorithmic techniques for executing sparse neural-network inference efficiently on x86 CPUs — including the model architecture, the sparsity-pattern encoding, and the inference-runtime techniques.

### Why the case matters for Cemini-relevant DTSA analysis

K7's specific citation (para 25) frames *Neural Magic* as the precedent demonstrating the **economic-value-from-secrecy burden** that DTSA plaintiffs carry. Three case-specific findings carry forward into Cemini's posture:

1. **AI-algorithm trade secrets are cognizable under DTSA + state UTSA**. The court rejected Meta's argument that NMI's proposed trade secrets were not legally protectable. This forecloses a major defense theory for any future AI-defendant in DTSA litigation.

2. **Employee-departure-with-trade-secrets is the canonical fact pattern**. Zlateski's path from NMI to Meta with allegedly-misappropriated algorithms is the textbook DTSA fact pattern. For Cemini's threat model, the analogous future scenario is: a contractor or eventual hire leaves Cemini, joins a competitor, and brings algorithmic trade secrets with them. **The defensive posture is the prescribed combination of: (a) signed NDAs, (b) access controls limiting who-can-see-what, (c) audit logging of who accessed what when, (d) clear documentation of which algorithmic-IP elements are designated trade secrets**. See @concepts/defend-trade-secrets-act.md for the doctrinal framework + @concepts/ip-sale-corporate-structure.md K7 Phase 2 step 7 ("Implement Trade Secret Protocols") for the prescribed engineering pattern.

3. **The economic-value-from-secrecy burden is real and document-intensive**. The court allowed expert testimony that Meta owed up to $766M in royalties — a number that signals both the scale of damages available under DTSA and the depth of expert-witness preparation required to establish economic value. The expert built the royalty estimate from NMI's R&D investment + performance benchmarks + market-comparable royalty rates. **For Cemini, the analogous evidentiary substrate is the §174A-capitalized R&E records + backtest performance metrics + paper-trading P&L attribution + model-card documentation.** See @concepts/defend-trade-secrets-act.md Cemini-side application table.

4. **GitHub publication does not necessarily destroy trade-secret status if the disclosure was unauthorized**. Meta argued in part that publication on GitHub vitiated trade-secret status — the court rejected this argument because the disclosure was alleged to be the misappropriation itself, not a prior public disclosure by the trade-secret owner. This is doctrinally important because it means **a defendant cannot launder away DTSA liability by republishing the misappropriated trade secret to OSS channels**.

### Cemini-side relevance: structural defense via dual-entity HoldCo

The *Neural Magic* fact pattern (employee-departure trade-secret-leakage, downstream use by well-resourced corporate defendant, GitHub republication) is precisely the threat model that the @concepts/ip-sale-corporate-structure.md dual-entity prescription addresses **structurally**:

- **HoldCo holds title to the IP**: the natural plaintiff in a future DTSA action; HoldCo's standing is unambiguous because HoldCo is the owner of the asset
- **Intercompany IP License Agreement defines OpCo's authorized scope**: any disclosure outside the license's scope is misappropriation by definition; the contractual baseline is documented from day one
- **Trade-secret protocols at Phase 2 step 7** (encrypted servers legally owned by HoldCo; OpCo accesses only via secure API keys): the engineering-and-access-control regime that satisfies the "reasonable measures" element of DTSA's trade-secret definition
- **NDAs with all collaborators going forward**: the contractual layer that supports the "duty to maintain secrecy" element of misappropriation

### Settlement and posture

The case settled on confidential terms August 9, 2023, with prejudice — the trade-secret-status question was never ultimately adjudicated by a jury, but Judge Casper's summary-judgment denial established the doctrinal foothold that AI-algorithm trade secrets are cognizable under DTSA + MUTSA. The settlement amount is undisclosed; the $766M expert-testimony figure should be treated as the upper end of the **demand range** in cases of this scale, not as a representative settlement value.

### Out-of-scope for this page

Detailed claim-construction analysis of specific NMI trade secrets (the 40 that survived + the 1 that did not) is not material to Cemini's posture and is not reproduced here. The case is cited for its **doctrinal posture** and **fact-pattern relevance** as a Cemini-litigation-defense reference, not as a closely-analogous business-fact precedent.

## Snippets

### S1 — K7 citation (K7 para 25)
> "Recent litigation, such as the Neural Magic, Inc. v. Facebook, Inc. case, underscores that plaintiffs must prove the trade secret derives actual economic value from its secrecy, a burden that requires meticulous documentation of the algorithm's performance and market advantage."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 25. The single canonical citation in the Cemini corpus; frames the case as the economic-value-from-secrecy precedent.*

### S2 — Court-of-record case caption + counts (vLex / D. Mass. summary-judgment opinion)
> "Plaintiff Neural Magic, Inc. ("NMI") has sued Defendants Meta Platforms, Inc. ("Meta") and Dr. Aleksandar Zlateski ("Zlateski") (collectively, "Defendants"), a former NMI employee, for Zlateski's alleged disclosure of trade secrets to Meta and Meta's internal use and posting of same on an open-source forum, GitHub. ... NMI alleges that both Defendants misappropriated trade secrets in violation of the Massachusetts Uniform Trade Secrets Act ("MUTSA"), Mass. Gen. L. c. 93, § 42 (Count I) and the Defend Trade Secrets Act ("DTSA"), 18 U.S.C. § 1836 (Count II), and committed unfair and deceptive business practices in violation of Mass. Gen. L. c. 93A, § 11 (Count III). NMI also alleges that Zlateski breached the non-disclosure and non-competition provisions of his employment contract with NMI (Count IV) and that Meta tortiously interfered with its advantageous contractual relations with Zlateski (Count V)."
>
> *— Neural Magic, Inc. v. Meta Platforms, Inc., 659 F. Supp. 3d 138 (D. Mass. 2023) (Casper, J.), summary judgment opinion. [Source: vLex / case-law.vlex.com case record (retrieved 2026-04-27 via Exa).]*

### S3 — Procedural posture: SJ denied + $766M royalty expert allowed (Reuters, March 7 2023)
> "Meta will have to face a trial over accusations that it took Neural Magic's 'breakthrough' algorithms that enable AI systems to process information more quickly, U.S. District Judge Denise Casper said. ... The court also allowed testimony from an expert who said Meta owes Neural Magic as much as $766 million in royalties. ... Meta asked the court to throw out the case last year, arguing Neural Magic had failed to identify any protectable trade secrets and that Zlateski had not acquired the information improperly. But the court on Monday allowed Neural Magic's case to continue for all but one of the 41 secrets it accused Meta of misappropriating."
>
> *— Blake Brittain, "Meta must face trial over AI trade secrets, judge says," Reuters, March 7, 2023. [Source: https://www.reuters.com/legal/meta-must-face-trial-over-ai-trade-secrets-judge-says-2023-03-07/ (retrieved 2026-04-27 via Exa).]*

### S4 — Settlement on confidential terms (Reuters, August 9 2023)
> "Meta Platforms has settled a lawsuit brought by an artificial-intelligence startup that accused the tech giant of stealing its trade secrets, according to a filing in Boston federal court. Plaintiff Neural Magic and Meta said in the Tuesday filing that they had resolved the case on confidential terms and asked the court to dismiss it with prejudice, which means it cannot be refiled. ... The trial had been set to begin next month."
>
> *— Blake Brittain, "Meta settles startup's lawsuit over artificial-intelligence trade secrets," Reuters, August 9, 2023. [Source: https://www.reuters.com/legal/transactional/meta-settles-startups-lawsuit-over-artificial-intelligence-trade-secrets-2023-08-09/ (retrieved 2026-04-27 via Exa).]*
