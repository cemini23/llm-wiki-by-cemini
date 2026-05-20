---
title: "Jim Simons interview — Using Mathematics to Make Money (Journal of Investment Consulting Masters Series, 2023)"
type: source
tags: [source, interview, quant-finance, renaissance-technologies, jim-simons, masters-series, ssrn, k55]
keywords: [jim-simons, renaissance-technologies, medallion-fund, chern-simons, peter-brown, flatiron-institute, math-for-america, hiring-philosophy, one-model-continuously-improved, data-mining, machine-learning, quant-hiring]
related:
  - concepts/quant-finance.md
  - concepts/hiring-quant-talent-philosophy.md
  - entities/people/jim-simons.md
  - entities/companies/renaissance-technologies.md
maturity: validated
read_status: deep-read
created: 2026-05-20
updated: 2026-05-20
clusters: [quant-finance, hiring]
---

## Relations

- @concepts/quant-finance.md — corpus-index home
- @concepts/hiring-quant-talent-philosophy.md — synthesized concept on the Simons / RenTech approach
- @entities/people/jim-simons.md — interview subject (founder of Renaissance Technologies; deceased May 2024 — post-dates this 2023 interview)
- @entities/companies/renaissance-technologies.md — firm entity

## Raw Concept

- **Title**: "James H. Simons, PhD: Using Mathematics to Make Money"
- **Series**: The Journal of Investment Consulting, Masters Series — Volume 22, Number 1 (2023)
- **Publisher**: Investments & Wealth Institute (reprinted with permission)
- **Format**: 8-page reprint of a roundtable interview conducted September 2022
- **SSRN**: https://ssrn.com/abstract=4668072
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/ssrn-4668072.pdf`
- **Retrieved**: 2026-05-20 (dropped into `research to be indexed/`)
- **Interviewers**: Inna Okounkova (Columbia, editor-in-chief), Edward Baker (Mesirow Financial), Ludwig Chincarini (USF / US Commodity Funds), Arun Muralidhar (Mcube Investment Technologies), Margaret Towle (Yakima River Partners)

## Narrative

Roundtable interview with James H. Simons (1938-2024), founder of Renaissance Technologies and the Medallion Fund — the highest-returning hedge fund vehicle on record. Conducted September 2022, published 2023. Covers Simons' career arc from differential geometry (Chern-Simons forms, 1968 *Minimal Varieties in Riemannian Manifolds* in *Annals of Mathematics*) through cryptanalysis at the Institute for Defense Analyses through founding Renaissance, alongside his philanthropic activities (Simons Foundation, Flatiron Institute, Math for America).

### Headline operational claims (from a primary source)

The Cemini-relevant material — Simons' direct statements on how Renaissance is run — sourced verbatim:

**Hiring philosophy** (the single most-cited claim from this interview):
> "We look for mathematicians and scientists and statisticians. **We don't look for anyone who has worked in the financial industry before.** We look for very good scientists who are interested in making some money, and we interview them."

**On interview style** (anti-fast-thinking, pro-deep-thinking):
> "I believe there's too much emphasis on a person's being able to answer questions quickly when being interviewed. I remember a guy who gave slow answers during his interview, but it seemed to me he would be a good addition to our firm. So I called his thesis advisor at Harvard ... 'He chose to work on the hardest one and did a great job.' I overruled the interviewing group and said, 'We're going to hire this guy.' And he was very good indeed."

> "I would never have done well at a math competition. I'm not an extremely fast thinker myself; I just work hard. ... A paper of mine that was published in 1968 took me five years to write. But it has had 1,850 citations in the mathematics literature."

**Model architecture** (the "one continuously improved model" claim):
> "We have only one model, one system, which is improved continuously on the basis of new signals and market behavior in general."
- Asked if changes are reversed: "Yes, that can happen."
- On longevity: "Some aspects of it last for a very long time, others not as long, and some are just wrong from the beginning because we've mistaken noise for signal."

**Data mining** (explicit endorsement):
> "Yes, we do a lot of data mining. We have thousands of computers scouring data for information related to the movement of tradeable instruments. Sometimes what we find works, and sometimes it does not."

**Behavioral / fundamental signals** — explicit pure-quant position:
> Asked whether RenTech considers behavioral biases or other non-quant frames: "We stick to the math."

**Machine learning at RenTech**:
> "Machine learning has come a long way, and is very important to our work at Renaissance and at Flatiron."

**Why Medallion is hard to replicate**:
> "It's hard to replicate because it took thousands of person-years to build it."

**On crowding in quant**:
> "I think this has made it harder. The more quantitative funds there are, the more competition we'll have. ... You just have to try to stay ahead of the pack. We don't know what they're doing, but we know what we're doing, and we just have to get better and better at it."

**Visibility / publication policy at RenTech**:
> "I don't know of any scientists at Renaissance who have published papers in their field after coming to Renaissance."

**On separating signal from noise** (back-pocket answer):
> "The mathematics I did was essentially training my mind; none of it had anything to do with making money. Although Chern-Simons was wonderful, it does not help at all with making money."

**Compensation structure** at RenTech (implicit from a Flatiron-Institute analogy):
> "[The Flatiron researchers] get good salaries, and the best people get the highest salaries, more or less. ... [At Renaissance] collaboration has been extremely important. [And earlier] the secret sauce of what made you successful: hiring great people ... providing great infrastructure ... and sharing profits with everyone."

**Closing advice** to a young mathematician considering a finance career:
> "I would encourage mathematicians who want to make money, and I would direct them to apply to Renaissance and see if they could be hired there. I think there's still plenty of opportunity."

### Cemini-relevance angle

The Simons interview directly supports several existing Cemini orientations and would-be orientations:

1. **One-model-continuously-improved over many-strategies-tournament** — matches the "single primary controller + continuously-evolving strategy library" thesis already in `@concepts/cemini-deployment.md` and the conductor/librarian architecture. The interview is a primary source backing the structural choice.
2. **Math-first, no-trader-priors** — the interview is the cleanest single statement of "hire quant talent, not finance talent." Implications for any Cemini hiring or external collaboration decisions.
3. **Data mining is endorsed, not avoided** — Simons explicitly says they data-mine across thousands of machines. The conventional academic-finance disapproval of data mining is rejected here. Consistent with the Cemini approach of generating + testing large numbers of signals.
4. **Backtesting + walk-forward + ML** — RenTech uses all of it (Simons confirms ML matters at RenTech and Flatiron). No reason for Cemini to treat any of these as inferior to "fundamental" approaches.
5. **"Some aspects last a long time, others wrong from the beginning"** — primary-source justification for the kill-fast culture on Cemini strategies that turn out to be noise-fitting.

### Caveats

- The interview is **conversational**, not technical. No equations, no implementation details, no specifics about Medallion's signals or risk-management. Treat as a *philosophical* primary source, not a how-to.
- Specific dollar figures (Norwegian fund "$1.2 trillion under management") are conversational asides and should be cross-checked if used in any quantitative analysis. Not relied on here.
- Simons' framing of his own role is post-CEO (he stepped back from RenTech CEO 2009, sole CEO is Peter Brown). The "we" in his answers refers to RenTech-as-it-was-while-he-led-it; current Brown-era RenTech may differ.

## Snippets

> "We look for mathematicians and scientists and statisticians. We don't look for anyone who has worked in the financial industry before. We look for very good scientists who are interested in making some money, and we interview them." [Source: ssrn-4668072.pdf p.5]

> "We have only one model, one system, which is improved continuously on the basis of new signals and market behavior in general." [Source: ssrn-4668072.pdf p.4]

> "Yes, we do a lot of data mining. We have thousands of computers scouring data for information related to the movement of tradeable instruments. Sometimes what we find works, and sometimes it does not." [Source: ssrn-4668072.pdf p.4]

> "We stick to the math." [Source: ssrn-4668072.pdf p.4]

> "It's hard to replicate because it took thousands of person-years to build it." [Source: ssrn-4668072.pdf p.4]

> "I would never have done well at a math competition. I'm not an extremely fast thinker myself; I just work hard." [Source: ssrn-4668072.pdf p.5]

> "Machine learning has come a long way, and is very important to our work at Renaissance and at Flatiron." [Source: ssrn-4668072.pdf p.4]
