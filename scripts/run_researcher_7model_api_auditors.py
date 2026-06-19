#!/usr/bin/env python3
"""Run Researcher 7-model API leg with Fusion → Grok fallback."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / ".cursor/skills/super-audit/scripts/run_api_auditors.py"
WORKSPACE = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE")
PACK = WORKSPACE / "agents/devfun-poker-arena/reports/audit/pack-researcher-hu-2026-06-19"
OUT = WORKSPACE / "agents/devfun-poker-arena/reports/audit/premium-researcher-hu-2026-06-19"

# Load env
for p in [
    Path.home() / ".cemini/llm-routing.env",
    WORKSPACE / ".env",
]:
    if p.is_file():
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        break

sys.path.insert(0, str(SCRIPT.parent))
from run_api_auditors import _call_openai_compat, _resolve_env  # noqa: E402

prompt_path = PACK / "audit_prompt.md"
base = prompt_path.read_text(encoding="utf-8")
OUT.mkdir(parents=True, exist_ok=True)
ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
errors: list[str] = []

# Slot 6: DeepSeek reasoning
label = "api-deepseek-reasoning"
prompt = base.replace("{{MODEL_SLOT}}", label)
print(f"Calling {label} (deepseek-reasoner)...")
try:
    text = _call_openai_compat(
        base_url=_resolve_env("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
        api_key=_resolve_env("DEEPSEEK_API_KEY"),
        model="deepseek-reasoner",
        prompt=prompt,
        system="Super audit slot 6/7 — DeepSeek reasoning. Required output format exactly.",
    )
    (OUT / f"{label}_{ts}.md").write_text(text, encoding="utf-8")
    print(f"  OK {len(text)} chars")
except Exception as e:
    errors.append(f"{label}: {e}")
    (OUT / f"{label}_{ts}_ERROR.txt").write_text(str(e), encoding="utf-8")
    print(f"  FAIL {e}")

# Slot 7: OpenRouter Fusion → Grok fallback
label = "api-openrouter-fusion"
prompt = base.replace("{{MODEL_SLOT}}", label)
or_key = _resolve_env("OPENROUTER_API_KEY")
or_base = _resolve_env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
fusion_models = ["openrouter/fusion", "x-ai/grok-4.3"]
fusion_ok = False
for model in fusion_models:
    print(f"Calling {label} ({model})...")
    try:
        extra = None
        if model == "openrouter/fusion":
            extra = {"plugins": [{"id": "fusion"}]}
        text = _call_openai_compat(
            base_url=or_base,
            api_key=or_key,
            model=model,
            prompt=prompt,
            system="Super audit slot 7/7 — OpenRouter Fusion/Grok. Required output format exactly.",
            extra=extra,
        )
        suffix = "fusion" if "fusion" in model else "grok-fallback"
        (OUT / f"{label}_{suffix}_{ts}.md").write_text(text, encoding="utf-8")
        print(f"  OK {len(text)} chars via {model}")
        fusion_ok = True
        break
    except Exception as e:
        print(f"  FAIL {model}: {e}")
        errors.append(f"{label}/{model}: {e}")

if not fusion_ok:
    (OUT / f"{label}_{ts}_ERROR.txt").write_text("\n".join(errors), encoding="utf-8")

meta = {"timestamp": ts, "pack": str(PACK), "errors": errors}
(OUT / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
print(json.dumps(meta, indent=2))
sys.exit(0 if not errors or fusion_ok else 1)
