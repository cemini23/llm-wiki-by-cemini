#!/usr/bin/env bash
# K141 Phase-0 — 2 docx + 2 arXiv inbox
set -euo pipefail

echo "K141 Phase-0 audits"
echo "==================="

for repo in scaleapi/SWE-Interact alibaba/page-agent usestrix/strix ChromeDevTools/chrome-devtools-mcp agentskills/agentskills TencentCloud/CubeSandbox baidu/Unlimited-OCR nationaldesignstudio/rampart InternScience/Agents-A1; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-07-03):"
echo "  Adopt (7): page-agent MIT · strix Apache-2.0 · chrome-devtools-mcp · agentskills · Unlimited-OCR MIT · Agents-A1"
echo "  CONDITIONAL-GO (2): CubeSandbox (gh license null) · rampart (CC-BY docx vs gh null)"
echo "  Steal-from: SWE-Interact harness · OmniRoute · cognee · loop-library"
echo "  arXiv REFERENCE: 2606.30573 SWE-INTERACT · 2607.00190 Latent Maps of Performance"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-07-03_k141-swe-interact-multiturn-steal.md"
echo "  briefs/ccc-2026-07-03_k141-swe-interact-harness-steal.md"
echo "  briefs/ccc-2026-07-03_k141-page-agent-chrome-devtools-adopt.md"
echo "  briefs/ccc-2026-07-03_k141-agentskills-standard-adopt.md"
echo "  briefs/cybersec-2026-07-03_k141-strix-adopt.md"
echo "  ../projects/Game Dev wiki/briefs/2026-07-03_k141-latent-maps-starcraft-feedback-steal.md"
echo "  ../projects/tipdrop-workspace-kit/briefs/2026-07-03_k141-unlimited-ocr-ingest-adopt.md"
echo "  ../projects/tipdrop-workspace-kit/briefs/2026-07-03_k141-rampart-pii-redaction-adopt.md"
