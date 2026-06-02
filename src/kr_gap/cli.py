from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from .align import calculate_gap_points, gap_points_to_frame
from .models import Candle


def _sample_reference() -> list[Candle]:
    return [
        Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 100, 101, 99, 100),
        Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 100, 103, 100, 102),
        Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 102, 104, 101, 103),
    ]


def _sample_market() -> list[Candle]:
    return [
        Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 50, 51, 49, 50),
        Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 50, 54, 50, 53),
        Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 53, 56, 52, 55),
    ]


def sample_command(out: str) -> None:
    points = calculate_gap_points(_sample_reference(), _sample_market())
    frame = gap_points_to_frame(points)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(out, index=False)
    print(f"Wrote {len(frame)} rows to {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Korean equity-linked perp gap monitor")
    sub = parser.add_subparsers(dest="command", required=True)

    sample = sub.add_parser("sample", help="write a sample gap-analysis CSV")
    sample.add_argument("--out", default="sample_gap.csv")

    args = parser.parse_args()
    if args.command == "sample":
        sample_command(args.out)


if __name__ == "__main__":
    main()
