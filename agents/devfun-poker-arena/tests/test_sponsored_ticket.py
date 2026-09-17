"""Sponsored 0.01 ticket rebuy — never pay 250 MON (T14 / T10 scar)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaError  # noqa: E402
from run_cemini_lobby import (  # noqa: E402
    _cash_rebuy_forbidden,
    _sponsored_rebuy_quota_open,
    _sponsored_ticket_dust,
    _sponsored_ticket_funded,
    _try_rebuy,
)

T14_DUST = {
    "amount": "0.01",
    "currency": "MON",
    "sponsored": True,
    "chain": "monad",
    "to": "0x" + "ab" * 20,
    "paymentReference": "pref-t14-dust",
    "sponsor": {"type": "admin_admission", "id": "ticket1", "status": "funded"},
}
CASH_250 = {"amount": "250", "currency": "MON", "sponsored": False}


@pytest.fixture
def _isolate_env():
    saved = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(saved)


@pytest.fixture
def _no_pay_sleep(monkeypatch):
    import run_cemini_lobby as lobby

    monkeypatch.setattr(lobby, "PAYMENT_CONFIRM_WAIT_S", 0)
    monkeypatch.setattr(lobby, "PAYMENT_CONFIRM_ATTEMPTS", 1)


class _RebuyClient:
    def __init__(self, first_body: dict, after_pay: dict | Exception):
        self.posts: list[tuple[str, dict | None]] = []
        self._first = first_body
        self._after = after_pay
        self._naked = 0

    def get(self, path: str, **kwargs):
        if "wallet" in path:
            return {"nativeBalance": {"value": "1600000000000000000", "formatted": "1.60"}}
        raise AssertionError(path)

    def post(self, path: str, json_body=None):
        self.posts.append((path, json_body))
        if path == "/texas/rebuy":
            pref = (json_body or {}).get("paymentReference")
            if not pref:
                self._naked += 1
                raise ArenaError(402, {
                    "error": "Payment required",
                    "paymentRequirements": dict(self._first),
                })
            if isinstance(self._after, Exception):
                raise self._after
            return self._after
        if path == "/agent/wallet/transfer/native":
            return {"txHash": "0xabc"}
        raise AssertionError(path)


def test_dust_and_cash_classifiers(_isolate_env):
    assert _sponsored_ticket_dust(T14_DUST) is True
    assert _sponsored_ticket_funded(T14_DUST) is True
    assert _cash_rebuy_forbidden(T14_DUST) is False
    assert _sponsored_ticket_dust(CASH_250) is False
    assert _cash_rebuy_forbidden(CASH_250) is True


def test_max_rebuys_zero_blocks_without_flag(_isolate_env):
    os.environ["CEMINI_MAX_REBUYS"] = "0"
    os.environ["CEMINI_SPONSORED_TICKET_REBUY"] = "0"
    state = {"rebuy_count": 0}
    client = _RebuyClient(T14_DUST, {"ok": True})
    assert _try_rebuy(client, "comp", state, lambda s: None) is False
    assert client.posts == []
    assert "max rebuys" in (state.get("rebuy_fund_block_reason") or "")


def test_sponsored_quota_pays_dust_once(_isolate_env, _no_pay_sleep):
    os.environ["CEMINI_MAX_REBUYS"] = "0"
    os.environ["CEMINI_SPONSORED_TICKET_REBUY"] = "1"
    os.environ["CEMINI_MAX_SPONSORED_REBUYS"] = "1"
    os.environ["CEMINI_REBUY_MAX_MON"] = "0"
    state = {
        "rebuy_count": 0,
        "hands_played": 193,
        "rebuy_fund_blocked_until": 9e12,
        "rebuy_fund_block_reason": "max rebuys 0 reached (post-mortem T10)",
    }
    saved = []
    client = _RebuyClient(T14_DUST, {"ok": True, "chips": 1000})
    assert _sponsored_rebuy_quota_open(state) is True
    assert _try_rebuy(client, "comp", state, saved.append) is True
    assert state["sponsored_ticket_rebuy_used"] == 1
    assert state["hands_played"] == 0
    assert state["rebuy_count"] == 0
    assert "rebuy_fund_blocked_until" not in state
    paths = [p for p, _ in client.posts]
    assert "/agent/wallet/transfer/native" in paths
    transfer = next(b for p, b in client.posts if p.endswith("transfer/native"))
    assert transfer["amount"] == "0.01"
    assert transfer["paymentReference"] == "pref-t14-dust"
    paid = next(b for p, b in client.posts if p == "/texas/rebuy" and (b or {}).get("paymentReference"))
    assert paid["paymentReference"] == "pref-t14-dust"


def test_second_sponsored_rebuy_blocked(_isolate_env, _no_pay_sleep):
    os.environ["CEMINI_MAX_REBUYS"] = "0"
    os.environ["CEMINI_SPONSORED_TICKET_REBUY"] = "1"
    os.environ["CEMINI_MAX_SPONSORED_REBUYS"] = "1"
    state = {"rebuy_count": 0, "sponsored_ticket_rebuy_used": 1}
    client = _RebuyClient(T14_DUST, {"ok": True})
    assert _try_rebuy(client, "comp", state, lambda s: None) is False
    assert client.posts == []


def test_250_cash_refused_even_with_sponsored_flag(_isolate_env, _no_pay_sleep):
    os.environ["CEMINI_MAX_REBUYS"] = "0"
    os.environ["CEMINI_SPONSORED_TICKET_REBUY"] = "1"
    os.environ["CEMINI_REBUY_MAX_MON"] = "0"
    state = {"rebuy_count": 0}
    client = _RebuyClient(CASH_250, {"ok": True})
    assert _try_rebuy(client, "comp", state, lambda s: None) is False
    assert any("transfer/native" in p for p, _ in client.posts) is False
    assert "cash buy-in" in (state.get("rebuy_fund_block_reason") or "")


def test_payment_amount_too_low_does_not_pay_250(_isolate_env, _no_pay_sleep):
    os.environ["CEMINI_MAX_REBUYS"] = "0"
    os.environ["CEMINI_SPONSORED_TICKET_REBUY"] = "1"
    state = {"rebuy_count": 0}
    too_low = ArenaError(400, {
        "error": "PAYMENT_AMOUNT_TOO_LOW",
        "message": "Payment amount too low: expected at least 250 MON with 5% tolerance",
    })
    client = _RebuyClient(T14_DUST, too_low)
    assert _try_rebuy(client, "comp", state, lambda s: None) is False
    assert state.get("entry_fee_amount_mismatch") is True
    assert state.get("sponsored_ticket_rebuy_used") in (None, 0)
