#!/usr/bin/env python3
"""Run dual premium-model S1a retrospective (Grok + DeepSeek Reasoner)."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = ROOT / "reports" / "exports" / "playground-s1-s1a-snapshot-2026-06-06" / "premium_pass_prompt.txt"
OUT_DIR = ROOT / "briefs" / "premium-pass-outputs"


def _load_env() -> None:
    for p in (
        Path.home() / ".cemini" / "llm-routing.env",
        Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/.env"),
    ):
        if not p.is_file():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def _build_prompt() -> str:
    field = (ROOT / "reports/exports/playground-s1-s1a-snapshot-2026-06-06/field_report.txt").read_text()
    analyze = (ROOT / "reports/hl-loop/latest_analyze.txt").read_text()
    return f"""You are a poker bot strategist reviewing dev.fun Playground S1a for a production Python decide() agent (cemini_decide.py).

CRITICAL CONSTRAINTS:
- Zero LLM calls at runtime. Output structural guards, env policies, and regression test ideas only.
- Bot is currently #1 on leaderboard — do not recommend widening for vanity metrics.
- Main KO tournament has NO REBUY — hour-one survival beats exploit EV.
- We already shipped: BTN trash vs limp fold, CEMINI_NUTS_DETECT=1, stagger locks, HL R8-20 patches.

CONTEXT — S1a arc:
- Early Jun 3: rank ~#215 @ 540 chips (near bust, rebuy disabled then)
- Jun 6: rank #1 @ 138,917 chips, 1,873 hands, 9.0% win rate, 12.3% VPIP / 4.3% PFR
- Field top leaders are LAG (40-70% VPIP); 327 Grok-branded agents
- Nemesis: hunterguy102 (18 pots won vs us / 87 tables)

FIELD REPORT:
{field}

HL ANALYZE (latest 100-hand sample, worst 15):
{analyze}

POSITION BREAKDOWN from analyze: UTG/SB/BB/MP/BTN all ~-100 avg; CO +175 (small sample).

DELIVERABLE (structured markdown):

## 1. Top 5 structural gaps
Rank by chip-risk × frequency. Not hand-specific hero calls — guard categories (e.g. "SB complete trash", "cold-start steal block").

## 2. Cold-start policy (hands 1–N)
Exact rules for first 50 / 200 hands when HUD empty. Join table pace. When to flip from survival to exploit.

## 3. S1b exploit toggles (HUD warm)
What to enable vs LAG/Grok/nemesis seats only. Margins or flags. What stays frozen until KO.

## 4. KO foundation (no rebuy)
Minimum viable stack policy, max playable fractions, when to sit out vs join.

## 5. Do NOT change
List 3-5 things that would hurt qualification despite sounding +EV.

## 6. Patch backlog (ranked)
Table: priority | guard name | target function area | regression spot idea

## 7. Regression / test ideas
5-8 frozen spot descriptions (position, hand class, forbidden action).

Be specific and actionable for a Python heuristic bot with preflop chart + MC equity + HUD archetypes (rock/maniac).
"""


def _call_openai_compat(*, base_url: str, api_key: str, model: str, prompt: str, extra: dict | None = None, max_tokens: int = 8192) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Expert poker bot architect. Concise, structural, no fluff.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = os.environ.get("OPENROUTER_HTTP_REFERER", "https://github.com/cemini")
        headers["X-Title"] = os.environ.get("OPENROUTER_APP_TITLE", "Gambling-wiki poker retrospective")
    r = httpx.post(
        url,
        headers=headers,
        json=body,
        timeout=300.0,
    )
    r.raise_for_status()
    data = r.json()
    return (data["choices"][0]["message"]["content"] or "").strip()


def main() -> int:
    _load_env()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prompt = _build_prompt()
    PROMPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROMPT_PATH.write_text(prompt)

    grok_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    ds_key = os.environ.get("DEEPSEEK_API_KEY")
    if not grok_key:
        print("OPENROUTER_API_KEY missing (needed for x-ai/grok-4.3)", file=sys.stderr)
        return 1
    if not ds_key:
        print("DEEPSEEK_API_KEY missing", file=sys.stderr)
        return 1

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    results: dict[str, str] = {}

    print("Calling x-ai/grok-4.3 via OpenRouter (reasoning=high)...")
    try:
        results["grok-4.3"] = _call_openai_compat(
            base_url=os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
            api_key=grok_key,
            model="x-ai/grok-4.3",
            prompt=prompt,
            extra={"reasoning": {"effort": "high"}},
            max_tokens=12000,
        )
        (OUT_DIR / f"grok-4.3_{ts}.md").write_text(results["grok-4.3"])
        print(f"  grok OK ({len(results['grok-4.3'])} chars)")
    except Exception as e:
        print(f"  grok failed: {e}", file=sys.stderr)
        results["grok-4.3"] = f"ERROR: {e}"

    print("Calling deepseek-reasoner...")
    try:
        results["deepseek-reasoner"] = _call_openai_compat(
            base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
            api_key=ds_key,
            model="deepseek-reasoner",
            prompt=prompt,
            max_tokens=12000,
        )
        (OUT_DIR / f"deepseek-reasoner_{ts}.md").write_text(results["deepseek-reasoner"])
        print(f"  deepseek OK ({len(results['deepseek-reasoner'])} chars)")
    except Exception as e:
        print(f"  deepseek failed: {e}", file=sys.stderr)
        results["deepseek-reasoner"] = f"ERROR: {e}"

    meta = {"timestamp": ts, "models": list(results.keys()), "prompt_chars": len(prompt)}
    (OUT_DIR / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2))
    return 0 if all(not v.startswith("ERROR:") for v in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
