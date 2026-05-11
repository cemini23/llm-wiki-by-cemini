"""
3-tier structured-output retry helper for DeepSeek API calls.

Adapted from kytmanov/obsidian-llm-wiki-local's `structured_output.py` (MIT,
Phase-0 audited 2026-05-10 at /tmp/olw-audit/). The Ollama-specific bits are
stripped; the Tier-1 JSON-mode prompt is rewritten for the DeepSeek chat-completion
API (OpenAI-compatible). Telemetry is reduced to a single stderr log line per call.

Strategy: three-tier fallback.
  Tier 1 — DeepSeek `response_format={"type": "json_object"}` + fill-in template
           system prompt. Direct json.loads() + Pydantic validation.
  Tier 2 — Extract JSON from raw response: ```json fence → bare ``` → first {...}
  Tier 3 — Re-prompt with error feedback (max_retries times)

Designed for small flat Pydantic schemas. Nested objects are rendered as fill-in
templates so the model sees the real structure rather than just `array<obj>`.

First consumer: `scripts/skill_audit.py --llm-mode` (v0.5+).
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
from typing import TYPE_CHECKING, TypeVar

from pydantic import BaseModel, ValidationError

if TYPE_CHECKING:
    from openai import OpenAI

T = TypeVar("T", bound=BaseModel)
log = logging.getLogger(__name__)

_SCHEMA_INSTRUCTION = """\
You MUST respond with ONLY valid JSON. No prose before or after.
Return the JSON object directly. Do NOT wrap it or add extra keys.

Fill in this exact JSON structure with real content:

{template}

Replace each placeholder string with actual content. Keep the same keys and types.
Respond with nothing but the completed JSON object."""

DEFAULT_MODEL = "deepseek-chat"
DEFAULT_BASE_URL = "https://api.deepseek.com/v1"


class StructuredOutputError(Exception):
    pass


def _resolve_ref(node: dict, defs: dict) -> dict:
    if "$ref" in node:
        key = node["$ref"].rsplit("/", 1)[-1]
        resolved = defs.get(key)
        return resolved if isinstance(resolved, dict) else node
    return node


def _render_example(node: dict, defs: dict, field_name: str = "") -> object:
    node = _resolve_ref(node, defs)

    if "anyOf" in node and "type" not in node:
        outer_desc = node.get("description", "")
        for alt in node["anyOf"]:
            if alt.get("type") != "null":
                if outer_desc and "description" not in alt:
                    alt = {**alt, "description": outer_desc}
                return _render_example(alt, defs, field_name)
        return None

    ftype = node.get("type")
    desc = node.get("description", "")
    enum = node.get("enum")

    if enum:
        return " | ".join(str(e) for e in enum)
    if ftype == "array":
        items = _resolve_ref(node.get("items", {}), defs)
        if items.get("type") == "object" or "properties" in items:
            return [_render_example(items, defs, field_name)]
        return [desc[:60] or f"<{field_name} item>"]
    if ftype == "object" or "properties" in node:
        return {
            sub_name: _render_example(sub, defs, sub_name)
            for sub_name, sub in node.get("properties", {}).items()
        }
    if ftype in ("integer", "number"):
        return 0
    if ftype == "boolean":
        return True
    return desc[:80] or f"<{field_name}>"


def _make_template(model_class: type[T]) -> str:
    schema = model_class.model_json_schema()
    defs = schema.get("$defs", {}) or schema.get("definitions", {})
    props = schema.get("properties", {})
    template = {name: _render_example(sub, defs, name) for name, sub in props.items()}
    return json.dumps(template, indent=2)


def _schema_system(model_class: type[T]) -> str:
    return _SCHEMA_INSTRUCTION.format(template=_make_template(model_class))


def _extract_json(text: str) -> str | None:
    m = re.search(r"```json\s*\n(.*?)\n\s*```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"```\s*\n(\{.*?\})\s*\n```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"\{[\s\S]*\}", text)
    if m:
        return m.group(0).strip()
    return None


def _unwrap(data: dict, model_class: type[T]) -> dict:
    """Unwrap containers small models sometimes produce around the real payload."""
    if not isinstance(data, dict):
        return data

    if len(data) == 1:
        key = next(iter(data))
        value = data[key]
        if isinstance(value, dict):
            return value
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                if isinstance(parsed, dict):
                    return parsed
            except (json.JSONDecodeError, ValueError):
                pass

    if "properties" in data and isinstance(data["properties"], dict):
        props = data["properties"]
        if all(not isinstance(v, dict) or "type" not in v for v in props.values()):
            return props

    return data


def _try_parse(raw: str, model_class: type[T]) -> tuple[T | None, str]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        if "Invalid \\escape" in str(e):
            try:
                data = json.loads(re.sub(r"\\(?![\"\\/bfnrtu])", r"\\\\", raw))
            except json.JSONDecodeError:
                return None, f"Invalid JSON: {e}"
        else:
            return None, f"Invalid JSON: {e}"
    last_err = ""
    try:
        return model_class.model_validate(data), ""
    except ValidationError as e:
        last_err = str(e)
    try:
        return model_class.model_validate(_unwrap(data, model_class)), ""
    except ValidationError as e:
        last_err = str(e)
    except Exception:
        pass
    return None, last_err


def _get_client(api_key: str | None = None, base_url: str | None = None):
    from openai import OpenAI
    key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        raise StructuredOutputError(
            "DEEPSEEK_API_KEY not set (pass api_key= or export the env var)"
        )
    return OpenAI(api_key=key, base_url=base_url or DEFAULT_BASE_URL)


def _emit_telemetry(
    stage: str, model: str, tier: int, retries: int,
    latency_ms: int, error: str | None,
) -> None:
    status = "ok" if error is None else "fail"
    log_line = (
        f"[_llm_retry] stage={stage} model={model} tier={tier} retries={retries} "
        f"latency_ms={latency_ms} status={status}"
    )
    if error:
        log_line += f" error={error[:120]!r}"
    print(log_line, file=sys.stderr)


def request_structured(
    prompt: str,
    model_class: type[T],
    *,
    system: str = "",
    model: str = DEFAULT_MODEL,
    max_retries: int = 2,
    temperature: float = 0.2,
    stage: str = "",
    client=None,
    api_key: str | None = None,
    base_url: str | None = None,
) -> T:
    """
    Request structured output from DeepSeek API, parse into a Pydantic model.

    Tier 1: JSON mode + fill-in template. Tier 2: extract from text. Tier 3: re-prompt
    with the parser error embedded. Loops max_retries+1 times before raising.

    Args:
        prompt:        User-facing prompt body
        model_class:   Pydantic v2 BaseModel subclass
        system:        Optional domain context prepended to the schema instruction
        model:         DeepSeek model id (default deepseek-chat)
        max_retries:   How many retry attempts after the initial call (default 2)
        temperature:   Sampling temperature (default 0.2 for deterministic checks)
        stage:         Pipeline-stage tag (audit/ingest/etc), surfaces in telemetry
        client:        Pre-built `openai.OpenAI` instance (testing). If None, built.
        api_key:       DeepSeek API key. Falls back to DEEPSEEK_API_KEY env var.
        base_url:      DeepSeek base URL. Defaults to https://api.deepseek.com/v1.

    Raises:
        StructuredOutputError: if all attempts exhausted or DEEPSEEK_API_KEY missing
    """
    if client is None:
        client = _get_client(api_key=api_key, base_url=base_url)

    schema_system = _schema_system(model_class)
    full_system = f"{system}\n\n{schema_system}" if system.strip() else schema_system

    last_error: str = ""
    current_prompt = prompt
    total_latency_ms = 0

    for attempt in range(max_retries + 1):
        log.debug("request_structured attempt %d/%d model=%s",
                  attempt + 1, max_retries + 1, model)

        t0 = time.time()
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": full_system},
                    {"role": "user", "content": current_prompt},
                ],
                response_format={"type": "json_object"},
                temperature=temperature,
            )
            raw = resp.choices[0].message.content or ""
        except Exception as e:
            total_latency_ms += int((time.time() - t0) * 1000)
            last_error = f"API call failed: {type(e).__name__}: {e}"
            if attempt < max_retries:
                continue
            _emit_telemetry(stage, model, tier=-1, retries=attempt,
                            latency_ms=total_latency_ms, error=last_error)
            raise StructuredOutputError(last_error) from e

        total_latency_ms += int((time.time() - t0) * 1000)

        result, parse_err = _try_parse(raw, model_class)
        if result is not None:
            tier = 3 if attempt > 0 else 1
            _emit_telemetry(stage, model, tier=tier, retries=attempt,
                            latency_ms=total_latency_ms, error=None)
            return result
        last_error = parse_err

        extracted = _extract_json(raw)
        if extracted:
            result, parse_err = _try_parse(extracted, model_class)
            if result is not None:
                tier = 3 if attempt > 0 else 2
                _emit_telemetry(stage, model, tier=tier, retries=attempt,
                                latency_ms=total_latency_ms, error=None)
                return result
            if parse_err:
                last_error = parse_err

        log.debug("attempt %d failed: %s. raw[:200]=%r",
                  attempt + 1, last_error, raw[:200])

        if attempt < max_retries:
            current_prompt = (
                f"Your previous response was invalid.\n"
                f"Error: {last_error}\n\n"
                f"Original request:\n{prompt}\n\n"
                f"Respond with ONLY valid JSON matching the schema. Nothing else."
            )

    _emit_telemetry(stage, model, tier=-1, retries=max_retries,
                    latency_ms=total_latency_ms, error=last_error)
    raise StructuredOutputError(
        f"Failed to get valid {model_class.__name__} after {max_retries + 1} "
        f"attempts. Last error: {last_error}"
    )
