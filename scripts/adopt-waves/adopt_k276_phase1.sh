#!/usr/bin/env bash
# OSINT K276 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K276 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K276" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k276_phase0.sh scripts/adopt_k276_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/concepts/k276-atto-htr-wave.md \
  wiki/concepts/k276-gambling-pm-wave.md \
  wiki/concepts/k276-harness-evolution-wave.md \
  wiki/concepts/k276-newsletter-macro-wave.md \
  wiki/concepts/k276-ood-stub-wave.md \
  wiki/concepts/k276-vol-quant-wave.md \
  wiki/sources/arxiv-2609.31473-game-arena-2026-09-30.md \
  wiki/sources/arxiv-2609.33213-fi-operator-2026-09-30.md \
  wiki/sources/arxiv-2609.33669-rsd-poker-2026-09-30.md \
  wiki/sources/arxiv-2609.33767-taming-greeks-2026-09-30.md \
  wiki/sources/arxiv-2609.34346-e-wave-2026-09-30.md \
  wiki/sources/arxiv-2609.34905-resight-smc-2026-09-30.md \
  wiki/sources/arxiv-2609.35473-htr-high-variance-2026-09-30.md \
  wiki/sources/arxiv-2609.35738-harness-learning-2026-09-30.md \
  wiki/sources/arxiv-2609.36257-hedging-price-impact-2026-09-30.md \
  wiki/sources/arxiv-2609.37195-htr-icl-2026-09-30.md \
  wiki/sources/arxiv-2609.37741-dyson-schwinger-2026-09-30.md \
  wiki/sources/arxiv-2609.37755-papyrus-htr-tolerance-2026-09-30.md \
  wiki/sources/arxiv-2609.38107-invalid-traces-2026-09-30.md \
  wiki/sources/arxiv-2609.38108-plan-execution-gap-2026-09-30.md \
  wiki/sources/arxiv-2609.38143-meta-skills-harness-2026-09-30.md \
  wiki/sources/arxiv-2609.38147-meta-reasoning-2026-09-30.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-solv.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-29-ainews-opus-55-is-good-at-explainer-videos.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-29-claude-codes-next-era-thariq-shihipar-anthropic.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultrafast.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-29-why-has-shopify-dropped-react-native.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-30-distributed-databases-with-peter-mattis.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-27-can-you-turn-off-google-reviews-on-a-business-pr.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-27-google-business-profile-performance-report-how-t.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-27-how-to-remove-bad-reviews-from-google-business-p.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-28-is-google-calling-me-or-is-it-a-scam-how-to-tell.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-28-why-is-posting-currently-turned-off-on-google-re.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-29-does-the-url-you-link-to-in-google-my-business-i.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-29-how-to-add-remove-managers-from-your-google-busi.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-30-googles-2025-2026-core-updates-are-destroying-lo.md \
  wiki/sources/substack-rss-addy-osmani-2026-09-28-the-code-nobody-reads.md \
  wiki/sources/substack-rss-capital-flows-2026-09-29-what-no-one-sees-right-now.md \
  wiki/sources/substack-rss-event-horizon-2026-09-29-you-definitely-can-stop-offshore-prediction-mark.md \
  wiki/sources/substack-rss-event-horizon-2026-09-30-prediction-markets-need-to-let-us-trade-on-the-f.md \
  wiki/sources/substack-rss-klement-2026-09-29-index-funds-make-active-managers-worse.md \
  wiki/sources/substack-rss-klement-2026-09-30-corporate-taxes-and-creative-destruction.md \
  wiki/sources/substack-rss-wublock-2026-09-29-after-the-bitget-hack-thorchains-role-in-launder.md \
  wiki/sources/substack-rss-wublock-2026-09-30-cz-hong-kong-ama-young-people-shouldnt-blindly-g.md \
  briefs/2026-09-30_k276-atto.md \
  briefs/2026-09-30_k276-guruwatcher.md \
  briefs/2026-09-30_k276-ceminidfs.md \
  briefs/2026-09-30_k276-ceminiparlays.md \
  briefs/2026-09-30_k276-ccc-harness.md \
  briefs/2026-09-30_k276-cyber-lab.md \
  briefs/2026-09-30_k276-gambling.md \
  briefs/2026-09-30_k276-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "FILE" wiki/concepts/k276-harness-evolution-wave.md
grep -q "policy_wired" wiki/concepts/k276-harness-evolution-wave.md
grep -q "Transkribus stays" wiki/concepts/k276-atto-htr-wave.md
grep -q "OSINT K276" wiki/index.md
grep -q "K276 wave" wiki/log.md
grep -q "K276" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
for d in \
  .local/adopts/game_arena \
  .local/adopts/igsm-trace-validity \
  .local/adopts/MetaSkill-AI4AI \
  .local/adopts/good_enough_papyrus_htr \
  .local/adopts/resight-smc
 do test ! -d "$d" || { echo "CLONE DIR PRESENT $d"; exit 1; }; done
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "=== DONE ==="
