import pytest

from kr_gap.metrics import max_drawdown, pct_return, premium_pct, return_spread_pct


def test_pct_return():
    assert pct_return(110, 100) == pytest.approx(10.0)
    assert pct_return(90, 100) == pytest.approx(-10.0)


def test_premium_pct():
    assert premium_pct(105, 100) == pytest.approx(5.0)


def test_return_spread_pct():
    assert return_spread_pct(110, 100, 105, 100) == pytest.approx(5.0)


def test_max_drawdown():
    assert max_drawdown([100, 120, 90, 130]) == pytest.approx(-25.0)
