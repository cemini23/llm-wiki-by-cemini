#!/usr/bin/env bash
# OSINT K283 Phase-1 verify. 1 product Integrate GO (open-notebook, human-gated). FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K283 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K283" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "open-notebook" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "MemTensor" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-github-repos-dev-tools-2026-10-06.md \
  wiki/sources/eval-bedrock-ecosystem-2026-10-06.md \
  wiki/sources/arxiv-2610.03849-beneath-the-vix-2026-10-06.md \
  wiki/sources/arxiv-2610.04530-broadcast-voter-model-2026-10-06.md \
  wiki/sources/arxiv-2610.06292-mean-field-fictitious-play-2026-10-06.md \
  wiki/sources/arxiv-2610.06495-uncertain-vol-error-bounds-2026-10-06.md \
  wiki/sources/arxiv-2610.06650-wikidata-search-traces-2026-10-06.md \
  wiki/sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md \
  wiki/sources/arxiv-2610.06790-bttf-eda-agentic-2026-10-06.md \
  wiki/sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md \
  wiki/sources/substack-rss-latent-space-2026-10-06-reflection-beam.md \
  wiki/sources/substack-rss-event-horizon-2026-10-06-religion-prediction-markets.md \
  wiki/sources/substack-rss-klement-2026-10-06-nationalisations.md \
  wiki/sources/substack-rss-secpro-2026-10-05-ciso-update-ep1.md \
  wiki/sources/substack-rss-secpro-2026-10-05-associated-authors.md \
  wiki/sources/substack-rss-wublock-2026-10-06-september-blockchain-tech.md \
  wiki/concepts/k283-eval-wave.md \
  wiki/concepts/k283-arxiv-wave.md \
  wiki/concepts/k283-feeds-wave.md \
  wiki/entities/tools/tester-army-e2e.md \
  wiki/entities/tools/agency-agents.md \
  wiki/entities/tools/ralph-claude-code.md \
  wiki/entities/tools/background-agents.md \
  wiki/entities/tools/keyed-lock.md \
  wiki/entities/tools/hotpath-rs.md \
  wiki/entities/tools/centralino-ai-studio-medico.md \
  wiki/entities/tools/t-search.md \
  wiki/entities/tools/mc-mod-migrator.md \
  wiki/entities/tools/void-minecraft-proxy.md \
  wiki/entities/tools/deepgemm.md \
  wiki/entities/tools/outreachr.md \
  wiki/entities/tools/bettercap.md \
  wiki/entities/tools/bedrock-ui-animations.md \
  wiki/entities/tools/simple-money-minecraft-bedrock-addon.md \
  briefs/2026-10-06_k283-atto-open-notebook.md \
  briefs/2026-10-06_k283-atto-italian-telephony.md \
  briefs/2026-10-06_k283-guruwatcher-concurrency.md \
  briefs/2026-10-06_k283-ccc-agent-harness.md \
  briefs/2026-10-06_k283-basgiath-bedrock-extracts.md \
  briefs/2026-10-06_k283-pm-hl-feeds.md \
  briefs/2026-10-06_k283-cyber-agent-verification.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "open-notebook" wiki/entities/tools/open-notebook.md
grep -q "K283 re-evaluation" wiki/entities/tools/open-notebook.md
grep -q "OSINT K283" wiki/index.md
grep -q "K283" wiki/log.md
grep -q "K283" ROADMAP.md
echo "1 product Integrate GO (open-notebook). FILE and HITL only. No install."
echo "=== DONE ==="
