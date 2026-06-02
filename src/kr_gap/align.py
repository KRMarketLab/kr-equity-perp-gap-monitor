from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from .metrics import pct_return
from .models import Candle, GapPoint


def candles_to_frame(candles: Iterable[Candle], prefix: str) -> pd.DataFrame:
    rows = [
        {
            "timestamp": c.timestamp,
            f"{prefix}_open": c.open,
            f"{prefix}_high": c.high,
            f"{prefix}_low": c.low,
            f"{prefix}_close": c.close,
            f"{prefix}_volume": c.volume,
        }
        for c in candles
    ]
    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame
    return frame.sort_values("timestamp").drop_duplicates("timestamp", keep="last")


def align_candles(reference: Iterable[Candle], market: Iterable[Candle]) -> pd.DataFrame:
    """Inner-join reference and market candles on exact timestamps."""
    ref = candles_to_frame(reference, "reference")
    mkt = candles_to_frame(market, "market")
    if ref.empty or mkt.empty:
        return pd.DataFrame()
    return ref.merge(mkt, on="timestamp", how="inner").sort_values("timestamp")


def calculate_gap_points(reference: list[Candle], market: list[Candle]) -> list[GapPoint]:
    aligned = align_candles(reference, market)
    if aligned.empty:
        return []

    ref_base = float(aligned.iloc[0]["reference_close"])
    mkt_base = float(aligned.iloc[0]["market_close"])

    points: list[GapPoint] = []
    for _, row in aligned.iterrows():
        ref_close = float(row["reference_close"])
        mkt_close = float(row["market_close"])
        ref_ret = pct_return(ref_close, ref_base)
        mkt_ret = pct_return(mkt_close, mkt_base)
        points.append(
            GapPoint(
                timestamp=row["timestamp"].to_pydatetime()
                if hasattr(row["timestamp"], "to_pydatetime")
                else row["timestamp"],
                reference_close=ref_close,
                market_close=mkt_close,
                reference_return_pct=ref_ret,
                market_return_pct=mkt_ret,
                gap_pct=mkt_ret - ref_ret,
            )
        )
    return points


def gap_points_to_frame(points: Iterable[GapPoint]) -> pd.DataFrame:
    return pd.DataFrame([p.__dict__ for p in points])
