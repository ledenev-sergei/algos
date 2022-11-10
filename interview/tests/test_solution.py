from random import randint
from typing import List

import pytest

from interview.solution import getMaxProfit


@pytest.mark.parametrize(
    "pnl, k, expected",
    [
        ([-3, 4, 3, -2, 2, 5], 4, 8),
        ([4, 3, -2, 9, -9, 2, 7, 6], 6, 15),
        ([2, 5, -7, 8, -6, 4, 1, -9], 5, 8),
        ([4, 3, -2, 9, -4, 2, 7], 6, 15),
        ([-7, -5, -8, -6, -7], 3, 0),
        ([3], 1, 3),
        ([randint(-10, 10) for _ in range(1000000)], 30, 0)
    ],
)
def test_max_subset_sum(pnl, k, expected: None):
    # given
    # when
    result = getMaxProfit(pnl, k)
    # then
    assert result == expected
