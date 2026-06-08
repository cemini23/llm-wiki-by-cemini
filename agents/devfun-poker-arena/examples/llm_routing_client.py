"""DeepSeek primary + OpenRouter failover (same env contract as OSINT llm_routing).

Primary: DEEPSEEK_API_KEY / DEEPSEEK_MODEL (default deepseek-v4-flash)
Fallback: OPENROUTER_API_KEY when LLM_FALLBACK_ENABLED (default true) — on quota,
billing, rate-limit, or primary API failure. Maps primary model → OpenRouter slug.
"""
from __future__ import annotations

import json
import logging
import os
import sys
from dataclasses import dataclass
from typing import Any, Optional

import httpx

log = logging.getLogger(__name__)

DEFAULT_DEEPSEEK_BASE = "https://api.deepseek.com/v1"
DEFAULT_DEEPSEEK_MODEL = "deepseek-v4-flash"
DEFAULT_OPENROUTER_BASE = "https://openrouter.ai/api/v1"
DEFAULT_OPENROUTER_FALLBACK_MODEL = "deepseek/deepseek-chat"

_DEEPSEEK_TO_OPENROUTER: dict[str, str] = {
    "deepseek-v4-flash": "deepseek/deepseek-chat",
    "deepseek-chat": "deepseek/deepseek-chat",
    "deepseek-reasoner": "deepseek/deepseek-reasoner",
    "deepseek-v4-pro": "deepseek/deepseek-chat",
}

_FALLBACK_HTTP_STATUS = frozenset({402, 429, 500, 502, 503, 504})
_FALLBACK_BODY_KEYWORDS = (
    "insufficient",
    "quota",
    "balance",
    "credit",
    "billing",
    "exhausted",
    "payment required",
    "out of credits",
    "insufficient_quota",
    "rate limit",
    "too many requests",
)


@dataclass(frozen=True)
class LlmRoute:
    provider: str  # deepseek | openrouter
    api_key: str
    base_url: str
    model: str
    is_fallback: bool = False


def _truthy(name: str, default: bool = True) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


def openrouter_model_for_deepseek(deepseek_model: str) -> str:
    explicit = os.environ.get("LLM_FALLBACK_MODEL", "").strip()
    if explicit:
        return explicit
    return _DEEPSEEK_TO_OPENROUTER.get(
        deepseek_model.strip(),
        DEFAULT_OPENROUTER_FALLBACK_MODEL,
    )


def get_primary_route() -> LlmRoute:
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise ValueError("DEEPSEEK_API_KEY not set")
    model = os.environ.get("DEEPSEEK_MODEL", DEFAULT_DEEPSEEK_MODEL).strip() or DEFAULT_DEEPSEEK_MODEL
    return LlmRoute(
        provider="deepseek",
        api_key=key,
        base_url=os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_DEEPSEEK_BASE).strip()
        or DEFAULT_DEEPSEEK_BASE,
        model=model,
        is_fallback=False,
    )


def get_fallback_route(*, deepseek_model: str | None = None) -> LlmRoute | None:
    if not _truthy("LLM_FALLBACK_ENABLED", default=True):
        return None
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        return None
    primary_model = (
        deepseek_model
        or os.environ.get("DEEPSEEK_MODEL", DEFAULT_DEEPSEEK_MODEL).strip()
        or DEFAULT_DEEPSEEK_MODEL
    )
    return LlmRoute(
        provider="openrouter",
        api_key=key,
        base_url=os.environ.get("OPENROUTER_BASE_URL", DEFAULT_OPENROUTER_BASE).strip()
        or DEFAULT_OPENROUTER_BASE,
        model=openrouter_model_for_deepseek(primary_model),
        is_fallback=True,
    )


def ordered_routes(*, deepseek_model: str | None = None) -> list[LlmRoute]:
    """DeepSeek first; OpenRouter second when configured (never parallel)."""
    routes: list[LlmRoute] = []
    try:
        routes.append(get_primary_route())
    except ValueError:
        pass
    fb = get_fallback_route(deepseek_model=deepseek_model)
    if fb is not None and (not routes or fb.model != routes[0].model):
        routes.append(fb)
    if not routes:
        raise ValueError("Neither DEEPSEEK_API_KEY nor OPENROUTER_API_KEY is configured")
    return routes


def _status_from_exc(exc: BaseException) -> int | None:
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code
    status = getattr(exc, "status_code", None)
    if status is not None:
        return int(status)
    if hasattr(exc, "response"):
        resp = getattr(exc, "response", None)
        status = getattr(resp, "status_code", None)
        if status is not None:
            return int(status)
    return None


def should_failover(exc: BaseException) -> bool:
    """True when primary (DeepSeek) should retry on OpenRouter fallback."""
    status = _status_from_exc(exc)
    if status in _FALLBACK_HTTP_STATUS:
        return True
    text = str(exc).lower()
    if any(k in text for k in _FALLBACK_BODY_KEYWORDS):
        return True
    # Primary unreachable — try fallback if configured
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError)):
        return True
    return False


def chat_json(
    *,
    system: str,
    user: str,
    max_tokens: int = 4096,
    temperature: float = 0.2,
    timeout: float = 120.0,
) -> dict[str, Any]:
    """Chat completion with JSON object response. DeepSeek → OpenRouter on failover."""
    routes = ordered_routes()
    last_err: Optional[Exception] = None
    for idx, route in enumerate(routes):
        try:
            result = _chat_once(
                route,
                system=system,
                user=user,
                max_tokens=max_tokens,
                temperature=temperature,
                timeout=timeout,
            )
            if route.is_fallback:
                log.warning(
                    "[llm-routing] response from OpenRouter fallback model=%s",
                    route.model,
                )
            return result
        except Exception as exc:
            last_err = exc
            has_next = idx + 1 < len(routes)
            if has_next and routes[idx].provider == "deepseek" and should_failover(exc):
                nxt = routes[idx + 1]
                msg = (
                    f"[llm-routing] DeepSeek failed ({type(exc).__name__}: {exc}); "
                    f"failover → OpenRouter model={nxt.model}"
                )
                print(msg, file=sys.stderr)
                log.warning(msg)
                continue
            raise
    raise last_err or RuntimeError("no LLM routes")


def _chat_once(
    route: LlmRoute,
    *,
    system: str,
    user: str,
    max_tokens: int,
    temperature: float,
    timeout: float,
) -> dict[str, Any]:
    url = route.base_url.rstrip("/") + "/chat/completions"
    body: dict[str, Any] = {
        "model": route.model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {route.api_key}",
        "Content-Type": "application/json",
    }
    if route.provider == "openrouter":
        referer = os.environ.get("OPENROUTER_HTTP_REFERER", "https://github.com/cemini23")
        title = os.environ.get("OPENROUTER_APP_TITLE", "devfun-poker hl-auto-analyst")
        headers["HTTP-Referer"] = referer
        headers["X-Title"] = title
    with httpx.Client(timeout=timeout) as client:
        resp = client.post(url, headers=headers, json=body)
        resp.raise_for_status()
        data = resp.json()
    content = data["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    if not isinstance(parsed, dict):
        raise ValueError("LLM JSON root must be an object")
    parsed["_llm_provider"] = route.provider
    parsed["_llm_model"] = route.model
    parsed["_llm_is_fallback"] = route.is_fallback
    return parsed
