#!/usr/bin/env bash
# K142 Phase-0 — Multi-Wiki URL Evaluation.docx + x.jpeg operator note
set -euo pipefail

echo "K142 Phase-0 audits"
echo "==================="

repos=(
  logto-io/logto
  allenai/olmocr
  facebook/astryx
  CoreBunch/Instatic
  langflow-ai/langflow
  hcengineering/platform
  JuliusBrussee/caveman
  HUANGCHIHHUNGLeo/claude-real-video
  Gitlawb/zero
  harvard-edge/cs249r_book
  ifixai-ai/iFixAi
  addyosmani/agent-skills
  microsoft/qlib
  Shubhamsaboo/awesome-llm-apps
  Panniantong/Agent-Reach
  autonomous-ai/autonomous-computer
  Zackriya-Solutions/meetily
  Archive228/loopkit
)

for repo in "${repos[@]}"; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at,open_issues:.open_issues_count,archived:.archived}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-07-03):"
echo "  Adopt (5): olmocr Apache-2.0 · caveman MIT · zero MIT · iFixAi Apache-2.0 · addyosmani/agent-skills MIT"
echo "  Steal-from (3): Astryx MIT · claude-real-video MIT · portablellm.wiki MIT/OKF pattern"
echo "  Defer (4): Instatic · Agent-Reach · Meetily · Langflow"
echo "  Reference-only (5): Logto · cs249r_book NOASSERTION · awesome-llm-apps · autonomous-computer · tasteskill.dev"
echo "  Reject (3): Huly EPL-2.0/SSRF · Qlib legacy equity mismatch · LoopKit medical-only"
echo ""
echo "Briefs/pages: OSINT source + tool pages; CCC K142 briefs; Cybersec iFixAi; TipDrop olmocr/iFixAi/OKF/Agent-Reach defer."
