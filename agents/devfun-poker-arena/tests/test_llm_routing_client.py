"""LLM routing: DeepSeek primary, OpenRouter fallback only."""
from __future__ import annotations

import pytest

from examples.llm_routing_client import (
    get_fallback_route,
    openrouter_model_for_deepseek,
    ordered_routes,
    should_failover,
)


def test_openrouter_model_maps_v4_flash():
    assert openrouter_model_for_deepseek("deepseek-v4-flash") == "deepseek/deepseek-chat"


def test_ordered_routes_deepseek_then_openrouter(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-ds-test")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    monkeypatch.setenv("LLM_FALLBACK_ENABLED", "true")
    routes = ordered_routes()
    assert len(routes) == 2
    assert routes[0].provider == "deepseek"
    assert routes[0].is_fallback is False
    assert routes[1].provider == "openrouter"
    assert routes[1].is_fallback is True
    assert routes[1].model == "deepseek/deepseek-chat"


def test_openrouter_only_when_no_deepseek(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    routes = ordered_routes()
    assert len(routes) == 1
    assert routes[0].provider == "openrouter"


def test_fallback_disabled(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-ds")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or")
    monkeypatch.setenv("LLM_FALLBACK_ENABLED", "false")
    assert get_fallback_route() is None
    assert len(ordered_routes()) == 1


def test_should_failover_quota():
    class E(Exception):
        status_code = 402
    assert should_failover(E("insufficient balance"))


def test_should_failover_network():
    import httpx
    assert should_failover(httpx.ConnectError("connection refused"))
