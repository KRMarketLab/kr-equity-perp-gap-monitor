from datetime import datetime, timezone

from kr_gap.align import calculate_gap_points
from kr_gap.models import Candle


def test_calculate_gap_points():
    t0 = datetime(2026, 1, 1, 0, tzinfo=timezone.utc)
    t1 = datetime(2026, 1, 1, 1, tzinfo=timezone.utc)

    reference = [
        Candle(t0, 100, 100, 100, 100),
        Candle(t1, 100, 105, 100, 105),
    ]
    market = [
        Candle(t0, 50, 50, 50, 50),
        Candle(t1, 50, 55, 50, 55),
    ]

    points = calculate_gap_points(reference, market)
    assert len(points) == 2
    assert points[-1].reference_return_pct == 5.0
    assert points[-1].market_return_pct == 10.0
    assert points[-1].gap_pct == 5.0
