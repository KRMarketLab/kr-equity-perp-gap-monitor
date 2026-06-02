from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import requests

from .models import Candle


HYPERLIQUID_INFO_URL = "https://api.hyperliquid.xyz/info"


def fetch_hyperliquid_candles(
    coin: str,
    interval: str,
    start_time_ms: int,
    end_time_ms: int,
    info_url: str = HYPERLIQUID_INFO_URL,
) -> list[Candle]:
    """Fetch public Hyperliquid candleSnapshot data.

    Hyperliquid public info endpoint is read-only and does not require API keys.
    """
    payload = {
        "type": "candleSnapshot",
        "req": {
            "coin": coin,
            "interval": interval,
            "startTime": start_time_ms,
            "endTime": end_time_ms,
        },
    }
    response = requests.post(info_url, json=payload, timeout=10)
    response.raise_for_status()
    return [_parse_hl_candle(item) for item in response.json()]


def _parse_hl_candle(item: dict[str, Any]) -> Candle:
    return Candle(
        timestamp=datetime.fromtimestamp(int(item["t"]) / 1000, tz=timezone.utc),
        open=float(item["o"]),
        high=float(item["h"]),
        low=float(item["l"]),
        close=float(item["c"]),
        volume=float(item.get("v", 0.0)),
    )
