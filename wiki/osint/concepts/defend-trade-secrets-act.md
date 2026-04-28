---
title: Defend Trade Secrets Act (DTSA, 18 U.S.C. § 1836 / § 1839)
type: concept
tags: [concept, legal, trade-secret, ip-sale, cemini-internal]
keywords: [dtsa, defend trade secrets act, 18 usc 1836, 18 usc 1839, trade secret, misappropriation, federal cause of action, ex parte seizure, exemplary damages, neural magic, mutsa, utsa, alice 101]
related:
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/ip-sale-readiness.md
  - concepts/neural-magic-v-facebook.md
  - concepts/milestone-ledger.md
  - concepts/cryptographic-audit-trail.md
  - concepts/section-174-rd-expensing.md
  - entities/platforms/mercury.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/fintech-startup-legal-ip-roadmap.md — K7 paras 23–25 are the **single canonical source** for this page; cite the DTSA (18 U.S.C. § 1839) as the federal pillar of the trade-secret-protection regime that algorithmic-trading firms should rely on **in lieu of** patent protection (which K7 argues is futile for AI/algorithm IP given §101 abstract-idea jurisprudence post-*Alice*)
- @concepts/ip-sale-corporate-structure.md — the Wyoming HoldCo (IP licensor under K7's prescribed dual-entity structure) is the natural plaintiff in any future DTSA action; trade-secret protection is the durable competitive moat that the HoldCo-segregation pattern formalizes
- @concepts/ip-sale-readiness.md — parent thesis; DTSA is the federal trade-secret enforcement instrument that backstops the IP-sale-prep window
- @concepts/neural-magic-v-facebook.md — DTSA case precedent demonstrating enforceability in AI/ML contexts; specifically cited by K7 para 25 as evidence that "plaintiffs must prove the trade secret derives actual economic value from its secrecy"
- @concepts/milestone-ledger.md — the milestone ledger / Git commit history is the **load-bearing trade-secret evidentiary substrate**: documents the "reasonable measures to maintain secrecy" element + supports the "economic value from secrecy" burden that *Neural Magic* makes load-bearing
- @concepts/cryptographic-audit-trail.md — sibling tamper-evident artifact pattern; the prescribed VCP/zkCA stack would supplement Git history as a cryptographically anchored secrecy-measure record
- @concepts/section-174-rd-expensing.md — sibling tax-treatment page; the same capitalized-R&E records that establish §174A small-business deduction also serve as the cost-of-development evidentiary substrate for the DTSA economic-value-from-secrecy burden — dual-purpose accounting documentation
- @entities/platforms/mercury.md — co-promoted K7-tail concept-promotion 2026-04-27 sibling page (rejected-banking-alternative for the dual-entity stack); kinship marker only — no direct DTSA-Mercury semantic relationship

## Raw Concept

The question this page answers: **How does Cemini protect its proprietary algorithm IP under federal law during the IP-sale-prep window, given that algorithm patents are not viable under *Alice* §101?**

Single-source canonical: derived from @sources/fintech-startup-legal-ip-roadmap.md K7 paras 23–25 only. K5 (3-9-pm-research) and K6 (3-10-ip-sale-audit) gesture at trade-secret protection without citing the federal statute by name. **Single-source claims should be flagged accordingly.** The case-precedent backing (Neural Magic v. Facebook/Meta) is verified externally via Exa search 2026-04-27 and detailed at @concepts/neural-magic-v-facebook.md.

## Narrative

**[CONFIRMED — 2026-04-27 K7 deep-read + Exa primary-source verification of Neural Magic precedent] doc-only.** Statutory + case-law framework. No engineering deliverable tied to this page; it captures the federal trade-secret enforcement regime that the prescribed corporate structure and milestone-ledger pattern feed into.

### What the DTSA is

The **Defend Trade Secrets Act of 2016**, codified at **18 U.S.C. § 1836** (private civil cause of action) and **18 U.S.C. § 1839** (definitions), is the federal civil cause of action for trade-secret misappropriation. It supplements (not preempts) state-law trade-secret statutes — every state except New York and North Carolina has enacted some version of the **Uniform Trade Secrets Act (UTSA)**, and Massachusetts has its own **MUTSA** (Mass. Gen. L. c. 93, § 42). Most modern trade-secret complaints plead DTSA + the relevant state-UTSA in parallel — exactly the pattern in *Neural Magic v. Meta* (DTSA Count II + MUTSA Count I; see @concepts/neural-magic-v-facebook.md).

K7's strategic positioning (paras 23–25): the DTSA + state UTSA + employment NDAs are the **federal/state/contractual three-layer protection regime** that Cemini should rely on **in lieu of patent protection**. K7's argument against patenting AI/algorithm IP:

- Patent registration mandates exhaustive public disclosure of mechanics
- Post-*Alice Corp. v. CLS Bank Int'l*, mathematical algorithms + abstract software concepts face severe patentability challenges under §101
- USPTO guidelines emphasize that AI-generated inventions without significant human ingenuity may not qualify at all
- Trade-secret law provides indefinite protection (vs. patent's 20-year term) **and** preserves secrecy (vs. patent's mandatory disclosure)

### Trade-secret definition (§ 1839(3))

A "trade secret" under DTSA is **any form of business or technical information** (formulas, methods, techniques, processes, programs, devices, etc.) that:

1. The owner has taken **reasonable measures to keep secret**, AND
2. Derives **independent economic value, actual or potential, from not being generally known to** and not being readily ascertainable through proper means by another person who can obtain economic value from its disclosure or use.

For an algorithmic trading firm, K7 para 24 specifies that the following all qualify as protectable trade secrets if reasonable secrecy measures are in place:

- **Neural network architecture** (model topology, layer composition)
- **Training-dataset composition + cleaning methodology** (the data lineage)
- **Hyperparameter configurations** (learning rates, batch sizes, regularization parameters)
- **Exact weight values of trained models** (the parameters themselves)
- **Orchestration topology** (how the trained models are wired into the trading pipeline)

### Misappropriation (§ 1839(5))

Misappropriation under DTSA covers three modalities:
- **Acquisition** by improper means (theft, bribery, misrepresentation, breach/inducement of breach of duty to maintain secrecy)
- **Disclosure** without consent by a person who used improper means or owed a duty of secrecy
- **Use** without consent by a person who used improper means or owed a duty of secrecy

The most common employment-context fact pattern (and the *Neural Magic* fact pattern): a former employee who owed a contractual duty of secrecy under an NDA leaves and brings the trade secret to a competitor. The new employer is liable under DTSA if it knew or had reason to know the information was acquired by improper means.

### Civil remedies (§ 1836(b)(3))

DTSA provides federal-court plaintiffs with:

- **Injunctive relief** — including affirmative acts to protect the trade secret
- **Compensatory damages** — actual loss caused by the misappropriation + unjust enrichment not addressed by actual loss, OR a reasonable royalty if neither is provable
- **Exemplary damages up to 2x the compensatory amount** for **willful and malicious misappropriation**
- **Attorneys' fees** for willful and malicious misappropriation, OR for bad-faith claim-or-defense
- **Ex parte seizure** (§ 1836(b)(2)) — the court may, on plaintiff's ex parte application, order seizure of property necessary to prevent the propagation or dissemination of the trade secret. This is unique to DTSA (state UTSA does not provide for it).

### Federal jurisdiction without diversity

Crucially for Cemini, DTSA establishes a **private right of action in federal court** for any trade secret used in interstate or foreign commerce — no diversity-of-citizenship requirement. A Cemini trade-secret claim against a defendant anywhere in the US can be brought directly in federal court (typically S.D.N.Y. or D. Mass. for AI/ML cases) without first establishing minimum contacts for diversity jurisdiction. This is a meaningful tactical advantage over pre-2016 state-court-only enforcement.

### Cemini-side application

The Cemini IP universe maps cleanly onto the DTSA trade-secret category, **provided** reasonable secrecy measures are documented:

| Cemini asset | DTSA category | Required secrecy measure |
|---|---|---|
| Trading algorithm source code | "method, technique, process" | Private repos; commit-signing; access-controlled deployment |
| Trained model weights | "device, formula" | Encrypted at rest; access via brokered API keys only |
| Training datasets + cleaning pipeline | "compilation, method" | Datasets stored in HoldCo-owned storage; lineage documented |
| Hyperparameter configurations | "formula, technique" | Stored in environment variables / secrets-manager, never in plaintext config |
| Orchestration topology (LangGraph state, Pydantic v2 schemas, MARL reward shaping) | "method, process" | Architecture documented internally only; published material is generic |
| Cryptographic audit trail pattern (prescribed @concepts/cryptographic-audit-trail.md) | "method, system" | The audit-trail design itself is documented internally; OSS-published components carry public licenses |

The **Wyoming HoldCo** (per @concepts/ip-sale-corporate-structure.md K7 prescription) is the natural DTSA plaintiff in any future enforcement action: HoldCo holds title to the source code, model weights, training data rights, and trade-secret protocols — meaning HoldCo has standing to sue. The OpCo, which licenses the IP under the prescribed Intercompany IP License Agreement, would be a co-plaintiff or have a derivative claim. **The structural decision to vest IP in a separate HoldCo is a DTSA-enforcement strategic decision as much as a tax/liability one.**

### The "reasonable measures" element — what the milestone ledger documents

K7 para 25 (citing Neural Magic) emphasizes that DTSA plaintiffs must prove **both** (a) the trade secret derives actual economic value from its secrecy, and (b) reasonable measures were taken to maintain that secrecy. The "reasonable measures" element is **highly fact-specific and document-intensive** in litigation:

- **NDAs with employees + contractors** (signed copies retained)
- **Access controls** on source code, model weights, datasets (audit-logged per-access)
- **Encryption at rest + in transit** (cryptographic protocols documented)
- **Need-to-know compartmentalization** (org-chart of who has access to what)
- **Physical security** for any on-premises servers (currently N/A — Cemini is Hetzner-cloud-hosted; cloud-vendor controls satisfy this dimension)
- **Audit trail** of what was disclosed and to whom (the cryptographic-audit-trail pattern, prescribed @concepts/cryptographic-audit-trail.md)

The **milestone ledger** (per @concepts/milestone-ledger.md) is the **load-bearing artifact** for satisfying this element in litigation: it documents both *what was developed and when* (the trade-secret content, with versioning) and *who had access to what at each point* (the secrecy-measure regime). The Git commit history itself is the minimum baseline; the prescribed Merkle-root-anchored ledger would be a tamper-evident superset that strengthens the secrecy-measure proof.

### The "economic value from secrecy" burden — what *Neural Magic* makes load-bearing

K7 para 25's specific citation to *Neural Magic v. Meta* is for the **economic-value-from-secrecy burden**: plaintiff must prove that the trade secret's value derives from the fact that competitors do not have it. In *Neural Magic*, the plaintiff supported this burden with:

- Trade-secret-specific R&D investment records (cost to develop)
- Performance benchmarks demonstrating competitive advantage (3–7x speedup on CPU inference vs. competing frameworks)
- Expert testimony on royalty value (allowed at trial; expert opined Meta owed up to $766M)

For Cemini, the analogous evidentiary substrate is:

- Capitalized R&E expense records (per @concepts/section-174-rd-expensing.md §174A regime — the same capitalized-cost record serves dual purposes)
- Backtest performance metrics (Sharpe, Sortino, max drawdown vs. published baselines)
- Live paper-trading P&L attribution (validating the algorithmic alpha is real)
- Model-card documentation of architectural choices that produce the alpha

### What DTSA does NOT do

- Does not preempt state-law trade-secret claims (most plaintiffs plead both)
- Does not create criminal liability (DTSA is the civil-side; the **Economic Espionage Act of 1996, 18 U.S.C. §§ 1831–1839** is the criminal-side framework, also enforced by DOJ)
- Does not protect against **independent development** by a competitor — if the competitor reverse-engineers the algorithm or develops it from scratch without access to the trade secret, no DTSA claim
- Does not protect against **disclosure under valid legal process** (subpoena, regulatory inquiry, etc.) — though protective orders can preserve secrecy in litigation

### Cemini deployment posture (2026-04-27)

| Component | DTSA prerequisite | Deployed | Gap |
|---|---|---|---|
| Trade-secret documentation regime | Reasonable measures must be documented | Informal (private repos, environment-variable secrets, cloud encryption-at-rest) | **Need formal Trade Secret Protocols document** (K7 Phase 2 step 7) |
| NDAs with collaborators | Signed contractual duty of secrecy | None (founder solo-operator currently) | **N/A until first hire / contractor** |
| Access logs | Audit-trail of who accessed what | Git commit history is the substrate; no access-log layer above | **Architectural — pairs with cryptographic-audit-trail prescription** |
| HoldCo as plaintiff | Wyoming HoldCo holds title | Not formed | **Pending HoldCo formation** |
| Capitalized R&E records | Cost-of-development evidentiary substrate | §174A election not yet exercised | **Awaiting tax-counsel engagement** |
| Performance-attribution records | Economic-value-from-secrecy substrate | Backtests run informally; no formal documentation | **Spot-check** |

## Snippets

### S1 — DTSA + economic-value-from-secrecy burden (K7 paras 24–25)
> "Trade secret law, governed federally by the Defend Trade Secrets Act (18 U.S.C. § 1839), provides indefinite legal protection for formulas, methods, techniques, and processes, provided they derive independent economic value from remaining secret and are subject to reasonable, documented measures to maintain their secrecy. For an algorithmic trading firm, the neural network architecture, the precise composition and cleaning methodology of the training datasets, the hyperparameter configurations, and the exact weight values of the reinforcement learning models all qualify as protectable trade secrets. ... Recent litigation, such as the Neural Magic, Inc. v. Facebook, Inc. case, underscores that plaintiffs must prove the trade secret derives actual economic value from its secrecy, a burden that requires meticulous documentation of the algorithm's performance and market advantage."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 paras 24–25. The single canonical citation in the Cemini corpus for the DTSA federal trade-secret regime + the *Neural Magic* economic-value-from-secrecy burden. See @concepts/neural-magic-v-facebook.md for the case-detail expansion.*

### S2 — Trade-secret over patent for AI (K7 para 23)
> "The debate between patent protection and trade secret classification is heavily skewed toward trade secrets in the context of artificial intelligence and algorithmic trading. Patent registration provides a powerful legal monopoly to exclude others from using an invention, but it mandates the exhaustive public disclosure of the underlying mechanics. Following the Supreme Court's landmark decision in Alice Corp. v. CLS Bank Int'l, mathematical algorithms and abstract software concepts face severe, often insurmountable challenges in meeting patentability thresholds. Furthermore, recent guidelines from the United States Patent and Trademark Office (USPTO) emphasize that inventions generated primarily by AI without significant, demonstrable human ingenuity may not qualify for patent protection at all."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 23. The strategic-positioning thesis statement: trade-secret protection is the durable competitive moat for AI/algorithm IP; patent protection is a strategic dead-end post-*Alice*.*
