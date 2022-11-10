import pytest

from dynamic import online_stock_span


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
    ],
)
def test_find_target_sum_ways(prices, expected):
    # given
    solution = online_stock_span.StockSpanner()
    # when
    result = [solution.next(p) for p in prices]
    # then
    assert result == expected
