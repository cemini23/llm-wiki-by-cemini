#!/usr/bin/env python3
"""Run 3-model premium gap audit (cursor-audit pattern) on prepared pack.

Models (OpenRouter + DeepSeek):
  1. x-ai/grok-4.3 (reasoning high)
  2. deepseek-reasoner
  3. anthropic/claude-opus-4.6 (or fallback gemini)

Usage:
  uv run python scripts/prepare_gap_audit_pack.py reports/exports/playground-s1-live/
  uv run python scripts/run_gap_premium_audit.py
  uv run python scripts/run_gap_premium_audit.py --pack reports/gap-audit/pack --dry-run
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PACK = ROOT / "reports/gap-audit/pack"
OUT_DIR = ROOT / "reports/gap-audit/premium"


def _load_env() -> None:
    for p in (
        Path.home() / ".cemini" / "llm-routing.env",
        Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/.env"),
        ROOT / ".env",
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


def _call_openai_compat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    extra: dict | None = None,
    max_tokens: int = 16000,
) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Expert poker bot strategist + quant audit. Gap retrospective only. "
                    "Use cursor-audit output format exactly."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = os.environ.get(
            "OPENROUTER_HTTP_REFERER", "https://github.com/cemini"
        )
        headers["X-Title"] = os.environ.get("OPENROUTER_APP_TITLE", "devfun-poker gap audit")
    r = httpx.post(url, headers=headers, json=body, timeout=600.0)
    r.raise_for_status()
    return (r.json()["choices"][0]["message"]["content"] or "").strip()


def _slot_prompt(base: str, slot: str) -> str:
    return base.replace("{{MODEL_SLOT}}", slot)


def _synthesize(paths: dict[str, Path], ts: str) -> str:
    parts = ["# Gap audit synthesis\n", f"**Built:** {ts}\n"]
    for model, path in paths.items():
        if path.is_file():
            parts.append(f"\n## {model}\n\n{path.read_text(encoding='utf-8')[:8000]}\n")
    parts.append(
        "\n## Merge instructions (human or follow-up session)\n"
        "- Consensus (≥2 models): …\n"
        "- Unique angles: …\n"
        "- Conflicts: …\n"
        "- Fix order for S1b: …\n"
    )
    return "".join(parts)


def main() -> int:
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    _load_env()
    pack = args.pack.resolve()
    prompt_path = pack / "audit_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path} — run prepare_gap_audit_pack.py first", file=sys.stderr)
        return 1

    base_prompt = prompt_path.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    if args.dry_run:
        print(f"Prompt ready: {len(base_prompt)} chars → {OUT_DIR}")
        print(base_prompt[:1200], "...")
        return 0

    grok_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    ds_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not grok_key:
        print("OPENROUTER_API_KEY missing", file=sys.stderr)
        return 1
    if not ds_key:
        print("DEEPSEEK_API_KEY missing", file=sys.stderr)
        return 1

    or_base = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    ds_base = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

    models = [
        ("grok-4.3", or_base, grok_key, "x-ai/grok-4.3", {"reasoning": {"effort": "high"}}),
        ("deepseek-reasoner", ds_base, ds_key, "deepseek-reasoner", None),
        ("claude-opus", or_base, grok_key, "anthropic/claude-opus-4.6", None),
    ]

    written: dict[str, Path] = {}
    for label, base, key, model, extra in models:
        print(f"Calling {model}...")
        prompt = _slot_prompt(base_prompt, label)
        try:
            text = _call_openai_compat(
                base_url=base, api_key=key, model=model, prompt=prompt, extra=extra
            )
            out = OUT_DIR / f"{label}_{ts}.md"
            out.write_text(text, encoding="utf-8")
            written[label] = out
            print(f"  OK {len(text)} chars → {out.name}")
        except Exception as e:
            print(f"  FAIL {e}", file=sys.stderr)
            written[label] = OUT_DIR / f"{label}_{ts}_ERROR.txt"
            written[label].write_text(str(e), encoding="utf-8")

    synth = OUT_DIR / f"synthesis_{ts}.md"
    synth.write_text(_synthesize(written, ts), encoding="utf-8")
    meta = {"timestamp": ts, "pack": str(pack), "models": list(written.keys())}
    (OUT_DIR / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(json.dumps(meta, indent=2))
    return 0 if all(p.suffix == ".md" for p in written.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
