from typing import List

import pytest

from sorting.mark_and_toys import maximumToys


@pytest.mark.parametrize(
    "prices,budget,expected",
    [
        ([1, 12, 5, 111, 200, 1000, 10], 50, 4),
    ],
)
def test_maximum_toys(prices: List[int], budget: int, expected: int):
    # given

    # when
    result = maximumToys(prices, budget)

    # then
    assert result == expected
