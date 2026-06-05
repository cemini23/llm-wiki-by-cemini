"""
Cross-project LLM routing: DeepSeek primary, OpenRouter fallback.

Used by OSINT scripts (_llm_retry, skill_audit), CeminiSuite llm_analyst brain,
and any OpenAI-compatible client (world-cup-bot ADVISOR_*, poker HL, etc.).

Env contract: config/llm-routing.env.example (copy to ~/.cemini/llm-routing.env
or project .env). Source via:  source scripts/source_llm_routing_env.sh
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openai import OpenAI

logger = logging.getLogger(__name__)

DEFAULT_DEEPSEEK_BASE = "https://api.deepseek.com/v1"
DEFAULT_DEEPSEEK_MODEL = "deepseek-v4-flash"
DEFAULT_OPENROUTER_BASE = "https://openrouter.ai/api/v1"
DEFAULT_OPENROUTER_FALLBACK_MODEL = "deepseek/deepseek-chat"

# DeepSeek model id -> OpenRouter slug (override with LLM_FALLBACK_MODEL).
_DEEPSEEK_TO_OPENROUTER: dict[str, str] = {
    "deepseek-v4-flash": "deepseek/deepseek-chat",
    "deepseek-chat": "deepseek/deepseek-chat",
    "deepseek-reasoner": "deepseek/deepseek-reasoner",
    "deepseek-v4-pro": "deepseek/deepseek-chat",
}

_FALLBACK_HTTP_STATUS = frozenset({402, 429})
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
)


def _truthy(name: str, default: bool = True) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


@dataclass(frozen=True)
class LlmRoute:
    """One OpenAI-compatible API endpoint + model."""

    provider: str  # "deepseek" | "openrouter"
    api_key: str
    base_url: str
    model: str
    is_fallback: bool = False

    def openrouter_extra_headers(self) -> dict[str, str]:
        if self.provider != "openrouter":
            return {}
        headers: dict[str, str] = {}
        referer = os.environ.get("OPENROUTER_HTTP_REFERER", "").strip()
        title = os.environ.get("OPENROUTER_APP_TITLE", "Cemini").strip()
        if referer:
            headers["HTTP-Referer"] = referer
        if title:
            headers["X-Title"] = title
        return headers


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
    return LlmRoute(
        provider="deepseek",
        api_key=key,
        base_url=os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_DEEPSEEK_BASE).strip()
        or DEFAULT_DEEPSEEK_BASE,
        model=os.environ.get("DEEPSEEK_MODEL", DEFAULT_DEEPSEEK_MODEL).strip()
        or DEFAULT_DEEPSEEK_MODEL,
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
    """Primary first, then OpenRouter fallback when configured."""
    routes: list[LlmRoute] = []
    try:
        routes.append(get_primary_route())
    except ValueError:
        pass
    fb = get_fallback_route(deepseek_model=deepseek_model)
    if fb is not None and (not routes or fb.model != routes[0].model):
        routes.append(fb)
    if not routes:
        raise ValueError(
            "Neither DEEPSEEK_API_KEY nor OPENROUTER_API_KEY is configured"
        )
    return routes


def should_failover(exc: BaseException) -> bool:
    """True when the error looks like quota/billing/rate-limit (try OpenRouter)."""
    status = getattr(exc, "status_code", None)
    if status is None and hasattr(exc, "response"):
        response = getattr(exc, "response", None)
        status = getattr(response, "status_code", None)
    if status in _FALLBACK_HTTP_STATUS:
        return True
    text = str(exc).lower()
    return any(k in text for k in _FALLBACK_BODY_KEYWORDS)


def build_openai_client(route: LlmRoute) -> OpenAI:
    from openai import OpenAI

    headers = route.openrouter_extra_headers()
    if headers:
        return OpenAI(
            api_key=route.api_key,
            base_url=route.base_url,
            default_headers=headers,
        )
    return OpenAI(api_key=route.api_key, base_url=route.base_url)


def advisor_env_from_routing(*, prefer_openrouter: bool = False) -> dict[str, str]:
    """
    Map routing env -> world-cup-bot ADVISOR_* (OpenAI-compatible).
    Default: DeepSeek primary when configured; OpenRouter-only when DeepSeek absent
    or prefer_openrouter=True (e.g. source_llm_routing_env.sh for OR credits).
    """
    if prefer_openrouter:
        fb = get_fallback_route()
        if fb is None:
            raise ValueError("OPENROUTER_API_KEY required for advisor OpenRouter mode")
        route = fb
    else:
        route = ordered_routes()[0]
    return {
        "ADVISOR_BASE_URL": route.base_url,
        "ADVISOR_API_KEY": route.api_key,
        "ADVISOR_MODEL": route.model,
    }


def apply_advisor_env() -> None:
    """Set ADVISOR_* in os.environ from routing (no-op if ADVISOR_BASE_URL already set)."""
    if os.environ.get("ADVISOR_BASE_URL", "").strip():
        return
    for key, value in advisor_env_from_routing().items():
        os.environ.setdefault(key, value)


def chat_completion_kwargs(route: LlmRoute, **payload: Any) -> dict[str, Any]:
    """Inject model from route into chat.completions.create kwargs."""
    out = dict(payload)
    out["model"] = route.model
    return out
