---
title: "Software engineering at Google and CS education with Titus Winters"
type: source
tags: [source, newsletter, ai-coding, cs-education, refactoring]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Software engineering at Google & CS education with Titus Winters |
| Source | The Pragmatic Engineer |
| File | `newsletter-rss-pragmatic-engineer-2026-10-29-software-engineering-at-google-cs-education-with.md` |
| Retrieved | 2026-11-01 |
| URL | https://newsletter.pragmaticengineer.com/p/software-engineering-at-google-and |
| Read status | read |

## Narrative

This page records a Pragmatic Engineer podcast summary. The file dates the post to 2026-10-29. The guest is Titus Winters. He spent more than a decade at Google, led the readability program, and built Abseil. He is now a Senior Principal Scientist at Adobe. The episode covers a large C++ refactor, mandatory tests, readability review, AI productivity, and the undergraduate computer science curriculum.

In 2010, a few months after Titus joined Google, a team of a dozen people cleaned old C++ code. The source says Google then had close to 250M lines of code, edited by 10,000 engineers. The team parsed each build target into an abstract syntax tree with MapReduce, matched call patterns, generated edits, kept the old API and the new API side by side, split the edits by directory, blocked the old pattern, and then deleted the old API. The source says the clang-format toolkit exists because this refactor needed it. These counts come from this one newsletter.

Around 2007, Search could no longer ship each month. The best cadence was quarterly. The source says almost every change at Google touched Search code, including a change to Gmail. Google then required a test with every change. Over time, Search returned to a higher cadence. A change also needed two sign-offs: a file owner, and a readability reviewer for that language. When Titus left Google three months before this episode, the source says 10,000+ engineers were enrolled in readability at any given time.

The source reports what Titus hears from engineers at other companies. Code output is up hugely versus a year ago. Outages are up about 30%. The number of features shipped is static. He still treats AI as a net productivity gain when teams start work they did not attempt before. He says a codebase is unsustainable when people cannot make a valuable change safely, and that safety nets remove that fear. These figures are a single-source claim from this conversation.

Titus was the only working engineer on the steering committee for the 2023 ACM/IEEE/AAAI computer science curriculum guidelines. He says most of the US undergraduate curriculum should be replaced. He says it has not changed in substance since around 2000, and that testing and verification are absent. Professors tell him that the best students use AI as a patient tutor, that students below a B grade tend not to understand the code at all, and that the weakest students can reach the middle mostly by producing slop with AI. He would grade prompts and tests, because those show how a student builds and checks software. He compares AI to an axe: the person does the work, and the tool carries that person's will. He tells students to go deep on work that is unique to them.

A coding-harness practitioner can use the 2010 sequence as a control pattern for an agent rewrite: parse, match, generate, coexist, shard, block, and delete. The same source says more generated code can raise outages while the feature count stays flat, and that tests are the safety net that lets a team change code without fear.

## Snippets

> "Titus talks to engineers at other companies and it’s the same picture: code output is up hugely versus a year ago, and outages are also up about 30%, while the number of features shipped is static. It seems like treading water." [Source: https://newsletter.pragmaticengineer.com/p/software-engineering-at-google-and (retrieved 2026-11-01)]
