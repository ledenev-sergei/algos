import pytest

from dynamic.stock_maximize import stockmax


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([1, 2], 1),
        ([2, 1], 0),
        ([5, 3, 2], 0),
        ([1, 2, 100], 197),
        ([1, 3, 1, 2], 3)
    ],
)
def test_stockmax(prices, expected):
    # given
    # when
    result = stockmax(prices)
    # then
    assert result == expected