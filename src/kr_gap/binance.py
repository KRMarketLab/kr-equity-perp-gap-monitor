from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import requests

from .models import Candle


BINANCE_FAPI_BASE = "https://fapi.binance.com"


def fetch_binance_futures_klines(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
    base_url: str = BINANCE_FAPI_BASE,
) -> list[Candle]:
    """Fetch public Binance USD-M futures klines.

    This does not require API keys. It is intentionally read-only.
    """
    if limit < 1 or limit > 1500:
        raise ValueError("limit must be between 1 and 1500")

    url = f"{base_url}/fapi/v1/klines"
    response = requests.get(
        url,
        params={"symbol": symbol.upper(), "interval": interval, "limit": limit},
        timeout=10,
    )
    response.raise_for_status()
    return [_parse_kline(item) for item in response.json()]


def _parse_kline(item: list[Any]) -> Candle:
    return Candle(
        timestamp=datetime.fromtimestamp(item[0] / 1000, tz=timezone.utc),
        open=float(item[1]),
        high=float(item[2]),
        low=float(item[3]),
        close=float(item[4]),
        volume=float(item[5]),
    )
