"""DeepSeek API client wrapper — single point for all LLM calls."""

from __future__ import annotations

import os
import time
from typing import Any

import openai
from dotenv import load_dotenv


class DeepSeekClient:
    """OpenAI-compatible client pointed at DeepSeek API.

    All Conductor LLM calls flow through this class so cost tracking,
    error handling, and token-prior injection happen in one place.
    """

    def __init__(self, config: dict[str, Any]) -> None:
        # Try local .env first (gitignored), fall back to server path
        load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
        load_dotenv("/opt/cemini/.env", override=False)
        api_cfg = config["api"]
        self._base_url = api_cfg["base_url"]
        self._timeout = api_cfg.get("timeout_seconds", 30)
        self._max_retries = api_cfg.get("max_retries", 3)
        self.default_model = api_cfg["default_model"]
        self.reasoner_model = api_cfg["reasoner_model"]
        self._client: openai.OpenAI | None = None
        cost_cfg = config.get("cost", {}).get("models", {})
        self._cost = {
            model: (
                float(entry.get("input_per_1k", 0)),
                float(entry.get("output_per_1k", 0)),
            )
            for model, entry in cost_cfg.items()
        }

    @property
    def client(self) -> openai.OpenAI:
        if self._client is None:
            self._client = openai.OpenAI(
                base_url=self._base_url,
                api_key=os.environ.get("DEEPSEEK_API_KEY"),
                timeout=self._timeout,
                max_retries=self._max_retries,
            )
        return self._client

    def complete(
        self,
        prompt: str,
        *,
        model: str | None = None,
        system: str | None = None,
        token_prior: str | None = None,
        temperature: float = 0.0,
        max_tokens: int = 2048,
        response_format: dict[str, Any] | None = None,
    ) -> tuple[str, dict[str, Any]]:
        """Send a completion request. Returns (content, usage_metadata)."""
        model = model or self.default_model

        system_msg = token_prior or ""
        if system:
            system_msg = f"{system_msg}\n\n{system}" if system_msg else system

        messages: list[dict[str, Any]] = []
        if system_msg:
            messages.append({"role": "system", "content": system_msg})
        messages.append({"role": "user", "content": prompt})

        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if response_format is not None:
            kwargs["response_format"] = response_format

        start = time.monotonic()
        try:
            resp = self.client.chat.completions.create(**kwargs)
        except openai.RateLimitError:
            raise
        except openai.AuthenticationError:
            raise
        except Exception as exc:
            raise RuntimeError(f"DeepSeek API call failed: {exc}") from exc
        elapsed_ms = (time.monotonic() - start) * 1000

        choice = resp.choices[0]
        content = choice.message.content or ""
        usage = resp.usage

        meta: dict[str, Any] = {
            "model": resp.model,
            "finish_reason": choice.finish_reason,
            "latency_ms": round(elapsed_ms, 1),
            "usage": {
                "prompt_tokens": usage.prompt_tokens if usage else 0,
                "completion_tokens": usage.completion_tokens if usage else 0,
                "total_tokens": usage.total_tokens if usage else 0,
            },
        }
        meta["cost_usd"] = self._estimate_cost(model, meta["usage"])
        return content, meta

    def classify_json(
        self,
        prompt: str,
        *,
        model: str | None = None,
        system: str | None = None,
        token_prior: str | None = None,
    ) -> tuple[str, dict[str, Any]]:
        """Completion with structured JSON output (for taxonomy + judging)."""
        return self.complete(
            prompt,
            model=model,
            system=system,
            token_prior=token_prior,
            temperature=0.0,
            response_format={"type": "json_object"},
        )

    def _estimate_cost(self, model: str, usage: dict[str, int]) -> float:
        """Estimate cost from token usage + configured pricing."""
        if model not in self._cost:
            return 0.0
        input_rate, output_rate = self._cost[model]
        return round(
            usage["prompt_tokens"] / 1000 * input_rate
            + usage["completion_tokens"] / 1000 * output_rate,
            6,
        )
