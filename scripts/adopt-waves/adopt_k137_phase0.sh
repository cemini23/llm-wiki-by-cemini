#!/usr/bin/env bash
# K137 Phase-0 — Multi-Wiki OpenClaw ecosystem docx (20 URLs)
set -euo pipefail

echo "K137 Phase-0 audits"
echo "==================="

for repo in openimsdk/open-im-server VoltAgent/awesome-openclaw-skills hesamsheikh/awesome-openclaw-usecases openclaw/clawhub linuxhsj/openclaw-zero-token abhi1693/openclaw-mission-control Gen-Verse/OpenClaw-RL TianyiDataScience/openclaw-control-center deepseek-ai/DeepSpec mengjian-github/openclaw101; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-30):"
echo "  Adopt (2): Gen-Verse/OpenClaw-RL Apache-2.0 · deepseek-ai/DeepSpec MIT"
echo "  Steal-from (5): openclaw/clawhub · openimsdk/open-im-server · linuxhsj/openclaw-zero-token · abhi1693/openclaw-mission-control · sunkencity/qwen25-3b-openclaw (HF, no SPDX)"
echo "  Reference-only (5): awesome-openclaw-* · OpenClaw-macOS HF · Gemma HF · openclaw-control-center MIT (gh corrected docx)"
echo "  Reject (4): Crazyrouter · continuous-pretraining · Qwen mash · openclaw101 (tutorial front-end; gh license null)"
echo "  UNAVAILABLE (4): HF phantom adapter URLs"
echo ""
echo "Briefs:"
echo "  briefs/2026-06-30_k137-deepspec-speculative-decoding-prod.md"
echo "  briefs/2026-06-30_k137-mission-control-fleet-audit-steal.md"
echo "  briefs/ccc-2026-06-30_k137-clawhub-skill-format-scan-steal.md"
echo "  ../projects/tipdrop-workspace-kit/briefs/2026-06-30_k137-clawhub-ingest-compliance-steal.md"
