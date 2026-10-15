#!/usr/bin/env bash
# OSINT K291 Phase-1 verify. FILE and HITL only. 0 Integrate GO.
#
# K291 was an arXiv + feeds wave: no eval docx, no clones, no install. This gate
# asserts the wave's pages exist, the wires section landed, the ledger is clean,
# and every domain index and log carries the wave.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K291 Phase-1 verify ==="

echo "1. wire ledger"
python3 scripts/wire_ledger_check.py

echo "2. wires section"
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K291" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "32% of within-website citation variance" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "0.896" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "0.608" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "53% lower execution cost" .cursor/rules/osint-phase1-adopt-wires.mdc

echo "3. wave pages (35)"
for f in \
  wiki/ccc/concepts/k291-ccc-wave.md \
  wiki/ccc/sources/arxiv-agent-reflex-reflective-agents-2610.17953-2026-10-14.md \
  wiki/ccc/sources/arxiv-chunkact-action-chunking-agentic-robotics-2610.18874-2026-10-14.md \
  wiki/ccc/sources/arxiv-davinci-tool-agentic-tool-use-supervision-2610.16867-2026-10-14.md \
  wiki/cybersec/concepts/k291-cybersec-wave.md \
  wiki/cybersec/sources/arxiv-attck-r-long-horizon-jailbreaking-2610.16305-2026-10-14.md \
  wiki/cybersec/sources/arxiv-ct0-cybersecurity-transformer-2610.16550-2026-10-14.md \
  wiki/cybersec/sources/arxiv-sp2ec-self-speculative-decoding-vlm-2610.18735-2026-10-14.md \
  wiki/cybersec/sources/arxiv-speccloak-harmful-code-specifications-2610.17907-2026-10-14.md \
  wiki/gambling/concepts/k291-gambling-wave.md \
  wiki/gambling/sources/k291-gambling-feeds-2026-10-14.md \
  wiki/game-dev/concepts/k291-game-dev-wave.md \
  wiki/game-dev/sources/arxiv-choosing-llms-strategic-agent-interactions-2610.18354-2026-10-14.md \
  wiki/game-dev/sources/arxiv-game2real-bench-toy-games-transfer-2610.18834-2026-10-14.md \
  wiki/game-dev/sources/arxiv-receiver-decides-agent-negotiations-2610.18424-2026-10-14.md \
  wiki/image-gen/concepts/k291-image-gen-wave.md \
  wiki/image-gen/sources/arxiv-finite-sample-conditional-diffusion-2610.13851-2026-10-14.md \
  wiki/image-gen/sources/arxiv-gad-geometry-attention-distillation-2610.18779-2026-10-14.md \
  wiki/image-gen/sources/arxiv-instantfusion-shared-latent-interface-2610.13944-2026-10-14.md \
  wiki/image-gen/sources/arxiv-on-policy-one-shot-tts-personalization-2610.17838-2026-10-14.md \
  wiki/image-gen/sources/arxiv-physics-aware-deepfake-detection-2610.18485-2026-10-14.md \
  wiki/osint/concepts/k291-osint-wave.md \
  wiki/osint/sources/arxiv-autoagent0-agentic-runtime-closed-loop-2610.18866-2026-10-14.md \
  wiki/osint/sources/arxiv-ddvr-net-historical-document-recognition-2610.16956-2026-10-14.md \
  wiki/osint/sources/arxiv-diffnash-diffusion-equilibrium-2610.15932-2026-10-14.md \
  wiki/osint/sources/arxiv-embodiedevo-self-improving-coding-agents-2610.18867-2026-10-14.md \
  wiki/osint/sources/arxiv-gromm-risk-neutral-option-market-2610.16732-2026-10-14.md \
  wiki/osint/sources/arxiv-longhisdoc-chinese-historical-documents-2610.14531-2026-10-14.md \
  wiki/osint/sources/arxiv-plaat-learning-to-play-rl-and-games-2610.17391-2026-10-14.md \
  wiki/osint/sources/gs-positioning-2026-10-12-week-41.md \
  wiki/osint/sources/k291-osint-feeds-2026-10-14.md \
  wiki/osint/sources/eval-url-multi-wiki-link-2026-10-14.md \
  wiki/seo/concepts/retrieval-vs-citation-visibility-geo.md \
  wiki/seo/sources/chen-2026-what-drives-ai-citations.md \
  wiki/seo/sources/jiang-2026-chatgpt-citations-retrieval-to-citation.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; };
done

echo "4. key claims present"
grep -q "32%" wiki/seo/sources/chen-2026-what-drives-ai-citations.md
grep -q "2.8%" wiki/seo/sources/chen-2026-what-drives-ai-citations.md
grep -q "0.896" wiki/cybersec/sources/arxiv-attck-r-long-horizon-jailbreaking-2610.16305-2026-10-14.md
grep -q "53.0% lower execution cost" wiki/osint/sources/arxiv-embodiedevo-self-improving-coding-agents-2610.18867-2026-10-14.md
grep -q "43.5bn" wiki/osint/sources/gs-positioning-2026-10-12-week-41.md
grep -q "5.51x" wiki/osint/sources/k291-osint-feeds-2026-10-14.md

echo "5. wave recorded in index, log and ROADMAP"
grep -q "K291" ROADMAP.md
for d in osint ccc cybersec seo image-gen gambling game-dev; do
  grep -q "K291" "wiki/$d/index.md" || { echo "MISSING K291 in wiki/$d/index.md"; exit 1; }
  grep -q "K291" "wiki/$d/log.md"   || { echo "MISSING K291 in wiki/$d/log.md"; exit 1; }
done

echo "6. out-of-scope items have no page"
for skip in arxiv-2610.14586 arxiv-2610.18500 arxiv-2610.18863 arxiv-2610.18818 arxiv-2610.18802; do
  if find wiki -name "*$skip*" | grep -q .; then echo "UNEXPECTED page for skipped $skip"; exit 1; fi
done

echo "0 Integrate GO. FILE and HITL only. No install. No scrape."
echo "=== DONE ==="
