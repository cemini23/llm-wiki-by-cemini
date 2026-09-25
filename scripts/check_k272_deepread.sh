#!/usr/bin/env bash
# K272 deep-read gate. Papers must be deep-read. Three pages stay skimmed.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
import re, sys
papers = [
"wiki/sources/arxiv-2609.29016-evotreenad-2026-09-25.md",
"wiki/sources/arxiv-2609.29035-bounded-coalescent-2026-09-25.md",
"wiki/sources/arxiv-2609.29333-llm-graders-2026-09-25.md",
"wiki/sources/arxiv-2609.29964-world-action-agent-2026-09-25.md",
"wiki/sources/arxiv-2609.30012-behavior-assays-2026-09-25.md",
"wiki/sources/arxiv-2609.30219-verified-commissioning-2026-09-25.md",
"wiki/sources/arxiv-2609.30249-rapid-2026-09-25.md",
]
hold = [
"wiki/sources/arxiv-2609.30266-trace-tamper-2026-09-25.md",
"wiki/sources/newsletter-rss-sterling-sky-2026-09-23-gmb-suspension.md",
"wiki/sources/newsletter-rss-tldrsec-2026-09-24-347.md",
]
news = [
"wiki/sources/newsletter-rss-latent-space-2026-09-24-foundries-navigators.md",
"wiki/sources/newsletter-rss-latent-space-2026-09-25-future.md",
"wiki/sources/newsletter-rss-latent-space-2026-09-25-worldprompt.md",
"wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-24-pulse.md",
"wiki/sources/substack-rss-capital-flows-2026-09-24-rates.md",
"wiki/sources/substack-rss-event-horizon-2026-09-25-kalshi-curry.md",
"wiki/sources/substack-rss-klement-2026-09-25-artist.md",
"wiki/sources/substack-rss-wublock-2026-09-24-bitget.md",
"wiki/sources/substack-rss-wublock-2026-09-24-vitalik.md",
"wiki/sources/substack-rss-wublock-2026-09-25-weekly.md",
]
fail = []
for rel in papers:
    t = Path(rel).read_text()
    if "read_status: deep-read" not in t:
        fail.append(rel + " not deep-read")
    if "## Snippets" not in t:
        fail.append(rel + " missing Snippets")
    nar = t.split("## Narrative", 1)[-1].split("## ", 1)[0]
    if len(nar.split()) < 120:
        fail.append(rel + " narrative short")
    if "0 product Integrate GO" not in t and "0 product Integrate GO" not in t:
        pass
for rel in hold:
    t = Path(rel).read_text()
    if "read_status: skimmed" not in t:
        fail.append(rel + " must stay skimmed")
trace = Path(hold[0]).read_text()
if "Tested harnesses let an agent delete its own trace." not in trace:
    fail.append("trace sentence changed")
ev = Path("wiki/sources/eval-github-repo-revenue-2026-09-25.md").read_text()
if "read_status: skimmed" in ev:
    fail.append("eval still skimmed")
if "gh api" not in ev.lower() and "gh api" not in ev:
    fail.append("eval missing gh api note")
for rel in news:
    t = Path(rel).read_text()
    deep = "read_status: deep-read" in t and "## Snippets" in t
    teaser = "read_status: read" in t and "paywall: teaser-only" in t
    if not (deep or teaser):
        fail.append(rel + " needs deep-read snippets or paywall: teaser-only")
if "K272 deep-read" not in Path("wiki/log.md").read_text().split("## ", 2)[0] + Path("wiki/log.md").read_text()[:800]:
    head = Path("wiki/log.md").read_text()[:1200]
    if "K272 deep-read" not in head:
        fail.append("log missing K272 deep-read entry")
if fail:
    print("\n".join(fail))
    sys.exit(1)
print("K272 deep-read gate OK")
PY
